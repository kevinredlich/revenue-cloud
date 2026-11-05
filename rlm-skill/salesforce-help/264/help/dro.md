# Salesforce Help 264 — área: dro (96 artículos)

=== ARTICLE: ind.dro_add_a_fulfillment_user.htm ===
---
article_id: ind.dro_add_a_fulfillment_user.htm
title: Create Fulfillment Users for Order Orchestration
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_add_a_fulfillment_user.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_permissions_in_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Create Fulfillment Users for Order Orchestration

During fulfillment, Dynamic Revenue Orchestrator (DRO) uses the permissions associated with the fulfillment user rather than those of the user who submits an order. You can specify a different user for certain orchestration tasks, but generally, the permissions default to the fulfillment user. Select the fulfillment user from the Dynamic Revenue Orchestrator Settings pane.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To add a fulfillment user:	DRO Admin
From Setup, in the Quick Find box, enter Dynamic Revenue Orchestrator Settings and select it.
Choose one of these options:
User who submitted the order: The permissions and name of the user who submitted the order are used for fulfillment processes.
Other User: Search for and select a user whose permissions and name are used for fulfillment processes.
IMPORTANT The fulfillment user must have the Assetize Order permission from the Revenue Lifecycle Management permission sets and either Submit Transaction User or DRO Admin User permissions.

The fulfillment user is set. You don't need to save your work.

SEE ALSO
Fulfillment User
Permission Sets in Dynamic Revenue Orchestrator

=== ARTICLE: ind.dro_advanced_setup.htm ===
---
article_id: ind.dro_advanced_setup.htm
title: Dynamic Revenue Orchestrator Advanced Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_advanced_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Dynamic Revenue Orchestrator Advanced Setup

Dynamic Revenue Orchestrator provides advanced setup options to customize and extend its core functionalities that is crucial for leveraging the product's full power and tailoring it to specific business needs.

SEE ALSO
Dynamic Revenue Orchestrator Basic Setup

=== ARTICLE: ind.dro_assetization_in_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_assetization_in_dynamic_revenue_orchestrator.htm
title: Fulfillment Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_assetization_in_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Fulfillment Assets

After an order is fulfilled, order line items and fulfillment order line items are converted to Salesforce assets.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Order line items are the items that customers order, such as phone or internet service. Fulfillment order line items are the products that order line items decompose into, such as a SIM card or a network interface controller. Upon fulfillment, both order line items and fulfillment order line items become assets.

Assets are created from order line items. View them on the Assets tab of the relevant Account page.
Fulfillment assets are created from fulfillment order line items. View them in the Fulfillment Asset section of the Related tab on the relevant Account page. If the Fulfillment Asset section doesn't appear, edit the layout for that page.

Dynamic Revenue Orchestrator reconciles fulfillment assets every 24 hours. It adjusts the quantity and validity of fulfillment assets based on the quantities of related assets and the asset state periods. If a technical product that is related to a fulfillment asset has fulfillment quantity calculation method set to Always one, the quantity field in the fulfillment asset is always one, regardless of the related asset quantities. If the calculation method is set to Aggregate, the quantity field in the fulfillment asset is the sum of the related asset quantities.

=== ARTICLE: ind.dro_assetization_rules_for_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_assetization_rules_for_dynamic_revenue_orchestrator.htm
title: Assetization Rules for Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_assetization_rules_for_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.qocal_order_submission_for_fulfillment.htm
fetched_at: 2026-09-05
---

# Assetization Rules for Dynamic Revenue Orchestrator

Use Asset Lifecycle Management to create and activate multiple asset-based orders (ABOs) for the same asset across different sales transactions or orders. Maintaining precise assetization rules makes sure that the system applies changes sequentially and prevents data conflicts during the fulfillment process.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Fulfillment Integrity and Asset Changes

Run an invocable action or Apex and add it to the order submit flow to apply exactly one change to an asset at a time. This sequential processing avoids failures during the fulfillment process. When an order item or order action applies to an asset after the invocable action runs, the system prevents the assetization of previously created order items for that asset due to outdated data.

Asset Verification Details

Load the quote line items or order line items to determine the creation date for each asset related to an order line item. Verify these specific details for each quote line item or order line item.

Determine if the created date of the quote line item or order item matches the created date of the most recent asset action.
Determine if the created date of the asset action is more recent than the created date of the quote line item or order item.

=== ARTICLE: ind.dro_associate_custom_context_definition_with_sales_transaction_attribute.htm ===
---
article_id: ind.dro_associate_custom_context_definition_with_sales_transaction_attribute.htm
title: Map Custom Context Definition with Sales Transaction
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_associate_custom_context_definition_with_sales_transaction_attribute.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_steps_to_create_a_custom_context_definition.htm
fetched_at: 2026-09-05
---

# Map Custom Context Definition with Sales Transaction

To start using a context definition, you must associate the context definition's newly created attribute with the context field in the sales transaction node.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To associate an attribute with a context field:	

DRO Admin User

Prerequisite: Create Custom Context Definition and Map Attribute to Field.

From Setup, in the Quick Find box, enter Context Definition Settings and select it.
From the Sales Transaction Context Definition header, select the newly created context definition.
From the context nodes list, select the SalesTransaction node, and then map the Context field for the Orchestration Group Key field node to the attribute that you created when you defined the context definition. Map other nodes from the custom context definition to the SalesTransaction nodes as required.

After the setup is complete, you can create and process orders by using the new context definition. The orders must contain the grouping key in the field that you mapped to the Orchestration Group Key. For more information on Orchestration Group Keys, see Cross-Plan Dependencies.

=== ARTICLE: ind.dro_basic_set_up.htm ===
---
article_id: ind.dro_basic_set_up.htm
title: Dynamic Revenue Orchestrator Basic Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_basic_set_up.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Dynamic Revenue Orchestrator Basic Setup

Dynamic Revenue Orchestrator (DRO) helps seamlessly design and manage the order fulfillment process. It allows you to break down orders into actionable components and track and act on the fulfillment of these components. The basic setup steps help to get started with using DRO.

SEE ALSO
Submit Sales Transactions for Orchestration

=== ARTICLE: ind.dro_clone_a_fulfillment_workspace.htm ===
---
article_id: ind.dro_clone_a_fulfillment_workspace.htm
title: Clone a Fulfillment Workspace
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_clone_a_fulfillment_workspace.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_define_orchestration_components.htm
fetched_at: 2026-09-05
---

# Clone a Fulfillment Workspace

Copy a fulfillment workspace and its supported design-time records to create a starting point for a new orchestration design. Changes to the cloned workspace don’t affect the source workspace.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To clone a fulfillment workspace:	DRO Admin

When you deep clone a fulfillment workspace with the preconfigured context definition FulfillmentWorkspaceDeepCloneContext, it copies the fulfillment workspace, workspace items, step definition groups, step definitions, and step dependency definitions. To include supported custom fields or objects, configure a context definition that extends FulfillmentWorkspaceDeepCloneContext. Optionally, you can also configure an expression set to transform field values during cloning. See Configure Deep Cloning for Fulfillment Workspaces.

Before you clone a fulfillment workspace, review these considerations.

Records outside the workspace aren't cloned, such as flows, queues, users, integration definitions, OmniScripts, and expression sets. The cloned records continue to reference the external records.
Execute On and Resume On rulesets aren't copied. They're not included in the cloned workspace.
You can clone a maximum of 500 records, including records in the source workspace and records created in the cloned workspace.
From the App Launcher, find and select Dynamic Revenue Orchestrator.
From the app navigation menu, find and select Fulfillment Workspaces.
Open the fulfillment workspace that you want to clone.
From the action menu, select Deep Clone.
Enter a unique name for the cloned workspace, and then click Deep Clone.
The workspace name is prefilled with the source workspace name and a prefix.

The Deep Clone Fulfillment Workspace window confirms that cloning succeeded and lists the copied object types and record counts.

To continue designing the cloned workspace, click View Cloned Fulfillment Workspace.

=== ARTICLE: ind.dro_comptibility_for_field_and_attributes_mapping.htm ===
---
article_id: ind.dro_comptibility_for_field_and_attributes_mapping.htm
title: Data Type Compatibility for Field and Attribute Mapping
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_comptibility_for_field_and_attributes_mapping.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_define_field_and_attribute_mapping.htm
fetched_at: 2026-09-05
---

# Data Type Compatibility for Field and Attribute Mapping

When you map a source attribute or field to a target attribute or tag, Dynamic Revenue Orchestrator (DRO) validates that the source and target data types are compatible. If they aren't compatible, the mapping can't be created.

REQUIRED EDITIONS
Available in: Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions

This table lists the supported target data types for each source data type.

Supported Source-to-Target Data Type Mappings
SOURCE DATA TYPE	SUPPORTED TARGET DATA TYPES
String (Context Tag)	String, Text
Text (Product Attribute)	String, Text
Date/Time	Date/Time, Date, String, Text
Date	Date, datetime, String, Text
Boolean (Context Tag)	Boolean, Checkbox, String, Text
Checkbox (Product Attribute)	Boolean, Checkbox, String, Text
Picklist	Picklist, String, Text
Currency	Currency, String, Text, Number
Number	Number, String, Text, Currency
Percent	Percent, String, Text
A context tag's String corresponds to a product attribute's Text datatype, and a context tag's Boolean corresponds to a product attribute's Checkbox. You can map between these equivalent types.
Any data type that isn't listed in the table can map only to the same data type, or to String or Text.
SEE ALSO
Define Field and Attribute Mapping

=== ARTICLE: ind.dro_conditions_in_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_conditions_in_dynamic_revenue_orchestrator.htm
title: Understand Execution Conditions for Order Fulfillment
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_conditions_in_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Understand Execution Conditions for Order Fulfillment

When you configure fulfillment plans, Dynamic Revenue Orchestrator directs you to create conditions that control when those fulfillment steps are executed.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

For example, set a condition so that a representative follows up by phone only if the customer lives in the same country. Or a condition that says that after a pause, fulfillment doesn’t continue until a credit check comes through.

When an entity in DRO requires, or allows, conditions to be set, it launches the Condition Builder pane.

To configure logic for your fulfillment processes, use the Condition Builder. To set up these rules, seeDefine Execution Rules for a Decomposition Rule

EXAMPLE This image shows three conditions.
Condition #1: There's a fulfillment order line item tag called FulfillmentItemAction that equals Add.
Condition #2: There's a tag called OriginalQuantity that's greater than 100.
Condition #3: There's a tag called FulfillmentOrderID that doesn't equal 1221.

The Custom Condition Logic says (1 OR 2) AND 3. That means that condition #3 must be met, and that either condition #1 or #2, or both, must be met.

Let's look at some possible examples after an order is submitted.

Order #1:

FulfillmentItemAction equals Add. Condition one is met.
OriginalQuantity equals 150. Condition two is met.
FulfillmentOrderID is 1221. Condition three isn't met. The condition requires that FulfillmentOrderID type is something other than 1221.

Because condition #3 isn't met, the set of conditions isn't met, and the entity associated with this rule doesn't run.

Order #2:
FulfillmentItemAction tag equals Add. Condition one is met.
OriginalQuantity equals 90. Condition two isn't met. The condition requires the value to be greater than 100.
FulfillmentOrderID is 1000. Condition three is met. The condition requires the value type to be anything except 1221, and it is.

This set of conditions is met according to the custom logic and the entity associated with this rule runs.

=== ARTICLE: ind.dro_configure_dynamic_revenue_orchestrator_analytics_dashboards.htm ===
---
article_id: ind.dro_configure_dynamic_revenue_orchestrator_analytics_dashboards.htm
title: Configure Dynamic Revenue Orchestrator Analytics Dashboards
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_dynamic_revenue_orchestrator_analytics_dashboards.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_enable_analytics.htm
fetched_at: 2026-09-05
---

# Configure Dynamic Revenue Orchestrator Analytics Dashboards

Add the delivered Order Analysis and Order Details dashboards to your home page and order record page, respectively. Use filters to further refine the details to be displayed on charts and graphs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
USER PERMISSIONS NEEDED
For fulfillment manager to configure dashboards:	

Tableau Next Consumer

AND

Data Cloud User


For admin to configure dashboards:	

Tableau Next User

AND

Data Cloud Admin

From the App Launcher, find and select Dynamic Revenue Orchestrator.
On the Dynamic Revenue Orchestrator Home page, select the Edit Page option from the Setup menu.
From the Standard components in the left panel, drag and drop the Tableau Next Dashboard into your home page layout.
From the Dashboard field, select Order Analysis.
Click the Add Filter button and define the filter using the Select Data Model and Field settings.
Save your changes and activate the dashboard.
Similarly, you can apply the Order Details dashboard to your Order Record details page layout and configure the filters.

=== ARTICLE: ind.dro_configure_es_mapping.htm ===
---
article_id: ind.dro_configure_es_mapping.htm
title: Configure Expression Set Based Mapping
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_es_mapping.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_define_field_and_attribute_mapping.htm
fetched_at: 2026-09-05
---

# Configure Expression Set Based Mapping

Use expression sets to perform complex transformations on the source product's fields and attributes and use the output variables of the expression sets to enrich the target product's fields and attributes. For example, set delivery priority in the target product based on the order value and the delivery zipcode.

REQUIRED EDITIONS
Available in: Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To configure an expression set based mapping:	

Fulfillment Designer

OR

DRO Admin

Consider these recommendations for expresssion set mapping.

Reuse expression sets for multiple mappings: To reduce performance impact during order submission, implement multiple transformations in a single expression set and reuse for multiple mappings.
Simulate expression sets before use: To validate the expected output and achieve accurate data transformation during fulfillment, simulate the expression set in Business Rules Engine's Expression Builder with sample data before using it in mapping. See Simulate and Activate Your Expression Set Version.

Before you begin, review the initial mapping set up steps in Define Field and Attribute Mapping.

Create a Field & Attribute Mapping within a Decomposition Rule.
For Mapping Type, select Expression Set Based Mapping.
Select the expression set.
To view or edit the expression set in Business Rules Engine's Expression Builder, click Source.
In the Input Variables section, map at least one input variable of the expression set to a source field or attribute.
In the Output Variables section, map one output variable of the expression set to a target field or attribute.
Save your work.
EXAMPLE

Consider a source commercial product that has attributes ProductType, CustomerAccount, and Price.

The target technical product has a Commission Amount attribute.

An expression set, CommissionCalculation is designed to calculate the commission amount by taking in ProductType, CustomerAccount, and Price as inputs variables.

Configure the mapping from the source to the target mapping by using the CommissionCalculation expression set. Map the input variables of the expression set to the source product attributes ProductType, CustomerAccount, and Price. Map the output variable of the expression set to the Commission Amount attribute of the target product.

When a user submits an order with ProductType as Advanced, CustomerAccount as Priority, and Price as $12000, the target product is set with Commission Amount as $1000.

When the user submits an order with ProductType as Basic, CustomerAccount as Regular, and Price as $1200, the target product is set with Commission Amount as $100.

=== ARTICLE: ind.dro_configure_fallout_rules.htm ===
---
article_id: ind.dro_configure_fallout_rules.htm
title: Configure Fallout Rules
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_fallout_rules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_fallout_administration.htm
fetched_at: 2026-09-05
---

# Configure Fallout Rules

Configure rules for how Dynamic Revenue Orchestrator (DRO) handles callouts and auto tasks that fail. Specify how often they're retried, at what intervals, and which queue they go to if they fatally fail.

REQUIRED EDITIONS

.

Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To configure Fallout:	System Administrator Profile

To configure fallout rules:

From Setup, in the Quick Find box, enter Fallout and SLA Settings, and select it.
In the Fallout section, turn on the fallout settings, then click Configure.
Click New.
If necessary, enter the integration definition that the callout uses to integrate with the external system.
If you leave the Integration Definition field blank, then the rule applies to all callouts or auto tasks that don't use more specific rules.
For auto tasks, add a flow definition name.
To set up retries, enter the retry policy, the retry intervals, and the retries allowed.
See: Configure Fulfillment Step Retries.
Enter the queue where fatally failed steps are assigned.
The queue must have fulfillment steps as supported objects. From that queue, you can bulk retry or bulk complete the steps.
If necessary, enter the error expected from the external system.
If you leave the Error Code field blank, then the rule applies to all callouts or auto tasks that don't use more specific rules.
IMPORTANT If you're changing the rules after previously saving them, you must refresh the Fulfillment Fallout Rules decision table to implement the new rules.
SEE ALSO
Create an Integration Definition
Refresh a Decision Table

=== ARTICLE: ind.dro_configure_fulfillment_step_jeopardy_rules.htm ===
---
article_id: ind.dro_configure_fulfillment_step_jeopardy_rules.htm
title: Configure Fulfillment Step Jeopardy Rules
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_fulfillment_step_jeopardy_rules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_sla_jeopardy_administration.htm
fetched_at: 2026-09-05
---

# Configure Fulfillment Step Jeopardy Rules

Configure the rules that determine when a fulfillment step is considered to be in jeopardy, and when it's considered late.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To configure fulfillment step jeopardy rules:	System Administrator profile
From Setup, in the Quick Find box, enter Fallout and SLA Settings and select it.
In the Service Level Agreement section, click Configure.
Click New.
In the Estimated Duration and Estimated Duration Unit fields, enter the time that you expect the step to take.
In the Jeopardy Threshold and Jeopardy Threshold Unit fields, enter the amount of time before the estimated duration is complete that the step is in jeopardy of running late. For example, if the estimated duration is ten minutes and you enter two minutes as the jeopardy threshold, the step is in jeopardy after running for eight minutes.
NOTE Because the jeopardy threshold counts back from the estimated duration, make sure that the jeopardy threshold is less than the estimated duration.
Optional: To specify callouts that the rule applies to, enter an integration definition in the Integration Definition field. If you leave the Integration Definition field blank, then the rule applies to all callouts.
Optional: To specify manual tasks or auto tasks that the rule applies to, enter a flow definition in the Flow Definition field. If you leave the Flow Definition field blank, then the rule applies to all manual tasks and auto tasks.
Save your work.
EXAMPLE

Let's say there's a manual task to check the credit of a customer. You set the Estimated Duration to 3 hours. Then you set the Jeopardy Threshold to 30 minutes. If the step isn’t completed within 2.5 hours after it starts, the task is considered in jeopardy.

To see the status of the fulfillment step, check the orchestration plan for the order. To learn more about monitoring your orchestration plans, see Monitor Fulfillment During Order Orchestration.
IMPORTANT If you edit an existing fulfillment step jeopardy rule, you must refresh the Fulfillment Step Jeopardy Rule Entries decision table for the changes to take effect.
SEE ALSO
Create an Integration Definition
Refresh a Decision Table

=== ARTICLE: ind.dro_configure_fulfillment_step_retries.htm ===
---
article_id: ind.dro_configure_fulfillment_step_retries.htm
title: Configure Fulfillment Step Retries
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_fulfillment_step_retries.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_fallout_administration.htm
fetched_at: 2026-09-05
---

# Configure Fulfillment Step Retries

Specify the number of times a failed fulfillment step tries again after failing, and how long it waits before each retry. You can even stagger the time between retries, so that, for example, it retries right away, then again in five minutes, and again in 20 minutes.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To configure fulfillment step retries:	System Administrator Profile

When steps such as callouts and auto tasks fail because a system is down, it wastes resources to immediately try again only to fail again. Fulfillment designers can schedule steps to wait before retrying. For example, they can schedule a retry every five minutes, or stagger the retries so that each retry waits longer than the one before it.

From Setup, in the Quick Find box, enter Fallout and SLA Settings, and select it.
In the Fallout section, click Configure.
Do one of these things:
To create a rule, click New.
To edit a rule that you've already created, create a list view to see the rules, then click the rule that you want to edit.
From Retry Policy, select the retry policy for the fulfillment process to follow when a step fails.
Immediate: The step immediately tries again, up to the number of times specified in the Retries Allowed field.
Monotonous: The step tries again at the intervals set in the Retry Intervals field, up to the number of times specified in the Retries Allowed field.
Staggered: The step tries again at the intervals set in the Retry Intervals field. It retries once for each interval that's specified. For example, if you set 10,15,40, then the step retries after 10 minutes, again after another 15 minutes, and then after another 40 minutes before moving to the Fatally Failed state.
In Retries Allowed, enter the number of times that the step retries before either succeeding or moving to the Fatally Failed state.
Leave this field blank for the Staggered policy.
In Retry Intervals, enter the time in minutes to wait before the step retries after failing.
Leave this field blank for the Immediate policy.

=== ARTICLE: ind.dro_configure_fulfillment_workspace_deep_cloning.htm ===
---
article_id: ind.dro_configure_fulfillment_workspace_deep_cloning.htm
title: Configure Deep Cloning for Fulfillment Workspaces
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_fulfillment_workspace_deep_cloning.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Configure Deep Cloning for Fulfillment Workspaces

Deep cloning uses the preconfigured context definition FulfillmentWorkspaceDeepCloneContext by default. Configure deep clone settings to include supported custom fields or objects, or to transform field values during cloning.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To configure deep cloning for fulfillment workspaces:	DRO Admin

Turn on Context Definitions to load the FulfillmentWorkspaceDeepCloneContext context definition. For more information, see Turn On Context Definitions.

By default, deep cloning uses this preconfigured FulfillmentWorkspaceDeepCloneContext context definition to copy the fulfillment workspace, workspace items, step definition groups, step definitions, and step dependency definitions. This configuration is optional. Configure deep cloning only when you want to:

Extend the context definition to include supported custom fields or objects. Create a context definition that extends FulfillmentWorkspaceDeepCloneContext, and then select it for deep cloning.
Select an expression set when you want to transform field values in the cloned records.
From Setup, in the Quick Find box, enter and then select Dynamic Revenue Orchestrator Settings.
Select Deep Clone Settings.
For Fulfillment Workspace Context Definition, select a context definition.
To copy the standard supported records, select FulfillmentWorkspaceDeepCloneContext.
To also copy supported custom fields or objects, select a context definition that extends FulfillmentWorkspaceDeepCloneContext.
Optional: To transform field values in the cloned records, select an expression set for Fulfillment Workspace Expression Set.
For example, use an expression set to append text to cloned record names or assign a different value to a custom field.

The selected context definition and expression set apply to all subsequent fulfillment workspace deep clones.

SEE ALSO
Clone a Fulfillment Workspace
Extend a Context Definition

=== ARTICLE: ind.dro_configure_inflight_plan_settings.htm ===
---
article_id: ind.dro_configure_inflight_plan_settings.htm
title: Configure Inflight Plan Settings for a Fulfillment Step
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_inflight_plan_settings.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_in_flight_order_changes.htm
fetched_at: 2026-09-05
---

# Configure Inflight Plan Settings for a Fulfillment Step

As part of creating fulfillment steps, you can configure inflight plan settings to handle customer requests to add, amend, cancel, or otherwise change their order before the order is committed by a sales rep.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To configure inflight plan settings:	

Fulfillment Designer

OR

DRO Admin User

To configure inflight plan settings, first create a fulfillment step using the fulfillment workspace. For more information, see Define Orchestration Plan Components.

Select an Amend Step Group.
Select a Cancel Step Group.
To apply the cancel step groups in reverse order of execution, see Set Dependencies Between Fulfillment Steps.
Configure the Point of No Return behavior. In the Available pane, select the type of source change (Changes Denied) to be applied to the line item, then click  to move the source change to the Chosen field. This selection ensures that when the fulfillment plan reaches this step, no changes to the order items in the bundle are allowed.
Optional: Force Plan Freeze During Execution. Select an option other than the default option to allow order representatives to forcefully freeze the plan. Specify how to complete the step before resuming the plan. Choose an action to apply to the In Progress step:
Never: The plan freezes only after the step is completed. Until then, the plan is in a Freezing state. This is the default option.
Yes But Forcefully Complete the Step: Moves the plan to a Frozen state, forcefully completes the step, and then resumes the plan if the related line item is amended or canceled.
Save your work.

=== ARTICLE: ind.dro_configure_list_mapping.htm ===
---
article_id: ind.dro_configure_list_mapping.htm
title: Configure List Mapping
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_list_mapping.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_define_field_and_attribute_mapping.htm
fetched_at: 2026-09-05
---

# Configure List Mapping

Use list mapping to set up pairs of source and destination values. For example, a list of cities that pair with post code values. When the source value is a city name, the target receives the post code of that city. Configure list mapping from the Fields & Attribute Mapping section of a decomposition rule.

REQUIRED EDITIONS
Available in: Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To configure a list mapping:	

Fulfillment Designer

OR

DRO Admin

Before you begin, review the initial mapping set up steps in Define Field and Attribute Mapping.

Create a Field & Attribute Mapping within a Decomposition Rule.
For Mapping Type, select List Mapping.
Select New List.
You can also use an existing list.
NOTE If you use an existing list, then any change you make for this mapping affects all other mappings that use the same list.
Name the list and click Add Row.
In the source product column, click  and enter a value that you expect to be in the source product.
NOTE Boolean attribute types don't work with list mapping.
Add more rows as required. Don't add duplicate source values to a list.
Save your work.
EXAMPLE

A source commercial product has the attribute Speed with two values: Fast and Ultra Fast.

The target technical product has a Bandwidth attribute with two values: 50 Mbps and 100 Mbps.

Create a mapping so that if the source product has a Speed value of Fast, then the target product has a Bandwidth value of 50 Mbps. And if the Speed is Ultra Fast, then the Bandwidth is 100 Mbps.

When a user submits an order with a speed attribute of Fast, the Broadband attribute gets the value of 50 Mbps.

=== ARTICLE: ind.dro_configure_procedure_plan_definition_for_business_process_orchestration.htm ===
---
article_id: ind.dro_configure_procedure_plan_definition_for_business_process_orchestration.htm
title: Configure Procedure Plan Definition for Business Process Orchestration
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_procedure_plan_definition_for_business_process_orchestration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_orchestrate_sales_transaction_business_processes.htm
fetched_at: 2026-09-05
---

# Configure Procedure Plan Definition for Business Process Orchestration

Use the procedure plan definition to determine the correct context definition and mapping, and orchestrate the business process to create a sales transaction fulfillment request.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
USER PERMISSIONS NEEDED
To create, update, and activate procedure plan definitions:	

Procedure Plan Access

AND

DRO Design Time User

Before you begin, extend the Sales Transaction context definition, map your entity to the new context definition, and activate the context definition. See Create Custom Context Definition and Map Business Objects.

TIP To orchestrate custom business objects, first create custom primary objects to define the process rules for each business process entity that you want to orchestrate. See Create a Custom Object.
Create a custom procedure plan definition.
From Setup, in the Quick Find box, enter Procedure Plan Definitions, and then select it.
Create a procedure plan definition by entering a title and a developer name.
Select DRO as the process type.
Select the object that you want to submit for orchestration as the primary object.
For example, Service Request or Case.
Select the custom context definition that you created from the Sales Transaction context definition.
Save your work.
Update and activate the procedure plan definition.
Open the procedure plan definition.
Select a value for the read context mapping.
Select the same value for the save context mapping.
NOTE The procedure plan definition doesn’t write any information to your object.
Save the plan definition.
Activate the procedure plan definition.

=== ARTICLE: ind.dro_configure_scenarios_for_a_fulfillment_step_definition_group.htm ===
---
article_id: ind.dro_configure_scenarios_for_a_fulfillment_step_definition_group.htm
title: Configure a Fulfillment Scenario
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_scenarios_for_a_fulfillment_step_definition_group.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# Configure a Fulfillment Scenario

Use a fulfillment scenario to define when Dynamic Revenue Orchestrator (DRO) adds a fulfillment step definition group to a fulfillment plan after an order is submitted. Fulfillment scenarios help you add common fulfillment steps automatically instead of creating the steps for each order.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
USER PERMISSIONS
NEEDED
To set conditions for fulfillment step groups:	

Fulfillment Designer

OR

DRO Admin User

Create scenarios for a specific product, a product classification, or an entire order.

A product-based scenario applies to a specific product.
A product classification-based scenario applies to products in a selected product classification.
An order-based scenario applies to the entire order, regardless of its products.
Fulfillment Scenario Types
CHARACTERISTIC	PRODUCT-BASED SCENARIO	PRODUCT CLASSIFICATION-BASED SCENARIO	ORDER-BASED SCENARIO
Configuration	Select a product.	Select a product classification.	Leave Product and Product Classification blank, and set Dependency Scope to Plan.
Applies To	An order that contains the selected product.	An order that contains a product in the selected product classification.	The entire order, regardless of its products.
Execution Rule Fields	Supports product attributes, order line item fields, and order-level fields.	Supports product attributes, order line item fields, and order-level fields.	Supports only order-level fields. Product-specific and order line item fields aren't available.
Changes After Order Submission	Supported. You can modify steps after the order is submitted.	Supported. You can modify steps after the order is submitted.	Not supported. You can't modify steps after the order is submitted.
Example Usecases	Specialized handling or delivery for a specific product. =	Warehouse processing or other common requirements for a group of products. =	Credit checks, approval workflows, and regional requirements for the entire order.

For example, you have a laptop bundle and fetching the laptop from the warehouse is a common fulfillment step. For this situation, define a fulfillment scenario with the condition that when the laptop bundle is added to an order, DRO adds a step to fetch the laptop from the warehouse.

From the App Launcher, find and select Fulfillment Workspaces.
Select a fulfillment step definition group.
In the Details panel, select Related.
Under Scenarios, click New.
Name the scenario.
Enter the name of the relevant fulfillment step definition group.
Select a product or a product classification the scenario applies to.
To apply the scenario to the entire order regardless of the products, leave the Product and Product Classification fields blank and set the dependency scope to Plan.
Select a Usage Type.
From the Available list, move the actions that trigger adding the group to a fulfillment plan to the Chosen list.
Save your work.
To save the scenario and see the details pane for the scenario, click Save.
To save the scenario and then define when the scenario runs during fulfillment, click Save & Configure Execution Rules.
NOTE To view the details and related scenarios for the step definition group, click the group and check the side panel. You can create a scenario from the side panel.
If you configure a fulfillment scenario between a product class and a step group, and then another scenario between a product belonging to the product class and the same step group, then the scenario configured for the product is applied during plan generation.
Define appropriate conditions to resolve the scenarios when multiple product-based or order-based fulfillment scenarios exist for an order.
EXAMPLE

Let’s say you create two products called HiTech ServerDrive and HiTech ServerDrive - Express under the classification Enterprise Server Components. To pull the units from the warehouse, you create a fulfillment step definition group called Standard Warehouse Processing.

Next, create a fulfillment scenario. Specify that the chosen action is Add, select the Standard Warehouse Processing step definition group, and select the Enterprise Server Components product classification.

Then, create another fulfillment scenario specifically for the HiTech ServerDrive - Express product and use the Express Delivery step group.

When HiTech ServerDrive is added to an order and the order is submitted, the Standard Warehouse Processing step definition group is added to the fulfillment plan. However, when HiTech ServerDrive - Express is added to the order, DRO recognizes the specific Express Delivery scenario defined for the product and uses the Express Delivery step group instead of the Standard Warehouse Processing step group from the product class.

This product-specific fulfillment scenario overrides the more general, class-based scenario, which helps HiTech to handle exceptions or special cases in their fulfillment process.

Define Conditions for a Product Fulfillment Scenario
After you've created a product fulfillment scenario, you can define conditions to determine whether the scenario is used during fulfillment.

=== ARTICLE: ind.dro_configure_steps_for_future_execution.htm ===
---
article_id: ind.dro_configure_steps_for_future_execution.htm
title: Configure Steps for Future Execution
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_configure_steps_for_future_execution.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# Configure Steps for Future Execution

Fulfillment designers can configure the steps to be executed at a future date and time. They can set a delay for the execution of steps based on the start date of the source line item, the execution time of the previous steps, or a custom date based on a context definition field.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To configure the steps:	

Fulfillment Designer

OR

DRO Admin

NOTE To schedule steps , enable Future-Dated Steps on the Dynamic Revenue Orchestrator Settings page. If this feature isn’t enabled, the Execution Schedule section doesn’t appear on the Fulfillment Definition Steps page.
Create a workspace or select a workspace from the Recently Viewed section.
Create the Fulfillment Step Group, add a step, and enter the details.
See Define Orchestration Plan Components.
To edit a step, select Edit from the dropdown.
Select the execution schedule
	
Source Line Start Date	To schedule the execution based on the start date of the source.
Previous Steps Execution Date	To schedule the execution based on the execution date of the previous steps.
Custom Date	To schedule the execution based on a custom date defined in the associated context definition.
To set a delay depending on the specified execution schedule, select the delay unit, and enter a positive number as the delay value.
Save your work.
View Step Status and Details
After you submit the order to DRO, go to Fulfillment Lines and select View Fulfillment Plan to view the step status, details, and dependencies.
Configure Context Definition Fields for Future Dated Fulfillment Steps
You can configure the execution of steps in your orchestration plan based on custom dates that correspond to date or datetime tags in context definition.
Use Custom Dates To Schedule Fulfillment Steps
Configure the execution of steps in your orchestration plan based on custom dates that correspond to date or datetime tags in context definition. For example, you can map a custom context tag to a custom field to activate a service on a date requested by the customer.

=== ARTICLE: ind.dro_considerations_for_backdated_changes_in_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_considerations_for_backdated_changes_in_dynamic_revenue_orchestrator.htm
title: Considerations for Backdated Changes in Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_considerations_for_backdated_changes_in_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_time_aware_fulfillment.htm
fetched_at: 2026-09-05
---

# Considerations for Backdated Changes in Dynamic Revenue Orchestrator

Review how Dynamic Revenue Orchestrator (DRO) decomposes and orchestrates backdated amend, renew, and cancel orders and rolls back amend and renew orders. Understand the behavior and constraints when time-awareness isn't turned on.

Backdated Amend, Renew, and Cancel Orders

A backdated order captures a change to an asset that's effective from a past date. When you submit a backdated amend, renew, or cancel order to DRO, DRO updates the Fulfillment Asset (FA) and orchestrates the change. Review these behaviors.

Decomposition and plan composition for a backdated order are the same as for an order that's effective today. DRO decomposes the order line items, determines the action for each Fulfillment Order Line Item (FOLI), and composes an orchestration plan.
Orchestration steps run no sooner than today. A step that's based on a past effective date runs as soon as it's in progress, and DRO doesn't flag the step as in jeopardy.
For a backdated cancel order, a line item-scoped FA is canceled on the effective date. An account-scoped FA is canceled on the effective date only when no related asset is active on that date.
For a backdated renewal order, DRO reactivates an FA whose related asset expired. To reactivate an expired asset, submit a renewal order that extends the asset's term.

To submit a backdated amend, renew, or cancel order, see Backdate Asset Transactions. For the requirements and limitations that apply to backdated changes, see Considerations for Assets with Backdated Changes.

Behavior When Time-Awareness Isn't Turned On

With time-awareness, DRO evaluates the past, current, and future state of an FA when it determines fulfillment actions. When time-awareness isn't turned on, FAs are time-agnostic and DRO determines fulfillment actions from the current state of the FA only.

Without time-awareness, a backdated or future-dated change can result in an incorrect action for a fulfillment line. For example, DRO can determine an Add action instead of an Amend action, or a No Change action instead of a Cancel action.
To decompose and orchestrate backdated amend, renew, and cancel orders correctly, turn on time-awareness. See Turn On Time-Awareness.
Rollback Orders

You can roll back a backdated or future-dated amendment or renewal. When you submit a rollback order, DRO reverses the change and returns the asset and its related Fulfillment Assets to the state they had before the transaction.

You can roll back an amendment or renewal order, whether it's backdated or future-dated.
You can't roll back a cancellation.
You can't roll back an initial sale, a transfer, or a rollback.
You can't roll back an amendment or renewal that added or removed a product in a bundle.

For the full list of rollback requirements and limitations, see Transaction Rollbacks Considerations.

Swap Orders

DRO decomposes and fulfills swap orders that upgrade or downgrade an asset to a different product. DRO doesn't evaluate constraint rules on swap orders, so swap eligibility that's governed by constraint rules isn't enforced during orchestration.

=== ARTICLE: ind.dro_considerations_for_changing_in_flight_orders.htm ===
---
article_id: ind.dro_considerations_for_changing_in_flight_orders.htm
title: Considerations for Changing In-Flight Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_considerations_for_changing_in_flight_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_in_flight_order_changes.htm
fetched_at: 2026-09-05
---

# Considerations for Changing In-Flight Orders

When you set up Dynamic Revenue Orchestrator (DRO) for in-flight order changes, it's important to understand exactly how DRO handles those changes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Dynamic Revenue Orchestrator is enabled
Amend and Cancel In-Flight Orders

Amend and Cancel are the types of changes that can be made to an in-flight order. A fulfillment designer can configure how a fulfillment step is compensated or rolled back when the step is amended or canceled because of an in-flight change to the order. These compensations and cancellations are defined by the Amend Step Group and Cancel Step Group, respectively, in the fulfillment step definition.

NOTE You can't amend or cancel an in-flight order through an autotask or callout if the step is part of the same fulfillment plan as the submitted order.
Compensation and Rollback Steps

When an in-flight change amends or cancels a fulfillment order, DRO activates the compensatory or rollback step group linked to the step that the plan has reached. The steps in each group compensate for the amended or canceled steps in the initial plan.

Amend Step Group
A group of steps added to compensate for the step that gets amended because of an in-flight change.
Cancel Step Group
A group of steps added to roll back the step that gets canceled because of an in-flight change. Reverse the order of step group execution by enabling the Execute Cancel Step Groups In Reverse Order option on the Fulfillment Step Dependency Definition page.

DRO inserts the Amend and Cancel step groups into the fulfillment plan between two steps. The groups go after a step in a terminal state, such as Completed or Amended, and before the next step in the Pending state.

To change an order that's already processing an in-flight change, define either the Amend Step Group or the Cancel Step Group to handle later changes.

Supplemental Order Behavior for Amend and Cancel Steps

A supplemental order carries the in-flight changes to an order. Based on the source line item changes, a supplemental action amends or cancels the affected fulfillment steps in the original order's fulfillment plan.

Each fulfillment step has two configurations: an Amend Step Group for in-flight amendment and a Cancel Step Group for in-flight cancellation. When a supplemental action amends or cancels a step, DRO inserts the corresponding step group as compensatory steps. DRO doesn't execute a discarded step or insert a step group for it. The step stays in the plan with an updated status.

IMPORTANT Amending or canceling a completed step doesn't automatically retrigger or recreate it in the fulfillment plan. DRO adds compensatory steps only when you explicitly configure an Amend Step Group or Cancel Step Group. If the step has no Amend Step Group or Cancel Step Group, the completed step remains unchanged.
NOTE A supplemental action updates the step status with the changes captured for the related order line items and fulfillment order line items. It doesn't rerun the orchestration steps. To learn how step statuses change for each supplemental action, see the Step Status Changes from Supplemental Actions table in Point of No Return State Propagation.
WARNING Configuring a large number of Amend and Cancel Step Groups can cause a fulfillment plan to reach the fulfillment platform's limit of 1,000 step groups. Both Amend and Cancel Step Groups count toward this limit. Define each group around only the steps that the change affects.
Point of No Return

Define fulfillment steps as a Point of No Return (PONR). When an item in a product bundle reaches the PONR step, the items in the bundle can no longer be modified. However, items within the same order but outside the bundle remain eligible for amendment or cancellation.

Point of No Return Override

If a step reaches PONR and you want to make some changes to the order line, DRO allows you to override the PONR setting. Achieve this override by passing parameters to the Submit Sales Transaction invocable action, specifically by enabling the allowOverrideOfPointOfNoReturn parameter.

See Developer Documentation: Submit Sales Transaction.

Fulfillment Plan States: Freezing and Frozen

Fulfillment plans in DRO progress through various states that control order fulfillment. The Freezing and Frozen states are significant for applying in-flight order changes.

Freezing
The plan is paused but one or more steps in the plan are in progress. You can't submit in-flight change requests when the plan is in the Freezing state.
Frozen
All steps in the plan are completed or in the Pending state. To amend or cancel an in-flight order, the fulfillment plan must be in this state.
Forcefully Freeze Plan During Execution

To change an in-flight order, the order must be in the Frozen state. But an order containing in-progress steps can't be frozen until the order steps are completed. A fulfillment designer can configure DRO to call the Freeze Sales Transaction invocable action, which forcefully completes the steps and changes the plan status to Frozen.

Configure the Force Plan Freeze During Execution option to determine whether the plan can be forcefully changed to the Frozen state. If you use this option, you must specify how to complete the step before resuming the plan.

SEE ALSO
Configure Inflight Plan Settings for a Fulfillment Step
In-Flight Order Change Example

=== ARTICLE: ind.dro_context_definitions_for_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_context_definitions_for_dynamic_revenue_orchestrator.htm
title: Context Definitions for Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_context_definitions_for_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_decomposition.htm
fetched_at: 2026-09-05
---

# Context Definitions for Dynamic Revenue Orchestrator

Dynamic Revenue Orchestrator (DRO) context definitions contain the information required to fulfill a sales transaction. A context definition includes the relationship between nodes and their structure, attributes, context tags, and mapping. Context mapping updates the nodes and attributes with the correct input data from Salesforce objects.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Salesforce Dynamic Revenue Orchestrator is enabled.
Predefined Context Definitions

DRO’s predefined context definitions include:

Sales Transaction Context Definition
Provides the details of a sales transaction such as order line items, relationships, and attributes to the Decomposition process.
Fulfillment Asset Context Definition
Provides the quantities and attributes of the fulfillment assets to the decomposition process to determine the actions on the fulfillment order line items.
Customize Context Definitions for DRO

These predefined context definitions provide a baseline of functionality for sales order decomposition and fulfillment. To customize or extend these context definitions, consult these Context Service learning resources:

Trailhead: Context Service Basics
Key Terms in Context Service
Considerations

When you map a source product tag to a target product tag and if that target product tag is mapped to a reference field in the context definition mapping, enrichment happens only if the outcome of the mapping is compatible with the reference field of the target product tag. We recommend that you avoid selecting such product tags for the target product in the Fields & Attribute Mapping tab.

In the event of an enrichment failure, the Decision Explainer Service (DES) captures the information in the log. See the Explainability Action Logs section on Submit Order Action and Action Logs.

=== ARTICLE: ind.dro_create_a_fulfillment_step_definition_group.htm ===
---
article_id: ind.dro_create_a_fulfillment_step_definition_group.htm
title: Create a Fulfillment Step Definition Group
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_create_a_fulfillment_step_definition_group.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_define_orchestration_components.htm
fetched_at: 2026-09-05
---

# Create a Fulfillment Step Definition Group

Create logical, reusable groups of fulfillment step definitions directly from a fulfillment workspace.

Fulfillment step definition groups represent workstreams in your fulfillment process. For example, you can define groups such as: Procure, Ship, Install, Activate, and Bill.

From the App Launcher, find and select Fulfillment Workspaces.
Click the workspace that you want to add a group to.
Click New Step Group.
Name the group and save your changes.

To help you manage orchestration plans at scale, you can import fulfillment step groups into other workspaces. For more information, see Import a Fulfillment Step Definition Group.

=== ARTICLE: ind.dro_create_and_submit_standard_orders.htm ===
---
article_id: ind.dro_create_and_submit_standard_orders.htm
title: Create and Submit an Order
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_create_and_submit_standard_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# Create and Submit an Order

Sales reps submit simple or bundled product orders in Dynamic Revenue Orchestrator (DRO) for decomposition and to instantiate the orchestration plan.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To create and submit a Standard Order:	

Fulfillment Designer

OR

DRO Admin

NOTE

Before creating order for fulfillment:

Design Your Order Orchestration solution.
Automate Order Submission to Dynamic Revenue Orchestrator.

To create an order and submit it to DRO:

From the App Launcher, find and select Dynamic Revenue Orchestrator.
From the app navigation menu, select Orders.
Click New Order.
Select an account name for the new order.
Enter an Order Start Date.
Save your work.
On the Order page, click Add Products.
From the Choose Price Book page, select Standard Price Book and save.
From the Add Products page, search for and select the products that you want to add to the order and click Next.
Enter the product quantity and save your changes.
Update the Order status to Activated and submit the order.
To make the Submit Sales Transaction invocable action button available on the Order page, you must create a flow for submitting an order and then add that flow to the Order page. For more information, see Automate Order Submission to Dynamic Revenue Orchestrator.
NOTE Some companies use additional Revenue Management features such as Product Catalog Management, Pricing, and Transaction Management. If this is the case, refer to Manage Quote and Order Lifecycle Actions.
SEE ALSO
Developer Documentation: Submit Sales Transactions (API)

=== ARTICLE: ind.dro_create_custom_context_definition_and_map_business_objects.htm ===
---
article_id: ind.dro_create_custom_context_definition_and_map_business_objects.htm
title: Create Custom Context Definition and Map Business Objects
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_create_custom_context_definition_and_map_business_objects.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_orchestrate_sales_transaction_business_processes.htm
fetched_at: 2026-09-05
---

# Create Custom Context Definition and Map Business Objects

Extend a standard context definition where you want to inherit all the standard components such as nodes, attributes, and mappings. Then add components to the extended context definition based on your business requirements.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
USER PERMISSIONS NEEDED
To extend a standard definition and to map attributes to fields:	

DRO Admin User

Prerequisite: Enable permission for context service users.

To make sure that your nodes and attributes are updated with the right input data, create a mapping structure for your context definition. After you create your context definition, search for objects, and click the node and attribute icons that you want to connect to the object fields to start mapping.

From Setup, in the Quick Find box, enter Context Definitions and select it.
For the SalesTransactionsContext record, click , and select Extend.
Enter a name for the context definition, and click Next.
Save your changes.
On the Custom Definition tab, open the new context definition.
For the OrderEntitiesMapping record, click , and select Clone.
Save the new mapping by entering a name and for the new mapping record, click , and then select Edit sObject Mapping.
To set this mapping as your default mapping, select Mark as default, and then click Map.
The page shows the mapping attributes on the left, and the entity fields on the right.
Delete these field mappings between the Sales Transaction node and the Order object by using the Delete icon: Order, OrderAction, OrderItem, OrderItemAttribute, OrderItemDetail, OrderItemGroup, OrderItemRecipient, OrderItemRelationship, and OrderItemTaxLineItem.
In the Connect Objects section on the right, click Add, find and select the business process object that you want to orchestrate, and save your changes.
To map the Sales Transaction node attributes with the new business process object fields, click a mapping attribute, and then click the field that you want to map the attribute to.
IMPORTANT You must delete the default mapping where the OrderID attribute of the FulfillmentTransaction node is mapped to the OrderID field in the FulfillmentOrder object. Then, if the FulfillmentOrder object already has a field that references the business object, map the FulfillmentTransaction node's OrderID attribute to that field. Otherwise, create a custom field on the FulfillmentOrder object and map the OrderID attribute to that field.
For information on the expected context structure and mapping from sales transactions to objects like order and quote, see Dynamic Revenue Orchestrator Context.
For information on mapping sales transactions to your business process object, see Extend Sales Transaction Context Definition.
Save the mapping changes. On the mapping details page, click Activate.
From Setup, in the Quick Find box, enter Context Definition Settings and select it.
In the Sales Transaction Context Definition section, select the new context definition and configure the context nodes that are used to orchestrate the business process.
Save your changes.
SEE ALSO
Configure Procedure Plan Definition for Business Process Orchestration

=== ARTICLE: ind.dro_create_custom_scope_config.htm ===
---
article_id: ind.dro_create_custom_scope_config.htm
title: Create Custom Fulfillment Scope Configuration
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_create_custom_scope_config.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Create Custom Fulfillment Scope Configuration

Custom scopes use a configurable field in the line item or product object as the scope identifier. This identifier defines how fulfillment line items and steps are instantiated. During decomposition and orchestration, custom scopes group fulfillment order line items and steps according to the scope identifier.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To create custom fulfillment scope configuration:	

DRO Admin User

To create a custom scope, define a custom scope configuration with a context tag mapped to a scope identifier field in the order product or a sales transaction item. Configure the custom scope as the custom decomposition scope in the technical product and the custom fulfillment scope in the fulfillment step definition. Update the scope identifier field in the configured order line item and order product. During decomposition, fulfillment order line items are grouped per scope identifier and during orchestration, fulfillment steps are grouped per scope identifier.

From Setup, in the Quick Find box, enter Dynamic Revenue Orchestrator Settings and select it.
Click Custom Fulfillment Scope Config.
Click New Custom Fulfillment Scope Config.
Enter a label for the Custom Fulfillment Scope Config.
Enter the item context tag.

This tag in the Sales Transaction Context Definition points to the field in Order Product or Fulfillment Order Line Item that specifies the custom scope identifier. Where you define and map the tag depends on how you use it.

Decomposition
Define the tag in the Context Node for Sales Transaction Item, and map it to the custom scope identifier field in Order Product.
Plan Generation
Define the tag in the Context Node for Sales Transaction Item, the Context Node for Fulfillment Transaction Item, or both. Map the tag in the Context Node for Sales Transaction Item to the custom scope identifier field in Order Product, and map the tag in the Context Node for Fulfillment Transaction Item to the custom scope identifier field in Fulfillment Order Line Item.
RESTRICTION

The item context tag must use the String data type.

Select the Participating Asset Impact checkbox if you want technical assets related to sales transactions to affect the decomposed line item actions.
When the Participating Asset Impact checkbox is selected, adding a product with the same scope identifier as an existing asset to the order will amend the existing asset. If the Participating Asset Impact checkbox isn't selected, adding any products to the order will create a new fulfillment asset, regardless of the scope identifier.
Select the Assetized checkbox to assetize the decomposed line items.
Save your work.
NOTE Line Item scope is the default fallback scope and is used when no custom scope is derived.
SEE ALSO
Apply Custom Scopes to Fulfillment Steps and Dependencies

=== ARTICLE: ind.dro_create_queues.htm ===
---
article_id: ind.dro_create_queues.htm
title: Create Queues for Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_create_queues.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Create Queues for Dynamic Revenue Orchestrator

Create Salesforce queues to contain fatally failed steps: For example, you can create a queue for each group in your organization that handles fallout. These queues must include Fulfillment Step as a supported object.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
From Setup, enter Queues in the Quick Find box, then select Queues.
Select New Queue.
Select Fulfillment Step as the supported object.
Assign users to the queue. These users must have Fulfillment Manager/Operator permission set assigned or have the Fulfillment User profile.

=== ARTICLE: ind.dro_creating_a_technical_product.htm ===
---
article_id: ind.dro_creating_a_technical_product.htm
title: Create a Technical Product
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_creating_a_technical_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_technical_product_in_dro.htm
fetched_at: 2026-09-05
---

# Create a Technical Product

To create technical products in Dynamic Revenue Orchestrator (DRO), follow these instructions.

REQUIRED EDITIONS
USER
PERMISSIONS NEEDED
To create a technical product:	

Fulfillment Designer

OR

DRO Admin

In Setup, find and select Dynamic Revenue Orchestrator.
Select Products.
Click New.
Enter a descriptive name for the Product.
Select the product type.
To manage the product as an asset, mark the product as assetizable.
Select the decomposition scope. To set the default order decomposition to line item, select None.
To set a custom decompostion scope, select Custom in the Decomposition Scope dropdown list.
Select from the list of custom fulfillment scope configs available in the org. To create a custom fulfillment scope, see Create Custom Fulfillment Scope Configuration.
If the product is marked as assetizable, also select a custom fulfillment scope configuration that is assetizable.
Select the fulfillment quantity calculation method. Selecting None defaults to Aggregate.
To begin decomposition, mark the product as activate.
Save your changes.

=== ARTICLE: ind.dro_cross_plan_dependencies.htm ===
---
article_id: ind.dro_cross_plan_dependencies.htm
title: Cross-Plan Dependencies
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_cross_plan_dependencies.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Cross-Plan Dependencies

Cross-plan dependencies establish connections between steps in different fulfillment plans that are part of related orders. Use cross-plan dependencies when a step in one order's fulfillment plan relies on the completion of a step in a different order's fulfillment plan.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

For example, consider a scenario where the fulfillment plan for Product A contains a platform service activation step. The platform is provisioned as a part of the fulfillment plan for Product B. The two products are part of independent order fulfillment plans belonging to separate orders. Use cross-plan dependencies to make sure that the platform service activation step starts only after the platform provisioning step is complete.

Fulfillment Plan Design

Prerequisites:

Provide a unique Orchestration Group Key for Dynamic Revenue Orchestrator (DRO) to group related orders. The Orchestration Group Key points to an attribute defined under the Sales Transaction node.
To establish ‌fulfillment plans that are grouped based on Orchestration Group Key, map context definitions to the Orchestration Group Key attribute. See Create Custom Context Definitions for Order Orchestration.

To design the fulfillment plan:

In the Fulfillment Workspace, select Cross Plan scope while defining the dependency. See Set Dependencies Between Fulfillment Steps.
Organize fulfillment steps so that dependent steps in one plan wait for the steps they rely on in another plan to complete.
Avoid bidirectional dependencies, where one plan is dependent on a second plan that, in turn, depends on the first. If you set up bidirectional dependencies, DRO doesn’t generate dependencies.
Orchestration

During the fulfillment process:

Access dependencies from the real-time plan view and open the related plans or steps to take action.
Review steps that have cross-plan dependencies within the fulfillment plan. See Monitor Decomposition During Fulfillment.
Submit orders in a specific sequence, so that orders with dependent steps are submitted later. For example, to activate a service before billing the customer, first submit the order with the Activate Service step, and then submit the order with the Bill Customer step.
Take actions such as marking a step as complete and accessing plan and step dependencies from the External Dependencies tab. See Orchestration Plan Actions and Information.
SEE ALSO
Import a Fulfillment Step Definition Group
Set Dependencies Between Fulfillment Steps

=== ARTICLE: ind.dro_custom_scope_step_dependencies.htm ===
---
article_id: ind.dro_custom_scope_step_dependencies.htm
title: Apply Custom Scopes to Fulfillment Steps and Dependencies
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_custom_scope_step_dependencies.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# Apply Custom Scopes to Fulfillment Steps and Dependencies

Use custom scopes to group fulfillment steps and resolve step dependencies based on a business value that you define, such as a tenant group, ramp segment, service location, or sales transaction item group. Standard scopes use a fixed level, such as Plan, Bundle, or Line Item.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
How a Custom Scopes Work

A fulfillment step scope controls the number of step instances Dynamic Revenue Orchestrator (DRO) creates. Use a custom scope on a fulfillment step definition to create one step instance for each distinct scope identifier.

A fulfillment step dependency scope controls which prerequisite step instances a dependent step waits for before it runs. Use a custom scope on a fulfillment step dependency definition to match dependent and prerequisite step instances that have the same scope identifier.

A step can use a standard scope when one of its dependencies uses a custom scope. If your step creation and dependency logic follow the same grouping, apply the same custom scope to the fulfillment step definition and dependency definition.

How a Custom Scopes Identifies a Business Group

DRO derives business groups by evaluating context tags mapped directly to these data fields.

The Sales Transaction Item tag maps to a scope value field on the order product.
The Fulfillment Transaction Item tag maps to a scope value field on the fulfillment order line item.

DRO evaluates these tags to read scope values for each item and groups items sharing the same value together. If DRO can't derive a scope identifier for an item, it assigns the Line Item scope by default.

See Create Custom Fulfillment Scope Configuration.

EXAMPLE

In this scenario, a custom scope named GroupScope uses the Sales Transaction Item Group as its context tag. An order contains four line items divided between two GroupScope values: two for Sales Cloud and two for Service Cloud.

Fulfillment Step Definitions

Fulfillment Step Definitions
FULFILLMENT STEP	FULFILLMENT STEP SCOPE	RESULT
Provision Tenant	Plan	DRO creates one plan-level step instance for the fulfillment plan.
Activate License	Line Item	DRO creates four step instances - one for each applicable order line item.
Notify Customer	Custom: GroupScope	DRO creates two step instances - one for each distinct GroupScope value.

Fulfillment Step Dependencies

Dependency Definitions
DEPENDENT STEP	PREREQUISITE STEP	DEPENDENCY SCOPE	RESULT
Activate License	Provision Tenant	Plan	Each line-item-level Activate License step waits for the plan-level Provision Tenant step.
Notify Customer	Activate License	Custom: GroupScope	Each custom-scoped Notify Customer step waits for Activate License steps whose source line items have the same GroupScope value.

Fulfillment Plan Created from the Custom Step and Dependency Scopes

Execution Logic
The Notify Customer step for Sales Cloud waits for the two Sales Cloud Activate License steps to complete.
The Notify Customer step for Service Cloud waits for the two Service Cloud Activate License steps to complete.
Steps in the other group don't delay either Notify Customer step.

=== ARTICLE: ind.dro_decomposition_relationship_types.htm ===
---
article_id: ind.dro_decomposition_relationship_types.htm
title: Decomposition Relationship Types
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_decomposition_relationship_types.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Decomposition Relationship Types

Dynamic Revenue Orchestrator (DRO) supports one-to-one, one-to-many, many-to-one, and many-to-many decomposition relationships.

REQUIRED EDITIONS
Available in: Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions

Use a one-to-many relationship to fulfill a commercial product as several technical products. Use a many-to-one relationship to consolidate several commercial products into one technical product.

Set the decomposition scope on the technical product to control how often the fulfillment line item is created.

You can also pick a different technical product based on an attribute value. See Define Execution Rules for a Decomposition Rule.

One-to-One Decomposition

A commercial product maps to exactly one technical product. This link is defined by a decomposition rule, which ensures the commercial product decomposes into that specific technical product.

For example, the QuantumBit Database commercial product decomposes to a Database Provisioning technical product.

Use the Order Line Item decomposition scope so that each commercial product line item produces its own technical product.

One-to-Many Decomposition

A one-to-many relationship decomposes a single commercial product into multiple technical products. Create a separate decomposition rule from the commercial product to each technical product.

For example, the QuantumBit Complete commercial product decomposes to three technical products on the same order:

Order Processing
Provisioning and Activation
Shipping for the PowerSwerve R750 server

You can define an execution rule to base the technical product based on an attribute value. For example, the PowerSwerve R750 decomposes to a 1 TB NLSAS drive when the Storage Tier attribute is Standard, or to an 8 TB NLSAS drive when it's Premium.

Many-to-One Decomposition

A many-to-one relationship consolidates multiple commercial products into a single technical product. Create a decomposition rule from each commercial product to the same technical product.

For example, several QuantumBit hardware products on an order need shipping, but you want only one shipping request.

To get one line item per order, map each product to the technical product, and set its decomposition scope to Order.
To decompose multiple commercial products of the same bundle into one technical product, set the decomposition scope to Bundle.
To decompose commercial products across the account, independent of the bundle, into a single technical product, set the decomposition scope to Account.
Many-to-Many Decomposition

A many-to-many relationship maps multiple commercial products to multiple technical products. It combines one-to-many fan-out with many-to-one consolidation: author a decomposition rule for each commercial product and technical product pair that you need.

For example, the QuantumBit Complete and PowerSwerve R750 commercial products both decompose to the Order Processing and Provisioning and Activation technical products. Set the Decomposition Scope on each technical product to control how the matching commercial products are consolidated.

The relationship type you configure while designing the decomposition defines the possible decomposition. The decomposition result depends on the commercial products present on that specific order and on whether the conditions on the decomposition rules qualify. For example, a many-to-one consolidation occurs only when multiple qualifying commercial products are actually on the same order.

=== ARTICLE: ind.dro_decomposition_scope.htm ===
---
article_id: ind.dro_decomposition_scope.htm
title: Decomposition Scope
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_decomposition_scope.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_technical_product_in_dro.htm
fetched_at: 2026-09-05
---

# Decomposition Scope

Set the decomposition scope to limit how many instances of a fulfillment order line item appear in fulfillment.

When you create a product, choose from one of these decomposition scopes in the Decomposition Scope field.

Order Line Item
For every order line item that decomposes to the fulfillment order line item, one instance of the fulfillment order line item is created. This scope is the default if you don't select a scope.
Order
A single instance of the fulfillment order line item is created per order. When the scope is set to Order, the fulfillment order line item cannot be assetized.
Bundle
A single instance of the fulfillment order line item is created per bundle within an order.
Account
A single instance of the fulfillment order line item is created across orders from the same account.
Custom
A single instance of the fulfillment order line item is created per scope identifier. See Create Custom Fulfillment Scope Configuration.

Here's an example of Decomposition Scope in action:

Let's say that there's a technical product called Shipping Service. There are lots of commercial products that decompose to Shipping Service, because lots of products require shipping. However, you don't want to fulfill each of those Shipping Service products individually for the same order.

To handle this situation, set the scope of the Shipping Service product to Order. That way, only one instance of the Shipping Service product is created for every order, no matter how many products in the order call for shipping.

WARNING

When you create a bundle, don't make the child product's scope broader than the parent's scope. For example, if the parent's scope is Order Line Item, then don't set the child's scope to Account. From broad to narrow, the scope is Account, Order, Bundle, Order Line Item.

=== ARTICLE: ind.dro_define_a_fulfillment_step.htm ===
---
article_id: ind.dro_define_a_fulfillment_step.htm
title: Define a Fulfillment Step
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_define_a_fulfillment_step.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_define_orchestration_components.htm
fetched_at: 2026-09-05
---

# Define a Fulfillment Step

After you create a fulfillment step definition group in the workspace, add a fulfillment step definition to it. When an order is submitted, Dynamic Revenue Orchestrator (DRO) creates a fulfillment step in the Orchestration Plan for the order based on this definition.

Here's how to create a fulfillment step definition:

From the App Launcher, find and select Fulfillment Workspaces.
Choose a fulfillment step definition group and click Add Step.
Enter a Fulfillment Step Definition Name.
Select a Step Type.
Some step types require additional information. For details on how to configure each step type, see Fulfillment Step Types.
Select a Scope.
The scope determines how many instances of the fulfillment step is created once the orchestration plan is underway. The scope options are:
Plan: One instance of the step appears in the entire orchestration plan.
Bundle: One instance of the step appears per bundle in the order.
Line Item: One instance of the step appears per line item.
Custom: One instance of the step appears per scope identifier. To create a custom fulfillment scope, see Create Custom Fulfillment Scope Configuration.
Optional: Enter a Custom Config Parameter.
A Custom Config Parameter is a step-specific configuration value passed from an autotask step to a Salesforce Flow. Use it to drive custom logic in the flow based on the parameter's value.
Optional: Select a Run As User.
When DRO executes this step, it uses the selected user's permissions. If you don't select a Run As User, then the step is executed as the Fulfillment User as defined in the DRO settings.
Optional: Select an Execution Schedule. For more information, see Configure Steps for Future Execution.
Optional: If you have In-flight amendment enabled in DRO settings, configure In-Flight Order Changes.
Optional: To configure the conditions for running the step, see Define Conditions for a Fulfillment Step to Run.

=== ARTICLE: ind.dro_define_conditions_for_a_decomposition_rule.htm ===
---
article_id: ind.dro_define_conditions_for_a_decomposition_rule.htm
title: Define Execution Rules for a Decomposition Rule
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_define_conditions_for_a_decomposition_rule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_decomposition.htm
fetched_at: 2026-09-05
---

# Define Execution Rules for a Decomposition Rule

To apply logic that determines when a specific decomposition rule runs, define execution rules that specify the conditions for the rule. By default, products decompose into fulfillment line items independent of execution rules.

REQUIRED EDITIONS
Available in: Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To define conditions for when a decomposition rule runs:	

Fulfillment Designer

OR

DRO Admin User

To prevent order orchestration failures during decomposition or plan composition, complete these configuration prerequisites:

For every context definition attribute you create, define a corresponding tag and map it to an sObject field.
Confirm that all tags are present so that resources appear correctly in the Condition Builder.
Confirm that all attributes are mapped to prevent incorrect condition evaluations during rule execution.
To apply changes to the context definitions, clone the DRO RuleLibrary version, associate the new context definition, and activate it.

To control when a decomposition rule executes, create an execution rule. Execution rules contain the conditions that must be met before the decomposition rule is executed.

From the App Launcher, find and select Dynamic Revenue Orchestrator.
From the app navigation menu, select Products.
Click a product.
Click the Decomposition tab. On the Decomposition Workspace, select a decomposition rule by clicking the connector icon on the line that connects the source and target products. A side panel opens with the Details, Execution Rules, and Attribute Mapping tabs.
In the side panel, click the Execution Rules tab.
Click Configure Execution Rules.
In the Condition Builder modal, configure the conditions.
In the Based On field, select Sales Transaction Items.
Select a Condition Requirement to determine how multiple conditions within the rule are evaluated:
For every condition to be met, select All Conditions Are Met (AND).
For at least one condition to be met, select Any Condition Is Met (OR).
To create complex logic, select Custom Logic Is Met.
NOTE If a decomposition rule condition (ruleset) contains multiple dynamic rules, they are evaluated separately. The condition evaluates to true if at least one individual dynamic rule is true, applying OR logic between the rule results.
In the Resource field, select a tag or attribute.
NOTE The items available in the resource list are determined by your tags and attributes configuration:
Tags: Sourced from the Sales Transaction Item (STI) context nodes within the active context definition mapped in Setup. If an STI context node does not have a defined tag, it does not appear in the resource list. If a tag is defined but is not mapped to an object field, the condition evaluates to false at runtime.
Attributes: Populated from the source product or product classification attributes.
From the Operator dropdown, select a value, such as Equals.
Enter or select a Value.
NOTE For picklist resource tags, enter the text value manually.
Save your changes.

Let's explore an example of a execution rule in action:

Imagine you sell a Cloud Security Suite with a service tier attribute that can be either Standard or Enterprise. You want the suite to decompose into different fulfillment patterns based on this style.

Single Execution Rule: To ensure only enterprise-tier suites follow a specific decomposition rule, go to the execution rule builder. In the Based On field, select Order Line Items. Set the condition to Service Tier Equals Enterprise. The rule executes only when an order line item contains an enterprise-tier suite.

Multiple Execution Rules: If you want the same decomposition rule to apply to both Standard and Enterprise tiers, you can create two separate execution rules—one for each tier. Because multiple rules are evaluated using OR logic at the ruleset level, the decomposition rule executes if either tier is detected in the order line item.

NOTE Enter the text value manually for resource tags of picklist type.

=== ARTICLE: ind.dro_define_conditions_for_a_fulfillment_step_to_run.htm ===
---
article_id: ind.dro_define_conditions_for_a_fulfillment_step_to_run.htm
title: Define Conditions for a Fulfillment Step to Run
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_define_conditions_for_a_fulfillment_step_to_run.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# Define Conditions for a Fulfillment Step to Run

You can prevent a fulfillment step from running until certain conditions are met.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To set conditions for a fulfillment step to run:	

Fulfillment Designer

OR

DRO Admin User

From the App Launcher, find and select Fulfillment Workspaces.
Locate a step you wish to add execution conditions to. Click  and select Configure Execution Rules.
Click Create Rule.
whether the rule is based on a Sales transaction item or a fulfillment line item. For more information, see Define Execution Rules for a Decomposition Rule.
NOTE For fulfillment steps, you can evaluate conditions against Fulfillment Line Items. As the fulfillment system has already generated the necessary fulfillment records by this stage, the data is available for the rule to check.
Set the conditions. Choose from these options:
All Conditions Are Met
Any Condition Is Met
Custom Condition Logic Is Met. In this case, you define the logic.
Select the resources to evaluate. The resources are either sales transaction or fulfillment line item context tags as defined in the DRO context definition.
Add additional resources to evaluate, if necessary.
Save your work.
To skip the entire branch of remaining steps rather than just one step, turn on Skip Branch.
When the step's conditions aren't met, DRO skips the step and the branch that depends solely on it. For more information, see How Skipping a Fulfillment Branch Works.
How Skipping a Fulfillment Branch Works
A fulfillment branch contains an initial step and a series of dependent steps that follow it. When you turn on Skip Branch for a step and that step is skipped, the branch that depends on the step is also skipped because the remaining steps no longer apply. For example, if the Get Shipping Address step is skipped, the subsequent steps related to shipping are also skipped.

=== ARTICLE: ind.dro_define_field_and_attribute_mapping.htm ===
---
article_id: ind.dro_define_field_and_attribute_mapping.htm
title: Define Field and Attribute Mapping
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_define_field_and_attribute_mapping.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_decomposition.htm
fetched_at: 2026-09-05
---

# Define Field and Attribute Mapping

Define how Dynamic Revenue Orchestrator (DRO) maps fields and attribute data between products. DRO uses this mapping to copy or transform commercial order data to the data that fulfillment systems or processes require.

REQUIRED EDITIONS
Available in: Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To define field and attribute mapping:	

Fulfillment Designer

OR

DRO Admin User

NOTE Before you begin, make sure you have created decomposition rules. For more information on how to create decomposition rules, see Define How a Product Decomposes.

To create a mapping for fields and attributes, follow these instructions:

From the App Launcher, find and select Dynamic Revenue Orchestrator.
From the app navigation menu, select Products.
Click a product.
Click the Decomposition tab and select a decomposition rule.
In the side panel, click More and then click Field & Attribute Mapping.
Click Create Mapping.
Click a source attribute or tag, and then click the target attribute or tag that you want to map to.
See the supported target data types for each source data type in Data Type Compatibility for Field and Attribute Mapping.
If in-flight amendments are enabled for DRO, select a Rule Enforcement:
To include amended or canceled in-flight orders, select All Fulfillment Requests.
To exclude amended or canceled in-flight orders, select Initial Fulfillment Request.
For Mapping Type, select As Is, List Mapping, or Expression Set Based Mapping
As Is mapping copies the exact value from the source product to the target product.
For information about List Mapping, see Configure List Mapping.
For information about Expression Set Based Mapping, see Configure Expression Set Based Mapping.
Save your work.

A line is drawn between the two items to show the mapping. When the commercial product decomposes, the target product is enriched with data from the source of the mapped pair. When you map a source product tag to a target product tag that points to a reference field, the data enriches only if the two fields are compatible. If they don't match, the enrichment process fails, and the Decision Explainer Service (DES) records the error in a log. See the Explainability Action Logs section in Submit Order Action and Action Logs.

NOTE Field and Attribute mapping relies on context definitions. If you wish to create custom mappings, you must extend and customize th predefined context definitions included with DRO. For more information, see Context Definitions for Dynamic Revenue Orchestrator.
Data Type Compatibility for Field and Attribute Mapping
When you map a source attribute or field to a target attribute or tag, Dynamic Revenue Orchestrator (DRO) validates that the source and target data types are compatible. If they aren't compatible, the mapping can't be created.
Configure List Mapping
Use list mapping to set up pairs of source and destination values. For example, a list of cities that pair with post code values. When the source value is a city name, the target receives the post code of that city. Configure list mapping from the Fields & Attribute Mapping section of a decomposition rule.
Configure Expression Set Based Mapping
Use expression sets to perform complex transformations on the source product's fields and attributes and use the output variables of the expression sets to enrich the target product's fields and attributes. For example, set delivery priority in the target product based on the order value and the delivery zipcode.
SEE ALSO
Define How a Product Decomposes

=== ARTICLE: ind.dro_define_how_a_product_decomposes.htm ===
---
article_id: ind.dro_define_how_a_product_decomposes.htm
title: Define How a Product Decomposes
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_define_how_a_product_decomposes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_decomposition.htm
fetched_at: 2026-09-05
---

# Define How a Product Decomposes

Use the decomposition workspace to set up rules that control how a commercial product or product classification breaks down into technical products. Define conditions and priorities for the decomposition rules. By default, all products decompose into fulfillment line items unless you specify an execution rule and that rule evaluates to false for a given sales transaction item.

REQUIRED EDITIONS
Available in: both Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To define how a product decomposes:	

Fulfillment Designer

OR

DRO Admin User


To define decimal quantity at design time and run time:	

Decimal Quantity Design Time

AND

Decimal Quantity Run Time

NOTE

Before you can define how products decompose, you must create your product catalog and understand the role of the Decomposition Scope. See Build Your Technical Product Catalog for Dynamic Revenue Orchestrator.

For information on the number of products and decomposition rules supported, see Dynamic Revenue Orchestrator Limits.

From the App Launcher, find and select Dynamic Revenue Orchestrator.
From the app navigation menu, select Products.
Click a product.
Go to the Decomposition tab.
The Decomposition tab is available out-of-the-box when accessing the product page within the DRO app. For other applications, manually add and configure the Product Decomposition Workspace Lightning Web Component to the record page using Lightning App Builder.
The workspace shows product class-based decomposition rules that the product inherited alongside the product’s decomposition rules. If the destination is a technical bundle, the workspace shows the complete hierarchy starting from the decomposed product as the root. By default, the canvas shows the full structure, including parent products. Switch the action bar toggle to only see the decomposed technical products. In the workspace side panel, rules are grouped and sorted to list the product class-based decomposition rules first, followed by product-based rules. Within these groups, rules are sorted by priority and then by modification date.

For details on how technical bundles affect grouping, see. Technical Bundles

Click Add Decomposition Rule and enter a unique name.
Enter a unique name for the decomposition rule.
Don't include special characters like the greater-than symbol (>) in decomposition rule names. This character can cause plan execution failures during fulfillment.
Enter the priority. The lower the number, the higher the priority.
When you configure two decomposition rules that map to the same target, Dynamic Revenue Orchestrator writes data from the rule with the lowest number to the destination product. If two decomposition rules have the same priority, then the most recently modified rule takes precedence.
Enter a destination product.
The source product or product classification decomposes to the destination product.
Save your work:
To save and view the details page for the rule, click Save.
To save and then define conditions for when the rule runs during fulfillment, click Save & Add Execution Rules. See Define Execution Rules for a Decomposition Rule.

You can map fields and attributes between the commercial and technical products of your decomposition rules, so that the fulfillment line items inherit data from the source products. See Define Field and Attribute Mapping.

SEE ALSO
Decomposition Relationship Types

=== ARTICLE: ind.dro_define_orchestration_components.htm ===
---
article_id: ind.dro_define_orchestration_components.htm
title: Define Orchestration Plan Components
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_define_orchestration_components.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# Define Orchestration Plan Components

Create and organize fulfillment steps, their dependencies, and fulfillment processes in fulfillment workspaces.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To create and manage fulfillment workspaces:	

Fulfillment Designer

OR

DRO Admin User

Manage your orchestration plans using fulfillment workspaces. The fulfillment workspace is a graphical representation of all the fulfillment tasks, organized into a timeline.

Within the workspace, organize your fulfillment workstreams using fulfillment step groups. Then, define each tasks, process, or milestone using fulfillment steps within the step groups.

Fulfillment step groups represent workstreams and fulfillment steps represent unique actions within those workstreams. Here's a diagram of showing how these elements are used in a workspace:

To get started with your orchestration plan, follow these instructions:

Create a Fulfillment Workspace
To get started, create a fulfillment workspace. You can then add fulfillment groups and steps to the workspace.
Clone a Fulfillment Workspace
Copy a fulfillment workspace and its supported design-time records to create a starting point for a new orchestration design. Changes to the cloned workspace don’t affect the source workspace.
Create a Fulfillment Step Definition Group
Create logical, reusable groups of fulfillment step definitions directly from a fulfillment workspace.
Define a Fulfillment Step
After you create a fulfillment step definition group in the workspace, add a fulfillment step definition to it. When an order is submitted, Dynamic Revenue Orchestrator (DRO) creates a fulfillment step in the Orchestration Plan for the order based on this definition.

=== ARTICLE: ind.dro_define_technical_attribute_scope.htm ===
---
article_id: ind.dro_define_technical_attribute_scope.htm
title: Define Technical Product Attribute Scope
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_define_technical_attribute_scope.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_decomposition.htm
fetched_at: 2026-09-05
---

# Define Technical Product Attribute Scope

Use technical product attribute scopes to define the role of product attributes in decomposition and assetization. The scope determines whether attribute changes trigger fulfillment or supplemental actions on decomposed line items, or impact fulfillment assets. Defining these scopes at design time optimizes orchestration by processing only relevant updates and keeping asset data lean.

REQUIRED EDITIONS
Available in: Both Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To define how a product decomposes:	

Fulfillment Designer

OR

DRO Admin User

Dynamic Revenue Orchestrator provides these three predefined opt-out scopes.

SCOPE NAME	ACTION	EFFECT
Decomposition Action Opt-Out Scope	It determines if an attribute influences fulfillment actions during order decomposition.	Use the new product attribute scope to prevent technical attribute changes from affecting fulfillment line actions. When you define an attribute with this scope, technical values don’t influence fulfillment actions during order decomposition.
Supplemental Action Opt-Out Scope	It determines if an attribute influences supplemental actions during order decomposition.	Use the new product attribute scope to prevent technical attribute updates from affecting supplemental actions. When you define an attribute with this scope, technical changes don’t influence supplemental actions during order decomposition.
Assetization Opt-Out Scope	It determines if an attribute value a part of the fulfillment assets.	If you define an attribute with this scope, the attribute is excluded from the fulfillment asset.

Define a product attribute mapped scope to associate one of the opt-out scopes to a product attribute. Note these considerations while creating product attribute mapped scopes.

Create a decomposition action opt-out mapped scope for a product attribute before you create an assetization opt-out mapped scope.
Delete the assetization action opt-out mapped scope for a product attribute before you delete the associated decomposition opt out mapped scope.
Create and delete the supplemental action opt-out scope independent of the other two scopes.
A product attribute can have only one mapped scope record per scope, allowing a maximum of three records—one for each predefined opt-out scope.

To create a product attribute mapped scope, perform these steps:

From the App Launcher, find and select Dynamic Revenue Orchestrator.
From the app navigation menu, select Product Attribute Mapped Scopes.
Click New.
Select Associated Product Attribute from the Product Attribute Definition or Product Classification Definition dropdown list.
Select a scope from the Product Attribute Scope dropdown list.
Save your work.

=== ARTICLE: ind.dro_design_time_decomposition.htm ===
---
article_id: ind.dro_design_time_decomposition.htm
title: Design Your Order Decomposition
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_design_time_decomposition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Design Your Order Decomposition

Define how your commercial products decompose into technical products that your order fulfillment team can deliver to your customers. Products decompose based on rules you define, and the technical products can inherit field and attribute data from related commerical products.

REQUIRED EDITIONS
Available in: Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
NOTE Dynamic Revenue Orchestrator relies on having a product catalog populated with both commercial and technical products. If you aren't familiar with building a product catalog, see Product Catalog Management.

When an order is submitted, the order line items decompose into fulfillment order line items. Your fulfillment designer creates the decomposition rules and mappings necessary to fulfill a commercial order with its technical products.

To get started designing your order decomposition solution, follow these instructions:

Build Your Technical Product Catalog for Dynamic Revenue Orchestrator
A technical product represents the items, services, or processes that enable order fulfillment to deliver a complete commercial product to your customer. A technical product lets fulfillment designers decouple front-office entities from mid- and back-office entities. To use Dynamic Revenue Orchestrator, you must configure your technical products using Product Catalog Management.
Define Technical Product Attribute Scope
Use technical product attribute scopes to define the role of product attributes in decomposition and assetization. The scope determines whether attribute changes trigger fulfillment or supplemental actions on decomposed line items, or impact fulfillment assets. Defining these scopes at design time optimizes orchestration by processing only relevant updates and keeping asset data lean.
Define How a Product Decomposes
Use the decomposition workspace to set up rules that control how a commercial product or product classification breaks down into technical products. Define conditions and priorities for the decomposition rules. By default, all products decompose into fulfillment line items unless you specify an execution rule and that rule evaluates to false for a given sales transaction item.
Define Execution Rules for a Decomposition Rule
To apply logic that determines when a specific decomposition rule runs, define execution rules that specify the conditions for the rule. By default, products decompose into fulfillment line items independent of execution rules.
Define Field and Attribute Mapping
Define how Dynamic Revenue Orchestrator (DRO) maps fields and attribute data between products. DRO uses this mapping to copy or transform commercial order data to the data that fulfillment systems or processes require.
Context Definitions for Dynamic Revenue Orchestrator
Dynamic Revenue Orchestrator (DRO) context definitions contain the information required to fulfill a sales transaction. A context definition includes the relationship between nodes and their structure, attributes, context tags, and mapping. Context mapping updates the nodes and attributes with the correct input data from Salesforce objects.
Unit Of Measure Inheritance and Rounding Values
During decomposition, the fulfillment order product inherits the unit of measure from the related technical product. During technical assetization, the fulfillment asset inherits the unit of measure from the corresponding fulfillment order line item.
SEE ALSO
Ramp Deals

=== ARTICLE: ind.dro_design_time_orchestration.htm ===
---
article_id: ind.dro_design_time_orchestration.htm
title: Design Your Order Orchestration
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_design_time_orchestration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Design Your Order Orchestration

Build strategic, efficient, and adaptable order orchestration in Dynamic Revenue Orchestrator (DRO). Create order fulfillment steps, fulfillment step groups, dependencies, and rules for how DRO fulfills orders. Fulfillment steps can be automated, manual, or dependent on other steps.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Order Orchestration runs after decomposition completes. If you haven't designed your decomposition rules yet, see Design Your Order Decomposition.

You can decide the depth at which to implement orchestration in DRO. Orchestration can a simple fulfillment tracker, with most of the fulfillment details handled by your ERP, or use DRO to more deeply model your orchestration.

To get started designing your order orchestration solution, follow these instructions:

Define Orchestration Plan Components
Create and organize fulfillment steps, their dependencies, and fulfillment processes in fulfillment workspaces.
Fulfillment Step Types
When you plan your orchestration, keep in mind the different types of fulfillment steps, and how they work. Fulfillment step types can be used to define manual tasks, automated tasks, milestones, callouts, and other actions.
Design Orchestration with the High Tech Order Orchestration Template
Use the High Tech Order Orchestration Template as a starting point for orders that combine project work, hardware assembly, software provisioning, billing, and revenue scheduling.
In-Flight Order Changes
Sometimes customers request modifications to their orders after the order is submitted for fulfillment by the sales rep. Modifications can include changing the entire order, specific line items, or even canceling part or all of the order. Changes that happen during fulfillment are called in-flight order changes.
Import a Fulfillment Step Definition Group
To help scale your fulfillment plans, and ensure consistency across plans, you can import your existing fulfillment step definition groups directly from a fulfillment workspace.
Set Dependencies Between Fulfillment Steps
Connect fulfillment step definitions to create a dependency between them. When an order is submitted, the steps run in the order that you define.
Create a Fulfillment Task Assignment Rule
Create reusable rules to automatically assign manual tasks to users based on the criteria and conditions defined in the rule.
Configure a Fulfillment Scenario
Use a fulfillment scenario to define when Dynamic Revenue Orchestrator (DRO) adds a fulfillment step definition group to a fulfillment plan after an order is submitted. Fulfillment scenarios help you add common fulfillment steps automatically instead of creating the steps for each order.
Define Conditions for a Fulfillment Step to Run
You can prevent a fulfillment step from running until certain conditions are met.
Configure Steps for Future Execution
Fulfillment designers can configure the steps to be executed at a future date and time. They can set a delay for the execution of steps based on the start date of the source line item, the execution time of the previous steps, or a custom date based on a context definition field.
Apply Custom Scopes to Fulfillment Steps and Dependencies
Use custom scopes to group fulfillment steps and resolve step dependencies based on a business value that you define, such as a tenant group, ramp segment, service location, or sales transaction item group. Standard scopes use a fixed level, such as Plan, Bundle, or Line Item.

=== ARTICLE: ind.dro_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_dynamic_revenue_orchestrator.htm
title: Order Orchestration in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
fetched_at: 2026-09-05
---

# Order Orchestration in Revenue Management

Dynamic Revenue Orchestrator (DRO) breaks down a single commercial order into multiple, manageable fulfillment steps. You can execute a tailored fulfillment plan for each product or service.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
NOTE Learn the fundamentals in Dynamic Revenue Orchestrator Foundations.

Dynamic Revenue Orchestrator breaks down a customer's commercial order into the individual technical products, services, and tasks that are needed to fulfill it. The decomposition process bridges the gap between how a product is sold by sales reps and how it is actually delivered and managed by your order fulfillment team.

After order items are decomposed into fulfillment line items, an orchestration fulfillment plan tracks the stages and tasks required to fulfill the order to completion. A fulfillment plan can contain prioritization rules, SLAs, external callouts, automated tasks, manual tasks, and order fallout contingencies.

Here's a high-level summary of the steps required to build your DRO solution.

Create your technical product catalog.
Define how products decompose using decomposition rules, field mapping, and execution rules.
Create fulfillment plans using a visual plan editor in the fulfillment workspace.
Define fulfillment steps and product fulfillment scenarios for each of your fulfillment plans.
Define rules for handling SLA jeopardy and order fallout.
Monitor orchestration in real time using the fulfillment orchestration dashboard.

To migrate product fulfillment decomposition rules, fulfillment scenarios, fulfillment step definitions, and fulfillment task assignment rules between Salesforce orgs, use Data API. For high-volume data transfers, use Bulk API to move these records and their associated condition data.

Dynamic Revenue Orchestrator Integrations

You can use DRO to orchestrate Industries Configure, Price, Quote (CPQ) orders. Because DRO is preintegrated with Industries CPQ, you can use DRO without migrating commercial product data out of Enterprise Price Catalog (EPC). See Salesforce Release Note: Integrate DRO with Industries CPQ.

You can fulfill a single order in Salesforce Commerce Cloud across both DRO and Order Management in one coordinated process. Order Management typically fulfills physical goods, while DRO fulfills digital and service items. When an order contains items handled by both systems and Order Management is enabled, Order Management converts the order into an order summary and submits it to Dynamic Revenue Orchestrator through the Submit API. Dynamic Revenue Orchestrator now supports order summaries in both the Submit API and orchestration, so each item is routed to the right system and these actions stay coordinated across the order lifecycle:

Validated cancellation: Cancel an item only when it's still allowed, based on the fulfillment progress of related items. For example, cancel the install only before the technician is dispatched.
Mid-flight adjustments: Keep quantities aligned across systems when an order is updated in flight. If only 5 of 10 locks ship, the install count drops to 5.
Global order termination: Cancel an entire order and stop all related fulfillment activity together, halting both the lock shipment and the scheduled install.
Linked exchange: Coordinate replacements across systems without duplicate charges, such as a no-charge reinstall when a lock is defective.

See Dynamic Revenue Orchestration with Order Management

NOTE Dynamic Revenue Orchestrator processes one in-flight cancellation or amendment request from Order Management per order. It rejects any later change requests.

=== ARTICLE: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm ===
---
article_id: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
title: Dynamic Revenue Orchestrator Concepts and References
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Dynamic Revenue Orchestrator Concepts and References

Learn about key concepts to help you understand how DRO works and how to get the most from using it.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

=== ARTICLE: ind.dro_dynamic_revenue_orchestrator_limits.htm ===
---
article_id: ind.dro_dynamic_revenue_orchestrator_limits.htm
title: Dynamic Revenue Orchestrator Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_dynamic_revenue_orchestrator_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Dynamic Revenue Orchestrator Limits

Order fulfillment processes are governed by limits on order submission, order line items, fulfillment order line items, and workspace usage. These limits differ for asynchronous and synchronous intake, and Dynamic Revenue Orchestrator responds in specific ways when the limits are exceeded.

REQUIRED EDITIONS
Available in: Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
Order Submission Limits
ORCHESTRATION ITEM	LIMIT DESCRIPTION	SYNCHRONOUS SUBMISSION LIMIT	ASYNCHRONOUS SUBMISSION LIMIT	SYSTEM ACTION IF THE LIMIT IS CROSSED
Fulfillment Orders	The number of high-priority fulfillment orders that can be submitted per hour.	2400	2400	Processes additional orders by using the default priority level or rejects them as configured. See Order Prioritization
Order Line Item Limits
ORCHESTRATION ITEM	LIMIT DESCRIPTION	SYNCHRONOUS SUBMISSION LIMIT	ASYNCHRONOUS SUBMISSION LIMIT	SYSTEM ACTION IF THE LIMIT IS CROSSED
Order Items	The number of order items that can be submitted per order.	200	1000	Rejects order submissions containing additional order items.
Attributes per order line item	The number of attributes that can be processed per line item.	50	100	Rejects order submissions containing additional attributes per order item.
Decomposition Rules	The number of decomposition rules that can be processed per order.	400	2000	Rejects order submissions containing additional decomposition rules.
Enrichment Rule Mapping	The number of enrichment rules that can be defined for a decomposition rule.	20	20	Prevents the creation of records.
Fulfillment Scenarios	The number of fulfillment scenarios that can be defined per order.	400	2000	Rejects order submissions containing additional fulfillment scenarios.
Fulfillment Order Limits
ORCHESTRATION ITEM	LIMIT DESCRIPTION	SYNCHRONOUS SUBMISSION LIMIT	ASYNCHRONOUS SUBMISSION LIMIT	SYSTEM ACTION IF THE LIMIT IS CROSSED
Attributes	The number of attributes that can be processed per order.	3000	3000	Rejects order submissions containing additional attributes.
Fulfillment Order Line Item Limits
ORCHESTRATION ITEM	LIMIT DESCRIPTION	SYNCHRONOUS SUBMISSION LIMIT	ASYNCHRONOUS SUBMISSION LIMIT	SYSTEM ACTION IF THE LIMIT IS CROSSED
Attributes	The number of attributes that can be processed per fulfillment order line item.	50	100	Rejects order submissions containing additional attributes.
Fulfillment Steps	The number of fulfillment steps that can be added to a fulfillment plan.	200	2000	Rejects order submissions containing additional fulfillment steps.
Step Sources	The number of order item sources or fulfillment transaction item sources that can be defined per fulfillment step.	25	125	Rejects order submissions containing additional sources.
Fulfillment Task Assignment Rules	The number of fulfillment task assignment rules that can automatically assign manual tasks to users.	200	200	Prevents additional manual task assignments.
The number of fulfillment task assignment rules that can automatically assign manual tasks to users for a matching source in the step definition.	10	10	Prevents additional manual task assignments.
Non-Sales Transaction Object Orchestration Limits
ORCHESTRATION ITEM	LIMIT DESCRIPTION	SYNCHRONOUS SUBMISSION LIMIT	SYSTEM ACTION IF THE LIMIT IS CROSSED
Fulfillment Scenarios	The number of fulfillment scenarios that can be defined per object.	100	Rejects submissions of objects containing additional fulfillment scenarios.
Fulfillment Steps	The number of fulfillment steps that can be added to a fulfillment plan.	100	Rejects object submissions containing additional fulfillment steps.
Step Sources	The number of sources that can be defined per fulfillment step.	10	Rejects object submissions containing additional sources.
Decomposition Workspace and Fulfillment Workspace Limits
ORCHESTRATION ITEM	LIMIT DESCRIPTION	LIMIT	SYSTEM ACTION IF THE LIMIT IS CROSSED
Decomposition Workspace	The number of products that can be shown in the workspace for a product bundle.	200	Products are filtered based on priority and last modified date. Additional products aren't shown in the workspace.
The number of decomposition rules that can be shown in the workspace.	200	Decomposition rules are filtered based on priority and last modified date. Additional rules aren't shown in the workspace.
The number of decomposition rules related to a product that can be shown on the workspace side panel.	From the product -100 To the product - 100	Decomposition rules are filtered based on priority and last modified date. Additional rules aren't shown in the side panel.
Fulfillment Workspace	The number of fulfillment step groups that can be associated with a fulfillment workspace.	100	The additional step groups that are created aren’t shown in the fulfillment workspace.
The number of dependencies that can be created within a fulfillment step definition group.	100	The additional dependencies that are created aren’t shown in the fulfillment workspace.
The number of fulfillment steps that can be created within a workspace item or fulfillment step definition group.	100	The additional fulfillment steps that are created aren’t shown in the fulfillment workspace.
The number of records in a fulfillment workspace that can be cloned.	500	The additional records in the fulfillment workspace aren’t cloned.
Expression Set Limits

This section lists the specific limits that apply to expression sets defined using the Decomposition Enrichment Mapping usage type. For additional default limits on expression sets from Business Rules Engine, see Business Rules Engine Default Limits.

LIMIT DESCRIPTION	LIMIT
The number of expression sets.	20
The number of steps in an expression set.	20
The total number of input and output variables in an expression set.	50

=== ARTICLE: ind.dro_enable_analytics.htm ===
---
article_id: ind.dro_enable_analytics.htm
title: Dynamic Revenue Orchestrator Analytics
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_enable_analytics.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.revenue_intelligence_rev_intelligence_apps_dashboards.htm
fetched_at: 2026-09-05
---

# Dynamic Revenue Orchestrator Analytics

After installing the Dynamic Revenue Orchestrator (DRO) Analytics app, you can use the delivered Tableau dashboards: Order Analysis and Order Details. While DRO fulfills the orders, monitor the processing from the dashboards.

REQUIRED EDITIONS
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management

Gain valuable insights into your fulfillment operations with the Order Analysis dashboard. Analyze the status of tasks, orders, and trends, and visualize key metrics using bar charts and line graphs to support informed decision-making.

The Order Details dashboard provides a comprehensive view of submitted sales orders. The dashboard includes the various fulfillment steps associated with each order and details for each fulfillment step, such as the fulfillment step's name, ID, type, jeopardy status, and current state.

Configure Dynamic Revenue Orchestrator Analytics Dashboards
Add the delivered Order Analysis and Order Details dashboards to your home page and order record page, respectively. Use filters to further refine the details to be displayed on charts and graphs.

=== ARTICLE: ind.dro_enable_in_flight_amendments.htm ===
---
article_id: ind.dro_enable_in_flight_amendments.htm
title: Turn On In-Flight Amendments
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_enable_in_flight_amendments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Turn On In-Flight Amendments

Enable your order reps to change fulfillment requests that are in progress. By enabling In-Flight Amendments, users can modify the order or specific line items, or even cancel the entire order or parts of it.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Dynamic Revenue Orchestrator is enabled
USER PERMISSIONS NEEDED
To enable In-Flight Amendments:	System Administrator profile

Before you begin, enable Dynamic Revenue Orchestrator.

From Setup, in the Quick Find box, enter Dynamic Revenue Orchestrator Settings and select it.
Turn on In-Flight Amendments.

=== ARTICLE: ind.dro_enable_permission_for_users.htm ===
---
article_id: ind.dro_enable_permission_for_users.htm
title: Enable Permission for Context Service Users
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_enable_permission_for_users.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_steps_to_create_a_custom_context_definition.htm
fetched_at: 2026-09-05
---

# Enable Permission for Context Service Users

Create and manage context definitions easily and efficiently by assigning permission set licenses to your users. Add permissions to specific user personas to complete the work assigned to their role. System admin users have default access to Context Service without requiring any specific permission set licenses.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To assign permissions to a user:	

DRO Admin User

From Setup, in the Quick Find box, enter Users and select it.
Select a user.
On the Permission Set License Assignment and Permission Set Assignments tabs, turn on Context Service Admin.
SEE ALSO
Create Custom Context Definition and Map Attribute to Field
Create Custom Context Definition and Map Business Objects

=== ARTICLE: ind.dro_fallout_administration.htm ===
---
article_id: ind.dro_fallout_administration.htm
title: Configure Automation Failure Handling
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_fallout_administration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Configure Automation Failure Handling

Define how Dynamic Revenue Orchestrator (DRO) handles an auto task or callout failure with fallout rules and fulfillment step retries.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Determine what DRO does when automated steps fail. For example, set up a rule so that a callout responds to error code 402 by retrying up to three times. Then if the callout still fails, it gets assigned to a specific queue for resolution.

=== ARTICLE: ind.dro_fallout_design_and_management.htm ===
---
article_id: ind.dro_fallout_design_and_management.htm
title: Fallout Design and Management
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_fallout_design_and_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Fallout Design and Management

Fallout refers to fulfillment steps that have failed. Dynamic Revenue Orchestrator (DRO) can retry failed callouts or auto tasks, send them to a queue, or simply mark them as failed. During fulfillment, operators can mark steps as complete, or retry them.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

When designing fulfillment, create rules that determine what DRO does when a step fails. For example, set the number of times the step retries before being assigned to a queue for resolution.

During the fulfillment process, retry failed steps, or mark them as complete, either one by one or in bulk.

EXAMPLE The fulfillment designer creates a rule so that if a Credit Check callout step receives an error from the credit department, the step retries 3 times. If the step still fails, then it goes to the Credit Team Fallout queue.

During fulfillment, the credit department's credit check system is down for a few minutes. After the credit check system is back online, the credit team checks the fallout queue, selects all the failed callouts in the queue, and clicks Retry.

All the steps retry, and since the system is back online, they're all successful and fulfillment continues.

Design Time

Before fulfillment, designers configure fallout in DRO:

Turn on Fallout settings. See Turn On Features to Manage Fallout and Service Level Agreements
Create Salesforce queues to contain fatally failed steps: For example, you can create a queue for each group in your organization that handles fallout. These queues must include Fulfillment Step as a supported object. See Create Queues. To add fatally failed steps to an existing queue, you must either be a member of the queue or have the System Administrator permission set. Assigning a fulfillment step to a fallout queue does not trigger email notifications or create Salesforce tasks.
Configure fallout rules: These rules tell DRO how many times a step retries, and when. They also tell DRO which queue to send fatally failed steps. See Configure Fallout Rules

After you create or update a Fulfillment Fallout Rule, refresh the Fulfillment Fallout Rules decision table.

NOTE Until you refresh the decision table, DRO reevaluates the previous rule configuration. If no rule matches the step and error code, DRO sets the step status to FATALLY_FAILED without retrying it.

DRO retries errors that a flow returns through an Auto Task Fault Path. It doesn't retry raw or unhandled Apex exceptions. To make an Apex failure eligible for retry, handle the failure through the flow's Fault Path and return the required Auto Task output variables. See Auto Task Fulfillment Step.

Run Time

During fulfillment, manage fallout:

Monitor fallout in queues To view fatally failed steps in a specific queue, navigate to the Fulfillment Steps tab and select the Fatally Failed Fulfillment Steps list view. Filter by the Queue column to see your assigned records. See Monitor Decomposition During Fulfillment.
To see steps that have failed, check the fulfillment plan, fallout queues, or the Fatally Failed Fulfillment Steps list view. See Monitor Decomposition During Fulfillment.
Retry callouts and auto task steps, or mark them complete. You can do so one at a time, or in bulk. See Retry or Complete Multiple Failed Fulfillment Steps.
SEE ALSO
Monitor Decomposition During Fulfillment

=== ARTICLE: ind.dro_fulfillment_order_line_item_actions.htm ===
---
article_id: ind.dro_fulfillment_order_line_item_actions.htm
title: Fulfillment Order Line Item Actions
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_fulfillment_order_line_item_actions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Fulfillment Order Line Item Actions

When an order is decomposed, each fulfillment order line item gets an action that’s derived from the related order line item actions.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
Fulfillment Order Line Item Actions

When Dynamic Revenue Orchestrator (DRO) decomposes asset-based orders, it compares the attributes and quantity of the order line items with the attributes and quantity of the related fulfillment asset.

DRO determines and sets the actions on the decomposed fulfillment order line items based on the changes in the attributes and quantity of the order line items.

ORDER LINE ITEM ACTION	FULFILLMENT ORDER LINE ITEM ACTION	DESCRIPTION
Add	Add	DRO sets the value and creates a fulfillment asset after the fulfillment plan is completed.
Amend	Amend	

DRO sets the value when the attribute values or quantity of the order line items related to the decomposed fulfillment order line item change.

After the plan is complete, DRO updates the fulfillment asset that's related to the fulfillment order line item.


No Change	No Change	DRO sets the value when the attribute values or quantity of the order line items that are related to the decomposed fulfillment order line item don’t change. There’s no change to the fulfillment asset.
Renew	Renew	DRO sets the value when the order line item is submitted to renew the lifecycle of a product.
Cancel	Cancel	DRO sets the value when the order line item is canceled. The relationship between the fulfillment asset and the asset is canceled.
NOTE

During order decomposition, if the enriched fulfillment order line item contains different attribute values and quantity than its fulfillment asset, then DRO sets the fulfillment order line item's action as Amend, irrespective of the action on its related order line item.

Understand order line items. See Order Line Item Actions.

=== ARTICLE: ind.dro_fulfillment_plan_actions_and_information.htm ===
---
article_id: ind.dro_fulfillment_plan_actions_and_information.htm
title: Monitor Fulfillment During Order Orchestration
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_fulfillment_plan_actions_and_information.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# Monitor Fulfillment During Order Orchestration

Act on steps or learn more about how the fulfillment process is progressing directly from the orchestration plan.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

You can see the entire process of an order from the orchestration plan. Search for steps, see their dependencies, and even change their status.

The Plan as a Whole

An orchestration plan shows you the fulfillment steps and their dependencies. You can see at a glance the state of each step, their dependencies, and even whether they're on time. You can quickly see whether a step has finished, is still pending, or has failed. Large orchestration plans load partially with options to add more steps to the plan viewer and to show them everything at once.

Plan States

Orchestration plans are generated and executed based on the submitted order and their states change as the fulfillment process progresses:

Not Started: The plan has not yet begun.
In Progress: The plan is currently running.
Freezing: The plan is paused but one or more steps in the plan are in progress. You can’t submit in-flight change requests when the plan is in a Freezing state.
Frozen: All steps in the plan are completed or in a Pending state. To amend or cancel an in-flight order, the plan must be in this state.
Completed: The entire plan has successfully finished.
Search for a Step

To find a step, enter a term in the Search field. The step is highlighted and you're brought directly to the term in the plan. You can also zoom the plan in or out, and refresh the plan as fulfillment progresses.

To see a list of filtered steps, click . To filter the steps by category, click a category:

Manual Tasks: Act on tasks or learn more about the upcoming and overdue tasks directly from the order details page.
Fatally Failed
In Progress
Pending
At Risk (this tab appears only if a step is at risk)
See the Details of the Step

Click  on a step to open a panel that shows information about the step.

The Details tab: See general information about the step, including the Execute On rule that defines when the step runs.
The Step Dependencies tab: See the dependencies related to the step. Click a dependency to highlight it in the plan.

To highlight a step's dependencies, hover over the step.

Act on the Step

Click  on a step to see various actions that you can take, such as marking a step as complete, or retrying an auto task or callout. If you can't take an action, then the button isn't available.

View the Cross-Plan Dependencies

Click  on a step to open the panel showing the External Dependencies tab. See the external step dependencies related to the step. Click a step or plan to open its details page, and take actions such as edit or complete a step.

NOTE The External Dependencies icon appears only if there is at least one external dependency.

Choose the Cross Plan scope when you're defining the dependency between step groups. See Set Dependencies Between Fulfillment Steps and Cross-Plan Dependencies.

Fulfillment State

Depending on their state, steps are different colors. For example, the green steps are in the Completed state, and the blue ones are in the Pending state. The state of a step is also written on the step.

The Jeopardy and SLA Clock: 

The color of the clock indicates whether a step is running on time (blue), late (orange), or is overdue (red). If the step is already completed, then the color indicates whether it was completed on time, in jeopardy, or late.

To see more details, hover over .

SEE ALSO
Monitor Decomposition During Fulfillment
Configure Fulfillment Step Jeopardy Rules
Set Dependencies Between Fulfillment Steps
Cross-Plan Dependencies

=== ARTICLE: ind.dro_fulfillment_step_states.htm ===
---
article_id: ind.dro_fulfillment_step_states.htm
title: Fulfillment Step States
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_fulfillment_step_states.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# Fulfillment Step States

As steps progress through the fulfillment process, you can check the fulfillment plan to see the state that the steps are in.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Table of Fulfillment Step States

STATE	MEANING
Pending	This fulfillment step is waiting for prerequisites to finish before moving to the next state.
Ready	This fulfillment step is ready to run, but hasn't started running yet. For example, it might be a manual task that no one has started working on yet.
In Progress	This fulfillment step is running.
Completed	This fulfillment step is completed.
Failed	This fulfillment step has failed and will be retried, based on the retry policy and fallout rules. Note: This state and Fatally Failed appear in the same color.
Fatally Failed	This fulfillment step has failed and the allowed number of retries, as defined in the fallout rule, have failed as well. The step won't be executed. Note: This state and Failed appear in the same color.
Skipped	This fulfillment step didn't run as planned. The conditions for the step's Execute On rule weren't met, so the step never executed.
Amended	A completed fulfillment step enters this state when a supplemental order amends the original order.
Canceled	A completed fulfillment step enters this state when a supplemental order cancels the original order.
Discarded	An incomplete fulfillment step enters this state when a supplemental order cancels the original order.
Scheduled	A future-dated fulfillment step that is waiting to run at a designated time.

=== ARTICLE: ind.dro_fulfillment_user.htm ===
---
article_id: ind.dro_fulfillment_user.htm
title: Fulfillment User
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_fulfillment_user.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Fulfillment User

A fulfillment user is the user whose permissions are used throughout the fulfillment process, unless you specify a different user at a more granular level. If you don't specifically configure a step to be run by a different user in the Run As User field, then Dynamic Revenue Orchestrator (DRO) uses the fulfillment user's permissions.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Dynamic Revenue Orchestrator uses permissions and permission sets to determine whether a user can do certain things. When you set the fulfillment user, it's like telling DRO: from now on, pretend that this is the user that submits every order.

Make sure that the fulfillment user has at least the permissions granted by DRO Admin User or Submit Transaction User, and that it has the Assetize Order permission from the Revenue Lifecycle Management permission sets.

When you design a fulfillment step, you can enter a different user in the Run As User field. For example, design a callout that runs as a user who has permissions on the external system that you call out to. If you don't specify a user on a fulfillment step, then the step runs as the fulfillment user.

SEE ALSO
Permission Sets in Dynamic Revenue Orchestrator

=== ARTICLE: ind.dro_fulfillment_viewer_page_failure.htm ===
---
article_id: ind.dro_fulfillment_viewer_page_failure.htm
title: Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_fulfillment_viewer_page_failure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.rev_cloud_upgrade_known_issues.htm
fetched_at: 2026-09-05
---

# Dynamic Revenue Orchestrator

If you set up Dynamic Revenue Orchestrator in Winter '27, understand these limitations and workaround, where applicable, to ensure a successful implementation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
Execution of Submit Sales Transaction action fails when Orchestration Group Key maps to a non-unique context definition field that returns more than the supported limit of 500 records. To fix this issue, update the context mapping for the Orchestration Group Key to point a unique field.
Clicking Launch Flow on a Manual Task step in a Fulfillment Plan or Fulfillment Step record results in an Flow Launch error, and halts the orchestration plan. As a workaround, run the screen flow manually. Then, mark the current step as Completed to resume the orchestration plan.

=== ARTICLE: ind.dro_hi_tech_order_orchestration_template.htm ===
---
article_id: ind.dro_hi_tech_order_orchestration_template.htm
title: Design Orchestration with the High Tech Order Orchestration Template
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_hi_tech_order_orchestration_template.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# Design Orchestration with the High Tech Order Orchestration Template

Use the High Tech Order Orchestration Template as a starting point for orders that combine project work, hardware assembly, software provisioning, billing, and revenue scheduling.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

The preconfigured template provides technical products, fulfillment steps, dependencies, and automations for common high tech order scenarios. To install the template, see Install the High Tech Order Orchestration Template.

The template installs these components, which you can adapt to your products and fulfillment processes.

COMPONENT	DESCRIPTION
Technical products	Billing, Project, Hardware Assembly, Tenant Provisioning, Software Provisioning, and Revenue Schedule
Fulfillment step definition groups	One group for each product. Each group contains the fulfillment steps that support delivery and revenue realization
Fulfillment step definitions	The individual steps in each group, including auto tasks, manual tasks, and assetization steps that perform the fulfillment work
Fulfillment step dependency definitions	The relationships that determine the order in which the fulfillment steps run within and across groups
Fulfillment workspace	The workspace and workspace items that organize the fulfillment steps in the workspace designer
Product fulfillment scenarios	The mappings that connect each technical product to its fulfillment step definition group
Apex classes and flows	Automations for processes such as creating billing schedules, generating invoice documents, and sending invoice emails

Adapt the products, fulfillment steps, and automations to your business processes.

How the Template Runs

To enable decomposition, create rules that map your commercial products to the technical products in the template. When an order is submitted, Dynamic Revenue Orchestrator decomposes its products into the template's technical products. The product fulfillment scenarios select the corresponding step definition groups and create a plan that preserves their dependencies.

Users complete manual tasks and milestones in the fulfillment plan. Automated tasks invoke flows for billing and invoicing. Staged assetization steps create fulfillment assets at the configured point in the plan. After invoice document generation completes, the final billing task sends the invoice document to the customer.

=== ARTICLE: ind.dro_hook_custom_logic_details.htm ===
---
article_id: ind.dro_hook_custom_logic_details.htm
title: Configure Custom Logic between Decomposition and Orchestration
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_hook_custom_logic_details.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# Configure Custom Logic between Decomposition and Orchestration

To insert custom logic into the fulfillment process between the decomposition and orchestration steps, invoke the two processes separately. The standard Submit Sales Transaction invocable action runs decomposition and orchestration processes sequentially. To decouple the processes, use the individual Decompose Sales Transaction and Orchestrate Sales Transaction invocable actions. Add your custom logic and compose the fulfillment plan with the necessary, up-to-date information. Custom logic is critical if certain data needed for specific validations or data enrichment is only available after decomposition. After the custom logic executes, trigger the Orchestrate Sales Transaction invocable action through various methods, such as custom platform events, Apex triggers, or direct flow actions.

The configuration of the flow differs depending on whether you are processing transactions synchronously or asynchronously.

NOTE Provide the same input parameter values in both the Decompose Sales Transaction and Orchestrate Sales Transaction invocable actions. For example, if allowOverrideOfPointOfNoReturn is set to true in the Decompose Sales Transaction invocable action, it must set to true for the Orchestrate Sales Transaction invocable action too.
NOTE The rollback behaviour when an error occurs depends on whether the flow runs synchronously or asynchronously.
Synchronous Rollback: An error causes both decomposition and orchestration artifacts to roll back.
Asynchronous Rollback: Successful decomposition artifacts aren't rolled back if orchestration fails, unless the error happens while composing the fulfillment plan.
Configure Custom Logic in a Synchronous Flow
When you configure the Decompose Sales Transaction and Orchestrate Sales Transaction invocable actions in a synchronous request, the flow executes the actions sequentially.
Configure Custom Logic in an Asynchronous Flow
When you configure the Decompose Sales Transaction and Orchestrate Sales Transaction invocable actions in an asynchronous request, the decomposition process runs in the background. Pause the flow until decomposition is finished before executing the custom logic and the Orchestrate Sales Transaction invocable action.

=== ARTICLE: ind.dro_how_in_flight_order_changes_decompose.htm ===
---
article_id: ind.dro_how_in_flight_order_changes_decompose.htm
title: In-Flight Order Change Example
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_how_in_flight_order_changes_decompose.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_in_flight_order_changes.htm
fetched_at: 2026-09-05
---

# In-Flight Order Change Example

To help fulfillment designers understand how in-flight order changes work, refer to this example scenario.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Dynamic Revenue Orchestrator is enabled

After in-flight changes are applied and submitted to Dynamic Revenue Orchestrator (DRO), DRO decomposes the supplemental order and generates fulfillment lines.

The fulfillment lines generated from the supplemental order include a supplemental action that records the changes compared to the actions in the fulfillment lines from the original order. The existing fulfillment plan is updated by assessing the impact of the steps that were already in the plan.

You can amend, cancel, or discard these steps, or they can remain unaffected. Additionally, the updated plan can introduce new steps or steps designed to compensate for or roll back the changes made to the amended or canceled steps.

EXAMPLE A customer, Sarah, places an order for an Office Security System Pro suite from a security company. The suite includes:
Smart Front Door Camera
Wireless Indoor Security Camera (Quantity: 2)
Motion Sensor (Quantity: 3)
Cloud Storage for 24/7 Professional Monitoring Service (1 year subscription)

Order Decomposition:

The graphic shows how Sarah's order undergoes initial decomposition. The commercial order, containing child items, is decomposed into technical products, and these technical products can be further decomposed into their own child items.

The graphic shows the fulfillment design for Sarah’s order. The Shipment Delivery step is the Point of No Return (PONR). Any changes made after the fulfillment reaches the Shipment Delivery step are rejected.

Changing the In-Flight Order

A few days after placing the order, Sarah wants an additional layer of security for the office backyard. She contacts the security company and requests to change her order.

The amendment involves:

Adding order line items: Sarah adds an Outdoor Wireless Security Camera and an additional Motion Sensor to her order.
Modifying attributes of order line items: Sarah decides to upgrade her Cloud Storage for 24/7 Professional Monitoring Service to a 2-year subscription instead of the 1 year subscription. This change modifies the subscription duration attribute of that service.

The graphic below shows the fulfillment plan for Sarah’s order. Because the fulfillment hasn’t reached the PONR  step, the supplemental order accommodates the additional camera and the updated subscription. Accordingly, the Amend Shipping Items step group is added to the plan.

Point of No Return Scenario

Let's say that the Smart Front Door Camera has progressed to the Shipment Delivery stage in the fulfillment process. According to the company's policy, after it's delivered, that line item has reached its Point of No Return (PONR). No further changes or cancellations are allowed for that specific item.

Attempting to Amend After PONR

Sarah calls the security company and wants to upgrade the Smart Front-door Camera to its next model.

The DRO representative attempts to process this change in the system. The system identifies that the Smart Front Door Camera has reached the PONR (Shipment Delivery) step. The system rejects the change because of the PONR restriction.

Override PONR Facility

However, the security company has an Override PONR facility for exceptional cases. In this case, the DRO representative, after getting approval from a supervisor, uses the Override PONR functionality that helps the representative bypass the PONR restriction. The system then processes the amended request for the Smart Front Door Camera.

Outcome

Even though the Smart Front Door Camera had reached PONR, the Override PONR facility helped the security company accommodate Sarah's request. DRO updates the fulfillment plan to reflect the cancellation, and any necessary reverse logistics or adjustments are initiated.

=== ARTICLE: ind.dro_import_a_fulfillment_step_definition_group.htm ===
---
article_id: ind.dro_import_a_fulfillment_step_definition_group.htm
title: Import a Fulfillment Step Definition Group
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_import_a_fulfillment_step_definition_group.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# Import a Fulfillment Step Definition Group

To help scale your fulfillment plans, and ensure consistency across plans, you can import your existing fulfillment step definition groups directly from a fulfillment workspace.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To import a fulfillment step definition group:	

Fulfillment Designer

OR

DRO Admin User

From the Fulfillment Workspace, import groups that contain fulfillment step definitions. You can either import a group based on its name, or import the group based on its associated fulfillment scenario.

From the App Launcher, find and select Fulfillment Workspaces.
Click the workspace that you want to import a group to.
Click Import Step Group.
The Import Step Group pane opens.
From the Import Step Group pane, click one of these options and click Next:
Step Definition Group List: Search from a list of step definition groups, select the step definition goups that you want to add to the workspace, then save your work.
Step Definition Scenario: Search from a list of product fulfillment scenarios. Each scenario is associated with a step definition group. Select the scenarios that are associated with the groups that you want to add to the workspace, then save your work.
NOTE Regardless of the option that you choose, one or more step definitions groups are added to the workspace. If the group is associated with a product fulfillment scenario, then that relationship is maintained.

=== ARTICLE: ind.dro_in_flight_order_changes.htm ===
---
article_id: ind.dro_in_flight_order_changes.htm
title: In-Flight Order Changes
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_in_flight_order_changes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# In-Flight Order Changes

Sometimes customers request modifications to their orders after the order is submitted for fulfillment by the sales rep. Modifications can include changing the entire order, specific line items, or even canceling part or all of the order. Changes that happen during fulfillment are called in-flight order changes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Dynamic Revenue Orchestrator is enabled

Dynamic Revenue Orchestrator (DRO) accepts amended or canceled in-flight orders, decomposes the orders, reconciles changes, updates the orchestration plan, and runs the plan until fulfillment is complete.

Amending In-Flight Orders

Changes to an ongoing order, such as adjusting the provisioning date, adding order line items, and modifying certain attributes of the order line items, are referred to as in-flight order amendments.

Canceling In-Flight Orders

Reversing the purchasing decision or requesting to remove certain line items from the order is called canceling in-flight orders.

Point of No Return (PONR)

In the order fulfillment process, a critical stage is Point of No Return (PONR). This milestone marks the point in the fulfillment of a line item beyond which no amendments or cancellations can be made.

When sales reps change in-flight orders, the system identifies the line items that have reached PONR. Sales reps can then make informed decisions about how to proceed with honoring the customer's request.

Considerations for Changing In-Flight Orders
When you set up Dynamic Revenue Orchestrator (DRO) for in-flight order changes, it's important to understand exactly how DRO handles those changes.
Configure Inflight Plan Settings for a Fulfillment Step
As part of creating fulfillment steps, you can configure inflight plan settings to handle customer requests to add, amend, cancel, or otherwise change their order before the order is committed by a sales rep.
Point of No Return State Propagation
After an order item reaches Point of No Return (PONR), you can’t cancel or amend the order. When a PONR-marked fulfillment step transitions to an In Progress status, the PONR state change applies to the related commercial and technical products within the bundle, depending on the product type.
In-Flight Order Change Example
To help fulfillment designers understand how in-flight order changes work, refer to this example scenario.

=== ARTICLE: ind.dro_install_hi_tech_order_orchestration_template.htm ===
---
article_id: ind.dro_install_hi_tech_order_orchestration_template.htm
title: Install the High Tech Order Orchestration Template
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_install_hi_tech_order_orchestration_template.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Install the High Tech Order Orchestration Template

Install the preconfigured High Tech Order Orchestration Template from Salesforce Go. Use its products, fulfillment steps, dependencies, and automations as a starting point for common high tech order scenarios.

REQUIRED EDITIONS
Available in: Developer, Enterprise, and Unlimited Editions
USER PERMISSIONS
NEEDED
To configure Dynamic Revenue Orchestrator and install the High Tech Order Orchestration solution by using Salesforce Go:	DRO Admin USer

Before installing the template, review your existing billing-schedule and assetization automations. The template includes automations for these processes, which can cause duplicate processing.

NOTE After it’s installed, you can’t uninstall a Salesforce Go solution.
Configure Dynamic Revenue Orchestrator in Salesforce Go. Skip this step if it’s already configured.
From Setup, in the Quick Find box, enter Salesforce Go, and then select Salesforce Go.
Go to the Features tab, and filter by Revenue Cloud.
View and turn on Dynamic Revenue Orchestrator.
The configuration can take a few minutes. Wait until it’s complete before installing the template.
Turn on Billing. For more information, see Turn On Billing in Revenue Management.
Install the High Tech Order Orchestration solution in Salesforce Go.
From Setup, in the Quick Find box, enter Salesforce Go, and then select Salesforce Go.
Select Revenue Cloud and then filter by the Data Packs content type.
Open High Tech Order Orchestration, and review the solution details and installation requirements.
Click Set Up.
To monitor the configuration status, in Setup, find and select Go Accelerate, and then click Solution Deployment Monitoring.
Salesforce Go assigns the solution permissions, validates the solution, and installs the metadata and data.
The complete solution installs six technical products, one fulfillment workspace, product fulfillment scenarios, fulfillment step groups and definitions, dependencies, and supporting automations.
SEE ALSO
Design Orchestration with the High Tech Order Orchestration Template

=== ARTICLE: ind.dro_monitor_decomposition_during_fulfillment.htm ===
---
article_id: ind.dro_monitor_decomposition_during_fulfillment.htm
title: Monitor Decomposition During Fulfillment
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_monitor_decomposition_during_fulfillment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# Monitor Decomposition During Fulfillment

After a user submits an order to Dynamic Revenue Orchestrator (DRO), you can see how products decompose and can spot issues right away.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To monitor decomposition:	

DRO Admin User

OR

Fulfillment Manager/Operator

The Decomposition Viewer shows how fulfillment order items decompose, so you can validate the correctness of order decomposition and troubleshoot fallout.

From the App Launcher, find and select Dynamic Revenue Orchestrator.
From the app navigation menu, select Orders.
Click an order, then on the order page, click the Fulfillment Lines tab.
The list of order and decomposed products appears. When time-awareness is turned on, the items are sorted by product and time segment. Child products grouped under their parent in the bundle hierarchy. The Subaction column identifies the operation applied to an order or decomposed product during decomposition, such as Rollback, Field Amendment, or Start Date Adjustment.
To find the product that you want, scroll or enter a term in the Search field, and then perform one of these actions:
To see how the product decomposes, or what products decompose to the one you selected, click .
To see the decomposition rule that's in effect, as well as the product's attribute names and field values, click .
To understand the reason for the action on the decomposed product, click  in the Action column of a Decomposed Product.
Actions are assigned to order products when an order is submitted. The actions required to fulfill the order are listed in the corresponding decomposed product actions. The reasons explain the impact of order products on ‌related decomposed product actions and why decomposition is proceeding in a particular way.
To view the order products and enrichment rules that led to the action on the decomposed product, click the links on the Reason for Action window.
Use this information to troubleshoot and optimize your decomposition process.
Click View Orchestration Plan to see the orchestration plan.

=== ARTICLE: ind.dro_orchestrate_a_business_process.htm ===
---
article_id: ind.dro_orchestrate_a_business_process.htm
title: Dynamic Revenue Orchestrator for Business Processes
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_orchestrate_a_business_process.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Dynamic Revenue Orchestrator for Business Processes

Use Dynamic Revenue Orchestrator (DRO) to design and orchestrate any object regardless of whether is is based on a sales transaction. Review the differences between sales transaction-based and non-sales transaction-based business process orchestration setup.

REQUIRED EDITIONS
Available in: both Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
FEATURE	SALES TRANSACTION BUSINESS PROCESS	NON-SALES TRANSACTION BUSINESS PROCESS
Sample use cases	Quote to Order, Order to Cash, Incidents, Cases, Service Requests	Dunning Process, Obligations Management, Compliance Verification
Primary goal	Streamline the standard sales-to-service lifecycle	Streamline the pre and post-sale workflows
Object origin	Derived from the Product2 object	Independent of Product2 object. For example, Collection Plan or Obligations.
Context definition	Extends Sales Transaction context definition	Defines a custom context definition or extends a standard context definition, such as Billing, with the required mapping.
Orchestration type	Predefined Sales Transaction usage type	Predefined Generic Orchestration Type
NOTE Dynamic Revenue Orchestrator supports multiple rule libraries based on the plan usage type. The system identifies the correct library using specific API naming conventions: DRORuleLibrary for the default fulfillment plan usage type, and DRORuleLibrary[UsageTypeName] for others. If your existing default rule library uses an API name other than DRORuleLibrary, create a new library with the API name DRORuleLibrary and migrate your rules to it. Failure to do so prevents you from creating, editing, or executing rules.

=== ARTICLE: ind.dro_orchestrate_non_sales_transaction_business_processes.htm ===
---
article_id: ind.dro_orchestrate_non_sales_transaction_business_processes.htm
title: Orchestrate Non-Sales Transaction Business Processes
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_orchestrate_non_sales_transaction_business_processes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_orchestrate_a_business_process.htm
fetched_at: 2026-09-05
---

# Orchestrate Non-Sales Transaction Business Processes

Dynamic Revenue Orchestrator (DRO) orchestrates objects even if they aren't based on sales transactions. For example, you can orchestrate the dunning processes by using DRO to trigger personalized workflows based on customer segments. DRO can orchestrate obligations to track and fulfill post-sale milestones like delivery or service level agreements.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
USER PERMISSIONS NEEDED
To orchestrate a non-sales transaction business processes:	

Submit Transaction and Orchestrate User

and

Submit Transactions User

and

Permission sets specific to the object to orchestrate

Let's design a workflow to orchestrate for a non-sales transaction-based business process.

NOTE
The usage type of the orchestration components you use in the fulfillment plan should be the same as the orchestration type selected in the Orchestration Plan Context Mapping entry.
Add the Usage Type field to the fulfillment scenario, fulfillment step definition groups, fulfillment step definitions, and fulfillment dependencies record pages if it isn't already present.
DRO accepts any context definition and isn't restricted to the sales transaction context definition. You can create a context definition or use an existing context definition. Map the attributes in the context definition to fields of the object you want to orchestrate. See Custom Context Definition to Orchestrate a Non-Sales Transaction Business Processes.
Create an Orchestration Plan Context Mapping entry to associate the context definition to the orchestration logic within DRO. See Create Orchestration Plan Context Mapping. Use the Generic Orchestration Type that is provided out-of-the-box from DRO to orchestrate non-sales transaction objects.
Create a fulfillment workspace and generate an orchestration plan with fulfillment step definitions groups, fulfillment steps, and fulfillment dependencies. Select the Plan or Item dependency scope when creating fulfillment dependencies. Other scopes are not valid for this orchestration.
Create a fulfillment scenario to link the object with the correct orchestration plan. To determine selection of the appropriate scenario during fulfillment, define conditions. See Define Orchestration Plan Components.
To show the orchestration plan's submission status and fulfillment progress on the object page, configure the orchestration plan summary component.
To initiate orchestration, submit the order to DRO by using the Orchestrate Transaction invocable action. See Dynamic Revenue Orchestrator Standard Invocable Actions .

=== ARTICLE: ind.dro_orchestrate_non_sales_transaction_business_processes_context.htm ===
---
article_id: ind.dro_orchestrate_non_sales_transaction_business_processes_context.htm
title: Considerations for Creating a Non-Sales Transaction Context Definition
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_orchestrate_non_sales_transaction_business_processes_context.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_orchestrate_non_sales_transaction_business_processes.htm
fetched_at: 2026-09-05
---

# Considerations for Creating a Non-Sales Transaction Context Definition

To orchestrate a non-sales transaction business process, create a context definition and map it to the fields of the object to orchestrate. You can also extend an existing context definition by adding a mapping to the object that you want to orchestrate. Keep these considerations in mind when creating a custom context definition and its mapping.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
USER PERMISSIONS NEEDED
To create or extend the context definition:	DRO Admin User

Prerequisite: Enable Permission for Context Service Users.

See Context service.

Define one root node for your object. To orchestrate a collection like a Collection Plan object with multiple items, add child item nodes.
Define an Id attribute for root and child nodes (if applicable). The Id is used to identify the record to orchestrate. Map the Id attribute to the object's Id field.
Define the StartDate attribute used to schedule the fulfillment steps.
To show an identifiable label for the context definition, define a Name attribute . Otherwise, the record Id is shown.
Generate tags for all the attributes.
Add appropriate mappings with the root and child nodes mapped to their respective object fields based on your use case, and activate the context definition.
NOTE
For every attribute tag in a rule condition, define a corresponding object field mapping to prevent execution failures during rule evaluation or fulfillment.
To maintain data consistency across the orchestration lifecycle and to provision multiple mappings, map all the root nodes and applicable child nodes to their respective objects.

=== ARTICLE: ind.dro_orchestrate_non_sales_transaction_mapping.htm ===
---
article_id: ind.dro_orchestrate_non_sales_transaction_mapping.htm
title: Requirements for Creating Orchestration Plan Context Mapping
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_orchestrate_non_sales_transaction_mapping.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_orchestrate_non_sales_transaction_business_processes.htm
fetched_at: 2026-09-05
---

# Requirements for Creating Orchestration Plan Context Mapping

Create an orchestration plan context mapping entry to connect the business data in an object to the orchestration logic within Dynamic Revenue Orchestrator (DRO) by using the orchestration type. DRO includes the Generic orchestration type to orchestrate non-sales transaction objects.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To create the custom context definition:	DRO Admin User

Keep these considerations in mind when creating a mapping.

Create one mapping entry for a specific object for DRO to orchestrate.
Map an orchestration type to only one context definition to maintain an exclusive relationship between the orchestration process and its logic.
Use the same orchestration type while creating the mapping as the usage type of the orchestration components.

Create the Orchestration Plan Context Mapping entry using these fields:

FIELD NAME	REQUIREMENT	DESCRIPTION
Object Name	Mandatory	The API name of the object for orchestration.
Context Definition	Mandatory	The context definition to be used for the object.
Context Mapping	Mandatory	The name of the context mapping to apply.
Root Node Name	Mandatory	The node name that represents the root in the context definition.
Item Node Name	Optional	The node name that represents an item in the context definition.
Orchestration Type	Mandatory	Select Generic orchestration type.

=== ARTICLE: ind.dro_orchestrate_sales_transaction_business_processes.htm ===
---
article_id: ind.dro_orchestrate_sales_transaction_business_processes.htm
title: Orchestrate Sales Transaction Business Processes
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_orchestrate_sales_transaction_business_processes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_orchestrate_a_business_process.htm
fetched_at: 2026-09-05
---

# Orchestrate Sales Transaction Business Processes

Set up a workflow to orchestrate business processes such as Quote to Order, Order to Cash, Incidents, Cases, Service Requests, and custom objects. First, extend the Sales Transaction context definition. Then, clone and save the required mapping, update the mapping to link the Sales Transaction node attributes to your business object's fields, create a procedure plan definition and associate it with the new context definition, and then configure the new context definition for the Sales Transaction Context Definition. Finally, submit the business process for orchestration.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
USER PERMISSIONS NEEDED
To orchestrate business processes:	

Fulfillment Designer

OR

DRO Admin

Before you begin, align your business process with the predefined sales transaction context that’s used to map sales transactions to objects such as Quote, Asset, and Order. See Create Custom Context Definitions for Order Orchestration.

Extend the sales transaction context definition into a new context definition, map your object, to the new context definition, and activate the context definition. On the Context Definition Settings page, configure the activated context definition for the Sales Transaction context definition. See Create Custom Context Definition and Map Business Objects.
This step makes sure that the necessary data is retrieved throughout the various orchestration phases as steps progress.
Create a procedure plan definition for your business process and associate it with the new context definition.
Finally, submit your business process for orchestration. See Submit Sales Transaction Action.
Use the default StandardOrder adapter for submitting orders and the GenericAdapter for submitting any other business process for orchestration.
EXAMPLE A customer, Jones, places a service request for an electrical meter connection at their office. Here's how Dynamic Revenue Orchestrator (DRO) orchestrates the service request.

Step 1: Create Custom Objects

This step is necessary only if you are orchestrating a custom service request that can’t be processed using the out-of-the-box entities. Delivered objects generally have the capability to perform the necessary orchestration.

To effectively manage and track this custom service request, you must first set up these required custom objects in your Salesforce org.

CUSTOM OBJECT	CUSTOM OBJECT ROLE
Service Request	Captures the details of the customer's request for an electrical connection and stores information such as customer details, service location, requested service date, and status.
Service Request Item	Represents a specific item or component. A single service request can involve multiple items. For an electrical connection, service request items can include digging the service trench, connecting to the power grid, and testing the electrical panel.
Service Request Action	Tracks the various actions or tasks that must be completed to orchestrate the service request. Service request actions can include scheduling the site visit, dispatching a technician, installing the meter, and activating the connection.
Service Request Item Attribute	Stores additional attributes or details about the items involved in the service request. For example, for a meter installation, attributes can include the meter type, serial number, and voltage rating.
Service Request Item Relationship	Captures the relationships between different items or components of the service request. For example, the relationship can link the meter installation task to the specific meter that's installed.

Step 2: Extend the Sales Transaction Context Definition and Map the Service Request Entity

Next, extend the standard Sales Transaction context definition and name it DROServiceRequest. This extension helps you to include service-specific data in the orchestration process.

Now, map the fields of the Service Request object to the extended DROServiceRequest context definition. This mapping makes sure that the necessary service request data is available during the orchestration process.

You must map attributes such as Customer ID to ServiceRequest field’s CustID and Request Date to ServiceRequest field’s ReqDt.

Step 3: Create a Procedure Plan Definition

In this step, select the Service Request object as the primary object and associate it with the DROServiceRequest context definition. This procedure plan definition identifies the context definition that orchestrates the service request.

Step 4: Submit the Service Request for Orchestration

Finally, submit the service request for orchestration by using the Submit Sales Transaction invocable action. This action triggers the orchestration of the business object.

By processing these steps, DRO makes sure that the decomposition, plan composition, and plan execution occur in the correct sequence, ultimately creating a sales transaction fulfillment request to efficiently manage the electrical connection service. See Design Your Order Decomposition.

=== ARTICLE: ind.dro_order_line_item_actions.htm ===
---
article_id: ind.dro_order_line_item_actions.htm
title: Order Line Item Actions
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_order_line_item_actions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Order Line Item Actions

When an order is submitted, each line item gets an action, such as Add and Amend. Learn about what these actions mean in Dynamic Revenue Orchestrator.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
Order Line Item Actions
Add: The item is added to the order. This is the most common action for a new order.
Amend: A supplemental order is submitted, changing this item in some way from the original order.
Renew: An order is submitted to renew the lifecycle of a product.
NoChange: There's no change at all to the item.
Cancel: The item is canceled and isn't to be fulfilled.

=== ARTICLE: ind.dro_order_submission_to_dro.htm ===
---
article_id: ind.dro_order_submission_to_dro.htm
title: Automate Order Submission to Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_order_submission_to_dro.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_basic_set_up.htm
fetched_at: 2026-09-05
---

# Automate Order Submission to Dynamic Revenue Orchestrator

Create a record-triggered flow that automatically submits Revenue Management (formerly Revenue Cloud) orders to Dynamic Revenue Orchestrator when the orders are activated.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management

To set up the flow and filter for Revenue Management records, see Automate Asset Creation from Orders. After you configure the flow and its decision paths, add the submission action.

In the Revenue Management Record branch, click .
Find and select Action.
In the New Action dialog box, specify these details.
Select Submit Order as the action.
For Label, enter Submit Order Action.
For API Name, enter Submit_Order_Action.
Select Prior Values of Triggering Order > Order ID as the order ID.
Click Done.
Save your work.
Enter a label and API name for the flow, and then save your changes.
Activate the flow.
Add an Action to Submit Orders to Dynamic Revenue Orchestrator

To identify and handle incomplete steps in the fulfillment plan before amending the asset, use the Submit Order with Validation flow. See Handle Conflicts During Asset Date Amendments by Using Submit Order with Validation Flow.

To call the decomposition and orchestration processes individually, use the Decompose Sales Transaction and Orchestrate Sales Transaction invocable actions. See Dynamic Revenue Orchestrator Standard Invocable Actions.

To add the Fulfillment Plan and Orchestration Submission Status fields, edit order page layouts. See Customize Page Layouts with the Enhanced Page Layout Editor.

This completes the basic setup for Dynamic Revenue Orchestrator.

To enable other features, see Dynamic Revenue Orchestrator Advanced Setup.

To proceed with the rest of the Revenue Management setup, see Set Up Revenue Management.

=== ARTICLE: ind.dro_permission_sets_in_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_permission_sets_in_dynamic_revenue_orchestrator.htm
title: Permission Sets in Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_permission_sets_in_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_permissions_in_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Permission Sets in Dynamic Revenue Orchestrator

A permission set is a collection of settings and permissions that give users access to various tools and functions. Permission sets extend the functional access of the users without changing their profiles and are the recommended way to manage user permissions.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
Create Users and Profiles

To begin, create users for Dynamic Revenue Orchestrator (DRO). Then assign users the appropriate permission sets. To help you plan, refer to the list of permission sets in DRO. Users must have create, read, update, and delete permissions for orders.

When you create a user, you must also assign a profile. Profiles define default settings for users. Some organizations create their own profiles, while others choose to use profiles included with Salesforce.

Remember, users can have only one profile, but can have many permission sets assigned to them.

Permission Sets in Dynamic Revenue Orchestrator
DRO Admin User: Gives access to the DRO app settings and all of its entities. This permission alone doesn't allow a user to submit an order.
Submit Transactions and Fulfillment User: Submit orders to DRO and call the invocable submitOrder action. Typically, users assigned this permission set perform order decomposition, plan composition, and plan execution.
NOTE To ensure that products are automatically assetized at the end of fulfillment, the user that submits the order must have the Assetize Order permission from the Revenue Lifecycle Management permission sets.
Submit Transactions User: Submit transactions to DRO and call the invocable actions. This permission set allows users to submit transaction requests, but doesn’t provide access to any design or fulfillment tasks. See: Fulfillment User
Fulfillment Designer: Gives access to all design time entities and interfaces that you require to configure products, decomposition rules, fulfillment plans, and scenarios.
Submit Transactions and Orchestrate User: Submit transactions to DRO. This permission set doesn’t include product and order permissions. With this permission set along with the Submit Transactions User permission set, users can orchestrate non-sales transactions.
Fulfillment Manager/Operator: Gives Read access to all DRO objects.
SEE ALSO
View and Manage Users
Create or Clone Profiles
View and Manage Your Permission Set Licenses

=== ARTICLE: ind.dro_permissions_in_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_permissions_in_dynamic_revenue_orchestrator.htm
title: Permissions in Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_permissions_in_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_basic_set_up.htm
fetched_at: 2026-09-05
---

# Permissions in Dynamic Revenue Orchestrator

Review the permissions required for Dynamic Revenue Orchestrator.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
Permission Sets and Users
Permission Sets in Dynamic Revenue Orchestrator
Manage Permission Set Assignments
Fulfillment User

=== ARTICLE: ind.dro_point_of_no_return_state_propagation.htm ===
---
article_id: ind.dro_point_of_no_return_state_propagation.htm
title: Point of No Return State Propagation
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_point_of_no_return_state_propagation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_in_flight_order_changes.htm
fetched_at: 2026-09-05
---

# Point of No Return State Propagation

After an order item reaches Point of No Return (PONR), you can’t cancel or amend the order. When a PONR-marked fulfillment step transitions to an In Progress status, the PONR state change applies to the related commercial and technical products within the bundle, depending on the product type.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Dynamic Revenue Orchestrator is enabled

Here’s how the PONR state propagates to the associated items within the product bundle.

PRODUCT ITEM TYPE IN PONR STATE	PROPAGATES PONR STATE TO PRODUCT ITEM TYPE
Commercial product parent item	All commercial product child items
Commercial product child item	Commercial product parent item
Technical product parent item	
All technical product child items
All commercial product items associated directly as well as through technical child items
Technical product parent item
All commercial product items associated directly as well as through the technical product parent item
Step Status Changes from Supplemental Actions

Here’s how step statuses change when supplemental actions are applied to in-flight orders.

NEW SUPPLEMENTAL ACTION APPLIED TO SUPPLEMENTAL ORDER	STATUS FOR APPLYING THE ACTION	CHANGE IN STEP STATUS
Add	Pending	—
Amend	

Pending

Completed

Skipped

Scheduled

Failed (applies only to the Callout and Autotask steps)

Fatally Failed (applies only to the Callout and Autotask steps)

	

—

Amended

—

Pending

Failed

Fatally Failed


Cancel	

Pending

Completed

Scheduled

Skipped

Failed (applies only to the Callout and Autotask steps)

Fatally Failed (applies only to the Callout and Autotask steps)

Canceled

	

Discarded

Canceled

Discarded

Discarded

Discarded (applies only to the Callout and Autotask steps)

Discarded (applies only to the Callout and Autotask steps)

No change (All compensation steps)


No Change	

Pending

Scheduled

Completed

Failed

Fatally Failed

Skipped

Amended

Canceled

	

—

—

—

—

—

—

No change (All compensation steps)

No change (All compensation steps)

Actions Not Applicable to Step Statuses

Here are the actions that aren’t applied to the steps that are in these statuses:

ACTION	STEP STATUSES WHEN THE ACTION ISN'T APPLIED
Amend	Ready, In Progress, Failed, Fatally Failed, Amended, Discarded, and Canceled
No Change	Ready, In Progress, Amended, Discarded, and Canceled
Cancel	

Ready, In Progress, Amended, Discarded, Canceled, Failed, and Fatally Failed

Failed and Fatally Failed (applies only to the Callout and Autotask steps)

=== ARTICLE: ind.dro_ramp_deal_decomposition.htm ===
---
article_id: ind.dro_ramp_deal_decomposition.htm
title: Decompose and Fulfill Ramp Deal Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_ramp_deal_decomposition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm
fetched_at: 2026-09-05
---

# Decompose and Fulfill Ramp Deal Orders

Use Dynamic Revenue Orchestrator (DRO) to decompose, orchestrate, and assetize ramp deal orders across time segments. DRO sequences fulfillment steps, creates fulfillment assets, and processes amendments based on each segment's effective dates and values. A ramp deal contains standalone order line items divided into time segments whose price, quantity, discount, and other attributes can vary.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
Decompose Ramp Deal Orders

DRO decomposes each ramp segment into fulfillment order line items (FOLIs). The subscription, term, and quantity defined in a segment determine the FOLIs generated for that period. When time-awareness is on, DRO maps the FOLIs and Fulfillment Asset State Period records to each segment's effective dates. As a result, a change to one segment updates only that period.

For more information about time-aware behavior, see Order Fulfillment With Time-Awareness.

Orchestrate Ramp Deal Fulfillment

DRO sequences fulfillment steps chronologically across ramp segments according to the configured dependencies and scopes. For example, steps for the first year run before steps for the second year. DRO also resolves dependencies across time segments to prevent fulfillment plans from stalling and to support multiyear subscription provisioning. To sequence fulfillment across ramp segments, configure the fulfillment steps and dependencies with the scopes required by your fulfillment design. The configured scopes determine which fulfillment order line items a step processes and how dependencies connect steps within and across segments.

For more control over execution timing, see Configure Steps for Future Execution.

Assetize Ramp Deal Orders

Assetize Ramp Deal Orders DRO handles assetization for ramp deal orders based on whether time awareness is on.

When time awareness is on, DRO constructs a fulfillment asset timeline using each ramp segment's effective dates and values. It creates a Fulfillment Asset State Period (FASP) for every segment using its corresponding fulfillment order line item as the source. If an amendment alters the order timeline, DRO supersedes the affected FASPs and creates updated FASPs to reflect the new dates, quantities, and attributes.

When time awareness is off, DRO processes fulfillment order line items using standard, time-agnostic assetization rules without constructing a FASP timeline. Segment effective dates do not establish separate asset state periods.

By using a staged assetize step, DRO creates assets during fulfillment plan execution rather than waiting until the plan fully completes. This step keeps asset creation aligned with delivery and revenue-recognition schedules for multiyear deals. The staged assetize step supports ramped products sourced from order line items or fulfillment order line items. DRO uses the product's ramp segments as source line items to create assets and asset state periods during execution.

Staged assetization of ramp segments is supported only for time-aware fulfillment assets. Commercial assetization requires all segments of a multisegment ramp to be assetized together. For source behavior, limitations, and setup information, see Staged Assetize Step.

Amend Ramp Deal Assets

When you amend a ramped asset, DRO detects time-based changes, generates fulfillment order line items with the applicable actions, and updates the related fulfillment assets during technical assetization. You can make these changes to a ramped asset:

Add one or more segments during an amendment. A new segment can retain the quantity and attributes of the previous segment or use different values.
Cancel the last segment or multiple future segments. Cancellation sets the quantity of each canceled segment to 0. You can't cancel a segment that falls between two existing segments.

DRO fulfills these amendments whether or not time-awareness is on.

For information about how additions, cancellations, and other dated changes affect fulfillment assets, see Considerations for Backdated Changes in Dynamic Revenue Orchestrator.

=== ARTICLE: ind.dro_retry_or_complete_multiple_failed_fulfillment_steps.htm ===
---
article_id: ind.dro_retry_or_complete_multiple_failed_fulfillment_steps.htm
title: Retry or Complete Multiple Failed Fulfillment Steps
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_retry_or_complete_multiple_failed_fulfillment_steps.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# Retry or Complete Multiple Failed Fulfillment Steps

From a list view or queue, retry or complete multiple steps at once. If you complete a step in this way, the step ignores any errors that can otherwise stop the completion of the step.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To view and edit fulfillment:	

Fulfillment Manager/Operator

OR

DRO Admin User

Complete and Retry buttons are available only if the Fallout and SLA Settings setting is turned on.

Sometimes a number of fulfillment steps fail because a system is down. When the system comes back online, the fulfillment designer can bulk retry the steps that failed, or mark the steps complete, rather than addressing them one at a time.

From the App Launcher, find and select Fulfillment Steps.
From the App Launcher, find and select Fulfillment Steps.
Select the list view for the queue that contains the failed steps, or select the Fatally Failed Fulfillment Steps list view.
Select the relevant steps, and then click Retry or Complete.
NOTE You can retry a step if it's in the Failed or Fatally Failed state and the plan is in the In Progress state.

You can complete a step if the plan is in the Freezing state and the step is in the In Progress state, or the plan is in the In Progress state and the step is in either the In Progress, Failed, or Fatally Failed state.

If you select some items that are eligible to be retried or completed, and others that aren't, then only the eligible ones are successful.

=== ARTICLE: ind.dro_run_time_administration.htm ===
---
article_id: ind.dro_run_time_administration.htm
title: Submit Orders for Decomposition and Order Fulfillment
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_run_time_administration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# Submit Orders for Decomposition and Order Fulfillment

Sales reps submit orders to Dynamic Revenue Orchestrator (DRO) for decomposition and fulfillment. During run time, fulfillment operators can track the decomposition and orchestration plans for submitted orders.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
Create and Submit an Order
Sales reps submit simple or bundled product orders in Dynamic Revenue Orchestrator (DRO) for decomposition and to instantiate the orchestration plan.
Monitor Decomposition During Fulfillment
After a user submits an order to Dynamic Revenue Orchestrator (DRO), you can see how products decompose and can spot issues right away.
Order Fulfillment With Time-Awareness
Manage complex, multi-year subscription lifecycles by using time-awareness in fulfillment assets. Instead of using a static snapshot of an asset, time-awareness aligns orchestration with the effective dates of each change, so that additions, cancellations, and renewals of backdated and future-dated orders update only the assets that change in that period.
Monitor Fulfillment During Order Orchestration
Act on steps or learn more about how the fulfillment process is progressing directly from the orchestration plan.
Fulfillment Step States
As steps progress through the fulfillment process, you can check the fulfillment plan to see the state that the steps are in.
View Fulfillment Step History
Monitor the changes to a fulfillment step, such as status modifications, on its detail page by using the Fulfillment Step History related list.
Retry or Complete Multiple Failed Fulfillment Steps
From a list view or queue, retry or complete multiple steps at once. If you complete a step in this way, the step ignores any errors that can otherwise stop the completion of the step.
Handle Conflicts During Asset Date Amendments by Using Submit Order with Validation Flow
It's common to request adjustments to license subscription start dates, either moving them earlier if your users are ready to use them or delaying them if they are not. However, if the order that created the asset has incomplete steps in its fulfillment plan, submitting an asset amendment can result in two orders updating the asset simultaneously. Identify and handle incomplete steps in the fulfillment plan by using the Submit Order with Validation flow.
Configure Custom Logic between Decomposition and Orchestration
To insert custom logic into the fulfillment process between the decomposition and orchestration steps, invoke the two processes separately. The standard Submit Sales Transaction invocable action runs decomposition and orchestration processes sequentially. To decouple the processes, use the individual Decompose Sales Transaction and Orchestrate Sales Transaction invocable actions. Add your custom logic and compose the fulfillment plan with the necessary, up-to-date information. Custom logic is critical if certain data needed for specific validations or data enrichment is only available after decomposition. After the custom logic executes, trigger the Orchestrate Sales Transaction invocable action through various methods, such as custom platform events, Apex triggers, or direct flow actions.

=== ARTICLE: ind.dro_set_dependencies_between_fulfillment_steps.htm ===
---
article_id: ind.dro_set_dependencies_between_fulfillment_steps.htm
title: Set Dependencies Between Fulfillment Steps
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_set_dependencies_between_fulfillment_steps.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_orchestration.htm
fetched_at: 2026-09-05
---

# Set Dependencies Between Fulfillment Steps

Connect fulfillment step definitions to create a dependency between them. When an order is submitted, the steps run in the order that you define.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To set dependencies between fulfillment steps:	

Fulfillment Administrator

OR

Fulfillment Designer

IMPORTANT If you set up dependencies that result in a loop, the entire fulfillment process is at risk of failing. For example, if you make Step A dependent on Step B, and then make Step B dependent on Step A, you have a loop.

The Fulfillment Workspace arranges the step definitions in the order that they're completed when an order is submitted.

To create a dependency between steps, follow these instructions.

From the App Launcher, find and select Fulfillment Workspaces.
On the step definition that must finish first, click .
On the step definition that must finish last, click .
Select the Dependency Scope.
For steps in the same plan that follow a standard hierarchy, match the dependency scope to the scope of the depends-on step.
For steps in different plans, select Cross Plan.
For steps that are grouped by a business value, select Custom. Then, in Custom Scope, select an existing custom fulfillment scope.
To learn how custom scopes affect step instances and their dependency relationships, see How Custom Scopes Apply to Fulfillment Steps and Dependencies.
NOTE Cross Plan Scope Considerations:
For the Cross Plan scope, one instance of the step appears per plan when a step in one plan is dependent on a step that’s in another plan.
To use the Cross Plan scope, make sure to configure the Cross Plan context definition in Sales Transaction Context Definition. Then add or import the fulfillment step groups within the Fulfillment Workspace. See Create Custom Context Definitions for Order Orchestration.
NOTE Propagate State to Dependent Step Considerations:
Use the Propagate State to Dependent Step option only if you have created a dependency between a call out or auto task step and a pause step.
After defining the dependency and propagating the state to the dependent step, you can’t change the step type value, unless you first set the Propagate State to Dependent Step value to None.
NOTE In-flight Change Considerations:
When a step is amended or canceled because of an in-flight change in the plan, configure whether the step state must propagate to the following step by using the Propagate State to Dependent Step field. The options are - None, Amended, Canceled, and Both.
When a step is canceled because of an in-flight change in the plan, to reverse the order of step group execution, select the Execute Cancel Step Groups In Reverse Order checkbox.
EXAMPLE

A step's scope determines how many instances of that step DRO creates when an order is fulfilled.

Plan: DRO creates one instance of the step for the entire order.
Bundle: DRO creates one instance of the step for each bundle in the order.
Line Item: DRO creates one instance of the step for each order line item.

For all the scope values, see Define a Fulfillment Step.

In a dependency, Step A depends on Step B, so Step B must finish before Step A can start. The dependency scope determines which Step B instance each Step A waits for. To create common dependency patterns, set the step scopes and the dependency scope as shown in this table.

Scope Settings for Common Dependency Patterns
TO CREATE	SET STEP B SCOPE TO	SET STEP A SCOPE TO	SET DEPENDENCY SCOPE TO
Multiple Step B and one Step A	Line Item	Plan	Line Item
One Step B and multiple Step A	Plan	Line Item	Plan
Multiple Step B and multiple Step A	Line Item	Line Item	Line Item

For example, to make each per-line-item step depend on one plan-level step, set Step B's scope to Plan and Step A's scope to Line Item. For an order that has three line items, DRO creates one Step B for the whole plan and one Step A for each line item, and all three Step A instances wait for that one Step B to finish.

Bundle scope works the same way at the bundle level. When a step's scope is Bundle, DRO creates one instance of the step for each bundle in the order. To pair a Bundle-scoped step with steps at another scope, apply the same rule: Set the dependency scope to the scope of the step that must finish first.

SEE ALSO
Context Definitions for Dynamic Revenue Orchestrator
Import a Fulfillment Step Definition Group
Cross-Plan Dependencies

=== ARTICLE: ind.dro_sla_jeopardy_administration.htm ===
---
article_id: ind.dro_sla_jeopardy_administration.htm
title: SLA Jeopardy Administration
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_sla_jeopardy_administration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator.htm
fetched_at: 2026-09-05
---

# SLA Jeopardy Administration

Honor your Service Level Agreements (SLAs) with alerts and other settings to handle fulfillment steps that run behind or fail to finish.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Dynamic Revenue Orchestrator (DRO) notifies you when a fulfillment step is late or in jeopardy of being late.

Jeopardy administration uses two concepts that work together: The Estimated Duration and the Jeopardy Threshold.

Estimated Duration
How long do you expect a fulfillment step to take? Enter a number, and then choose a unit, such as minutes or days. Let's say that you choose 10 minutes. If a step takes longer than ten minutes, then it's late.
Jeopardy Threshold
When do you want to be warned that a step is in jeopardy of being late? Enter a number, then choose a unit, such as minutes or days.
TIP The jeopardy threshold counts backwards from the estimated duration. So if the estimated duration is 100 minutes and the Jeopardy Threshold is 10 minutes, then the step is considered in jeopardy after 90 minutes.

To specify the callouts, manual tasks, or auto tasks that the rule applies to, enter an integration definition or a flow definition.

Integration definition
This field specifies the callouts that the rule applies to. If you leave it blank, then the rule applies to all callouts.
Flow definition
This field specifies the manual tasks or auto tasks that the rule applies to. If you leave it blank, then the rule applies to all manual tasks and auto tasks.

To create fulfillment step jeopardy rules, follow these instructions:

SEE ALSO
Turn On Features to Manage Fallout and Service Level Agreements

=== ARTICLE: ind.dro_steps_to_create_a_custom_context_definition.htm ===
---
article_id: ind.dro_steps_to_create_a_custom_context_definition.htm
title: Create Custom Context Definitions for Order Orchestration
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_steps_to_create_a_custom_context_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Create Custom Context Definitions for Order Orchestration

During the fulfillment of orders, Dynamic Revenue Orchestrator (DRO) sometimes uses the permissions associated with context definitions. Add a custom context definition by extending the Sales Transaction Context Definition.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
NOTE If you aren't familiar with Context Service and working with Context Definitions, learn Context Service Basics at Trailhead.

Create a custom context definition by choosing nodes, defining their relationship, and adding attributes. These custom definitions are available on the Custom Definitions tab. Create custom definitions by using the Extend action.

=== ARTICLE: ind.dro_submit_order_with_validation_flow.htm ===
---
article_id: ind.dro_submit_order_with_validation_flow.htm
title: Handle Conflicts During Asset Date Amendments by Using Submit Order with Validation Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_submit_order_with_validation_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# Handle Conflicts During Asset Date Amendments by Using Submit Order with Validation Flow

It's common to request adjustments to license subscription start dates, either moving them earlier if your users are ready to use them or delaying them if they are not. However, if the order that created the asset has incomplete steps in its fulfillment plan, submitting an asset amendment can result in two orders updating the asset simultaneously. Identify and handle incomplete steps in the fulfillment plan by using the Submit Order with Validation flow.

REQUIRED EDITIONS
Available in: Both Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To run the Submit Order with Validation Flow:	

Fulfillment Designer

OR

DRO Admin User

Use the flow to discard future-dated or pending steps that are no longer relevant in the existing fulfillment plan, so asset amendments are processed without conflicts.

The Submit Order with Validation flow uses the Get Steps from Order subflow, that retrieves the incomplete steps from an order. The order is identified using the orderID passed to the subflow. Both the flows are available as out-of-the-box template flows.

NOTE The Submit Order with Validation flow is designed for orders containing up to 200 order line items. To work with larger orders, contact your Salesforce admin.

To use the Get Steps from Order subflow in the Submit Order with Validation flow, follow these steps:

From Setup, find and select Flows.
Find and select Get Steps from Order.
Save the Get Steps from Order template as a new flow and activate it.
Find and select Submit Order with Validation.
Save the Submit Order with Validation template as a new flow.
Replace the Get Steps from Order subflow step in the Submit Order with Validation flow with a call to the newly created active Get Steps from Order subflow.
Assign the same input and output variables that were used in the old subflow.
Activate the Submit Order with Validation flow.
When you call the Submit Order with Validation flow using the orderId of an order with an incomplete fulfillment plan, the incomplete steps found in the order are shown. Review the steps and remove those that you don’t want to discard. Then, you can choose to discard the remaining incomplete steps and submit the order. Now, any future amendments to the asset can be processed without issues.

=== ARTICLE: ind.dro_technical_bundles.htm ===
---
article_id: ind.dro_technical_bundles.htm
title: Technical Bundles
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_technical_bundles.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_dynamic_revenue_orchestrator_concepts_and_references.htm
fetched_at: 2026-09-05
---

# Technical Bundles

Technical bundles organize related fulfillment line items into a hierarchy under a single root. This grouping keeps related products together so they follow consistent fulfillment actions throughout their lifecycle.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Technical bundles use decomposition rules and order lineage to keep related products grouped during fulfillment. As shown in the diagram, the Premium AI Workspace Bundle commercial product decomposes into a technical bundle. The root, AI Workspace Technical Bundle, groups three fulfillment tasks — Compute Provisioning, Vector Storage, and Identity Provisioning — in a single Fulfillment Order.

Generate a fulfillment order line item (FOLI) for a technical bundle only when a decomposition rule is defined.
Parent-child products under a technical bundle only if their lineage traces back to that parent. To establish this hierarchy, the system verifies catalog relationships. If it doesn't find an immediate match, the system searches the order hierarchy for the nearest valid ancestor.
Qualify every decomposition rule in the parent-child chain to maintain the bundle structure. If a rule for a middle node doesn't qualify, the bundle hierarchy splits.
Consolidate FOLI records when multiple products within a technical bundle share a decomposition rule.
Assign bundled FOLI records to a single Fulfillment Order (FO) to make sure that technical dependencies remain unified for downstream systems.
NOTE Bubbling up the actions assigned to child components determines the parent FOLI actions:
If a parent item has a cancel action but at least 1 child remains active, the parent action is updated to Amend.
If a parent item has a No Change action but a child is assigned a cancel or Amend action, the parent action is updated to Amend to make sure that the parent reflects the changes to its components.

=== ARTICLE: ind.dro_technical_product_in_dro.htm ===
---
article_id: ind.dro_technical_product_in_dro.htm
title: Build Your Technical Product Catalog for Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_technical_product_in_dro.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_decomposition.htm
fetched_at: 2026-09-05
---

# Build Your Technical Product Catalog for Dynamic Revenue Orchestrator

A technical product represents the items, services, or processes that enable order fulfillment to deliver a complete commercial product to your customer. A technical product lets fulfillment designers decouple front-office entities from mid- and back-office entities. To use Dynamic Revenue Orchestrator, you must configure your technical products using Product Catalog Management.

NOTE If you aren't familiar with creating products and product catalogs, see Product Catalog Management.
Model a Technical Product

Model a technical product when:

The packaged products are decoupled from the services and equipment provided to the customer. In this case, you can model a technical product for services and equipment.
A technical product contains the details of order fulfillment through orchestration that CRM systems don't provide during the order capture.
The technical product's attributes contain necessary data for fulfillment, such as specifications of RAM for a server.
Multiple commercial products use the same fulfillment processes or systems. For example, all products in a portfolio use the same billing system to generate invoices.
Commercial line items decompose into multiple technical products, and each component requires a different fulfillment process or system.
Attributes of a commercial product or order are passed to different fulfillment systems, either directly or after transformation. For example, the start date of a line item is passed to the provisioning system, and the weight is passed to the shipping partner.

Don't model a technical product in these cases:

The technical product duplicates a commercial product.
It has information of commercial significance.
It determines pricing during quoting or ordering.
It changes attributes and fields during quoting or ordering.
Scenarios to Model a Technical Product in Dynamic Revenue Orchestrator
Fulfilling Tangible Products

Consider a scenario for fulfilling orders for servers bundled with RAM and storage as child products. The fulfillment plan can include steps that run in sequence or in parallel. For example, you can model a technical product for:

Managing warehouse-related activities
Managing the shipping of items
Generating the invoice for the customer

In this scenario, you can reuse technical products when new models and variants of servers, RAM, memory, and products in similar categories are added to the commercial catalog.

Fulfilling Non-Tangible Products

Consider a scenario for selling a suite of cloud-based productivity and collaboration tools, including email, cloud storage, word processor, and spreadsheets to businesses. In this scenario, you can model a technical product for:

Account creation and management service
Identity and access management provisioning service for the users
License provisioning for each application that requires activation
Usage-entitlement provisioning
Fulfilling Bundled Tangible and Non-Tangible Products

Consider a scenario of a car dealer providing three years of free annual service along with vehicle insurance. In this case, you can model a technical product for:

Dealer-specific activities such as placing orders with manufacturers, car inspections, registrations, and deliveries.
Non-dealer activities such as providing annual servicing and warranties.
Examples of Technical Products

Consider a scenario for fulfilling orders for office laptops. The customer understands that these laptops have specifications like 16GB RAM, 500 GB SSD storage, and uses operating system version 22.04. However, your fulfillment team needs to keep track of many more details.

When the retail order decomposes for fulfillment, you might use technical products such as:

The physical laptop itself
The operating system license
Corporate user account activation
Office productivity application licenses
Corporate VPN account
Antivirus protection license
IT asset tag registration
Laptop peripherals package
Create a Technical Product
To create technical products in Dynamic Revenue Orchestrator (DRO), follow these instructions.
Decomposition Scope
Set the decomposition scope to limit how many instances of a fulfillment order line item appear in fulfillment.

=== ARTICLE: ind.dro_time_aware_fulfillment.htm ===
---
article_id: ind.dro_time_aware_fulfillment.htm
title: Order Fulfillment With Time-Awareness
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_time_aware_fulfillment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# Order Fulfillment With Time-Awareness

Manage complex, multi-year subscription lifecycles by using time-awareness in fulfillment assets. Instead of using a static snapshot of an asset, time-awareness aligns orchestration with the effective dates of each change, so that additions, cancellations, and renewals of backdated and future-dated orders update only the assets that change in that period.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Time-awareness is ideal for multi-year deals in which product configurations, such as quantity and attributes, change over time. It's especially useful for managing ramp deals, where annual changes occur within a single multi-year contract.

For example, a customer signs a 3-year subscription for 100, 200, and 300 licenses in Years 1, 2, and 3. If they amend Year 1 to add 50 licenses, time-aware fulfillment updates only Year 1 and leaves Years 2 and 3 unchanged.

How Time-Awareness Works
Fulfillment Order Product and Fulfillment Asset records use the Fulfillment Asset State Period (FASP) object to track a subscription's state, quantity, and attributes over time. Each FASP record represents a fulfillment asset's distinct time segment, tied to an asset state period of the corresponding source asset. When a source asset has multiple asset state periods, Dynamic Revenue Orchestrator (DRO) creates multiple FASP records accordingly.
Orchestrate Orders with Time-Awareness
Dynamic Revenue Orchestrator (DRO) sequences fulfillment steps across time period. Steps for a future period wait for the preceding period to finish, while configured dependencies continue to control the order of execution within each period.
How Dynamic Revenue Orchestrator Determines Actions for Time-Aware Assets
When you turn on time-awareness, Dynamic Revenue Orchestrator (DRO) evaluates the state of a Fulfillment Asset (FA) record and its Fulfillment Asset State Period (FASP) records before and after technical assetization, along with any attribute changes. DRO then determines the decomposition action for a given period.
Migrate Fulfillment Assets from Time-Agnostic to Time-Aware
Attribute values of Fulfillment Asset (FA) records created before time-awareness reflect only the most recent assetization state and not the values that were in effect during each asset state period in the past. When you submit an Amend, Renew, or Cancel order on these assets, decomposition can derive the wrong fulfillment order line item action for the affected period. Also, the resulting fulfillment asset state period (FASP) values can be incorrect.
Example: Add Action with Time-Awareness Turned On
Let's see how Dynamic Revenue Orchestrator (DRO) uses time-awareness to decompose a multi-year ramp deal into fulfillment order line items (FOLIs) and Fulfillment Asset State Period (FASP) records that align with each year's effective dates.
Example: Mid-Year Amendment with Split Fulfillment Asset State Periods
Let's see how Dynamic Revenue Orchestrator (DRO) uses time-awareness to split existing Fulfillment Asset State Period (FASP) records when a new contract starts mid-year, and how it derives No Change, Amend, and Renew actions for the overlapping timeline.
Considerations for Backdated Changes in Dynamic Revenue Orchestrator
Review how Dynamic Revenue Orchestrator (DRO) decomposes and orchestrates backdated amend, renew, and cancel orders and rolls back amend and renew orders. Understand the behavior and constraints when time-awareness isn't turned on.
SEE ALSO
Turn On Time-Awareness

=== ARTICLE: ind.dro_time_aware_fulfillment_actions.htm ===
---
article_id: ind.dro_time_aware_fulfillment_actions.htm
title: How Dynamic Revenue Orchestrator Determines Actions for Time-Aware Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_time_aware_fulfillment_actions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_time_aware_fulfillment.htm
fetched_at: 2026-09-05
---

# How Dynamic Revenue Orchestrator Determines Actions for Time-Aware Assets

When you turn on time-awareness, Dynamic Revenue Orchestrator (DRO) evaluates the state of a Fulfillment Asset (FA) record and its Fulfillment Asset State Period (FASP) records before and after technical assetization, along with any attribute changes. DRO then determines the decomposition action for a given period.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
BEFORE TECHNICAL ASSETIZATION	AFTER TECHNICAL ASSETIZATION	FA ATTRIBUTE/QUANTITY CHANGE	ACTION	EFFECT
FA	FASP	FA	FASP
Doesn't exist	Not applicable	Exists	Exists	Not applicable	Add	Creates an FA and an FASP.
Exists	Doesn't exist	Exists	Exists	Not applicable	Renew	Adds an FASP to an existing FA.
Exists	Exists	Exists	Doesn't exist	Not applicable	Cancel	A new FASP superseeds the existing one.
Exists	Exists	Exists	Exists	Changes present	Amend	A new FASP superseeds the existing one.

=== ARTICLE: ind.dro_time_aware_fulfillment_architecture.htm ===
---
article_id: ind.dro_time_aware_fulfillment_architecture.htm
title: How Time-Awareness Works
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_time_aware_fulfillment_architecture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_time_aware_fulfillment.htm
fetched_at: 2026-09-05
---

# How Time-Awareness Works

Fulfillment Order Product and Fulfillment Asset records use the Fulfillment Asset State Period (FASP) object to track a subscription's state, quantity, and attributes over time. Each FASP record represents a fulfillment asset's distinct time segment, tied to an asset state period of the corresponding source asset. When a source asset has multiple asset state periods, Dynamic Revenue Orchestrator (DRO) creates multiple FASP records accordingly.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
When of a fulfillment asset's quantity or attributes change, DRO creates an FASP record to represent the new state. FASP records change the validity of an existing fulfillment asset or overwrite the fulfillment asset configuration for a specific time period.
When a state period is updated, DRO marks the previous FASP records as superseded. During order decomposition, it filters out superseded records and queries only the fulfillment asset's current state.
A nightly background job identifies assets with configuration end dates that passed and updates their current quantity and attributes to match the next effective state period.

=== ARTICLE: ind.dro_time_aware_fulfillment_enable.htm ===
---
article_id: ind.dro_time_aware_fulfillment_enable.htm
title: Turn On Time-Awareness
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_time_aware_fulfillment_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Turn On Time-Awareness

Dynamic Revenue Orchestrator (DRO) supports both time-agnostic and time-aware data. During decomposition and assetization, time-awareness evaluates timelines to identify changes in fulfillment asset quantities and attributes over time.

REQUIRED EDITIONS
Available in: Both Salesforce Classic (not available in all orgs) and Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS
NEEDED
To define how a product decomposes:	

Fulfillment Designer

OR

DRO Admin User

Before you enable time-awareness, run the migration scripts that move your existing time-agnostic data to the time-aware model. See Migrate Fulfillment Assets from Time-Agnostic to Time-Aware.
Update your orchestration plans that were designed for time-agnostic data so they can handle the fulfillment order line item outputs that time-aware decomposition generates.
NOTE
Staged assetization of ramp segments is supported only for time-aware fulfillment assets. For more information, see Staged Assetize Step.
Once you turn on time-awareness, you can't turn it off.

Time-awareness is turned off by default. To turn it on, complete these steps.

From Setup, in the Quick Find box, enter and then select Dynamic Revenue Orchestrator Settings.
Turn on Time-Awareness.
SEE ALSO
Order Fulfillment With Time-Awareness

=== ARTICLE: ind.dro_time_aware_fulfillment_example_add.htm ===
---
article_id: ind.dro_time_aware_fulfillment_example_add.htm
title: "Example: Add Action with Time-Awareness Turned On"
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_time_aware_fulfillment_example_add.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_time_aware_fulfillment.htm
fetched_at: 2026-09-05
---

# Example: Add Action with Time-Awareness Turned On

Let's see how Dynamic Revenue Orchestrator (DRO) uses time-awareness to decompose a multi-year ramp deal into fulfillment order line items (FOLIs) and Fulfillment Asset State Period (FASP) records that align with each year's effective dates.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Consider a commercial product, Agentforce for Sales, that decomposes into SC-Business or SC-Enterprise based on the Business attribute, and Tenant and License Provisioning. This example uses the Business attribute, so only SC-Business is created.

EXAMPLE

The customer purchases Agentforce for Sales in a 3-year ramp deal that starts January 1, 2026, with license quantities increasing each year.

Year 1: 100 licenses
Year 2: 200 licenses
Year 3: 300 licenses

Without time-awareness, decomposition produces a single configuration with no effective start or end dates. Later amendments overwrite past or future data and leave the asset in an inaccurate state.

With time-awareness enabled, DRO generates FOLIs mapped to each effective date range.

DRO generates these FOLIs for each technical product:

SC-Business: Three FOLIs for 100, 200, and 300 licenses, one per year.
License Provisioning: Three FOLIs that match the ramping quantities across the timeline.
Tenant: Three FOLIs that maintain a quantity of 1 across all three years. Because Tenant has account scope, its quantity stays at 1 regardless of the license ramp.

Each FOLI produces an Add action because no prior Fulfillment Asset or FASP records existed for these technical products on this account.

Because the FOLIs are sliced by time, DRO creates FASP 1, FASP 2, and FASP 3 for each FA. This structure prevents data overwrites and makes sure that the asset configuration that is active at any point in time drives orchestration.

=== ARTICLE: ind.dro_time_aware_fulfillment_example_amend.htm ===
---
article_id: ind.dro_time_aware_fulfillment_example_amend.htm
title: "Example: Mid-Year Amendment with Split Fulfillment Asset State Periods"
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_time_aware_fulfillment_example_amend.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_time_aware_fulfillment.htm
fetched_at: 2026-09-05
---

# Example: Mid-Year Amendment with Split Fulfillment Asset State Periods

Let's see how Dynamic Revenue Orchestrator (DRO) uses time-awareness to split existing Fulfillment Asset State Period (FASP) records when a new contract starts mid-year, and how it derives No Change, Amend, and Renew actions for the overlapping timeline.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

This example builds on the 3-year Agentforce for Sales ramp deal described in Example: Add Action with Time-Awareness Turned On. The account now adds Agentforce for Service in a second 3-year ramp deal that starts on June 1, 2026. Agentforce for Service decomposes into the same two shared technical products as Agentforce for Sales: Tenant and License Provisioning.

EXAMPLE

The Agentforce for Service ramp specifies these quantities:

Year 1: 50 licenses
Year 2: 150 licenses
Year 3: 250 licenses

Because the Agentforce for Service deal starts mid-Year 1 of the existing Agentforce for Sales contract, time-aware decomposition splits the Year 1 FASP timeline for the shared technical products into two segments: January 1 to May 31, and June 1 to December 31. The split generates six fulfillment order line items (FOLIs) for Tenant and six FOLIs for License Provisioning across the 3-year overlap.

Time-awareness derives these actions from the overlap:

No Change
The Tenant technical product has account scope, so its quantity stays at 1 across all periods. Tenant doen't require new FASP values for the existing periods.
Amend
The License Provisioning technical product uses an aggregate quantity rule. Starting June 1, Agentforce for Service contributes 50 more License Provisioning, which aggregate with the existing Agentforce for Sales License Provisioning for the second half of Year 1. The Amend action updates the existing License Provisioning FASPs to reflect the new aggregated quantity.
Renew
The Renew action applies in two situations: to insert a new FASP between two existing FASPs when DRO splits the timeline, and to add a new FASP for the final term of the Agentforce for Service deal that extends into 2029.

DRO marks the baseline License Provisioning and Tenant FASPs as superseded and replaces them with the newly generated FASPs that reflect the split time periods and the derived actions.

NOTE This example doesn't demonstrate the Cancel action. Cancel applies when a FASP that existed before technical assetization no longer exists afterward, such as when a customer terminates a specific term of a subscription.

=== ARTICLE: ind.dro_time_aware_fulfillment_migration.htm ===
---
article_id: ind.dro_time_aware_fulfillment_migration.htm
title: Migrate Fulfillment Assets from Time-Agnostic to Time-Aware
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_time_aware_fulfillment_migration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_time_aware_fulfillment.htm
fetched_at: 2026-09-05
---

# Migrate Fulfillment Assets from Time-Agnostic to Time-Aware

Attribute values of Fulfillment Asset (FA) records created before time-awareness reflect only the most recent assetization state and not the values that were in effect during each asset state period in the past. When you submit an Amend, Renew, or Cancel order on these assets, decomposition can derive the wrong fulfillment order line item action for the affected period. Also, the resulting fulfillment asset state period (FASP) values can be incorrect.

To fix this issue, manually create the missing state period data for each affected fulfillment asset before turning on time-awareness:

Identify the FA records created before time-awareness was enabled. Look for records whose quantity or attribute values change over time.
For each FA record, create an FASP record with the configuration for every state change, with the correct start date, end date, and quantity for that period.
For each FASP record, create the corresponding FASP attribute records that capture the attribute key-value pairs in effect during that period.
SEE ALSO
Turn On Time-Awareness

=== ARTICLE: ind.dro_time_aware_plan_sequence.htm ===
---
article_id: ind.dro_time_aware_plan_sequence.htm
title: Orchestrate Orders with Time-Awareness
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_time_aware_plan_sequence.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_time_aware_fulfillment.htm
fetched_at: 2026-09-05
---

# Orchestrate Orders with Time-Awareness

Dynamic Revenue Orchestrator (DRO) sequences fulfillment steps across time period. Steps for a future period wait for the preceding period to finish, while configured dependencies continue to control the order of execution within each period.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

When DRO creates an orchestration plan for a time-aware order, it groups instantiated fulfillment steps that apply to the same time period. DRO sequences these groups according to the start and end dates and times of the steps’ sources. It then adds dependencies from the applicable final steps in one group to the applicable first steps in the next group. As a result, fulfillment for a later period begins only after the required fulfillment for the preceding period finishes.

DRO preserves dependencies configured within each time period, including dependencies that use Plan, Bundle, Line Item, or Custom scope. Steps in the same period can run in parallel unless a configured dependency requires them to run sequentially. If a group has multiple first or final steps, DRO connects the applicable steps so that the required steps in the preceding period finish before the dependent steps in the next period begin.

NOTE
To sequence fulfillment correctly across time periods, configure the required dependencies and scopes in the fulfillment step definitions and step dependencies. DRO preserves this configuration within each time period and uses it when connecting one time-period group to the next.
A fulfillment step whose sources span multiple time periods can remain shared across the periods instead of belonging to a single time-period group.
Example: Fulfillment Across Time Periods

Consider an order with a two-year ramp for Sales Cloud and Service Cloud. In year 1, the plan runs Provision Tenant, Activate License, and Notify Customer according to their configured dependencies and scopes. Steps without dependencies between them run in parallel. DRO sequences the groups of instantiated steps according to the start and end dates and times of their sources. The applicable year 2 steps start only after the required Year 1 steps finish.

=== ARTICLE: ind.dro_turn_on_dynamic_revenue_orchestrator.htm ===
---
article_id: ind.dro_turn_on_dynamic_revenue_orchestrator.htm
title: Turn On Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_turn_on_dynamic_revenue_orchestrator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_basic_set_up.htm
fetched_at: 2026-09-05
---

# Turn On Dynamic Revenue Orchestrator

You must turn on Dynamic Revenue Orchestrator so that your org is prepared to use it for fulfillment.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To turn on Dynamic Revenue Orchestrator:	

DRO Admin User

Don’t turn on Dynamic Revenue Orchestrator unless you’re a Revenue Management (formerly Revenue Cloud) customer. When you turn on Dynamic Revenue Orchestrator, you also enable Revenue Management, if it's not already enabled.

From Setup, in the Quick Find box, enter Dynamic Revenue Orchestrator Settings and select it.
Switch on Dynamic Revenue Orchestrator.

Select the fulfillment user. See Create Fulfillment Users for Order Orchestration

=== ARTICLE: ind.dro_turn_on_feature_to_link_task_to_step_source.htm ===
---
article_id: ind.dro_turn_on_feature_to_link_task_to_step_source.htm
title: Turn On Task Linking to Step Source
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_turn_on_feature_to_link_task_to_step_source.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_basic_set_up.htm
fetched_at: 2026-09-05
---

# Turn On Task Linking to Step Source

Salesforce tasks are linked to fulfillment steps. Enable the linking of a Salesforce task to a fulfillment step source.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To turn on the Link Task to Step Source feature:	

System Administrator profile

By linking the task to the step source, users can see the activity details for the entire fulfillment order in one place, without going to individual steps. For example, if a fulfillment order consists of multiple manual tasks, the activities of each task is shown at the order level. The activity details include information on all upcoming and overdue tasks related to the fulfillment order.

From Setup, in the Quick Find box, enter Dynamic Revenue Orchestrator Settings and select it.
Turn on Link Task to Source Step.
SEE ALSO
Monitor Decomposition During Fulfillment

=== ARTICLE: ind.dro_turn_on_features_to_manage_fallout_and_service_level_agreements.htm ===
---
article_id: ind.dro_turn_on_features_to_manage_fallout_and_service_level_agreements.htm
title: Turn On Features to Manage Fallout and Service Level Agreements
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_turn_on_features_to_manage_fallout_and_service_level_agreements.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_basic_set_up.htm
fetched_at: 2026-09-05
---

# Turn On Features to Manage Fallout and Service Level Agreements

Turn on features to manage failed or late fulfillment steps.

REQUIRED EDITIONS

Turn On Dynamic Revenue Orchestrator

Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To turn on Fallout and SLA features:	System Administrator profile

To use the features that help you manage fallout and SLAs (Service Level Agreements), Dynamic Revenue Orchestrator (DRO) must set up certain decision tables. When you turn on the features, DRO sets up those tables automatically. To turn on fallout and SLA features, you must have permissions to create Decision Tables. See: Create a Decision Table.

From Setup, in the Quick Find box, enter Fallout and SLA Settings and select it.
Switch on Fallout and Service Level Agreement.

Configure Fallout Rules or Configure Fulfillment Step Jeopardy Rules

SEE ALSO
Configure Fulfillment Step Jeopardy Rules
Configure Fallout Rules

=== ARTICLE: ind.dro_turn_on_future_dated_steps.htm ===
---
article_id: ind.dro_turn_on_future_dated_steps.htm
title: Turn On Future Dated Steps
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_turn_on_future_dated_steps.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_advanced_setup.htm
fetched_at: 2026-09-05
---

# Turn On Future Dated Steps

Turn on Future Dated Steps feature to configure steps to execute at a future date and  time.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
From Setup, in the Quick Find box, enter Dynamic Revenue Orchestrator Settings and select it.
Turn on Future Dated Steps.

=== ARTICLE: ind.dro_unit_of_measure_inheritance_and_rounding_values.htm ===
---
article_id: ind.dro_unit_of_measure_inheritance_and_rounding_values.htm
title: Unit Of Measure Inheritance and Rounding Values
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_unit_of_measure_inheritance_and_rounding_values.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_design_time_decomposition.htm
fetched_at: 2026-09-05
---

# Unit Of Measure Inheritance and Rounding Values

During decomposition, the fulfillment order product inherits the unit of measure from the related technical product. During technical assetization, the fulfillment asset inherits the unit of measure from the corresponding fulfillment order line item.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions

Quantity values are rounded off in both fulfillment order line items and fulfillment assets, based on the Dynamic Revenue Orchestrator's (DRO) Unit Of Measure (UOM) scale and rounding rules. See Decimal Quantity Support in Product Catalog Management.

When multiple commercial products with different UOMs decompose into a single technical product that uses the Aggregate quantity calculation method, the system sums up the quantity values of the commercial products without converting them to the technical product's UOM. The summed quantity is then applied to the fulfillment order product.

IMPORTANT

Make sure that you convert all quantities of each commercial product to match the corresponding technical product's UOM before you submit the order to DRO.

=== ARTICLE: ind.dro_use_context_definitions.htm ===
---
article_id: ind.dro_use_context_definitions.htm
title: Turn On Context Definitions
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_use_context_definitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_basic_set_up.htm
fetched_at: 2026-09-05
---

# Turn On Context Definitions

Context definitions ensure efficient data access at every step of the orchestration process. A context definition includes a structure that defines the nodes, its attributes, and context tags.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To create and view context definitions:	

DRO Admin User permission set

In order to view context definitions on your org:

Enable the Salesforce Dynamic Revenue Orchestrator (DRO) admin user licenses.
Enable the Context Service platform license, Context Service Access.
Turn on Context Definitions.

To turn on context definitions:

 From Setup, in the Quick Find box, enter Context Service, and then select Context Service Settings. 
To load the predefined context definitions, turn on the toggle next to Context Definitions.
IMPORTANT The Salesforce DRO solution comes with its own predefined context definitions that are used to map sales transactions to objects and Order. However, if you want to customize parts of this context definition for reuse, extend or clone it and make modifications.

All the context definitions, predefined or created by you, can be viewed on the Context Definitions page. To view the Context Definitions page, from Setup, in the Quick Find box, enter Context Service, then select Context Definitions.

SEE ALSO
Trailhead:: Context Service Basics
Context Definitions

=== ARTICLE: ind.dro_view_fulfillment_step_history.htm ===
---
article_id: ind.dro_view_fulfillment_step_history.htm
title: View Fulfillment Step History
source_url: https://help.salesforce.com/s/articleView?id=ind.dro_view_fulfillment_step_history.htm&type=5&release=264
release: 264
release_name: Winter '27
area: dro
parent_article: ind.dro_run_time_administration.htm
fetched_at: 2026-09-05
---

# View Fulfillment Step History

Monitor the changes to a fulfillment step, such as status modifications, on its detail page by using the Fulfillment Step History related list.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions
USER PERMISSIONS NEEDED
To view the fulfillment step history:	

Fulfillment Designer

OR

DRO Admin User

Whenever a user changes a standard or custom field, the system logs an entry in the Fulfillment Step History related list, irrespective of the order's status. Each entry captures the date and time of the change, the affected field, the user who made the change, and the specific details of the change.

From the App Launcher, find and select Fulfillment Steps.
Select a step to view its details and history.

