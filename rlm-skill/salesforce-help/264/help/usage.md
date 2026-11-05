# Salesforce Help 264 — área: usage (52 artículos)

=== ARTICLE: ind.um_add_wallet_components_to_record_pages.htm ===
---
article_id: ind.um_add_wallet_components_to_record_pages.htm
title: Add Wallet Components to Record Pages
source_url: https://help.salesforce.com/s/articleView?id=ind.um_add_wallet_components_to_record_pages.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_set_up_experience_cloud_for_wallet_management.htm
fetched_at: 2026-09-07
---

# Add Wallet Components to Record Pages

Configure record layouts in Experience Cloud to show wallet balances, usage, and entitlement data for your customers.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To view the wallet dashboard:	Wallet Management User
In Setup, find and select All Sites.
In the Action column for your site, click Builder.
In Experience Cloud Builder, click the Pages in the top toolbar, and then click New Page.
Click Object Pages, select Usage Entitlement Bucket from the list, and then click Create.
Drag the Wallet Statement component to the Usage Entitlement Bucket page.
Add components to other pages:
From Pages and select Account, Asset, Contract, and Binding Object detail pages.
Drag the Wallet Details component and add it to each page.
Save and activate the Usage Entitlement Bucket page.

=== ARTICLE: ind.um_anchor_product_drawdowns.htm ===
---
article_id: ind.um_anchor_product_drawdowns.htm
title: Anchor Product Drawdowns
source_url: https://help.salesforce.com/s/articleView?id=ind.um_anchor_product_drawdowns.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_buckets_and_drawdowns.htm
fetched_at: 2026-09-07
---

# Anchor Product Drawdowns

An anchor product is the base purchase, such as a basic mobile plan that offers 4,000 text messages. When this anchor product is sold, the initial entitlement of 4,000 text messages is granted and is placed into a child bucket.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license

This child bucket is linked to a parent bucket, which serves as an overarching wallet showing the total balance of that resource across the account. When text messages are consumed, Consumption Management deducts the consumed units directly from the anchor's child bucket.

EXAMPLE When a customer purchases a Basic Mobile Plan anchor product that offers 4,000 text messages, the initial entitlement of 4,000 units is granted and placed into a child bucket. As text messages are consumed during the billing cycle, Consumption Management performs a drawdown to deduct the consumed units directly from this child bucket.

=== ARTICLE: ind.um_billing_schedules_for_usage_products.htm ===
---
article_id: ind.um_billing_schedules_for_usage_products.htm
title: Billing Schedules and Invoices for Usage-Based Products
source_url: https://help.salesforce.com/s/articleView?id=ind.um_billing_schedules_for_usage_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_management.htm
fetched_at: 2026-09-07
---

# Billing Schedules and Invoices for Usage-Based Products

For usage-based products, Billing considers late usage and extra orders.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

When you activate an order, Billing creates a billing schedule and a billing schedule group for each binding instance and usage resource pair. The status of the billing schedule for usage resources is always Ready for Invoicing.

When another order creates a billing schedule for the same binding instance and usage resource, the dates of the existing billing schedule and billing schedule group are updated.

Unlike other charge types, usage charges don’t transition to a completely billed status. Usage billing schedules remain open beyond their end date to accommodate late usage and new orders tied to the same binding instance.

Usage-based products are invoiced under these conditions.

When you generate invoices by using the Invoice Scheduler, you select All or Usage filter.
Billing picks usage billing schedules for invoicing when the account is in a billing batch schedule and the schedules are ready for invoicing.
The liable summary status is marked as Ready for Invoicing.
The liable summary, usage entitlement bucket, and usage entitlement account share the grant binding target.
The usage billing schedule and the usage entitlement bucket correspond to the same usage resource, which is referenced from the billing period item.
When the usage entitlement bucket’s usage resource is populated, the same resource is autopopulated on the billing period item record.
NOTE For usage billing schedules and billing schedule groups, Billing doesn’t calculate invoice periods. Instead, it uses the liable summary start date and end date, stamping them on the billing period item and invoice line.

For example, if a company starts billing on January 20, 2025, and the billing cadence is monthly, the first billing period ends on February 19, 2025. Usage records are aggregated for invoicing if their event date falls within this window. The start date on the order product and the frequency define the billing period. During the invoice posting process, the liable summary status changes to Invoiced.

NOTE Draft invoices don’t affect the liable summary status. If a user voids a posted invoice, the liable summary status automatically reverts to Ready for Invoicing status and for rebilling.
Business Use Case

TelcoOne offers a data connect plan, a subscription that includes a monthly data allowance and charges for extra usage. The plan’s anchor product is the subscription itself, while mobile data consumption is modeled as a usage resource billed according to actual usage.

When a user activates an order, Billing creates billing schedules and billing schedule groups for both the subscription and its usage resources. Assets are created only for the anchor subscription product. Billing doesn’t create assets for usage resources.

The data allowance is provisioned as a grant. If the grant is exceeded, overage is chargeable. Actual data usage is recorded against the billing period, and Billing gets the usage data from the liable summaries record to generate invoice lines.

SAMPLE INVOICE LINES
PRODUCT	USAGE TYPE	QUANTITY	UNIT PRICE	TOTAL	ASSET ID
Data Connect Plan	Base Subscription	1	$30	$30	Asset-201
Data Connect Plan	Data Overage GB	2	$10	$20	Asset-201

This model provides a clear visibility into included allowances versus overage charges. It’s ideal for Telecom providers that need transparent and flexible invoicing for subscription and consumption-based services.

=== ARTICLE: ind.um_buckets_and_drawdowns.htm ===
---
article_id: ind.um_buckets_and_drawdowns.htm
title: Buckets and Drawdowns
source_url: https://help.salesforce.com/s/articleView?id=ind.um_buckets_and_drawdowns.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_consumption_management.htm
fetched_at: 2026-09-07
---

# Buckets and Drawdowns

A bucket acts as a digital wallet that holds a customer's available grants or entitlements. Consumption Management creates usage entitlement buckets after the product is sold and assetized. When usage summaries are created, Consumption Management performs a drawdown to deduct the consumed units from these buckets. If the usage exceeds the available bucket balance, the remaining quantity is accounted as overage.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Usage Entitlement Bucket Balance-Related Fields

The Usage Entitlement Bucket object provides these fields to help you track available balances.

FIELD	DESCRIPTION
Total As of Balance	Aggregated total of all grants available as of the current date.
Bucket Balance	Balance available at an individual (child) bucket level.
Total Provisional Balance	Aggregated balance used during daily rating to reflect in-progress drawdowns.
Provisional Balance	Temporary balance at the individual bucket level while the daily rating is in progress.
Parent and Child Buckets

The parent bucket represents the combined total balance of a specific resource across the binding target, which can be an account, an anchor asset, a contract, or a custom object. Child buckets represent the actual specific grants tied to an individual grant action, such as a new purchase, a grant renewal, a grant refresh, or grant rollover, or an amendment.

Drawdown Orders

If a customer has multiple child buckets for the same resource, you must define the order of buckets that consumption management uses for drawdown. Use the Drawdown Order field in the associated Product Usage Grant record. The field provides these valid values.

Expiring First—draws from the bucket that is closest to its expiration date. This is the default value.
Granted First—draws from the oldest bucket, based on the earliest start date.
Granted Last—draws from the newest bucket, based on the most recent start date.
How to Determine the Resulting Bucket Balance

To determine the expected bucket balance after the consumption is processed, evaluate the bucket balance before usage, the consumption date, and any active lifecycle changes like amendments, renewals, or cancellations. You must also account for the quantity being rated and the balance status—provisional or finalized. The resulting balance reflects the net remaining grants after the drawdown is applied.

Anchor Product Drawdowns
An anchor product is the base purchase, such as a basic mobile plan that offers 4,000 text messages. When this anchor product is sold, the initial entitlement of 4,000 text messages is granted and is placed into a child bucket.
Pack Product Drawdowns
Pack products are add-ons purchases that supplement an existing anchor product, such as adding a temporary international roaming pack or extra data.
Commitment Product Drawdowns
In a commitment product, the customer commits to consuming a specific quantity, token amount, or monetary spend in exchange for discounted rates. Commitments are applied by associating the commitment product with an anchor product.
Token Commitment Drawdowns
The consumption process for token commitments uses a two-step rating procedure. The process in the first step converts usage to tokens, and then in the second step, tokens to currency.
Token Commitment Drawdown Use Cases
The relationship between commitments and anchors, and how their consumption is processed varies depending on the binding target and the number of active products.
Consumption Proration Calculations
Proration is used to ensure that customers are only billed or granted resources for the fraction of a billing period that a product was active. Consumption Management uses a proration engine that performs the calculation and provides accurate billing.

=== ARTICLE: ind.um_cnsption_mngmnt_lifecycle.htm ===
---
article_id: ind.um_cnsption_mngmnt_lifecycle.htm
title: Consumption Management Lifecycle
source_url: https://help.salesforce.com/s/articleView?id=ind.um_cnsption_mngmnt_lifecycle.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_consumption_management.htm
fetched_at: 2026-09-07
---

# Consumption Management Lifecycle

Consumption management lifecycle is the structured process that tracks, monitors, and processes consumption data for consumption-based products and services. The process also manages grants and entitlements that help your users understand how the drawdowns take place for each usage resource and identify the overages.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Consumption Management Flows
To process consumption data and generate invoice-ready summaries, the consumption management process uses schedule-triggered flows.
Orchestrate Usage Management Flow Stages
The Orchestrate Usage Management flow with its subflows processes consumption data in various stages.
Consumption Management Lifecycle Statuses
The successful processing of consumption data involves status changes across the interlinked summaries—Usage Summary, Usage Ratable Summary, and Liable Summary. The entire flow, from raw usage data in the transaction journal to the calculation of net unit rates and the creation of invoice-ready data, is managed through these coordinated summaries.

=== ARTICLE: ind.um_commitment_product_drawdowns.htm ===
---
article_id: ind.um_commitment_product_drawdowns.htm
title: Commitment Product Drawdowns
source_url: https://help.salesforce.com/s/articleView?id=ind.um_commitment_product_drawdowns.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_buckets_and_drawdowns.htm
fetched_at: 2026-09-07
---

# Commitment Product Drawdowns

In a commitment product, the customer commits to consuming a specific quantity, token amount, or monetary spend in exchange for discounted rates. Commitments are applied by associating the commitment product with an anchor product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license

For commitment-based products, Consumption Management monitors usage relative to the customer’s committed limit rather than deducting consumption from an asset’s wallet balance. Until the customer hasn’t consumed beyond the committed amount, unit, or tokens, the discounted commitment rate applies.

When the customer consumes over the commitment or if the commitment period expires, Consumption Management evaluates the configured policies to determine whether to resume the standard anchor rate, or to keep the discounted rate for the remainder of the billing term.

EXAMPLE A customer purchases a QuantumBit Database anchor product with the standard catalog rate of $10 per GB for DB storage. The customer then commits to consuming 1,000 GB that provides them a 20% discount, lowering the rate to $8 per GB. As DB storage is consumed, Consumption Management performs a drawdown against the 1,000-GB committed limit, rating usage at the discounted $8 price. If usage exceeds 1,000 GB, the resulting overage is billed at either the standard $10 anchor rate or the discounted $8 rate, depending on the defined expiration and commitment policies.

=== ARTICLE: ind.um_configure_usage_product_with_guided_workflow.htm ===
---
article_id: ind.um_configure_usage_product_with_guided_workflow.htm
title: Configure a Usage-Based Product with Guided Workflow
source_url: https://help.salesforce.com/s/articleView?id=ind.um_configure_usage_product_with_guided_workflow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_product_setup_with_guided_workflow.htm
fetched_at: 2026-09-07
---

# Configure a Usage-Based Product with Guided Workflow

Follow the guided workflow to create the related records required for your usage-based product. These records complete the product setup so that you can start selling quickly.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Advanced license and the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To use guided workflow with Revenue Management Advanced license:	

Product Catalog Management Designer

Rate Management Design Time User

Usage Design User


To use guided workflow with Revenue Management Advanced and Revenue Management Billing license:	

Product Catalog Management Designer

Rate Management Design Time User

Usage Management Designer

Before you use the workflow, configure organization-wide defaults for these objects. See Configure Record Sharing.

OBJECT	ORGANIZATION-WIDE DEFAULTS
Unit of Measure	Public Read/Write
Unit of Measure Class	Public Read/Write
Usage Resource	Public Read/Write
Usage Aggregation Policy	Public Read/Write
Usage Overage Policy	Public Read/Write
Rating Frequency Policy	Public Read/Write
Usage Commitment Policy	Public Read/Write
Usage Grant Refresh Policy	Public Read/Write
Usage Grant Rollover Policy	Public Read/Write
SEE ALSO
Rate Cards and Rate Card Entries
Manage Product Selling Model in Revenue Cloud
Define Prices in Price Books
Decision Tables for Rate Cards
Initiate the Guided Workflow
From the App Launcher, find and select Products.
Go to an anchor or pack product page, and then click Configure Usage Properties.
The Configure Usage Properties page appears with sections to add usage product related records, such as product usage resources and product usage grants.
Add or Create Product Usage Resources

To create product usage resources, you can either add existing usage resources or create new resources.

To add existing usage resources, in the Product Usage Resources pane, click Add.
In Add Usage Resources, select the resources, and then click Add.
If there are no resources available, click New.
Enter a name for the resource, and select a unit of measure class and a default unit of measure.
To ease setup, out-of-the-box policies, such as a Usage Aggregation Policy and Usage Overage Policy, are autopopulated. If the autopopulated policies don't meet your requirements, you can create or select different policies.
Click Add.
The product usage resource record is created and added to the Product Usage Resources list.
NOTE When you associate usage resources with a product, the related product usage resource record is created by default at 12:00 AM in your locale. For example, if your user in Germany selects a usage resource with a product on March 25, 2026, the product usage resource is created with an Effective Start Date of 25.03.2026 12:00 AM.
View and Define Usage Resource Details and Policies

While the product usage resource records are in the draft state, you can update their properties.

In the Product Usage Resource pane, select a record.
The right panel shows details of the selected record.
In the Product Usage Resource section, configure the effective start date and end date.
Review the autopopulated policies related to the product usage resource.
The policies are autopopulated with default lookups based on the selected usage resource. If the autopopulated policies don't meet your requirements, you can create or select different policies. The policies section isn't shown for pack products.
To save product usage resource and product usage resource policy record changes, under the Product Usage Resource section, click Save.
The action also creates the product usage resource policy record.
Configure Product Usage Grants

Define the grants provided with the product usage resource and the policies governing them.

In the Usage Grant section, enter the grant quantity, validity period term and unit, and effective period.
Review the autopopulated grant policies that are provided out of the box.
If the autopopulated policies don't meet your requirements, you can create or select different policies.
To save the product usage grant record, under the Product Usage Grant Details section, click Save.
The product usage grant record is saved and added to the Product Usage Grants list in the right panel.
To edit an existing product usage grant:
In the Product Usage Grants list, from the quick actions menu for a record, click Edit.
In the Product Usage Grant Details section, update the required fields.
Save your changes.
Validate and Activate Usage Product and Related Records

When you activate the usage records, the system runs cross-object validations to evaluate if all records work together. If the system detects issues, such as overlapping effective dates between product usage resource and product usage grant records, the errors are shown with error icons.

IMPORTANT Before you can successfully activate your product, you must create and associate an active Product Selling Model (PSM), price book (PB), and Rate Card Entry (RCE) records.
Click Activate.
If there are validation errors, resolve them by updating draft records.
Click Activate again.

These usage records get activated.

Usage Product
Usage Resource
Product Usage Resource
Product Usage Resource Policy
Product Usage Grant

If you've created new records for units of measure, unit of measure class, rate card entry, or any policy for product usage resource or product usage grant, they also get activated.

Manually refresh the decision tables used for the rate card and rate card entries.

=== ARTICLE: ind.um_configure_usage_records.htm ===
---
article_id: ind.um_configure_usage_records.htm
title: Configure Usage Management Records Manually
source_url: https://help.salesforce.com/s/articleView?id=ind.um_configure_usage_records.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_management_setup.htm
fetched_at: 2026-09-07
---

# Configure Usage Management Records Manually

Use manual configuration when your setup requires direct control over individual records or involves product types that the guided workflow doesn't support.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Advanced license and the Revenue Cloud Billing license

To successfully set up your usage management system, you must configure your usage records in a specific sequence. Follow the configuration tasks in order because each record depends on the records created before it.

Create a Unit of Measure Class
Unit of measure class defines the groupings of units of measure (UOM). For example, the Currency unit of measure class groups various currencies, such as euros, dollars, and rupees.
Create Units of Measure
A unit of measure quantifies the consumption of a usage resource. You can define units of measure to support a wide range of usage resources. For example, a unit of measure can be time-based, volume-based, transaction-based, or count-based.
Create Usage-Based Products
Evaluate and select the appropriate usage model type for creating a sellable product.
Create a Usage Resource
Usage resource is an entitlement or service that you grant your customers along with a product that you sell. Before you define rates and rate adjustments for usage resources, create usage resources for your products.
Create a Product Usage Resource
Associate existing usage resources with products, with a limit of one token resource per product.
Create a Product Usage Grant
Define the details of a grant associated with a resource, product, or service, such as the granted quantity, renewal and rollover policy, and the grant's validity period.
Create Usage Aggregation Policy
Define the method used to aggregate consumption of a usage resource over a period.
Create Rating Frequency Policy
The rating frequency policy defines how often the rating for a sellable product and a usage resource should be computed.
Create a Usage Overage Policy
Define the set of rules that determine how units consumed beyond the granted limit are managed for a usage resource.
Create Usage Grant Refresh Policy
Define whether the grants provided with the usage resource can be refreshed and the frequency of the grant refresh.
Create Usage Grant Rollover Policy
Each grant provided with the product has a validity period. Usage grant rollover policies define whether the usage resource’s grants expire or can be rolled over after the initial validity period is completed.
Create Usage Product Grant Binding Policy
Define the association between a usage resource’s grant with a sellable product.
Create a Usage Resource Policy
Define the policies applicable to a usage resource, regardless of whether it's associated with a sellable product.
Create a Product Usage Resource Policy
Define the policies that apply when a usage resource is associated with a sellable product. After the product is sold, these rules automatically apply to the resource. The policies you select here override the policies defined in the individual usage resource policy record.
Create a Usage Commitment Policy
Define the set of rules that determine how commitments are applied to a usage resource.
Create a Usage Commitment Asset Related Object
Apply discounted rates and additional grants available for the commitment product to the resources consumed by an anchor product. To provide these benefits, link the commitment product to the anchor product.

=== ARTICLE: ind.um_considerations_for_validator.htm ===
---
article_id: ind.um_considerations_for_validator.htm
title: Usage Product Validator Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.um_considerations_for_validator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_validate_your_setup.htm
fetched_at: 2026-09-07
---

# Usage Product Validator Considerations

The validator checks only the records that are effective and active. Before you use this feature, understand the validation rules, warning thresholds, and the different types of logic that the validator applies.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
The effectivity validation between the product usage resource and the rate card entry begins from the start date of the product usage resource.
If the time difference between these pairs of records is greater than 12 hours, the validator shows a warning.
Two consecutive product usage resource records for the same usage resource.
Two consecutive rate card entry records associated with a single product usage resource.
Start date of the product usage resource and the start date of the first associated rate card entry.
End date of the product usage resource and the end date of the last associated rate card entry. The validator checks for this gap only if the product usage resource has a defined end date.
NOTE If the usage model type of your product is changed after all the associated objects are created, manually check and update the associated objects before running the validator. If the associated objects aren’t verified, the validator can produce incorrect results.

=== ARTICLE: ind.um_consumption_management.htm ===
---
article_id: ind.um_consumption_management.htm
title: Manage Consumption for Usage-Based Products
source_url: https://help.salesforce.com/s/articleView?id=ind.um_consumption_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_management.htm
fetched_at: 2026-09-07
---

# Manage Consumption for Usage-Based Products

Track and manage consumption data, rate consumption accurately, and generate invoice-ready summaries for billing. Consumption management provides standard flows that you can schedule to run. You can also create usage and ratable summaries as needed. The ad hoc summary generation helps account executives generate reports to forecast consumption of a resource or resolve customer disputes.

Consumption Management Records
Usage Management creates certain object records that the Consumption Management process uses to track and manage the grant consumption. You can use these records to view and understand how the process manages the provided grants.
Buckets and Drawdowns
A bucket acts as a digital wallet that holds a customer's available grants or entitlements. Consumption Management creates usage entitlement buckets after the product is sold and assetized. When usage summaries are created, Consumption Management performs a drawdown to deduct the consumed units from these buckets. If the usage exceeds the available bucket balance, the remaining quantity is accounted as overage.
Consumption Management Lifecycle
Consumption management lifecycle is the structured process that tracks, monitors, and processes consumption data for consumption-based products and services. The process also manages grants and entitlements that help your users understand how the drawdowns take place for each usage resource and identify the overages.
Manage Consumption-Related Summaries
While the consumption management process automatically generates and updates consumption-related summaries, you can also generate them manually. Generate and view ad hoc summaries to support customer investigations or audits.
Unified Usage Dashboard
A single, consolidated source of truth for post-sale usage management. Track consumption, negotiated rates, and grant balances, and ensure data integrity across your records. Depending on how your products are structured, you can access this unified experience from either an accounts or an asset record page.
Consumption Management Considerations
Here are the key things to consider when you use Consumption Management for your organization.

=== ARTICLE: ind.um_consumption_management_standard_flow_templates.htm ===
---
article_id: ind.um_consumption_management_standard_flow_templates.htm
title: Consumption Management Flows
source_url: https://help.salesforce.com/s/articleView?id=ind.um_consumption_management_standard_flow_templates.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_cnsption_mngmnt_lifecycle.htm
fetched_at: 2026-09-07
---

# Consumption Management Flows

To process consumption data and generate invoice-ready summaries, the consumption management process uses schedule-triggered flows.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
IMPORTANT Before you schedule the flows, change the default context in which the flows run to System Context without Sharing. See Change the Flow Run Context.

To process consumption data, save each flow as a new flow and schedule it based on your organization’s needs. Schedule the Entitlement Refresh flow to run before the Orchestrate Usage Management flow. See Schedule-Triggered Flows.

Schedule Entitlement Refresh flow—runs the entitlement refresh batch job at the scheduled date and time.
Call Entitlement Refresh Service—calls the Refresh Usage Entitlement Bucket invocable action to refresh usage entitlements.
Orchestrate Usage Management flow—processes consumption data and creates invoice-ready summaries by using these subflows.
Generate Usage Summary flow—creates zero-value summaries and updates usage summaries by aggregating transaction journal records.
Generate Usage Ratable Summary flow—processes drawdowns, applies the net unit rate retrieved by using the rating request, and updates the usage ratable summary and the asset-related wallets.
Generate Liable Summary—summarizes the consumption overages in the usage summary and usage ratable summary.

=== ARTICLE: ind.um_consumption_mgmnt_impl_considerations.htm ===
---
article_id: ind.um_consumption_mgmnt_impl_considerations.htm
title: Consumption Management Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.um_consumption_mgmnt_impl_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_consumption_management.htm
fetched_at: 2026-09-07
---

# Consumption Management Considerations

Here are the key things to consider when you use Consumption Management for your organization.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Usage management creates empty usage, ratable, and liable summary records in advance, but only up to the active billing period. For example, if an asset's effective period is from July 1, 2025, to June 30, 2026, and you trigger the Orchestrate Usage flow on April 9, 2026, the system generates zero-value summaries only through the April 2026 billing period. It doesn't create summaries for May or June until you run the flow again in those respective months. 
Usage Summary records are created only when the liable summary period term is longer than the ratable summary period term and the ratable summary period term is longer than the usage summary period term.
The timestamp on the transaction journal records is in the Coordinated Universal Time (UTC) time zone.
To view transaction journal entries, the Standard User profile must have Read access to the Quantity, Quantity Unit, Transaction Amount, Start Date, and End Date fields on the Transaction Journal object.
To maintain the accuracy of transaction journal data, set the scale to 6 for the Quantity field of the Transaction Journal object.
Consumption Management uses these Data Processing Engine definitions:
Generate Usage Summary
Generate Ratable Summary
Generate Liable Summary
NOTE To use the Create Usage Summary definition, set field-level security for all the fields on the Transaction Journal object. See Field Permissions.
When a usage entitlement account record isn't processed after it's created, the billing period start date and end date fields default to December 31, 1969, 4 PM PST. The system uses January 1, 1970, 12 AM GMT as a placeholder to indicate that the record is unprocessed. The fields update with the correct values after the Create Summary flow is triggered.
If an order is assetized with a start date earlier than the date the order was created, you must run the Call Entitlement Refresh Service standard flow to refresh the active transaction usage entitlements. You must also call the flow for the back-dated products that are part of group segments. Usage entitlement buckets aren’t refreshed for expired segments.
Consumption Management considers only the date of an asset, regardless of the time the product is ordered. For example, if a customer buys a mobile plan at 3 PM on October 10, 2025, the order start date and time is October 10, 2025, at 3:00 PM. However, Consumption Management considers the start date for that asset to be October 10, 2025, at 12:00 AM.
If you encounter issues with the usage liable summary, such as the overage amount shown is zero, ask your Salesforce admin to enable Null Measure Handling. See Enable Null Measure Handling.
In orgs that use multiple currencies, match the currency of the user who runs the Generate Liable Summary Data Processing Engine definition to the currency of the Salesforce admin. If those currencies don't match, the definition fails. We don't recommend running the definition as the integration user, because that user can have only one currency in an org.
SEE ALSO
Orchestrate Usage Management Flow Stages

=== ARTICLE: ind.um_consumption_proration_calculations.htm ===
---
article_id: ind.um_consumption_proration_calculations.htm
title: Consumption Proration Calculations
source_url: https://help.salesforce.com/s/articleView?id=ind.um_consumption_proration_calculations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_buckets_and_drawdowns.htm
fetched_at: 2026-09-07
---

# Consumption Proration Calculations

Proration is used to ensure that customers are only billed or granted resources for the fraction of a billing period that a product was active. Consumption Management uses a proration engine that performs the calculation and provides accurate billing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license

Consumption is prorated when either grants are added or rates are updated between the billing cycles.

EXAMPLE

Mid-Cycle Grant Amendments

SCENARIO	PRORATION CALCULATION	RESULT
A customer purchases an anchor plan starting July 20 that grants them 4,000 text messages per month. The initial child bucket is created with a validity of July 20 to August 19, containing 4,000 texts. On August 3, the customer decided to amend the quote to purchase an additional quantity of the product.	Instead of granting the complete 4,000 texts for the new purchase, the proration engine cuts the original transaction's validity and creates a child bucket effective from August 3 to August 20. The new bucket is only active for 16 days of the billing cycle and therefore, the system's proration engine calculates a prorated balance of 2,193 text messages.	When the customer consumes texts between August 3 and August 20, Consumption Management draws down from a pooled total balance that includes the prorated 2,193 messages.

Mid-Cycle Rate Amendments

SCENARIO	PRORATION CALCULATION	RESULT
A customer is consuming an active plan that’s valid from Jan 1 to Jan 31. In the middle of a customer’s billing period, a sales rep overrides and amends the negotiated rate of a resource from $10 to $9.	The proration engine splits the consumption for the different rate durations. Consumed units logged before Jan 15 are aggregated and rated at the $10 rate, while usage logged after the amendment date is aggregated separately and rated at the new $9 rate.	Consumption Management generates two separate Liability Summary rows for the split periods, ensuring the total invoice accurately reflects the prorated mid-cycle rate change.

=== ARTICLE: ind.um_create_a_product_usage_resource.htm ===
---
article_id: ind.um_create_a_product_usage_resource.htm
title: Create a Product Usage Resource
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_a_product_usage_resource.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Product Usage Resource

Associate existing usage resources with products, with a limit of one token resource per product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create product usage resource:	Usage Management Designer
From the App Launcher, find and select Product Usage Resource.
Click New.
Select a product created with a usage model type.
Select a usage resource related to the selected product.
Select the effective start date and end date.
The Usage Resource isn't part of the product after the effective end date.
Select a status.
	
Draft	Indicates that the record is still open for modifications. This is the default value.
Active	Indicates that Usage Management is using this record for resource consumption calculations and you can make limited modifications.
Inactive	Indicates that the record isn't in use.
If necessary, select Optional.
The Optional checkbox is applicable only when the selected product is one of the commitment usage model types. Selecting the checkbox indicates that the usage resource is optional and may or may not be included in the commitment-based product.
If necessary, select a token resource.
This token resource is used to charge the selected usage resource.
Save your changes.

=== ARTICLE: ind.um_create_a_usage_commitment_asset_related_object.htm ===
---
article_id: ind.um_create_a_usage_commitment_asset_related_object.htm
title: Create a Usage Commitment Asset Related Object
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_a_usage_commitment_asset_related_object.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Usage Commitment Asset Related Object

Apply discounted rates and additional grants available for the commitment product to the resources consumed by an anchor product. To provide these benefits, link the commitment product to the anchor product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage commitment asset related object:	Usage Management Designer
From the App Launcher, find and select Usage Commitment Asset Related Object.
Click New.
Select an asset and an object that is to be related to the asset.
Select an effective start and end date.
Save your changes.
SEE ALSO
Sell Commitment-Based Usage Products
Set Up Usage-Based Product and Services

=== ARTICLE: ind.um_create_a_usage_product_grant_binding_policy.htm ===
---
article_id: ind.um_create_a_usage_product_grant_binding_policy.htm
title: Create Usage Product Grant Binding Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_a_usage_product_grant_binding_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create Usage Product Grant Binding Policy

Define the association between a usage resource’s grant with a sellable product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create usage product grant binding policies:	Usage Management Designer
IMPORTANT The binding target can't be changed after the order is activated and assetized. If you configure the wrong binding target for your policy, you must redesign the product from scratch. Verify your choice before activating any orders that use this policy. For guidance on selecting a binding target and understanding how consumption is aggregated across shared grants, see Grant Binding.
From the App Launcher, find and select Usage Product Grant Binding Policies.
Click New.
Enter a name.
Select a sellable product.
Select a grant binding type.
	
Self	Apply the product's usage grant to a single asset so that each purchased product tracks its consumption independently. This is the default for anchor and pack product configurations.
Target	Share usage grants across multiple assets, such as an account, contract, or custom object. This binding type requires an associated grant binding target.
Select a grant binding target if the grant binding type is Target.
	
Product	A sellable product within the Revenue Management to which the grant is to be associated.
Custom	An external product outside the Revenue Management to which the grant is to be associated.
Contract	A specific agreement or service contract within Revenue Management to which the usage grant is to be associated.
Account	A customer or organization within Revenue Management to which the usage grant is to be associated.
Save your changes.

=== ARTICLE: ind.um_create_on_demand_usage_ratable_summary.htm ===
---
article_id: ind.um_create_on_demand_usage_ratable_summary.htm
title: Create an On-demand Usage Ratable Summary
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_on_demand_usage_ratable_summary.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_manage_consumption_related_summaries.htm
fetched_at: 2026-09-07
---

# Create an On-demand Usage Ratable Summary

To calculate rates for unrated usage summary records outside the specified schedule, create a usage ratable summary.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage ratable summaries:	Usage Management Run Time User
From the App Launcher, find and select Usage Summaries.
On the Usage Summaries list view page, click Calculate Rate.
NOTE The Calculate Rate button is available only for users with System Admin access.
A new usage ratable summary is created.

To view the newly created usage summary, go to the Usage Ratable Summary list view.

=== ARTICLE: ind.um_create_on_demand_usage_summary.htm ===
---
article_id: ind.um_create_on_demand_usage_summary.htm
title: Create an On-demand Usage Summary
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_on_demand_usage_summary.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_manage_consumption_related_summaries.htm
fetched_at: 2026-09-07
---

# Create an On-demand Usage Summary

Create comprehensive usage summaries that the admin can use to generate reports.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage summaries:	

Usage Management Run Time User

Data Pipelines Base User

IMPORTANT To access the Transaction Journals list view page, assign the Profile user View All Records Standard Object permission for the Transaction Journals object. See Edit Object Permissions in Profiles.
From the App Launcher, find and select Transaction Journals.
On the Transaction Journals list view page, click Summarize.
NOTE The Summarize button is available only for users with System Admin access.
A new usage summary is created.

To view the newly created usage summary, go to the Usage Summary list view.

=== ARTICLE: ind.um_create_product_usage_resource_policy.htm ===
---
article_id: ind.um_create_product_usage_resource_policy.htm
title: Create a Product Usage Resource Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_product_usage_resource_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Product Usage Resource Policy

Define the policies that apply when a usage resource is associated with a sellable product. After the product is sold, these rules automatically apply to the resource. The policies you select here override the policies defined in the individual usage resource policy record.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create product usage resource policies:	Usage Management Designer
From the App Launcher, find and select Product Usage Resource Policies.
Click New.
Select a product usage resource.
If necessary, select a product selling model.
Select rating frequency policy, usage aggregation policy, usage commitment policy, and usage overage policy for the selected product usage resource.
Save your changes.

=== ARTICLE: ind.um_create_rating_frequency_policy.htm ===
---
article_id: ind.um_create_rating_frequency_policy.htm
title: Create Rating Frequency Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_rating_frequency_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create Rating Frequency Policy

The rating frequency policy defines how often the rating for a sellable product and a usage resource should be computed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create rating frequcny policies:	Usage Management Designer
From the App Launcher, find and select Rating Frequency Policies.
Click New.
Select a usage resource.
Select a product that you want to configure.
Select a rating period. The available options are Daily and Monthly.
Optionally, enter a rating delay duration and select a rating delay duration unit.
Save your changes.

=== ARTICLE: ind.um_create_unit_of_measure_class.htm ===
---
article_id: ind.um_create_unit_of_measure_class.htm
title: Create a Unit of Measure Class
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_unit_of_measure_class.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Unit of Measure Class

Unit of measure class defines the groupings of units of measure (UOM). For example, the Currency unit of measure class groups various currencies, such as euros, dollars, and rupees.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create a usage product grant binding policies:	Usage Management Designer
From the App Launcher, find and select Unit of Measure Classes.
Click New.
Enter a name, a unique identifier code, and a description.
If necessary, select a default unit of measure.
If you don’t select a default unit of measure, Salesforce uses the unit of measure within this class as the default unit for all conversions. If no unit of measure is available, create a new record.
Select a type.
	
Usage	For measuring consumption in non-currency units, such as API calls, GB, or hours.
Currency	For measuring consumption value in currency, such as USD or EUR.
Token	For measuring redeemable credits.
When you select a Unit of Measure, align the category with the Unit of Measure class. For example, the Data class uses the Usage category, with GB, MB, and TB as the units associated with the usage type. The Currency class includes units such as USD, INR, and EUR and requires the Currency category because it represents currency types.
Select a status.
	
Draft	Indicates that this record is still open for modifications. This is the default value.
Active	Indicates that Usage Management is using this record for resource consumption calculations and you can make limited modifications.
Inactive	Indicates that the record is not in use.
Save your changes.
SEE ALSO
Create Units of Measure

=== ARTICLE: ind.um_create_units_of_measure.htm ===
---
article_id: ind.um_create_units_of_measure.htm
title: Create Units of Measure
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_units_of_measure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create Units of Measure

A unit of measure quantifies the consumption of a usage resource. You can define units of measure to support a wide range of usage resources. For example, a unit of measure can be time-based, volume-based, transaction-based, or count-based.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage product grant binding policies:	Usage Management Designer
From the App Launcher, find and select Units of Measure.
Click New.
Enter a name, a unique identifier code, and a description.
The Unit Code field must exactly match the currency ISO code configured in your org settings, such as USD. Mismatched casing or spelling hides rate cards during selling without an error message.
To group the unit of measure under a class, select a unit of measure class.
If necessary, to show the unit of measure in a specific order in a list, enter a sequence number.
Enter a conversion factor that converts the value of the unit of measure into the default unit of measure of the unit of measure class.
Select a type of measurement.
You can add new values to the type picklist. See Add or Edit Picklist Values.
Select a status.
	
Draft	Indicates that this record is still open for modifications. This is the default value.
Active	Indicates that Usage Management is using this record for resource consumption calculations and you can make limited modifications.
Inactive	Indicates that the record is not in use.
Save your changes.
SEE ALSO
Create a Unit of Measure Class

=== ARTICLE: ind.um_create_usage_aggregation_policy.htm ===
---
article_id: ind.um_create_usage_aggregation_policy.htm
title: Create Usage Aggregation Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_usage_aggregation_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create Usage Aggregation Policy

Define the method used to aggregate consumption of a usage resource over a period.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage aggregation policies:	Usage Management Designer
From the App Launcher, find and select Usage Aggregation Policies.
Click New.
Enter a name and a unique identifier code.
Select an accumulation method.
Sum	Aggregates all events in the specified accumulation period.
Peak	Finds the entry with the maximum consumption within the specified accumulation period.
Select a usage accumulation period.
Select a status.
	
Draft	Indicates that this record is still open for modifications. This is the default value.
Active	Indicates that Usage Management is using this record for resource consumption calculations and you can make limited modifications.
Inactive	Indicates that the record is not in use.
Save your changes.

=== ARTICLE: ind.um_create_usage_commitment_policy.htm ===
---
article_id: ind.um_create_usage_commitment_policy.htm
title: Create a Usage Commitment Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_usage_commitment_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Usage Commitment Policy

Define the set of rules that determine how commitments are applied to a usage resource.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage commitment policies:	Usage Management Designer
From the App Launcher, find and select Usage Commitment Policies.
Click New.
Enter a name for the policy.
Select a value that indicates the rate applicable after the initial commitment is fulfilled.
	
Bounded Object Rate	Bill overage at the rate defined on the object bound to the line item. Ideal when the commitment has a discounted rate and consumption over the commitment has a separately defined rate.
Lowest Commitment Rate	Bill overage at the lowest negotiated commitment rate after the customer consumes beyond the committed quantity. Ideal for a single unified tier structure where the commitment and overage rates are identical.
Save your changes.
EXAMPLE
Bounded Object Rate: A customer purchases a mobile data plan. The first 10 GB is included in their commitment at $1 per GB, which is the committed rate. If they consume 12 GB, the extra 2 GB is billed at the anchor product rate of $15 per GB. The $15 per GB rate is the standard retail rate on the bound asset. This model suits plans where committed usage is discounted, but overage carries a higher rate.
Lowest Commitment Rate: A customer purchases a cloud storage product with a standard rate of $10 per GB. They commit to 1,000 GB at a discounted rate of $8 per GB. If they consume 1,200 GB, the extra 200 GB is also billed at $8 per GB. Use the Lowest Commitment Rate when you want one consistent rate across both committed consumption and overage.
SEE ALSO
Create a Usage Overage Policy
Commitment Product Drawdowns

=== ARTICLE: ind.um_create_usage_grant_refresh_policy.htm ===
---
article_id: ind.um_create_usage_grant_refresh_policy.htm
title: Create Usage Grant Refresh Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_usage_grant_refresh_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create Usage Grant Refresh Policy

Define whether the grants provided with the usage resource can be refreshed and the frequency of the grant refresh.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage grant refresh policies:	Usage Management Designer
From the App Launcher, find and select Usage Grant Refresh Policies.
Click New.
Enter a name and a unique identifier code.
If grants can be refreshed, select Refresh Allowed.
Enter the frequency for the renewals and the frequency unit.
For example, if you want the grants to be refreshed every quarter, in the Renewal Frequency field, enter 3. For the Renewal Frequency Unit, select Month.
Select a status.
	
Draft	Indicates that this record is still open for modifications. This is the default value.
Active	Indicates that Usage Management is using this record for resource consumption calculations and you can make limited modifications.
Inactive	Indicates that the record is not in use.
Save your changes.

=== ARTICLE: ind.um_create_usage_grant_rollover_policy.htm ===
---
article_id: ind.um_create_usage_grant_rollover_policy.htm
title: Create Usage Grant Rollover Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_usage_grant_rollover_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create Usage Grant Rollover Policy

Each grant provided with the product has a validity period. Usage grant rollover policies define whether the usage resource’s grants expire or can be rolled over after the initial validity period is completed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage grant rollover policies:	Usage Management Designer
From the App Launcher, find and select Usage Grant Rollover Policies.
Click New.
Enter a name and a unique identifier code.
If the grant units associated with the usage resource can be rolled over, select Rollover Allowed.
If you select Rollover Allowed, specify these values:
If ‌grants must expire after a specific number of rollovers, select Allow Rollover Expiry.
Enter the number of rollovers post when the rolled over grants are considered expired.
Select a status.
	
Draft	Indicates that this record is still open for modifications. This is the default value.
Active	Indicates that Usage Management is using this record for resource consumption calculations and you can make limited modifications.
Inactive	Indicates that the record is not in use.
Save your changes.

=== ARTICLE: ind.um_create_usage_overage_policy.htm ===
---
article_id: ind.um_create_usage_overage_policy.htm
title: Create a Usage Overage Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_usage_overage_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Usage Overage Policy

Define the set of rules that determine how units consumed beyond the granted limit are managed for a usage resource.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage overage policies:	Usage Management Designer
From the App Launcher, find and select Usage Overage Policies.
Click New.
Enter a name for the policy.
Select a value that indicates whether the overage is chargeable.
Save your changes.

=== ARTICLE: ind.um_create_usage_resource.htm ===
---
article_id: ind.um_create_usage_resource.htm
title: Create a Usage Resource
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_usage_resource.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Usage Resource

Usage resource is an entitlement or service that you grant your customers along with a product that you sell. Before you define rates and rate adjustments for usage resources, create usage resources for your products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create usage resources:	Usage Management Designer
From the App Launcher, find and select Usage Resources.
Click New.
Enter a name and a unique identifier code.
If necessary, select a unit of measure class and the default unit of measure.
Select a resource category.
Currency - for resources of type Currency
Token - for resources of type Tokens
Usage - for resources of type Usage
Select a status.
	
Draft	Indicates that this record is still open for modifications. This is the default value.
Active	Indicates that Usage Management is using this record for resource consumption calculations and you can make limited modifications.
Inactive	Indicates that the record is not in use.
To associate the usage resource to a sellable product, select a usage definition product.
If necessary, select a usage aggregation policy.
Save your changes.

=== ARTICLE: ind.um_create_usage_resource_policy.htm ===
---
article_id: ind.um_create_usage_resource_policy.htm
title: Create a Usage Resource Policy
source_url: https://help.salesforce.com/s/articleView?id=ind.um_create_usage_resource_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Usage Resource Policy

Define the policies applicable to a usage resource, regardless of whether it's associated with a sellable product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create usage resource policies:	Usage Management Designer
From the App Launcher, find and select Usage Resource Policies.
Click New.
Select a usage resource and a usage commitment policy.
If required, select rating frequency policy, usage aggregation policy, and usage overage policy for the selected usage resource.
Save your changes.

=== ARTICLE: ind.um_define_a_product_usage_grant.htm ===
---
article_id: ind.um_define_a_product_usage_grant.htm
title: Create a Product Usage Grant
source_url: https://help.salesforce.com/s/articleView?id=ind.um_define_a_product_usage_grant.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_configure_usage_records.htm
fetched_at: 2026-09-07
---

# Create a Product Usage Grant

Define the details of a grant associated with a resource, product, or service, such as the granted quantity, renewal and rollover policy, and the grant's validity period.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create product usage grants:	Usage Management Designer
From the App Launcher, find and select Product Usage Grants.
Click New.
Enter a unique label for the usage grant.
Select a product usage resource.
Select a drawdown order.
	
Expiring First	Process the consumption of usage resources from the entitlements with the expiration date closest to the current date. This is the default value.
Granted First	Process the consumption of usage resources from the entitlements that were granted first in the set of granted entitlements.
Granted Last	Process the consumption of usage resources from the entitlements that were granted last in the set of granted entitlements.
Enter the quantity in units associated with the grant or commitment.
Select a type.
	
Grant	A discount can be negotiated for the usage resource when the usage resource is associated with an anchor product.
Commit	

A discount can be negotiated for the usage resource when the associated anchor product is committed for a specific quantity, spend, or tokens.

If you select Commit, the usage resource to be associated must be of the Commit category.
Select a unit of measure class.
Select ‌the default unit of measure for the selected unit of measure class.
Select a value that indicates whether the overage is chargeable.
Select a status.
	
Draft	Indicates that this record is still open for modifications. This is the default value.
Active	Indicates that Usage Management is using this record for resource consumption calculations and you can make limited modifications.
Inactive	Indicates that the record is not in use.
If necessary, select a usage definition product and a product selling model.
If necessary, select a refresh policy and a rollover policy.
Select a validity period unit and enter a correspoding validity period term.
Select an effective start date.
Save your changes.

=== ARTICLE: ind.um_discover_and_explore.htm ===
---
article_id: ind.um_discover_and_explore.htm
title: Begin Using Usage Management
source_url: https://help.salesforce.com/s/articleView?id=ind.um_discover_and_explore.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_management.htm
fetched_at: 2026-09-07
---

# Begin Using Usage Management

Turn on Usage Management to efficiently set up, track and manage consumption-based products. Customize the experience of using Usage Management for all users using permission sets to give them precise access to what they need.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Enable Usage Management
Give your users access to the Usage Management objects and features.
Permission Set Licenses, Personas, and User Permissions
Manage the Usage Management functionality securely with permission set licenses. Assign user permissions to specific user personas to enable them to complete the work that's assigned to their role.

=== ARTICLE: ind.um_enable_usage_management.htm ===
---
article_id: ind.um_enable_usage_management.htm
title: Enable Usage Management
source_url: https://help.salesforce.com/s/articleView?id=ind.um_enable_usage_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_discover_and_explore.htm
fetched_at: 2026-09-07
---

# Enable Usage Management

Give your users access to the Usage Management objects and features.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To enable Usage Management:	Customize Application
From Setup, in the Quick Find box, enter Usage Management, and then select Usage Management Settings.
Enable Usage Management.

To access the rate management objects and features, enable Rate Management. See Enable Rate Management.

=== ARTICLE: ind.um_guided_workflow_considerations.htm ===
---
article_id: ind.um_guided_workflow_considerations.htm
title: Guided Workflow Considerations and Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.um_guided_workflow_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_product_setup_with_guided_workflow.htm
fetched_at: 2026-09-07
---

# Guided Workflow Considerations and Limits

Review the record limits, supported policy types, and custom field constraints when you configure your usage product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Advanced license and the Revenue Cloud Billing license
Considerations
You can only edit the usage-related records until they’re in the draft state.
You can add up to 3 mandatory custom fields in the workflow interface. The workflow interface only shows the required custom fields. Optional custom fields are hidden. Supported data types for custom fields include Text, Text Area, Number, Checkbox, Date, Percent, Currency, and Picklist. However, the Product Usage Resource object doesn’t support custom fields.
For product usage resource and product usage grant records, the time for the effective start date defaults to 12:00 AM and the effective end date defaults to 11:59 PM, in your locale.
If you have a custom page layout or custom record page, add the Configure Usage Properties action manually. See Customize Page Layouts and Create and Add Actions in Lightning App Builder.
For ease of setup, Usage Management creates these policies with the names listed in the table. If you already have existing policies with the same configuration, the workflow doesn’t create new policies and uses the existing policies.
POLICY TYPE	POLICY NAME	CONFIGURATION
Usage Aggregation Policy	Aggregate Usage Monthly by Sum	
Usage Accumulation Method—Sum
Usage Accumulation Period—Monthly
Status—Active

Usage Grant Refresh Policy	Renew Grants Monthly	
Renewal Frequency—1
Renewal Frequency Unit—Month

Usage Grant Rollover Policy	Rollover Grants without Expiry	
Rollover Allowed—selected
Allow Rollover Expiry—unselected
Maximum Rollover count—Empty

Usage Overage Policy	Overage Chargeable	
Chargeable—Yes

Usage Commitment Policy	Lowest Commitment Fulfilled Rate	
Commitment Fulfilled Rate—Lowest commitment

Rating Frequency Policy	Rate Usage Monthly	
Rating Period—Monthly
Rating Delay Duration—Empty
Rating Delay Duration Unit—Empty
Limitations

To manage scale, the workflow has these record limits.

The guided workflow doesn’t support:
Commitment-based usage products
Inactive records
Configuring rate management records, price books, and product selling models changes
Customizing field layouts
Configuring global rate cards that all products use if they’re using the same resource
The Add Usage Resource page shows a maximum of 200 usage resources, and users can select a maximum of 10 resources at one time.
The guided workflow supports a maximum of 20 Product Usage Resource (PUR) record creations.
Each PUR supports a maximum of five Product Usage Grant (PUG) records.

=== ARTICLE: ind.um_key_objects_in_consumption_management.htm ===
---
article_id: ind.um_key_objects_in_consumption_management.htm
title: Consumption Management Records
source_url: https://help.salesforce.com/s/articleView?id=ind.um_key_objects_in_consumption_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_consumption_management.htm
fetched_at: 2026-09-07
---

# Consumption Management Records

Usage Management creates certain object records that the Consumption Management process uses to track and manage the grant consumption. You can use these records to view and understand how the process manages the provided grants.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
OBJECT	DESCRIPTION
Usage Entitlement Account	A usage entitlement account is a customer instance of the purchased product. Usage Management creates this record after an order is assetized. The object record includes the billing cycle details for the product, such as billing frequency, billing day of the month, start and end date of billing period and the service. A usage entitlement account has individual usage entitlement buckets for each usage resource.
Usage Entitlement Bucket	A usage entitlement bucket represents a wallet that records the credits and debits of a usage resource. If grants are rolled over or renewed, units are added to the bucket balance. When the customer consumes the usage resource, units are debited from the bucket balance.
Usage Entitlement Entry	A usage entitlement entry represents a transaction entry that records each credit and debit entry for the usage entitlement bucket.
Transaction Usage Entitlement	A transaction usage entitlement stores information about how grants are tracked and managed. The object record includes the associated usage grant rollover policy, usage grant refresh policy, drawdown order in which the grant consumption is debited, and other details.

=== ARTICLE: ind.um_manage_consumption_related_summaries.htm ===
---
article_id: ind.um_manage_consumption_related_summaries.htm
title: Manage Consumption-Related Summaries
source_url: https://help.salesforce.com/s/articleView?id=ind.um_manage_consumption_related_summaries.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_consumption_management.htm
fetched_at: 2026-09-07
---

# Manage Consumption-Related Summaries

While the consumption management process automatically generates and updates consumption-related summaries, you can also generate them manually. Generate and view ad hoc summaries to support customer investigations or audits.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Create an On-demand Usage Summary
Create comprehensive usage summaries that the admin can use to generate reports.
Create an On-demand Usage Ratable Summary
To calculate rates for unrated usage summary records outside the specified schedule, create a usage ratable summary.
View Liable Summaries
The Orchestrate Usage Management flow automatically creates the liable summaries by processing the aggregated usage consumption logs and the rates applicable from the usage ratable summaries.

=== ARTICLE: ind.um_pack_product_drawdowns.htm ===
---
article_id: ind.um_pack_product_drawdowns.htm
title: Pack Product Drawdowns
source_url: https://help.salesforce.com/s/articleView?id=ind.um_pack_product_drawdowns.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_buckets_and_drawdowns.htm
fetched_at: 2026-09-07
---

# Pack Product Drawdowns

Pack products are add-ons purchases that supplement an existing anchor product, such as adding a temporary international roaming pack or extra data.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license

When a pack is added, it doesn’t overwrite the anchor product. Instead, Consumption Management creates a child bucket for the pack's specific grants. This new child bucket accumulates into the same parent bucket as the anchor product. The parent bucket now reflects the combined total of both the anchor and the pack.

In this instance, the parent bucket now has multiple child buckets to choose from. Therefore, Consumption Management uses the Drawdown Order you specified to decide the bucket to deduct the consumption from first.

EXAMPLE A customer determines during an existing plan cycle that their anchor plan's 4,000 text messages are insufficient and purchases a temporary add-on pack for 2,000 additional units. Consumption Management creates a second child bucket for the new grant, linking it to the anchor’s parent bucket with a total aggregated balance of 6,000 units. As the add-on pack is set to expire at the end of the week, the default Expiring First drawdown order ensures that usage is deducted from the 2,000-message pack first.

=== ARTICLE: ind.um_run_validator.htm ===
---
article_id: ind.um_run_validator.htm
title: Run the Usage Product Validator
source_url: https://help.salesforce.com/s/articleView?id=ind.um_run_validator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_validate_your_setup.htm
fetched_at: 2026-09-07
---

# Run the Usage Product Validator

Verify your product's usage and rating design time setup.

REQUIRED EDITIONS

Make sure that you add the validator to your product record page and add a usage model type for the product that is to be validated.

Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
View and Run Usage Product Validator	

Usage Management Design Time User

Rate Management Design Time User

Create, read, update, and delete on all usage management design time objects

Create, read, update, and delete access for all rate management objects

From the App Launcher, find and select Products.
Select a product.
On the product record page, under Usage Product Validator, click Validate.

This completes the basic setup for Usage Management. To proceed with the rest of the Revenue Cloud setup, see Set Up Revenue Management.

=== ARTICLE: ind.um_set_up_experience_cloud_for_wallet_management.htm ===
---
article_id: ind.um_set_up_experience_cloud_for_wallet_management.htm
title: Set Up Wallet View for Experience Cloud
source_url: https://help.salesforce.com/s/articleView?id=ind.um_set_up_experience_cloud_for_wallet_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_wallet_management.htm
fetched_at: 2026-09-07
---

# Set Up Wallet View for Experience Cloud

Give your customers a way to independently track their balances, usage, and entitlements. To set up the wallet interface, configure the required Experience Cloud security settings and add the Wallet view to your site’s navigation menu. This feature is available to users with Customer Community or Partner Community licenses.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To view wallet management dashboard:	Wallet Management User
Add Wallet Components to Record Pages
Configure record layouts in Experience Cloud to show wallet balances, usage, and entitlement data for your customers.
Set Up Navigation for Wallets
By using the Billing self-service portal, configure the navigation menu to include the Wallets page.
Configure Security for External Access

Set up the components and navigation required for external users to view their wallet information in Experience Cloud.

From Setup, in the Quick Find box, enter Sharing Settings, and then select Sharing Settings.
For both Usage Resource and Binding Object Custom Extension, set the Default External Access to Public Read-Only.

=== ARTICLE: ind.um_set_up_menu_access.htm ===
---
article_id: ind.um_set_up_menu_access.htm
title: Set Up Navigation for Wallets
source_url: https://help.salesforce.com/s/articleView?id=ind.um_set_up_menu_access.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_set_up_experience_cloud_for_wallet_management.htm
fetched_at: 2026-09-07
---

# Set Up Navigation for Wallets

By using the Billing self-service portal, configure the navigation menu to include the Wallets page.

In Setup, find and select All Sites.
In the Action column for your site, click Builder.
To open the Settings panel, click the settings icon.
From the Settings panel, click Navigation.
Click the dropdown icon for Default Navigation, and then click Edit.
Click Add Menu Item and enter the name and select the the type and page:
Name: Wallets
Type: Site Page
Page: Wallet
Save your changes.
SEE ALSO
Experience Cloud
Set Up Experience Cloud for Billing

=== ARTICLE: ind.um_sum_statuses_through_cnsmptn_mngmnt_lifecycle.htm ===
---
article_id: ind.um_sum_statuses_through_cnsmptn_mngmnt_lifecycle.htm
title: Consumption Management Lifecycle Statuses
source_url: https://help.salesforce.com/s/articleView?id=ind.um_sum_statuses_through_cnsmptn_mngmnt_lifecycle.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_cnsption_mngmnt_lifecycle.htm
fetched_at: 2026-09-07
---

# Consumption Management Lifecycle Statuses

The successful processing of consumption data involves status changes across the interlinked summaries—Usage Summary, Usage Ratable Summary, and Liable Summary. The entire flow, from raw usage data in the transaction journal to the calculation of net unit rates and the creation of invoice-ready data, is managed through these coordinated summaries.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Usage Summary

The usage summary stores the aggregated transaction journal entries and drawdown results for a specified period.

STATUS	WHAT DOES IT MEAN?	PROCESSING JOB
New	Zero-value usage summary record is created.	Create Empty Summaries batch job
Usage Summary In Progress	Usage summary is being updated with consumption data provisionally.	Create Usage Summary Data Processing Engine job
Usage Summary Complete	The time period to rate the consumption data along with the waiting period is achieved for the linked usage summary. The usage summary is frozen and sent for drawdown. After the Usage Summary reaches this state, no transaction journal entries are considered for the specified period.	Create Usage Summary Data Processing Engine job
Drawdown Complete	Consumption drawdowns are processed, and the overages are added to the usage summary. The usage summary is sent to generate the ratable summary.	Process Consumption Overages batch job
Ratable Summary Complete	Ratable summary is generated for the usage summary.	Create Ratable Summary batch job
Liable Summary Complete	Liable summary is generated for the usage summary.	Usage Liable Summary DPE Job
Usage Ratable Summary

The usage ratable summary stores the aggregated usage summaries and the calculated rates at which the overages are charged.

STATUS	WHAT DOES IT MEAN?	PROCESSING JOB
New	Zero-value usage ratable summary record is created.	Create Empty Summaries batch job
Rating In Progress	The provisional rating of the usage ratable summary is complete. During the provisional rating run, the rating process rates the usage summary cumulatively, and the calculated rate is reevaluated as new usage is recorded throughout the billing cycle.	Create Ratable Summary batch job
Summary Created	Usage ratable summary is updated with the aggregated usage summaries after the billing period is complete.	Create Ratable Summary batch job
Rating Complete	Usage ratable summary is updated with the net unit rate applicable for the overages.	Retrieve Net Unit Rates for Ratable Summary batch job
Rating Failed	Usage ratable summary failed to record the net unit rates and couldn’t be updated.	Net Unit Rate batch job
Liable Summary

The liable summary stores the calculated overages for the services and the amount that’s charged for these overages.

STATUS	WHAT DOES IT MEAN?	PROCESSING JOB
New	Zero-value usage summary record is created.	Create Empty Summaries batch job
Liable Summary In Progress	Liable summary is updated with provisional data, including the current running overage amount and the total unbilled usage quantity for the billing period to date.	Create Liable Summary DPE Job
Liable Summary Complete	Liable summary is updated with the details of overages and the applicable net unit rate.	Create Liable Summary DPE job
Ready for Invoicing	The billing cycle is completed for the liable summary, and the liable summary is ready for invoicing.	Create Liable Summary DPE job

=== ARTICLE: ind.um_token_commitment_drawdowns.htm ===
---
article_id: ind.um_token_commitment_drawdowns.htm
title: Token Commitment Drawdowns
source_url: https://help.salesforce.com/s/articleView?id=ind.um_token_commitment_drawdowns.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_buckets_and_drawdowns.htm
fetched_at: 2026-09-07
---

# Token Commitment Drawdowns

The consumption process for token commitments uses a two-step rating procedure. The process in the first step converts usage to tokens, and then in the second step, tokens to currency.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Step 1: PPU (Points Per Unit) - Usage to Token Conversion
Transaction journal records are aggregated to generate a usage summary for each resource within the billing period.
Consumption is drawn from the earliest expiring usage entitlement bucket associated with the anchor product, or from the grants provided by commitments.
The discount provided by the commitment is applied to the anchor's base rate to calculate the token charge for any overages.
The tokens are calculated for each resource and added to the Usage Summary.
Step 2: PPP (Price Per Point) - Token to Currency Conversion
Calculated PPU charges are aggregated across all resources to generate a row for the token resource in the usage summary.
Tokens are drawn from the earliest expiring usage entitlement bucket for tokens associated with the anchor, or from the commitments.
The token overages are rated into a real currency value, and then a liable summary is generated for invoicing. The resulting invoice shows the tokens or credit points rated in the final currency.
EXAMPLE A customer buys a Data Cloud Premium product with these configurations.
PRODUCT	RESOURCE	ANCHOR RATE	COMMIT RATE	COMMITTMENT
Data Cloud Premium	Data Credits	$5 per credit	$2.5 per credit (PPP)	1,000 credits per month
API Calls	3 credits per API Call (PPU)	3 credits per API Call (PPU)	 
Storage	5 credits per GB (PPU)	5 credits per GB (PPU)	 

The customer consumes 200 API Calls and 25 GB of storage in the first month. Here’s how the consumption is calculated.

RESOURCE	CONSUMPTION	BUCKET BALANCE	OVERAGE
API Calls	

200 API Calls

200 x 3 = 600 credits

	 	 
Storage	

25 GB

25 x 5 = 125 credits

	 	 
Data Credits	725 credits	275 credits	Nil

In the second month, consumption grew to 800 API Calls and 30-GB storage. So, here’s how the consumption is calculated.

RESOURCE	CONSUMPTION	BUCKET BALANCE	OVERAGE
API Calls	

800 API Calls

800 x 3 = 2400 credits

	 	 
Storage	

30 GB

30 x 5 = 15 credits

	 	 
Data Credits	2550 credits	1000-2550=-1550	Overage by 1550 credits

The consumption leads to an overage of 1550 credits. The commitment policy specifies that after the commitment is fulfilled the bounded targeted rates apply. Therefore, the amount that the customer is liable to pay is $7750 (1550 x $5).

=== ARTICLE: ind.um_token_committment_drawdown_use_cases.htm ===
---
article_id: ind.um_token_committment_drawdown_use_cases.htm
title: Token Commitment Drawdown Use Cases
source_url: https://help.salesforce.com/s/articleView?id=ind.um_token_committment_drawdown_use_cases.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_buckets_and_drawdowns.htm
fetched_at: 2026-09-07
---

# Token Commitment Drawdown Use Cases

The relationship between commitments and anchors, and how their consumption is processed varies depending on the binding target and the number of active products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
One Commit to One Anchor

A customer has a token commitment bound directly to an anchor product.

If the commitment is active and unexhausted, the consumption process draws directly from the committed tokens.
If the commitment is active but exhausted, the consumption process applies the rate available for the anchor product or the commit rate, as specified in the commitment policy.
One Commitment to Multiple Anchors

A customer buys a token commitment product and binds it to an account. The account has multiple assets (Asset A, Asset B, and Asset C) pooling their usage.

If the commitment is active and unexhausted, the consumption process draws directly from the committed tokens. However, because multiple assets are associated with the same product, they’re sorted in ascending order by their Asset Billing End Date.
If the commitment is active but exhausted, the consumption process applies the rate available for the anchor product or the commit rate, as specified in the commitment policy.
If there’s a conflict between end dates, the asset with the highest resource rate draws down first to minimize the overall cost of overages.

=== ARTICLE: ind.um_track_usage_with_unified_dashboard.htm ===
---
article_id: ind.um_track_usage_with_unified_dashboard.htm
title: Track Usage Components with Unified Usage Dashboard
source_url: https://help.salesforce.com/s/articleView?id=ind.um_track_usage_with_unified_dashboard.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_wallet_management.htm
fetched_at: 2026-09-07
---

# Track Usage Components with Unified Usage Dashboard

After an order is activated, assetized, and entitlements are granted, you can use the dashboard to track wallet balances, monitor overages, and verify applicable rates.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To access the unified usage dashboard:	Usage Management Run Time User

Before you access the unified dashboard, make sure that you’ve completed these prerequisites.

Select the latest Rating Discovery Procedure in Revenue Settings.
Add Usage Component to the Record Pages.
SEE ALSO
Grant Binding
Anchor Products with Packs
Access the Unified Usage Dashboard

Go to the usage dashboard and review the individual tabs for usage details, grants, and policies.

From the App Launcher, find and select the Usage Management App.
To view the dashboard, go to the relevant account page for pooled resources, or an asset page for independent resources.
Click Usage Details.
The Usage Details tab lists all assets that are bound to the account, such as assets, contracts, or any custom object.
To view the grants available for each resource, click Grants.
The Grants tab lists all associated grants with details, such as the associated product and the rollover and refresh policies, with the effective period dates.
To view the policies that govern the usage resources, click Policies.
The Policies tab shows a centralized list of the governing policies created for the target, such as aggregation policies, rating frequency policies, and overage policies.
View Applicable Rates

When a customer has multiple assets bound to the same account, such as a standard anchor product and an add-on pack with different rates and validity periods, Consumption Management automatically identifies and shows the winning rate. The proration engine evaluates these varying validity periods and shows you the currently applicable net unit rate.

On the Account page, click Rates.
The Rates section shows the finalized, winning rates for any consumption on the account or asset. This tab ensures that you’re viewing the net rate the rating engine uses for rate calculations. For example, a newer add-on pack rate takes precedence over an older anchor rate until the pack expires.
To view the specific negotiated rate for an individual asset, go to that asset record page, and then click Rates.
Monitor Wallet Balances

Track how many grants have the customer consumed and what remains available.

On the Account page, click Wallets.
The Wallet tab shows digital wallets that represent parent buckets created for the resources, such as data, calls, and compute time. The visual indicators show the percentage of resources consumed.
To open the parent Usage Entitlement Bucket record associated with the wallet, click View Details.
The record shows the aggregated balance of all associated grants in the Total Age of Balance field.
To view child buckets associated with the parent bucket, click Related in the Usage Entitlement Bucket record.
The Related tab shows child buckets under the Usage Entitlement Bucket section with the balances for individual purchases or add-on packs.
To review the detailed audit trail for either a parent or child bucket, click Wallet Statement in the Usage Entitlement Bucket record.
The Wallet Statement tab provides a chronological log of all credit entries and debit entries.

=== ARTICLE: ind.um_usage_management.htm ===
---
article_id: ind.um_usage_management.htm
title: Manage and Track Usage-Based Products in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.um_usage_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
fetched_at: 2026-09-07
---

# Manage and Track Usage-Based Products in Revenue Management

With a consumption-based product, a customer pays based on usage rather than a fixed subscription or upfront fee. Usage Management provides a comprehensive solution to define, rate, sell, track, and bill consumption-based products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license

Usage Management handles the entire lifecycle of a consumption-based product, from setup to final billing.

Usage Modeling
Set up consumable products and services, units of measure, usage resources, product usage grants, and policies that manage rollovers and renewals of grants or entitlements.
Rate Management
Calculate and manage rates for consumption-based products. Define rate cards, rate card entries for rate adjustments, and rating procedures and rating discovery procedures to calculate and retrieve net unit rate for a usage resource.
Usage Selling
Sell consumption-based products with upfront visibility of rating details. Usage product quotes, orders, and activation are part of Transaction Management. The usage selling process includes creating a quote, adding a usage product to that quote, managing rates and grants of the associated resources, and then creating an order. When an order is activated, Usage Management creates an asset for the individual product, and all object records are linked to the asset.
Consumption Management
Track consumption data, drawdown grants, and generate invoice-ready summaries for billing and analysis.
Wallet Management
Manage wallets for every purchased usage resource tied to an account. Wallet Management provides a consolidated view that lists and tracks resources by account.
Begin Using Usage Management
Turn on Usage Management to efficiently set up, track and manage consumption-based products. Customize the experience of using Usage Management for all users using permission sets to give them precise access to what they need.
Set Up Usage Management in Revenue Management
Usage Management provides the essential components for tracking and managing the consumption of your usage-based products. To implement this framework effectively, first set up usage management objects, such as usage resources, product usage grants, and their units of measure. This setup represents the foundational layer of your configuration and is a prerequisite for creating usage management policies. The policies ensure that consumption data can be accurately aggregated, grant policies can be correctly applied, and overall usage can be managed with efficiency.
Manage Consumption for Usage-Based Products
Track and manage consumption data, rate consumption accurately, and generate invoice-ready summaries for billing. Consumption management provides standard flows that you can schedule to run. You can also create usage and ratable summaries as needed. The ad hoc summary generation helps account executives generate reports to forecast consumption of a resource or resolve customer disputes.
Billing Schedules and Invoices for Usage-Based Products
For usage-based products, Billing considers late usage and extra orders.
Usage Management Limits
Before you plan and set up usage management, sell consumption-based products, or process their consumption, review the supported limits and features.
SEE ALSO
Set Up Usage Management in Revenue Management
Rate Management
Usage Selling
Consumption Management
Unified Usage Dashboard

=== ARTICLE: ind.um_usage_management_limits.htm ===
---
article_id: ind.um_usage_management_limits.htm
title: Usage Management Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.um_usage_management_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_management.htm
fetched_at: 2026-09-07
---

# Usage Management Limits

Before you plan and set up usage management, sell consumption-based products, or process their consumption, review the supported limits and features.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Usage Selling
A quote or an order can have up to:
200 quote line items or order items
200 quote line item rate card entries
800 quote line item rate adjustments
Usage Management doesn't support selling usage-based products as part of a product bundle.
You can't add a usage-based product as a child component within a bundled product. For example, adding a usage-based API consumption product as part of a software bundle.
You can't configure a usage-based product as the parent product of a bundle. For example, creating a bundle where the main product tracks consumption.
To sell multiple usage-based products together, add them as separate line items on the same quote or order rather than bundling them into a single product.
You can sell usage-based and non-usage products in the same order, but they must be separate line items.
Usage Selling doesn’t support these Transaction Management features:
Evergreen or onetime anchor products
Early renewals for ramp and non-ramp assets are supported for Usage Selling, but not for Consumption Management.
Renewals of expired assets is supported for Usage Selling, but not for Consumption Management.
Start-date amendments, including pulling in or pushing out the start date
End-date amendments
Account and asset transfers
Amendment of a usage-based product with a future-dated and back-dated change.
Upgrades, downgrades, and swaps
Backdated amendments, renewals, and cancellations
Amendment rollbacks
Revival of canceled assets
Pausing and resuming assets
Consumption Management

Consumption Management requires Usage Selling and has the same Usage Selling limitations. In addition, Consumption Management has these limitations:

Consumption Management objects don’t support creating records in Data Cloud.
Consumption Management doesn’t support processing of data from monetary and quantity commitment products.

=== ARTICLE: ind.um_usage_management_psls_and_personas.htm ===
---
article_id: ind.um_usage_management_psls_and_personas.htm
title: Permission Set Licenses, Personas, and User Permissions
source_url: https://help.salesforce.com/s/articleView?id=ind.um_usage_management_psls_and_personas.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_discover_and_explore.htm
fetched_at: 2026-09-07
---

# Permission Set Licenses, Personas, and User Permissions

Manage the Usage Management functionality securely with permission set licenses. Assign user permissions to specific user personas to enable them to complete the work that's assigned to their role.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Create Users and Profiles

To begin, create users for Usage Management. Then assign users the appropriate permission sets. To help you plan, refer to the permissions table for Usage Management.

When you create a user, you must also assign a profile. Profiles define default settings for users. Some organizations create their own profiles, while others choose to use profiles included with Salesforce.

Remember, users can have only one profile, but can have many permission sets assigned to them.

Assign Permissions
PERMISSION
SET LICENSE	USER PERMISSION	PERSONAS	WHAT PERSONAS CAN DO
Usage Management Design Time	Usage Management Designer	

Usage Management Admin

Usage Designers

	
Create, read, update, and delete all design time objects
Read all run time objects

Usage Management Run Time	Usage Management Run Time User	

Usage Management Admin

Usage Designers

Account Executive

Customers

	
Create, read, update, and delete all run time objects
Read all design time objects

Wallet Management User	Wallet Management User	

Usage Management Admin

Account Executive

Customers

	R​ead all design time and run time objects

To view the count of the Usage Management permission set licenses that are available in your Salesforce org, go to Company Information in Setup. If you need permission set licenses in addition to the ones provided by the Usage Management license enabled in your org, contact your Salesforce account executive.

SEE ALSO
View and Manage Users
Create or Clone Profiles
Permission Set Licenses

=== ARTICLE: ind.um_usage_management_setup.htm ===
---
article_id: ind.um_usage_management_setup.htm
title: Set Up Usage Management in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.um_usage_management_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_management.htm
fetched_at: 2026-09-07
---

# Set Up Usage Management in Revenue Management

Usage Management provides the essential components for tracking and managing the consumption of your usage-based products. To implement this framework effectively, first set up usage management objects, such as usage resources, product usage grants, and their units of measure. This setup represents the foundational layer of your configuration and is a prerequisite for creating usage management policies. The policies ensure that consumption data can be accurately aggregated, grant policies can be correctly applied, and overall usage can be managed with efficiency.

NOTE Customers purchase sellable products. Usage grants, usage resources, and policies are defined for these sellable products. Salesforce uses the Usage Resources object for consumption data processing and the Usage Product object for invoicing consumption overages.
Choose Your Setup Path

You can set up your usage-based product via two paths. Review the supported product types and limitations before you begin.

SETUP PATH	RECOMMENDED FOR
Guided workflow	
First-time setup of anchor and pack products
Step-by-step validation with cross-object checks at each stage
Out-of-the-box default policies that reduce manual configuration

Manual configuration	
Commitment-based usage products—quantity, monetary, or token
Advanced users who need direct control over individual policy records
TIP If you're setting up a usage-based product for the first time, use the guided workflow. Before you start, review the record limits, supported policy types, and custom field constraints. See Guided Workflow Considerations and Limits.

Complete all of the following steps before continuing to use Usage Management.

Usage-Based Product Setup with Guided Workflow
A logical, sequential workflow guides you through a structured journey—creating a base product and resource definition, defining policy, linking Product Usage Grant (PUG), and setting rates. Finally, you can activate all records created through the journey with one click. It also simplifies the setup by providing preselected, out-of-the-box default policies.
Configure Usage Management Records Manually
Use manual configuration when your setup requires direct control over individual records or involves product types that the guided workflow doesn't support.
Validate Your Usage Product Setup
Run the product validator after you complete your usage management setup by using the guided workflow or manual configuration. The validator checks your configuration for errors and identifies the specific record to resolve before you activate them.

=== ARTICLE: ind.um_usage_orchestration_flow_stages.htm ===
---
article_id: ind.um_usage_orchestration_flow_stages.htm
title: Orchestrate Usage Management Flow Stages
source_url: https://help.salesforce.com/s/articleView?id=ind.um_usage_orchestration_flow_stages.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_cnsption_mngmnt_lifecycle.htm
fetched_at: 2026-09-07
---

# Orchestrate Usage Management Flow Stages

The Orchestrate Usage Management flow with its subflows processes consumption data in various stages.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
Generate Zero-Value Summary Records
Generates advanced zero-value records for Usage Summary, Usage Ratable Summary, and Liable Summary (Usage Billing Period Item). This stage streamlines downstream operations that let the subsequent batch management jobs update existing summaries. For products that are assetized on the current date but were purchased on an earlier date, this stage creates summaries with records aggregated until today.
Aggregate Transaction Journal Records
Summarizes raw usage records from transaction journal entries by using the batch job and determines the overall consumption within a specified period. This aggregation is governed by the usage accumulation method and the usage accumulation period specified in the usage aggregation policy. The aggregated consumption is then stored in a Usage Summary record.
Transaction journal entries are aggregated into usage summaries throughout the billing period. For late data ingestion, the process adds a waiting period (x) after the ratable period's end date and time (T). The default value for this waiting period (or rating delay duration) is 3 days, however, you can customize the flows and update it as per your requirements.
After the waiting period is complete, the status of the usage summary is updated to UsageSummaryComplete.
On the T+x+1 day, the process executes the drawdown process, aggregates any overages to update the ratable summary, and calculates the net unit rate.
If you add consumption logs via transaction journal entries after the T+x waiting period is complete and the usage summary status is updated to UsageSummaryComplete or DrawdownComplete, the Data Processing Engine filters out and ignore the newly added logs for that period.
Process Drawdowns
Processes the aggregated usage summary records. The batch management job in this stage calls the entitlement service that processes the drawdowns for the grants allocated with the asset. The drawdowns happen after the deterministic order logic is applied to the usage summaries. Here’s the priority sequence that the deterministic logic applies.
Usage Summary with the earliest start date is prioritized. For example, a usage summary starting on January 1, 2024 is prioritized over a usage summary starting on January 2, 2024.
If start times are identical, the summary related to the asset that was created earliest with the earliest transaction usage entitlement start date is prioritized. For example, if two usage summaries have the same start date, the summary related to an asset that started on January 1 (Asset 1) is prioritized over the usage summary associated with the other asset that started on September 1 (Asset 2).
If the first two scenarios are tied, the summary related to the transaction usage entitlement with the lowest numerical name is processed first. For example, two usage summaries and their related assets started on the same date, but one is related to a transaction usage entitlement record with the TUE-0000000034 record name, and the other is related to the TUE-0000000045 record name. So, the usage summary related to TUE-0000000034 is prioritized.
After the drawdowns are processed, the corresponding wallet for each asset or binded object is also updated.
Retrieve Net Unit Rates
Retrieves the applicable net unit rate by using the rating procedure specified in the Generate Ratable Summary flow. Usage Management executes rating daily. The batch job first determines the rating schedule and processes summaries provisionally. By using the selected rating procedure, the process identifies the relevant context definition ID and mapping ID required by the rating service to determine the final net unit rate. This rate, along with the identified IDs, is then stamped on the ratable summary records. Customers can gain immediate insight into provisional balances and overages visible on their summaries before the end of the billing period. After the billing period is complete, a cumulative ratable summary is created with the rates applied to the usage summaries based on consumption from the start of the billing period.
Generate Liable Summary Records
Generates the invoice-ready records on a periodic schedule. The process filters the usage summary records that were successfully rated, determines the billing period, calculates the overages and the overage amount, identifies the related liable summary records, and updates these records with the overage amount and quantity.

=== ARTICLE: ind.um_usage_product_setup_with_guided_workflow.htm ===
---
article_id: ind.um_usage_product_setup_with_guided_workflow.htm
title: Usage-Based Product Setup with Guided Workflow
source_url: https://help.salesforce.com/s/articleView?id=ind.um_usage_product_setup_with_guided_workflow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_management_setup.htm
fetched_at: 2026-09-07
---

# Usage-Based Product Setup with Guided Workflow

A logical, sequential workflow guides you through a structured journey—creating a base product and resource definition, defining policy, linking Product Usage Grant (PUG), and setting rates. Finally, you can activate all records created through the journey with one click. It also simplifies the setup by providing preselected, out-of-the-box default policies.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Advanced license and the Revenue Cloud Billing license

The guided workflow introduces mandatory validations at each step. It also has cross-object validations that evaluate how different records work together. After you create the records and activate them, the product and its related records are activated only if you resolve all validation errors.

Configure a Usage-Based Product with Guided Workflow
Follow the guided workflow to create the related records required for your usage-based product. These records complete the product setup so that you can start selling quickly.
Guided Workflow Considerations and Limits
Review the record limits, supported policy types, and custom field constraints when you configure your usage product.

=== ARTICLE: ind.um_validate_your_setup.htm ===
---
article_id: ind.um_validate_your_setup.htm
title: Validate Your Usage Product Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.um_validate_your_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_usage_management_setup.htm
fetched_at: 2026-09-07
---

# Validate Your Usage Product Setup

Run the product validator after you complete your usage management setup by using the guided workflow or manual configuration. The validator checks your configuration for errors and identifies the specific record to resolve before you activate them.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Usage Product Validator Considerations
The validator checks only the records that are effective and active. Before you use this feature, understand the validation rules, warning thresholds, and the different types of logic that the validator applies.
Run the Usage Product Validator
Verify your product's usage and rating design time setup.

=== ARTICLE: ind.um_view_liable_summary.htm ===
---
article_id: ind.um_view_liable_summary.htm
title: View Liable Summaries
source_url: https://help.salesforce.com/s/articleView?id=ind.um_view_liable_summary.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_manage_consumption_related_summaries.htm
fetched_at: 2026-09-07
---

# View Liable Summaries

The Orchestrate Usage Management flow automatically creates the liable summaries by processing the aggregated usage consumption logs and the rates applicable from the usage ratable summaries.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To view liable summaries:	Usage Management Run Time User
From the App Launcher, find and select Liable Summaries.
The Liable Summaries list view shows the recently viewed liable summaries.
To view all the generated liable summaries, from the list view dropdown menu, select All Liable Summaries.

=== ARTICLE: ind.um_wallet_management.htm ===
---
article_id: ind.um_wallet_management.htm
title: Unified Usage Dashboard
source_url: https://help.salesforce.com/s/articleView?id=ind.um_wallet_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: usage
parent_article: ind.um_consumption_management.htm
fetched_at: 2026-09-07
---

# Unified Usage Dashboard

A single, consolidated source of truth for post-sale usage management. Track consumption, negotiated rates, and grant balances, and ensure data integrity across your records. Depending on how your products are structured, you can access this unified experience from either an accounts or an asset record page.

Track Usage Components with Unified Usage Dashboard
After an order is activated, assetized, and entitlements are granted, you can use the dashboard to track wallet balances, monitor overages, and verify applicable rates.
Set Up Wallet View for Experience Cloud
Give your customers a way to independently track their balances, usage, and entitlements. To set up the wallet interface, configure the required Experience Cloud security settings and add the Wallet view to your site’s navigation menu. This feature is available to users with Customer Community or Partner Community licenses.

