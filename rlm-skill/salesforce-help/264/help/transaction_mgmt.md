# Salesforce Help 264 — área: transaction_mgmt (208 artículos)

=== ARTICLE: ind.qocal_action_button_group_important_considerations.htm ===
---
article_id: ind.qocal_action_button_group_important_considerations.htm
title: Action Button Group Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_action_button_group_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_configure_placement_of_action_buttons.htm
fetched_at: 2026-09-04
---

# Action Button Group Considerations

Learn how action button groups behave in the Transaction Line Editor (TLE) and Sales Transaction Line Editor (STLE) to design an efficient experience for your sales team.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

Keep these requirements and system limits in mind when configuring your button layouts.

Salesforce uses the default action button configuration until you configure a custom one. After you define a custom layout, the system uses that configuration instead.
If you don't specify which actions appear or how they're arranged, the editor shows the default actions divided into four groups. The first three groups contain a single action each: QuoteAdjustment, AddAssets, and ImportQuoteLineItems. The last group contains the remaining actions, with only four visible.
You can’t include Salesforce admin-created custom actions at the header or row level. Only standard, built-in STLE actions are available in the action picker.
You can drag actions to reorder them within a group, but you can't drag entire button groups into a different order.
Each action can belong to only 1 button group at a time.
You can create up to 10 button groups, with each group having up to 10 actions. Only the first 10 actions appear on the STLE header at run time. The more button groups you add, the fewer buttons are visible.

=== ARTICLE: ind.qocal_activate_an_object_state_definition.htm ===
---
article_id: ind.qocal_activate_an_object_state_definition.htm
title: Activate an Object State Definition
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_activate_an_object_state_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_order_lifecycle_management_using_object_state_definitions.htm
fetched_at: 2026-09-04
---

# Activate an Object State Definition

To use an object state definition, you must activate it.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To activate object state definitions:	
View on orders
Edit on object state definitions
From the App Launcher, find and select Object State Definitions.
Click the object state definition, and select Active.
Save your changes.

=== ARTICLE: ind.qocal_add_a_special_term_to_a_quote.htm ===
---
article_id: ind.qocal_add_a_special_term_to_a_quote.htm
title: Add a Special Term to a Quote
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_add_a_special_term_to_a_quote.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contracts_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Add a Special Term to a Quote

Search the Document Clause Library and insert an active clause as a quote special term. Resolve any placeholder tokens, then save so that the term stays relevant to your quote.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To create, edit, and search document clause sets and document clauses:	

ClauseUser

OR

ClauseDesignerUser

OR

ClauseDigitalExperienceUser

NOTE
You can add active document clauses with placeholder tokens or no tokens only.
You can't add the same document clause more than one time as a special term on the same quote.
To add the quote special terms on your quote, see Customize Related Lists.
On the quote, go to the Quote Special Terms related list.
Click Add.
In the Search Terms from Clause Library window, filter by clause set, clause, or category, and select a document clause.
Review Language, Category, and Clause Type.
Click Insert.
NOTE While adding a clause to a quote with rich text, the number of characters, including default values and HTML tags, can't exceed 131,000 characters.
If the term includes placeholder tokens, enter values in the token panel, and then click Apply.
Save your changes.

After all placeholders are resolved, you can edit the term content on the quote. After special terms are on the quote, you can generate a quote document that includes those terms. To carry out document generation, create a document template with repeating tokens and map these repeating tokens to Quote Special Terms by using Context Definition & mappings. The Core Omniscript is available for document generation.

See Also

Salesforce Help: Create a Document Clause

Salesforce Help: Example: Generating a Proposal from a Quote by Using Context Service

=== ARTICLE: ind.qocal_add_assets_considerations_for_amendment_and_renewal_quotes_orders.htm ===
---
article_id: ind.qocal_add_assets_considerations_for_amendment_and_renewal_quotes_orders.htm
title: Add Assets Considerations for Amendment and Renewal Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_add_assets_considerations_for_amendment_and_renewal_quotes_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Add Assets Considerations for Amendment and Renewal Quotes and Orders

Before you add assets to an amendment or renewal quote or order, understand how the Contract lookup field affects which assets are eligible to appear in the Add Assets modal.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
When the Contract field on the quote or order is populated, the Add Assets modal shows only assets related to that contract through an Asset Contract Relationship (ACR). Assets that exist on the account but lack an ACR to the specified contract don't appear in the modal, even if they're otherwise eligible.
When the Contract field is blank, the Add Assets modal retrieves all eligible assets at the account level, regardless of ACR.

=== ARTICLE: ind.qocal_add_custom_fields_for_usage_based_products.htm ===
---
article_id: ind.qocal_add_custom_fields_for_usage_based_products.htm
title: Create and Add Custom Fields for Usage-Based Products
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_add_custom_fields_for_usage_based_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_usage_selling.htm
fetched_at: 2026-09-04
---

# Create and Add Custom Fields for Usage-Based Products

Ensure that your custom fields are visible to users during sales transactions. By default, custom fields aren’t visible on the quote creation, manage usage resource, and asset pages.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

To show custom fields on the Manage Usage Resources page while creating quotes or orders, create custom fields on these objects:

Quote Line Rate Card Entry
Quote Line Rate Adjustment
Order Item Rate Card Entry
Order Item Rate Adjustment

To show custom fields on the usage-related tabs on an asset page, create the custom fields on these objects:

Asset Rate Card Entry
Asset Rate Adjustment

After creating the fields, map them in the context definitions to support them in your sales transactions.

NOTE Usage products support custom fields with the Text, Text Area, Number, Checkbox, Date, Percent, Currency, and Picklist data types.
Create custom fields: Use Object Manager to add fields to relevant sales objects (for example, Quote, Order, Product).
Add attributes: Add corresponding attributes and tag names to the extended SalesTransactionContext context definition.
Map attributes: Map these attributes to the custom fields on the entity.
Add custom fields to the page layout.
Go to a record page, click the settings icon, and then click Edit Page.
For adding custom fields to the Manage Usage Resources page, edit a quote or an order record page. And for adding fields to assets, edit an asset record page.
Select the Usage Rates component.
Custom fields aren't supported for the Usage Rates component on the Account, Contract, and Binding Object Custom Extension record pages.
In the right panel, click Select for Select custom fields for the Usage Rates card.
Move the custom fields from the Available list to the Selected list, and then click OK.
Save the changes.
On Activation: Asset Record Page, select APP DEFAULT, and then click Assign as App Default.
In Select Apps, select Usage Management.
Click Next, and save your changes.

The custom fields are now visible for the Manage Usage Resources page, and under the Rates tab for an Asset record page.

=== ARTICLE: ind.qocal_add_the_contract_pricing_schedule_component_in_revenue_cloud.htm ===
---
article_id: ind.qocal_add_the_contract_pricing_schedule_component_in_revenue_cloud.htm
title: Add the Contract Pricing Schedule Component to Lightning Record Pages
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_add_the_contract_pricing_schedule_component_in_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_contract_features.htm
fetched_at: 2026-09-04
---

# Add the Contract Pricing Schedule Component to Lightning Record Pages

Provide sales reps and contract managers with a simple, comprehensive interface for managing contract pricing by adding the Contract Pricing Schedule component to Contract pages. Customize the component to show only the information that your users need.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To edit page layouts in Lightning App Builder:	Customize Application
In Setup, select Object Manager.
Search for and select Contracts.
Go to Lightning Record Pages.
Click the Tabs component.
In the Tabs component properties, click Add Tab.
Click the tab that you added and then select Pricing Schedule as the tab label.
Drag the Contract Pricing Schedule component to the tab.
Click the Contract Pricing Schedule component.
In the properties pane, select the table columns and product price tier columns that you want to show.
Save your changes.

=== ARTICLE: ind.qocal_adjust_subscription_start_date_with_amendments.htm ===
---
article_id: ind.qocal_adjust_subscription_start_date_with_amendments.htm
title: Adjust Subscription Start Dates
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_adjust_subscription_start_date_with_amendments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_advanced_amendment_and_renewal_features.htm
fetched_at: 2026-09-04
---

# Adjust Subscription Start Dates

In subscription selling, it’s common to book a sale, but defer the start of the subscription for a future date. To adjust the start date, sales users can amend a subscription, provided the original start date hasn't occurred yet.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To amend start dates:	

InitiateAmendment API permission set

AND

Sales Rep permission group

Before you begin, review these requirements when adjusting subscription start dates.

You can't amend the start dates of rampable products.
You can change the start date only if the amendment start date is later than today's date.
You change the start date multiple times, if necessary.
On the quotes page, find and review the quote where you want to adjust the start date of an asset.
On the Account page, under the Assets tab, select the asset included in your quote.
In the Managed Assets viewer, select Amend and select a new date.
To set the amendment start date, select one of these options.
Use the subscription start date for the amendment start date
Enter a new Amendment Date
Click Submit.

=== ARTICLE: ind.qocal_adjustment_type_column.htm ===
---
article_id: ind.qocal_adjustment_type_column.htm
title: Adjustment Type Column
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_adjustment_type_column.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_customize_transaction_line_editor.htm
fetched_at: 2026-09-04
---

# Adjustment Type Column

The Adjustment Type column merges multiple adjustment fields into a single column so that sales reps can make pricing adjustments more efficiently.

Supported Fields

The Adjustment Type column supports editable currency and percent fields from both quote and order line items and their associated groups. Fields of other data types aren’t supported and don’t appear in this column.

To include a field in the Adjustment Type column, add the field to the Display Columns and select the same field in Select Fields to Group and Display in the Adjustment Type column. Only add fields that are editable and designed for pricing adjustments.

NOTE In Lightning App Builder, don’t select Start Date or End Date in the field selection for the Adjustment Type column. If these fields are included, editing an adjustment type can reset the start and end dates on ramped quote lines.
IMPORTANT Don’t add read-only or calculated fields (such as Total Adjustment) to the Adjustment Type column. When you include non-editable fields, the system attempts to set values on these fields during pricing, which causes errors. If you encounter pricing errors after adding a field to the Adjustment Type column, remove any non-editable fields from the field selection list.
Default Adjustment Fields
Discount Amount
Discount (Percentage)
Margin Amount
Margin (Percentage)
Unit Cost

These adjustment types are available on Quote Line Items, Quote Line Groups, Order Line Items, and Order Item Groups objects.

NOTE You can add custom currency or percent fields to the Adjustment Type column, but verify that the fields are editable. Don't add read-only, calculated, or formula fields.

=== ARTICLE: ind.qocal_advanced_amendment_and_renewal_features.htm ===
---
article_id: ind.qocal_advanced_amendment_and_renewal_features.htm
title: Advanced Amendment and Renewal Features
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_advanced_amendment_and_renewal_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_assets_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Advanced Amendment and Renewal Features

Revenue Management provides flexible asset management by helping sales reps to apply negotiated contract pricing to amendments and renewals. You can use specialized features to adjust subscription start and end dates for termed assets, perform field or price-only updates without changing configurations, and use the Rollback tool to reverse the most recent future-dated transactions. These capabilities ensure data integrity and accommodate evolving customer needs throughout the asset lifecycle.

Apply Contract Pricing When Amending or Renewing
Apply negotiated contract prices or discounts to amendments and renewals to ensure sales reps honor original customer agreements. Maintaining contracts with contract-based pricing includes these negotiated rates in all subsequent lifecycle transactions.
Manage Assets with Field and Price Amendments
Update asset details and adjust pricing without changing quantities, attributes, or bundle configurations by using Field Amendments and Price Amendments. Use Field Amendments to modify standard and custom fields, such as billing frequency. Use Price Amendments to update the Sales Price on quote lines or the Unit Price on order lines.
Adjust Subscription Start Dates
In subscription selling, it’s common to book a sale, but defer the start of the subscription for a future date. To adjust the start date, sales users can amend a subscription, provided the original start date hasn't occurred yet.
Change Subscription End Dates of Termed Assets
Modify the subscription end date for termed assets during amendments and renewals to lengthen or shorten a subscription's term. This flexibility helps you accommodate evolving customer needs within the Revenue Management asset lifecycle.
Roll Back the Last Transaction for an Asset
To reverse the most recent future-dated amendment or renewal due to errors or changes in customer plans, use the Rollback feature. This action restores the asset to its original state, eliminating the need for complicated manual workarounds.

=== ARTICLE: ind.qocal_advanced_detail_line_pricing_for_custom_and_derived_products.htm ===
---
article_id: ind.qocal_advanced_detail_line_pricing_for_custom_and_derived_products.htm
title: Use Advanced Transaction Detail Line Pricing to Map Custom Fields
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_advanced_detail_line_pricing_for_custom_and_derived_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.pricing_unique_pricing_scenarios.htm
fetched_at: 2026-09-04
---

# Use Advanced Transaction Detail Line Pricing to Map Custom Fields

Users can update custom fields on sales transaction items or sales transaction item details through pricing procedures by using the Advanced Detail Line Pricing feature. With this feature, users no longer need to use custom triggers or flows to update those fields. This feature is useful for amendment, renewal, and cancellation use cases.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To set up and use advanced detail line pricing:	

Salesforce admin

AND

Pricing Design Time User permission set

Before you begin, complete these tasks.

To turn on the Advanced Detail Line Pricing feature, in Setup, find and select Revenue Settings, and then turn on the Advanced Detail Line Pricing setting.
Configure your pricing procedure.
Add Context Tag Mappings to the Pricing Procedure Map Line Item Element Using JSON
To configure a pricing procedure to use advanced detail line pricing, copy and paste the map line item JSON to a pricing procedure in Revenue Pricing.
Add Context Tag Mappings to the Discovery Procedure Map Line Item Element Using JSON
To configure a discovery procedure to use advanced detail line pricing with derived-pricing products, copy and paste the map line item for derived pricing JSON to a discovery procedure in Revenue Pricing.
Update Revenue Pricing Procedure

To configure advanced detail line pricing, modify your revenue pricing procedure.

From the App Launcher, find and select Pricing Procedures, and then select a pricing procedure to update.
Modify the pricing procedure by adding a new map line item element as the second element next to the pricing setting in the pricing procedure.
Add context tag mappings to the map line item.

Input Variable

	

Output Variable




LineItem

	

SalesTrxnItemDetailSource




LineItemQuantity

	

ItemDetailQuantity




NetUnitPrice

	

ItemDetailNetUnitPrice




price_water_fall

	

DetailPriceWaterfallIdentifier




InputUnitPrice

	

ItemDetailUnitPrice




ItemBillingReference

	

ItemDetailBillingReference




ItemNetTotalPrice

	

ItemDetailTotalPrice




TotalLineAmount

	

ItemDetailTotalLineAmount




EffectiveFrom

	

ItemDetailEffectiveFrom__std




EffectiveTo

	

ItemDetailEffectiveTo__std




PricingTermCount

	

ItemDetailPricingTermCount__std




itemTransientEndDate

	

ItemDetailTransientEndDate__std




ItemPricingSource

	

ItemDetailPricingSource__std




DerivedPricingAttribute

	

ItemDetailDerivedPricingAttribute__std




ItemGroupSummarySubtotal

	

ItemDetailGroupSummaryTotal__std




ListPrice

	

ItemDetailListPrice__std




IsContracted

	

ItemDetailIsContracted__std




ItemContractPrice

	

ItemDetailContractPrice__std




STI_TenantName__c

	

STID_TenantName__c

After adding the context tag mappings, you’ll see the default mappings between SalesTransaction and SalesTransactionItemDetail with updated context definitions.
Update Derived Pricing Discovery Procedure

If you're using derived pricing, make additional changes to your discovery procedure after completing changes to your revenue pricing procedure. These changes are necessary to determine valid contributing and derived products.

From the App Launcher, find and select Discovery Procedures, and then select a discovery procedure to update.
Add two new elements to the discovery procedure to price derived products: Discovery Settings and Map Line Item.
Add these variables to discovery settings.
Input Variable: Line Item
Output Variable: LineItem
Add these variables to the map line item.
Input Variable: SalesTransactionItem
Output Variable: SalesTransactionItemDetail

Add these additional variables to the map line item.

Input Variable

	

Output Variable




LineItem

	

SalesTrxnItemDetailSource




EffectiveFrom

	

ItemDetailEffectiveFrom__std




EffectiveTo

	

ItemDetailEffectiveTo__std




DerivedPricingAttribute

	

ItemDetailDerivedPricingAttribute__std

Support custom fields by using pricing procedures for amend, renew, and cancel (ARC) use cases.
Custom field setup is applicable if you use ARC APIs and want to use custom fields.
Add custom fields to the QuoteLineItem, QuoteLineItem Detail, OrderProduct, and OrderProductDetails objects.
In the context definition, create an entry for these custom fields in both SalesTransactionItem and SalesTransactionItemDetail nodes.
Create the required mappings in QuoteEntitiesMapping and OrderEntitiesMapping.
Modify the revenue pricing procedure for custom fields.
In the pricing procedure, modify the MapLineItem element to add a mapping between SalesTransactionItem.CustomField and SalesTransactionItemDetail.CustomField.
Create any necessary customization elements within the pricing procedure to assign a value to SalesTransactionItem.CustomField.

The pricing procedure automatically detects if a specific line has detail entries and writes to SalesTransactionItemDetail.CustomField if they exist. Otherwise, it writes to SalesTransactionItem.CustomField.

During new sale transactions, CustomField on SalesTransactionItem is populated. For ARC scenarios with detail lines, the detail line is written to CustomField on SalesTransactionItemDetail. If no detail lines are created for ARC, the detail line is it written to CustomField on SalesTransactionItem.

To write custom fields on QuoteLineItem or OrderProducts with detail lines, complete this additional setup involving procedure plans and Apex classes.
Enable a procedure plan. In Setup, find and select Revenue Settings, and turn on the Procedure Plan Orchestration for Pricing setting.
Create a procedure plan for the quote and order.
In the procedure plan, verify all steps include the MapLineItem element. Modify the mappings based on the fields used in the pricing procedure.
Use this ApexCustomFieldHandler Apex class example, which you can enhance to update multiple custom fields if required. This class queries SalesTransactionItem and SalesTransactionItemDetail nodes, extracts custom field values from detail items, and then updates the corresponding custom fields on SalesTransactionItem.
EXAMPLE
global class ApexCustomFieldHandler implements RevSignaling.SignalingApexProcessor {

    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        

        // STEP 2 - Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem', 'SalesTransactionItemDetail' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');
        List<Object> itemDetailData = (List<Object>) itemQueryResult.get('SalesTransactionItemDetail');


        Map<String, String> salesTransactionItemIdToCustomAggregatedValue = new Map<String, String>();
        
        // STEP 3 - Custom Field Value from SalesTransactionItemDetail
        for(Object itemDetailObj : itemDetailData) {
            Map<String, Object> itemDetailNode = (Map<String, Object>) itemDetailObj;
            Map<String, Object> detailTagMap = (Map<String, Object>) itemDetailNode.get('tagValue');
            
            String lineItemId = (String)((Map<String, Object>) detailTagMap.get('SalesTrxnItemDetailParent')).get('tagValue');
            String cfValue = (String)((Map<String, Object>) detailTagMap.get('STID_TenantName__c')).get('tagValue');
            
            System.debug('Custom Field Value for Detail Item' + cfValue);
            if(cfValue != null) {
                salesTransactionItemIdToCustomAggregatedValue.put(lineItemId, cfValue);
            }
        }


        // STEP 4 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();

        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            Map<String, Object> tagMap = (Map<String, Object>) itemNode.get('tagValue');
            
            String lineItemId = (String)((Map<String, Object>) tagMap.get('LineItem')).get('tagValue');
            
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');

            dataPath.remove(0); // Remove contextId

            itemNodeUpdates.add(new Map<String, Object>{
                'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                'attributes' => new List<Object>{
                    new Map<String, Object>{
                        'attributeName' => 'STI_TenantName__c',
                        'attributeValue' => salesTransactionItemIdToCustomAggregatedValue.get(lineItemId)
                    }
                }
            });
        }

        // STEP 5 - Create collection context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };
            
            //Step 6 - Update context
            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        return response;
    }
}

IMPORTANT To add custom field information to Asset State Period and Asset Action Source, create appropriate cross-context mappings.

=== ARTICLE: ind.qocal_advanced_example_ramp_deals_for_groups.htm ===
---
article_id: ind.qocal_advanced_example_ramp_deals_for_groups.htm
title: Advanced Example of Ramp Deals for Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_advanced_example_ramp_deals_for_groups.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.ramp_deals_examples.htm
fetched_at: 2026-09-04
---

# Advanced Example of Ramp Deals for Groups

See an example of adding products to specific segments, dynamic configuration, varying rates, and asset management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
Introduction

Alex, a sales rep from SmartBytes, creates a quote for Acme that spans over 5 years based on the requirements shared in the opportunity record. Alex shares the quote with James from Bloomington Caregivers, a healthcare client who wants to transition from traditional learning methods to digital learning solutions.

After sharing the quote, Alex meets James and realizes that the requirements have more nuances. Alex updates and fine-tunes the quote based on his requirements.

Configure Products

For the first year, James wants only a subset of the child products from each category in the Digital Education Solution.

Collaboration Software
Classroom Collaboration Software
Parent-Teacher Collaboration Software
Support Services
Implementation Support
Education Software
Classroom Management Software
Assessment Software

From the second year onward, James wants to include Email Application and replace Implementation Support with Maintenance Support.

Here’s how Alex updates the quote.

Open the quote.
Click  corresponding to Digital Education Solution in the Year 1 segment, and then select Configure.
Product Configurator opens.
In the Collaboration Software section, select Classroom Collaboration Software and Parent-Teacher Collaboration Software.
In the Support Services section, select Implementation Support.
In the Education Software section, select Assessment Software and Classroom Management Software.
Save the changes.

Transaction Management updates the child products in the Year 1 segment and all the subsequent segments.

To include Email Application and replace Implementation Support with Maintenance Support from the Year 2 segment, complete these steps.
Open Product Configurator for Digital Education Solution in the Year 2 segment.
Select Email Application.
Deselect Implementation Support.
Select Maintenance Support.
Save the changes.
Transaction Management automatically updates the lines in the Year 2 segment and the subsequent segments.
To view the snapshot of the Email Application product, click  corresponding to the product and then select View Ramp Details.

The child product is available only from the second year.

Add Products to Specific Segments

When discussing the requirements with Alex, James realizes that they also need a storage solution for the second and third years. By the fourth year, their in-house storage solution will be ready.

Here’s how Alex adds products.

To add products to the Year 2 segment, click  corresponding to it and then select Browse Catalogs.
Browse and select Cloud Storage Pro, enter the quantity, click Add, and then click Next.
To add the product to the Year 2 and the subsequent segments, select Current and Subsequent Segments.

To view the details of Cloud Storage Pro, click  corresponding to it and then click View Ramp Details.

The newly added product is ramped and is available only from the second year.
To delete the product from the Year 4 and Year 5 segments, click  corresponding to Cloud Storage Pro in the Year 4 segment, and then select Delete.
In the Delete ramped line item Cloud Storage Pro? window click Delete.

Transaction Management deletes Cloud Storage Pro from the fourth year and fifth years.
Save the changes.

James is happy with the quote and approves it. Alex creates an order from the quote, and then activates the order

Amend Consolidated Assets

In the middle of the second year, James calls Alex and informs her that their growth was faster than anticipated. For the third year, he wants 2000 more licenses of Cloud Storage Pro.

Here’s how Alex amends the assets to increase the number of licenses.

From the App Launcher, find and select Account.
Click Bloomington Caregivers.
Under Managed Assets, for Cloud Storage Pro, select the checkbox in the Asset Name column.
Click Amend.
Select an amendment date, and then click Submit.
You can’t modify the fulfilled part of a ramp segment. However, you can modify the upcoming part of the segment.
For Year 3, enter the number of extra licenses, 2000, in the Quantity column.
Save the changes.
Create an order from the amendment quote, and then activate the order.
Click the Bloomington Caregivers tab.
To view the updated asset state periods, click  corresponding to Cloud Storage Pro and then select View.

When the amendment order is submitted, Transaction Management:

Creates the asset action, AA-000000243, to track the upsell.
Updates the asset state period, ASP-000000520, for the fulfilled duration of the current segment.
Creates the asset state period, ASP-000000561, for the remaining duration of the current segment.
Updates the asset state period, ASP-000000521, of the modified segment.

=== ARTICLE: ind.qocal_advanced_line_discovery_map_line_json_task.htm ===
---
article_id: ind.qocal_advanced_line_discovery_map_line_json_task.htm
title: Add Context Tag Mappings to the Discovery Procedure Map Line Item Element Using JSON
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_advanced_line_discovery_map_line_json_task.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_advanced_detail_line_pricing_for_custom_and_derived_products.htm
fetched_at: 2026-09-04
---

# Add Context Tag Mappings to the Discovery Procedure Map Line Item Element Using JSON

To configure a discovery procedure to use advanced detail line pricing with derived-pricing products, copy and paste the map line item for derived pricing JSON to a discovery procedure in Revenue Pricing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To set up and use advanced detail line pricing:	

Salesforce admin

AND

Pricing Design Time User permission set

From the App Launcher, find and select Discovery Procedures, and then select a discovery procedure to update.
Add two new elements to the discovery procedure to price derived products: Discovery Settings and Map Line Item.
Add the context tag mappings to the map line item using this JSON.
{"componentName":"Map Line Item","businessKnowledgeModelName":"BreakdownLineMapping","usageType":"PricingDiscovery","elementAttributes":null,"parameters":null,"inputVariablesMappingText":{"section-0-input1":"LineItem","section-1-input1":"EffectiveFrom","section-2-input1":"EffectiveTo","section-3-input1":"DerivedPricingAttribute","section-0-output":"SalesTrxnItemDetailSource","section-1-output":"ItemDetailEffectiveFrom__std","section-2-output":"ItemDetailEffectiveTo__std","section-3-output":"ItemDetailDerivedPricingAttribute__std","sectionCount":"4","sectionJsonString1":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Text\",\"name\":\"section-0-input1\",\"value\":\"LineItem\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Text\",\"name\":\"section-0-output\",\"value\":\"SalesTrxnItemDetailSource\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString2":"{\"whereConditions\":[{\"field\":{\"dataType\":\"DateTime\",\"name\":\"section-1-input1\",\"value\":\"EffectiveFrom\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"DateTime\",\"name\":\"section-1-output\",\"value\":\"ItemDetailEffectiveFrom__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString3":"{\"whereConditions\":[{\"field\":{\"dataType\":\"DateTime\",\"name\":\"section-2-input1\",\"value\":\"EffectiveTo\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"DateTime\",\"name\":\"section-2-output\",\"value\":\"ItemDetailEffectiveTo__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString4":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Boolean\",\"name\":\"section-3-input1\",\"value\":\"DerivedPricingAttribute\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Boolean\",\"name\":\"section-3-output\",\"value\":\"ItemDetailDerivedPricingAttribute__std\",\"allowCompatibleDataTypes\":true}}]}"},"outputVariablesMappingText":{}}
Save your changes.

=== ARTICLE: ind.qocal_advanced_line_pricing_map_line_json_task.htm ===
---
article_id: ind.qocal_advanced_line_pricing_map_line_json_task.htm
title: Add Context Tag Mappings to the Pricing Procedure Map Line Item Element Using JSON
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_advanced_line_pricing_map_line_json_task.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_advanced_detail_line_pricing_for_custom_and_derived_products.htm
fetched_at: 2026-09-04
---

# Add Context Tag Mappings to the Pricing Procedure Map Line Item Element Using JSON

To configure a pricing procedure to use advanced detail line pricing, copy and paste the map line item JSON to a pricing procedure in Revenue Pricing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To set up and use advanced detail line pricing:	

Salesforce admin

AND

Pricing Design Time User permission set

From the App Launcher, find and select Pricing Procedures, and then select a pricing procedure to update.
Modify the pricing procedure by adding a new map line item element as the second element next to the pricing setting in the pricing procedure.
Add the context tag mappings to the map line item using this JSON.
{"componentName":"Map Line Item","usageType":"DefaultPricing","businessKnowledgeModelName":"BreakdownLineMapping","outputVariablesMappingText":{"MapLineItemNodeOutput":"SalesTransactionItemDetail"},"inputVariablesMappingText":{"section-0-input1":"LineItem","section-1-input1":"LineItemQuantity","section-2-input1":"NetUnitPrice","section-3-input1":"price_water_fall","section-4-input1":"InputUnitPrice","section-5-input1":"ItemBillingReference","section-6-input1":"ItemNetTotalPrice","section-7-input1":"TotalLineAmount","section-8-input1":"EffectiveFrom","section-9-input1":"EffectiveTo","section-10-input1":"PricingTermCount","section-11-input1":"itemTransientEndDate","section-12-input1":"ItemPricingSource","section-13-input1":"DerivedPricingAttribute","section-14-input1":"ItemGroupSummarySubtotal","section-15-input1":"ListPrice","section-16-input1":"IsContracted","section-17-input1":"ItemContractPrice","section-0-output":"SalesTrxnItemDetailSource","section-1-output":"ItemDetailQuantity","section-2-output":"ItemDetailNetUnitPrice","section-3-output":"DetailPriceWaterfallIdentifier","section-4-output":"ItemDetailUnitPrice","section-5-output":"ItemDetailBillingReference","section-6-output":"ItemDetailTotalPrice","section-7-output":"ItemDetailTotalLineAmount","section-8-output":"ItemDetailEffectiveFrom__std","section-9-output":"ItemDetailEffectiveTo__std","section-10-output":"ItemDetailPricingTermCount__std","section-11-output":"ItemDetailTransientEndDate__std","section-12-output":"ItemDetailPricingSource__std","section-13-output":"ItemDetailDerivedPricingAttribute__std","section-14-output":"ItemDetailGroupSummaryTotal__std","section-15-output":"ItemDetailListPrice__std","section-16-output":"ItemDetailIsContracted__std","section-17-output":"ItemDetailContractPrice__std","MapLineItemNodeInput":"SalesTransactionItem","sectionCount":"18","sectionJsonString1":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Text\",\"name\":\"section-0-input1\",\"value\":\"LineItem\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Text\",\"name\":\"section-0-output\",\"value\":\"SalesTrxnItemDetailSource\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString2":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Numeric\",\"name\":\"section-1-input1\",\"value\":\"LineItemQuantity\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Numeric\",\"name\":\"section-1-output\",\"value\":\"ItemDetailQuantity\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString3":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Currency\",\"name\":\"section-2-input1\",\"value\":\"NetUnitPrice\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Currency\",\"name\":\"section-2-output\",\"value\":\"ItemDetailNetUnitPrice\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString4":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Text\",\"name\":\"section-3-input1\",\"value\":\"price_water_fall\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Text\",\"name\":\"section-3-output\",\"value\":\"DetailPriceWaterfallIdentifier\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString5":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Currency\",\"name\":\"section-4-input1\",\"value\":\"InputUnitPrice\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Currency\",\"name\":\"section-4-output\",\"value\":\"ItemDetailUnitPrice\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString6":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Text\",\"name\":\"section-5-input1\",\"value\":\"ItemBillingReference\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Text\",\"name\":\"section-5-output\",\"value\":\"ItemDetailBillingReference\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString7":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Currency\",\"name\":\"section-6-input1\",\"value\":\"ItemNetTotalPrice\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Currency\",\"name\":\"section-6-output\",\"value\":\"ItemDetailTotalPrice\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString8":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Currency\",\"name\":\"section-7-input1\",\"value\":\"TotalLineAmount\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Currency\",\"name\":\"section-7-output\",\"value\":\"ItemDetailTotalLineAmount\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString9":"{\"whereConditions\":[{\"field\":{\"dataType\":\"DateTime\",\"name\":\"section-8-input1\",\"value\":\"EffectiveFrom\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"DateTime\",\"name\":\"section-8-output\",\"value\":\"ItemDetailEffectiveFrom__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString10":"{\"whereConditions\":[{\"field\":{\"dataType\":\"DateTime\",\"name\":\"section-9-input1\",\"value\":\"EffectiveTo\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"DateTime\",\"name\":\"section-9-output\",\"value\":\"ItemDetailEffectiveTo__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString11":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Numeric\",\"name\":\"section-10-input1\",\"value\":\"PricingTermCount\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Numeric\",\"name\":\"section-10-output\",\"value\":\"ItemDetailPricingTermCount__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString12":"{\"whereConditions\":[{\"field\":{\"dataType\":\"DateTime\",\"name\":\"section-11-input1\",\"value\":\"itemTransientEndDate\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"DateTime\",\"name\":\"section-11-output\",\"value\":\"ItemDetailTransientEndDate__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString13":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Text\",\"name\":\"section-12-input1\",\"value\":\"ItemPricingSource\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Text\",\"name\":\"section-12-output\",\"value\":\"ItemDetailPricingSource__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString14":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Boolean\",\"name\":\"section-13-input1\",\"value\":\"DerivedPricingAttribute\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Boolean\",\"name\":\"section-13-output\",\"value\":\"ItemDetailDerivedPricingAttribute__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString15":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Currency\",\"name\":\"section-14-input1\",\"value\":\"ItemGroupSummarySubtotal\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Currency\",\"name\":\"section-14-output\",\"value\":\"ItemDetailGroupSummaryTotal__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString16":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Currency\",\"name\":\"section-15-input1\",\"value\":\"ListPrice\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Currency\",\"name\":\"section-15-output\",\"value\":\"ItemDetailListPrice__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString17":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Boolean\",\"name\":\"section-16-input1\",\"value\":\"IsContracted\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Boolean\",\"name\":\"section-16-output\",\"value\":\"ItemDetailIsContracted__std\",\"allowCompatibleDataTypes\":true}}]}","sectionJsonString18":"{\"whereConditions\":[{\"field\":{\"dataType\":\"Currency\",\"name\":\"section-17-input1\",\"value\":\"ItemContractPrice\",\"allowCompatibleDataTypes\":true},\"value\":{\"dataType\":\"Currency\",\"name\":\"section-17-output\",\"value\":\"ItemDetailContractPrice__std\",\"allowCompatibleDataTypes\":true}}]}"},"elementAttributes":null,"parameters":null}
Save your changes.

=== ARTICLE: ind.qocal_agentforce_considerations.htm ===
---
article_id: ind.qocal_agentforce_considerations.htm
title: Considerations for Agentforce in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_agentforce_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-04
---

# Considerations for Agentforce in Revenue Management

To use Agentforce for Revenue, consider supported functionality, usage, limitations and allowances, limits, and other issues.

Language and Locale Support

Agentforce for Revenue supports English in this locale.

LOCALE	CODE
English (United States)	en_US
Agent Type

The agent templates for Revenue Management are based on the Agentforce Employee Agent type.

For information about large language model support, Einstein trust layer service support, standard action usage type billed for this agent, and other considerations, see Considerations for Agentforce Employee Agent.

=== ARTICLE: ind.qocal_agentforce_quote_mgmt.htm ===
---
article_id: ind.qocal_agentforce_quote_mgmt.htm
title: Agentforce for Revenue Quote Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_agentforce_quote_mgmt.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-04
---

# Agentforce for Revenue Quote Management

With the new Revenue Quote Management template, your sales reps can streamline quoting workflows and accelerate the sales cycle. This template comes with a suite of advanced Agentforce actions that automate routine tasks like product selection, quote creation, and management, helping sales reps create and update quotes and line items within minutes. By leveraging simple prompts, sales reps can easily create initial, renewal, and amendment quotes. This allows them to respond to customer needs more quickly and accurately, ultimately improving productivity and driving more meaningful customer interactions.

To review the billing considerations for Revenue Quote Management, see Considerations for Agentforce in Revenue Management.

Set Up Revenue Quote Management
To use additional features relevant to quotes, turn on the required features and assign permissions.
Subagent: Product Selection
Use Agentforce to power product discovery and filtering with AI-driven assistance. Sales users can use the Product Selection topic to search the product catalog, ask clarifying questions, and refine results based on customer criteria. The topic helps users explore available products, review key details, and receive recommendations that support accurate and complete quote building. You can customize the Product Selection topic to match your catalog, sales workflows, and conversational experience.
Subagent: Quote Management
Create and modify quotes and their quote line items in Revenue Management.
Subagent: Consumption Management
Get consumption details of accounts with resource overages and generate quotes for the resources with overages.

=== ARTICLE: ind.qocal_agentforce_quote_mgmt_setup.htm ===
---
article_id: ind.qocal_agentforce_quote_mgmt_setup.htm
title: Set Up Revenue Quote Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_agentforce_quote_mgmt_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_agentforce_quote_mgmt.htm
fetched_at: 2026-09-04
---

# Set Up Revenue Quote Management

To use additional features relevant to quotes, turn on the required features and assign permissions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license with the Agentforce Employee Agent add-on.
Set Up Agentforce for Revenue Management.
To improve the accuracy and relevance of product search results, configure indexing. You can also turn on semantic search for broader matching. If semantic search doesn’t return the results you expect, turn it off and continue using indexed search.
Configure multiple currencies.
Set up multiple currencies for transactions.
From Setup, in the Quick Find box, find and select Flows.
Under Flow Definitions, open the Add QuoteLineItem to Quote flow.
Add a condition to the Get Product element that verifies whether the Currency ISO Code field is available on the product record.
Open the Get Price Book Entry element.
In the Filter Price Book Entry Records section, set the Condition Requirements field to All Conditions Are Met (AND).
Click + Add Condition.
Set the Product ID field to productId and the Currency ISO Code field to the currency you want to support.
Specify the currency by using its ISO code.
To access the Consumption Management topic within the Revenue Quote Management template, turn on rate management and usage management.

=== ARTICLE: ind.qocal_amend_a_usage_based_product.htm ===
---
article_id: ind.qocal_amend_a_usage_based_product.htm
title: Amend a Usage-Based Product
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_amend_a_usage_based_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_amending_rates_and_grants_on_usage_based_products.htm
fetched_at: 2026-09-04
---

# Amend a Usage-Based Product

Change the rates, grants, or quantities of an existing asset to reflect new customer agreements.

REQUIRED EDITIONS
NOTE Grant negotiations are not supported on existing quotes and orders.
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Transaction Management is enabled
USER PERMISSIONS NEEDED
To amend assets:	Amend Assets and Sales Rep permission group
NOTE Before you being to amend a usage-based product, remember the following.
Existing quotes and orders don’t support grant negotiations.
Ensure that the amendment date is within the asset's lifecycle.
From the App Launcher, find and select Orders.
Select the order number.
Click Account Name, and then click Assets.
Select the asset, and then click Amend.
Enter the amendment date.
If needed, select Use the amendment start date for the subscription start date, and click Submit.
Submitting the amendment creates the quote line item usage resource grants.
From the Quick Actions menu, select Manage Usage Resources.
Specify the grant quantity and applicable rate.
Save your changes.
The system creates an amendment for the quote line item.
EXAMPLE

To update an existing subscription for ACME, a cloud storage company, define a grant quantity of 70,000 Revenue Management Credits and an applicable rate of $18 USD. After you save, use the amended quote line item to create an order.

=== ARTICLE: ind.qocal_amend_and_renew_assets_with_contract_pricing.htm ===
---
article_id: ind.qocal_amend_and_renew_assets_with_contract_pricing.htm
title: Apply Contract Pricing When Amending or Renewing
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_amend_and_renew_assets_with_contract_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_advanced_amendment_and_renewal_features.htm
fetched_at: 2026-09-04
---

# Apply Contract Pricing When Amending or Renewing

Apply negotiated contract prices or discounts to amendments and renewals to ensure sales reps honor original customer agreements. Maintaining contracts with contract-based pricing includes these negotiated rates in all subsequent lifecycle transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To use contract pricing:	Salesforce Pricing Design Time User
To amend assets:	Amend Assets and Sales Rep permission group
To renew assets:	Renew Assets and Sales Rep permission group
IMPORTANT Refresh the decision table for contract pricing after activating a contract that contains contract item prices or price adjustment schedules.

When you initiate an amendment or renewal from a contract, the system creates a quote associated with that contract. All quote line products use the contract's item prices and price adjustment schedules unless the asset-level pricing source specifies otherwise. If the contract includes a specified renewal term, the system renews assets in the renewal quote for a length equal to that term.

From App Launcher, find and select Contracts.
From the Contract List view, select a contract.
On the Assets tab of the contract, select the assets that you want to amend or renew.
Select Amend or Renew.

=== ARTICLE: ind.qocal_amend_and_renew_with_new_end_date.htm ===
---
article_id: ind.qocal_amend_and_renew_with_new_end_date.htm
title: Change Subscription End Dates of Termed Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_amend_and_renew_with_new_end_date.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_advanced_amendment_and_renewal_features.htm
fetched_at: 2026-09-04
---

# Change Subscription End Dates of Termed Assets

Modify the subscription end date for termed assets during amendments and renewals to lengthen or shorten a subscription's term. This flexibility helps you accommodate evolving customer needs within the Revenue Management asset lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To change end dates on amendments or renewals:	Amend Assets and Renewal Assets permissions
IMPORTANT This feature applies exclusively to termed subscriptions. Users can’t modify terms for evergreen subscriptions.
From the App Launcher, find and select Accounts.
Select an asset on the Managed Assets Viewer on the Assets tab.
Select the termed subscription asset to amend, and click Amend.
Create an amendment quote or order.
On the quote line item (QLI) or order line item (OLI), adjust the subscription end date by modifying these fields.
End Date: The new ‌end date for the subscription.
Subscription Term: The subscription term unit determines the length of the subscription.
Run the Quote-to-Order process to finalize your quote changes and convert them into an order.
Assetize the order to verify the new end date on the asset record.

=== ARTICLE: ind.qocal_amend_assets.htm ===
---
article_id: ind.qocal_amend_assets.htm
title: Amend Assets with the Managed Asset Viewer
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_amend_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_general_procedures.htm
fetched_at: 2026-09-04
---

# Amend Assets with the Managed Asset Viewer

To meet changing customer needs and optimize revenue, use the asset lifecycle amendment action to modify products your customers purchased. The Managed Asset viewer on your Account or Contract page initiates these changes directly within the asset lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To amend assets:	

InitiateAmendment API permission set

AND

Sales Rep persona permissions

Before you amend an asset that has a derived price, we recommend you refresh your decision tables. Also, when derived pricing is enabled for amendments, the Net Unit Price of the derived product is not displayed in the amendment, however the total line amount will be accurate.

Prerequisites

Before you begin:

Add the Managed Asset Viewer component to your preferred page layouts, such as the Account page layout.
Add the Assets related list to the Account or Contracts page to show the Managed Assets list.
To complete asset amendments in Managed Assets, add the component to the Contracts page layout.
Select a pricing source for the amendment on the asset record to price positive quantity amendment orders.
Refresh your decision tables before amending an asset that has a derived price.
IMPORTANT
When you use the Contracts page layout, the system automatically adds the contract number to the amendment quote or order.
If an asset has a future-dated amend, renew, or cancel transaction, you can’t initiate a transaction with an earlier start date.
While you can change quantities for termed subscriptions, you can’t change the subscription end date during an amendment.
If an amendment contains a negative delta quantity, the system calculates the total price based on prior asset sale prices by using a Last In First Out (LIFO) strategy for multiple prior transactions.
For derived products, the amendment doesn’t show the Net Unit Price, but the total line amount remains accurate.
Amend Assets
From the App Launcher, find and select Accounts.
In Accounts List View, select an account name.
Under Managed Assets, select the checkbox in the Asset Name column for the asset that you want to update. For bundled assets, select the parent asset instead of the child asset.
Select Amend.
Select the amendment date by using the calendar and click Submit.
The transaction system creates an amendment quote or order based on your default flow and copies asset attribute values to line item attribute values.
NOTE Deactivated product attributes don’t affect existing quote line item, order product, or asset attributes.
Update the quantity.
You can’t reduce the quantity to less than the original asset quantity.
Add assets to the amendment quote if needed.
Review your amendment request and save your changes.
EXAMPLE

=== ARTICLE: ind.qocal_amend_renew_end_date_important_considerations.htm ===
---
article_id: ind.qocal_amend_renew_end_date_important_considerations.htm
title: Changing Subscription End Dates of Termed Assets Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_amend_renew_end_date_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Changing Subscription End Dates of Termed Assets Considerations

Understand the requirements and limitations for modifying subscription end dates during amendments and renewals. Familiarizing yourself with these rules helps you accurately lengthen or shorten a subscription's term to meet evolving customer needs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Term Modification Constraints

Review these critical rules before adjusting a subscription end date.

Product Restrictions: You can’t change the end date on subscriptions containing ramp deals or usage-based products.
Transaction Sequence: A term change amendment serves as the final transaction in the chain before an asset expires.
Isolation Requirements: You can’t perform the amendment within other amendments, renewals, or cancellations.
Date Limits: The system prohibits setting an end date that occurs before the start date of the current amendment, renewal, or cancellation quote or order.
Asset Impact: If a quote line item (QLI) or order line item (OLI) has a positive quantity, the term change applies to all end quantity assets.
Action Categorization: Increasing the subscription term counts as an upsell, while decreasing the term counts as a downsell for the asset action category.

=== ARTICLE: ind.qocal_amending_rates_and_grants_on_usage_based_products.htm ===
---
article_id: ind.qocal_amending_rates_and_grants_on_usage_based_products.htm
title: Usage-Based Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_amending_rates_and_grants_on_usage_based_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_specialized_asset_considerations.htm
fetched_at: 2026-09-04
---

# Usage-Based Assets

Learn how usage-based products enable flexible rate and grant negotiations throughout an asset's lifecycle. This understanding is essential for successfully managing usage resources before you begin amendment or renewal tasks.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Transaction Management is enabled
Benefits of Usage Management
Negotiation flexibility
Sales reps view and directly edit both default catalog rates and previously negotiated rates.
Auditability
An asset-level audit trail tracks all modifications to provide a clear history of changes.
Lifecycle support
Sales teams effectively negotiate new rates, grants, and quantities during early and on-time renewals.
Amend a Usage-Based Product
Change the rates, grants, or quantities of an existing asset to reflect new customer agreements.
Proration for Usage Amendments and Cancellations
Understand how the system recalculates grants when you change quantities or cancel services early.
Renew Usage-Based Assets Early
Change pricing on an active usage-based asset before the asset's end date by setting a new renewal term and negotiating rates and grants.
Renew Expired Usage-Based Assets
Continue a customer's subscription after a usage-based asset expires by setting a new renewal term and negotiating rates and grants.

=== ARTICLE: ind.qocal_anchor_with_monetary_commit.htm ===
---
article_id: ind.qocal_anchor_with_monetary_commit.htm
title: Anchor Product with Monetary Commitments
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_anchor_with_monetary_commit.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling_advanced_concepts.htm
fetched_at: 2026-09-04
---

# Anchor Product with Monetary Commitments

In a monetary commitment, your customer agrees to spend a specific dollar amount, for example, $1,000 per month. Monetary commitment products are used when your customer wants a discount on the overall spend and doesn’t want the discount to be tied to a specific resource type, such as SMS or storage.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
EXAMPLE

Anchor Product—Cloud Infrastructure Suite

Commitment Offer—if the customer signs a contract committing to$10,000 per month in total spend, they receive a 20% discount on all usage resources across the suite.

If the customer uses various services, such as storage, compute, and IOPS. Regardless of whether their actual usage calculates to $8,000 or $9,500, they’re billed the$10,000 minimum commitment.

=== ARTICLE: ind.qocal_anchor_with_quantity_commit.htm ===
---
article_id: ind.qocal_anchor_with_quantity_commit.htm
title: Anchor Product with Quantity Commitments
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_anchor_with_quantity_commit.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling_advanced_concepts.htm
fetched_at: 2026-09-04
---

# Anchor Product with Quantity Commitments

In a quantity commitment, the customer agrees to consume a specific number of units for a specific resource, for example, 100 GB of storage or 10,000 API calls.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

Customer purchases a commitment product that grants a fixed bucket of units at a lower price per unit.

If the customer consumes more than the committed quantity, the excess usage is charged as overage. For example, if a customer uses 110 GB when they commit to 100 GB. Depending on the configuration, the overage is billed at the standard anchor rate or a special commitment rate.

The commitment acts as a bucket. To make sure that usage draws from the committed bucket first, associate the anchor product that tracks the actual usage with this commitment.

EXAMPLE

Anchor Product—QuantumBit Database

Standard Rate—$1.00 per compute API call

Commitment Offer—if the customer agrees to the Monthly Compute Saver commitment, where they’re committing to 100 compute API calls per month, they get a $50 flat fee. The commitment rate gives them a discount of $0.50 per call.

If the customer uses calls beyond the committed quantity, the original rate of $1 per call applies. For example, if the customer uses 120 calls, they pay $70. For the first 100 calls, they pay $50 and $20 for the 20 overage calls at the standard$1.00 rate.

=== ARTICLE: ind.qocal_asset_lifecycle.htm ===
---
article_id: ind.qocal_asset_lifecycle.htm
title: Manage Asset Lifecycle in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_asset_lifecycle.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Manage Asset Lifecycle in Revenue Management

Track purchased products and services to provide excellent support and build your business relationships. Amend assets to meet changing customer needs, renew them for uninterrupted service, and cancel assets that you no longer require.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.

Through effective asset management, you can:

Amend assets to meet customers' changing needs.
Renew assets to provide uninterrupted service.
Cancel assets that are no longer needed.
Asset Lifecycle Management Principles and Permissions
Learn more about key terms and the permissions necessary to use Asset Lifecycle Management.
Set Up Asset Management in Revenue Management
Set up features that provide your sales reps and partners with the capabilities to efficiently manage assets.
View and Manage Assets in Revenue Management
Use the Assets tab on account and contract pages to track and oversee purchased products and services. This centralized view helps you to perform essential lifecycle tasks, such as changing renewal terms or enabling auto-renewal.
Amending, Renewing, and Canceling Assets
Use Revenue Management (formerly Revenue Cloud) to manage the products or assets that your customers purchase. With this feature, your sales reps can amend, renew, or cancel assets to meet the needs of your customers.
Asset Lifecycle Considerations
This topic details known limitations for the Asset Lifecycle features of Transaction Management.

=== ARTICLE: ind.qocal_asset_lifecycle_considerations.htm ===
---
article_id: ind.qocal_asset_lifecycle_considerations.htm
title: Asset Lifecycle Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_asset_lifecycle_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle.htm
fetched_at: 2026-09-04
---

# Asset Lifecycle Considerations

This topic details known limitations for the Asset Lifecycle features of Transaction Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Important Considerations
When you renew a bundle that includes one-time products, the system doesn't create Asset Contract Relationship records for those products. Renewal of one-time products isn't supported. The system sets the action to No Change and the quantity to zero, which prevents assetization. To manage Asset Contract Relationships for one-time products after renewal, manually create the ACR directly from the asset record on the account. See Create Asset Contract Relationships.
When amending or renewing an asset, you cannot change its price book or currency. The amendment or renewal transaction must use the same price book and currency as the initial sale.
Usage Selling Assets Considerations
Understand the limitations and behaviors of usage-based assets before setting up or selling usage products. Reviewing these requirements ensures accurate grant management, consumption tracking, and account binding throughout the asset lifecycle.
Field and Price Amendment Considerations
Familiarize yourself with the specific requirements for using Field Amendments and Price Amendments to update asset details and adjust pricing effectively. Understanding these technical mappings and supported fields helps you accurately reflect amendments in asset state periods (ASPs) and audit trails.
Transaction Rollbacks Considerations
Understand the requirements and limitations of the rollback feature to reverse the most recent transaction on an asset. Familiarizing yourself with these rules ensures data integrity and helps you determine when a transaction is eligible for reversal.
Changing Subscription End Dates of Termed Assets Considerations
Understand the requirements and limitations for modifying subscription end dates during amendments and renewals. Familiarizing yourself with these rules helps you accurately lengthen or shorten a subscription's term to meet evolving customer needs.
Zero-Quantity Quote Detail Lines Considerations
Zero-quantity quote detail lines appear when the lifecycle transaction state must be preserved even though the effective quantity for a period equals zero.
Asset Transfer Considerations
Familiarize yourself with the requirements and limitations for moving assets between accounts to ensure data consistency and compliance. Reviewing these constraints helps you manage quantities, price books, and product types correctly during the transfer process.
Swap, Upgrade, and Downgrade Amendments Considerations
Familiarize yourself with the requirements and restrictions for processing swaps, upgrades, and downgrades as specialized types of amendments. Understanding these constraints ensures accurate lifecycle management and prevents transaction errors during asset modification.
Considerations for Assets with Future-Dated Changes
Keep these considerations in mind when amending, renewing, canceling, transferring, or swapping assets with future-dated changes.
Considerations for Assets with Backdated Changes
These considerations apply when you amend, renew, or cancel an asset with an effective date in the past.
Add Assets Considerations for Amendment and Renewal Quotes and Orders
Before you add assets to an amendment or renewal quote or order, understand how the Contract lookup field affects which assets are eligible to appear in the Add Assets modal.

=== ARTICLE: ind.qocal_asset_lifecycle_date_time_precision.htm ===
---
article_id: ind.qocal_asset_lifecycle_date_time_precision.htm
title: Honor Precise Time Zones in Asset Lifecycle Start and End Dates
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_asset_lifecycle_date_time_precision.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_assets_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Honor Precise Time Zones in Asset Lifecycle Start and End Dates

Specify exact time zone precision for asset lifecycle start and end dates to meet detailed contract requirements and manage complex global subscriptions. Time resolution makes sure that asset state periods (ASPs) and subsequent amend, renew, cancel, transfer, and swap operations start and end exactly as specified, providing parity for noncontiguous changes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To specify time precision on quotes:	Create on Quotes
To specify time precision on orders:	PlaceOrder API permission set
IMPORTANT Set field-level security for the Start Time, End Time, and Start End Time Zone fields on the Quote Line Item and Order Product objects. You need the ManageAssets or CalmSObject permission set to set field-level security. Set Field-Level Security for a Field on All Profiles.

Standardized asset lifecycle processes honor the order line item (OLI) date and time when setting asset and ASP start and end dates during Order-to-Asset and Order-Product-to-Asset processes. By moving beyond the default 00:00:00 universal time-coordinated (UTC) setting, Revenue Management handles precise moments, such as a 12:00 AM PST start and 11:59 PM PST end.

During assetization, the line item time zone is stored on the ASP. When you amend, renew, or cancel an asset, the stored time zone is used to show the start and end dates and times instead of defaulting to UTC. This behavior keeps amendment and renewal dates aligned with the stored time zone and calculates the correct period boundary day.

Review these considerations for time precision.

All the line items in a transaction must have the same time zone.
Set the time zone on the quote or order line items to match the time zone on the ASP.
The pricing engine calculates prices by using UTC and doesn't support time precision.
Proration calculations use date precision only.
If you don't specify a start time, the start time defaults to 12:00:00 AM in the local time zone. If you don't specify an end time, the end time defaults to 11:59:59 PM in the local time zone.
If you don't specify a start or end time, the system defaults the time portion to 12:00 AM in the local time zone.
The system translates and stores all specified local times in UTC for disambiguation.
Each line item inherits its time zone from its source asset. When you amend, renew, or cancel multiple assets in a single action, use the same time zone for all the assets.
Set the Start End Time Zone field on a new sale to the customer's local time zone. The time zone is stored on the ASP and used for subsequent amendments, renewals, and cancellations.
Assets that are assetized before the time zone is stored on the ASP use UTC until they’re reassetized or you populate the time zone on the asset's existing ASPs.
In Setup, find and select Lightning App Builder.
Click Edit next to Order Record Page or Quote Record Page in the Lightning page list.
On the Components tab, find and select Transaction Line Editor, or drag it to the page if it isn't present.
On the right, click Select... next to Display Columns.
Move the Start Time, End Time, and Start End Time Zone fields from the Available section to the Selected section.
Click OK.
Save your changes.
Set field-level security for the Start End Time Zone field on the Asset State Period object.
Sync the context definition.

When field-level security is enabled for the Start End Time Zone field on the Asset State Period object, the sync updates the field mapping automatically. No manual mapping is required.

Initial Sale Example

A sales rep specifies a start time of 1/1/2025 9:00:00 PST and an end time of 12/31/2025 8:59:59 PST. The transaction system translates the time to 1/1/2025 17:00:00 UTC and 12/31/2025 16:59:59 UTC, respectively.

Amendment Example

An asset runs from 1/1/2025 17:00:00 UTC to 12/31/2025 16:59:59 UTC. A sales rep amends the asset with a start time of 2/1/2025 11:00 AM PST (2/1/2025 19:00:00 UTC). Upon assetization, the system creates consecutive ASPs.

The first ASP ends at 2/1/2025 18:59:59 UTC.
The new ASP starts exactly at 2/1/2025 19:00:00 UTC and ends at 12/31/2025 16:59:59 UTC.

Amendment Time Zone Example

A customer buys a yearly subscription with a start date and time of 1/1/2026 12:00 AM PST and an end date and time of 12/31/2026 11:59 PM PST. The time zone is stored on the ASP. When a sales rep initiates an amendment effective 7/1/2026, the amendment line items use the stored time zone instead of UTC. The amendment shows a start date and time of 7/1/2026 12:00 AM PT and an end date and time of 12/31/2026 11:59 PM PST.

=== ARTICLE: ind.qocal_asset_lifecycle_management_principles_and_permissions.htm ===
---
article_id: ind.qocal_asset_lifecycle_management_principles_and_permissions.htm
title: Asset Lifecycle Management Principles and Permissions
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_asset_lifecycle_management_principles_and_permissions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle.htm
fetched_at: 2026-09-04
---

# Asset Lifecycle Management Principles and Permissions

Learn more about key terms and the permissions necessary to use Asset Lifecycle Management.

Asset Lifecycle Management Principles

To use asset management, understand the crucial designs, data structures, and interactions that govern the system. Understand these terms that help users successfully use Asset Management features.

Assetization
After completing quote or order changes for an amendment, renewal, or cancellation, update your assets by using a flow to reflect the lifecycle changes.
Asset State Periods (ASPs)
ASPs represent the state of an asset over a period. Changes to assets create accurate asset state periods to provide parity for complex global subscription management.
Data Integrity and Audits
The transaction system maintains a complete and accurate history of all transactions through a ledger-style approach. Asset-level audit trails track all rate and grant modifications.
Last In First Out (LIFO)
If an asset consists of multiple prior sales transactions, use the LIFO strategy to compute the quote line item’s total price for negative quantities.
Managed Asset Viewer
A component added to the Account or Contract page layout that helps users to view and manage the asset lifecycle.
Future-Dated Changes
After completing quote or order changes for an amendment, renewal, or cancellation, update your assets by using a flow to reflect the lifecycle changes.
Rollback
A feature used to reverse the most recent future-dated amendment or renewal to restore an asset to its original state.
Proration
The transaction system automatically recalculates and prorates grants for usage-based products based on the asset's actual lifecycle during amendments or cancellations.
Asset Lifecycle Permissions

Before you begin managing assets, make sure that you have the necessary user permissions to perform successful feature adoption.

Assign user permissions based on the specific lifecycle task that you perform.

TASK	USER PERMISSIONS NEEDED
View Assets	Read, Create, Edit, and Delete access on Assets to manage assets and use the Managed Asset Viewer component.
Amend Assets	

InitiateAmendment API permission set

AND

Sales Rep persona permissions


Renew Assets	

InitiateRenewal API permission set

AND

Sales Rep persona permissions


Cancel Assets	

InitiateCancellation API permission set

AND

Sales Rep persona permissions


Time Zone Precision	To specify time precision on quotes, users need Create on Quotes and the PlaceOrder API permission set for orders.

=== ARTICLE: ind.qocal_asset_transfer_important_considerations.htm ===
---
article_id: ind.qocal_asset_transfer_important_considerations.htm
title: Asset Transfer Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_asset_transfer_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Asset Transfer Considerations

Familiarize yourself with the requirements and limitations for moving assets between accounts to ensure data consistency and compliance. Reviewing these constraints helps you manage quantities, price books, and product types correctly during the transfer process.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Asset Transfer Requirements and Constraints

Review these critical rules before initiating an asset transfer.

Quantity Synchronization: If you adjust the transfer quantity on one quote or order, manually update the destination quantity to keep them in sync. You change the line item quantity in the source order and then apply changes to the destination order.
Configuration Limits: You can’t reconfigure bundles or change product attributes on the source quote or order during a transfer.
Transaction Volume: Asset Transfer supports a maximum of 50 line items per transaction.
Product Compatibility: The initial release of Asset Transfer doesn’t support transferring ramped assets or usage-based products.
Asset Status: You can’t transfer an expired asset.
Pricing Restrictions: You can’t use different price books for a transfer.
API Behavior: The Transfer API is synchronous. Any issue during processing reverts the entire transaction.

=== ARTICLE: ind.qocal_assetize_assets.htm ===
---
article_id: ind.qocal_assetize_assets.htm
title: Update Assets to Reflect Changes by Using Flows
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_assetize_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_assets_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Update Assets to Reflect Changes by Using Flows

Update your assets after completing amendment, renewal, or cancellation changes to your quotes or orders. This process ensures that your assets accurately reflect modifications made to the asset lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To amend, renew or cancel assets:	

InitiateAmendment API, InitiateRenewal API, and InitiateCancellation API permission sets

AND

Sales Rep persona permissions


To open, edit, or create a flow in Flow Builder:	Manage Flow
To activate object state definitions:	Assetize Order permission set

Trigger the same flow you created and activated in Automate the Creation and Update of Assets from Orders by Using Flows to update your assets. Running this flow synchronizes your asset records with the final changes from your amendment, renewal, or cancellation transactions.

=== ARTICLE: ind.qocal_auto_refresh_stle_transaction_summary_considerations.htm ===
---
article_id: ind.qocal_auto_refresh_stle_transaction_summary_considerations.htm
title: Sales Transaction Line Editor and Transaction Summary Auto-Refresh Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_auto_refresh_stle_transaction_summary_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_auto_refresh_stle_transaction_summary_help.htm
fetched_at: 2026-09-04
---

# Sales Transaction Line Editor and Transaction Summary Auto-Refresh Considerations

Auto-refresh keeps data up to date across the Transaction Line Editor (TLE), Sales Transaction Line Editor (STLE), and Transaction Summary as sales reps make changes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

Review these considerations and limitations before configuring or enabling auto-refresh.

Auto-refresh only applies to changes made by the currently active sales rep's actions. If another user changes the same quote or order while it’s open, the active sales rep's view doesn't auto-refresh. To include those changes, select Refresh from the dropdown menu.
Turn on Change Data Capture for auto-refresh to work on both quotes and orders. Turning on only one object limits auto-refresh to that object type. Changes to quote line item, order item, quote line group, order line group, quote line detail, and order line detail refresh too.

=== ARTICLE: ind.qocal_auto_refresh_stle_transaction_summary_help.htm ===
---
article_id: ind.qocal_auto_refresh_stle_transaction_summary_help.htm
title: Turn On Auto-Refresh for the Sales Transaction Line Editor and Transaction Summary
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_auto_refresh_stle_transaction_summary_help.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_customize_transaction_line_editor.htm
fetched_at: 2026-09-04
---

# Turn On Auto-Refresh for the Sales Transaction Line Editor and Transaction Summary

Keep your sales reps focused on closing deals instead of reloading pages. To turn on auto-refresh for Sales Transaction Line Editor (STLE) and Transaction Summary, set up Change Data Capture for the quote and order objects. The auto-refresh feature captures changes made outside STLE, including record pages, flows, Apex triggers, and Agentforce actions. After it's turned on, sales reps see accurate line items right away, helping them work with confidence and complete quotes and orders faster.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.

Suppose a server-side process, such as an Apex trigger, an auto-launched or record-triggered flow, or an Agentforce action, updates a quote or order. STLE and the Transaction Summary automatically reflect the updated line items. You don't reload the browser to see the latest data.

Auto-refresh delivers value to your sales team in a few key ways.

Users see updated line items the moment that their automation changes a quote or order, which reduces errors and can speed up a deal.
Apex triggers, flows, and Agentforce actions benefit automatically. You don't change any code after you complete the one-time setup. There’s no disruption to existing automation.
The Refresh option in the dropdown menu reloads the STLE data, so users can use it to pull in any change that isn't auto-refreshed, such as an edit made by another user.
Auto-refresh uses the same access that grants use of the STLE. This feature doesn't introduce a new permission or permission set.

A Salesforce admin completes these steps.

From Setup, in the Quick Find box, enter Change Data Capture, and then select Change Data Capture.
In the Available Entities list, select Quote, and then click the arrow to move it to Selected Entities.
Select Order, and then move it to Selected Entities.
Select both quote and order for full coverage. If you turn on only one object, then auto-refresh works only for that object type.
Save your changes.

The next time a user opens a quote or order in the Sales Transaction Line Editor, auto-refresh is active.

IMPORTANT You don't turn on Change Data Capture on child objects. Turning on the quote and order objects covers edits to a quote or order and to its line items, line groups, and line-item attributes.

Only the user who triggers the change sees the auto-refresh. When a rep runs the flow, trigger, or agent action, that rep's STLE refreshes. If another user changes the same quote or order while a rep has it open, then the rep's STLE doesn't auto-refresh. The rep selects Refresh from the dropdown menu to pull in those changes.

If a refresh arrives and the user has no unsaved edits, STLE refetches the data quietly and shows the update after a brief loading state. When the user has unsaved edits, the STLE shows a prompt with these options.

Save: Save the pending edits, and then refresh the data.
Discard: Revert the pending edits, and then refresh the data.
Cancel: Keep the pending edits and don't refresh.

When a sales rep is mid-edit or a save is still processing, STLE holds incoming changes. The existing save or discard flow resolves the sales rep's unsaved edits.

The transaction summary refreshes the same way. Because it's read-only, it refreshes the data without a save or discard prompt.

Sales Transaction Line Editor and Transaction Summary Auto-Refresh Considerations
Auto-refresh keeps data up to date across the Transaction Line Editor (TLE), Sales Transaction Line Editor (STLE), and Transaction Summary as sales reps make changes.

=== ARTICLE: ind.qocal_automate_creation_and_update_of_assets.htm ===
---
article_id: ind.qocal_automate_creation_and_update_of_assets.htm
title: Automate Asset Creation from Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_automate_creation_and_update_of_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_asset_management_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Automate Asset Creation from Orders

To ensure assets related to an order remain current, use flows to create and update them. When you activate Revenue Management orders, create a record-triggered flow that invokes the Create or Update Asset from Order flow action. Customize the flow or add more conditions to perform other actions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To open, edit, or create a flow in Flow Builder:	Manage Flow
To activate object state definitions:	Assetize Order permission set
Create a Record-Triggered Flow
From Setup, in the Quick Find box, enter Flows, and then select Flows.
Click New Flow.
Select Record-Triggered Flow and click Create.
Select Order as the object.
Select A record is updated for the trigger configuration.
In the Set Entry Conditions section, specify these details.
Condition Requirements: All Conditions Are Met (AND)
Field: Status
Operator: Equals
Value: Activated
Configure Application Usage Type Assignment Records
Click .
Find and select Get Records.
Enter Get Application Usage Type for the label and Get_Application_Usage_Type for the API name.
Select Application Usage Assignment as the object.
Add these filter conditions.
Field: RecordId
Operator: Equals
Value: {!$Record.Id}
Click Add Condition and specify these filter conditions.
Field: AppUsageType
Operator: Equals
Value: RevenueLifecycleManagement
Select Choose fields and assign variables (advanced).
In the Record field, select New Resource.
Specify these details for the new resource.
Resource Type: Variable
API Name: ApplicationUsageAssignmentRecord
Data Type: Record
Object: Application Usage Assignment
Click Done.
Add a Decision to Check for Revenue Management Records
Click .
Find and select Decision.
Enter Revenue Lifecycle Management Record? for the label and Is_Revenue_Lifecycle_Management_Record for the API name.
Specify these outcome details.
Label: Revenue Lifecycle Management Record
API Name: Revenue_Lifecycle_Management_Record
Condition Requirements: All Conditions Are Met (AND)
Resource: {!ApplicationUsageAssignmentRecord.Id}
Operator: Does Not Equal
Value: {!$GlobalConstant.EmptyString}
Add an Action to Create or Update an Asset
Click  in the Revenue Lifecycle Management Record branch.
Find and select Action.
Specify these action details.
Action: Create or Update Asset from Order
Label: Invoke Order to Asset Action
API Name: Invoke_Order_to_Asset_Action
Order ID: {$Record.Id}
Click Done.
Save your changes.
Enter a label and API name for the flow and save again.
Activate the flow.

=== ARTICLE: ind.qocal_automate_tax_calculations.htm ===
---
article_id: ind.qocal_automate_tax_calculations.htm
title: Tax Configurations in Transaction Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_automate_tax_calculations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_common_capabilities.htm
fetched_at: 2026-09-04
---

# Tax Configurations in Transaction Management

Automate tax calculations for taxable products or services by using your selected tax engine, policies, and treatments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

Configure these settings to ensure compliance with tax regulations across different regions.

Create Tax Engine Provider and Tax Engine
Create Tax Policies and Treatments

=== ARTICLE: ind.qocal_backdate_asset_transactions.htm ===
---
article_id: ind.qocal_backdate_asset_transactions.htm
title: Backdate Asset Transactions
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_backdate_asset_transactions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_specialized_asset_considerations.htm
fetched_at: 2026-09-04
---

# Backdate Asset Transactions

Apply an amendment, renewal, or cancellation to an asset with a past effective date so that the asset reflects the change from the date it took effect.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To amend, transfer, or swap assets:	

Initiate Amend user permission

OR

initiateAmendment API access


To renew and cancel assets:	

Initiate Renew and Initiate Cancel user permissions

OR

initiateRenew API and initiateCancel API access

Before you backdate a change, review Considerations for Assets with Backdated Changes.

IMPORTANT Backdated changes require the standard flow for managing assets. In Revenue Settings, under Set Up Flow for Managing Assets, confirm that the flow API name is runtime_revenue_arcflows__arcFlow. If your org uses a custom or earlier flow, such as RLM_ARC_Assets, enter the new API name and save.

A backdated change is a transaction with an effective date in the past. It records an update that already took effect for the customer so the asset reflects the correct pricing, quantities, or status from the backdated effective date. You can backdate amendment, renewal, and cancellation transactions for standard and ramped assets. You can also backdate transfer and swap transactions for standard assets.

Backdated transactions can have a revenue recognition impact for your business. Consider adding a confirmation dialog to the user experience when they create a backdated amendment. The Salesforce Flow drives the amendment, renewal, and cancellation user experience. Add a confirmation dialog box to the flow specifically for backdated transactions.

If your org uses Revenue Cloud Billing, billing schedules and invoices align with the backdated effective date. The system prorates amounts for the affected period and generates credit memos for previously invoiced periods.

For the account that you want to change, go to the Assets tab and open the Managed Asset viewer.
Select the assets, and then select Amend, Renew, or Cancel.
Enter the effective date for the change.

Enter a date in the past and on or after the asset's start date.

Select Create Order, and then select Create Single Order.
Select the new order and activate it.

The asset state periods update so the asset reflects the change as of the backdated effective date.

EXAMPLE

Today is November 12, 2025. A customer canceled a product effective November 1, 2025, so that they aren't billed for access after that date. You select the asset in the Managed Asset viewer, select Cancel, and enter a cancellation date of November 1, 2025. Then, you create the cancellation order and activate it. The asset reflects the cancellation as of November 1, 2025, even though you entered the change on November 12, 2025.

To make a change that takes effect today or later, see Future-Dated Changes.

=== ARTICLE: ind.qocal_basic_example_ramp_deals_for_groups.htm ===
---
article_id: ind.qocal_basic_example_ramp_deals_for_groups.htm
title: Basic Example of Ramp Deals for Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_basic_example_ramp_deals_for_groups.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.ramp_deals_examples.htm
fetched_at: 2026-09-04
---

# Basic Example of Ramp Deals for Groups

See how sales reps can structure a simple, multiyear deal with phased rollouts, segment-specific pricing, and consolidated assets.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.

First, create a ramp deal to deploy products and services incrementally. Then, we apply segment-specific adjustments by applying discounts and price uplifts. Finally, we see how Transaction Management tracks consolidated assets for simplified management.

Introduction

Alex, a sales rep from SmartBytes, is negotiating a 3-year deal with Susan from Acme, a fast-growing client. Acme wants a solution that can scale with their business, starting with a main set of products that increase over time.

Alex knows that the Salesforce admin at SmartBytes set up the Ramp Deals for Groups in Quotes and Orders feature, which perfectly meets his requirements.

Create a Ramp Deal for Multiple Products

Alex creates a quote with the products required for the first year, and converts it into a group ramp segment.

Create a quote.
Add the necessary products, and enter the quantity.
Laptop with the One Time product selling model: 500
Digital Education Solution with the Term-Defined product selling model: 1000
Cloud Storage Pro with the Term-Defined product selling model: 1000
Click Add Group, and then click Save.
A group is created. Transaction Management automatically moves all the products into the group.
Click the group name to open the side panel.
Set the start and end dates for the first year.
NOTE If the segment type is Yearly, set the segment duration to 365 days.
For segment type, select Yearly.
Turn on Is Ramped.

Save the changes.

After Alex enters the dates for the group and turns on the Is Ramped setting, Transaction Management:

Creates a group ramp schedule and converts the group into the first ramp segment
Applies the group's dates to all the lines in the quote
Populates ramp and segment identifiers for all rampable products, including child products

In this example, Cloud Storage Pro, Digital Education Solution, and child products of Digital Education Solution are rampable products. So, Transaction Management populates ramp and segment identifiers for these products.

Because the product Laptop has a One Time product selling model, it’s not a rampable product. So, Transaction Management doesn’t populate ramp and segment identifiers for it.

Add Segments for Multiple Terms

For the second year, Susan wants the same number of laptops but twice the number of licenses. For the third year, Susan doesn’t want any laptops but wants to retain the same number of licenses as the second year.

Alex clones the segments to create segments and copy lines to the new segments.

To create a segment for the second year, click  corresponding to the group, and then select Clone Segment.
The Specify lines to clone window opens.
Select All Line Items, and then click Clone.

Transaction Management copies all the lines, including the non-ramped laptop line. Transaction Management also automatically increments and assigns dates to the new segment and the lines in it.
In the Quantity column for Digital Education Solution and Cloud Storage Pro, enter 2000.
To create a segment for the third year, click  corresponding to the second group, and then select Clone Segment.
Select Only Ramped Line Items, and then click Clone.
Transaction Management creates another ramp segment and copies only the ramped products to the newly created segment. Because laptops have the One Time product selling model, they’re not copied to the new segment.

To make it easier to read the group names, click  corresponding to any group, and then select Edit Ramp Schedule.
Update the segment names, and then save the changes.
If needed, change the start and end dates of the segments too.
Apply Discounts and Price Uplifts

Alex and Susan agree to a 5% discount in year one, then 5% and 10% price increases in years two and three. Susan also wants a quick snapshot of the pricing for Digital Education Solution before confirming their decisions.

Here’s how Alex applies the negotiated discount and price uplifts.

To apply for discounts all the lines for the first year, in the Adjustment Type column of the Year 1 group, select Discount as the type and then enter 5 as the value.
To apply price uplifts for the second and third year, in the Unit Price Uplift column of each line, enter the uplift percent values.
To view the price calculation, hover over values in the Net Unit Price column.
The price waterfall shows how the price was calculated, including the applied uplift.
To view the snapshot of the Digital Education Solution product, click  corresponding to any line of the product and then select View Ramp Details.
The View Ramp Details window shows details of the product, including segments, quantity, prices, discounts, and uplifts.

After these steps, Alex shares a single quote that clearly outlines the 3-year commitment, including changes in quantity, discounts, and pricing over time. She shares the quote with Susan, who reviews the quote and confirms the order. Alex creates an order from the quote, and then activates the order.

View Consolidated Assets

Alex takes a quick look at the assets to get an overview of the deal.

From the App Launcher, find and select Account.
In the All Accounts list view, click Acme.
For ramped products, Digital Education Solution and Cloud Storage Pro, Transaction Management creates only one consolidated asset for all the lines. This consolidation makes it easy to track and manage assets. For the non-ramped product, Laptop, Transaction Management creates a separate asset for each line.
Click  corresponding to Digital Education Solution, and then select View.
The Asset Action related list shows one asset action for the initial sale. The Asset State Period related list shows three asset state period records, one for each segment.

Click the Dashboard tab.
The Dashboard shows how quantity and monthly recurring revenue change over time.

=== ARTICLE: ind.qocal_before_you_begin_extending_your_transactions.htm ===
---
article_id: ind.qocal_before_you_begin_extending_your_transactions.htm
title: Before you Begin
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_before_you_begin_extending_your_transactions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_extend_your_transactions_with_custom_field_support.htm
fetched_at: 2026-09-04
---

# Before you Begin

Complete these requirements before configuring your extended transactions:

Turn on Context Service in Salesforce Setup.
Verify Permissions: Make sure that you have the Context Service Admin and Manage Revenue Cloud permissions to extend definitions.
Assign Pricing Permissions: Assign the Salesforce Pricing Design Time User permission to edit pricing procedures.
Set Security: Configure field-level security for all fields you intend to extend so they map correctly.
Grant Access: Provide read access to source custom fields and edit access to destination custom fields to help APIs to populate data.
Review Mapping Paths: Confirm that your business process aligns with supported mapping flows, such as Product to Quote Line or Order to Asset.

This table maps the business process and mapping required between their objects.

BUSINESS PROCESS OR API	SOURCE OBJECT	DESTINATION OBJECT	CONTEXT TO CONTEXT MAPPING REQUIRED?
Browse Catalog	Product	Quote Line	Y
Product	Order Product	Y
Configuration	Product	Quote Line	Y
Product	Order Product	Y
Quote to Order	Quote	Order	N
Quote Line	Order Product
Quote Action	Order Action
Order to Asset	Order Product	Asset Action Source	

Y

Use the AssetToSalesTransactionMapping


Order Item Detail	Asset Action Source
Order Action	Asset Action
Asset to Quote and Asset to Order	Asset Action Source	Quote Line Detail	

Y

Use the SalesTransactionToAssetMapping


Asset Action Source	Order Item Detail
Quote to Contract	Quote	Contract	Y
Order to Contract	Order	Contract	Y
NOTE You can't map a QuoteLineItem or OrderItem object to an Asset object.

=== ARTICLE: ind.qocal_cancel_assets.htm ===
---
article_id: ind.qocal_cancel_assets.htm
title: Cancel Assets with the Managed Asset Viewer
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_cancel_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_general_procedures.htm
fetched_at: 2026-09-04
---

# Cancel Assets with the Managed Asset Viewer

To optimize revenue and manage your product lifecycle, use the asset lifecycle cancellation action to terminate purchased products. The Managed Asset viewer on your Account or Contract page helps you to initiate cancellations and make sure that your records accurately reflect your business relationships.

Prerequisites

Before you begin:

Add the Managed Asset Viewer component to your preferred page layouts, such as the Account page layout.
Add the Assets related list to the Account or Contracts page to show the Managed Assets list.
To complete asset cancellations in Managed Assets, add the component to the Contracts page layout.
NOTE If the Create Quotes Without a Related Opportunity setting is true, creating a related opportunity is optional. If the setting isn’t true, the system creates an opportunity for a new cancellation quote. When you use the Contracts page layout, the system automatically adds the contract number to the cancellation quote or order. See Enable Quote Creation Without a Related Opportunity.

You can’t initiate a transaction with an earlier start date when an asset that has a future-dated amend, renew, or cancel transaction. If a cancellation quote line item contains a negative delta quantity, the system calculates the total price based on prior asset sale prices. For assets consisting of multiple prior sales transactions, the system computes the total price based on a Last In First Out strategy.

Cancel Assets
From the App Launcher, find, and select Accounts.
Click an account name in the Accounts list view.
Under Managed Assets, select the checkbox in the Asset Name column for the asset that you want to update. For bundled assets, select the parent asset instead of the child asset.
Select Cancel.
Select the cancellation date by using the calendar and click Submit.
The system creates a cancellation quote or order.
Review your cancellation request and save your changes.
EXAMPLE

=== ARTICLE: ind.qocal_clone_quotes_and_orders.htm ===
---
article_id: ind.qocal_clone_quotes_and_orders.htm
title: Clone Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_clone_quotes_and_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_sales_transactions_rev_cloud.htm
fetched_at: 2026-09-04
---

# Clone Quotes and Orders

Duplicate quotes or orders along with their associated line items and groups to save time and ensure data consistency. Cloning reduces manual entry errors by creating an exact draft replica of a source record while leaving the original unchanged.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To edit a page layout:	Customize Application

The cloning process copies the complete transaction structure, including field values, related records from standard and custom objects, product configurations such as bundles, standalone lines, grouped lines, and associated actions for quote line items and order products.

When you clone transactions with group ramp schedules, the cloned transaction preserves the original schedule structure. Amendment and renewal quotes with ramp schedules also preserve ramp and segment relationships after cloning.

For complex transactions, the process also duplicates group structures and clones amendment, renewal, and cancellation quotes.

Set Up Clone Quotes and Orders

When you turn on Clone Quotes and Orders on the Revenue Settings page, it reflects as the Deep Clone action on the quote or order record page.

From Setup, in the Quick Find box, search for and select Revenue Settings.
Turn on Clone Quotes and Orders.
NOTE This setting only controls user interface actions. The Clone Sales Transaction API supports cloning even when this setting is off.
Add the Deep Clone Action to Page Layouts

Add the Deep Clone action to page layouts to make the feature accessible on record pages.

From Setup, select Object Manager.
Select the Quote or Order object.
Click Page Layouts, select the specific layout to modify, and click Edit.
Select Mobile & Lightning Actions in the palette.
Drag the Deep Clone action into the Salesforce Mobile and Lightning Experience Actions section.
Save the layout.
Clone a Transaction

Clone an entire quote or order to create a duplicate of a transaction. Cloned quotes and orders are created in Draft status. Approval work items aren't copied to the cloned transaction.

Open a quote or order record.
Select Deep Clone from the dropdown menu.
Confirm the action.
NOTE
You can clone up to 6,000 records per transaction. For transactions with more than 1,000 lines, contact your Salesforce account executive to increase the limit.
Cloning quotes or orders using the Deep Clone action, Clone Sales Transaction API, or Deep Clone Sales Transaction invocable action doesn’t support the ISCLONE() formula function.
To clone custom objects and custom fields, configure the context definition for the sales transaction. For custom child objects, map the ParentReference field to the parent record ID.
Clone Lines or Groups

Duplicate individual components within a transaction by cloning specific line items or groups.

Open the quote or order record.
Select the component to copy.
To duplicate a line item, select the item and click Clone.
To duplicate a group, select the group and click Clone Group.
Review the duplicated data.
Line item clones include configurations, field values, and related records.
Bundle clones include the entire structure and all child line items.
Group clones include the group and every line item inside it.

=== ARTICLE: ind.qocal_common_capabilities.htm ===
---
article_id: ind.qocal_common_capabilities.htm
title: Transaction Management Features
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_common_capabilities.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Transaction Management Features

Manage common Transaction Management features across all sales transaction records for your business. Review these configurations to unify pricing, tax, and currency settings across your organization.

Pricing Customization for Different Transaction Types
Link custom fields to different pricing procedures to show unique prices based on the transaction type. For example, B2B customers receive volume discounts while B2C customers see standard pricing.
Multiple Currencies for Transactions
Turn on multiple currencies to help your users to transact in different global units. The system uses the currency code in the Quote or Order Currency fields to determine the transaction's currency.
Set Up Header Adjustments
Configure header adjustments to help your sales reps to apply discounts to an entire quote or order. Use the Discount Distribution Service (DDS) element in your pricing procedures to support this feature.
Tax Configurations in Transaction Management
Automate tax calculations for taxable products or services by using your selected tax engine, policies, and treatments.
Set Up Derived Pricing Assets to a Quote or Order
Streamline the quoting process by automatically adding derived product assets when your users add contributing products to a transaction.
Set Up Transaction Processing for Complex Product Configurations
To handle complex product configurations, increase the number of product attributes that a sales transaction can support. To control performance, you can also specify the number of records processed in a single transaction.

=== ARTICLE: ind.qocal_configure_placement_of_action_buttons.htm ===
---
article_id: ind.qocal_configure_placement_of_action_buttons.htm
title: Configure Header-Level Action Buttons in Sales Transaction Line Editor
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_configure_placement_of_action_buttons.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_customize_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Configure Header-Level Action Buttons in Sales Transaction Line Editor

To provide an intuitive experience for sales reps, you can customize the placement and sequence of action buttons in Sales Transaction Line Editor (STLE). Choose which actions appear as standalone buttons, button groups, or menu items in a dropdown list.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To customize the Transaction Line Editor or Sales Transaction Line Editor:	
Customize Application
Manage Revenue Management system permission

To view Transaction Line Editor or Sales Transaction Line Editor on the Orders page:	
Field-level security to these OrderItem fields:
ValidationResult (Read-only)
PriceWaterfallIdentifier (Read-only)
ParentOrderItemId (Read-only)
OrderActionId (Read-only)
Field-level security to these OrderItemRelationship fields.
AssociatedOrderItemPricing (Read-only)
AssociatedQuantScaleMethod (Read-only)
IMPORTANT Complete these prerequisites before you configure action buttons.
Turn on Enable Groups on the Revenue Settings page to include group-specific actions.
Turn on Header Adjustments on the Revenue Settings page to include QuoteAdjustment or OrderAdjustment actions.
Identify the exact, case-sensitive API names for the actions you want to appear.
In Lightning App Builder, open the quote or order record page and select Edit.
Select the STLE component.
In the Action Buttons field, enter the API names of the actions.
To show a single button, enter the action name on its own line. For example, enter AddGroup.
To separate multiple buttons with a divider line, enter the API names on the same line separated by a comma. For example, enter AddGroup, and Ungroup.
To nest actions as menu items under a main action button, place the secondary actions in parentheses. For example, enter MoveSelectedLines, (AddGroup), (Ungroup).
To create a standalone dropdown menu for multiple actions, enter the names in parentheses. For example, enter (AddGroup, ExpandAllGroups, CollapseAllGroups, Ungroup).
Save your changes.
Go to the quote or order record page to verify the button sequence and layout.

In Winter ’27, the STLE supports the built-in header-level actions that admins have been able to configure via the Lightning App Builder.

Set how many header-level actions are visible at run time and add button groups to organize actions specifically for your sales team. You can create up to 10 button groups, with each group having up to 10 actions. You can distribute up to 10 visible action slots across all groups. Within a group, drag actions to reorder them. The action picker lists only your available actions, so every action that you configure is available at run time.

If you don't specify which actions appear or how they're arranged, the editor shows the default actions divided into four groups. The first three groups contain a single action: QuoteAdjustment, AddAssets, and ImportQuoteLineItems. The last group contains the remaining actions, with only four visible.

Use these supported API names.

Supported Actions
ACTION API NAME	DESCRIPTION	DISPLAY LABEL	API NAME
AddAssets	Add assets to the editor.	Add Assets	AddAssets
AddGroup	Create a group of line items.	Add Group	AddGroup
Ungroup	Remove grouping from selected lines.	Ungroup	Ungroup
MoveSelectedLines	Reorganize selected lines within the editor.	Move Selected Lines	MoveSelectedLines
RepriceAll	Recalculate prices for all lines.	Reprice All	RepriceAll
BulkDelete	Delete multiple selected lines simultaneously.	Bulk Delete	BulkDelete
EstimateTaxes	Calculate tax estimates for the transaction.	Estimate Taxes	EstimateTaxes
ImportQuoteLineItems	Upload line items from an external source.	Import Lines	ImportQuoteLineItems
CreateRampSchedule	Create a ramp schedule.	Create Ramp Schedule	CreateRampSchedule
ManageHeaderAdjustment	Manage header changes.	Manage Header Adjustment	HeaderAdjustment
Action Button Group Considerations
Learn how action button groups behave in the Transaction Line Editor (TLE) and Sales Transaction Line Editor (STLE) to design an efficient experience for your sales team.

=== ARTICLE: ind.qocal_configure_ramp_segments.htm ===
---
article_id: ind.qocal_configure_ramp_segments.htm
title: Configure Ramp Segments in Ramp Deals for Lines
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_configure_ramp_segments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.understanding_ramp_deals.htm
fetched_at: 2026-09-04
---

# Configure Ramp Segments in Ramp Deals for Lines

Divide transaction lines into ramp segments with varying prices and quantities over time.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS
NEEDED
To configure ramp segments in quotes:	Create on Quotes
To configure ramp segments in orders:	Create on Orders

Ensure Ramp Deals for Lines in Quotes and Orders is turned on and the product has a ramp segment configured.

From the App Launcher, find and select Quotes or Orders.
Open the quote or order that contains the rampable product as a line item.
Open the tab with the Transaction Line Editor component.
From the quick action menu on the rampable quote line item, select Ramp.
The Ramp Deal window opens.
Enter a subscription term in months for the ramped line item.
Select a segment type-Annual or Custom.
Enter a trial term in days if you enabled a trial segment for the product.
Click to generate your segments.
Edit the discount and quantity details for each segment as required.
Click Update Segments to recalculate prices.
Save your changes.

View pricing in the Line Item Details tab or hover over Total Price in Transaction Line Editor.

Create a Product Ramp Segment
A ramp deal is a type of sales agreement where price and volume vary across time periods. A ramp segment is a specific period within a ramp deal during which certain prices and volume are in effect.

=== ARTICLE: ind.qocal_configure_transaction_processing.htm ===
---
article_id: ind.qocal_configure_transaction_processing.htm
title: Set Up the Transaction Processing Type for Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_configure_transaction_processing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Set Up the Transaction Processing Type for Quotes and Orders

Define how Revenue Management processes transactions by selecting a default Transaction Processing Type (TPT).

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create transaction processing type records and to select a default transaction processing type:	

Customize Application

AND

View Setup and Configuration

Set a default processing type for all transactions and define exceptions via the Tooling API. Use these configurations to turn on the Advanced Configurator or skip tax calculations. Help your sales representatives override the default, add the Transaction Type field to quote, and order page layouts.

IMPORTANT Select the default transaction type carefully. This action is irreversible after enablement.
Create a Transaction Processing Type record and specify preferences that use the TransactionProcessingType Tooling API.
From Setup, in the Quick Find box, search for and select Revenue Settings.
Turn on Transaction processing for quotes and orders.
Add the Transaction Type field to quote and order page layouts to provide override capabilities. See Customize Page Layouts with the Enhanced Page Layout Editor and Modify Field Access Settings.

=== ARTICLE: ind.qocal_considerations_for_assets_with_backdated_changes.htm ===
---
article_id: ind.qocal_considerations_for_assets_with_backdated_changes.htm
title: Considerations for Assets with Backdated Changes
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_considerations_for_assets_with_backdated_changes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Considerations for Assets with Backdated Changes

These considerations apply when you amend, renew, or cancel an asset with an effective date in the past.

You can't backdate a change to a date earlier than the asset's start date.
You can't backdate a change for an asset that has a future-dated cancel transaction.
You can't amend a usage-based product when both a future-dated change and a backdated change exist.
You can't reduce the quantity below the quantity available between the quote line item's start and end dates.

=== ARTICLE: ind.qocal_considerations_for_group_ramps_for_usage_products.htm ===
---
article_id: ind.qocal_considerations_for_group_ramps_for_usage_products.htm
title: Set Up Ramp Deals for Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_considerations_for_group_ramps_for_usage_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.setting_up_ramp_deals.htm
fetched_at: 2026-09-04
---

# Set Up Ramp Deals for Groups

After prerequisites are complete, here's the end-to-end setup flow.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
Step 1: Complete the Prerequisites

Complete all steps in Prerequisites: Ramp Deals for Groups. Turn on Enable Groups in Quotes and Orders, Clone Quotes and Orders, and Ramp Deals for Groups in Quotes and Orders. Optionally turn on Multiple Ramp Schedules Per Transaction and Trial Segments for Group Ramp Schedules.

Step 2: Configure the Product Discovery Flow

Use the Discover Products flow to select a catalog and then add products from the catalog to their associated record pages. The Discover Products flow is readily available with Product Discovery, and you can customize the flow beyond the available capabilities to meet your business needs. For more information, follow steps 5 to 7 in Prerequisites: Ramp Deals for Groups.

Step 3: Configure the Transaction Line Editor

In Setup, add the Sales Transaction Line Editor component to quote and order page layouts and configure it to show the required segment and group fields as described in the prerequisites.

Step 4: Create Ramp Schedules

In Setup, find and select Revenue Settings. In Set Up Flow for Creating Ramp Schedules, provide the API name of the flow to use when creating a ramp schedule. This setting unlocks segment selection, letting sales reps add products to the current segment only or to current and subsequent segments.

Step 5: Test

Create a quote or order with ramp deals for groups to verify the setup works as expected.

=== ARTICLE: ind.qocal_considerations_ramp_deals.htm ===
---
article_id: ind.qocal_considerations_ramp_deals.htm
title: Considerations for Ramp Deals
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_considerations_ramp_deals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm
fetched_at: 2026-09-04
---

# Considerations for Ramp Deals

Review these known considerations and limitations for the Ramp Deals feature.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
Ramp Deals for Lines
Transaction Management supports ramp deals for term-defined products. You can't use bundle products.
You can't renew a ramp deal before its end date.
You can't create a price-only amendment for a ramp deal.
You can configure up to 10 ramp segments per transaction line.
Uneven subscription terms round to full years, and the remaining months go in the last segment with prorated pricing.
Transaction lines require start and end dates.
Segment start and end dates can't have gaps or overlaps.
In an initial sale, you can edit the start date of the first annual ramp segment.
After you configure and save ramp segments on a transaction line, you can't change the start and end dates of the transaction line.
When you create an amendment transaction, you can't add or delete ramp deals.
In an amendment transaction, the Ramp Deal window shows the changes in the total price of the transaction.
Generated quote PDFs that include ramp deals don't show any difference between the ramped transaction lines and other transaction lines.
Ramped line items support the GMT time zone only. Non-GMT time zones aren't supported.
Ramp Deals for Groups

Transaction Management doesn't create ramps for all products in group ramp segments. A group ramp segment contains ramped lines and non-ramped Lines. When assetized, ramped lines become a single consolidated ramped asset, with associated asset state periods representing individual segments. Non-ramped lines become standard non-ramped assets.

Separate assets are created for each line for these products.
Supported Ramp Deal Products
PRODUCT TYPE	SUPPORTED
Term-defined standard	
Term-defined standard usage	
Standalone one-time	
Standalone evergreen	
Bundle with a parent and all children termed defined	
Bundle with a parent term-defined, but any child is one-time or evergreen, and Quantity Scale Method (QSM) = Proportional	
Bundle with a parent term-defined, but any child is one-time or evergreen, QSM = None or Constant, and Allow Quantity Edit = True	
Bundle with a parent term-defined, any child is one-time or evergreen, QSM = None or Constant, and Allow Quantity Editing = False	
Bundle with a one-time evergreen parent, and a term-defined child	
Nested bundle with a term-defined parent, and other parents are term-defined	
If you add derived pricing products to a ramp deal for groups, their prices don't calculate correctly.
With only Ramp Deals for Groups enabled (Multiple Ramp Schedules off), create only 1 ramp schedule per transaction. The ramp schedule is implicit—the entire transaction is part of a single ramp schedule.
When Multiple Ramp Schedules Per Transaction is on, you can create up to 10 ramp schedule groups in a quote or order.
You can create up to 12 group ramp segments in a ramp schedule.
After converting a group into a ramp segment within a schedule, you can clone the ramp segment to add more segments. You can't convert any other group within the schedule into a ramp segment.
When you turn on Multiple Ramp Schedules Per Transaction, you can't add non-ramped groups within ramp schedule groups.
You can't create a group ramp schedule for groups that contain child groups.
You can't create nested groups in group ramp segments.
You can't apply renewal price uplifts tied to the Consumer Price Index (CPI) to ramped products.
You can't create ramp deals for groups and ramp deals for lines in the same quote or order.
Product Configuration in Ramp Deals
For line-level ramps, configuration stays consistent across all ramp segments.
For group-level ramps, most configuration changes that you make in a ramp segment apply to the current and subsequent segments. Previous segments remain unchanged to preserve data integrity.
Root or component quantity updates apply only to the current segment and don't propagate to other segments.
When you include or exclude a child product within a bundle in one segment, that change propagates to all subsequent segments. If you remove a child product from a segment that remains in previous segments, you can't add it back again in subsequent segments. This restriction prevents gaps in the ramp schedule.
Attribute changes made to a child product propagate only to the subsequent segments that include that child product.
Configuration rules override your manual ramp segment configurations and evaluate for each segment.
Configuration rules don't recognize quote or order groups. Rules that add standalone products to a ramp segment don't automatically ramp them or add them to subsequent segments. However, this behavior doesn't affect child products of a ramped parent product. When a rule adds a child product to a previously ramped parent, it also ramps the child product and adds it to subsequent segments.
When initiating Browse Catalog from a ramp segment, configuration for non-rampable products isn't available.
Amend, Renew, and Cancel Ramped Assets
With Ramp Deals for Groups enabled, amending, or canceling ramped assets automatically creates groups.
With Single Ramp Schedule (Groups ON, Multiple OFF), you can amend multiple ramped assets in a single transaction only if the start and end dates of all their asset state period (ASP) records match. Don't add or delete ramp segments during amendments.
With Multiple Ramp Schedules (Groups ON, Multiple ON, you can amend multiple ramped and non-ramped assets in one transaction, even if their ASP start and end dates don't match. Transaction Management groups assets into a ramp schedule when the asset lifecycle and all ASP dates match. Don't add or delete segments for existing assets. However, you can create group ramp schedules on amendment, renewal, and cancellation quotes or orders to generate other ramp deals.
You can't change the start and end dates of auto-generated segments. To make structural changes, create a separate amendment.
During the renewal of a ramped asset, the price uplift from the final segment becomes the renewal uplift.
You can't use these capabilities when amending, renewing, or canceling ramped assets: lot-based renewal, asset transfer, early renewal (except via the dedicated early renewal flow), and rolling back the most recent amendment.
Editing the start date of the first segment of an amendment quote or order in the Edit Ramp Schedule page requires the date to be within the original segment's date window. You can't have any future dated amendments, renewals, or cancellations scheduled.
Ramp Segments
START DATE	END DATE
1/1/2026 (initial sale)	12/31/2026
1/1/2027	12/31/2027
1/1/2028	12/31/2028

If you amend the deal on 6/1/2026, you can only edit the amendment start date to be between 1/1/2026 and 12/31/2026.

You can only delete newly cloned segments in an amendment quote or order.
You can only clone the last segment. If you prorate the last segment, then the second to last segment is the segment you can clone. Segment cloning differs from segment extension because an extension is always applied to the last segment, regardless of segment type.
You can clone or change the end date of the last segment, but you can't do both in a single amendment transaction per ramp schedule. For example, you can't use the Clone segment action if you extended the end date on the auto-generated ramp schedule in the current transaction, and vice versa.
You can't change start or end dates during amendments on ramp schedules containing usage-based assets. You can only clone those segments.
If there's only one auto-generated segment in the amendment quote or order, you can't clone that segment.
Compound Uplift in Ramp Deals
Compound uplift is available only when you turn on Advanced Detail Line Pricing in Revenue Settings. Without this preference turned on, you only see standard uplift. Make sure to sync your context definition.
Ramp uplift type applies to the ramp schedule group level and propagates to all lines in that group. For initial sales, you can't set the ramp mode per line.
Ramp uplift type is read-only on individual quote line items and order products. You can update the ramp uplift type on quote line group and order item group. The value on the parent group applies, and group-level changes cascade to every ramped line.
New ramped lines added to the transaction inherit the ramp uplift type from its group. After a quote line is assetized, the mode recorded in the asset state period can't change. Amendments and renewals inherit the original mode for asset-sourced lines. Uplift percentages update, but you can't change the mode to standard or compound.
All ramped line items in a single initial sale transaction have the same ramp uplift type for initial sales. Amendment and renewal quotes can contain a mix of standard and compound asset-sourced lines. Each line keeps the type from its own asset state period.
The first segment of any ramp deal has no preceding segment to compound from. That segment is always priced at the baseline with an applied uplift equal to the unit price uplift on the line item.
On renewal, the compound uplift resets. Year 1 of the new term becomes the new baseline.
For amendments, the previous segment uplift is used to calculate the applied uplift percentage. The previous segment uplift is the preceding asset state period in chronological order.
Existing ramped records created before Winter ’27 use standard uplifts. Compound mode applies only when set on new transactions.
You can't use compound uplift with Consumer Price Index (CPI) uplifts, usage-based products, or derived pricing products.
The default pricing procedure templates in Revenue Management don't automatically update for compound uplift. Update your pricing procedure's price revision element to support compound uplift. See Salesforce Help for configuration guidance.
The price revision element is used to apply compound ramp uplift to ramped lines. Refer to the Apply Uplifts to Ramped Subscription Items section in the Revenue Management Default Pricing Procedure Template. Review Build Your Expression Set From a Template.
Turning off Advanced Detail Line Pricing after quotes, orders, or assets exist with compound ramp uplift causes pricing calculations, amendments, and renewals to return incorrect prices.
Dynamic Revenue Orchestrator (DRO) and Ramp Deals
Turn on the rampDealForQocal setting in your org and make sure that your order line items include ramp and segment identifiers.
For amend, renew, and cancel orders. DRO applies the same order action to all segments, even if a specific segment hasn't changed. DRO applies order line item actions to fulfillment order lines and processes them.
DRO skips Staged Assetize steps in ramp order fulfillment plans and assetizes all segments at plan completion.

=== ARTICLE: ind.qocal_considerations_syncing_quotes_and_opportunities_in_revenue_cloud.htm ===
---
article_id: ind.qocal_considerations_syncing_quotes_and_opportunities_in_revenue_cloud.htm
title: Considerations for Syncing Quotes and Opportunities
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_considerations_syncing_quotes_and_opportunities_in_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_management_lifecyle.htm
fetched_at: 2026-09-04
---

# Considerations for Syncing Quotes and Opportunities

Get to know the data differences between quotes and opportunities before you sync quote line items to an opportunity. These differences determine how the quote to opportunity sync handles bundle products, attributes, and term-defined items. Review these behaviors to ensure data consistency between your quotes and related opportunities.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

Starting the sync process makes sure that any changes you make to quote line items automatically update the associated opportunity.

Syncing occurs only from quote line item to opportunity product. You can't update the opportunity products while the sync is in process.

If the out-of-the-box sync process is running, you can’t use a custom automation to update quote line item fields to opportunity product fields as the fields lock.

Product and Attribute Mapping
Opportunities don’t support bundle structures, so the system adds all products within a bundle as separate, individual products in the opportunity.
Products appear as separate quote line items rather than a bundle when you create a subsequent quote from an opportunity.
The system doesn’t copy the selected quote line item’s attributes to the opportunity because opportunities don’t support product attributes. If needed, you can manually select attribute values when creating another quote from that opportunity.
Field Visibility and Term-Defined Products
Opportunity line items don’t include term-definition fields, such as period boundaries.
The system transfers only one-time products and excludes term-defined products when you create a quote from an opportunity.
Manage the Sync Process
Use the Start Sync quick action on the quote page to begin the process.
Use the Stop Sync quick action on the quote page to terminate the automatic update process.

=== ARTICLE: ind.qocal_considerations_usage_selling.htm ===
---
article_id: ind.qocal_considerations_usage_selling.htm
title: Usage Selling Assets Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_considerations_usage_selling.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Usage Selling Assets Considerations

Understand the limitations and behaviors of usage-based assets before setting up or selling usage products. Reviewing these requirements ensures accurate grant management, consumption tracking, and account binding throughout the asset lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Usage Asset Lifecycle Behaviors

When you manage usage-based assets, the system applies specific rules to rates and resource grants.

Amended Rates: The rate for an amended asset changes to reflect the new terms.
Unused Grants: The system forfeits any unused resource grants when you renew or cancel the asset.
Grant Proration: The system supports proration for these scenarios.
Amendments: The amendment process prorates new grants amended mid-term for the remaining duration.
Refreshes: The refresh process prorates new grants.
Cancellations: The cancellation process prorates grants for the remaining duration based on the cancellation date.
Early and Late Renewals
Amendments, renewals, and cancellations require today's date or a future date as the effective date. Past-date changes are blocked to prevent billing mismatches with recorded usage.
You can renew expired assets with a start date that can be today, in the future, or in the past after the expiry date. The process fills gaps with zero Asset State Periods.
Ramped usage-based products don't support amendments, renewals, or cancellations with a backdated or future-dated effective date. Use today's date for these transactions on ramped usage-based products.
Consumption Object Updates for Same-Day Cancellations

When you create and cancel assets within the same day, associated consumption objects remain active. Update these fields to prevent continuous summary generation and rating failures caused by missing rate card entries.

CONSUMPTION OBJECT	FIELD UPDATES
Usage Entitlement Account	Set the end date and time to match the start date and time.
Usage Entitlement Bucket	Set the end date and time to match the start date and time.
Transaction Usage Entitlement	Set the end date and time to match the start date and time.
Liability Summary	Set status to Invoiced.
Usage Ratable Summary	Set status to Rated and rate to zero.
Usage Summary	Set status to Liable Summary Complete.
Grant Binding Requirements

The transaction system prioritizes accounts for grant binding based on the specified hierarchy.

1. Opportunity Account
If present, the system uses the opportunity account even if an account for quote exists.
2. Account for Quote
If the opportunity account is missing, the system uses the account specified in the Account for Quote field.
3. Binding Failure
Grant binding fails if both the opportunity account and account for quote are missing.
NOTE

If you turn off the Create Quotes Without a Related Opportunity setting, the Account for Quote field is unavailable. Binding fails in this scenario even if an opportunity is linked to the quote.

SEE ALSO
Usage Management Limits

=== ARTICLE: ind.qocal_consumer_price_index_and_price_uplifts.htm ===
---
article_id: ind.qocal_consumer_price_index_and_price_uplifts.htm
title: Use Consumer Price Index for Automated Renewal Price Uplifts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_consumer_price_index_and_price_uplifts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.pricing_apply_policy_driven_price_revisions.htm
fetched_at: 2026-09-04
---

# Use Consumer Price Index for Automated Renewal Price Uplifts

Automate the calculation of renewal price increases by using the consumer price index (CPI) and additional negotiated price uplift. With this feature, your pricing keeps pace with market conditions and maximizes your high-margin annual contract value (ACV).

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To use CPI for renewal price uplifts:	Renew Assets user permission

Integrating CPI into your renewal price uplift strategy provides significant business benefits.

Price uplift provides instrumentation to monetize ongoing investments in products, platforms, and support.
Uplift minimizes the impact of dollars lost on an account, helping offset attrition.
Price uplift delivers a significant amount of high-margin ACV. All uplift dollars count toward the account executive quota.
Price uplift can be offset or combined with extended terms or additional products during negotiations.
Customers often raise their own prices based on market conditions, input costs, and other factors, requiring similar tools for monetization.
By tying the renewal uplift percentage to CPI, you can apply the new price at renewal time, based on CPI and any additional negotiated uplift amount.

Salesforce admins create price revision policies—for example, US CPI, that define the floating rate portion of the renewal price uplift. Over time, your admin creates index rate records to define the value for a price index for a time period. The US CPI for July 2025 was 2.7%.

Sales reps who are negotiating a deal at the quote line item or order item level select a price revision policy. They select a spread over the base rate in the Unit Price Uplift field—for example +5%, to get the CPI-based uplift, such as US CPI plus 5%.

At renewal time, the system automatically calculates the correct price based on the price revision policy, index rate, and unit price uplift. For example, CPI-adjusted uplift for a renewal in July 2025 is 7.7% because US CPI was 2.7% and the agreed-upon spread was +5%.

To implement CPI-based renewal uplift, configure data objects and fields within Revenue Management to capture and apply relevant inflation data.

Configure a price revision policy.
With a price revision policy, a Pricing design-time user or Salesforce admin can define the CPI policy and the formula to be applied when calculating renewal uplift.
From the App Launcher, find and select Price Revision Policies.
Click New, and update the new price revision policy fields.
For example, set Policy Name to US CPI, Argentina Inflation Rate, or United Kingdom Inflation Rate; Type to Price Index; Effective From to 1/1/2025; Effective To to 12/31/2025; Region to US instead of Argentina or the United Kingdom; and Formula to PriceIndex, that is, the variable rate added to the fixed renewal uplift percentage.
Define and capture CPI data by creating index rate records, and save your changes.
Add the Price Revision Policy Name field and the Unit Price Uplift field to the Transaction Line Editor component on the quote and order pages.
In Setup, find and select Lightning App Builder.
Click Edit next to Quote Record Page.
On Quote Record Page, select the Transaction Line Editor (TLT 2.0) component.
On the component properties pane, under Display Columns, click Select....
In the Available section, select Unit Price Uplift and move it to the Selected section. Click OK.
Save your changes.
In Lightning App Builder, select Edit next to Order Record Page.
To add the Unit Price Uplift field to Transaction Line Editor, click the Details tab on Transaction Line Editor.
Click the Fields tab, and search for Unit Price Uplift.
Drag the Unit Price Uplift field to the Record Detail component.
Save your changes.
Add the Price Revision Policy field on quote line item (QLI), order product (OP), and asset state period (ASP) objects.
From Setup, in the Quick Find box, enter Object Manager, and then select Object Manager. Next, click Quote Line Item, and then click Page Layouts.
Click Quote Line Item Layout.
If the Pricing Revision Policy field isn't present in the Pricing Information section, in the Quick Find box, enter Price Revision Policy, and then drag the field to the Pricing Information section.
Save your changes.
Similarly, add the field to OP and ASP.
Add the Unit Price Uplift field to the QLI and OP objects.
From Setup, in the Quick Find box, enter Object Manager, and then select Object Manager. Next, click Quote Line Item, and then click Page Layouts.
If the Unit Price Uplift field isn't present in the Pricing Information section, in the Quick Find box, enter Unit Price Uplift, and then drag the field to the Pricing Information section.
Save your changes.
Similarly, add the field to OP.
Create a renewal quote or order.
If the asset’s pricing source is last transaction price (LTP) and uplift type is CPI/Variable, the net unit price is calculated as the latest asset action source (AAS) change in subtotal divided by the change in quantity * (1 + the renewal uplift percent).
The renewal process requires a matching CPI record for the effective date. If an effective date can't be found, an error occurs.
Sales reps can apply an additional discount on top of the calculated price uplift, overriding the net unit price.
EXAMPLE

Sales reps can use CPI in several scenarios to determine the final renewal price.

Standard CPI calculation: Revenue Management calculates the renewal price by applying the CPI rate plus an additional defined uplift percentage to the LTP.

Last Transaction Price: $100
CPI Percentage: 3.5%
Additional uplift percentage: 2.0%
Calculation: LTP * (1 + CPI % + additional uplift %)
Result: $100 * (1 + 0.035 + 0.02) = $100 * 1.055 = $105.50

Asset renewal with a defined CPI type: The renewal flow checks the asset for specific CPI settings to determine the correct price.

Asset configuration: A Sales Cloud asset has an LTP of $150 per user per month, a CPI type of US CPI, and an additional 3% uplift with an uplift type of CPI/Variable.
CPI data match: The renewal process finds and uses a US CPI record for the effective renewal date with a 4.50% CPI value.
Net unit price calculation: Revenue Management calculates the new net unit price as $150\times (1 + \text{CPI} + \text{Renewal Uplift}). Result: $150\times (1 + 0.045 + 0.03) = 150\times 1.075 =\mathbf($161.25).

Regional/international uplift: CPI uplift supports defining different inflation rates for localized sales.

A sales rep operating in China negotiates a renewal for Sales Cloud. The asset is set with an uplift percentage of 3%, an uplift enumeration of CPI uplift, and an uplift type of China Inflation Rate. The renewal process uses the correct CPI data for China, such as the 8% China Inflation Rate from January 2025.

Automated periodic price amendments: Sales reps can use CPI to automatically adjust prices periodically, not just at the primary renewal date.

For a three-year contract with a CPI anniversary clause, CPI automatically updates the prices for year two and year three at the first and second anniversary dates.
The system automatically sends a notification to the customer informing them of the price change.

=== ARTICLE: ind.qocal_consumer_price_index_and_uplifts_important_considerations.htm ===
---
article_id: ind.qocal_consumer_price_index_and_uplifts_important_considerations.htm
title: CPI and Renewal Price Uplift Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_consumer_price_index_and_uplifts_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_renewal_price_uplifts.htm
fetched_at: 2026-09-04
---

# CPI and Renewal Price Uplift Considerations

Familiarize yourself with the supported product types, field behaviors, and system logic for applying Consumer Price Index (CPI) and renewal price uplifts. Understanding these constraints ensures accurate pricing calculations during asset renewal and helps you determine where uplift data appears in the price waterfall.

Product and Field Support

Review these functional limitations for price uplifts to ensure your products and quote lines support the feature.

CPI renewal price uplifts apply only to termed assets.
One-time and evergreen assets don’t support price uplifts.
Usage-based products don’t support price uplifts.
Derived pricing products don't support price uplifts.
Ramped quote line items and order line items don’t support the Price Uplift field.
System Behavior and Pricing Logic

Understand how the system processes uplift data during the renewal phase.

Renewal uplift percent appears in the price waterfall.
If the asset pricing source is list price, the system ignores the uplift field and doesn’t uplift the price at renewal time.

=== ARTICLE: ind.qocal_contract_management_essentials.htm ===
---
article_id: ind.qocal_contract_management_essentials.htm
title: Contract Management Essentials
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_contract_management_essentials.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contracts_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Contract Management Essentials

Understand the components of Revenue Management contracting to organize customer assets efficiently and maintain accurate pricing agreements throughout the business relationship.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

Map assets to their respective contracts through Asset Contract Relationships. Then, assign the required application usage tags to ensure the correct legal and financial terms govern every product. This foundational knowledge helps your sales operations team to use advanced automation like contract cotermination and cumulative pricing, which streamlines the renewal process and promotes larger customer purchases. Understanding these structures is essential before you begin creating records or negotiating complex multi-tier discounts.

Create a Contract and Application Usage Assignment
Set up a contract to centralize the management of your customers' assets and establish negotiated pricing by assigning a Revenue Management lifecycle usage tag.
Create Asset Contract Relationships
Manually link assets to a contract to track which products-specific customer agreements govern. Creating these relationships helps you to review contract details or open related contracts directly from an asset record.
Manage Contracts in the Revenue Management
Manage contracts and their assets and contract pricing schedules.

=== ARTICLE: ind.qocal_contract_pricing_extensibility.htm ===
---
article_id: ind.qocal_contract_pricing_extensibility.htm
title: Set Up Contract Pricing Extensibility
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_contract_pricing_extensibility.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contract_pricing_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Set Up Contract Pricing Extensibility

Define unique Contract Item Price (CIP) records by using custom fields to bypass default uniqueness checks and record validations. This extensibility helps your business to set flexible contract pricing based on custom parameters that match your specific organizational needs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To set up contract pricing extensibility:	Salesforce admin

By default, Revenue Management provides one negotiated contract price per unique product and Product Selling Model (PSM) combination for a specific date range. This restriction prevents you from defining multiple Contract Item Price (CIP) records for the same product and PSM during overlapping effective dates.

From Setup, in the Quick Find box, find and select Revenue Settings.
Turn on Advanced Order Creation From Quote to generate multiple orders from a single quote.
Turn on Customize Contract Pricing to define unique contract item prices based on custom fields.
To apply contract item prices with custom fields at run time, complete these additional setup steps.
Add a custom field, such as Location__c, to the Contract Item Price (CIP), Order Item, and Quote Line Item (QLI) objects.
Add the custom field to the Contract Pricing Entries decision table.
Update your default pricing procedure to include the new custom field.
Update context definition mappings for QuoteEntitiesMapping and OrderEntitiesMapping to map STI.ItemCustomFieldId to both QuoteLineItem.CustomFieldId and OrderLineItem.CustomFieldId.
Save your changes.

=== ARTICLE: ind.qocal_control_access_to_states_and_state_transitions.htm ===
---
article_id: ind.qocal_control_access_to_states_and_state_transitions.htm
title: Control Access to States and State Transitions
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_control_access_to_states_and_state_transitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_order_lifecycle_management_using_object_state_definitions.htm
fetched_at: 2026-09-04
---

# Control Access to States and State Transitions

Create custom permissions to restrict or grant access to order states and transitions for specific user groups. Assigning these permissions ensures that only authorized agents move an order to its next supported stage in the fulfillment process.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Add the Custom Permission field to the Object State Value and the Object State Transition page layouts. See Customize Page Layouts with the Enhanced Page Layout Editor.
Create custom permissions. See Custom Permissions.
Edit object state values or object state transition records, and in the Custom Permission field, select a custom permission. See Create Object State Values and Create Object State Transitions.
Assign custom permissions to users. See Enable Custom Permissions in Permission Sets.

=== ARTICLE: ind.qocal_coterminate_contract_important_considerations.htm ===
---
article_id: ind.qocal_coterminate_contract_important_considerations.htm
title: Considerations for Contract Cotermination
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_coterminate_contract_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_coterminate_with_contract_end_date.htm
fetched_at: 2026-09-04
---

# Considerations for Contract Cotermination

Review the limitations and requirements for aligning subscription end dates with contract end dates to ensure successful sales and renewal processes. Reference these specifics when you build or troubleshoot transactions that use cotermination.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Ramped Products Limitations

The following restrictions apply when you use cotermination with ramped products:

Users can’t add ramped products to a quote or order that references a contract with the cotermination flag set to True.
Assetization generates an error when an order attempts to assetize both a cotermed contract and ramped products.

=== ARTICLE: ind.qocal_coterminate_with_contract_end_date.htm ===
---
article_id: ind.qocal_coterminate_with_contract_end_date.htm
title: Coterminate Subscription Assets with Contract End Dates
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_coterminate_with_contract_end_date.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contract_pricing_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Coterminate Subscription Assets with Contract End Dates

Synchronize subscription end dates with their corresponding contract end dates to improve accuracy and efficiency in sales and renewal processes. Cotermination reduces manual mistakes, simplifies renewals, and minimizes administrative tasks associated with managing subscription lifecycles.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To use contract cotermination:	Renew Assets user permission
Considerations for Contract Cotermination
Review the limitations and requirements for aligning subscription end dates with contract end dates to ensure successful sales and renewal processes. Reference these specifics when you build or troubleshoot transactions that use cotermination.
Prerequisites to Use Cotermination

Before you begin, configure Contract Cotermination.

In Setup, select Object Manager.
Search for and select Contract.
In the Contract Layout, add the Co-termination field to the Contract Detail section.

After you turn on cotermination, API validation prevents saving quote line items (QLIs) or order line items (OLIs) if their end dates don’t align with the contract end date. Sales reps typically operate at the contract level, so synchronized end dates for all subscriptions within a contract facilitate smooth renewal events.

Perform Contract Cotermination
From the App Launcher, search for and select Contracts.
Select a contract record
On the Details tab, select Contract Cotermination.
Create an initial sale, amendment, or renewal quote or order for that contract.
Add termed subscription products to the quote or order.
The quote line item (QLI) or order line item (OLI) end date automatically populates to match the contract end date. The system locks these end dates to prevent manual edits.
EXAMPLE
Consider contract A with a start date of 1/1/2025 and an end date of 12/31/2025 with cotermination enabled.
User created an initial sale order on 2/1/2025 and assigned the order to contract A.
User added a product to the order and noted that the OLI's start and end dates are automatically set to 2/1/2025–12/31/2025. With the end date locked, the subscription end date is set to coterminate with the contract end date.
After the Quote-to-Order process and assetization, the product is created with subscription dates of 2/1/2025–12/31/2025.

Add-on sale order:

User starts with the same contract A with a start date of 1/1/2025 and an end date of 12/31/2025.
User adds another product to this contract on 3/1/2025 by creating an initial sale order and linking it to contract A.
The QLI's start date and end date are automatically set to 3/1/2025–12/31/2025. The subscription end date is set to the contract end date.
After assetization, the product is created with subscription dates of 3/1/2025–12/31/2025.

Amendment order: A user extends contract A’s end date to 6/30/2026 and then amends a product. The product’s QLI end date automatically adjusts to 6/30/2026.

Renewal order: If you’re renewing a contract where the cotermination flag is set to True, subscription end dates automatically align with the contract renewal date.

Negative amendments with contract date changes: An initial sale of 100 product licenses with a start date 1/1/2025 and an end date 12/31/2025 are under a cotermed contract. Later, if the user extends the contract end date to 6/1/2026 with a negative amendment of 10 licenses, the end dates of the remaining 90 licenses update to 6/1/2026.

Cotermination Scenarios

Review these examples of how the feature automatically aligns subscription end dates.

Initial Order Sale
For a contract with a start date of 1/1/2025 and an end date of 12/31/2025, an initial sale order created on 2/1/2025 automatically sets the OLI start and end dates to 2/1/2025–12/31/2025. After assetization, the product carries these same subscription dates.
Add-on Sale Order
Adding another product to the same contract on 3/1/2025 via an initial sale order automatically sets the QLI dates to 3/1/2025–12/31/2025 to match the contract end date.
Amendment Order
When a user extends the contract end date to 6/30/2026 and amends a product, the QLI end date automatically adjusts to 6/30/2026.
Renewal Order
If you renew a contract with the cotermination flag set to True, subscription end dates automatically align with the contract renewal date.
Negative Amendments with Contract Date Changes
If a user extends a contract end date to 6/1/2026 while performing a negative amendment for 10 licenses of an original 100-license sale, the end dates for the remaining 90 licenses update to 6/1/2026.

=== ARTICLE: ind.qocal_create_a_pricing_procedure_for_product_discovery.htm ===
---
article_id: ind.qocal_create_a_pricing_procedure_for_product_discovery.htm
title: Create a Procedure to Get List Prices for Product Discovery
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_a_pricing_procedure_for_product_discovery.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_product_discovery_setup.htm
fetched_at: 2026-09-04
---

# Create a Procedure to Get List Prices for Product Discovery

Use the Product Discovery Pricing Procedure template to create a pricing procedure that fits your company's needs. The Pricing Procedure is used to determine and populate pricing information for Product Discovery.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing: Design time user
To use pricing procedures:	Salesforce Pricing: Run time user

For the pricing procedure created by using the template, the ProductDiscoveryContext context definition is set as the context definition by default. If necessary, replace it with your extended ProductDiscoveryContext context definition.

Before you create a pricing procedure for Product discovery, ensure that:

Salesforce Pricing is enabled in your org. See Salesforce Pricing.
You have access to the Price Book Entries V2 decision table.
From the App Launcher, find and select Expression Set Templates.
Click Product Discovery Pricing Procedure.
Click Save As.
To use a custom context definition or change the name of the pricing procedure, complete these steps.
From the App Launcher, find and select Pricing Procedures.
Open your pricing procedure.
Click Edit.
Change the name of the procedure.
Select the context definition.
NOTE The qualification procedure and pricing procedure for product discovery must use the context definition selected on the Product Discovery Settings page.
Save your changes.
To open your pricing procedure in Expression Set Builder, on the Details tab, in the Pricing Procedure Versions section, click the name of the pricing procedure version.
Select the Pricing Setting element and then verify the mapping.
Select the List Price element and then verify the mapping.
IMPORTANT If you enable multicurrency after you create a pricing procedure, add the Currency field, whose API name is CurrencyIsoCode, to the Price Book Entries V2 decision table. Then edit the List Price element in the pricing procedure and map the Currency field to the PricingCurrencyCode attribute of the context definition. Keep in mind that you must deactivate the context definition and pricing procedure before you can edit them.
Click , and enter a rank.
Enter a start date and time that’s later than or the same as the effective from date and time of the context definition.
If necessary, edit the version name and description.
If necessary, configure your pricing procedure to add pricing elements. See Configure Your Pricing Procedure and Pricing Elements.
For each element, click , and ensure that Include in Output is selected.
Save your changes.
Simulate and activate the pricing procedure. See Simulate and Activate Your Pricing Procedure.
SEE ALSO
Configure Your Pricing Procedure

=== ARTICLE: ind.qocal_create_and_map_an_installation_date_field_in_revenue_lifecycle_management.htm ===
---
article_id: ind.qocal_create_and_map_an_installation_date_field_in_revenue_lifecycle_management.htm
title: "Example: Map an Installation Date Field"
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_and_map_an_installation_date_field_in_revenue_lifecycle_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_extend_your_transactions_with_custom_field_support.htm
fetched_at: 2026-09-04
---

# Example: Map an Installation Date Field

Follow these steps to track a custom InstallationDate__c field across the sales lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Add Products

Add the field to the Product and Quote Line Item objects. Then, update the Product Discovery and Sales Transaction context definitions. 

Use Object Manager to add InstallationDate__c to Product and Quote Line Item.
In Context Service, edit your Product Discovery context definition.
Under the CategoryProduct node, create an InstallationDate attribute.
Under the CategoryProduct node, create an InstallationDate tag.
To map InstallationDate to InstallationDate__c, add a Product object mapping in ProductDiscoveryMapping.
In Context Service, edit your Sales Transaction context definition.
Under the QuoteLineItem node, create an InstallationDate attribute.
Under the QuoteLineItem node, create an InstallationDate tag.
To map InstallationDate to InstallationDate__c, add a QuoteLineItem object mapping in QuoteEntitiesMapping.
Create a cross-context attribute mapping in ProductDiscoveryContextMapping that maps ProductDiscoveryContext.Product.InstallationDate to SalesTransactionContext.QuoteLineItem.InstallationDate.
Quote to Order

Add the field to Quote Line Item and Order Item. Then, update the Sales Transaction context definition.

Use Object Manager to add InstallationDate__c to Quote Line Item and Order Item.
In Context Service, edit your Sales Transaction context definition.
Under the SalesTransactionItem node, create an InstallationDate attribute.
Under the SalesTransactionItem node, create an InstallationDate tag.
To map InstallationDate to InstallationDate__c, add a QuoteLineItem object mapping in QuoteEntitiesMapping.
To map InstallationDate to InstallationDate__c, add an OrderItem object mapping in OrderEntitiesMapping.
Set SalesTransaction as the default mapping on the extended SalesTransactionContext and then activate it.
Quote to Contract

Add the field to Quote and Contract. Then, update the Sales Transaction context definition.

Use Object Manager to add InstallationDate__c to Quote and Contract.
In Context Service, edit your Sales Transaction context definition.
Under the SalesTransaction and Contract nodes, create an InstallationDate attribute.
Under the SalesTransaction and Contract nodes, create an InstallationDate tag.
To map InstallationDate to InstallationDate__c, add a Quote object mapping in QuoteToContractSlsTrxnMapping.
To map InstallationDate to InstallationDate__c, add a Contract object mapping in ContractNodeMapping.
To map InstallationDate from SalesTransaction node to InstallationDate on the Contract node, create a mapping in ContractToSalesTxnMapping.
ContractToSalesTxnMapping is an intra-context mapping. Select the Context Definition object next to the mapping as well. Then, map from source (SalesTransaction node) to target (Contract node).
Set SalesTransaction as the default mapping on the extended SalesTransactionContext and then activate it.
Quote Line Item to Contract Item Price

Add the field to Quote Line Item and Contract Item Price. Then, update the Sales Transaction context definition.

Use Object Manager to add InstallationDate__c to QuoteLineItem and ContractItemPrice.
In Context Service, edit your Sales Transaction context definition.
Under the SalesTransactionItem and ContractItemPrice nodes, create an InstallationDate attribute.
Under the SalesTransactionItem and ContractItemPrice nodes, create an InstallationDate tag.
To map InstallationDate to InstallationDate__c, add a QuoteLineItem object mapping in QuoteToContractSlsTrxnMapping.
To map InstallationDate to InstallationDate__c, add a ContractItemPrice object mapping in ContractNodeMapping.
To map InstallationDate from SalesTransactionItem node to InstallationDate on the ContractItemPrice node, create a mapping in ContractToSalesTxnMapping.
ContractToSalesTxnMapping is an intra-context mapping. Select the Context Definition object next to the mapping as well. Then, map from source (SalesTransactionItem node) to target (ContractItemPrice node).
Set SalesTransaction as the default mapping on the extended SalesTransactionContext and then activate it.
Order to Contract

Add the field to Order and Contract. Then, update the Sales Transaction context definition.

Use Object Manager to add InstallationDate__c to Order and Contract.
In Context Service, edit your Sales Transaction context definition.
Under the SalesTransaction and Contract nodes, create an InstallationDate attribute.
Under the SalesTransaction and Contract nodes, create an InstallationDate tag.
To map InstallationDate to InstallationDate__c, add an Order object mapping in OrderToContractSlsTrxnMapping.
To map InstallationDate to InstallationDate__c, add a Contract object mapping in ContractNodeMapping.
To map InstallationDate from SalesTransaction node to InstallationDate on the Contract node create a mapping in ContractToSalesTxnMapping.
ContractToSalesTxnMapping is an intra-context mapping. Select the Context Definition object next to the mapping as well. Then, map from source (SalesTransaction node) to target (Contract node).
Set SalesTransaction as the default mapping on the extended SalesTransactionContext and then activate it.
Order to Asset

Add the field to Order and Asset Action Source. Then, update the Sales Transaction context definition. 

NOTE Custom field mapping from Order to Asset Action Source is only available for Agentforce Revenue Management.
Use Object Manager to add InstallationDate__c to Order Item and Asset Action Source.
In Context Service, edit your Sales Transaction context definition.
Under the SalesTransactionItem and AssetActionSource nodes, create an InstallationDate attribute.
Under the SalesTransactionItem and AssetActionSource nodes, create an InstallationDate tag.
To map InstallationDate to InstallationDate__c, add an OrderItem object mapping in OrderEntitiesMapping.
To map InstallationDate to InstallationDate__c, add an AssetActionSource object mapping in AssetEntitiesMapping.
Set SalesTransaction as the default mapping on the extended SalesTransactionContext and then activate it.
Create a new mapping from the Installation Date in AssetActionSource to InstallationDate in SalesTransactionItem in the Order to Asset inter-context mapping called AssetToSalesTransactionMapping.
Amend, Renew, Cancel

Add the field to Quote Line Item, Order Item and Asset State Period. Then, update the Sales Transaction context definition.

Use Object Manager to add InstallationDate__c to QuoteLineItem, OrderItem and AssetStatePeriod.
In Context Service, edit your Sales Transaction context definition.
Under the SalesTransactionItem and Asset State Period nodes, create an InstallationDate attribute.
Under the SalesTransactionItem and Asset State Period nodes, create an InstallationDate tag.
To map InstallationDate to InstallationDate__c, add a Quote Line Item object mapping in QuoteEntitiesMapping.
To map InstallationDate to InstallationDate__c, add an Order Item object mapping in OrderEntitiesMapping.
To map InstallationDate to InstallationDate__c, add an AssetStatePeriod object mapping in AssetEntitiesMapping.
Set SalesTransaction as the default mapping on the extended SalesTransactionContext and then activate it.
Create a new mapping between the Installation Date in SalesTransactionItem to InstallationDate in AssetStatePeriod in the Amend, Renew, Cancel cross-context mapping called SalesTxnItmToAssetStatePrdMap.
Cross-context mappings don’t have default connected objects. Select the data source Context Definition Objects and the context definition you're using from the dropdown to create mappings between the two entities.
Create a new mapping between the Installation Date in AssetStatePeriod to InstallationDate in SalesTransactionItem in the cross-context mapping called AssetStatePrdToSalesTxnItmMap.

=== ARTICLE: ind.qocal_create_asset_contract_relationship.htm ===
---
article_id: ind.qocal_create_asset_contract_relationship.htm
title: Create Asset Contract Relationships
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_asset_contract_relationship.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_contract_management_essentials.htm
fetched_at: 2026-09-04
---

# Create Asset Contract Relationships

Manually link assets to a contract to track which products-specific customer agreements govern. Creating these relationships helps you to review contract details or open related contracts directly from an asset record.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To create an asset contract relationship:	Sales Operations Rep permission set
 	 
IMPORTANT Verify that the asset and the contract belong to the same account. Make sure that your Salesforce admin has added the Asset Contract Relationship component to your Asset and Contract page layouts.

If an order is linked to a contract with a Revenue Management application usage assignment, the system automatically creates asset contract relationships. This automation occurs when the Create or Update Asset from Order API or Order Product API runs. These automated records default the start and end dates to match the parent asset's lifecycle dates, though the relationship end date can’t exceed the contract's end date.

In the App Launcher, find and select Assets or Contracts.
Select an asset name or contract number.
On the Related tab, locate Asset Contract Relationships, and click New.
Starting from an asset defaults to the Asset field.
Starting from a contract defaults to the Contract field.
Search for and select the corresponding asset or contract.
Select a start date and time.
End Date and Time are optional.
If the parent asset has a lifecycle end date in the past, you can't set an asset contract relationship end date in the past.
Save your changes.

After linking your assets, use the Managed Assets Viewer on the contract record to perform lifecycle actions like amending, renewing, or canceling assets.

SEE ALSO
Add a Related List to an Object
Customize Related Lists

=== ARTICLE: ind.qocal_create_contract_prices_or_discounts_manually.htm ===
---
article_id: ind.qocal_create_contract_prices_or_discounts_manually.htm
title: Manage Contract Prices or Discounts Manually
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_contract_prices_or_discounts_manually.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contract_pricing_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Manage Contract Prices or Discounts Manually

Sales reps manually specify contract prices or discounts when they create a contract. When you create contract item prices and price adjustment schedules, the system applies the negotiated pricing and discounts to future business transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To use Contract Pricing:	Salesforce Pricing Design Time User

Before you create pricing schedules, review these considerations.

Review the start and end dates for products to make sure that they are within the contract's date range.
Select a product selling model that is available in the price book for the product you’re adding.
Manage Pricing Schedule by Using the Contract Pricing Schedule Component

To manage all products and their pricing schedules in one view, use the Contract Pricing Schedule component.

NOTE The Contract Pricing Schedule component is available on contract pages only if an admin adds the component to the pages.
From the App Launcher, find and select Contracts.
Open a contract.
On the Pricing Schedule tab, search for and add a product.
NOTE You can’t add multiple instances of a product with the same product selling model to a contract.
Enter the discount type, discount value, and start date.
Enter any additional details, such as the end date, if needed.
Save your changes.
Click  next to the product and select View.
On the Contract Item Price subtab, enter a product selling model.
Save your changes and close the subtab.
Activate the contract.
Manage Pricing Schedule by Using the Contract Item Prices Related List

To manage the pricing schedule for each product separately, use the Contract Item Prices related list.

From the App Launcher, find and select Contracts.
Open a contract.
In the Contract Item Prices related list, select New.New.
Enter the item, product selling model, and start date.
IMPORTANT Don’t add an item that has the same product selling model, start date, and end date as an existing item in the contract.
To enter pricing not based on volume, enter the discount type and value, or the contract price.
Save your changes.
To use volume-based pricing, create contract item price adjustment tiers.
On the Contract Item Prices related list, click the entry in the Name column.
Select an adjustment method.
Open the Contract Item Price Adjustment Tiers related list.
Click New.
Select a tier type, and then enter the lower bound, upper bound, and tier values.
Save your changes.
Create more tiers.
Similarly, create additional contract item price records.
Activate the contract.

=== ARTICLE: ind.qocal_create_contract_revenue_cloud.htm ===
---
article_id: ind.qocal_create_contract_revenue_cloud.htm
title: Create a Contract and Application Usage Assignment
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_contract_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_contract_management_essentials.htm
fetched_at: 2026-09-04
---

# Create a Contract and Application Usage Assignment

Set up a contract to centralize the management of your customers' assets and establish negotiated pricing by assigning a Revenue Management lifecycle usage tag.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create contracts:	CreateContract API permission set

Before you begin, establish the base contract details—such as the account name and start date—to streamline the record creation process.

From the App Launcher, find and select Contracts.
Click New and enter the contract details—including account name, start date, and status.
Save your work.
Go to the Related tab.
In the Application Usage Assignments section, click New.
Enter RevenueLifecycleManagement for the Application Usage Type.
Save your changes.
Select the Details tab, edit the Status field, and select Activated.

After activating your contract, you can link specific products by creating asset contract relationships or begin negotiating rates by managing contract prices and discounts.

Create asset contract relationships
Manage contract prices and discounts

=== ARTICLE: ind.qocal_create_contracts_from_a_quote_or_order.htm ===
---
article_id: ind.qocal_create_contracts_from_a_quote_or_order.htm
title: Add a New Contract Button
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_contracts_from_a_quote_or_order.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_contract_features.htm
fetched_at: 2026-09-04
---

# Add a New Contract Button

Help your sales reps create contracts directly from finalized records by using the New Contract button on the Quote or Order pages. This configuration streamlines the sales process by automatically copying essential details, such as the account name and start date, from the source record to the New Contract.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To customize page layouts:	Customize Application
IMPORTANT Review your order status before attempting to create a contract. You link contracts only to draft orders. You can’t create a contract for an activated order.
NOTE The New Contract button and the Create Contract button serve different purposes. The New Contract button creates a contract that inherits details from the source record. The Create Contract button is the standard Salesforce action that creates a basic contract without inheriting transaction details. To create contracts with Revenue Management data, use the New Contract button.
In Setup, select Object Manager.
Search for and select Quote or Order.
Go to Page Layouts.
Either create a page layout or select the page layout to modify.
In the Quote Layout or Order Layout section, select Buttons.
Select and drag New Contract from the palette to the Salesforce Mobile and Lightning Experience Actions section.
Save your changes.
Contracts created by using the New Contract button have the Revenue Management application usage tag assigned by default.
SEE ALSO
Customize Standard and Custom Buttons on Page Layouts

=== ARTICLE: ind.qocal_create_contracts_using_a_flow.htm ===
---
article_id: ind.qocal_create_contracts_using_a_flow.htm
title: Automate Contract Creation from Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_contracts_using_a_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_contract_features.htm
fetched_at: 2026-09-04
---

# Automate Contract Creation from Quotes and Orders

Use flows to automatically create contracts from a quote or an order. Create a flow that invokes the Create Contracts from Quote flow action when Revenue Management quotes are changed to Accepted status. You can also add more conditions or customize the flow to perform other actions. Create contracts from orders by using a similar flow.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To open, edit, or create a flow in Flow Builder:	Manage Flow
From Setup, in the Quick Find box, enter Flows, and then select Flows.
Click New Flow.
Select Start from Scratch and click Next.
Select Record-Triggered Flow and click Create.
Select Quote or Order as the object.
Select A record is updated for the trigger configuration.
In the Set Entry Conditions section, specify these values.
Condition Requirements: All Conditions Are Met (AND)
Field: Status
Operator: Equals
Value: Accepted
Save your changes, and name your flow.
Click , search for and select Action.
In New Action, filter by Category, and select Revenue Cloud.
Click the Action search option and select Create Contract.
Add the Label and Source ID from the previous action, either Quote or Order object ({!$Record__Prior.Id}).
Save your changes.

After you complete the flow setup, add the Contract field to the Quote Details Page and the Order Details Page layouts to help users to view the linked contract record.

SEE ALSO
Automate Asset Creation from Orders by Using Flows

=== ARTICLE: ind.qocal_create_custom_fields.htm ===
---
article_id: ind.qocal_create_custom_fields.htm
title: Create Custom Fields and Add Custom Attributes
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_custom_fields.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_extend_your_transactions_with_custom_field_support.htm
fetched_at: 2026-09-04
---

# Create Custom Fields and Add Custom Attributes

After extending the definition, add the actual fields to Salesforce objects and the corresponding attributes to the context.

Create custom fields: Use Object Manager to add fields to relevant sales objects (for example, Quote, Order, Product).
Add attributes: Add corresponding attributes and tag names to the extended context definition.
Map attributes: Map these attributes to the custom fields on the entity.

=== ARTICLE: ind.qocal_create_documents_from_quotes.htm ===
---
article_id: ind.qocal_create_documents_from_quotes.htm
title: Create a Document from a Quote
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_documents_from_quotes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_document_builder_for_quotes.htm
fetched_at: 2026-09-04
---

# Create a Document from a Quote

Create and share a PDF document directly from the quote page.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To view quotes:	Read on quotes
NOTE Quote documents show all root products. They show only the child products whose Quote Visibility field isn't selected, is set to Always, or is set to Quote Document Only. See Manage Product Relationships in Revenue Management.
On the quote record page, click , and then select Create PDF.
Click Save to Quote or Save and Email Quote.
Saved PDF documents are added to the Quote PDFs related list. You can use the Email PDF action in the related list to share the documents.
NOTE Quote PDFs generated by using Create PDF use the org default quote document template. To change the template used for quote PDFs, create or update a quote document template in Document Builder and assign it as the default. Assigning a different template as the default overrides the previously assigned template. Only one default quote document template can be active per org at a time.

For instructions on creating and managing quote document templates, see Create a Quote Document Template.

=== ARTICLE: ind.qocal_create_object_state_definition.htm ===
---
article_id: ind.qocal_create_object_state_definition.htm
title: Implement an Object State Definition for Order Lifecycle Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_object_state_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_order_lifecycle_management_using_object_state_definitions.htm
fetched_at: 2026-09-04
---

# Implement an Object State Definition for Order Lifecycle Management

Establish the foundation for managing an order through its lifecycle by defining object state values and valid transitions. Object state definitions help you to control the progression of orders and establish a clear fulfillment process within Revenue Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create object state definitions for orders:	
View on orders
Create on object state definitions

Configure the state model for orders by selecting the reference object and specifying the application context.

From the App Launcher, find and select Object State Definition.
Enter a name for the definition, for example, Order Lifecycle Management.
Select Order for the reference object.
Select Status for the Reference Field.
Enter RevenueLifecycleManagement for the Application Usage Type.
Enter information for Additional Field and Additional Field Value to apply this definition only to a subset of Revenue Management order records.
For example, create two object state definitions to use different lifecycles for B2B and B2C orders.
For the B2B definition, set Additional Field to Channel__c and Additional Field Value to B2B.
For the B2C definition, set Additional Field to Channel__c and Additional Field Value to B2C.
Save your changes.

=== ARTICLE: ind.qocal_create_object_state_transitions.htm ===
---
article_id: ind.qocal_create_object_state_transitions.htm
title: Create Object State Transitions for Order Lifecycle Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_object_state_transitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_order_lifecycle_management_using_object_state_definitions.htm
fetched_at: 2026-09-04
---

# Create Object State Transitions for Order Lifecycle Management

Define valid status changes between states to control how an order moves through its lifecycle. For example, create a transition that moves an order from Draft to Activated.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create object state values:	
View on orders and object state definitions
Create on object state transitions

Specify the "from" and "to" states to establish authorized paths for order status changes.

From the App Launcher, find and select Object State Definitions.
Click the object state definition that requires transitions.
Click Related.
In the Object State Transitions section, click New.
Enter a name for the transition.
Select the "from" and "to" states for the transition.
Save your changes.
Repeat this step for each status transition that you want to add.

=== ARTICLE: ind.qocal_create_object_state_values.htm ===
---
article_id: ind.qocal_create_object_state_values.htm
title: Create Object State Values for Order Lifecycle Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_object_state_values.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_order_lifecycle_management_using_object_state_definitions.htm
fetched_at: 2026-09-04
---

# Create Object State Values for Order Lifecycle Management

Define the possible states for the order object to establish the stages of your order lifecycle. Ensure the name of your object state values exactly match the API names of your order status picklist values to maintain data integrity.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create object state values:	
View on orders and object state definitions
Create on object state values

By default, the status field of the order object includes two picklist values: Draft and Activated. Before you create other object state values, create a picklist value for each custom state and sort them in the required sequence. To learn how to use picklists, see Add or Edit Picklist Values.

Add specific status values to your object state definition to represent each stage of the order process.

From the App Launcher, find and select Object State Definitions.
Click the object state definition that you want to add states to.
Click Related.
In the Object State Values section, click New.
Enter the API name of an order status picklist value.
Save your changes.
Repeat this step for each status that you want to add.
NOTE The Reference Record Access Type and Reference Record Layout Field Value fields aren’t applicable for order object state values.

=== ARTICLE: ind.qocal_create_orders.htm ===
---
article_id: ind.qocal_create_orders.htm
title: Create an Order
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_orders_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Create an Order

Skip the quotation and approval phases for straightforward transactions by generating an order record directly. This process enables you to manage sales that require immediate fulfillment without preliminary quote documentation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create orders:	PlaceOrder API permission set
On the Orders tab, click New Order.
Enter the order details such as account name, order start date, status, and any other necessary information.
Save your changes.
Select the Related tab.
In the Application Usage Assignments section, click New.
For Application Usage Type, enter RevenueLifecycleManagement.
Save your changes.
Click Lines.
Browse and add products to the order.
The added products appear in the Order Products section.
SEE ALSO
Revenue Cloud Developer Guide: Place Order (POST)
Create and Submit an Order

=== ARTICLE: ind.qocal_create_orders_from_a_quote.htm ===
---
article_id: ind.qocal_create_orders_from_a_quote.htm
title: Create an Order from a Quote
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_orders_from_a_quote.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_order_features.htm
fetched_at: 2026-09-04
---

# Create an Order from a Quote

Convert an accepted quote into an order with one click to synchronize product, quantity, pricing, and tax data. By using this process, the order record automatically inherits these details directly from the quote record.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To create orders from quotes:	Create Orders from Quotes

The order record copies product, quantity, pricing, and tax information directly from the quote record. If you make any tax-impacting changes to the order record, Salesforce recalculates the tax for the order.

IMPORTANT Revenue Management doesn't support creating orders from future-dated contracts. The system defaults the Order Start Date to the current date. If the contract has a future start date, this date mismatch causes an error during order creation.
Open the quote record.
Click Create Order.
Monitor your notifications to confirm the status of the order creation.

=== ARTICLE: ind.qocal_create_quote_document_template.htm ===
---
article_id: ind.qocal_create_quote_document_template.htm
title: Create a Quote Document Template
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_quote_document_template.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_document_builder_for_quotes.htm
fetched_at: 2026-09-04
---

# Create a Quote Document Template

Use the default quote template or a blank template to create professional quote document templates. Document Builder standard components capture all relevant quote details within the template.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To create a quote document template:	Document Builder User
From Setup, in the Quick Find box, enter Document Builder, and then select Document Builder.
Click New Template.
Give your document template a label.
Select the Quote object from the dropdown.
Select a blank template or a default quote template.
The default quote template contains account and contact details, quote line items, and acceptance details.
Build your template by using the standard components.
Save and activate your finished template.

Use standard components to populate your quote document templates with specific data from your quote.

Company Details: Captures the company details of your customer in the quote document.
Quote Line Items: Shows a table containing quantity and price details for quote line items.
Quote line items organize into a hierarchy within the table.Salesforce prevents customization of the fields shown in the quote line items table.
Grid: Provides structural layout for document content.
Image and Image Gallery: Inserts visual elements into the template.
Page Numbers: Adds pagination to the document.
Related Record Table: Shows data from records related to the quote.
Rich Text: Helps with custom formatted text blocks.

=== ARTICLE: ind.qocal_create_quote_for_usage_based_products.htm ===
---
article_id: ind.qocal_create_quote_for_usage_based_products.htm
title: Build a Quote for Usage-Based Products
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_quote_for_usage_based_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling.htm
fetched_at: 2026-09-04
---

# Build a Quote for Usage-Based Products

Create quotes for usage-based products that meet your customer’s needs. Review the resources included with the product, including the granted quantity and rates.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create quotes:	Create on Quotes
From the App Launcher, find and select Quotes.
Select a quote.
Click Browse Catalogs.
Select a pricebook, and save your changes.
Select a product, and click Add.
To add a product with a future date, add the product to the quote line item by using the Related tab. Before refreshing the price, edit the quote line item record and update the start date to the required future date. The related grants and policy records are created based on the specified start date.
The product is added to the quote as a quote line item.
On the quote line item for the product that you added, click Manage Usage Resources.
Under Line Item Details, select the binding type.
	
Self	Binds the line item with the same product that the line item is added to. This option is available only for Anchor products.
Target	Binds the line item with a product, account, contract, or custom object. When you select a target, you must select a binding target type and the binding target that the line item is to be bound to. This option is available only when the product in the line item is of the usage model type Anchor or Pack.
NOTE When you create a quote by converting an opportunity, the quote details are automatically populated with the account name. If you add a product as a line item to this quote and attempt to bind the line item product to the same account on the Manage Usage Resources page, the account name doesn't populate automatically as the binding target. You must manually select the account name as the binding target.
If you select Binding Type as the target, then select the binding target type.
	
Product	

Binds the usage to a specific product. When you select this binding type, you can either set Binding Scope to the existing asset or line item. With this option, you have the flexibility to bind the current line item to another line item, which is part of the same quote or order.


Custom	Binds the usage to a custom object. This is for use cases where you want to track the usage against a unique object that isn't a standard Salesforce object.
Account	Binds the usage to a specific account, which is useful for tracking all usage associated with an account.
Contract	Binds the usage to a specific contract that makes sure that usage is billed according to the terms of a specific agreement.
Review the usage resources that are included in the product and their rates.

If you have trouble viewing rates for usage resources, check that your rating discovery procedure includes the latest elements. If your procedure doesn't have the latest elements, clone the Default Rating Discovery Procedure and reapply your customizations. For more information, see Clone the Default Rating Discovery Procedure.

If necessary, to update and apply the negotiated rates, select Override Rate.
To view details of a specific usage resource, click the usage resource.
A pane on the right side shows the details of the rate cards, tier rates, and policies, such as rollover, refresh, and aggregation policies, governing that resource.
Save your changes.
EXAMPLE Let’s say you’re a salesperson and you've successfully negotiated a special deal with Tech Innovators. Tech Innovators, a leading company in data-driven solutions, uses the Acme suite of products. The final quote reflects these key points:
A discount on your Acme Analytics API, which is a token-rated anchor product. The customer wants more calls at a lower rate.
A special discount on their Acme Cloud Storage, which is a token commitment product. They’ve agreed to a monthly token commitment in exchange for a percentage discount.
A per-unit rate for your Data Processing Suite, which normally uses tiered pricing. The customer wants a simple, consistent price, no matter the volume.

Here’s how you use the Manage Usage Resources interface to modify the negotiated rates.

For Acme Analytics API—on Manage Usage Resources page, in the Usage Resources table, update the grant quantity from 10,000 to 15,000 tokens and the applicable rate from $0.50 to $0.45 per token.
For Acme Cloud Storage—on Manage Usage Resources page, in the Commitment Rate column, update the value to 10%.
For Data Processing Suite—on the Manage Usage Resources page, under Resources and Grants, select Override Rate. Then, enter your negotiated per-unit price of $7.50 per GB.
SEE ALSO
Quotes in Revenue Cloud
Amending, Renewing, and Canceling Assets
Considerations for Managing Usage Selling Assets
View Applicable Rates for Individual Assets

=== ARTICLE: ind.qocal_create_quotes.htm ===
---
article_id: ind.qocal_create_quotes.htm
title: Create a Quote
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_quotes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_management_lifecyle.htm
fetched_at: 2026-09-04
---

# Create a Quote

Discover and price products for your customers by creating quotes directly in Revenue Cloud. These records help you organize product selections and apply pricing logic before finalizing a transaction.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To create quotes:	Manage Revenue Management

Generate a new quote record from an opportunity or the main Quotes tab to begin the pricing process.

Start the quote creation process.
From an opportunity record, go to the Quotes section, and select New Quote.
From the Quotes tab, click New Quote.
Enter the quote details, including the name, account, opportunity, and status.
Optionally, select any custom fields that your Salesforce admin enabled.
Save your changes.

=== ARTICLE: ind.qocal_create_ramp_deal_for_groups_for_usage_products.htm ===
---
article_id: ind.qocal_create_ramp_deal_for_groups_for_usage_products.htm
title: Ramp Deals for Usage Products
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_create_ramp_deal_for_groups_for_usage_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm
fetched_at: 2026-09-04
---

# Ramp Deals for Usage Products

Use ramp deals for groups for usage products to break down a long-term deal into smaller time-based segments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.

Look at DataFlow, a software company that sells a data transfer service with tiered pricing based on usage. They want to offer a promotional deal to a new customer, GlobalCorp, for a three-year contract.

Set Up Subscription: GlobalCorp signs a three-year subscription. The sales rep sets up a ramp deal with three annual group segments.
Group Products: The rep creates a Data Transfer Services group containing usage products like inbound and outbound data transfer.
Define Ramp Schedule: The rep defines the ramp schedule for the group, with each segment lasting one year.
Ramp 1 (Year 1): To attract GlobalCorp, DataFlow offers a 20% discount on all data transfer usage for the first year.
Ramp 2 (Year 2): The discount is reduced to 10% for the second year.
Ramp 3 (Year 3): Rating is done on the standard rate, and DataFlow includes a loyalty grant of 100 GB of data transfer at no additional cost, to encourage renewal.
Billing: As GlobalCorp uses the service, usage management automatically applies the correct pricing for each year.

When you add a usage product to a ramp deal, the initial addition copies rates to all segments. After that, manage usage of products in ramp segments as follows.

ACTION	DESCRIPTION	CONSIDERATIONS
Rate Changes	Modify the rate of a usage product within a segment.	The initial product addition copies rates to all segments. However, subsequent modifications to a rate in a segment apply only to that specific segment—rate changes don't carry to other segments.
Binding Type Changes	Change the binding type per segment.	Changes to the binding type propagate across all segments with the same ramp identifier, because binding types are consistent for the entire deal. This propagation happens both forward and backward through the segments.
Grant Changes	Modify the grant quantity for a usage product within a segment.	The grant quantity can be changed on a per-segment basis.

=== ARTICLE: ind.qocal_cumulative_quantity_contract_pricing.htm ===
---
article_id: ind.qocal_cumulative_quantity_contract_pricing.htm
title: Calculate Cumulative Quantity Pricing for Contractual Discounts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_cumulative_quantity_contract_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contract_pricing_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Calculate Cumulative Quantity Pricing for Contractual Discounts

Motivate larger purchases by aggregating product quantities across transactions and active assets to apply accurate negotiated price or discount tiers. This approach combines quantities from quote lines with existing active assets to make sure that the system applies the correct tier based on total purchase volume over time.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To use cumulative quantity pricing:	Sales Pricing Design Time User permission

Cumulative pricing is designed to work with contract-based volume and tier pricing methods.

IMPORTANT For active orders or assets, cumulative pricing requires Contract Pricing Volume or Tiered Discounts. However, you can use it independently when simulating a pricing procedure.
From the App Launcher, find and select Pricing Procedures.
Select Default Pricing Procedure.
If you’ve created a custom pricing procedure, select that procedure.
Select the Volume Discount or Tier Discount element.
Select Use Cumulative Pricing.
Map the correct input and output variables in your pricing procedure.
Save your changes and activate the pricing procedure. Alternatively, if you want step-by-step instructions on creating a custom pricing procedure to perform cumulative pricing calculations, see Calculate Volume or Tiered Discounts With Cumulative Pricing.
Update your Contract page layout with the Pricing Schedule component to view and negotiate contractual pricing..
In Setup, search for and select the Contract object in the Object Manager.
Select Lightning Record Pages, and then the Contract Record Page.
Select Edit, then select Tabs on the page layout of the Lightning App Builder.
Select Add Tab, select the new tab, and select the Pricing Schedule tab label.
Click Done, then select the new Pricing Schedule tab on the Lightning App Builder.
Drag the Contract Pricing Schedule component from the Standard Components section to the new tab and save.
Return to the Contract page and select the Pricing Schedule tab.
Create contract pricing for a product by using the Pricing Schedule.
Create contract-based volume tiers for a product.
Select New or view existing Product Pricing Tiers.
Select Edit Tiers under Adjustment Value to change tiers.
Activate the contract and refresh the Contract Pricing decision tables.
On the Contract Details tab, set the Aggregation Strategy field to Cumulative. If you don’t set this field, the system prices each line item individually without cumulative quantity.
Create a quote.
Add the contract number to the Pricing Contract field on the quote to apply contract pricing.
Add at least two quote line items for the same product with a matching product selling model (PSM) and unit of measure (UOM).
The system aggregates the total purchase quantity across matching quote lines and applies the tiers cumulatively. The quote’s Net Unit Price updates to the aggregated cumulative tier price.

When you set the Aggregation Strategy to Cumulative, the transaction system uses these rules to aggregate quantity:

Aggregates quantities based on transaction line items with a matching product, PSM, and UOM.
Bundle lines that meet the same matching criteria.
Active assets on the account that meet the same matching criteria.

=== ARTICLE: ind.qocal_customize_page_layouts_for_quote_and_order_capture.htm ===
---
article_id: ind.qocal_customize_page_layouts_for_quote_and_order_capture.htm
title: Required Fields and Related Lists for Transaction Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_customize_page_layouts_for_quote_and_order_capture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_customize_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Required Fields and Related Lists for Transaction Management

Configure your page layouts by adding the fields and related lists necessary for your users to manage revenue transactions effectively. These additions make sure that sales reps can access critical quotes and order data directly from the records they use most.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Page Layout Configurations

Customize your page layouts to include the following related lists and fields.

Opportunity Page Layout: Add this related list to help users track associated pricing documents.
Quotes
Order Page Layout: Add these related lists to provide visibility into lifecycle actions and usage.
Order Actions
Application Usage Assignments
Order Product Relationships
Order Product Page Layout: Add these related lists and fields to detail the specific terms and pricing of each order item.
ELEMENT TYPE	ITEMS TO ADD
Related Lists	Order Product Details, Order Product Attributes
Fields	Product Selling Model, Order Action, Start Date, End Date, Proration Policy, Period Boundary, Period Boundary Day, Period Boundary Start Month, Start Quantity, End Quantity, Pricing Term Count, Net Unit Price, Product Subtotal, Validation Result

Check out these additional resources.

Add a Related List to an Object
Customize Page Layouts with the Enhanced Page Layout Editor
SEE ALSO
Customize Related Lists

=== ARTICLE: ind.qocal_customize_pricing_for_different_types_of_transactions.htm ===
---
article_id: ind.qocal_customize_pricing_for_different_types_of_transactions.htm
title: Pricing Customization for Different Transaction Types
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_customize_pricing_for_different_types_of_transactions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_common_capabilities.htm
fetched_at: 2026-09-04
---

# Pricing Customization for Different Transaction Types

Link custom fields to different pricing procedures to show unique prices based on the transaction type. For example, B2B customers receive volume discounts while B2C customers see standard pricing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create pricing procedures:	Salesforce Pricing Design Time User
To create Sales Transaction Type records:	Manage Revenue Management
To create custom fields:	Customize Application
To add field-level security to profiles or permission sets:	Manage Profiles and Permission Sets
To create Flows:	Manage Flow
Before You Begin

Before you begin, create a pricing procedure and custom field for your use case. Also, create a custom field on the transaction object that your sales reps can select to trigger the pricing procedure.

Create a pricing procedure.
See Configure Your Pricing Procedure
Create a custom checkbox field and add it to the transaction object page layouts.
See Create Custom Fields.
Create a Sales Transaction Type
From the App Launcher, find and select Sales Transaction Types.
Click New.
Enter a name for your sales transaction type.
For example, B2C_Sales_Transaction
Select you new pricing procedure.
Save your changes.
Note the ID of the sales transaction type from the URL.
For example, if your URL is https://<your-instance>.force.com/lightning/r/SalesTransactionType/1ChDU000000000L0AQ/view, the ID is 1ChDU000000000L0AQ
Link the Custom Field and Sales Transaction Type With a Flow

Trigger the pricing procedure when sales reps select the custom field using a Flow.

From Setup, in the Quick Find box, enter Flows, and then select Flows.
Click New Flow.
Select Start from Scratch and click Next.
Select Record-Triggered Flow and click Create.
Select an object. For example, you can select Quote or Order.
Select A record is created or updated for the trigger configuration.
In the Set Entry Conditions section, specify these details.
Condition Requirements: All Conditions Are Met (AND)
Field: Select the custom field that you’ve created. For example, B2C_Sales_Transaction
Operator: Equals
Value: True
Select Only when a record is updated to meet the condition requirements for the run frequency.
Select Fast Field Updates.
Add an Update Records element and map the Sales Transaction TypeID to the ID you noted earlier.
Give your flow a name and activate it.

=== ARTICLE: ind.qocal_customize_quote_and_order_capture.htm ===
---
article_id: ind.qocal_customize_quote_and_order_capture.htm
title: Personalize the Transaction Management Experience
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_customize_quote_and_order_capture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_user_experience_and_customization.htm
fetched_at: 2026-09-04
---

# Personalize the Transaction Management Experience

Deliver an intuitive sales and partner experience by customizing Transaction Management visual elements and actions.

Understanding these customization options helps you align the user interface with specific business workflows before you begin configuration tasks. Customize the Transaction Line Editor to show relevant data fields and action buttons based on the needs of your sales operations teams.

Customize Transaction Summary
The Transaction Summary component shows a snapshot of key financial details from quote and order records. It provides a scannable overview of pricing, discounts, and total amounts to help users verify transaction accuracy before processing.
Configure Header-Level Action Buttons in Sales Transaction Line Editor
To provide an intuitive experience for sales reps, you can customize the placement and sequence of action buttons in Sales Transaction Line Editor (STLE). Choose which actions appear as standalone buttons, button groups, or menu items in a dropdown list.
Required Fields and Related Lists for Transaction Management
Configure your page layouts by adding the fields and related lists necessary for your users to manage revenue transactions effectively. These additions make sure that sales reps can access critical quotes and order data directly from the records they use most.

=== ARTICLE: ind.qocal_customize_transaction_line_editor.htm ===
---
article_id: ind.qocal_customize_transaction_line_editor.htm
title: Add and Customize the Transaction Line Editor or Sales Transaction Line Editor
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_customize_transaction_line_editor.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Add and Customize the Transaction Line Editor or Sales Transaction Line Editor

To help sales reps to view and manage quote and order line items efficiently, add the Transaction Line Editor or Sales Transaction Line Editor (STLE) to the page layout and customize the fields that the editor shows. We strongly recommend using STLE because its streamlined, single-grid layout improves performance at scale and provides access to the latest capabilities in Transaction Management. The Transaction Line Editor remains available, but it’s no longer being enhanced.

The Sales Transaction Line Editor helps:

Organize quotes and orders by using nested groups and group ramps.
Perform bulk actions such as editing fields, updating discounts, or deleting selected line items or groups.
Filter and sort items across groups.
View and edit group details in the side panel.

The line editors show as Quote Line Items on the Quote page and as Order Products on the Order page. To access this component, users need an Revenue Management permission set, such as Assetize Order or Price and Tax Calculation for Quoting.

The line editors use the Transaction Line Progress Indicator component to:

Show the progress of line item additions and changes.
Show informational and error messages.
Support the browse catalogs functionality.

After you add a line editor to the page layout, add the Transaction Line Progress Indicator component. For more context about the Transaction Line Progress Indicator, see Transaction Line Progress Indicator Component.

Add the component to a quote or order page.
From Setup, in the Quick Find box, enter Lightning App Builder, and then select Lightning App Builder.
For Quote Record Page, click Edit.
Click the Tabs component.
NOTE We recommend that you add the Transaction Line Editor or Sales Transaction Line Editor to the default tab on quote or order record pages. This addition makes sure that the editor loads along with the page, rather than only when you switch to another tab.
In the Tabs component's Page panel, click Add Tab.
In the Page panel, click the tab item that you added, and then select Lines as the tab label.
On the canvas, click the Lines tab.
Drag the Transaction Line Editor or Sales Transaction Line Editor component to the tab.
Drag the Transaction Line Progress Indicator component above the line editor.
Customize the line editor component.
Highlight the component.
Under Display Columns, click Select....
Select the columns (fields) that you want to show on the line editor. See Select Fields for the Line Editor.
If needed, select the Show product quick add and the Show side panel when users click a record link options.
To show fields on the side panel, move the fields to the Selected section and arrange them in your preferred order.

The side panel shows up to 200 product attributes for each quote line, sorted alphabetically by their definition name. It shows only attributes that aren't marked hidden in Product Catalog Management. See Working with Product Attribute Fields.

If you're using STLE and ramp deals for groups, select fields to display in the View Ramp Details and Edit Ramp Schedule window.
Save your changes.
Activate the page and select a form factor.

You can further customize the page to set the placement and sequence of the action buttons. See Configure the Placement and Sequence of Action Buttons in Line Editor.

Select Fields for the Line Editor
Select line-level fields, group fields, and related record fields in the Display Columns to manage which fields appear in the line editor.
Adjustment Type Column
The Adjustment Type column merges multiple adjustment fields into a single column so that sales reps can make pricing adjustments more efficiently.
Turn On Auto-Refresh for the Sales Transaction Line Editor and Transaction Summary
Keep your sales reps focused on closing deals instead of reloading pages. To turn on auto-refresh for Sales Transaction Line Editor (STLE) and Transaction Summary, set up Change Data Capture for the quote and order objects. The auto-refresh feature captures changes made outside STLE, including record pages, flows, Apex triggers, and Agentforce actions. After it's turned on, sales reps see accurate line items right away, helping them work with confidence and complete quotes and orders faster.

=== ARTICLE: ind.qocal_customize_transaction_summary.htm ===
---
article_id: ind.qocal_customize_transaction_summary.htm
title: Customize Transaction Summary
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_customize_transaction_summary.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_customize_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Customize Transaction Summary

The Transaction Summary component shows a snapshot of key financial details from quote and order records. It provides a scannable overview of pricing, discounts, and total amounts to help users verify transaction accuracy before processing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To customize the Transaction Summary:	Customize Application
To view Transaction Summary on the Orders page:	

Field-level security to these Order fields:

TotalRoundedLineAmount (Read-only)
DiscountPercent (Read-only)
TotalAmount (Read-only)
NOTE Use a custom permission set to provide read access for users who lack the Place Order API permission but require access to other order fields.
Open any quote or order record page.
From Setup, select Edit Page.
Select the Transaction Summary component to view its properties.
Select Expanded by Default to show all summary details automatically when the page loads.
Move the required fields to the Selected section for both the footer and body areas.
Drag fields within the list to arrange them in your preferred order.
Save your changes and activate the page.

Review these requirements to ensure that your components appear and function correctly in your quote document templates.

Vertical Positioning: Place the Transaction Summary component in the same tab as the Sales Transaction Line Editor or the Transaction Line Editor. Its vertical position within that tab doesn't affect functionality.
Rendering Behavior: The component always renders at the bottom of the page in the live view, regardless of where you drop it in the Lightning App Builder.
Field Limitations: Avoid adding fields with the Address data type, such as Ship To or Bill To, as the component doesn’t support them.
Component Selection: If other components hide the component box in the Lightning App Builder, confirm your selection by checking for Transaction Summary in the properties panel.

=== ARTICLE: ind.qocal_differences_between_calculation_status_field_and_validation_result_field.htm ===
---
article_id: ind.qocal_differences_between_calculation_status_field_and_validation_result_field.htm
title: Differences Between Calculation Status Field and Validation Result Field
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_differences_between_calculation_status_field_and_validation_result_field.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_sales_transactions_rev_cloud.htm
fetched_at: 2026-09-04
---

# Differences Between Calculation Status Field and Validation Result Field

Map the Calculation Status field and Validation Result field to specific tasks within your pricing and orchestration engine to maintain an effective transaction lifecycle and avoid inaccurate business decisions. While both fields track transaction states, each serves a unique purpose based on your business requirements.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

Use the Calculation Status field exclusively to monitor the real-time progress of execution tasks. For example, use it to see if pricing or tax calculation is in progress for a specific quote. Because these values are often imprecise, avoid using them as a definitive state machine to block business logic such as order activation or billing.

Use the Validation Result field as the primary indicator to determine if a transaction is valid and ready to advance. This field provides granular control over the transaction lifecycle by preventing lifecycle advancement. For example, if a transaction is marked as complete, this field prevents the quote from becoming an order.

This example illustrates some best practices for an effective integration of the pricing and order orchestration for a transaction.

Imagine a user performs a corrective action on pricing fields and configures the transaction process to skip pricing. Follow these validation standards to integrate the pricing and order orchestration effectively.

Set validation status: Explicitly update the Validation Result to TransactionIncomplete if a skipped action renders the quote invalid.
Automate the process: Automate the setting of these results through integrated quote and order systems rather than relying on manual user input.
Avoid ambiguity: Don’t rely on null values, because they fail to differentiate between a successful action and no action.

Include all system validations to calculate the final transaction state. Use this table to compare how these fields determine if an order is ready for activation.

FIELD NAME	RECOMMENDED USE	BUSINESS LOGIC IMPACT
Calculation Status	Progress monitoring only. For example, Pricing in progress.	Don’t use this status to block lifecycle steps, such as billing or assetization.
Validation Result	Determining transaction validity. For example, TransactionIncomplete.	Use this field to prevent lifecycle advancement for invalid quotes and orders.

In summary, use the Calculation Status field to view background task progress and the Validation Result field to determine if a transaction is complete and valid for the next stage.

If an error occurs during transaction processing, the Calculation Status update may not complete, which can leave the transaction in the Saving state. In this state, users can't edit the transaction in the Sales Transaction Line Editor. To retry the transaction, use the Place Sales Transaction (PST) API through Apex, Flow, or Connect REST API endpoints.

IMPORTANT We recommend that you don't manually update the Calculation Status field unless no other recovery option is available. Manual updates can introduce inconsistencies and lead to unexpected behavior in downstream processes such as quote-to-order conversion or order assetization.

To manually update the Calculation Status field, create a permission set that includes the Edit Calculation Status on Quote and Order system permission. Before updating the Calculation Status field on the quote or order, assign the permission set to the user.

=== ARTICLE: ind.qocal_discover_and_configure_products.htm ===
---
article_id: ind.qocal_discover_and_configure_products.htm
title: Discover and Configure Products for Transactions
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_discover_and_configure_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_sales_transactions_rev_cloud.htm
fetched_at: 2026-09-04
---

# Discover and Configure Products for Transactions

Browse catalogs, view product lists, configure products, and add items to your quotes or orders.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To view catalogs:	Read on catalogs
To view products:	Read on products
To add products to quotes:	Edit on quotes
To add products to orders:	Edit on orders
To browse for products:	
Use Product Discovery
Manage Revenue Management
Run Flows

Product Discovery provides a centralized workspace to find and filter products based on specific criteria. Use this page to select buying options, configure bundles, and select quantities before adding them to a transaction.

IMPORTANT Revenue Management doesn’t support adding or editing products via the standard buttons in the Quote Line Items or Order Products related lists.

Find and select products from a catalog to populate your quote or order. Use the Product Discovery workspace to complete these selections.

Open a quote, order, or account record.
Click Browse Catalogs on a quote or order page, or click View Catalogs on an account page.
Select a catalog and click Next.
Filter the product list to find specific items, then select your quantities.
Select buying options or configuration settings.
Click Show buying options (1) if product selling models exist for the item.
Click Configure (2) for configurable products to set up specific attributes or bundles.
Use the Add or Configure button within the buying options window if you change the default selection.
Click Add (4) or Add Selection to Quote (5) to move products to the New Quote Line Items list (3). This is also known as the preview component. If you save your changes after configuring a product, the system creates the quote line item even if it doesn't appear in the preview component.
Click Add Items to Quote (6) to add your selections as unsaved transient lines to the transaction.
Save the quote or order before you attempt to edit the lines.
For products that use derived pricing, the system calculates the final price only after you add the product to the transaction.

Review eligibility requirements, direct saving options, and derived pricing behavior to ensure accurate product selection and transaction totals.

Save your quote on the Browse Catalogs page to save products directly if the quote page lacks the Transaction Line Editor component.
Select the All Products checkbox to add only the eligible products from the shown list.
The list price is 0 for derived pricing products until the system calculates the final price after you add the item to the transaction.

=== ARTICLE: ind.qocal_document_builder_for_quotes.htm ===
---
article_id: ind.qocal_document_builder_for_quotes.htm
title: Document Builder for Quotes
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_document_builder_for_quotes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_features.htm
fetched_at: 2026-09-04
---

# Document Builder for Quotes

Document Builder provides a professional document generation solution to create formatted documents that meet business and customer requirements. Adopting Document Builder helps you to build professional, customized, and dynamic quote documents.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

The Template Builder and associated tools offer these capabilities for your quote generation process.

Customize standard quote document templates to align with company business practices.
Drag standard components into the builder, including Company Details, Grid, Image, and so on.
Show relevant information about a quote and its related records by using the Field panel.
Use Document Builder to share details of performed work in real-time.
Preview, generate, and email PDF documents to customers within seconds.
Select between Document Builder or the existing quote PDF generation feature when you turn on the Document Builder feature in an org.
Create a Document from a Quote
Create and share a PDF document directly from the quote page.
Set Up Document Builder for Quotes
Turn on Document Builder to begin creating customized, dynamic quote templates that align with your business practices.
Create a Quote Document Template
Use the default quote template or a blank template to create professional quote document templates. Document Builder standard components capture all relevant quote details within the template.

=== ARTICLE: ind.qocal_early_renewal_of_ramped_assets.htm ===
---
article_id: ind.qocal_early_renewal_of_ramped_assets.htm
title: Early Renewal of Ramped Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_early_renewal_of_ramped_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm
fetched_at: 2026-09-04
---

# Early Renewal of Ramped Assets

You can renew one or more ramped assets before their scheduled end date to lock in pricing, consolidate contracts, or restructure a large upsell. Early renewal generates cancellation credits for the uncharged portion of the terminated segments and produces a new system-generated ramp structure on the renewal quote.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To renew group ramp assets early:	

InitiateRenewal API permission set

AND

Sales rep persona permissions

You can only early renew term-defined products or term-defined bundles in which all child products are also term-defined. You can renew usage-based ramped assets early with the Revenue Cloud Advanced license. If usage-based ramp segments have expired, you can renew them as non-ramp segments but not as continuous ramp segments. To renew nonramped usage-based products, see Renew Assets with the Managed Asset Viewer.

IMPORTANT Early renewal for usage-based ramped assets isn’t supported for orgs with the Revenue Cloud Billing license.
Before You Begin
In Setup, find and select Revenue Settings.
Turn on Ramp Deals for Groups in Quotes and Orders.
The auto-generated ramp schedule structure on the quote depends on the Multiple Ramp Schedules Per Transaction setting. Turn on the setting to create a two-level nested structure. When it's turned off, the process creates a single-level list of segments.
To set up ramp deals, add the Managed Asset Viewer component to your preferred page layouts, such as the Account page layout.
Add the Assets related list to the Account page for the Managed Assets list to appear.

To perform early renewal of ramped assets:

You can select a mix of ramped and non-ramped assets, and at least one term-defined asset. For usage-based assets, only term-defined assets are supported.
Select term-defined products or term-defined bundles with all term-defined child products.
If an asset is part of a ramped bundle, the bundle can't contain one-time or evergreen child assets.
Assets selected can't be expired—they have end dates on or after today's date.
Early Renew
In the Managed Assets viewer, select the assets for early renewal.
Click Renew.
In the Set Renewal Term window, select Override Renewal Term, then select Create a ramp schedule.
NOTE If a selected asset is ramped, this option isn't available.
Enter a renewal start date on or before the end date of every selected asset.
You receive a warning if the start date falls within a segment that isn't the final segment. All current and future ramp segments from the start date onward are canceled, and new segments are created.
Select a segment type and specify the duration:
Annual: Creates 12-month segments. If the total duration isn't a multiple of 12, the last segment covers the remaining months.
Custom: Specify the number of segments. The total duration is divided equally across segments.
With either segment type, if the duration divided by the number of months has a remainder, that segment is listed first as a prorated segment.
Review the cancellation and confirm to generate the renewal quote.
EXAMPLE

Your customer has a 3-year ramped subscription (Product A) starting January 1, 2026, with segments at quantities of 100, 150, and 200. They also have a non-ramped asset (Product B) ending November 30, 2028.

On March 1, 2027, the sales rep initiates an early renewal for both assets with a start date of June 1, 2027, a 24-month duration, and yearly segment type. Two new 12-month segments are created: June 1, 2027–May 31, 2028 and June 1, 2028–May 31, 2029.

The renewal quote inherits quantity 150 from the active segment and generates cancellation credits for uncharged remainders.

After the renewal quote is generated, you can modify quantities and attribute values and add products to segments. You can't change dates on auto-generated ramp schedule lines, delete auto-generated ramped lines, or remove child products from a ramped bundle. To make those changes and complete the renewal, create a separate amendment.

=== ARTICLE: ind.qocal_einstein_gen_ai_assisted_quote_creation.htm ===
---
article_id: ind.qocal_einstein_gen_ai_assisted_quote_creation.htm
title: Einstein Gen AI for Quotes
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_einstein_gen_ai_assisted_quote_creation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_foundational_setup_for_quotes_and_orders.htm
fetched_at: 2026-09-04
---

# Einstein Gen AI for Quotes

Einstein Generative AI provides automated overviews and personalized communication to streamline the quote management process. Sales representatives use these features to understand deal status and share proposals with customers efficiently.

Set Up Quote Summaries
Set up Einstein Generative AI and configure quote page layouts to provide sales reps with digestible quote overviews. By using customer data, Einstein summarizes records so reps quickly see the current state of a deal, customer, or prospect for approval.
Set Up Quote Emails
Use Einstein to help your sales reps draft emails to share quote proposals with their customers.

=== ARTICLE: ind.qocal_elevated_data_access_for_pricing.htm ===
---
article_id: ind.qocal_elevated_data_access_for_pricing.htm
title: Secure Data Access for Pricing with Elevated Permissions
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_elevated_data_access_for_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Secure Data Access for Pricing with Elevated Permissions

Protect sensitive data from unauthorized access and have business continuity during sales transaction pricing. This feature helps sales users to price quotes and orders without needing field-level security (FLS) to query, view, or modify the underlying sensitive fields.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To configure data access in quotes and orders:	

Salesforce admin

OR

Customize Application

AND

Manage Profiles and Permission Sets permission


To create and deploy the Pricing Procedure Apex hook class:	Author Apex permission

Before you begin:

In Setup, find and select Revenue Settings. In the Pricing section, turn on Elevated Data Access for Quotes and Orders and Procedure Plan Orchestration for Pricing.
Turn on both settings to apply elevated access to the full pricing execution path, including Procedure Plan Orchestration.

By default, Revenue Cloud's context and pricing services run under the profile of the logged-in user. Elevated Data Access for Quotes and Orders helps the Revenue Cloud pricing engine internally access sensitive fields to calculate prices, even when a user's profile lacks field-level security on those fields.

Users without FLS can price new-sale and amendment, renewal, and cancellation quotes and orders end-to-end. They’re restricted from querying, viewing, or modifying the underlying protected data. Your Salesforce admin controls which sensitive fields the pricing engine uses by creating a custom Apex hook that determines the field inputs to use in the pricing context.

This feature helps you apply strict field-level security to sensitive financial data while allowing sales reps to complete pricing tasks end-to-end.

Configure field-level security on sensitive fields. See Set Field-Level Security for a Field on All Profiles and Assign Permission Set Groups to Users.
Identify all fields that feed into your pricing procedure. For example, cost-book lookup fields, cost-plus inputs, or discount table fields. Work with your pricing procedure author to get a complete list.
Remove Read and Edit access for those fields on any profile that shouldn’t view the sensitive pricing data.
Review the page layouts, list views, or reports accessible to the restricted profile to verify that those fields aren’t available. Removing the FLS is the authoritative control. Hiding fields from layouts alone isn’t sufficient.
Confirm that the fields remain available to the system or pricing admin profile used to run the elevated pricing context.
Create the pricing procedure Apex hook. See Customize Your Procedure Plans with Apex Hooks.
Implement the appropriate pricing hook interface (pre-pricing or post-pricing or both).
In the pre-pricing hook, add or validate the sensitive fields that the engine needs internally.
In the post-pricing hook, strip those fields from the context output before it’s returned to the calling user context.
Deploy and register the Apex class in your Pricing Procedure configuration.
Verify your setup.
Log in as a user with the restricted profile (a sales rep without FLS on the sensitive fields).
Open a quote or order and trigger pricing.
Confirm that the price calculates successfully and the correct output values appear on the transaction.
Confirm that the sales rep can’t see the restricted fields in the record detail, in list views, or through reports.
As a Salesforce admin, run a test to confirm that the Apex hook fires, for both pre-pricing and post-pricing stages, without errors.

=== ARTICLE: ind.qocal_enable_lot_based_renewals.htm ===
---
article_id: ind.qocal_enable_lot_based_renewals.htm
title: Use Lot-Based Renewals to Preserve Original Prices
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_enable_lot_based_renewals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_specialized_transaction_types.htm
fetched_at: 2026-09-04
---

# Use Lot-Based Renewals to Preserve Original Prices

To honor existing prices at renewal time, use lot-based or As-Is renewals to renew asset lot quantities at their original purchase prices. For example, if a sales rep sells an asset across multiple transactions, a lot-based renewal includes both the initial sale and subsequent amendments. The system applies a price uplift individually to each lot based on the renewal uplift.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create as-is renewals:	

InitiateRenewal API permission set

AND

Sales Rep persona permissions

IMPORTANT You use lot-based renewals only when you turn on the As-Is renewals setting. See Enable Revenue Settings. Before you generate a renewal with As-Is Renewals enabled, set the asset's Pricing Source field to Last Transaction Price. If you leave Pricing Source blank or set it to another value, the renewal will be priced at the current list price instead of preserving the original purchase prices.
In the App Launcher, search for and select Assets.
To view all sales transactions for an asset, select an asset and select the Related tab.
Review Asset Actions to see prior sales transactions.

Asset Record

In App Launcher, search for and select Accounts. On the Account page under the Assets tab, select the asset that you want to renew.
To generate a new quote, in the Managed Assets viewer, select Renew.
Under the Quote Line Items tab, on the renewal quote, select View on the product's line.
To review the quote line detail records, under the Related tab, select View All.
The quote line details show the breakdown of the prices honored for lot-based pricing.

=== ARTICLE: ind.qocal_example_automate_order_submission_for_fulfillment.htm ===
---
article_id: ind.qocal_example_automate_order_submission_for_fulfillment.htm
title: "Example: Automate Order Submission for Fulfillment"
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_example_automate_order_submission_for_fulfillment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_order_submission_for_fulfillment.htm
fetched_at: 2026-09-04
---

# Example: Automate Order Submission for Fulfillment

Create a record-triggered flow to submit Revenue Management orders to Dynamic Revenue Orchestrator automatically when users activate the orders. Automation makes sure that all eligible records enter the fulfillment pipeline immediately upon meeting specified status criteria.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To open, edit, or create a flow in Flow Builder:	Manage Flow
To submit orders to Dynamic Revenue Orchestrator and call the invocable actions:	Submit Transaction User
Create a Record-Triggered Flow

Configure the initial trigger and entry conditions for the order object.

From Setup, in the Quick Find box, enter Flows, and then select Flows.
Click New Flow.
Select Start from Scratch and click Next.
Select Record-Triggered Flow and click Create.
Select Order as the object.
Select A record is updated for the trigger configuration.
In the Set Entry Conditions section, specify these details.
Condition Requirements: All Conditions Are Met (AND)
Field: Status
Operator: Equals
Value: Activated
Select Only when a record is updated to meet the condition requirements for the run frequency.
Add a Component to Get Application Usage Type Assignment Records

Find the specific application usage assignment to verify the record type.

Click .
Find and select Get Records.
Enter Get Application Usage Type for the label and Get_Application_Usage_Type for the API name.
Select Application Usage Assignment as the object.
Add these filter conditions.
Field: RecordId
Operator: Equals
Value: {!$Record__Prior.Id}
Click Add Condition and specify these filter conditions.
Field: AppUsageType
Operator: Equals
Value: RevenueLifecycleManagement
Select Choose fields and assign variables (advanced).
In the Record field, select New Resource.
Specify these details for the new resource.
Resource Type: Variable
API Name: ApplicationUsageAssignmentRecord
Data Type: Record
Object: Application Usage Assignment
Click Done.
Add a Decision to Check for Revenue Management Records

Verify that the record belongs to the Revenue Lifecycle Management usage type before proceeding.

Click .
Find and select Decision.
Enter Revenue Lifecycle Management Record? for the label and Is_Revenue_Lifecycle_Management_Record for the API name.
Specify these outcome details.
Label: Revenue Lifecycle Management Record
API Name: Revenue_Lifecycle_Management_Record
Condition Requirements: All Conditions Are Met (AND)
Resource: !ApplicationUsageAssignmentRecord.Id
Operator: Does Not Equal
Value: !$GlobalConstant.EmptyString
Add an Action to Submit Orders to Dynamic Revenue Orchestrator

Invoke the fulfillment submission for the qualified record.

Click  in the Revenue Lifecycle Management Record branch.
Find and select Action.
Specify these action details.
Action: Submit Order
Label: Submit Order Action
API Name: Submit_Order_Action
Order ID: {$Record_Prior.Id}
Click Done.
Save your changes.
Enter a label and API name for the flow and save again.
Activate the flow.

To add the Fulfillment Plan and Orchestration Submission Status fields, edit order page layouts. See Customize Page Layouts with the Enhanced Page Layout Editor.

SEE ALSO
Create or Update Asset From Order Action

=== ARTICLE: ind.qocal_example_extract_product_mentions.htm ===
---
article_id: ind.qocal_example_extract_product_mentions.htm
title: "Example: Extract Products from Opportunity Descriptions"
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_example_extract_product_mentions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_extract_product_mentions.htm
fetched_at: 2026-09-04
---

# Example: Extract Products from Opportunity Descriptions

The sales team at QuantumBit wants to streamline quote creation because critical product and pricing discussions often remain buried within the unstructured text of opportunity description fields. To resolve this issue, the Transaction Management Salesforce admin uses the Extract Product Mentions prompt template to automate the identification of these key details. By creating a custom Flex prompt template and deploying it as an agent action, the Salesforce admin enables sales reps to extract product names, quantities, and attributes directly from the opportunity description to expedite the quoting process.

Follow this example to create a Flex template that extracts details from an Opportunity's Description field.

Create a Flex Prompt Template
Open the Extract Product Mentions template in Prompt Builder and copy its instructions.
Return to the Prompt Builder page and click New Prompt Template.
Select Flex in the Prompt Template Type dropdown.
Specify a name and description.
Under Inputs, click Add to define the resource.
Name: Opportunity Data
API Name: Opportunity_Data
Source Type: Object
Object: Opportunity
Paste the copied instructions into the Prompt section.
In Template Settings, click Resources.
Under Inputs, select Opportunity, then select Description.
Test and click Activate.
Deploy the Template as an Agent Action
Create a custom agent action with a Prompt Template reference action type.
In Setup, select Agentforce Agents and click Revenue Quote Management.
Click Open in Builder.
On the Topics panel, click Quote Management and add your custom action.
Open an opportunity containing product details in its description.
Enter Extract product details for this opportunity in the agent chat window.
The agent retrieves product names, quantities, and attributes.
Add the extracted products to a new or existing quote.

=== ARTICLE: ind.qocal_extend_and_use_sales_transaction_context_definition.htm ===
---
article_id: ind.qocal_extend_and_use_sales_transaction_context_definition.htm
title: Extend the Sales Transaction Context Definition
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_extend_and_use_sales_transaction_context_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_extend_your_transactions_with_custom_field_support.htm
fetched_at: 2026-09-04
---

# Extend the Sales Transaction Context Definition

Extend the standard definition to preserve necessary nodes and attributes for your custom requirements.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To extend context definitions:	

Context Service Admin

AND

Manage Revenue Management


To edit pricing procedures:	Salesforce Pricing Design Time User
From Setup, in the Quick Find box, enter Context Service, and then select Context Definitions.
Locate SalesTransactionContext in the Standard Definitions tab.
Click the dropdown menu and select Extend.
 Give your extended context definition a name and save your changes.
In the Custom Definitions tab, click Edit on your new definition.
Set the Effective From date to occur earlier than your pricing procedure’s start date.
Click Next, leave default structure options unchanged, and save.
Optional: Under the Map Data tab, click Edit as SObject Mapping for Sales Transaction, select Mark as Default, and click Map.
Select your custom definition and click Activate.

=== ARTICLE: ind.qocal_extend_context_definitions.htm ===
---
article_id: ind.qocal_extend_context_definitions.htm
title: Link Context Definitions to Pricing Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_extend_context_definitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_extend_your_transactions_with_custom_field_support.htm
fetched_at: 2026-09-04
---

# Link Context Definitions to Pricing Procedures

Link your pricing procedure to your extended context definition to enable efficient data access.

From the App Launcher, find and select Pricing Procedures.
Select your pricing procedure and deactivate the current version.
Click Edit and select your extended context definition in the Context Definition field.
Save your changes.
Update the Pricing Procedure Properties start date to a time after you created the extended context definition.
Save and activate the pricing procedure.
In Revenue Settings within Setup, select this pricing procedure to apply it to all quotes and orders.

Context Definition Troubleshooting

If you encounter pricing errors after extending a context definition, check for these common issues:

Context definition has both ClonedFrom and InheritedFrom populated
If a context definition record has values in both the ClonedFrom and InheritedFrom fields, it can cause pricing errors. If you find affected records, delete them and recreate the context definition extension.
Something went wrong while hydrating additional context fields
This error can occur when the context definition is out of sync with the pricing procedure, when the context definition was cloned instead of extended, or when the context definition was created without the required permissions. Verify that you extended (not cloned) the context definition and that the pricing procedure references the correct extended context definition.

=== ARTICLE: ind.qocal_extend_your_transactions_with_custom_field_support.htm ===
---
article_id: ind.qocal_extend_your_transactions_with_custom_field_support.htm
title: Extend and Map Sales Transactions in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_extend_your_transactions_with_custom_field_support.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Extend and Map Sales Transactions in Revenue Management

Extend or customize default features to meet business-specific requirements by creating and mapping custom fields in Revenue Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

For example, if your business requires delivery or installation dates that aren’t available by default on sObjects, you can add these custom fields to your sales process objects. Mapping these fields in context definitions makes sure that they appear during transactions and that entered values persist after a refresh.

Before you Begin
Complete these requirements before configuring your extended transactions:
Extend the Sales Transaction Context Definition
Extend the standard definition to preserve necessary nodes and attributes for your custom requirements.
Create Custom Fields and Add Custom Attributes
After extending the definition, add the actual fields to Salesforce objects and the corresponding attributes to the context.
Map Custom Fields in Context Service
Use Context Service to map custom fields across definitions to make sure that values persist during transactions. If you don’t map custom fields to their corresponding attributes, you can’t update those fields on records.
Link Context Definitions to Pricing Procedures
Link your pricing procedure to your extended context definition to enable efficient data access.
Example: Map an Installation Date Field
Follow these steps to track a custom InstallationDate__c field across the sales lifecycle.

=== ARTICLE: ind.qocal_extract_product_mentions.htm ===
---
article_id: ind.qocal_extract_product_mentions.htm
title: Configure Extract Product Mentions Template
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_extract_product_mentions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_foundational_setup_for_quotes_and_orders.htm
fetched_at: 2026-09-04
---

# Configure Extract Product Mentions Template

Use the Extract Product Mentions template to identify products and quantities from emails, Slack messages, or call summaries. This automation eliminates manual data entry by extracting product names, quantities, and attributes directly into quotes or transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Einstein or Agentforce for Sales or Einstein 1 Sales add-on.
USER PERMISSIONS NEEDED
To manage prompt templates in Prompt Builder:	Prompt Template Manager permission set
To access and run the Extract Product Mentions prompt template:	Prompt Template User permission set

Set up Einstein Generative AI and Prompt Builder. When you use agents, turn on Agentforce and set up the Revenue Quote Management agent template.

Review or customize the standard Extract Product Mentions template to suit your business requirements.

From Setup, find and select Prompt Builder.
Under All Prompt Templates, select Extract Product Mentions to open the Prompt Template Workspace .
Review the template ingredients, including the participant, goal, instructions, and output examples.
Save as a new template to override the standard version. You only modify template instructions when overriding a standard template. To ground the template with more data sources like specific object fields, create a Flex prompt template.
Enter the template details
Test your custom prompt template.
Activate the template when you’re satisfied with the outputs.

After you configure the prompt template, integrate it into your sales processes using an invocable action, an agent action, the Connect REST API, or Connect in Apex.

Example: Extract Products from Opportunity Descriptions
The sales team at QuantumBit wants to streamline quote creation because critical product and pricing discussions often remain buried within the unstructured text of opportunity description fields. To resolve this issue, the Transaction Management Salesforce admin uses the Extract Product Mentions prompt template to automate the identification of these key details. By creating a custom Flex prompt template and deploying it as an agent action, the Salesforce admin enables sales reps to extract product names, quantities, and attributes directly from the opportunity description to expedite the quoting process.

=== ARTICLE: ind.qocal_fdo_examples_of_amendment_types_and_results.htm ===
---
article_id: ind.qocal_fdo_examples_of_amendment_types_and_results.htm
title: Future-Dated Amendment Types and Results
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_fdo_examples_of_amendment_types_and_results.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_future_dated_order_amendments.htm
fetched_at: 2026-09-04
---

# Future-Dated Amendment Types and Results

Familiarize yourself with the various types of future-dated amendments and their impact on your asset records. Understanding these behaviors ensures that you accurately manage upsells, reductions, and attribute changes within your asset lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Positive Amendments: Upsell or Add Quantity

Increase the quantity of an asset by setting a positive change on the quote line item (QLI) or order item (OI).

The QLI or OI represents the quantity increase for the entire lifecycle of the amendment.
The process applies the delta quantity increase to all asset state periods (ASPs) that exist beyond the new amendment start date.
Termed assets don’t generate detail lines for positive increases.
Example: You add 10 licenses on May 1, even though you scheduled 5 more licenses for June 1.
Negative Amendments: Reduction or Downgrade

Reduce asset quantity by setting a negative change on the QLI or OI.

Quantity reductions follow a Last In, First Out (LIFO) strategy across the quantity of each asset action source (AAS) within affected ASPs.
A negative amendment creates a detail line for each future-dated ASP with dates corresponding to the generated ASPs.
If an ASP lacks sufficient quantity for the reduction, the system returns an over-reduction validation error.
Repricing and cancellations apply to all pricing reduction scenarios.
Termed Asset Reductions

For termed assets where the product selling model (PSM) is term defined, the reduction quantity applies LIFO per ASP.

Example: An asset has ASP I (Jan 1 to June 30, qty 10) and ASP II (July 1 to Dec 31, qty 15).
If you reduce the quantity by 7 starting Feb 1, the process creates three detailed lines:
One detailed line for ASP I: Feb 1 to June 30, quantity (-7).
Two detail lines for ASP II (by using LIFO): quantity (-5) and quantity (-2), both covering July 1 to Dec 31.
Non-Termed Asset Reductions

For non-termed assets where the PSM is one-time, evergreen, or empty, the reduction quantity follows LIFO order based on the current quantity.

Example: An asset starts Jan 1 with ASP I (qty 10), ASP II (qty 15 starting July 1), and ASP III (qty 20 starting Sept 1).
A reduction of 7 starting Feb 1 creates one detail line because the quantity at that lifecycle point is 10.
A reduction of 7 starting Aug 1 creates two detail lines of -5 and -2. This occurs because the initial quantity of 15 consists of 10 units from the previous Asset State Period and 5 units from an amended transaction.
Attribute or Field Amendments Requiring Repricing

Change attributes, such as upgrading from a basic to an enterprise edition, or modify fields that trigger repricing events.

You set the new attribute value on the order item and select a start date.
This amendment functions as a cancel and reprice operation.
The process creates multiple pairs of cancel and reprice detail lines for each impacted future ASP.
ASP updates apply from the new amendment start date onward.
If attributes differ among intersecting and future ASPs, the attribute value on the amendment line item overrides all future ASP attribute values.
Quantity changes for assets with future ASPs containing different attributes process as an attribute change, resulting in cancellation and repricing.
Early Renewal

Initiating a renewal transaction before the scheduled renewal date overrides all future ASPs, amendments, and renewals.

If you enable As-Is Renewals, the asset renews based on the latest Asset State Period (ASP) quantity. This process uses different prices and quantities than the original purchase price.
Cancellation

Canceling an asset before a future-dated ASP is a specialized reduction type.

Assetization of the cancellation order impacts all future-dated ASPs.
The cancellation places the asset in a terminal state; you can’t perform further ARC operations on a canceled asset.
Transfers and Swaps
Transfers
An asset transfer between accounts acts as an amendment and copies the ASP from the source account to the destination account. It creates a negative amendment (TransferFrom) for the source and adds the asset to the destination (TransferTo). You only transfer the minimum quantity available across all current and future ASPs.
Swaps
A product swap acts as both an add amendment and a negative amendment. Swapped products inherit the ASP and relevant actions, with the quantity reduction applying to all future-dated ASPs starting on the swap date.

=== ARTICLE: ind.qocal_field_and_price_amend_important_considerations.htm ===
---
article_id: ind.qocal_field_and_price_amend_important_considerations.htm
title: Field and Price Amendment Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_field_and_price_amend_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Field and Price Amendment Considerations

Familiarize yourself with the specific requirements for using Field Amendments and Price Amendments to update asset details and adjust pricing effectively. Understanding these technical mappings and supported fields helps you accurately reflect amendments in asset state periods (ASPs) and audit trails.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Implementation Considerations

The Field Amendments feature supports bundles, derived pricing products (DPPs), and usage-based products. Note these technical requirements for field mapping and behavior.

Identification of Changes: The feature identifies field amendment differences by comparing field values on the quote line item (QLI) or order item (OI) against the ASP.
ASP Versioning: ASPs created before Winter ’26 show field value differences between the Asset Action Source (AAS) and the ASP. This discrepancy results in the creation of field amendment actions for line items even without manual changes.
Value Sourcing: During amend, renew, or cancel (ARC) actions, the transaction pulls field values from the ASP record. However, the QLI Legal Entity field maps to and retrieves its value from the AAS field for ARC actions. The system references non-custom field values, including the start date, from the most recent AAS.
Supported Fields

These fields are supported for Field Amendments and Price Amendments.

FEATURE	SUPPORTED FIELDS
Field Amendments	Billing Frequency, Legal Entity, Uplift Percent, Uplift Policy
Price Amendments	Custom Fields, Discount Amount, Discount Percent, Sales Price, Unit Price
Price Amendment Behaviors
Product Support: Price Amendments work on bundles and usage-based products. However, you can't set a new Sales Price or Unit Price for usage-based products.
Derived Pricing: You can use Price Amendments for a derived pricing product (DPP) when a contributing product's price changes. Existing DPP pricing behavior remains unchanged.

=== ARTICLE: ind.qocal_field_and_pricing_amendments.htm ===
---
article_id: ind.qocal_field_and_pricing_amendments.htm
title: Manage Assets with Field and Price Amendments
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_field_and_pricing_amendments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_advanced_amendment_and_renewal_features.htm
fetched_at: 2026-09-04
---

# Manage Assets with Field and Price Amendments

Update asset details and adjust pricing without changing quantities, attributes, or bundle configurations by using Field Amendments and Price Amendments. Use Field Amendments to modify standard and custom fields, such as billing frequency. Use Price Amendments to update the Sales Price on quote lines or the Unit Price on order lines.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To apply field and pricing amendments:	

InitiateAmendment API permission set

AND

Sales Rep persona permissions

Apply a Field Amendment

Field Amendments trigger a formal amendment when you modify a designated field on a quote line item (QLI), changing the quote status from No Change to Amend. Upon activation, the system assetizes the change and adds a Field Amendment asset action subtype to provide a clear audit trail. You can update standard QLI fields and custom fields mapped to the asset state period (ASP).

When you initiate an amendment and change only a price-impacting field, the system performs a cancel and reprice action for the remainder of the term. Assetization creates a cancel line for the remaining term based on the previous value and a reprice line for the new value.

From App Launcher, find and select Accounts.
Select an asset from the Assets tab, and click Amend.
Update a field value in the Transaction Line Table or on the QLI record, such as changing billing frequency from Quarterly to Monthly.
Confirm that the quote action changes to Amend and the subtype updates to Field Amendment.
Complete the Quote-to-Order and order activation processes to create an order with the Amend action.
Assetize the order by using a flow to record the Field Amendment subtype and update the ASP with the new field value.
See Automate Asset Creation from Orders.
EXAMPLE Net Unit Price Increase

A user sells 100 units of an asset at a net unit price of 100. In the middle of the subscription term, the user changes a price-impacting custom field. This change triggers a field amendment effective from the date of the field change.

Assetization creates a cancel line for the remaining term based on the previous custom field value and a reprice line for the remaining term.

Apply a Price Amendment

Price Amendments help you adjust pricing without changing the quantity, attributes, or bundle configuration of an existing asset. You can update the Sales Price on a quote line or the Unit Price on an order line, or apply a discount amount or discount percent. Updated prices are reflected throughout the standard order and billing processes.

NOTE Before you can set a new price by using a Price Amendment, turn on Sales Price Amendments in Revenue Settings. See Set Up Price Amendments.
Select an asset from the Assets tab of the Account page, and click Amend.
Select an effective date for the price change.
To set a new price, enter the new Sales Price or Unit Price. To apply a discount instead, enter a discount percentage or discount amount.
Save your changes.
An amendment quote is created with a delta quantity of zero, and the quote action is updated to Amend.
The total price reflects a prorated credit for the old price and a new charge for the updated price starting from the effective date.
Assetize the order by using a flow.
The creation of an offsetting asset action source (AAS) record cancels the original price and applies the new price
The asset action updates to Upsell for higher total prices or Downsell for lower total prices.
The ASP updates to reflect the new monthly recurring revenue starting from the amendment effective date.
EXAMPLE Decrease the Sales Price

A customer owns 50 CloudSQL seats at a sales price of $50 per user per month for a 3-month subscription. During the term, the sales rep agrees to lower the price to $45 per user per month.

The rep starts a price amendment, sets the effective date, changes the sales price to $45, and leaves the quantity unchanged. The amendment reprices the 50 seats at $45 per user per month for the remainder of the term. The quote line item detail records show a credit for the previous price and a charge for the new price, and the totals roll up to the quote line item and subtotal levels.

=== ARTICLE: ind.qocal_filter_line_items_with_standard_and_advanced_filters.htm ===
---
article_id: ind.qocal_filter_line_items_with_standard_and_advanced_filters.htm
title: Manage Product Visibility with Filters
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_filter_line_items_with_standard_and_advanced_filters.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_user_experience_and_customization.htm
fetched_at: 2026-09-04
---

# Manage Product Visibility with Filters

Use predefined and advanced filters to control which quote or order line items appear in the line editor. Filtering helps sales representatives manage complex quotes by focusing on specific product groups or line item statuses.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Transaction Management is enabled
USER PERMISSIONS NEEDED
To use the Transaction Line Editor or Sales Transaction Line Editor:	

Manage Revenue Management

AND

Create Orders from Quotes permission set

AND

Price and Tax Calculation for Quoting

Predefined filters provide quick access to specific line categories, such as all lines, ramped lines, errored lines, or unconfigured lines. For more granular control, advanced filters provide up to 5 custom conditions based on fields from the Quote Line Item or Order Product objects. These conditions support various operators—such as Equals, Contains, or Greater Than—depending on the data type of the selected field. To target specific sections of a complex quote, apply these conditions to all groups or selected subgroups.

Filter quote or order line items to refine the list of visible products and streamline the quoting process:

Open the Sales Transaction Line Editor and click the filter icon.
Select a filter option based on your needs.
Select a predefined category: All Lines, Errored Lines, Ramped Lines, or Unconfigured Lines.
Select advanced filters to define custom conditions.
In the Advanced Filters panel, set the filter scope. For Filter by Group, select All Groups or specific groups.
Click Add Filter and define the condition by selecting a field, an operator, and a value.
NOTE
To filter by a field from a related record, select the field from the field list. Related record fields include the relationship field name in brackets, such as [Product ID] Product Name.
Advanced filters support fields from records directly related to the Quote Line Item or Order Line Item. Fields that require more than one relationship aren't available for filtering
Filter only by fields that are available to the line editor. If a field isn't listed, add it as a column in the line editor.
For picklist fields, select one or more picklist values.
Add up to 5 conditions and use Add Filter Logic with AND or OR operators to refine the results.
Save your changes.
NOTE
If you apply a field-level column filter and a predefined or advanced filter, the most recently applied filter takes precedence.
When advanced filters are applied, sorting applies only to the filtered results.
NOTE When you apply advanced filters, sorting applies only to the filtered results.
The line editor applies the filter and shows only the matching line items.
To clear the active filter, click Remove Filter. To clear all conditions in the panel, click Remove All.
Advanced Filter Operators
Select an operator to define how the system evaluates field values. Available operators vary by the field's data type.

=== ARTICLE: ind.qocal_flow_templates_automate_renewal_opportunity_creation_and_asset_renewal.htm ===
---
article_id: ind.qocal_flow_templates_automate_renewal_opportunity_creation_and_asset_renewal.htm
title: Asset Renewal Automation Templates
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_flow_templates_automate_renewal_opportunity_creation_and_asset_renewal.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_asset_management_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Asset Renewal Automation Templates

Prebuilt flow templates automatically create renewal opportunities for forecasting and renewing assets. Customize these templates to meet specific business needs before activation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

For example, update Text Template resources to capture more information or match your company's voice, and enter values in the Configure Sender Details section to specify the outgoing email address.

Flow Template Details

Review the descriptions and prerequisites for each flow before activation.

FLOW NAME	DESCRIPTION	PREREQUISITES
Create and Update Renewal Opportunities	

This flow creates opportunity records for renewable assets during order assetization.

If multiple assets share an end date, the flow adds them to the same opportunity record.

	
If your Salesforce org uses multiple currencies, customize the flow to assign asset CurrencyIsoCode values to opportunity products.
Customize the flow to assign the median of net unit prices of a product as the opportunity product net unit price.
Edit the OpportunityName constant to change the name of created opportunity records.
When associating a contract with the order, specify the Renewal Term and Renewal Term Unit on the contract before activating the order.

Automatically Renew Expiring Assets	This flow creates and activates renewal orders for assets set to expire and marked for automatic renewal.	
Assign the InitiateRenewal API permission set to the default workflow user.
Edit page layouts to show the auto-renewal fields.
Show the Automatically Renew Asset by Default field on Product Selling Model pages.
Show the Automatically Renew field on Quote Line Item, Order Item, and Asset pages. See Customize the Transaction Line Editor and Add the Managed Asset Viewer to the Account and Contract Page Layouts.
Product designers and sales reps use these fields to selet products for automatic renewal.
Edit the NumberOfDaysInTheFuture variable to change how many days before expiration the asset renews.
Edit the RetryCount variable to change how many times the flow tries order activation again.
Set a condition to prevent the renewal of discontinued products.

=== ARTICLE: ind.qocal_foundational_setup_for_quotes_and_orders.htm ===
---
article_id: ind.qocal_foundational_setup_for_quotes_and_orders.htm
title: Foundational Setup for Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_foundational_setup_for_quotes_and_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quotes_and_orders_in_the_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Foundational Setup for Quotes and Orders

Execute these configuration procedures to optimize quote and order performance within Salesforce Revenue Management (formerly Revenue Cloud). Prioritize the setup of the Transaction Line Editor, refine all pricing logic, and stabilize API invocation protocols to ensure seamless system integration.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Set Up Quote and Order Features in Revenue Management
Set up features that provide your sales reps, partners, and customers with the capabilities required to efficiently manage quotes and orders.
User Experience and Customization
Personalize the sales and partner experience by customizing Transaction Management visual elements and actions. Use these steps to refine the interface and streamline workflows.
Manage Quote and Order Lifecycle Actions
Sales representatives use specialized actions to duplicate records, adjust pricing, and apply negotiated terms to streamline the transaction lifecycle. These tools ensure consistency across proposals and help sales reps manage complex customer requirements efficiently while reducing manual entry errors.
Configure Extract Product Mentions Template
Use the Extract Product Mentions template to identify products and quantities from emails, Slack messages, or call summaries. This automation eliminates manual data entry by extracting product names, quantities, and attributes directly into quotes or transactions.
Manage Quotes in Revenue Management
Run these configuration procedures to optimize the quote management lifecycle and document generation within Revenue Management. Prioritize the setup of quote line item imports and opportunity synchronization to accelerate record creation while maintaining data alignment across your sales pipeline. By stabilizing these foundational dataflows, you make sure that complex elements like bundles and attributes transition accurately from preliminary offers to finalized orders.
Einstein Gen AI for Quotes
Einstein Generative AI provides automated overviews and personalized communication to streamline the quote management process. Sales representatives use these features to understand deal status and share proposals with customers efficiently.
Quote to Order Conversion
Convert quotes to orders to ensure pricing, product, and tax details transition into your fulfillment and billing workflows. One-click conversion or advanced quote-splitting helps your sales reps maintain data integrity across Revenue Management while segmenting orders based on specific business needs.

=== ARTICLE: ind.qocal_future_dated_order_amendments.htm ===
---
article_id: ind.qocal_future_dated_order_amendments.htm
title: Future-Dated Changes
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_future_dated_order_amendments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_specialized_asset_considerations.htm
fetched_at: 2026-09-04
---

# Future-Dated Changes

To adjust assets that have scheduled future transactions, such as upsells, downsells, renewals, transfers, swaps, or attribute changes, use the Managed Asset viewer. This process updates assets that have more than one subsequent future-dated change recorded as an asset state period (ASP).

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To amend, transfer, or use swaps in orders with future-dated asset state periods:	Initiate Amend user permission or initiateAmendment API access
To renew and cancel orders:	

Initiate Renew and Initiate Cancel user permissions

OR

initiateRenew API and initiateCancel API access

sThe transaction system creates a regular amend, renew, or cancel transaction if the transaction has only one ASP or occurs in the last ASP. Changing an asset before a future ASP on a quote or order creates a single quote line item (QLI) or order item (OI) per asset transaction. The create order process resets the ASP timeline to reflect the new transaction through the end of the subscription period.

For the account that you want to change, go to the Assets tab and open the Managed Assets viewer.
Select the assets and click Amend, Renew, or Cancel.
Enter the date for the change to take effect.
You can select a date before the start date of an existing future ASP.
Click Create Order, and then click Create Single Order.
Select the new order, activate it, and set the status to complete.
Future-Dated Amendment Types and Results
Familiarize yourself with the various types of future-dated amendments and their impact on your asset records. Understanding these behaviors ensures that you accurately manage upsells, reductions, and attribute changes within your asset lifecycle.

=== ARTICLE: ind.qocal_future_dated_order_amendments_important_considerations.htm ===
---
article_id: ind.qocal_future_dated_order_amendments_important_considerations.htm
title: Considerations for Assets with Future-Dated Changes
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_future_dated_order_amendments_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Considerations for Assets with Future-Dated Changes

Keep these considerations in mind when amending, renewing, canceling, transferring, or swapping assets with future-dated changes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
You can't renew an asset with a future-dated renewal already scheduled.
You can’t amend, renew, or cancel before a future asset state period on ramp deals.
You can’t use derived-pricing products (DPP) for future-dated ARC transactions. If the amended date results in a future-dated change, you can’t add DPP assets to a future-dated transaction or select a DPP asset.
You can’t amend a usage-based product with a future-dated and back-dated change.
You can’t reduce the quantity (over-reduce) beyond the quantity between the quote line item’s start and end dates.
You can’t use a rollback amendment to roll back a future-dated amendment change.
You can amend a future-dated order with products that have Constraint Modeling Language rules set up. However, the amendment doesn’t conform to all the rules.

=== ARTICLE: ind.qocal_general_procedures.htm ===
---
article_id: ind.qocal_general_procedures.htm
title: General Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_general_procedures.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_assets_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# General Procedures

Manage products and optimize revenue across your organization by using the asset lifecycle amendment, renewal, and cancellation actions. Use the Managed Asset viewer on your Account or Contract page to initiate these lifecycle changes.

Amend Assets with the Managed Asset Viewer
To meet changing customer needs and optimize revenue, use the asset lifecycle amendment action to modify products your customers purchased. The Managed Asset viewer on your Account or Contract page initiates these changes directly within the asset lifecycle.
Renew Assets with the Managed Asset Viewer
To optimize revenue and manage products efficiently, use the asset lifecycle renewal action. The Managed Asset viewer on your Account or Contract page initiates these renewals directly within the asset lifecycle.
Cancel Assets with the Managed Asset Viewer
To optimize revenue and manage your product lifecycle, use the asset lifecycle cancellation action to terminate purchased products. The Managed Asset viewer on your Account or Contract page helps you to initiate cancellations and make sure that your records accurately reflect your business relationships.

=== ARTICLE: ind.qocal_generate_quote_document_doc_builder.htm ===
---
article_id: ind.qocal_generate_quote_document_doc_builder.htm
title: Generate a Quote Document with Document Builder
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_generate_quote_document_doc_builder.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_features.htm
fetched_at: 2026-09-04
---

# Generate a Quote Document with Document Builder

Preview, generate, and email quote PDFs to serve your customers. Use this professional document generation solution to share details of work performed with your customers in real-time.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To generate a quote PDF document:	Document Builder User permission set

In your generated documents, products are visible in this manner.

Quote documents show all root products.
Quote documents show child products only when you leave the Quote Visibility field unselected or set the field to Always or Quote Document Only.
Go to a quote.
From , click Generate PDF Document.
Click Preview PDF to preview your quote document.
Review the details on the quote document, and then click Create PDF.
You receive a notification when the PDF is ready.
Access your created PDFs on the quote record by scrolling to the Quote PDFs section on the Related tab.
View your PDF by clicking a quote document name in the list view.
Email the PDF to your customer by clicking next to the quote document and selecting Email PDF.

=== ARTICLE: ind.qocal_grant_binding.htm ===
---
article_id: ind.qocal_grant_binding.htm
title: Grant Binding
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_grant_binding.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling_advanced_concepts.htm
fetched_at: 2026-09-04
---

# Grant Binding

Grant binding determines how the grants of resources contained in an asset are pooled and consumed. In simpler terms, the binding decides whether a purchased service (like 1,000 text messages) is related to a single asset or shared across a wider group, such as an organization or a specific contract.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Binding Targets

When you add a quote line item or an order item to a quote or an order for usage-based products, you must select a binding target.

BINDING TARGET	DESCRIPTION
Self	The usage resources are bound to the asset itself. A standalone asset is created where the grants are only available to that specific line item. This is the default target for all usage products.
Product	The usage resources are bound to a product. An asset linked to the pack product or a line item can consume the resources.
Account	The usage resources are bound to a specific account. Multiple assets associated with the selected account can share the resources.
Contract	The usage resources are bound to a specific contract. Any asset linked to that contract can consume the resources.
Custom	The usage resources are bound to a custom object, if the standard options don’t fit the business model. Use the BindingObjectCustomExt object for custom object binding.
NOTE You can’t bind a commitment-based usage product to a target.

When you bind to a target and the order is activated, the consumption process creates a Usage Entitlement Account (UEA) record. This record acts as the container for the lifecycle of the service.

Multiple assets can be bound to the same target (for example, five different phones that use data service attached to the family account). The UEA tracks the validity period of the shared service by calculating the minimum start date and the maximum end date of all assets bound to that account. The UEA remains active as long as at least one asset bound to the target is active.

For every binding target and usage resource combination, the Usage Management process creates a wallet, which is tracked by the Usage Entitlement Bucket. Even if you buy multiple pack products, the total balance is aggregated and shown in this wallet.

IMPORTANT After an order is assetized, you can neither change the binding target nor move assets from one target to another.

When you bind multiple assets to the same target:

The product and price book entry associated with the usage entitlement account are determined by the first asset bound to the target.
The effective period for the bounded target is determined by the earliest start date and the latest end date of all associated assets.
The transaction usage entitlement associated with the parent usage entitlement is the first transaction usage entitlement created after the first product related to the bounded target is assetized.
EXAMPLE

To understand which binding type to select, let’s consider a company, Quantum Corp. The company purchases a communication suite that includes 500 SMS, 1,000 emails, and 10,000 API calls. Depending on their organizational needs, they can bind these grants in four ways:

Bind to Self (Asset Binding)—Quantum Corp buys a plan specifically for a remote contractor. The grants are bound to the individual asset. Only the contractor’s specific device can use these 500 SMS. In the Wallet view, the target is listed as Self.
Bind to Account—Quantum Corp wants their entire organization to share the resource pool and therefore, the grants are bound to the account. All departments, such as Sales, Marketing, and Finance that are associated with that account draws from the same 1,000 emails. The binding allows for resource sharing across multiple assets linked to an account.
Bind to Contract—Quantum Corp has a specific legal agreement for a three-year project. The grants are bound to the Contract ID. Any asset created under this specific contract draws from the 10,000 API calls. The binding makes sure that usage is strictly tied to the terms and duration of a specific legal entity.
Bind to Custom—Quantum Corp uses a multitenant cloud architecture. The grants are bound to a custom entity, such as a Tenant ID. This is used for specialized business models where resources must be isolated by a unique identifier other than a standard account or contract.
Rate Conflicts and Negotiation

A complexity arises when you attempt to bind multiple products to the same target that share the same resource, but have different negotiated rates.

EXAMPLE

If you bought a product bound to Account A with a negotiated rate of $0.80 per text, and later try to buy another product bound to Account A with a rate of $0.70 per text, it becomes a conflict.

To resolve the conflict, for a given resource and binding target combination, there must be a single agreed-upon rate. Usage Management automatically picks the cheapest rate available across multiple assets linked to the target. If a new asset or pack is purchased later, it overrides the existing rates.

SEE ALSO
Build a Quote for Usage-Based Products

=== ARTICLE: ind.qocal_header_adjustments_overview.htm ===
---
article_id: ind.qocal_header_adjustments_overview.htm
title: Set Up Header Adjustments
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_header_adjustments_overview.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_common_capabilities.htm
fetched_at: 2026-09-04
---

# Set Up Header Adjustments

Configure header adjustments to help your sales reps to apply discounts to an entire quote or order. Use the Discount Distribution Service (DDS) element in your pricing procedures to support this feature.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create pricing procedures:	Salesforce Pricing Design Time User permission set
IMPORTANT You can’t apply discount distribution to a pricing procedure that was used to calculate a product's derived price. This means that you can't have a Derived Price and a Discount Distribution Service element within the same pricing procedure.
SEE ALSO
Apply Header Adjustments to Quotes and Orders
Option 1: Set Up Header Adjustments Without Derived Pricing
Clone your Transaction Management pricing procedure.
Open the version in Pricing Procedure Builder and delete any existing derived pricing elements.
Add constants for header distribution types.
See Create Constant Resources.
Constant DDS Amount - Type: Text and Value: Amount
Constant DDS Percentage - Type: Text and Value: Percentage
Constant DDS Override - Type: Text and Value: Override
Add a List Group and Assignment for each discount type - Amount, Percentage, and Override.
Configure the Discount Distribution Service element and map the header variables.
In Revenue Settings, turn on Header Adjustments.
Option 2: Set Up Header Adjustments With Derived Pricing
Configure a separate pricing procedure specifically for the Discount Distribution Service element.
Create a Procedure Plan Definition for Quotes and another for Orders.
See Create a Custom Procedure Plan Definition.
Add two sections to the plan for these calculations.
Standard Pricing
DDS Pricing Procedure
In Revenue Settings, turn on Procedure Plan Orchestration for Pricing and turn on Header Adjustments.

=== ARTICLE: ind.qocal_header_adjustments_use.htm ===
---
article_id: ind.qocal_header_adjustments_use.htm
title: Apply Header Adjustments to Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_header_adjustments_use.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_sales_transactions_rev_cloud.htm
fetched_at: 2026-09-04
---

# Apply Header Adjustments to Quotes and Orders

Provide amount and percent discounts or override the total amount for an entire quote or order. Transaction Management automatically distributes these discounts equally or proportionally among line items based on your selected distribution method. The price waterfall shows the specific discount applied to each line item to ensure pricing transparency.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To use header discounts:	Salesforce Pricing Run Time User permission set
NOTE Complete the setup for header adjustments, to apply header adjustments to your transactions. See Set Up Header Adjustments.

Modify the total price of a transaction by selecting an adjustment type and distribution logic within the Manage Header Adjustment interface.

Open a quote or an order.
Click Manage Header Adjustment.
Select an adjustment type.
Amount: Distributes a specific currency amount among all lines based on the selected distribution logic.
Percentage: Applies a specified discount percentage to every line item.
Amount Override: Calculates the difference between your specified value and the current total price, then distributes that difference among all lines.
Enter an adjustment value.
Select adjustment distribution logic.
Equal: Distributes the discount value equally among all line items.
Proportionate: Distributes the discount proportionally based on the List Price Total (List Price * Quantity) of each line.
Click Reprice All if the Delta Pricing for Quotes and Orders setting is turned on.
The system applies adjustments correctly and shows accurate prices for all lines.
SEE ALSO
Discount Distribution Service
Set Up Delta Pricing for Quotes and Orders

=== ARTICLE: ind.qocal_improve_usability.htm ===
---
article_id: ind.qocal_improve_usability.htm
title: Add an Order Application Usage Type Automatically in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_improve_usability.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_orders_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Add an Order Application Usage Type Automatically in Revenue Management

Simplify order creation by using an Apex trigger to populate the Application Usage Type field . This field establishes the application context for the record. For all new orders, it creates an AppUsageAssignments record of type RevenueLifecycleManagement.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Apex Trigger Sample for Application Usage

Use this sample code snippet to populate the AppUsageType field with RevenueLifecycleManagement.

trigger RlmOrderTriggerSample on Order(after insert) {
    List<AppUsageAssignment> assignments = new List <AppUsageAssignment>();
    for (Order ord: Trigger.New) {
        // Do further filtering as necessary
        AppUsageAssignment aua = new AppUsageAssignment(
            RecordId = ord.Id,
            AppUsageType = 'RevenueLifecycleManagement'
        );
        assignments.add(aua);
    }
    insert assignments;
}

=== ARTICLE: ind.qocal_inflight_supplemental_order_amendments.htm ===
---
article_id: ind.qocal_inflight_supplemental_order_amendments.htm
title: Modify Activated Orders Before Fulfillment in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_inflight_supplemental_order_amendments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_orders_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Modify Activated Orders Before Fulfillment in Revenue Management

Use in-flight amendments or supplemental change orders to modify existing orders after activation but before fulfillment. This feature captures changes in a linked order to establish a unified order view, streamline order modification, and improve accuracy.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To place supplemental orders:	

Place Supplemental Orders permission set

AND

Sales Operations Rep permission group

Prerequisites for Supplemental Orders

Before modifying orders, perform these setup tasks.

For the Order object, configure a new Superseded status. For more help, see Create a Custom Picklist Field.
Add the Change button to the order page layout. To modify an object's page layout, see Customize Page Layouts with the Enhanced Page Layout Editor.
IMPORTANT Review these impacts when you submit an original order to DRO.
Salesforce locks line items when the fulfillment process reaches the point of no return (PONR).
The system locks the fulfillment plan associated with the original order.
Submitting the supplemental order updates the original fulfillment plan instead of creating one.
Change an Activated Order

Update products and quantities for an activated but unfulfilled order by creating a supplemental order.

On the order page, select an activated order and click Change.
Salesforce creates a copy of the original order in Draft status.
The system copies all products, application usage assignments, order actions, relationships, attributes, and custom child entities.
The supplemental order appears under the Related Order list of the original order with the Related Order Type set to supplemental order.
From the order line dropdown, select Configure to reconfigure an order item.
Edit the product attributes.
Select Save & Exit.
The Supplemental Change Type column updates to Amend for edited products or quantity changes.
New order items receive the Add type.
Items without updates show the No Change type.
Pricing preference defaults to Skip.
Activate the order.
The original order status changes to Superseded and the new supplemental order replaces it.

=== ARTICLE: ind.qocal_invoke_place_sales_transaction_in_a_flow.htm ===
---
article_id: ind.qocal_invoke_place_sales_transaction_in_a_flow.htm
title: Invoke the Place Sales Transaction API in a Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_invoke_place_sales_transaction_in_a_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Invoke the Place Sales Transaction API in a Flow

Invoke the Place Sales Transaction (PST) API to create, update, and delete quotes and orders and price their related products and services. Before you can invoke the action, create and set the values of an Apex-defined variable to use as the graph input for the action. You can use the other inputs to configure how Salesforce prices and validates the quote or order. The action returns the ID of the sales transaction as well as status information.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
NOTE Use the Invoke Place Sales Transaction API action in Agentforce Quoting flows only. The action is designed for the Agentforce Quoting flow execution context and isn't compatible with other flow types. To call the Place Sales Transaction API from a flow other than an Agentforce Quoting flow, use a custom Apex action that calls the API directly. The Place Sales Transaction invocable action is designed for agentic invocation and doesn't support ramp deals or automated processes.

In Flow Builder, add an Action element to your flow. Select the Revenue Cloud category, and search for Invoke Place Sales Transaction API.

Set Input Values
INPUT PARAMETER	DESCRIPTION
Catalog Rates Preferences	

Specify how Revenue Management prices a quote or order during processing. For example, if you add a quote line item to a quote, it’s possible that you don’t want to price the quote yet. Possible values are:

Force—Always price the quote or order.
Skip—Never price the quote or order.
System—Follow the system preference, which is used to determine whether a pricing calculation is required.

The default value is System.


Configuration Method	

Specify when Revenue Management fetches rate card entries for quote line items with usage-based pricing during the quote creation process. Possible values are:

Fetch—Retrieve the rate card entries during the quote creation process.
Skip—Skip retrieving rate card entries for quote line items during the quote creation process.

The default value is Skip. This property is available only when usage-based selling is enabled.


Configuration Options	

Specify the rules that Salesforce follows to validate a quote or order. These options are expressed as booleans. To specify Revenue Cloud to perform an action, set the value for the option to true. You can specify true for multiple options. Options include:

validateProductCatalog—When true, validates against the product catalog.
validateAmendRenewCancel—When true, runs validations for amend, renew, or cancel processes.
executeConfigurationRules—When true, the order must adhere to configuration rules during processing. When false, the rules are bypassed and a warning is issued.
addDefaultConfiguration—When true, automatically add the default configurations to the quote or order.

The default value for all options is false.


Context Detail	Specify a string that contains the context ID so you can reuse the session context in a subsequent Place Sales Transaction API operation.
Graph	

This input is an Apex-defined variable of class RevSalesTrxn_RecordReference. It has two fields.

graphId—A string that identifies the graph.
records—An Apex-defined variable of class RevSalesTrxn_RecordReference.

The value of the records field depends on the object that you’re acting on and the action that you’re taking on the object. For example, to add line items to a Quote, you can set the records field as follows.

RecordReference.referenceId—A string that identifies the variable.
RecordReference.record.method—A string that defines the API method to call, for example, POST.
RecordReference.record.type—A string that defines the object to change, for example, QuoteLineItem.
RecordReference.record.fieldValues—A collection of Apex-defined variables of class RevSalesTrxn_RecordMapWrapper. Add the value of these Apex-defined variables to the fieldValues collection.
TransactionNameRecordMapWrapper
OppNameRecordMapWrapper
PricebookNameRecordMapWrapper
Store Output Values
OUTPUT PARAMETER	DESCRIPTION
Context Detail	An alphanumeric string that identifies the context.
Sales Transaction ID	The ID of the quote or order in this transaction.
Status URL	A link to the AsyncOperationTracker table that shows the status of your request. To return the status of that action, append an action’s Tracker ID to the URL.
Tracker ID	An alphanumeric string that identifies the specific action. To return the action’s status, append this ID to the Status URL.
Usage

To set up the Place Sales Transaction API input:

Use an Assignment element to set the field values of the TransactionNameRecordMapWrapper, OppNameRecordMapWrapper, and PricebookNameRecordMapWrapper of RevSalesTrxn_RecordMapWrapper class variables.
If you want to include configuration options, create the options as new Boolean variables.
NOTE Updates made through the Sales Transaction Line Editor don’t trigger record-triggered flows on Quote Line Group. The Sales Transaction Line Editor processes these updates through the Place Sales Transaction API in this order: Quote, Quote Line Group, and then Quote Line Item. When a Quote Line Group field changes in the Sales Transaction Line Editor and related Quote Line Items require updates, use custom Apex hooks instead of declarative record-triggered flows.

=== ARTICLE: ind.qocal_limitations_for_using_quote_and_order_capture.htm ===
---
article_id: ind.qocal_limitations_for_using_quote_and_order_capture.htm
title: Transaction Management Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_limitations_for_using_quote_and_order_capture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Transaction Management Considerations

Review essential requirements and behaviors before using Transaction Management to manage your quotes and orders. Understanding these configurations, including page layout updates, pricing synchronization, and field permissions, ensures accurate transaction processing and data integrity.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
UI and Button Configurations
Revenue Management excludes support for Add Products and Edit Products buttons on quote and order related lists.
Turn off these buttons on quote and order page layouts.
Sales reps use the Add Product search field or the Browse Catalog button to find and add products.
To use the Browse Catalogs quick action on quote and account record pages, set up Product Discovery.
Pricing and Data Synchronization
Product updates and price changes require decision table refreshes, price syncing, and updates to context definitions.
If you add a new product, update product pricing, or create contract pricing, refresh all decision tables in your org.
If you define a qualification rule for a new product in Product Catalog Management, update the decision table for that specific rule.
Sync pricing data after changing information in Salesforce Pricing to make sure that reps see accurate prices.
Salesforce Pricing automatically populates Net Unit Price, Net Total Price, Total Adjustment Amount, Pricing Term Count, and Total Line Amount for order products.
Make these fields "read only" on the order product page layout to prevent manual edits when a pricing engine is active.
API and Integration Rules
Use the Place Order API to create, edit, and price orders for custom user interfaces.
Salesforce Pricing doesn’t trigger when you use other mechanisms, such as sObject APIs.
Any update to Order or Order Product records outside the Transaction Line Editor or Sales Transaction Line Editor (including updates through the API, Process Builder, or manual field edits) sets the validation result to Transaction Incomplete. This requires repricing before the order can be activated. This behavior applies to all fields, including non-pricing fields such as Description.
Similarly, any update to Quote Line Items outside the line editors invalidates the pricing status and triggers a Reprice All requirement. If your org has automations or triggers that modify Quote Line Item or Order Product fields, ensure they run within the supported transaction flow to avoid pricing validation errors.
The Asset object doesn’t support the Quote Action related list because Revenue Management creates assets from finalized orders rather than quotes.
To view amendments, renewals, or cancellations, use the associated order records.
Feature Compatibility and Permissions
Users with Subscription Management permissions use existing standalone products, bundles, and generate assets in both Subscription Management and Revenue Management.
Revenue Management shows these fields after enablement: Include component by default (set to true for static bundles), Allow qty changes, Min qty, Max qty, and Group.
Contact Salesforce Customer Support to resolve validation errors resulting from modifications to an existing bundle.
Subscription Management users manage standalone products, bundles, and assets in both Subscription Management and Revenue Management.
More Resources
Customize Related Lists
Refresh a Decision Table
Product Discovery Setup
Customize Page Layouts with the Enhanced Page Layout Editor
Field Permissions
Sync Pricing Data

=== ARTICLE: ind.qocal_limits.htm ===
---
article_id: ind.qocal_limits.htm
title: Transaction Management Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Transaction Management Limits

Review the record, attribute, and bundle limits for Transaction Management to make sure that your quotes and orders remain within supported thresholds. Understanding these technical specifics helps you optimize performance and avoid process timeouts during asset lifecycle operations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Record and Attribute Limits

Transaction Management enforces limits on the number of line items and related records to maintain system stability.

OBJECT	LIMIT
Quote Line Items	Up to 2,000 per quote
Order Products	Up to 2,000 per order
Total Quote Records	Up to 5,000 total records per quote, including related records like relationships, attributes, related objects, tax items, and price adjustments
Quote Line Item Attributes	Up to 3,000 per quote
Order Line Item Attributes	Up to 3,000 per order
Asset Lifecycle Flow Limits

Standard flow timeouts impact the creation of amendment, renewal, and cancellation (ARC) quotes when they use the UI.

The UI supports creating ARC quotes with up to 300 lines.
Update quotes to 1,000 lines using Asset Lifecycle Standard Invocable Actions or the Add Assets button in the Quote Viewer.
Bundle and Apex Performance Recommendations
Bundle Size: A bundle includes up to 200 lines, including the root product. This means a single quote line item or order line item for a bundle supports up to 199 associated child items.
Apex Optimization: Synchronous custom Apex code consumes significant resources and triggers governor limits. Use Asynchronous Apex to optimize performance.
IMPORTANT To raise these limits when possible, contact Salesforce Customer Support.

=== ARTICLE: ind.qocal_manage_assets_from_a_contract.htm ===
---
article_id: ind.qocal_manage_assets_from_a_contract.htm
title: Manage Contracts in the Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_manage_assets_from_a_contract.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_contract_management_essentials.htm
fetched_at: 2026-09-04
---

# Manage Contracts in the Revenue Management

Manage contracts and their assets and contract pricing schedules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To amend, renew or cancel assets:	Amend Assets, Renew Assets, Cancel Assets, and Sales Rep permission group
From the App Launcher, find and select Contracts.
In the Contracts List View, click a contract number.
On the Assets tab, use the Managed Assets Viewer to select an asset for amendment, renewal, or cancellation.
Create contract prices or discounts.
Save your changes.
EXAMPLE

=== ARTICLE: ind.qocal_manage_assets_in_revenue_lifecycle_management.htm ===
---
article_id: ind.qocal_manage_assets_in_revenue_lifecycle_management.htm
title: Amending, Renewing, and Canceling Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_manage_assets_in_revenue_lifecycle_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle.htm
fetched_at: 2026-09-04
---

# Amending, Renewing, and Canceling Assets

Use Revenue Management (formerly Revenue Cloud) to manage the products or assets that your customers purchase. With this feature, your sales reps can amend, renew, or cancel assets to meet the needs of your customers.

IMPORTANT Amend, Renew, and Cancel operations work only with assets that were created through the standard Revenue Management lifecycle (order activation). Assets that were migrated from another system or manually created may not have the required data relationships for these operations. If you need to amend, renew, or cancel a migrated or manually created asset, create a new order through Revenue Management to establish the correct asset record.
General Procedures
Manage products and optimize revenue across your organization by using the asset lifecycle amendment, renewal, and cancellation actions. Use the Managed Asset viewer on your Account or Contract page to initiate these lifecycle changes.
Advanced Amendment and Renewal Features
Revenue Management provides flexible asset management by helping sales reps to apply negotiated contract pricing to amendments and renewals. You can use specialized features to adjust subscription start and end dates for termed assets, perform field or price-only updates without changing configurations, and use the Rollback tool to reverse the most recent future-dated transactions. These capabilities ensure data integrity and accommodate evolving customer needs throughout the asset lifecycle.
Specialized Transaction Types
Streamline sales operations by transferring asset quantities between accounts or swapping products while maintaining accurate audit trails and relationship labels. Use lot-based renewals to honor original purchase prices across multiple transactions and apply price uplifts to individual lots. You can also renew expired assets and subscriptions by choosing new start and end dates, providing flexibility for late renewals and trial extensions.
Specialized Asset Considerations
Revenue Management allows you to modify assets with scheduled future transactions, such as upsells, renewals, or swaps, by using specific amendment types. Sales reps can meet precise contract requirements and manage global subscriptions by using exact time zone precision to establish accurate asset state periods. Additionally, users can negotiate and track changes to catalog or negotiated rates and grants through an asset-level audit trail during amendments and renewals
Honor Precise Time Zones in Asset Lifecycle Start and End Dates
Specify exact time zone precision for asset lifecycle start and end dates to meet detailed contract requirements and manage complex global subscriptions. Time resolution makes sure that asset state periods (ASPs) and subsequent amend, renew, cancel, transfer, and swap operations start and end exactly as specified, providing parity for noncontiguous changes.
Update Assets to Reflect Changes by Using Flows
Update your assets after completing amendment, renewal, or cancellation changes to your quotes or orders. This process ensures that your assets accurately reflect modifications made to the asset lifecycle.

=== ARTICLE: ind.qocal_manage_contract_pricing_in_revenue_lifecycle_management.htm ===
---
article_id: ind.qocal_manage_contract_pricing_in_revenue_lifecycle_management.htm
title: Contract Pricing Agreements
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_manage_contract_pricing_in_revenue_lifecycle_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contracts_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Contract Pricing Agreements

Negotiate and apply customer-specific prices and discounts to future business transactions by creating contract item prices and adjustment schedules. Managing these agreements makes sure that your sales reps honor negotiated rates consistently across quotes and orders.

Manage Contract Prices or Discounts Manually
Sales reps manually specify contract prices or discounts when they create a contract. When you create contract item prices and price adjustment schedules, the system applies the negotiated pricing and discounts to future business transactions.
Set Up Tiered Contract Pricing
Negotiate prices and discounts based on purchase quantities to encourage larger sales and apply customer-specific adjustments to ongoing transactions. Managing these agreements helps you to create volume tiers against a contract item price record and view the calculations in the net unit price waterfall.
Set Up Contract Pricing Extensibility
Define unique Contract Item Price (CIP) records by using custom fields to bypass default uniqueness checks and record validations. This extensibility helps your business to set flexible contract pricing based on custom parameters that match your specific organizational needs.
Calculate Cumulative Quantity Pricing for Contractual Discounts
Motivate larger purchases by aggregating product quantities across transactions and active assets to apply accurate negotiated price or discount tiers. This approach combines quantities from quote lines with existing active assets to make sure that the system applies the correct tier based on total purchase volume over time.
Coterminate Subscription Assets with Contract End Dates
Synchronize subscription end dates with their corresponding contract end dates to improve accuracy and efficiency in sales and renewal processes. Cotermination reduces manual mistakes, simplifies renewals, and minimizes administrative tasks associated with managing subscription lifecycles.

=== ARTICLE: ind.qocal_manage_contracts_in_revenue_lifecycle_management.htm ===
---
article_id: ind.qocal_manage_contracts_in_revenue_lifecycle_management.htm
title: Contracts in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_manage_contracts_in_revenue_lifecycle_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Contracts in Revenue Management

Use contracts in Revenue Management (formerly Revenue Cloud) to organize and manage customer assets, products, and services throughout their lifecycle.

Contractual agreements serve as a central hub for establishing long-term relationships and applying negotiated pricing across various sales scenarios. By grouping multiple assets under a single contract, you simplify tracking and help sales reps to perform critical actions—such as amending, renewing, or canceling assets—directly from the contract record via the Managed Assets viewer.

Set Up Contract Features in Revenue Management
Revenue Management offers capabilities for sales reps and partners to manage contracts. These features ensure data consistency by automatically pulling account and date details from source quotes or orders.
Contract Management Essentials
Understand the components of Revenue Management contracting to organize customer assets efficiently and maintain accurate pricing agreements throughout the business relationship.
Add a Special Term to a Quote
Search the Document Clause Library and insert an active clause as a quote special term. Resolve any placeholder tokens, then save so that the term stays relevant to your quote.
Contract Pricing Agreements
Negotiate and apply customer-specific prices and discounts to future business transactions by creating contract item prices and adjustment schedules. Managing these agreements makes sure that your sales reps honor negotiated rates consistently across quotes and orders.

=== ARTICLE: ind.qocal_manage_orders_in_revenue_lifecycle_management.htm ===
---
article_id: ind.qocal_manage_orders_in_revenue_lifecycle_management.htm
title: Manage Orders in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_manage_orders_in_revenue_lifecycle_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quotes_and_orders_in_the_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Manage Orders in Revenue Management

Orders signify a formal agreement between your business and the customer, detailing the products, services, and pricing. Learn how to create and manage orders effectively.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Create an Order
Skip the quotation and approval phases for straightforward transactions by generating an order record directly. This process enables you to manage sales that require immediate fulfillment without preliminary quote documentation.
Add an Order Application Usage Type Automatically in Revenue Management
Simplify order creation by using an Apex trigger to populate the Application Usage Type field . This field establishes the application context for the record. For all new orders, it creates an AppUsageAssignments record of type RevenueLifecycleManagement.
Order Lifecycle Management
Define the possible states and transitions for an order by using order lifecycle. For example, define states such as Submitted, Processing, and Fulfilled. Then specify that an order state changes from Submitted to Processing and from Processing to Fulfilled.
Order Submission to Dynamic Revenue Orchestrator
Submit sales transactions to Dynamic Revenue Orchestrator (DRO) for fulfillment by using the Submit Sales Transaction invocable action in flows or Apex classes. Automating this process via record-triggered flows makes sure that all eligible records enter the fulfillment pipeline immediately upon meeting specified criteria. Customizing order page layouts to include Orchestration Plan and Orchestration Submission Status fields provides users with real-time visibility into the fulfillment progress.
Modify Activated Orders Before Fulfillment in Revenue Management
Use in-flight amendments or supplemental change orders to modify existing orders after activation but before fulfillment. This feature captures changes in a linked order to establish a unified order view, streamline order modification, and improve accuracy.

=== ARTICLE: ind.qocal_manage_sequencing_for_tiered_volume_discounts.htm ===
---
article_id: ind.qocal_manage_sequencing_for_tiered_volume_discounts.htm
title: Configure Line Item Sequencing for Tiered Volume Discounts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_manage_sequencing_for_tiered_volume_discounts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_contract_features.htm
fetched_at: 2026-09-04
---

# Configure Line Item Sequencing for Tiered Volume Discounts

Define a sequencing field to control the order in which the system applies tiered or volume contractual discounts to sales transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To configure the Cumulative Quantity Pricing Sort Order Tag Configuration setting:	Customize Application

By default, the system sequences line items by quantity when applying tiered volume discounts, but you can override this behavior by setting a field in the Cumulative Quantity Pricing Sort Order Tag Configuration setting. To manage sequencing and apply discounts in sequence, your sales reps enter a sequence number in the configured field for each line item within the transaction.

Map the field that you want to use for sequencing to a custom context tag in your custom sales transaction context definition. See Context Definitions.

From Setup, in the Quick Find box, search for and select Revenue Settings.
For the Cumulative Quantity Pricing Sort Order Tag Configuration setting, enter the context tag of your field.
Save your changes.

=== ARTICLE: ind.qocal_manage_transaction_processing_and_attribute_handling.htm ===
---
article_id: ind.qocal_manage_transaction_processing_and_attribute_handling.htm
title: Set Up Transaction Processing for Complex Product Configurations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_manage_transaction_processing_and_attribute_handling.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_common_capabilities.htm
fetched_at: 2026-09-04
---

# Set Up Transaction Processing for Complex Product Configurations

To handle complex product configurations, increase the number of product attributes that a sales transaction can support. To control performance, you can also specify the number of records processed in a single transaction.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Transaction Management is enabled
USER PERMISSIONS NEEDED
To configure transaction processing and attribute handling:	

Customize Application

AND

View Setup and Configuration

From Setup, in the Quick Find box, enter and then select Revenue Settings.
Turn on Increased Attribute Limits.
The default limit is 3,000 product attributes across all quote lines, but a standard transaction supports up to 10,000 product attributes. To increase the limit, contact Salesforce Customer Support.
IMPORTANT
If you increase the number of supported product attributes and then turn off Increased Attribute Limits, the attribute limit resets to the default value of 3,000. To restore a higher limit, contact Salesforce Customer Support.
If you turn off Increased Attribute Limits after creating quotes or orders that use higher attribute limits, reset the attribute limits before updating existing transactions. Existing quotes or orders can fail if the previous attribute limits are still applied.
To specify the number of records processed in a single transaction, in Revenue Settings, for Records Persisted per Transaction, select either 200 or 500 records.
A higher value can increase the processing load. Before updating this setting, make sure that the associated triggers, flows, and validation rules can handle the increased number of records per transaction within governor limits.

=== ARTICLE: ind.qocal_map_custom_fields.htm ===
---
article_id: ind.qocal_map_custom_fields.htm
title: Map Custom Fields in Context Service
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_map_custom_fields.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_extend_your_transactions_with_custom_field_support.htm
fetched_at: 2026-09-04
---

# Map Custom Fields in Context Service

Use Context Service to map custom fields across definitions to make sure that values persist during transactions. If you don’t map custom fields to their corresponding attributes, you can’t update those fields on records.

Here are the list of key mapping types.

sObject Mapping: Links a context definition node to a Salesforce object (for example, QuoteEntitiesMapping).
Cross-context mapping: Links attributes between two different definitions (for example, Product Discovery to Sales Transaction).
Context definition mapping: Links attributes within a specific flow (for example, Order to Asset).
CONTEXT DEFINITION	MAPPING	PROCESS	SOURCE	DESTINATION	TYPE OF MAPPING
ProductDiscovery Extended Context Definition	ProductDiscoveryMapping	Product Discovery	ProductDiscoveryExtended Context Definition	Product2	sObject
Sales Transaction Context Definition	ProductDiscoveryContextMapping	Product Discovery to Sales Transaction	SalesTransaction Context Definition	Product Discovery Extended Context Definition	Cross-context definition mapping
QuoteEntitiesMapping	Quote	SalesTransaction Context Definition	QuoteEntities	sObject
OrderEntitiesMapping	Order	SalesTransaction Context Definition	Order Entities	sObject
ContractNodeMapping	Contract	SalesTransaction Context Definition	Contract Entities	sObject
AssetEntitiesMapping	Assets	SalesTransaction Context Definition	Asset Entities	sObject
ContractToSalesTxnMapping	

Order to Contract 

Quote to Contract

	SalesTransaction Context Definition	SalesTransaction Context Definition	Context definition mapping
AssetToSalesTransactionMapping	Order to Asset	SalesTransaction Context Definition	SalesTransaction Context Definition	Context definition mapping
SalesTransactionToAssetMapping	Amend, Renew, Cancel	SalesTransaction Context Definition	SalesTransaction Context Definition	Context definition mapping
NOTE Twin mapping supports custom fields only. Standard-to-standard field mapping from Product2 to QuoteLineItem isn't supported. For a worked example of custom field twin mapping, see How to Twin Map a Custom Field from Product2 to QuoteLineItem. For details about the standard field limitation and available workarounds, see Twin Mapping Standard Fields from Product2 to QuoteLineItem Not Supported.

=== ARTICLE: ind.qocal_operators_for_advanced_filters.htm ===
---
article_id: ind.qocal_operators_for_advanced_filters.htm
title: Advanced Filter Operators
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_operators_for_advanced_filters.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_filter_line_items_with_standard_and_advanced_filters.htm
fetched_at: 2026-09-04
---

# Advanced Filter Operators

Select an operator to define how the system evaluates field values. Available operators vary by the field's data type.

DATA TYPE	SUPPORTED OPERATORS
Text (String, Email, Phone, URL)	
Equals
Not Equal
Less Than
Greater Than
Less Or Equal
Greater Or Equal
Contains
Not Contain
Starts With

Numeric (Number, Currency, Percent)	
Equals
Not Equal
Less Than
Greater Than
Less Or Equal
Greater Or Equal

Date & Time	
Equals
Not Equal
Less Than
Greater Than
Less Or Equal
Greater Or Equal

Picklist	Includes
Boolean	Equals or Not Equal

=== ARTICLE: ind.qocal_order_lifecycle_management_example.htm ===
---
article_id: ind.qocal_order_lifecycle_management_example.htm
title: Order Lifecycle States and Transitions
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_order_lifecycle_management_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_order_lifecycle_management_using_object_state_definitions.htm
fetched_at: 2026-09-04
---

# Order Lifecycle States and Transitions

Familiarize yourself with the specific states and transitions used to manage an order through its lifecycle. Use this example and the accompanying object state definitions to configure valid status changes and establish clear fulfillment milestones in your Salesforce org.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Order Lifecycle Diagram

Review these specific transition rules from the diagram.

The status changes from Submitted to Processing.
The status changes from Processing to either Fulfilled or Rejected.
The status doesn’t change from Rejected or Fulfilled.

To implement this example order lifecycle, create an object state definition and then add these object state values and object state transitions.

Object State Values

To implement this lifecycle, create an object state definition and add these values.

ORDER STATUS AND OBJECT STATE VALUE	DESCRIPTION
Draft	The order is being created.
Ready to Submit	The order is ready for submission or approval.
Submitted	The order is submitted and is ready for processing.
Processing	The order is being processed.
Rejected	The order is rejected, or there’s an error during processing.
Fulfilled	The order is fulfilled.
Object State Transitions

Define these transitions to control the movement between states.

OBJECT STATE TRANSITION NAME	FROM STATE	TO STATE
Draft_to_ReadytoSubmit	Draft	Ready to Submit
ReadytoSubmit_to_Draft	Ready to Submit	Draft
ReadytoSubmit_to_Submitted	Ready to Submit	Submitted
Submitted_to_Processing	Submitted	Processing
Processing_to_Rejected	Processing	Rejected
Processing_to_Fulfilled	Processing	Fulfilled

=== ARTICLE: ind.qocal_order_lifecycle_management_using_object_state_definitions.htm ===
---
article_id: ind.qocal_order_lifecycle_management_using_object_state_definitions.htm
title: Order Lifecycle Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_order_lifecycle_management_using_object_state_definitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_orders_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Order Lifecycle Management

Define the possible states and transitions for an order by using order lifecycle. For example, define states such as Submitted, Processing, and Fulfilled. Then specify that an order state changes from Submitted to Processing and from Processing to Fulfilled.

Control access to specific states or state transitions by using custom permissions. Define different lifecycles for different application usage types. For each application usage type, create multiple lifecycles and enter the criteria to specify which lifecycle is applicable. Use object state definitions to define order lifecycles.

Order Lifecycle States and Transitions
Familiarize yourself with the specific states and transitions used to manage an order through its lifecycle. Use this example and the accompanying object state definitions to configure valid status changes and establish clear fulfillment milestones in your Salesforce org.
Implement an Object State Definition for Order Lifecycle Management
Establish the foundation for managing an order through its lifecycle by defining object state values and valid transitions. Object state definitions help you to control the progression of orders and establish a clear fulfillment process within Revenue Management.
Create Object State Values for Order Lifecycle Management
Define the possible states for the order object to establish the stages of your order lifecycle. Ensure the name of your object state values exactly match the API names of your order status picklist values to maintain data integrity.
Create Object State Transitions for Order Lifecycle Management
Define valid status changes between states to control how an order moves through its lifecycle. For example, create a transition that moves an order from Draft to Activated.
Control Access to States and State Transitions
Create custom permissions to restrict or grant access to order states and transitions for specific user groups. Assigning these permissions ensures that only authorized agents move an order to its next supported stage in the fulfillment process.
Activate an Object State Definition
To use an object state definition, you must activate it.

=== ARTICLE: ind.qocal_order_submission_for_fulfillment.htm ===
---
article_id: ind.qocal_order_submission_for_fulfillment.htm
title: Order Submission to Dynamic Revenue Orchestrator
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_order_submission_for_fulfillment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_orders_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Order Submission to Dynamic Revenue Orchestrator

Submit sales transactions to Dynamic Revenue Orchestrator (DRO) for fulfillment by using the Submit Sales Transaction invocable action in flows or Apex classes. Automating this process via record-triggered flows makes sure that all eligible records enter the fulfillment pipeline immediately upon meeting specified criteria. Customizing order page layouts to include Orchestration Plan and Orchestration Submission Status fields provides users with real-time visibility into the fulfillment progress.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Assetization Rules for Dynamic Revenue Orchestrator
Use Asset Lifecycle Management to create and activate multiple asset-based orders (ABOs) for the same asset across different sales transactions or orders. Maintaining precise assetization rules makes sure that the system applies changes sequentially and prevents data conflicts during the fulfillment process.
Example: Automate Order Submission for Fulfillment
Create a record-triggered flow to submit Revenue Management orders to Dynamic Revenue Orchestrator automatically when users activate the orders. Automation makes sure that all eligible records enter the fulfillment pipeline immediately upon meeting specified status criteria.
SEE ALSO
Customize Page Layouts with the Enhanced Page Layout Editor
Initiate Fulfillment Process of any Sales Transaction

=== ARTICLE: ind.qocal_permissions_for_quote_and_order_capture.htm ===
---
article_id: ind.qocal_permissions_for_quote_and_order_capture.htm
title: Personas and Permissions Sets for Transaction Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_permissions_for_quote_and_order_capture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Personas and Permissions Sets for Transaction Management

Transaction Management offers specific permission sets for different users involved in creating and managing sales transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
IMPORTANT Assign permission sets to users before they create quotes or orders. If a user creates a quote without the required permissions, the system permanently assigns a non-Revenue Management pricing type to the quote. Adding the correct permissions after creating the quote doesn't change the pricing type. The user must create a new quote after receiving the correct permissions.
Create Users and Profiles

To begin, create users for Transaction Management. Then assign users the appropriate permission sets. To help you plan, refer to the Transaction Management Personas table.

When you create a user, you must also assign a profile. Profiles define default settings for users. Some organizations create their own profiles, while others choose to use profiles included with Salesforce.

Remember, users can have only one profile, but can have many permission sets assigned to them.

Transaction Management Personas

Multiple users who work in various capacities within an organization can use and manage Transaction Management.

PERSONA	DESCRIPTION
Transaction Management Admin	

The admins perform these tasks.

Enable Quote and Order Capture.
Customize page layouts.
Customize components in Lightning App Builder.
Enable features.

Sales Rep	Sales reps browse catalogs, create quotes, and place orders.
Sales Operations Rep	Sales operations reps assetize orders and amend, renew, and cancel orders using Asset Lifecycle Management.
NOTE Non-admin users may encounter a FieldUndefined error (RelatedRevenueTransactionErrorLogs) when accessing quote line items. For troubleshooting steps, see Non-Admin Users Error Accessing Quote Line Items.
Transaction Management Permission Sets and Licenses

Manage sales transactions easily and securely by using permission sets that use the Revenue Cloud User permission set license. Permissions are added so that specific user personas can complete the work for their role.

The Revenue Cloud User permission set license provides access to product configuration, quotes, orders, and asset lifecycle management.

PERMISSION SET	QUOTE AND ORDER CAPTURE ADMIN	SALES REP	SALESFORCE OPERATIONS REP
Assetize Order	—	—	Yes
CalculatePrices API	Yes	Yes	Yes
CalculateTaxes API	—	Yes	Yes
Create Orders from Quotes	—	Yes	Yes
CreateContract API	—	Yes	Yes
InitiateAmendment API	—	—	Yes
InitiateCancellation API	—	—	Yes
InitiateRenewal API	—	—	Yes
PlaceOrder API	—	Yes	Yes
Price and Tax Calculation for Quoting	—	Yes	—
ProductAndPriceConfiguration API	Yes	Yes	Yes
ProductImport API	Yes	Yes	Yes
Document Builder User	Yes	Yes	Yes

=== ARTICLE: ind.qocal_product_browsing_experience_customization.htm ===
---
article_id: ind.qocal_product_browsing_experience_customization.htm
title: Product Discovery Lightning Components
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_product_browsing_experience_customization.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.product_catalog_product_discovery.htm
fetched_at: 2026-09-04
---

# Product Discovery Lightning Components

Product Discovery provides Product List, Product Details, Product Bundle Details, and Product Attribute Details components that you can add to pages on supported Salesforce Lightning Apps and Experience Cloud sites. To provide easy access to these components, some Salesforce Apps also use a tailored version of these components.

REQUIRED EDITIONS
View supported products and editions.
Product Discovery Lightning Components
COMPONENT	DESCRIPTION	SUPPORTED PAGES
Product List	Shows products, product categories, product eligibility, and pricing. Users can search and filter products.	Catalog
Product Details	Shows product images, price, and description. Users can select a buying option, select quantity, and configure and add products.	Product
Product Bundle Details Component	Shows products in a bundle along with their quantity and pricing information.	Product
Product Attribute Details Component	Shows product attributes. Users can specify attribute values.	Product

Some apps also use tailored versions of Product Discovery components. For example, in the Revenue Lifecycle Management app, the View Catalogs quick action on account record pages and the Browse Catalogs quick action on quote and order use tailored versions of these components.

Considerations When Adding Product Discovery Components

In Salesforce Lightning Service Console, you can add Product Discovery components only to the supported pages. In Experience Cloud sites, you can add these components to any page.

In Salesforce Lightning Service Console, you can add Product Discovery components only to supported end user apps. For example, you can add components to the Revenue Management app.
In console apps, when your users click the View Catalogs quick action on account pages to open a catalog page, the account ID is passed to the catalog page. Product Discovery considers this account information to determine the eligibility of the products shown on the catalog page. However, in standard apps, the account ID isn’t passed to the catalog page. See How Are Console Apps Different from Standard Apps?
SEE ALSO
Create and Configure Lightning Experience Record Pages
Locate the Unique ID of a Record in Salesforce

=== ARTICLE: ind.qocal_product_discovery_setup.htm ===
---
article_id: ind.qocal_product_discovery_setup.htm
title: Product Discovery Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_product_discovery_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Product Discovery Setup

To populate the information that users see when they use Product Discovery, select a context definition, and if necessary, select a qualification procedure and a pricing procedure.

REQUIRED EDITIONS
View supported products and editions.

To set up product discovery, follow all the instructions in each of these sections. To keep track of your progress, bookmark this page for easy reference.

Configure Product Discovery Settings
Select the context definition, qualification procedure, and pricing procedure to populate the information that users see when they use Product Discovery. After you enable qualification and pricing procedures for Product Discovery, you can enable or disable them for the Product List, Product Details, or Product Bundle Details components.
Create a Procedure to Get List Prices for Product Discovery
Use the Product Discovery Pricing Procedure template to create a pricing procedure that fits your company's needs. The Pricing Procedure is used to determine and populate pricing information for Product Discovery.
Assign Product Discovery Permissions
To provide users access to Product Discovery data and components, assign the necessary permissions and data access.
Record Sharing in Product Discovery
Set up record sharing and grant all runtime users of Product Discovery read access to all child records and related object records for a given product.

=== ARTICLE: ind.qocal_product_variation_important_considerations.htm ===
---
article_id: ind.qocal_product_variation_important_considerations.htm
title: Considerations for Adding Product Variations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_product_variation_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_product_variation_use_in_transaction_management.htm
fetched_at: 2026-09-04
---

# Considerations for Adding Product Variations

Keep these considerations in mind for product variations when managing and selling assets.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Variation parent and child products don’t support dynamic attributes, but you can have a combination of variation products and configurable product line items in a sales transaction.
You can include product variations as part of static bundles, but not configurable bundles.
The Change action isn’t available on amendment, renewal, or cancellation orders.
The Change action isn’t available on bundle components.
The Change action isn’t available for ramped groups.
The Change action isn’t available on supplemental order items.
You can’t swap an asset for a variation product by using the UI. The alternative is to use the swap API.

=== ARTICLE: ind.qocal_product_variation_use_in_transaction_management.htm ===
---
article_id: ind.qocal_product_variation_use_in_transaction_management.htm
title: Add Product Variations in Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_product_variation_use_in_transaction_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_sales_transactions_rev_cloud.htm
fetched_at: 2026-09-04
---

# Add Product Variations in Quotes and Orders

Sales reps can search for and add specific product variations to a quote or order by using Browse Catalog or Quick Add. After adding a variation, such as color or size, the side panel includes its attributes. Sales reps can switch to a different variation by using the change action.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
Sales reps use of product variations in quotes and orders:	Product Catalog Management Viewer

Reference these Product Catalog Management resources to turn on the product variation feature and set up product variation records.

Turn On Product Variants
Create a Variation Attribute Set in Product Catalog Management
Create a Variation Parent
Create a Variation Product

Optionally, you can set up the Quick Add and Browse catalog search that requires that each product variation has a defined product selling model, price book entry, and category.

After your Salesforce admin completes catalog setup, sales reps can add, view, and modify product variations in their quotes and orders.

Considerations for Adding Product Variations
Keep these considerations in mind for product variations when managing and selling assets.
Add a Product Variation by Using Browse Catalog
Create or open a quote or order.
Click Browse Catalog and select a price book.
Select a variation parent product.
Click View Options to open the Product Detail Page.
Select an attribute set. For example, Color: Green, Size: 10.
Enter the quantity and click Save and Exit to create a line item on the quote or order with the selected variation.
To Quick Add a Product Variation
To add a product variation in the Sales Transaction Line Editor, use the Quick Add search bar to search for a product by name.
Variation products show in the results. Variation parents are filtered out and don’t appear.
Select the variation to add.
Confirm that the line item attributes are added by clicking the product, and review the attributes listed in the side panel’s Attributes tab. This information is read-only.
Change a Variation Product
To change a variation product on an existing quote or order, click the row-level action dropdown on the Sales Transaction Line Editor and select Change.
Select the new attribute set and save your changes.
NOTE The change action deletes the original line item and creates a new line item. New variation line items don’t have any discounts, promotions, or adjustments from the original line item carried over. Have sales reps reapply any discounts or promotions after a change action.

=== ARTICLE: ind.qocal_qli_import_considerations_custom_csv_template.htm ===
---
article_id: ind.qocal_qli_import_considerations_custom_csv_template.htm
title: Considerations for Custom CSV Template
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_qli_import_considerations_custom_csv_template.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_qli_import_custom_csv_template.htm
fetched_at: 2026-09-04
---

# Considerations for Custom CSV Template

Download and review the default CSV template headers to determine if a custom version is necessary. If you use custom templates, adhere to these requirements.

Include a unique row identifier, such as RowNumber.
Include a unique product identifier, such as ProductCode.
Include the product quantity, such as Quantity.
Include the product selling model, such as ProductSellingModelName.
Include the billing frequency when you turn on Billing.
Exclude headers for read-only or calculated fields, such as List Price and Net Unit Price.
Limit the template to 18 columns.
The Data Processing Engine definition supports 20 columns, but the Transaction Management flow adds the quoteId and quoteLineGroupId columns at run time.
Create attributes in the extended Sales Transaction context definition and map them to any custom fields added to the template.

=== ARTICLE: ind.qocal_qli_import_considerations_customize_flow.htm ===
---
article_id: ind.qocal_qli_import_considerations_customize_flow.htm
title: Considerations for Customizing the Quote Line Item Import Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_qli_import_considerations_customize_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_qli_import_extend_functionality.htm
fetched_at: 2026-09-04
---

# Considerations for Customizing the Quote Line Item Import Flow

When users select import lines, Transaction Management uses a flow to provide options for downloading a CSV template and uploading a CSV file for processing. Review these requirements and limits to customize the import flow effectively.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Custom Template Configuration

To use a static resource for a custom CSV template, modify the ComponentUploadCsvForProcessing component within the Import Quote Line Items page element.

Set the Use Static Resource for CSV File Template attribute to True.
Enter the name of the static resource in the Downloadable CSV Template Name attribute.
Clone and modify the flow to change the CSV template or other processing behaviors.
Import Limits and Variables

The flow manages specific data limits and requires certain input variables to function with Transaction Management.

Use the rowsImportLimit variable to set the maximum number of rows for a single import.
Users import up to 1000 quote line items together, even if the rowsImportLimit variable value exceeds 1000.
Users perform multiple imports until they reach the quote line item limit per quote.
The flow includes the quoteId and dataProcessingEngineDefinitionId input variables.
Transaction Management automatically passes values for these variables to the flow when a user clicks Import Quote Line Items.

After creating a custom flow, go to the Flow for Importing Quote Line Items field and select your new flow.

SEE ALSO
Automate Tasks with Flows
Transaction Management Limits

=== ARTICLE: ind.qocal_qli_import_create_custom_dpe_definition.htm ===
---
article_id: ind.qocal_qli_import_create_custom_dpe_definition.htm
title: Customize Data Processing Engine Definitions for Quote Line Item Imports
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_qli_import_create_custom_dpe_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_qli_import_extend_functionality.htm
fetched_at: 2026-09-04
---

# Customize Data Processing Engine Definitions for Quote Line Item Imports

Modify the Data Processing Engine definition if you want users to import custom fields. Transaction Management uses this definition to process quote line items after a user uploads a CSV file.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create a Data Processing Engine definition:	

Customize Application

AND

Modify All Data

Before you begin, download the existing template.
In Setup, find and select Data Processing Engine.
Click  corresponding to the Create Quote Line Items from a CSV File template and select Download.
Because the execution platform type of the definition is Core, you can’t open it in the visual definition builder tool.
Open and edit the downloaded JSON file. Adhere to these requirements during customization.
Retain the default values for the definitionRunMode, executionPlatformType, and processType fields.
Keep the Get_Related_Quote_Line_Items_Relationships_and_Attributes and Consolidate_and_Write_Quote_Line_Item_and_Its_Related_Records nodes to create default child line items for bundled products and default quote line item attributes.
Maintain the Quote Line Reference parameter in the Get_Related_Quote_Line_Items_Relationships_and_Attributes custom node and the Consolidate_and_Write_Quote_Line_Item_and_Its_Related_Records node.
Set the value of the isTemplate field to false.
Use the API name for custom field aliases and change the suffix __c to _c.
For example, use the alias SpecialInstructions_c for the SpecialInstructions__c custom field.
Use the BatchCalcJobDefinition API to upload the updated Data Processing Engine definition.
Select the updated definition in the Data Processing Engine Definition for Importing Quote Line Items field.
EXAMPLE

In this example, the definition includes specific nodes and logic for processing data.

The Get Unique Products node uses an aggregate function to count unique product codes from filtered quote line item rows.
The appended node combines quote line item rows with and without product selling models.
The Consolidate and Write Quote Line Item and its Related Records node consolidates quote line items, relationships, and attributes. It then writes them together to target objects.
Filters restrict rows based on the QuoteId input variable and identify products without selling models.
Expression fields identify blank selling models and determine default values for StartDate and SubscriptionTerm.
{
  "FullName" : "SpecialInstructions_c",
  "Metadata" : {
    "aggregates" : [ {
      "description" : "Gets a list of unique products from the quote line item rows and their count.",
      "fields" : [ {
        "aggregateFunction" : "Count",
        "alias" : "UniqueProductCodeCount",
        "sourceFieldName" : "ProductCode"
      } ],
      "groupBy" : [ "ProductCode", "QuoteId" ],
      "label" : "Get Unique Products",
      "name" : "Get_Unique_Products",
      "sourceName" : "Filter_Quote_Line_Item_Rows_by_Quote_ID"
    } ],
    "appends" : [ {
      "description" : "Combines quote line item rows that have a product selling model with those that don’t have one.",
      "isDisjointedSchema" : false,
      "label" : "Combine Quote Line Item Rows With and Without Product Selling Models",
      "name" : "Combine_Quote_Line_Item_Rows_With_and_Without_Product_Selling_Models",
      "sources" : [ "Add_Product_Fields_to_Quote_Line_Item_Rows_with_Product_Selling_Models", "Add_Product_Fields_to_Quote_Line_Item_Rows_Without_Product_Selling_Models" ]
    } ],
    "atomicWritebacks" : [ {
      "description" : "Consolidates quote line item, quote line relationship, and quote line item attribute records, and then writes all the records together to the target objects.",
      "label" : "Consolidate and Write Quote Line Item and Its Related Records",
      "name" : "Consolidate_and_Write_Quote_Line_Item_and_Its_Related_Records",
      "writebackObjectRelationships" : [ {
        "childWritebackObjectName" : "Create_Quote_Line_Item_Relationship",
        "parentWritebackObjectName" : "Create_Quote_Line_Item_Records",
        "sequenceNumber" : 1
      }, {
        "childWritebackObjectName" : "Create_Quote_Line_Attributes",
        "parentWritebackObjectName" : "Create_Quote_Line_Item_Records",
        "sequenceNumber" : 1
      } ],
      "writebackSequence" : 1
    } ],
    "customNodes" : [ {
      "description" : "Gets child line item, relationship, and attribute records for the input quote line items. It also adds QuoteLineReference values to these records. The Composite Writeback node uses these values to write the related records together.",
      "extensionName" : "GetRelatedLinesRelationshipsAndAttributes",
      "extensionNamespace" : "TransactionManagement",
      "label" : "Get Related Quote Line Items, Relationships, and Attributes",
      "name" : "Get_Related_Quote_Line_Items_Relationships_and_Attributes",
      "parameters" : [ {
        "name" : "Attribute_AttributeName",
        "value" : "Attribute_AttributeName"
      }, {
        "name" : "Attribute_AttributeValue",
        "value" : "Attribute_AttributeValue"
      }, {
        "name" : "Attribute_AttributePicklistValueId",
        "value" : "Attribute_AttributePicklistValueId"
      }, {
        "name" : "Attribute_AttributeDefinitionId",
        "value" : "Attribute_AttributeDefinitionId"
      }, {
        "name" : "Relationship_MainQuoteLineId",
        "value" : "Relationship_MainQuoteLineId"
      }, {
        "name" : "Relationship_AssociatedQuoteLineId",
        "value" : "Relationship_AssociatedQuoteLineId"
      }, {
        "name" : "Relationship_ProductRelationshipTypeId",
        "value" : "Relationship_ProductRelationshipTypeId"
      }, {
        "name" : "Relationship_AssociatedQuoteLinePricing",
        "value" : "Relationship_AssociatedQuoteLinePricing"
      }, {
        "name" : "Relationship_AssociatedQuantScaleMethod",
        "value" : "Relationship_AssociatedQuantScaleMethod"
      }, {
        "name" : "Relationship_ProductRelatedComponent",
        "value" : "Relationship_ProductRelatedComponent"
      }, {
        "name" : "RowType",
        "value" : "RowType"
      }, {
        "name" : "QuoteLineReference",
        "value" : "QuoteLineReference"
      } ],
      "sources" : [ "Add_Default_Fields_to_Quote_Line_Item_Rows" ]
    } ],
    "dataSpaceApiName" : "default",
    "datasources" : [ {
      "description" : "Gets all rows from the CSV file, which is used as a data source to create quote line item records.",
      "fields" : [ {
        "alias" : "BillingFrequency",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "BillingFrequency"
      }, {
        "alias" : "SubscriptionTerm",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "SubscriptionTerm"
      }, {
        "alias" : "StartDate",
        "dataType" : "Date",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "StartDate"
      }, {
        "alias" : "SalesPrice",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "SalesPrice"
      }, {
        "alias" : "QuoteId",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "QuoteId"
      }, {
        "alias" : "Quantity",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "Quantity"
      }, {
        "alias" : "ProductSellingModelName",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "ProductSellingModelName"
      }, {
        "alias" : "ProductName",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "ProductName"
      }, {
        "alias" : "ProductDescription",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "ProductDescription"
      }, {
        "alias" : "ProductCode",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "ProductCode"
      }, {
        "alias" : "EndDate",
        "dataType" : "Date",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "EndDate"
      }, {
        "alias" : "DiscountPercentage",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "DiscountPercentage"
      }, {
        "alias" : "DiscountAmount",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "DiscountAmount"
      }, {
        "alias" : "ServiceDate",
        "dataType" : "Date",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "ServiceDate"
      }, {
        "alias" : "RowNumber",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : true,
        "name" : "RowNumber"
      }, {
        "alias" : "QuoteLineGroupId",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "QuoteLineGroupId"
      }, {
        "alias" : "SpecialInstructions_c",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "SpecialInstructions"
      } ],
      "fileIdentifier" : "{!CSV_File_ID}",
      "fileSource" : "ContentManagement",
      "label" : "Get Quote Line Item Rows from a CSV File",
      "name" : "Get_Quote_Line_Item_Rows_from_a_CSV_File",
      "sourceName" : "Get_Quote_Line_Items_from_a_CSV_File_CSV",
      "type" : "CSV"
    }, {
      "description" : "Gets all price book entries, which are used as a data source to populate pricing information.",
      "fields" : [ {
        "alias" : "IsActive",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "IsActive"
      }, {
        "alias" : "Pricebook2Id",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "Pricebook2Id"
      }, {
        "alias" : "Id",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "Id"
      }, {
        "alias" : "Product2Id",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "Product2Id"
      }, {
        "alias" : "ProductCode",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "ProductCode"
      }, {
        "alias" : "ProductSellingModelId",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "ProductSellingModelId"
      } ],
      "label" : "Get Price Book Entries from Salesforce Object",
      "name" : "Get_Price_Book_Entries_from_Salesforce_Object",
      "sourceName" : "PricebookEntry",
      "type" : "StandardObject"
    }, {
      "description" : "Gets all product selling models, which are used as a data source to populate the method by which a product is sold.",
      "fields" : [ {
        "alias" : "ProductSellingModelId",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "Id"
      }, {
        "alias" : "ProductSellingModelName",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "Name"
      }, {
        "alias" : "SellingModelType",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "SellingModelType"
      }, {
        "alias" : "PricingTerm",
        "dataType" : "Numeric",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "PricingTerm"
      } ],
      "label" : "Get Product Selling Models from Salesforce Object",
      "name" : "Get_Product_Selling_Models_from_Salesforce_Object",
      "sourceName" : "ProductSellingModel",
      "type" : "StandardObject"
    }, {
      "description" : "Gets all quotes and their related price book IDs. Price books contain the list of products and their prices.",
      "fields" : [ {
        "alias" : "Pricebook2Id",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "Pricebook2Id"
      }, {
        "alias" : "Id",
        "dataType" : "Text",
        "displaySequence" : 1,
        "isPrimaryKey" : false,
        "name" : "Id"
      } ],
      "label" : "Get Quote and Related Price Books from Salesforce Object",
      "name" : "Get_Quote_and_Related_Price_Books_from_Salesforce_Object",
      "sourceName" : "Quote",
      "type" : "StandardObject"
    } ],
    "definitionRunMode" : "OnDemand",
    "description" : "Adds quote line items from a CSV file to a quote.",
    "doesGenAllFailedRecords" : false,
    "executionPlatformObjectType" : "None",
    "executionPlatformType" : "CORE",
    "filters" : [ {
      "criteria" : [ {
        "inputVariable" : "QuoteId",
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "QuoteId"
      } ],
      "description" : "Filters the quote line item rows where the QuoteId field value matches the Quote ID variable value.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Quote Line Item Rows by Quote ID",
      "name" : "Filter_Quote_Line_Item_Rows_by_Quote_ID",
      "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
    }, {
      "criteria" : [ {
        "inputVariable" : "QuoteId",
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "Id"
      } ],
      "description" : "Filters the quote record where the ID matches the value in the Quote ID variable.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Quote with Matching Quote ID",
      "name" : "Filter_Quote_with_Matching_Quote_ID",
      "sourceName" : "Get_Quote_and_Related_Price_Books_from_Salesforce_Object"
    }, {
      "criteria" : [ {
        "inputVariable" : "Pricebook2Id",
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "Pricebook2Id"
      } ],
      "description" : "Filters the price book record where the ID matches the value in the Price Book ID input variable.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Price Book Entries by Price Book ID",
      "name" : "Filter_Price_Book_Entries_by_Price_Book_ID",
      "sourceName" : "Get_Price_Book_Entries_from_Salesforce_Object"
    }, {
      "criteria" : [ {
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "IsProductSellingModelEmpty",
        "value" : "0"
      } ],
      "description" : "Filters quote line item rows that have a product selling model.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Quote Line Item Rows with Product Selling Models",
      "name" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models",
      "sourceName" : "Identify_Quote_Line_Item_Rows_Without_Product_Selling_Models"
    }, {
      "criteria" : [ {
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "IsProductSellingModelEmpty",
        "value" : "1"
      } ],
      "description" : "Filters quote line item rows that don’t have a product selling model.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Quote Line Item Rows without Product Selling Models",
      "name" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models",
      "sourceName" : "Identify_Quote_Line_Item_Rows_Without_Product_Selling_Models"
    }, {
      "criteria" : [ {
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "IsProductSellingModelBlank",
        "value" : "1"
      } ],
      "description" : "Filters products that don't have a product selling model.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Products Without Product Selling Model",
      "name" : "Filter_Products_Without_Product_Selling_Model",
      "sourceName" : "Identify_Products_Without_Product_Selling_Models"
    }, {
      "criteria" : [ {
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "RowType",
        "value" : "QuoteLineItem"
      } ],
      "description" : "Filters all the quote line item records.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Quote Line Item Rows",
      "name" : "Filter_Quote_Line_Item_Rows",
      "sourceName" : "Get_Related_Quote_Line_Items_Relationships_and_Attributes"
    }, {
      "criteria" : [ {
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "RowType",
        "value" : "QuoteLineRelationship"
      } ],
      "description" : "Filters all the quote line item relationship records.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Quote Line Item Relationship",
      "name" : "Filter_Quote_Line_Item_Relationship",
      "sourceName" : "Get_Related_Quote_Line_Items_Relationships_and_Attributes"
    }, {
      "criteria" : [ {
        "operator" : "Equals",
        "sequence" : 1,
        "sourceFieldName" : "RowType",
        "value" : "QuoteLineItemAttribute"
      } ],
      "description" : "Filters all the quote line item attribute records.",
      "filterCondition" : "1",
      "isDynamicFilter" : false,
      "label" : "Filter Quote Line Attributes",
      "name" : "Filter_Quote_Line_Attributes",
      "sourceName" : "Get_Related_Quote_Line_Items_Relationships_and_Attributes"
    } ],
    "isTemplate" : false,
    "joins" : [ {
      "description" : "Adds price book entry fields to the products based on the product code.",
      "fields" : [ {
        "alias" : "ProductCode_CSV",
        "sourceFieldName" : "ProductCode",
        "sourceName" : "Get_Unique_Products"
      }, {
        "alias" : "Id",
        "sourceFieldName" : "Id",
        "sourceName" : "Filter_Price_Book_Entries_by_Price_Book_ID"
      }, {
        "alias" : "IsActive",
        "sourceFieldName" : "IsActive",
        "sourceName" : "Filter_Price_Book_Entries_by_Price_Book_ID"
      }, {
        "alias" : "Pricebook2Id",
        "sourceFieldName" : "Pricebook2Id",
        "sourceName" : "Filter_Price_Book_Entries_by_Price_Book_ID"
      }, {
        "alias" : "Product2Id",
        "sourceFieldName" : "Product2Id",
        "sourceName" : "Filter_Price_Book_Entries_by_Price_Book_ID"
      }, {
        "alias" : "ProductCode",
        "sourceFieldName" : "ProductCode",
        "sourceName" : "Filter_Price_Book_Entries_by_Price_Book_ID"
      }, {
        "alias" : "ProductSellingModelId",
        "sourceFieldName" : "ProductSellingModelId",
        "sourceName" : "Filter_Price_Book_Entries_by_Price_Book_ID"
      } ],
      "joinKeys" : [ {
        "primarySourceFieldName" : "ProductCode",
        "secondarySourceFieldName" : "ProductCode"
      } ],
      "label" : "Add Price Book Entries to Products",
      "name" : "Add_Price_Book_Entries_to_Products",
      "primarySourceName" : "Get_Unique_Products",
      "secondarySourceName" : "Filter_Price_Book_Entries_by_Price_Book_ID",
      "type" : "Inner"
    }, {
      "description" : "Adds the price book ID to quote line item rows based on the quote ID.",
      "fields" : [ {
        "alias" : "DiscountAmount",
        "sourceFieldName" : "DiscountAmount",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "DiscountPercentage",
        "sourceFieldName" : "DiscountPercentage",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "EndDate",
        "sourceFieldName" : "EndDate",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "ProductCode",
        "sourceFieldName" : "ProductCode",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "ProductDescription",
        "sourceFieldName" : "ProductDescription",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "ProductName",
        "sourceFieldName" : "ProductName",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "ProductSellingModelName",
        "sourceFieldName" : "ProductSellingModelName",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "Quantity",
        "sourceFieldName" : "Quantity",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "QuoteId",
        "sourceFieldName" : "QuoteId",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "QuoteLineGroupId",
        "sourceFieldName" : "QuoteLineGroupId",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "RowNumber",
        "sourceFieldName" : "RowNumber",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "SalesPrice",
        "sourceFieldName" : "SalesPrice",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "ServiceDate",
        "sourceFieldName" : "ServiceDate",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "SpecialInstructions_c",
        "sourceFieldName" : "SpecialInstructions_c",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "StartDate",
        "sourceFieldName" : "StartDate",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "SubscriptionTerm",
        "sourceFieldName" : "SubscriptionTerm",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "BillingFrequency",
        "sourceFieldName" : "BillingFrequency",
        "sourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File"
      }, {
        "alias" : "Pricebook2Id",
        "sourceFieldName" : "Pricebook2Id",
        "sourceName" : "Filter_Quote_with_Matching_Quote_ID"
      } ],
      "joinKeys" : [ {
        "primarySourceFieldName" : "QuoteId",
        "secondarySourceFieldName" : "Id"
      } ],
      "label" : "Add Price Book ID to Quote Line Item Rows",
      "name" : "Add_Price_Book_ID_to_Quote_Line_Item_Rows",
      "primarySourceName" : "Get_Quote_Line_Item_Rows_from_a_CSV_File",
      "secondarySourceName" : "Filter_Quote_with_Matching_Quote_ID",
      "type" : "Inner"
    }, {
      "description" : "Adds product selling model fields to products based on the product selling model ID.",
      "fields" : [ {
        "alias" : "Pricebook2Id",
        "sourceFieldName" : "Pricebook2Id",
        "sourceName" : "Add_Price_Book_Entries_to_Products"
      }, {
        "alias" : "PricebookEntryId",
        "sourceFieldName" : "Id",
        "sourceName" : "Add_Price_Book_Entries_to_Products"
      }, {
        "alias" : "Product2Id",
        "sourceFieldName" : "Product2Id",
        "sourceName" : "Add_Price_Book_Entries_to_Products"
      }, {
        "alias" : "ProductCode",
        "sourceFieldName" : "ProductCode_CSV",
        "sourceName" : "Add_Price_Book_Entries_to_Products"
      }, {
        "alias" : "PricingTerm",
        "sourceFieldName" : "PricingTerm",
        "sourceName" : "Get_Product_Selling_Models_from_Salesforce_Object"
      }, {
        "alias" : "ProductSellingModelName",
        "sourceFieldName" : "ProductSellingModelName",
        "sourceName" : "Get_Product_Selling_Models_from_Salesforce_Object"
      }, {
        "alias" : "SellingModelType",
        "sourceFieldName" : "SellingModelType",
        "sourceName" : "Get_Product_Selling_Models_from_Salesforce_Object"
      } ],
      "joinKeys" : [ {
        "primarySourceFieldName" : "ProductSellingModelId",
        "secondarySourceFieldName" : "ProductSellingModelId"
      } ],
      "label" : "Add Product Selling Models to Products",
      "name" : "Add_Product_Selling_Models_to_Products",
      "primarySourceName" : "Add_Price_Book_Entries_to_Products",
      "secondarySourceName" : "Get_Product_Selling_Models_from_Salesforce_Object",
      "type" : "LeftOuter"
    }, {
      "description" : "Adds price book entry and product selling model fields to quote line item rows that have a product selling model, based on product code, price book ID, and product selling model name.",
      "fields" : [ {
        "alias" : "DiscountAmount",
        "sourceFieldName" : "DiscountAmount",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "DiscountPercentage",
        "sourceFieldName" : "DiscountPercentage",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "EndDate",
        "sourceFieldName" : "EndDate",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "ProductDescription",
        "sourceFieldName" : "ProductDescription",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "ProductName",
        "sourceFieldName" : "ProductName",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "Quantity",
        "sourceFieldName" : "Quantity",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "QuoteId",
        "sourceFieldName" : "QuoteId",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "QuoteLineGroupId",
        "sourceFieldName" : "QuoteLineGroupId",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "SalesPrice",
        "sourceFieldName" : "SalesPrice",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "ServiceDate",
        "sourceFieldName" : "ServiceDate",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "SpecialInstructions_c",
        "sourceFieldName" : "SpecialInstructions_c",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "StartDate",
        "sourceFieldName" : "StartDate",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "SubscriptionTerm",
        "sourceFieldName" : "SubscriptionTerm",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "BillingFrequency",
        "sourceFieldName" : "BillingFrequency",
        "sourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models"
      }, {
        "alias" : "PricebookEntryId",
        "sourceFieldName" : "PricebookEntryId",
        "sourceName" : "Add_Product_Selling_Models_to_Products"
      }, {
        "alias" : "PricingTerm",
        "sourceFieldName" : "PricingTerm",
        "sourceName" : "Add_Product_Selling_Models_to_Products"
      }, {
        "alias" : "Product2Id",
        "sourceFieldName" : "Product2Id",
        "sourceName" : "Add_Product_Selling_Models_to_Products"
      }, {
        "alias" : "SellingModelType",
        "sourceFieldName" : "SellingModelType",
        "sourceName" : "Add_Product_Selling_Models_to_Products"
      } ],
      "joinKeys" : [ {
        "primarySourceFieldName" : "ProductCode",
        "secondarySourceFieldName" : "ProductCode"
      }, {
        "primarySourceFieldName" : "Pricebook2Id",
        "secondarySourceFieldName" : "Pricebook2Id"
      }, {
        "primarySourceFieldName" : "ProductSellingModelName",
        "secondarySourceFieldName" : "ProductSellingModelName"
      } ],
      "label" : "Add Product Fields to Quote Line Item Rows with Product Selling Models",
      "name" : "Add_Product_Fields_to_Quote_Line_Item_Rows_with_Product_Selling_Models",
      "primarySourceName" : "Filter_Quote_Line_Item_Rows_with_Product_Selling_Models",
      "secondarySourceName" : "Add_Product_Selling_Models_to_Products",
      "type" : "LeftOuter"
    }, {
      "description" : "Adds price book entry and product selling model fields to quote line item rows that don’t have a product selling model, based on product code, price book ID, and product selling model name.",
      "fields" : [ {
        "alias" : "DiscountAmount",
        "sourceFieldName" : "DiscountAmount",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "DiscountPercentage",
        "sourceFieldName" : "DiscountPercentage",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "EndDate",
        "sourceFieldName" : "EndDate",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "ProductDescription",
        "sourceFieldName" : "ProductDescription",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "ProductName",
        "sourceFieldName" : "ProductName",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "Quantity",
        "sourceFieldName" : "Quantity",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "QuoteId",
        "sourceFieldName" : "QuoteId",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "QuoteLineGroupId",
        "sourceFieldName" : "QuoteLineGroupId",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "SalesPrice",
        "sourceFieldName" : "SalesPrice",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "ServiceDate",
        "sourceFieldName" : "ServiceDate",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "SpecialInstructions_c",
        "sourceFieldName" : "SpecialInstructions_c",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "StartDate",
        "sourceFieldName" : "StartDate",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "SubscriptionTerm",
        "sourceFieldName" : "SubscriptionTerm",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "BillingFrequency",
        "sourceFieldName" : "BillingFrequency",
        "sourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models"
      }, {
        "alias" : "PricebookEntryId",
        "sourceFieldName" : "PricebookEntryId",
        "sourceName" : "Filter_Products_Without_Product_Selling_Model"
      }, {
        "alias" : "PricingTerm",
        "sourceFieldName" : "PricingTerm",
        "sourceName" : "Filter_Products_Without_Product_Selling_Model"
      }, {
        "alias" : "Product2Id",
        "sourceFieldName" : "Product2Id",
        "sourceName" : "Filter_Products_Without_Product_Selling_Model"
      }, {
        "alias" : "SellingModelType",
        "sourceFieldName" : "SellingModelType",
        "sourceName" : "Filter_Products_Without_Product_Selling_Model"
      } ],
      "joinKeys" : [ {
        "primarySourceFieldName" : "ProductCode",
        "secondarySourceFieldName" : "ProductCode"
      }, {
        "primarySourceFieldName" : "Pricebook2Id",
        "secondarySourceFieldName" : "Pricebook2Id"
      } ],
      "label" : "Add Product Fields to Quote Line Item Rows Without Product Selling Models",
      "name" : "Add_Product_Fields_to_Quote_Line_Item_Rows_Without_Product_Selling_Models",
      "primarySourceName" : "Filter_Quote_Line_Item_Rows_Without_Product_Selling_Models",
      "secondarySourceName" : "Filter_Products_Without_Product_Selling_Model",
      "type" : "LeftOuter"
    } ],
    "label" : "SpecialInstructions_c",
    "parameters" : [ {
      "dataType" : "FileIdentifier",
      "description" : "The ID of the CSV file that contains the quote line item rows that must be processed to create records.",
      "isMultiValue" : false,
      "label" : "CSV File ID",
      "name" : "CSV_File_ID"
    }, {
      "dataType" : "Text",
      "description" : "The ID of the quote for which quote line items must be created.",
      "isMultiValue" : false,
      "label" : "Quote ID",
      "name" : "QuoteId"
    }, {
      "dataType" : "Text",
      "description" : "The ID of the price book associated with the quote to which the quote line items must be added.",
      "isMultiValue" : false,
      "label" : "Price Book ID",
      "name" : "Pricebook2Id"
    } ],
    "processType" : "RevenueTransactionManagement",
    "status" : "Active",
    "transforms" : [ {
      "name" : "Identify_Quote_Line_Item_Rows_Without_Product_Selling_Models",
      "sourceName" : "Add_Price_Book_ID_to_Quote_Line_Item_Rows",
      "label" : "Identify Quote Line Item Rows without Product Selling Models",
      "transformationType" : "Expression",
      "partitionBy" : [ ],
      "orderBy" : [ ],
      "expressionFields" : [ {
        "alias" : "IsProductSellingModelEmpty",
        "expression" : "IF(ISBLANK({ProductSellingModelName} ),1,0)",
        "dataType" : "Numeric",
        "length" : 1,
        "decimalPlaces" : 0
      } ],
      "droppedFields" : [ ]
    }, {
      "name" : "Identify_Products_Without_Product_Selling_Models",
      "sourceName" : "Add_Product_Selling_Models_to_Products",
      "label" : "Identify Products Without Product Selling Models",
      "transformationType" : "Expression",
      "partitionBy" : [ ],
      "orderBy" : [ ],
      "expressionFields" : [ {
        "alias" : "IsProductSellingModelBlank",
        "expression" : "IF(ISBLANK({ProductSellingModelName} ),1,0)",
        "dataType" : "Numeric",
        "length" : 1,
        "decimalPlaces" : 0
      } ],
      "droppedFields" : [ ]
    }, {
      "name" : "Add_Default_Fields_to_Quote_Line_Item_Rows",
      "sourceName" : "Combine_Quote_Line_Item_Rows_With_and_Without_Product_Selling_Models",
      "label" : "Add Default Fields to Quote Line Item Rows",
      "transformationType" : "Expression",
      "partitionBy" : [ ],
      "orderBy" : [ ],
      "expressionFields" : [ {
        "alias" : "DefaultPeriodBoundary",
        "expression" : "IF({SellingModelType} == \"TermDefined\" || {SellingModelType} == \"Evergreen\",\"Anniversary\",NULL)",
        "dataType" : "Text",
        "length" : 100
      }, {
        "alias" : "DefaultStartDate",
        "expression" : "IF({SellingModelType} == \"OneTime\",{StartDate},IF({SellingModelType} == \"TermDefined\" &&  ISBLANK({StartDate}),TODAY(),IF({SellingModelType} == \"Evergreen\" &&  ISBLANK({StartDate}),TODAY(),{StartDate})))",
        "dataType" : "Date"
      }, {
        "alias" : "DefaultSubscriptionTerm",
        "expression" : "IF({SellingModelType} == \"OneTime\" || {SellingModelType} == \"Evergreen\",{SubscriptionTerm},IF({SellingModelType} == \"TermDefined\" && ISBLANK({SubscriptionTerm}),IF(ISBLANK({EndDate}),TEXT(FLOOR({PricingTerm})),{SubscriptionTerm}),{SubscriptionTerm}))",
        "dataType" : "Text",
        "length" : 100
      } ],
      "droppedFields" : [ ]
    } ],
    "writebacks" : [ {
      "name" : "Create_Quote_Line_Item_Records",
      "label" : "Create Quote Line Item Records",
      "sourceName" : "Filter_Quote_Line_Item_Rows",
      "targetObjectName" : "QuoteLineItem",
      "writebackRecordMaxLimit" : 0,
      "isChangedRow" : false,
      "shouldCreateTargetObject" : false,
      "isExistingDataset" : false,
      "description" : "Creates quote line item records for all the rows in the CSV file, including their child line items.",
      "canWrtbckToNonEditableFields" : false,
      "storageType" : "sObject",
      "operationType" : "Insert",
      "writebackSequence" : 1,
      "fields" : [ {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "PricebookEntryId",
        "targetFieldName" : "PricebookEntryId"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Product2Id",
        "targetFieldName" : "Product2Id"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Quantity",
        "targetFieldName" : "Quantity"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "QuoteId",
        "targetFieldName" : "QuoteId"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "DiscountAmount",
        "targetFieldName" : "DiscountAmount"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "DiscountPercentage",
        "targetFieldName" : "Discount"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "DefaultStartDate",
        "targetFieldName" : "StartDate"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "DefaultPeriodBoundary",
        "targetFieldName" : "PeriodBoundary"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "DefaultSubscriptionTerm",
        "targetFieldName" : "SubscriptionTerm"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "EndDate",
        "targetFieldName" : "EndDate"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "ProductDescription",
        "targetFieldName" : "Description"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "ProductName",
        "targetFieldName" : "CustomProductName"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "SalesPrice",
        "targetFieldName" : "UnitPrice"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "ServiceDate",
        "targetFieldName" : "ServiceDate"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "QuoteLineGroupId",
        "targetFieldName" : "QuoteLineGroupId"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "BillingFrequency",
        "targetFieldName" : "BillingFrequency"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "SpecialInstructions_c",
        "targetFieldName" : "SpecialInstructions__c"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "QuoteLineReference",
        "targetFieldName" : "QuoteLineReference"
      } ]
    }, {
      "name" : "Create_Quote_Line_Item_Relationship",
      "label" : "Create Quote Line Item Relationship",
      "sourceName" : "Filter_Quote_Line_Item_Relationship",
      "targetObjectName" : "QuoteLineRelationship",
      "writebackRecordMaxLimit" : 0,
      "isChangedRow" : false,
      "shouldCreateTargetObject" : false,
      "isExistingDataset" : false,
      "description" : "Creates quote line item relationship records for all the quote line items.",
      "canWrtbckToNonEditableFields" : false,
      "storageType" : "sObject",
      "operationType" : "Insert",
      "writebackSequence" : 2,
      "fields" : [ {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Relationship_AssociatedQuoteLinePricing",
        "targetFieldName" : "AssociatedQuoteLinePricing"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Relationship_ProductRelationshipTypeId",
        "targetFieldName" : "ProductRelationshipTypeId"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Relationship_AssociatedQuantScaleMethod",
        "targetFieldName" : "AssociatedQuantScaleMethod"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Relationship_ProductRelatedComponent",
        "targetFieldName" : "ProductRelatedComponentId"
      }, {
        "isAutogenerated" : false,
        "parentName" : "QuoteLineItem",
        "relationshipName" : "MainQuoteLine",
        "runtimeParameter" : false,
        "sourceFieldName" : "Relationship_MainQuoteLineId",
        "targetFieldName" : "QuoteLineReference"
      }, {
        "isAutogenerated" : false,
        "parentName" : "QuoteLineItem",
        "relationshipName" : "AssociatedQuoteLine",
        "runtimeParameter" : false,
        "sourceFieldName" : "Relationship_AssociatedQuoteLineId",
        "targetFieldName" : "QuoteLineReference"
      } ]
    }, {
      "name" : "Create_Quote_Line_Attributes",
      "label" : "Create Quote Line Attributes",
      "sourceName" : "Filter_Quote_Line_Attributes",
      "targetObjectName" : "QuoteLineItemAttribute",
      "writebackRecordMaxLimit" : 0,
      "isChangedRow" : false,
      "shouldCreateTargetObject" : false,
      "isExistingDataset" : false,
      "description" : "Creates quote line item attribute records for all the quote line items.",
      "canWrtbckToNonEditableFields" : false,
      "storageType" : "sObject",
      "operationType" : "Insert",
      "writebackSequence" : 2,
      "fields" : [ {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Attribute_AttributeDefinitionId",
        "targetFieldName" : "AttributeDefinitionId"
      }, {
        "isAutogenerated" : false,
        "parentName" : "QuoteLineItem",
        "relationshipName" : "QuoteLineItem",
        "runtimeParameter" : false,
        "sourceFieldName" : "QuoteLineReference",
        "targetFieldName" : "QuoteLineReference"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Attribute_AttributeName",
        "targetFieldName" : "AttributeName"
      }, {
        "isAutogenerated" : false,
        "runtimeParameter" : false,
        "sourceFieldName" : "Attribute_AttributePicklistValueId",
        "targetFieldName" : "AttributePicklistValueId"
      } ]
    } ]
  }
}

=== ARTICLE: ind.qocal_qli_import_custom_csv_template.htm ===
---
article_id: ind.qocal_qli_import_custom_csv_template.htm
title: Custom CSV Templates for Quote Line Item Imports
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_qli_import_custom_csv_template.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_qli_import_extend_functionality.htm
fetched_at: 2026-09-04
---

# Custom CSV Templates for Quote Line Item Imports

Customize the import process to meet specific business needs by creating a custom CSV template. Custom templates support the addition of unique fields while maintaining the structure required for data processing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

Update the downloadable CSV template that your sales reps use to import quote line items.

Create a CSV file template containing the required headers.
Define a static resource in Setup and upload the template file.

After creating the static resource, complete these setup tasks.

Customize the Import Quote Line Items flow and specify the new static resource to make sure that users download the correct file. See Import Quote Line Items.
Customize the Data Processing Engine definition to update the processing logic for the new headers. .
Considerations for Custom CSV Template
Download and review the default CSV template headers to determine if a custom version is necessary. If you use custom templates, adhere to these requirements.

=== ARTICLE: ind.qocal_qli_import_extend_functionality.htm ===
---
article_id: ind.qocal_qli_import_extend_functionality.htm
title: Quote Line Item Import Extension
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_qli_import_extend_functionality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_line_item_import.htm
fetched_at: 2026-09-04
---

# Quote Line Item Import Extension

The default import setup supports data entry for standard, commonly used fields. Customize the import process to meet unique business requirements by adding custom fields, modifying the import flow, or changing the processing logic.

Custom CSV Templates for Quote Line Item Imports
Customize the import process to meet specific business needs by creating a custom CSV template. Custom templates support the addition of unique fields while maintaining the structure required for data processing.
Considerations for Customizing the Quote Line Item Import Flow
When users select import lines, Transaction Management uses a flow to provide options for downloading a CSV template and uploading a CSV file for processing. Review these requirements and limits to customize the import flow effectively.
Customize Data Processing Engine Definitions for Quote Line Item Imports
Modify the Data Processing Engine definition if you want users to import custom fields. Transaction Management uses this definition to process quote line items after a user uploads a CSV file.

=== ARTICLE: ind.qocal_qli_import_user_considerations.htm ===
---
article_id: ind.qocal_qli_import_user_considerations.htm
title: Considerations for Creating a CSV File
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_qli_import_user_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_qli_import_user_import_lines_csv.htm
fetched_at: 2026-09-04
---

# Considerations for Creating a CSV File

Familiarize yourself with recommendations, supported products, required fields, and limits before creating your file.

Enter values for all required fields, which include ProductCode, RowNumber, and Quantity in the default template.
Include the Billing Frequency if you turn on Billing.
Provide the ProductSellingModelName for products with product selling models.
Use unique values in the RowNumber column, though they appear in any order.
Match the values in the ProductCode and ProductSellingModelName columns to the values defined in Revenue Management.
Use unique values in the ProductName column to identify rows if they fail to process.
Make sure that all associated products have product codes before attempting an import.
Import only the root product to add a bundle product. Manually configure child products after the import finishes.
Import the source product in the CSV file or ensure it exists in the quote to import a product that uses derived pricing.
Refrain from importing usage-based products as they lack support.
Import static product bundles and products with static attributes only after an admin configures the Data Processing Engine definition to populate related default records.
Add quote line items to initial and amendment quotes.
Avoid importing quote line items to renewal and cancellation quotes.
Limit the CSV file to 1,000 rows, ensuring the total number of lines created doesn’t exceed 1,000.
Import multiple files until you reach the quote line item limit per quote.
Verify that the imported line items add to the first group if your quote contains groups.
Use only comma-delimited CSV files that meet all readiness criteria. For more information, see CSV File Readiness.
IMPORTANT The error logs exclude ProductCode and RowNumber columns. If you import both root and child products of a bundle via CSV, the system adds them as separate products.

=== ARTICLE: ind.qocal_qli_import_user_import_lines_csv.htm ===
---
article_id: ind.qocal_qli_import_user_import_lines_csv.htm
title: Import Quote Line Items from a CSV File
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_qli_import_user_import_lines_csv.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_line_item_import.htm
fetched_at: 2026-09-04
---

# Import Quote Line Items from a CSV File

Create quotes faster by importing quote line items from CSV files. After the import completes, configure the products and view the prices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To download the CSV template file and import quote line items:	Advanced CSV Data Import permission set

To import quote line items, download the CSV template, add your data, and upload the file to your quote record.

Open a quote record page.
Click Import Lines.
Click Download CSV Template to receive a template containing headers.
Add quote line items to the downloaded template.
Click Upload Files.
Browse and select your file, and then click Open.
Click Import.
If the process completes or fails, receive a notification.
If the import fails, access Revenue Transaction Error Log records from the related list on the quote to identify and fix issues.
Configure quote line items and make any other necessary changes to the quote after a successful import.
If the file upload doesn't complete and the Done button remains disabled, see Understanding "Query Non Vetoed Files" Permission and File Access.
WARNING Transaction Management suspends all actions on the quote while the import is in progress.
Considerations for Creating a CSV File
Familiarize yourself with recommendations, supported products, required fields, and limits before creating your file.

=== ARTICLE: ind.qocal_quote_and_order_capture.htm ===
---
article_id: ind.qocal_quote_and_order_capture.htm
title: Manage Sales Transactions in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_quote_and_order_capture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
fetched_at: 2026-09-04
---

# Manage Sales Transactions in Revenue Management

Transaction Management is a core component of Salesforce Revenue Management (formerly Revenue Cloud) that streamlines and automates the entire sales process, from quoting to order capture.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.

Empower sales reps to efficiently create and manage all types of sales—including initial, renewal, and amendment—while simplifying the subscription lifecycle. By integrating with tools for product configuration, pricing, and fulfillment, Transaction Management ensures accuracy and reduces manual effort. This results in a more efficient sales cycle, improved pricing accuracy, and an enhanced customer experience.

From a business perspective, the key benefit is the optimization of revenue operations. By automating the end-to-end quote-to-cash process, Transaction Management helps ensure revenue compliance and maximizes the potential of every deal. This creates a single, reliable source of truth for all sales transactions, giving businesses greater insight and control over their revenue streams.

Begin Using Transaction Management
Transaction Management simplifies subscription lifecycles while ensuring the integrity of all sales transactions. You can tailor the Revenue Management (formerly Revenue Cloud) experience by using permission sets and setup instructions to give each user precise access to the features they need.
Transaction Management Features
Manage common Transaction Management features across all sales transaction records for your business. Review these configurations to unify pricing, tax, and currency settings across your organization.
Quotes and Orders in the Revenue Management
Quotes serve as preliminary offers to propose products, services, and their pricing to customers. Sales representatives and partners create and revise multiple quotes before finalizing an order. Orders establish a formal agreement between the business and the customer by detailing the specific products, services, and pricing.
Sell Usage-Based Products
Sell products that are billed based on the consumption. When you create quotes and orders, you can view, edit, and reprice the rates, commitments, and grants for resources included in the usage-based products to fit your deal.
Contracts in Revenue Management
Use contracts in Revenue Management (formerly Revenue Cloud) to organize and manage customer assets, products, and services throughout their lifecycle.
Manage Asset Lifecycle in Revenue Management
Track purchased products and services to provide excellent support and build your business relationships. Amend assets to meet changing customer needs, renew them for uninterrupted service, and cancel assets that you no longer require.

=== ARTICLE: ind.qocal_quote_einstein_summary.htm ===
---
article_id: ind.qocal_quote_einstein_summary.htm
title: Set Up Quote Summaries
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_quote_einstein_summary.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_einstein_gen_ai_assisted_quote_creation.htm
fetched_at: 2026-09-04
---

# Set Up Quote Summaries

Set up Einstein Generative AI and configure quote page layouts to provide sales reps with digestible quote overviews. By using customer data, Einstein summarizes records so reps quickly see the current state of a deal, customer, or prospect for approval.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with Transaction Management and Einstein for Sales add-on
Set up Einstein Generative AI to access generative AI features.
Enable Prompt Builder to create prompt templates for drafting personalized summaries.
Assign the required permission sets to your users.
Assign the required permission sets to your users.
Prompt Template Manager
Prompt Template User
Einstein Sales Summaries User
Enable Prompt Builder.
Add the Einstein Summary component to the quote page layout. To learn how to configure record pages, see Create and Configure Lightning Experience Record Pages.
Click the Einstein Summary component to edit its properties.
Select the Record Summary prompt template type. Select the Summarize Quote prompt template. Save your changes.
Select the Summarize Quote prompt template. Save your changes.
Select the Summarize Quote prompt template. Save your changes.

After you save your changes, verify the quote summary availability.

The Quote Summary component appears on quote pages.
Your users can generate overviews of quotes that use the prompt templates.

=== ARTICLE: ind.qocal_quote_emails.htm ===
---
article_id: ind.qocal_quote_emails.htm
title: Set Up Quote Emails
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_quote_emails.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_einstein_gen_ai_assisted_quote_creation.htm
fetched_at: 2026-09-04
---

# Set Up Quote Emails

Use Einstein to help your sales reps draft emails to share quote proposals with their customers.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with Transaction Management and Einstein for Sales add-on
Set Up Einstein Generative AI to access generative AI features such as Prompt Builder.
To create prompt templates for drafting personalized emails for your quote, enable Prompt Builder, and assign Prompt Template Manager and Prompt Template User permission sets to relevant users.
See Create a Sales Email Prompt Template.
Set Up Sales Emails and assign the Einstein Sales Emails permission set to your sales reps.

When your users click  on quote pages, they will see the Draft with Einstein button. They can use this button to generate personalized email content. If necessary, they can revise the content before sending the emails.

=== ARTICLE: ind.qocal_quote_line_item_import.htm ===
---
article_id: ind.qocal_quote_line_item_import.htm
title: Quote Line Item Imports
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_quote_line_item_import.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_features.htm
fetched_at: 2026-09-04
---

# Quote Line Item Imports

Importing quote line items from a CSV file accelerates the quoting process by eliminating manual data entry for large volumes of products. Revenue Management uses Transaction Management components to process these imports, ensuring data consistency across multiple product types and currency models.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

The import process relies on specific templates and automated flows to handle data.

The CSV template provides standardized headers for common fields, such as ProductCode, ProductName, and ProductSellingModelName.
The import flow manages the user experience and facilitates CSV template downloads and file uploads for processing.
Data Processing Engine definition templates provide the necessary backend support for both multicurrency and single-currency organizations.

The import functionality supports standard quote line items and accommodates custom requirements. Salesforce admins extend the default behavior to include custom fields, ensuring the import meets unique business needs.

Set Up Quote Line Items Import
Turn on the Import Quote Line Items setting and create a Data Processing Engine definition to perform bulk quote creation from CSV files.
Quote Line Item Import Extension
The default import setup supports data entry for standard, commonly used fields. Customize the import process to meet unique business requirements by adding custom fields, modifying the import flow, or changing the processing logic.
Import Quote Line Items from a CSV File
Create quotes faster by importing quote line items from CSV files. After the import completes, configure the products and view the prices.

=== ARTICLE: ind.qocal_quote_management_lifecyle.htm ===
---
article_id: ind.qocal_quote_management_lifecyle.htm
title: Quote Management Lifecyle
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_quote_management_lifecyle.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_features.htm
fetched_at: 2026-09-04
---

# Quote Management Lifecyle

Sales representatives use quotes as preliminary offers to propose products and pricing to customers. This lifecycle involves discovering products, entering quote details, and managing revisions before converting a final proposal into an order.

Quote synchronization automates the connection between quote line items and products in the related opportunity. Because opportunities lack support for bundles and attributes, the system transfers these elements as separate line items or one-time products. This automated update process maintains data alignment until a user terminates the link.

Create a Quote
Discover and price products for your customers by creating quotes directly in Revenue Cloud. These records help you organize product selections and apply pricing logic before finalizing a transaction.
Considerations for Syncing Quotes and Opportunities
Get to know the data differences between quotes and opportunities before you sync quote line items to an opportunity. These differences determine how the quote to opportunity sync handles bundle products, attributes, and term-defined items. Review these behaviors to ensure data consistency between your quotes and related opportunities.

=== ARTICLE: ind.qocal_quote_to_contract_flow.htm ===
---
article_id: ind.qocal_quote_to_contract_flow.htm
title: Map a Flow to Capture Quote Line Pricing on Contracts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_quote_to_contract_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_contract_features.htm
fetched_at: 2026-09-04
---

# Map a Flow to Capture Quote Line Pricing on Contracts

Configure a flow to generate contracts from quotes automatically, helping sales reps to capture negotiated prices and discounts as contract item prices. This automation simplifies the contract lifecycle by giving users the choice to include quote line details or create a contract without specific pricing records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To open, edit, or create a flow in Flow Builder:	Manage Flow
To use Contract Pricing:	Salesforce Pricing Design Time User

Contracts created from quotes include contract item price records generated from quote line items. Conversely, the system doesn’t create contract item price records from order products when you generate a contract from an order.

From Setup, search for and select Revenue Settings.
In Set Up Flow for Creating Contracts from Quotes section, enter rev_contracts__CreateCntrFromQuote and save your changes.
Admins can customize this automation by entering a different flow API name and saving.
When users click the New Contract button, select one of the options.
Capture net unit prices or discounts of quote line items as contract item prices.
Create a contract without capturing any contract-based prices or discounts.

=== ARTICLE: ind.qocal_quotes_and_orders_in_the_revenue_cloud.htm ===
---
article_id: ind.qocal_quotes_and_orders_in_the_revenue_cloud.htm
title: Quotes and Orders in the Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_quotes_and_orders_in_the_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Quotes and Orders in the Revenue Management

Quotes serve as preliminary offers to propose products, services, and their pricing to customers. Sales representatives and partners create and revise multiple quotes before finalizing an order. Orders establish a formal agreement between the business and the customer by detailing the specific products, services, and pricing.

NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.

Revenue Management (formerly Revenue Cloud) provides tools for sales representatives, partners, and customers to manage these transactions efficiently. Both quotes and orders use shared functionalities, such as transaction management components and advanced pricing features.

Foundational Setup for Quotes and Orders
Execute these configuration procedures to optimize quote and order performance within Salesforce Revenue Management (formerly Revenue Cloud). Prioritize the setup of the Transaction Line Editor, refine all pricing logic, and stabilize API invocation protocols to ensure seamless system integration.
Quote to Opportunity Sync Support
Sync quotes with up to 15,000 line items to opportunities asynchronously to maintain performance. Background processing keeps sales reps working without interruption.
Manage Orders in Revenue Management
Orders signify a formal agreement between your business and the customer, detailing the products, services, and pricing. Learn how to create and manage orders effectively.
View and Edit Quotes in Revenue Management
Use the Transaction Line Editor or Sales Transaction Line Editor to add, configure, and price quotes in Revenue Management (formerly Revenue Cloud). These editors provide a centralized workspace to manage product selections, apply discounts, and verify pricing details before final submission.
View and Edit Orders in Revenue Management
The order page lists product and pricing details. Use this workspace to add, remove, and manage products within your transactions.
Negotiate Price Uplifts for Subscription Renewals
Apply renewal price uplifts to subscriptions, including adjustments based on the Consumer Price Index (CPI). Sales reps negotiate renewal price uplifts during the initial sale and modify uplift percentages on assets and line items during renewals to ensure accurate pricing and maintain data integrity.

=== ARTICLE: ind.qocal_ramp_deal_compound_uplift.htm ===
---
article_id: ind.qocal_ramp_deal_compound_uplift.htm
title: Set Up Ramp Deals with Standard or Compound Price Uplifts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deal_compound_uplift.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.setting_up_ramp_deals.htm
fetched_at: 2026-09-04
---

# Set Up Ramp Deals with Standard or Compound Price Uplifts

Salesforce admins configure either standard or compound price uplifts for ramp schedule groups so sales reps can quote multi-year deals. The uplift type selection determines a flat annual increase or an increase that builds on the prior segment's net price. Compound uplifts match how many enterprise customers negotiate multi-year contracts. They keep pricing transparent for approvers and remove the manual steps that lead to quoting errors and forecast drift.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To configure the default Ramp Uplift Type in Revenue Settings:	Customize Application
To set the Ramp Uplift Type on quote line groups:	Create on Quotes
To set the Ramp Uplift Type on order product groups:	Create on Orders

From Setup, in the Quick Find box, enter Revenue Settings, and select Revenue Settings. Then, turn on Advanced Detail Line Pricing. Set the default Ramp Uplift Type to standard or compound uplift.

Compound uplift calculations require this preference. If Advanced Detail Line Pricing is off, Salesforce doesn't show the compound option in the Ramp Uplift Type picklist or in the Default Ramp Uplift Type setting.

While in Revenue Settings, also turn on Ramp Deals for Groups in Quotes and Orders. The Ramp Uplift Type applies to group-based ramp deals. Set the Default Ramp Uplift Type to standard or compound. New ramp schedules inherit this default, but sales reps can override it at the ramp schedule group level.

Standard: Each segment's uplift applies to the original list price.
Compound: Each segment's uplift builds on the net price of the prior segment.

The prebuilt Revenue Management Default Pricing Procedure doesn't update automatically. If you use the prebuilt template, clone the latest template to apply the updates.

Follow Use Advanced Transaction Detail Line Pricing to Map Custom Fields and add another map line item mapping ItemApplUnitPriceUpliftPct__std to itemDetailApplUnitPriceUpliftPct__std to the prebuilt template.

From Setup, select Object Manager. Search for and select the quote or order object. Click Lightning Record Pages, then the quote or order record page. Click Edit to open Lightning App Builder. Select the Sales Transaction Line Editor (STLE) component to add the Ramp Uplift Type field to the quote line group and order product group. Add the Applied Unit Price Uplift field to the quote line item and the order product.

Synch the context definition before using compound uplift.

=== ARTICLE: ind.qocal_ramp_deal_compound_uplift_sales_reps.htm ===
---
article_id: ind.qocal_ramp_deal_compound_uplift_sales_reps.htm
title: Create Ramp Deals with Standard or Compound Price Uplifts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deal_compound_uplift_sales_reps.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_for_groups_considerations.htm
fetched_at: 2026-09-04
---

# Create Ramp Deals with Standard or Compound Price Uplifts

Ramp deals break a multi-year contract into segments so that price, quantity, and terms can change over the life of the deal. Standard uplifts apply to the original list price, which works well for predictable contracts. However, many enterprise customers negotiate agreements where the annual increase applies to the prior year's net price rather than the list price. Compound uplifts reflect the growing value of a subscription over time and are common in multi-year contracts.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
For sales reps to use Ramp Uplift Type:	

Price and Tax Calculation for Quoting and Manage Revenue Lifecycle Management permissions

AND

Create Orders from Quotes permission set

Without compound uplift, sales reps calculate compounded prices in spreadsheets. Deal desk analysts can't easily audit the math, and a risk for finance teams is that they forecast the deal at the wrong contract value. With compound uplift, Salesforce automates the calculation, sets the applied unit price uplift for each segment, and preserves the uplift type in amendments and renewals. As a result, Sales reps present what they conclude is a fair, predictable price to the customer. Deal desk analysts can approve deals faster because the price waterfall shows exactly how the compounded price calculates. Sales operations managers can forecast revenue with confidence.

The ramp uplift type is set at the ramp schedule group level. When a sales rep changes the type on a ramp schedule group, the new type propagates to every group segment and ramped line item, repricing the transaction.

To select standard or compound uplift for a ramp deal, sales reps complete these steps.

Open the quote or order in Sales Transaction Line Editor (STLE).
Add a ramp schedule group and its segments, or open an existing ramp schedule group.
The new ramp schedule group inherits the default ramp uplift type from Revenue Settings.
Click the ramp schedule group name to open the side panel.
Set Ramp Uplift Type to Standard or Compound.
Set this value on the parent ramp schedule group only. For individual segments and line items, the ramp uplift type is read-only. If Multiple Ramp Schedules Per Transaction is off, set the type on the single ramp schedule segment. In both cases, Transaction Management cascades the change to every ramped line in the schedule.
Enter the Unite Price Uplift % for each segment.
The first segment always acts as the baseline. Segments with a zero percent uplift or with no uplift entered react the same way. The prior segment's cumulative multiplier carries over and no new uplift applies.
Save your changes.
Transaction Management applies the ramp uplift type on every ramped segment and line item, and Native Global Pricing (NGP) reprices the transaction. For a compound ramp schedule, NGP reprices every line in the group because each segment's price depends on the segment before it. For a standard schedule, only the segments that you change reprice. NGP populates the applied unit price uplift on each line item with the effective percentage used to calculate the net price. Confirm the values in the price waterfall.
EXAMPLE

Compare Standard and Compound Uplifts.

Consider a 3-year ramp deal with a $50.00 list price and a 10% annual uplift. These tables show how the two modes produce different prices.

Standard Uplift

SEGMENT	LIST PRICE	SEGMENT UPLIFT %	NET UNIT PRICE
Year 1	$50.00	0%	$50.00
Year 2	$50.00	10%	$55.00
Year 3	$50.00	10%	$55.00

Compound Uplift

SEGMENT	LIST PRICE	SEGMENT UPLIFT %	CUMULATIVE MULTIPLIER CALCULATION	APPLIED UNIT UPLIFT %	NET UNIT PRICE
Year 1	$50.00	0%	Baseline (1.0000)	0%	$50.00
Year 2	$50.00	10%	1.0000 × 1.10 = 1.1000	10%	$55.00
Year 3	$50.00	10%	1.1000 × 1.10 = 1.2100	21%	$60.50

In standard mode, Year 3 yields $55.00. In compound mode, Year 3 yields $60.50. The 21% applied unit price uplift in Year 3 reflects the geometric effect of two compounded 10% uplifts: (1.10 × 1.10) − 1 = 21%.

A segment with a zero percent compound uplift is a carryover. The prior cumulative multiplier remains rather than resetting, so the segment maintains the compounded gain from earlier segments.

=== ARTICLE: ind.qocal_ramp_deal_for_groups_create.htm ===
---
article_id: ind.qocal_ramp_deal_for_groups_create.htm
title: Create a Ramp Deal for Groups with Single Ramp Schedule Per Transaction
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deal_for_groups_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_for_groups_considerations.htm
fetched_at: 2026-09-04
---

# Create a Ramp Deal for Groups with Single Ramp Schedule Per Transaction

Turn on only Ramp Deals for Groups in Quotes and Orders to treat the entire transaction automatically as a single implicit ramp schedule.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To manage ramp deals for quote line item groups:	Create on Quotes
To manage ramp deals for order product groups:	Create on Orders
Open a quote or order and click Add Group.
Click the group name to open the side panel.
Enter start and end dates. For a Yearly segment type, set the duration to exactly 365 days.
Turn on Is Ramped. Always use the side panel—don't use the group record page.
Select a segment type as Yearly (exactly 365 days for all segments, fixed) or Custom (flexible duration).
Save your changes.
Transaction Management creates a ramp schedule and converts the group into the first segment.
To add subsequent segments, click Show more actions on the last segment and select Clone Segment.
Use Edit Ramp Schedule on an initial sale quote or an amended quote to rename segments, adjust dates, and change segment types.

=== ARTICLE: ind.qocal_ramp_deal_for_groups_manage.htm ===
---
article_id: ind.qocal_ramp_deal_for_groups_manage.htm
title: Manage a Ramp Deal
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deal_for_groups_manage.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm
fetched_at: 2026-09-04
---

# Manage a Ramp Deal

After you create a group ramp schedule, use these actions to manage segments and lines.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
ACTION	LEVEL	WHAT IT DOES	SUPPORTED QUOTES OR RAMP SCHEDULES
Browse Catalogs	Segment	Adds products into the current segment or all subsequent ramp schedule group segments. If you use Browse Catalogs at the quote or order level instead, products are added only to the first group as non-ramped lines.	All quote types and ramp schedules.
Clone Segment	Segment	Creates the next segment by copying lines and updating the start and end dates for the new segment. You can copy only the ramped lines or all the lines.	
Initial Sale Ramp Deal
Auto-generated ramp schedule on Amendment and Renewal Quotes

Delete Segment	Segment	Deletes a segment and all its lines. Only available at the start or end of a schedule. You can't use the Bulk Delete option on a quote or order that contains a group ramp schedule.	
Initial Sale Ramp Deal
Newly cloned segment on auto-generated ramp schedule on Amendment and Renewal Quotes

Remove from Schedule	Segment	Removes a segment from the schedule and converts its lines to non-ramped lines. Only available at the start or end of a schedule.	New ramp schedule segments
Edit Ramp Schedule	Schedule or Segment	Shows options to edit the names, start dates, and end dates of segments. If you change a segment's start and end dates, Transaction Management automatically updates the dates of all the line items within the segment. Available at the segment level when only Ramp Deals for Groups in Quotes and Orders is turned on. Available at the schedule level when both Ramp Deals for Groups in Quotes and Orders and Multiple Ramp Schedules Per Transaction are turned on.	New ramp schedule segments.
View Past Segments	Schedule	Shows a summary of segments that are in the past. Available for auto-generated asset ramp schedules in amendments created after enabling Multiple Ramp Schedules Per Transaction.	Auto-generated ramp schedule on Amendment Quotes.
View Ramp Details	Line	

Shows a summary of a ramped line, including its quantity, price, and dates across all the segments it's part of.

Available only for ramped line items.

	This ramp action is only available on ramped lines for all quote types.
Delete	Line	Deletes a line item and all its related ramped line items in subsequent segments. If you add the same product back to a ramp segment, the product is treated as a separate line and a new asset is created for it.	
New ramp schedule lines
Auto-generated ramp schedule lines on all quote types.

=== ARTICLE: ind.qocal_ramp_deals_asset_considerations.htm ===
---
article_id: ind.qocal_ramp_deals_asset_considerations.htm
title: Ramp Deal Structure for Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deals_asset_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.understanding_ramp_deals.htm
fetched_at: 2026-09-04
---

# Ramp Deal Structure for Groups

Ramp deals contain time-bounded segments with distinct pricing, quantities, and discounts. The active structural mode dictates how you organize them.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
Single-Level Structure (Default)

When only Ramp Deals for Groups in Quotes and Orders setting is turned on, the entire transaction is one implicit ramp schedule. Segments appear as a flat list of groups in the quote or order.

Quote or Order
└── Segment 1 (Group, Is Ramped = true)
└── Segment 2 (cloned from Segment 1)
└── Segment 3 (cloned from Segment 2)

This structure is the simpler of the two modes and works well when a deal has a single product set that ramps uniformly over time.

Two-Level Nested Structure

When the Multiple Ramp Schedules Per Transaction setting is also turned on, the quote or order supports up to 10 independent ramp schedules. Each schedule is a top-level Ramp Schedule Group, and its segments are subgroups nested within it.

Quote or Order
├── Ramp Schedule Group A
│   ├── Segment 1 (Subgroup)
│   ├── Segment 2 (Subgroup)
│   └── Segment 3 (Subgroup)
└── Ramp Schedule Group B
    ├── Segment 1 (Subgroup)
    └── Segment 2 (Subgroup)

Use this structure when different product sets in the same deal ramp on different timelines—for example, a software subscription that scales annually alongside a professional services package that ramps quarterly.

Key Objects
OBJECT	ROLE
Ramp Schedule Group	Top-level container for a ramp schedule (two-level mode only).
Segment (Group or Subgroup)	A single time period with its own pricing, quantity, and discount.
Quote Line Item / Order Product	A product line assigned to one or more segments.
Structure to Use
SCENARIO	RECOMMENDED STRUCTURE
Single product set, uniform ramp	Single-level
Multiple product sets with different ramp timelines	Two-level nested
Early renewal generating an auto-structured quote	Determined by the Multiple Ramp Schedules Per Transaction setting
NOTE All segments in a ramp schedule must share the same segment type. You can't combine Yearly and Custom segments in one schedule. The segment type you select for the first segment sets the type for the entire schedule.

To change it later, use Edit Ramp Schedule window to convert the whole schedule from Yearly to Custom, or from Custom to Yearly.

=== ARTICLE: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm ===
---
article_id: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm
title: Ramp Deals in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deals_complex_long_term_multiple_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
fetched_at: 2026-09-04
---

# Ramp Deals in Revenue Management

Use ramp deals for groups to break down a long-term deal into smaller time-based segments, each with different products, quantities, discounts, and price uplifts.

NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.
Understanding Ramp Deals
A ramp deal is a long-term sales agreement where price, quantity, and discounts vary across defined time periods called segments. Instead of quoting a flat rate across the entire contract, you break the deal into multiple segments—each with its own pricing, quantities, and discounts. This gives your customers clear, upfront visibility into how costs evolve over the life of the contract.
Set Up Ramp Deals
Prepare your system settings, clone required flows, update page layouts, and configure product segments to deploy the full ramp deal experience for sales reps.
Build Ramp Deals
Learn how to build structured ramp deals for your groups based on your organization's administrative settings. Depending on your configuration, you can use a single global schedule per transaction or build multiple custom schedules.
Add Products to a Ramp Deal
After creating the ramp structure, add products to segments.
Manage a Ramp Deal
After you create a group ramp schedule, use these actions to manage segments and lines.
Ramp Deals for Usage Products
Use ramp deals for groups for usage products to break down a long-term deal into smaller time-based segments.
Early Renewal of Ramped Assets
You can renew one or more ramped assets before their scheduled end date to lock in pricing, consolidate contracts, or restructure a large upsell. Early renewal generates cancellation credits for the uncharged portion of the terminated segments and produces a new system-generated ramp structure on the renewal quote.
Decompose and Fulfill Ramp Deal Orders
Use Dynamic Revenue Orchestrator (DRO) to decompose, orchestrate, and assetize ramp deal orders across time segments. DRO sequences fulfillment steps, creates fulfillment assets, and processes amendments based on each segment's effective dates and values. A ramp deal contains standalone order line items divided into time segments whose price, quantity, discount, and other attributes can vary.
Ramp Deals for Groups Examples
Explore the following examples to see how ramp deals scale from basic, single-schedule configurations to advanced, multi-schedule scenarios.
Considerations for Ramp Deals
Review these known considerations and limitations for the Ramp Deals feature.

=== ARTICLE: ind.qocal_ramp_deals_for_groups_considerations.htm ===
---
article_id: ind.qocal_ramp_deals_for_groups_considerations.htm
title: Build Ramp Deals
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deals_for_groups_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm
fetched_at: 2026-09-04
---

# Build Ramp Deals

Learn how to build structured ramp deals for your groups based on your organization's administrative settings. Depending on your configuration, you can use a single global schedule per transaction or build multiple custom schedules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Create a Ramp Deal for Groups with Single Ramp Schedule Per Transaction
Turn on only Ramp Deals for Groups in Quotes and Orders to treat the entire transaction automatically as a single implicit ramp schedule.
Create Ramp Deals for Groups with Multiple Ramp Schedules Per Transaction
If your admin turned on the Multiple Ramp Schedules Per Transaction setting, create a ramp schedule for each ramp deal.
Create Ramp Deals with Standard or Compound Price Uplifts
Ramp deals break a multi-year contract into segments so that price, quantity, and terms can change over the life of the deal. Standard uplifts apply to the original list price, which works well for predictable contracts. However, many enterprise customers negotiate agreements where the annual increase applies to the prior year's net price rather than the list price. Compound uplifts reflect the growing value of a subscription over time and are common in multi-year contracts.
Use the Create Ramp Schedule Guided Flow
The Create Ramp Schedule guided flow generates a full multi-segment deal structure in one step.

=== ARTICLE: ind.qocal_ramp_deals_for_groups_transition.htm ===
---
article_id: ind.qocal_ramp_deals_for_groups_transition.htm
title: Ramp Deals for Lines vs. Ramp Deals for Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deals_for_groups_transition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.understanding_ramp_deals.htm
fetched_at: 2026-09-04
---

# Ramp Deals for Lines vs. Ramp Deals for Groups

There are two types of ramp deals in Revenue Management - Ramp Deals for Lines and Ramp Deals for Groups.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
Ramp Deals for Groups

Apply ramp segments at the group level, covering all eligible products within a group together. This is the recommended approach for new implementations. All subscription products that meet the requirements are eligible by default — no per-product configuration in Product Catalog Management is needed. To provide trials at no additional cost with ramp deals for groups, sales reps apply a 100% manual discount to segments at the group or line level.

Ramp deals for groups offer several advantages over ramp deals for lines:

Supports bundle products. Configuration changes made to a ramp segment automatically propagate to that segment and all subsequent segments.
Supports usage products. You can specify different rates across ramp segments.
Supports unit price uplifts per segment for precise, transparent pricing.
Shows segments in quote documents, making it easier to collaborate with customers.
Supports amending ramped assets to adjust prices and change field values.
Supports trial and pro-rated segments.
Available on Experience Cloud sites.

If you're currently using ramp deals for lines, Salesforce recommends transitioning to ramp deals for groups. You can run both approaches in parallel during migration, but you can't mix them in the same quote or order.

Ramp Deals for Lines

Apply ramp segments at the individual transaction line level. A subscription-based product appears as a single quote line item divided into segments, each with its own price, quantity, and discount. To use this approach, admins configure product ramp segments in Product Catalog Management — only products explicitly set up with ramp segments are eligible. To provide trials at no additional cost with ramp deals for lines, you create product segments with the Free Trial segment type.

IMPORTANT Salesforce recommends that you use Ramp Deals for Groups only.

=== ARTICLE: ind.qocal_ramp_deals_for_groups_transition_steps.htm ===
---
article_id: ind.qocal_ramp_deals_for_groups_transition_steps.htm
title: Transition from Ramp Deals for Lines to Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deals_for_groups_transition_steps.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.understanding_ramp_deals.htm
fetched_at: 2026-09-04
---

# Transition from Ramp Deals for Lines to Groups

If you're moving from ramp deals for lines to ramp deals for groups, follow these steps.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To turn off Ramp Deals for Lines in Quotes and Orders:	Customize Application
To turn on Ramp Deals for Groups in Quotes and Orders:	Customize Application
Before transitioning, delete ramped lines from all in-progress quotes and orders.
In Revenue Settings, turn on Ramp Deals for Groups in Quotes and Orders.
Work with your users to recreate ramp deals for the deleted lines that use the groups' approach.
Update all in-progress transactions, then turn off Ramp Deals for Lines in Quotes and Orders.

By default, you can amend assets originally created for ramp deals for lines by using the capabilities provided by ramp deals for groups.

=== ARTICLE: ind.qocal_ramp_deals_groups_create_multiple_ramp_schedules.htm ===
---
article_id: ind.qocal_ramp_deals_groups_create_multiple_ramp_schedules.htm
title: Create Ramp Deals for Groups with Multiple Ramp Schedules Per Transaction
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_deals_groups_create_multiple_ramp_schedules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_for_groups_considerations.htm
fetched_at: 2026-09-04
---

# Create Ramp Deals for Groups with Multiple Ramp Schedules Per Transaction

If your admin turned on the Multiple Ramp Schedules Per Transaction setting, create a ramp schedule for each ramp deal.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To manage ramp deals for quote line item groups:	Create on Quotes
To manage ramp deals for order product groups:	Create on Orders
Open a quote or order and click Add Group.
Save your changes. Click the group name to open the side panel.
In the side panel, set Quote Line Group Type to Ramp Schedule Group. Save your changes.
Click Show more actions on the schedule, then click Add Sub Group to create the first segment.
Save your changes, then click the subgroup name to open the side panel.
Enter start and end dates and turn on Is Ramped.
Select a segment type.
You can't edit the segment type later.
Save your changes.
To add subsequent segments, click Show more actions on the last segment and select Clone Segment.
Use Edit Ramp Schedule at the schedule level to manage names and dates.

=== ARTICLE: ind.qocal_ramp_schedule_with_trial_and_proration_segments.htm ===
---
article_id: ind.qocal_ramp_schedule_with_trial_and_proration_segments.htm
title: Use the Create Ramp Schedule Guided Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_ramp_schedule_with_trial_and_proration_segments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_ramp_deals_for_groups_considerations.htm
fetched_at: 2026-09-04
---

# Use the Create Ramp Schedule Guided Flow

The Create Ramp Schedule guided flow generates a full multi-segment deal structure in one step.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To create a ramp schedule:	

Create and Edit on QuoteLineGroup

AND

Sales rep persona


To open, edit, or create a flow in Flow Builder:	Manage Flow
Open a quote or order.
In the Sales Transaction Line Editor actions dropdown list, select Create Ramp Schedule.
Select the schedule type.
Annual: Generates 12-month segments. The minimum total duration is 12 months.
Custom: Divides total duration into a specified number of equal-length segments.
Annual and custom segment types can't coexist in the same schedule.
Optionally add a trial segment.
A trial segment is a fixed-duration trial period (in days or months) prepended before the main schedule. Trial duration is additive—it doesn't count toward the main schedule duration.
Optionally specify a prorated segment position (first or last) for cases where the total duration doesn't divide evenly into full periods. A ramp schedule can contain only one trial segment (as the first segment) and one prorated segment (as the first or last segment).
Review the generated segments, and revise the details as needed.
Edit dates. Changing the first segment's start date updates the Ramp Schedule Start Date. You can only change the start date for an annual or trial segment. You can edit the start and end dates for a custom segment.
Edit discounts and uplifts.
Before generating the ramp schedule, verify:
There are no errors, gaps, or overlapping segments.
The schedule has no more than 12 segments, excluding the trial segment.
Segment dates are contiguous—each segment starts exactly 1 day after the previous segment ends.
Click Create.
EXAMPLE
Annual Ramp with a Trial Segment
Number	Segment Name	Type	Duration	Start Date	End Date
1	Trial	TRIAL	45 Days	Oct 01, 2025	Nov 14, 2025
2	Year 1	ANNUAL	12 months	Nov 15, 2025	Nov 14, 2026
3	Year 2	ANNUAL	12 months	Nov 15, 2026	Nov 14, 2027
4	Year 3	ANNUAL	12 months	Nov 15, 2027	Nov 14, 2028
Annual Ramp with a Prorated Segment
Number	Segment Name	Type	Duration	Start Date	End Date
1	Year 1 - Prorated	PRORATED	4 months	Oct 01, 2025	Jan 31, 2026
2	Year 1	ANNUAL	12 months	Feb 01, 2026	Jan 31, 2027
3	Year 2	ANNUAL	12 months	Feb 01, 2027	Jan 31, 2028
4	Year 3	ANNUAL	12 months	Feb 01, 2028	Jan 31, 2029
Annual Ramp with Trial and Prorated Segments
Number	Segment Name	Type	Duration	Start Date	End Date
1	Trial	TRIAL	30 days	Oct 01, 2025	Oct 30, 2025
2	Year 1	ANNUAL	12 months	Oct 31, 2025	Oct 30, 2026
3	Year 2	ANNUAL	12 months	Oct 31, 2026	Oct 30, 2027
4	Year 3 - Prorated	PRORATED	1 month	Oct 31, 2027	Nov 29, 2027

After creating the ramp schedule, keep in mind:

To add products to any segment, use Browse Catalog from within the segment group. Products inherit the segment's Discount Percent and Uplift Percent.
To modify an existing schedule's dates or segment types after creation, use Edit Ramp Schedule. The Create Ramp Schedule flow only creates new, empty ramp schedule structures—it doesn't modify existing ramp schedules.
You can't clone a prorated segment. To extend a schedule that ends with a prorated segment, clone the last standard segment instead. The process automatically moves the prorated segment's dates forward.

=== ARTICLE: ind.qocal_renew_assets.htm ===
---
article_id: ind.qocal_renew_assets.htm
title: Renew Assets with the Managed Asset Viewer
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_renew_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_general_procedures.htm
fetched_at: 2026-09-04
---

# Renew Assets with the Managed Asset Viewer

To optimize revenue and manage products efficiently, use the asset lifecycle renewal action. The Managed Asset viewer on your Account or Contract page initiates these renewals directly within the asset lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To renew assets:	

InitiateRenewal API permission set

AND

Sales Rep persona permissions

Prerequisites

Before you begin:

Add the Managed Asset Viewer component to your preferred page layouts, such as the Account page layout.
Add the Assets related list to the Account page for the Managed Assets list to appear.
To complete asset renewals in Managed Assets, add the component to the Contract page layout.
NOTE When the Create Quotes Without a Related Opportunity setting is true, select whether to create a related opportunity. If the setting is false or undefined, the system creates an opportunity for the renewal quote. However, when you use the Contract page layout, the system adds the contract number to the renewal quote or order automatically. See Enable Quote Creation Without a Related Opportunity.
Renew Assets
From the App Launcher, find, and select Accounts.
Click an account name in the Accounts list view.
Under Managed Assets, select the checkbox in the Asset Name column for the asset that you want to update. For bundled assets, select the parent asset instead of the child asset.
Select Renew and confirm the renewal if prompted.
The quote or order inherits the renewal term and unit from the asset or the associated contract. Defining these values prevents errors.
Transaction Management copies the asset attribute values to line item attribute values.
Deactivating a product attribute in the catalog doesn’t affect existing attributes.
Update the fields for renewal.
Add assets to the renewal quote if needed.
Review your renewal request and save your changes.
Asset Renewal Scenarios and Requirements

Review how the system handles renewal data based on the original purchase method to avoid validation errors during the renewal process.

Asset created without a contract
When the system creates an asset from a New Sale order without a contract, it copies the renewal term and unit from the order item’s pricing fields. If these values are present, the system marks the asset as renewal-ready, but if they’re missing, it creates the asset without renewal details. During a later renewal attempt via the Contract or Account Asset Viewer, the system verifies these values. If they’re missing, it blocks the renewal and shows an error. To resolve this issue, update the asset with the required values in the viewer and resubmit the renewal.
Asset created with a contract
For assets created from a New Sale order with a contract header, the system leaves the asset's renewal fields blank to derive them from the contract instead. When you initiate a renewal from the Contract Asset Viewer, the system reads values directly from the associated contract and proceeds if they’re valid. However, if both the asset and the contract lack these values, or if you initiate renewal from the Account Asset Viewer where no contract is passed, the system returns a validation error. In these cases, update the asset record with the required information to unblock the renewal.
Future-date assets
Future-dated assets on a contract include an Asset Contract Relationship (ACR), and Salesforce blocks renewals if it can’t find a current ACR to copy. To resolve this error, update the Renewal Term and Renewal Term Unit in the Managed Asset Viewer on the Account page. After you provide these values, you can proceed with the renewal. After completing the renewal, delete related opportunity line items to improve forecasting accuracy, unless your admin has automated renewals via a renewal opportunity flow.

=== ARTICLE: ind.qocal_renew_expired_assets.htm ===
---
article_id: ind.qocal_renew_expired_assets.htm
title: Renew Expired Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_renew_expired_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_specialized_transaction_types.htm
fetched_at: 2026-09-04
---

# Renew Expired Assets

To maintain customer relationships and close deals faster, renew assets and subscriptions after their original end date. Enabling late renewals and trial extensions provides flexibility when customers want to repurchase products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To renew expired assets:	

InitiateRenewal API permission set

AND

Sales Rep persona permissions

You can change the asset start date even if the subscription renewal date occurs after the subscription end date. The renewal term's start date falls on or after the lifecycle end date. If a gap exists between the asset expiration date and the new renewal start date, the system updates the asset with a new asset state period of zero quantity.

NOTE Renewal of expired usage-based assets is only available in orgs with Revenue Cloud Advanced license. If you have an org with both Revenue Cloud Advanced and Revenue Cloud Billing licenses, or you add the Revenue Cloud Billing license later, then you can’t renew expired usage-based assets.
In the App Launcher, search for and select Accounts.
From the Assets tab of an account's page, select the asset you want to review.
Select Renew.
To select a new renewal term start date, on the Set Renewal Term prompt, select Override Renewal Term and a date.
To save your changes, click Submit.

=== ARTICLE: ind.qocal_renew_expired_usage_based_assets.htm ===
---
article_id: ind.qocal_renew_expired_usage_based_assets.htm
title: Renew Expired Usage-Based Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_renew_expired_usage_based_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_amending_rates_and_grants_on_usage_based_products.htm
fetched_at: 2026-09-04
---

# Renew Expired Usage-Based Assets

Continue a customer's subscription after a usage-based asset expires by setting a new renewal term and negotiating rates and grants.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To renew expired usage-based assets:	InitiateRenewal API permission set AND Sales Rep persona permissions
NOTE Renewal of expired usage-based assets is available in orgs with the Revenue Cloud Advanced license. If an org has the Revenue Cloud Advanced and Revenue Cloud Billing licenses, or if the Revenue Cloud Billing license is added later, you can't renew expired usage-based assets.

Confirm that the asset expired at the end of its term. A canceled asset isn't eligible for renewal.

When a customer wants to continue a usage-based product after its subscription ends, renew the expired asset instead of creating a new one. The renewal start date must be on or after the asset's lifecycle end date. It can be in the past, today, or in the future. No grace period applies when renewing an expired usage-based asset.

If a gap exists between the asset's lifecycle end date and the renewal start date, a zero-quantity Asset State Period is added for the gap.

NOTE When you renew an expired ramp usage-based asset, the renewed asset is non-ramped. Creating new ramp segments during late renewal isn't supported.

To renew assets through the Managed Asset Viewer, see Renew Assets with the Managed Asset Viewer.

From the App Launcher, find and select Accounts.
Select the customer's account, and then select the Assets tab.
Select the expired usage-based asset that you want to renew.
Select Renew.
On the Set Renewal Term prompt, select Override Renewal Term, and then enter a Renewal Term Start Date.

Set a date on or after the asset's lifecycle end date. Selecting a renewal start date overrides the existing subscription renewal term.

To save your changes, click Submit.

The renewal quote opens for the asset.

Review and negotiate the rates and grants for the new term, and then finalize the quote.

The renewed term begins on the renewal start date. The asset's usage entitlements and rate cards are updated for the new term.

No usage records are associated with zero-quantity Asset State Periods during gap periods. Consumption or rating of usage during a gap period isn't supported.

EXAMPLE

A customer's usage-based subscription ended on March 31, and the customer signs a new deal on May 15. You select the expired asset, click Renew, click Override Renewal Term, and then set the renewal start date to May 15. Because the renewal starts after the asset's lifecycle end date, a zero-quantity Asset State Period is added for the gap between the lifecycle end date and the renewal start date. The renewed term begins on May 15.

For rate and grant negotiation on usage-based products, see Usage-Based Assets.

=== ARTICLE: ind.qocal_renew_usage_based_assets_early.htm ===
---
article_id: ind.qocal_renew_usage_based_assets_early.htm
title: Renew Usage-Based Assets Early
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_renew_usage_based_assets_early.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_amending_rates_and_grants_on_usage_based_products.htm
fetched_at: 2026-09-04
---

# Renew Usage-Based Assets Early

Change pricing on an active usage-based asset before the asset's end date by setting a new renewal term and negotiating rates and grants.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
For early renewal of usage-based assets:	InitiateRenewal API permission set AND Sales Rep persona permissions
NOTE Early renewal of usage-based assets is available in orgs with the Revenue Cloud Advanced license. If an org has the Revenue Cloud Advanced and Revenue Cloud Billing licenses, or if the Revenue Cloud Billing license is added later, you can't renew usage-based assets early.

Confirm that the asset is active and uses a term-defined product selling model. Early renewal is available for assets that use the Anchor, Pack, and Commitment usage models, but not for assets that use the one-time or evergreen product selling model.

Early renewal replaces an active asset's current term with a new term instead of creating a new asset. The renewal start date must be in the future and on or before the asset's end date. Early renewal ends the current term on the day before the renewal start date and begins the renewed term on the renewal start date.

You can renew a single asset from the account's Assets tab or renew multiple assets from the Managed Asset Viewer. To renew assets through the Managed Asset Viewer, see Renew Assets with the Managed Asset Viewer.

From the App Launcher, find and select Accounts.
Select the customer's account, and then select the Assets tab.
Select the active usage-based asset that you want to renew.
Select Renew.
On the Set Renewal Term prompt, select Override Renewal Term, and then enter a Renewal Term Start Date and a Renewal Term End Date.

Set a start date in the future, on or before the asset's end date. Set an end date on or after the renewal term start date. Selecting a renewal term start date overrides the existing subscription renewal term.

To save your changes, click Submit.

The renewal quote opens for the asset.

Review and negotiate the rates and grants for the new term, and then finalize the quote.
Activate the renewal order to create the renewed asset.

The current term ends and the renewed term begins on the renewal start date. The asset's usage entitlements and rate cards are updated for the new term.

EXAMPLE

A customer's usage-based subscription runs from January 1, 2026, through December 31, 2026. On April 1, 2026, you renew the asset early to apply new rates. You select the active asset, select Renew, select Override Renewal Term, and then set the renewal start date to April 1, 2026. The current term ends on March 31, 2026, and the renewed term runs from April 1, 2026, through March 31, 2027.

For rate and grant negotiation on usage-based products, see Usage-Based Assets.

To renew a usage-based asset after its term ends, see Renew Expired Usage-Based Assets.

=== ARTICLE: ind.qocal_renewal_of_a_usage_based_product.htm ===
---
article_id: ind.qocal_renewal_of_a_usage_based_product.htm
title: Proration for Usage Amendments and Cancellations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_renewal_of_a_usage_based_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_amending_rates_and_grants_on_usage_based_products.htm
fetched_at: 2026-09-04
---

# Proration for Usage Amendments and Cancellations

Understand how the system recalculates grants when you change quantities or cancel services early.

Grant Recalculation

When a line item quantity changes, the system automatically recalculates and prorates grants based on the asset's lifecycle. View the proration message and the net-applicable grants in the Manage Usage Resources window.

Early Cancellations

Cancel usage resources early to ensure that the system prorates grants based on the asset's actual lifecycle. The system counts consumption until the date of cancellation and reduces it by the number of prorated grants.

Calculation Logic

Consider an asset with an initial count of 10 units and 100 grants per unit. During a mid-month amendment, the quantity increases by 5 units, and the new grant is 200 per unit.

QUANTITY	RATE	CALCULATION


Current Month (Prorated)

10 existing units + 5 new units

	100 grants/unit (existing) + 200 grants/unit (new)	(10 x 100) + (5 x 200 / 2) = 1500 grants


Next Month (Full)

10 existing units + 5 new units

	100 grants/unit (existing) + 200 grants/unit (new)	(10 x 100) + (5 x 200) = 2000 grants (full)

For more information, refer to these resources.

Renew Assets with the Managed Asset Viewer
Cancel Assets with the Managed Asset Viewer

=== ARTICLE: ind.qocal_renewal_price_uplifts.htm ===
---
article_id: ind.qocal_renewal_price_uplifts.htm
title: Negotiate Price Uplifts for Subscription Renewals
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_renewal_price_uplifts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quotes_and_orders_in_the_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Negotiate Price Uplifts for Subscription Renewals

Apply renewal price uplifts to subscriptions, including adjustments based on the Consumer Price Index (CPI). Sales reps negotiate renewal price uplifts during the initial sale and modify uplift percentages on assets and line items during renewals to ensure accurate pricing and maintain data integrity.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create price uplifts:	

Manage Revenue Management

AND

Create Orders from Quotes

AND

Renew Assets

AND

Sales Rep permission group

IMPORTANT Review these requirements before applying uplifts to your records.
Renewal price uplifts apply only to products with a term-defined product selling model.
The pricing procedure includes the uplift as a calculation by using the Formula-Based Pricing element.
Ensure accurate pricing by applying uplifts after discounts when you use Last Transaction Pricing.
Set the asset's Pricing Source to Last Transaction Pricing before adding the asset to a new quote or order and selecting an uplift percentage.

Modify uplift percentages on items and verify the results on the generated renewal record.

Specify the uplift percentage for the unit price in a quote line item or an order item.
Save your changes.
Select Create Order and activate the order to assetize it.
Review the asset to verify the applied unit price uplift.
Generating a renewal quote applies the negotiated price uplift.
Create and activate a new order from the renewal quote that includes the unit price uplift.
View unit price uplift details in the waterfall by hovering over the Net Unit Price field.
CPI and Renewal Price Uplift Considerations
Familiarize yourself with the supported product types, field behaviors, and system logic for applying Consumer Price Index (CPI) and renewal price uplifts. Understanding these constraints ensures accurate pricing calculations during asset renewal and helps you determine where uplift data appears in the price waterfall.

=== ARTICLE: ind.qocal_reprice_all_quotes_and_orders.htm ===
---
article_id: ind.qocal_reprice_all_quotes_and_orders.htm
title: Reprice All for Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_reprice_all_quotes_and_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Reprice All for Quotes and Orders

Refresh and validate prices across an entire transaction by recalculating all quote or order lines.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

The Reprice All action performs a full repricing of every transaction line, even when no changes exist. This action always runs a full recalculation, regardless of whether you turn on Delta Pricing.

The Reprice All action refreshes only pricing and skips configuration, so product configuration rules are not re-evaluated. To refresh prices and product configurations, use the Refresh Prices action instead.

Repricing Scenarios
The Transaction Processing Type (TPT) skipped pricing during the record commitment process.
Validation errors prevented a successful pricing run.
Discounts, adjustments, or bundle configurations require a refresh.
Estimated taxes need calculation (requires the Add Estimated Tax to Quotes and Orders setting in Revenue Settings).
Button Accessibility

Access the Reprice All button within the Transaction Line Editor or the Sales Transaction Line Editor. If the button isn’t visible, use the Lightning App Builder to add it to the interface. See Configure Action Buttons in Transaction Line Editor.

Accuracy in Usage-Based Quotes

Salesforce maintains the connection between quote line items and usage data through system-generated resource grants. System-generated grants ensure accurate resource quantity negotiations and successful record commitments.

Protect quote data integrity by following these guidelines.

Avoid manual deletion of usage resource grants for quote line items.
Acknowledge that manual deletion breaks resource links, which causes record commitment failures and locked resources.
Restore accidentally deleted grants by clicking Reprice All to rebuild the records.
Contact your Salesforce admin or Customer Support if repricing fails to restore data consistency.

=== ARTICLE: ind.qocal_rollback_important_considerations.htm ===
---
article_id: ind.qocal_rollback_important_considerations.htm
title: Transaction Rollbacks Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_rollback_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Transaction Rollbacks Considerations

Understand the requirements and limitations of the rollback feature to reverse the most recent transaction on an asset. Familiarizing yourself with these rules ensures data integrity and helps you determine when a transaction is eligible for reversal.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Rollback Eligibility and Usage

Review these critical constraints and behaviors before initiating a rollback.

Timing Restrictions: You only roll back future-dated transactions that haven’t started. If the start date occurred in the past or occurs today, the system prohibits rolling back the last transaction.
Bundle Constraints: Rollback rules apply to child products within a bundle. If renewal or amendment of any child product has started, you can’t roll back the entire bundle transaction.
Transaction Scope: The system doesn’t support the partial rollback of a transaction.
Legacy Data: You can’t roll back assets created before the Salesforce Winter '26 release.
Sequence of Actions: The rollback action always applies to the most recent or last transaction. You can perform multiple rollbacks to undo transactions sequentially. After you roll back the last transaction, you can then roll back the next most recent transaction.
Action Restrictions: You can’t roll back a rollback transaction.
Unsupported Transaction Types: The system doesn’t support the rollback of initial sales, cancellations, or transfer transactions.
Feature Incompatibility: The system doesn’t support rollbacks for asset transactions involving ramps, usage-based products, or Dynamic Revenue Orchestration features.

=== ARTICLE: ind.qocal_rollback_last_transaction_on_asset.htm ===
---
article_id: ind.qocal_rollback_last_transaction_on_asset.htm
title: Roll Back the Last Transaction for an Asset
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_rollback_last_transaction_on_asset.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_advanced_amendment_and_renewal_features.htm
fetched_at: 2026-09-04
---

# Roll Back the Last Transaction for an Asset

To reverse the most recent future-dated amendment or renewal due to errors or changes in customer plans, use the Rollback feature. This action restores the asset to its original state, eliminating the need for complicated manual workarounds.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To roll back the last transaction for an asset:	InitiateAmend user permission

The Rollback feature reverts an asset to its previous state by creating a counteracting transaction. It preserves a complete history of all transactions to ensure data integrity through a ledger-style approach.

For example, if you renew a subscription but require a quantity adjustment first, roll back the renewal, amend the quantity, and then process the corrected renewal.

Go to the Accounts or Contracts page containing the asset.
On the Assets tab, in the Managed Asset Viewer, select the asset for the transaction reversal.
Select Rollback.
The rollback process generates a new quote or order to reverse the previous transaction. You can't edit the transaction lines on this new record to perform another complete reversal.
Activate the generated rollback quote or order.
A new quote or order appears with an Amend action type and a Rollback subtype.
Your asset returns to its state before the rolled-back transaction.
Asset Action, Asset Action Source, and Asset State Period records update automatically to reflect the reversal. .
A new asset action provides a Rolledback Asset Action lookup link to the original reversed action.

Review the asset history to confirm the rollback processed correctly. Check the asset action related to the asset for a new record with type Amend and subtype Rollback. Verify that this record points to the reversed asset action and that the asset state matches its condition before the rollback transaction.

=== ARTICLE: ind.qocal_sales_transactions_rev_cloud.htm ===
---
article_id: ind.qocal_sales_transactions_rev_cloud.htm
title: Manage Quote and Order Lifecycle Actions
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_sales_transactions_rev_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
fetched_at: 2026-09-04
---

# Manage Quote and Order Lifecycle Actions

Sales representatives use specialized actions to duplicate records, adjust pricing, and apply negotiated terms to streamline the transaction lifecycle. These tools ensure consistency across proposals and help sales reps manage complex customer requirements efficiently while reducing manual entry errors.

The transaction system creates draft records by copying groups and positive-quantity line items from existing transactions. For high-level pricing changes, automated tools apply discounts or total overrides that distribute across all line items based on specified logic. When working with established customers, initiating new transactions from active contracts automatically includes pre-negotiated rates and adjustment schedules. To maintain an effective lifecycle, separate indicators monitor real-time background task progress and verify if a transaction is valid to advance to the next stage.

Clone Quotes and Orders
Duplicate quotes or orders along with their associated line items and groups to save time and ensure data consistency. Cloning reduces manual entry errors by creating an exact draft replica of a source record while leaving the original unchanged.
Apply Header Adjustments to Quotes and Orders
Provide amount and percent discounts or override the total amount for an entire quote or order. Transaction Management automatically distributes these discounts equally or proportionally among line items based on your selected distribution method. The price waterfall shows the specific discount applied to each line item to ensure pricing transparency.
Generate a Quote or Order from a Contract
Create quotes or orders from an active contract with contract-based pricing to include negotiated contract prices in your new transaction. Sales reps use existing contract-based pricing to ensure financial accuracy for specific customers.
Discover and Configure Products for Transactions
Browse catalogs, view product lists, configure products, and add items to your quotes or orders.
Add Product Variations in Quotes and Orders
Sales reps can search for and add specific product variations to a quote or order by using Browse Catalog or Quick Add. After adding a variation, such as color or size, the side panel includes its attributes. Sales reps can switch to a different variation by using the change action.
Differences Between Calculation Status Field and Validation Result Field
Map the Calculation Status field and Validation Result field to specific tasks within your pricing and orchestration engine to maintain an effective transaction lifecycle and avoid inaccurate business decisions. While both fields track transaction states, each serves a unique purpose based on your business requirements.

=== ARTICLE: ind.qocal_saving_usage_rates_for_quotes_and_orders.htm ===
---
article_id: ind.qocal_saving_usage_rates_for_quotes_and_orders.htm
title: Saving Usage Rates for Quotes and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_saving_usage_rates_for_quotes_and_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling_advanced_concepts.htm
fetched_at: 2026-09-04
---

# Saving Usage Rates for Quotes and Orders

Automatically save current usage rates by generating rate card entries when you save a quote or order. This process helps maintain rate consistency for the duration of the sale, even if the product catalog is updated later.

REQUIRED EDITIONS
NOTE To enable this feature, admins must configure the Revenue Management transaction processing type with RatingPreference set to Fetch. Automatic rate capture does not trigger if you use a different transaction processing type.
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
How Rate Capture Works

To support rate stability, Revenue Management saves usage rates at the beginning of the sales process. This prevents future catalog changes from affecting quotes in progress and helps maintain rate consistency from the quote to the order.

Revenue Management automatically captures catalog rates during the quoting process:

When you save a quote, Revenue Management captures the current catalog rates and generates a Quote Line Rate Card Entry record, which prevents subsequent catalog updates from impacting the quote.
When you successfully order the quote, Salesforce transforms those records into Order Item Rate Card Entry records to maintain the exact rates for the order.
NOTE When you add quote line items from a related list, Revenue Management doesn't create the quote line rate card entries immediately. The entries are created the next time the pricing service is invoked, such as when you edit a quote line item, save the quote, or assetize the quote.

=== ARTICLE: ind.qocal_select_fields_for_the_line_editor.htm ===
---
article_id: ind.qocal_select_fields_for_the_line_editor.htm
title: Select Fields for the Line Editor
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_select_fields_for_the_line_editor.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_customize_transaction_line_editor.htm
fetched_at: 2026-09-04
---

# Select Fields for the Line Editor

Select line-level fields, group fields, and related record fields in the Display Columns to manage which fields appear in the line editor.

Line-level fields, such as Quantity, Description, and Total Price, appear as individual columns in the editor.
Group fields, such as [Quote Line Group] Subtotal or [Order Line Group] Subtotal, appear only when a quote or order includes groups. If a transaction isn’t grouped, these fields don’t appear in the editor.
Fields from related records, such as [Account] Name, appear as individual columns in the editor. If the related record doesn’t exist, the column shows empty cells that you can’t edit.
NOTE If you add custom fields to the Transaction Line Editor or Sales Transaction Line Editor columns, add those fields to the context definition used for sales transactions. Otherwise, changes made to those fields in the editor aren’t saved when you save your changes.

If you’re using Transaction Line Editor, select both Discount (Percentage) and Discount (Amount) fields in the Display Columns. When both fields are present, the editor merges them into a single Discount column.

If you’re using Sales Transaction Line Editor, configure the Adjustment Type column. See Adjustment Type column.

IMPORTANT If you want the product and group names to appear in Sales Transaction Line Editor, add [Product] Product Name and [Quote Line Group] Quote Line Group Name or [Order Line Group] Order Line Group Name fields to the Display Columns. We recommend you to place the [Product] Product Name field as the first column in the editor.
Merged Columns in Sales Transaction Line Editor

When you add a group field and its corresponding line field to the Display Columns, Sales Transaction Line Editor automatically merges them into a single column. This behavior improves data visibility across group and line levels. The merging applies only to standard fields.

The merged column uses the line-level field name as the header and appears in the position of the first selected field in the Display Columns. When you view groups, the editor shows values from the group record. When you view line items, the editor shows values from the line record.

By default, these group-level and line-level fields merge into a single column when you add them to the Display Columns in Sales Transaction Line Editor.

QUOTELINEITEM FIELD	QUOTELINEGROUP FIELD	ORDERITEM FIELD	ORDERITEMGROUP FIELD
Product.Name	Name	Product.Name	Name
NetTotalPrice	SummarySubtotal	NetTotalPrice	SummarySubtotal
SortOrder	SortOrder	SortOrder	SortOrder
Description	Description	Description	Description
StartDate	StartDate	ServiceDate	ServiceDate
EndDate	EndDate	EndDate	EndDate
SegmentType	SegmentType	SegmentType	SegmentType
TotalLineAmount	SummaryTotalAmount	TotalLineAmount	SummaryTotalAmount
TotalCost	TotalCost	TotalCost	TotalCost
TotalAdjustment	TotalAdjustment	TotalAdjustment	TotalAdjustment
TotalAdjustmentAmount	TotalAdjustmentAmount	TotalAdjustmentAmount	TotalAdjustmentAmount
TotalMargin	TotalMargin	TotalMargin	TotalMargin
TotalMarginAmount	TotalMarginAmount	TotalMarginAmount	TotalMarginAmount
QuoteLineGroup	ParentQuoteLineGroup	OrderItemGroup	ParentOrderItemGroup
NOTE If a field supports both group-line merging and Adjustment Type merging, the Adjustment Type merge takes precedence. The field appears in the Adjustment Type column instead of merging with its related group or line field.

=== ARTICLE: ind.qocal_sell_commitment_based_usage_products.htm ===
---
article_id: ind.qocal_sell_commitment_based_usage_products.htm
title: Sell Commitment-Based Usage Products
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_sell_commitment_based_usage_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling.htm
fetched_at: 2026-09-04
---

# Sell Commitment-Based Usage Products

For selling commitment-based usage products, a sales rep must follow a three-step process—creating the anchor product, creating the commitment product, and linking the anchor and commitment products together.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create quotes:	Create on Quotes

Let’s take a scenario where a customer wants to purchase Quantum Bit Database—the anchor product, and wants to commit to 1,000 tokens to secure a discounted rate.

SEE ALSO
Build a Quote for Usage-Based Products
Anchor Product with Token Commitments
Create a Usage Commitment Asset Related Object
Step 1: Quote and Assetize the Anchor Product

The anchor product represents the primary service that tracks the customer's consumption.

Create a quote and add the Anchor product—Quantum Bit Database Token Offering.
Under Quote Line Items, from the quick actions, click Manage Usage Resources.
On the Manage Usage Resource page, the Usage Resources table shows the resources included in the product, for example, DB Storage, Compute Time. The table also shows the default token values for each resource, such as 10 tokens per GB.
Save the quote.
Generate the order, and activate it. The activation process creates an asset for the anchor product.
Step 2: Quote and Assetize the Commitment Product

The Commitment product defines the minimum usage or spends and the discounted pricing.

Create a quote and add a commitment product from the catalog—Quantum Token Commitment.
Enter the commitment parameters. For example, the customer commits to 1,000 units of Quantum Tokens.
For the commitment of 1000 tokens, a 6% discounted rate and an extra grant of 10 GB of storage and 10 minutes of compute time are provided.
Save the quote.
Generate the order, and activate it. The activation process creates an asset for the commitment product.
Step 3: Link the Commitment to the Anchor Assets

To apply discounts available in the commitment product to the consumption of the anchor product resources, the two standalone assets must be tied together by using a junction object Usage Commitment Asset Related Object.

NOTE You can’t link multiple commitment products to the same anchor that have the same validity period.
From the App Launcher, find and select Usage Commitment Asset Related Objects.
Click New.
In the Related Object field, select Asset and then select the anchor product you assetized in Step 1 (Quantum Bit Database).
In the Asset field, select the commitment product you assetized in Step 2 (Quantum Token Commitment).
Select an effective start and end date.
Save your changes.

The commitment product is now configured. Whenever the customer consumes DB Storage or Compute Time against their Anchor product, the rating engine processes the consumption by using the 6% discounted rate provided by the linked Commitment.

=== ARTICLE: ind.qocal_set_up_add_derived_pricing_assets_to_a_quote_or_order.htm ===
---
article_id: ind.qocal_set_up_add_derived_pricing_assets_to_a_quote_or_order.htm
title: Set Up Derived Pricing Assets to a Quote or Order
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_add_derived_pricing_assets_to_a_quote_or_order.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_common_capabilities.htm
fetched_at: 2026-09-04
---

# Set Up Derived Pricing Assets to a Quote or Order

Streamline the quoting process by automatically adding derived product assets when your users add contributing products to a transaction.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To update revenue settings:	

Customize Application

AND

Manage Revenue Management

From Setup, in the Quick Find box, find and select Revenue Settings.
In the Quote, Order, and Configuration Settings section, turn on Add Derived Pricing Assets to a Quote or Order.
NOTE Future-dated amendments or renewals include contributing products but only add derived-pricing products explicitly included in the current request.

=== ARTICLE: ind.qocal_set_up_asset_lifecycle_viewer.htm ===
---
article_id: ind.qocal_set_up_asset_lifecycle_viewer.htm
title: Add the Managed Asset Viewer Page Layouts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_asset_lifecycle_viewer.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_asset_management_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Add the Managed Asset Viewer Page Layouts

To view a consolidated list of lifecycle-managed assets, add the Managed Asset Viewer to your account and contract record pages. The Managed Asset Viewer shows standalone and bundled assets. Users expand bundled assets to view the bundle hierarchy and edit data within the viewer or through a side panel.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To add the Managed Asset Viewer component to page layouts:	Customize Application
NOTE The Managed Asset Viewer component shows the assets for Revenue Management contracts only when an application usage assignment named RevenueLifecycleManagement exists.

Users expand their asset view by selecting the asset name to turn on the side panel for more details and attributes. Users edit data within the Managed Asset Viewer or through the side panel. To go to the asset record, click View on the asset row action.

From the management settings for the Accounts or Contracts object that you want to edit, go to Page Layouts.
Create a page layout or modify an existing one.
In the Related Lists section, ensure that the Assets related list is on the page.
Edit the columns in the Assets related list by clicking the gear icon and selecting the fields to show as columns.
The Assets related list fields determine the default fields in the Managed Assets related list.
Save your changes.
Go to Lightning Record Pages, select your page layout, and click Edit to open the Lightning App Builder.
Drag the Related Lists component and the Managed Asset Viewer component on the layout.
Select the checkbox to show the side panel when a user clicks a record link.
The Assets related list and the Managed Assets related lists appear on the page. By default, the Managed Assets list shows the same columns that are shown in the Assets related list.
Configure the columns in the Managed Assets related list.
To change columns, click Select under Display Columns, select columns from the Available list, and move them to the Selected list.
The Managed Asset Viewer shows your selected columns.
Save your changes.
NOTE The Asset Viewer shows only attributes active on the current date; attributes with future start dates remain hidden until they become effective.

=== ARTICLE: ind.qocal_set_up_asset_management_features_in_revenue_cloud.htm ===
---
article_id: ind.qocal_set_up_asset_management_features_in_revenue_cloud.htm
title: Set Up Asset Management in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_asset_management_features_in_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle.htm
fetched_at: 2026-09-04
---

# Set Up Asset Management in Revenue Management

Set up features that provide your sales reps and partners with the capabilities to efficiently manage assets.

Add the Managed Asset Viewer Page Layouts
To view a consolidated list of lifecycle-managed assets, add the Managed Asset Viewer to your account and contract record pages. The Managed Asset Viewer shows standalone and bundled assets. Users expand bundled assets to view the bundle hierarchy and edit data within the viewer or through a side panel.
Automate Asset Creation from Orders
To ensure assets related to an order remain current, use flows to create and update them. When you activate Revenue Management orders, create a record-triggered flow that invokes the Create or Update Asset from Order flow action. Customize the flow or add more conditions to perform other actions.
Set Up Asset Lifecycle Flows
To streamline asset management through their lifecycle and optimize revenue, select a default flow for your assets from the Revenue Settings page. Adding an amend, renew, and cancel flow saves time and money by automating the transition of products through different lifecycle stages.
Asset Renewal Automation Templates
Prebuilt flow templates automatically create renewal opportunities for forecasting and renewing assets. Customize these templates to meet specific business needs before activation.
Set Up Price Amendments
Sales reps can set a new price when they amend an asset instead of applying only a discount amount or discount percent.

=== ARTICLE: ind.qocal_set_up_asset_record_page_for_usage_selling.htm ===
---
article_id: ind.qocal_set_up_asset_record_page_for_usage_selling.htm
title: Add Usage Components to Usage Object Record Pages
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_asset_record_page_for_usage_selling.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_usage_selling.htm
fetched_at: 2026-09-04
---

# Add Usage Components to Usage Object Record Pages

To track consumption, rates, and grant balances, you can use a consolidated view for an object record page. You can also clone the view for your objects in a different app, such as Rate Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To edit page layouts in Lightning App Builder:	Customize Application
From Setup, in the Quick Find box, enter Lightning App Builder, and then select Lightning App Builder.
Select a record page, and then click Edit.
You can select an account, an asset, a contract, or a custom binding object record page.
To add components to tabs for the consolidated view, from the Components list, select these components and drop them to the record page layout.
	
Component name	Corresponding tab
Usage Rates	Rates
Usage Grant Details	Grants
Policy Details	Policies
Source Asset Details	Source Assets
Commitment Relationship Details	Commitment Details
Managed Assets	Manage Asset
Save your changes.
SEE ALSO
Add and Customize Tabs on Lightning Pages Using the Lightning App Builder

=== ARTICLE: ind.qocal_set_up_contract_features.htm ===
---
article_id: ind.qocal_set_up_contract_features.htm
title: Set Up Contract Features in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_contract_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contracts_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Set Up Contract Features in Revenue Management

Revenue Management offers capabilities for sales reps and partners to manage contracts. These features ensure data consistency by automatically pulling account and date details from source quotes or orders.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

Users can manually generate contracts via a dedicated button or automate the process by using flows triggered by quote status. The system supports contract-based pricing by capturing quote line prices or discounts as contract item prices. Also, the Contract Pricing Schedule component provides a visual interface for managing pricing tiers, while custom sequencing controls how volume discounts apply to transactions.

Add a New Contract Button
Help your sales reps create contracts directly from finalized records by using the New Contract button on the Quote or Order pages. This configuration streamlines the sales process by automatically copying essential details, such as the account name and start date, from the source record to the New Contract.
Add the Contract Pricing Schedule Component to Lightning Record Pages
Provide sales reps and contract managers with a simple, comprehensive interface for managing contract pricing by adding the Contract Pricing Schedule component to Contract pages. Customize the component to show only the information that your users need.
Map a Flow to Capture Quote Line Pricing on Contracts
Configure a flow to generate contracts from quotes automatically, helping sales reps to capture negotiated prices and discounts as contract item prices. This automation simplifies the contract lifecycle by giving users the choice to include quote line details or create a contract without specific pricing records.
Automate Contract Creation from Quotes and Orders
Use flows to automatically create contracts from a quote or an order. Create a flow that invokes the Create Contracts from Quote flow action when Revenue Management quotes are changed to Accepted status. You can also add more conditions or customize the flow to perform other actions. Create contracts from orders by using a similar flow.
Configure Line Item Sequencing for Tiered Volume Discounts
Define a sequencing field to control the order in which the system applies tiered or volume contractual discounts to sales transactions.

=== ARTICLE: ind.qocal_set_up_document_builder_quotes.htm ===
---
article_id: ind.qocal_set_up_document_builder_quotes.htm
title: Set Up Document Builder for Quotes
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_document_builder_quotes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_document_builder_for_quotes.htm
fetched_at: 2026-09-04
---

# Set Up Document Builder for Quotes

Turn on Document Builder to begin creating customized, dynamic quote templates that align with your business practices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To enable Document Builder:	Customize Application
From Setup, in the Quick Find box, enter Revenue Settings, and then select Revenue Settings.
Turn on Document Builder, and refresh the setup page.

=== ARTICLE: ind.qocal_set_up_flow_for_managing_assets.htm ===
---
article_id: ind.qocal_set_up_flow_for_managing_assets.htm
title: Set Up Asset Lifecycle Flows
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_flow_for_managing_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_asset_management_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Set Up Asset Lifecycle Flows

To streamline asset management through their lifecycle and optimize revenue, select a default flow for your assets from the Revenue Settings page. Adding an amend, renew, and cancel flow saves time and money by automating the transition of products through different lifecycle stages.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To update the Revenue Settings in Revenue Management:	Customize Application

Create a custom flow by using the default flow as a guide or starting point. The default output type is Quote, but you can change it to Order.

IMPORTANT The flow times out after 10 seconds. Users interacting with the user interface can’t create an Amendment, Renewal, or Cancellation quote with 1,000 line items. Users create the initial quote with fewer line items and then update it to include up to 1,000 items by using APIs or the Add Assets button in the Quote Viewer.
From Setup, in the Quick Find box, search for and select Revenue Settings.
In the Quote, Order, and Configuration Settings section, find Set Up Flow for Managing Assets.
Enter the name of the Amend, Renew, and Cancel Salesforce Flow for the system to use when users select the Amend, Renew, or Cancel buttons in the Managed Assets Viewer.
Save your changes.
EXAMPLE

=== ARTICLE: ind.qocal_set_up_multiple_currencies.htm ===
---
article_id: ind.qocal_set_up_multiple_currencies.htm
title: Multiple Currencies for Transactions
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_multiple_currencies.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_common_capabilities.htm
fetched_at: 2026-09-04
---

# Multiple Currencies for Transactions

Turn on multiple currencies to help your users to transact in different global units. The system uses the currency code in the Quote or Order Currency fields to determine the transaction's currency.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To edit pricing procedures:	Salesforce Pricing Design Time User
Turn on and activate other currencies in Setup.
Enable multiple currencies
Activate and Deactivate Currencies
Create a price book for the new currencies and add your products. Create a price book for the currencies. See .
See Define Prices in Price Books
Open your Pricing Procedure and deactivate the version.
Map the CurrencyIsoCode input variable to PricingCurrencyCode in the Pricing Setting element.
See Map Context Tags in Pricing Procedures.
Activate the procedure.
NOTE Only the Place Sales Transaction API supports multi-currency transactions.

=== ARTICLE: ind.qocal_set_up_order_features.htm ===
---
article_id: ind.qocal_set_up_order_features.htm
title: Quote to Order Conversion
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_order_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_foundational_setup_for_quotes_and_orders.htm
fetched_at: 2026-09-04
---

# Quote to Order Conversion

Convert quotes to orders to ensure pricing, product, and tax details transition into your fulfillment and billing workflows. One-click conversion or advanced quote-splitting helps your sales reps maintain data integrity across Revenue Management while segmenting orders based on specific business needs.

Create an Order from a Quote
Convert an accepted quote into an order with one click to synchronize product, quantity, pricing, and tax data. By using this process, the order record automatically inherits these details directly from the quote record.
Considerations for Creating Multiple Orders from a Quote
Familiarize yourself with these limitations and functional behaviors that use the Advanced Order Creation From Quote feature to create multiple orders from a single quote. This information helps you determine when to use the API versus the user interface and how the system handles pricing and bundled products during the split process.
Split Quotes into Multiple Orders
Unlock greater flexibility in your sales process by creating multiple, independent orders from a single quote. Segmenting a quote helps streamline downstream operations, such as fulfillment, billing, and invoicing. For example, create separate orders by using quote groups or quote line fields like shipping locations, recipients, or start dates.

=== ARTICLE: ind.qocal_set_up_price_amendments.htm ===
---
article_id: ind.qocal_set_up_price_amendments.htm
title: Set Up Price Amendments
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_price_amendments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_asset_management_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Set Up Price Amendments

Sales reps can set a new price when they amend an asset instead of applying only a discount amount or discount percent.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To update revenue settings:	

Customize Application

AND

Manage Revenue Cloud

The Sales Price Amendments setting controls price amendment behavior for quote and order lines. It's turned off by default in existing orgs and turned on by default in new orgs.

From Setup, in the Quick Find box, enter Revenue Settings, and then select Revenue Settings.
Turn on Sales Price Amendments.
Update the pricing procedure selected in Revenue Settings to set the amended price.
In Pricing Procedure Builder, open the procedure selected in Revenue Settings. For example, to set the net unit price when the pricing source is the last transaction, add a List Group element after the Assignment element that assigns the EffectiveFrom date to PricingDate.
In the List Group element, configure the List Operation with these conditions.
Filter Condition Requirements: All Conditions Are Met (AND)
Resource: ItemPricingSource, Operator: Is Not Null
Resource: ItemPricingSource, Operator: Equals, Value: LastTransaction
In the List Group element, add an Assignment element, and map these variables.
Input Variable: InputUnitPrice
Output Variable: NetUnitPrice

To know more about these pricing elements, see List Group and List Operation and Map Context Tag Data Using Assignment Element. To edit a pricing procedure, see Configure Your Pricing Procedure.

=== ARTICLE: ind.qocal_set_up_product_discovery.htm ===
---
article_id: ind.qocal_set_up_product_discovery.htm
title: Configure Product Discovery Settings
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_product_discovery.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_product_discovery_setup.htm
fetched_at: 2026-09-04
---

# Configure Product Discovery Settings

Select the context definition, qualification procedure, and pricing procedure to populate the information that users see when they use Product Discovery. After you enable qualification and pricing procedures for Product Discovery, you can enable or disable them for the Product List, Product Details, or Product Bundle Details components.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To set up product discovery:	

Customize Application system permission

AND

Product Catalog Management Designer permission set

USER PERMISSIONS
NEEDED
To set a default catalog:	Customize Application system permission

Before you begin, complete these tasks.

Create a context definition.
To run qualification rules to evaluate eligibility, create a qualification rule procedure.
To use a pricing procedure to get list prices, make sure that Salesforce Pricing is enabled, and then create a pricing procedure for Product Discovery.
To use a custom flow to browse and add products from quote and order pages in Transaction Management, create a custom flow.
IMPORTANT The qualification procedure and pricing procedure for Product Discovery must use the context definition selected on the Product Discovery Settings page.
From Setup, in the Quick Find box, enter Product Discovery, and then select Product Discovery Settings.
For context definition, select ProductDiscoveryContext or the extended context definition.
To use a qualification procedure for Product Discovery, turn on Qualification Procedure, and then select the qualification procedure.
Only procedures with Product Qualification as the Usage Type appear in the Select Qualification Procedure dropdown. Procedures with Product Category Qualification as the Usage Type aren’t supported. To qualify or disqualify product categories in Product Discovery, add category-level elements to a Product Qualification procedure.
To use a pricing procedure for Product Discovery, turn on Pricing Procedure, and then select the pricing procedure.
To use a custom flow to browse and add products from quote and order pages, in Select a Custom Flow for Browsing and Adding Products in Revenue Management, select the custom flow.
The Select a Custom Flow for Browsing and Adding Products setting is available only when Transaction Management is available in your org.
To configure a default catalog for the product list page, select a default catalog.
Configure your search settings.
To find products in catalogs of more than 4 million products, turn on Product Field Search.
Use Product Field Search to search all text-indexed fields of the product object such as product name, description, product code, and custom product fields of type text.
To use indexed product catalog data for product browse and search, turn on Use Indexed Data for Product Listing and Search.
To find your products, you can also search for indexed product fields and attribute values in the catalog.
To help users find their products faster, turn on Guided Product Selection.
Guided Product Selection uses dynamic forms that filter products in the catalog based on user responses.
To use Einstein AI to generate product descriptions, turn on Generate Product Descriptions with Einstein AI.
SEE ALSO
Context Definitions
Guided Product Selection
Manage Qualification Rules for Products in Revenue Cloud
Search Options in Product Catalog Management
Write Product Descriptions with Einstein Generative AI

=== ARTICLE: ind.qocal_set_up_quote_and_order_capture.htm ===
---
article_id: ind.qocal_set_up_quote_and_order_capture.htm
title: Begin Using Transaction Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_quote_and_order_capture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Begin Using Transaction Management

Transaction Management simplifies subscription lifecycles while ensuring the integrity of all sales transactions. You can tailor the Revenue Management (formerly Revenue Cloud) experience by using permission sets and setup instructions to give each user precise access to the features they need.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Personas and Permissions Sets for Transaction Management
Transaction Management offers specific permission sets for different users involved in creating and managing sales transactions.
Enabling Revenue Settings
Give your users access to Transaction Management. Also, enable optional features to enhance the sales experience for your reps.
Extend and Map Sales Transactions in Revenue Management
Extend or customize default features to meet business-specific requirements by creating and mapping custom fields in Revenue Management.
Transaction Management Considerations
Review essential requirements and behaviors before using Transaction Management to manage your quotes and orders. Understanding these configurations, including page layout updates, pricing synchronization, and field permissions, ensures accurate transaction processing and data integrity.
Transaction Management Limits
Review the record, attribute, and bundle limits for Transaction Management to make sure that your quotes and orders remain within supported thresholds. Understanding these technical specifics helps you optimize performance and avoid process timeouts during asset lifecycle operations.

=== ARTICLE: ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm ===
---
article_id: ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm
title: Set Up Quote and Order Features in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_foundational_setup_for_quotes_and_orders.htm
fetched_at: 2026-09-04
---

# Set Up Quote and Order Features in Revenue Management

Set up features that provide your sales reps, partners, and customers with the capabilities required to efficiently manage quotes and orders.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Add and Customize the Transaction Line Editor or Sales Transaction Line Editor
To help sales reps to view and manage quote and order line items efficiently, add the Transaction Line Editor or Sales Transaction Line Editor (STLE) to the page layout and customize the fields that the editor shows. We strongly recommend using STLE because its streamlined, single-grid layout improves performance at scale and provides access to the latest capabilities in Transaction Management. The Transaction Line Editor remains available, but it’s no longer being enhanced.
Set Up the Transaction Processing Type for Quotes and Orders
Define how Revenue Management processes transactions by selecting a default Transaction Processing Type (TPT).
Set Up Delta Pricing
Improve large transaction performance by enabling Delta Pricing to recalculate only modified quote or order lines and their dependencies.
Invoke the Place Sales Transaction API in a Flow
Invoke the Place Sales Transaction (PST) API to create, update, and delete quotes and orders and price their related products and services. Before you can invoke the action, create and set the values of an Apex-defined variable to use as the graph input for the action. You can use the other inputs to configure how Salesforce prices and validates the quote or order. The action returns the ID of the sales transaction as well as status information.
Reprice All for Quotes and Orders
Refresh and validate prices across an entire transaction by recalculating all quote or order lines.
Secure Data Access for Pricing with Elevated Permissions
Protect sensitive data from unauthorized access and have business continuity during sales transaction pricing. This feature helps sales users to price quotes and orders without needing field-level security (FLS) to query, view, or modify the underlying sensitive fields.

=== ARTICLE: ind.qocal_set_up_quote_features.htm ===
---
article_id: ind.qocal_set_up_quote_features.htm
title: Manage Quotes in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_quote_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_foundational_setup_for_quotes_and_orders.htm
fetched_at: 2026-09-04
---

# Manage Quotes in Revenue Management

Run these configuration procedures to optimize the quote management lifecycle and document generation within Revenue Management. Prioritize the setup of quote line item imports and opportunity synchronization to accelerate record creation while maintaining data alignment across your sales pipeline. By stabilizing these foundational dataflows, you make sure that complex elements like bundles and attributes transition accurately from preliminary offers to finalized orders.

Use advanced professional tools like the Document Builder and Einstein Generative AI to streamline proposal sharing and deal overviews. Configure automated order conversion. Segment quotes into multiple independent orders by using groups or specific fields. This segmented approach provides the flexibility required to manage complex fulfillment and billing needs. These integrated features help the sales teams to refine proposals efficiently and move from customer acceptance to draft orders with a single click.

Quote Management Lifecyle
Sales representatives use quotes as preliminary offers to propose products and pricing to customers. This lifecycle involves discovering products, entering quote details, and managing revisions before converting a final proposal into an order.
Quote Line Item Imports
Importing quote line items from a CSV file accelerates the quoting process by eliminating manual data entry for large volumes of products. Revenue Management uses Transaction Management components to process these imports, ensuring data consistency across multiple product types and currency models.
Document Builder for Quotes
Document Builder provides a professional document generation solution to create formatted documents that meet business and customer requirements. Adopting Document Builder helps you to build professional, customized, and dynamic quote documents.
Generate a Quote Document with Document Builder
Preview, generate, and email quote PDFs to serve your customers. Use this professional document generation solution to share details of work performed with your customers in real-time.
Create a Quote Template with Document Builder
Design a template that defines how information appears on your quote documents. Use this template to generate customized quotes for your customers.
Capture Signatures on Web and Mobile App
Streamline your approval process by capturing digital signatures in Document Builder. Whether in the office or in the field, make sure that quotes are legally binding and professional by adding a signature to your PDFs.

=== ARTICLE: ind.qocal_set_up_quote_line_item_import.htm ===
---
article_id: ind.qocal_set_up_quote_line_item_import.htm
title: Set Up Quote Line Items Import
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_quote_line_item_import.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_line_item_import.htm
fetched_at: 2026-09-04
---

# Set Up Quote Line Items Import

Turn on the Import Quote Line Items setting and create a Data Processing Engine definition to perform bulk quote creation from CSV files.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Turn On Import Quote Line Items

Before you begin, perform these actions.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To turn on the Import Quote Line Items setting:	Advanced CSV Data Import permission set
On the Revenue Settings page:
Turn on Enable Groups in quotes and orders.
Turn off Hide Price Refresh Notification.
Add product codes to all products intended for import.
In Setup, find and select Revenue Settings.
Turn on Import Quote Line Items.
The Import Lines button now appears on quote pages.
In the Flow for Importing Quote Line Items field, enter the API name of the flow that processes the imported quote line items.
To use the predefined flow, keep the default value, transactionManagement__ImpQuotLineItm.
To use a custom flow, enter your specific flow API name.
The flow opens when a user clicks Import Lines.
Create and Set Up a Data Processing Engine Definition

Create a Data Processing Engine definition to process CSV data and create quote line items. Revenue Management provides templates based on organization type.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To create a Data Processing Engine definition:	

Customize Application

AND

Modify All Data

Revenue Management provides these Data Processing Engine definition templates.

ORG TYPE	NAME	API NAME
Single-currency	Create Quote Line Items from a CSV File	CreateQuoteLineItemsFromCSV
Multicurrency	Create Quote Line Items from a CSV File in Multi-Currency Orgs	CreateQuoteLineItemsWithCurrencyFromCSV
NOTE These definitions use the Core execution platform type and don’t open in the Data Processing Engine builder. To learn how to edit these definitions, see Customize Data Processing Engine Definitions for Quote Line Item Imports .
In Setup, find and select Data Processing Engine.
Next to the preferred template, click  and select Save As.
Enter a name, API name, and description, and save your changes.
Next to your new definition, click  and select Activate.
In Setup, find and select Revenue Settings.
Select your activated definition from the Data Processing Engine Definition for Importing Quote Line Items dropdown.
Test the definition by performing a quote line item import.

After you complete the setup:

Monitor import status by using Monitor Workflow Services.
Extend the import functionality to support more requirements, such as custom fields.

=== ARTICLE: ind.qocal_set_up_ramp_deals_for_groups.htm ===
---
article_id: ind.qocal_set_up_ramp_deals_for_groups.htm
title: "Prerequisites: Ramp Deals for Groups"
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_ramp_deals_for_groups.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.setting_up_ramp_deals.htm
fetched_at: 2026-09-04
---

# Prerequisites: Ramp Deals for Groups

Complete these essential setup steps before configuring your highly recommended group-based ramp deals.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To turn on the Ramp Deal for Groups in Quotes and Orders setting:	Customize Application
In Setup, find and select Revenue Settings. Turn on both the Enable Groups in Quotes and Orders and the Clone Quotes and Orders settings.
Update your custom flows.
If you created a custom Product Discovery flow before Winter '25, clone the latest prebuilt Discover Products flow and customize it.
If you customized the Transaction Management pricing procedure before Winter '25, clone the latest prebuilt Revenue Management Default Pricing Procedure and customize it.
If you customized Product Configurator flows before Winter '25, clone the Default Product Configurator Flow and customize it.
In Setup, find and select Revenue Settings. Turn on Ramp Deals for Groups in Quotes and Orders.
Turn on Multiple Ramp Schedules Per Transaction.
Sales reps can create up to 10 separate ramp schedules within a single quote or order. If you turn on this setting after ramp deals for groups are active, Transaction Management can't activate orders created between the two activations. Use a migration script to resolve those orders.
If your org uses a custom Discover Products flow and you want to enable upgraded group ramp support, complete these steps.
From Setup, in the Quick Find box, enter Flows and select it.
Open the custom Discover Products flow.
Rearrange the nodes in the Discover Products flow.
In your custom Discover Products flow, move the Ramped Group node so that it appears after the catalog selection node, and before the Product List node.
Configure the Select Ramp Segments node.
Click the Select Ramp Segments node.
Click the node again to open its settings.
In Advanced, set the Discover Products context output variable.
Save the node.
Update the Product List node settings.
Click the Product List node.
In Advanced, locate the Revisited Screen Values field.
Change the value from Use values from when the user last visited this screen to Refresh inputs to incorporate changes elsewhere in the flow.
Save the node.
For instructions, see Override Flow for Product Discovery.
Add the Sales Transaction Line Editor component to quote and order page layouts.
NOTE The legacy Transaction Line Editor component doesn't support ramp deals for groups. Use the Sales Transaction Line Editor.

Configure the Sales Transaction Line Editor to show these fields:

RECORD TYPE	FIELDS TO SHOW
Quote line items and order products	
Start Date
End Date
Segment Type

To identify ramped lines during testing, also show:

Ramp Identifier
Segment Identifier

Quote line groups and order product groups	
Start Date
End Date
Segment Type
Is Ramped
Quote Line Group Name or Order Product Group Name

Product and group name fields appear in the first column.


Uplifts (optional)	Add Unit Price Uplift
Edit Ramp Schedule and View Ramp Details windows (optional)	Configure which fields appear in these windows.
During debugging or setup	

Add the Ramp Identifier column to make debugging easier.

You can remove this field once you move to production.

IMPORTANT Don't rename the Uplift formula-based pricing component. Renaming it causes the system to apply the uplift without showing the value in the price waterfall.

=== ARTICLE: ind.qocal_set_up_usage_product_and_services.htm ===
---
article_id: ind.qocal_set_up_usage_product_and_services.htm
title: Set Up Usage-Based Product and Services
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_usage_product_and_services.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_usage_selling.htm
fetched_at: 2026-09-04
---

# Set Up Usage-Based Product and Services

The first step to sell usage-based products is to set up the product structure, its resources, and setting up the grants provided with the sellable product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Define Usage Resources and Units of Measure

Use the Usage Resource object to define services that are provided as grants, units of measure to measure these services, and unit of measure classes to group the units of measure.

Configure Sellable Product and Mapping

To provide the usage-based services, you must associate it with a sellable product. Create a sellable product by selecting a usage model type in the product record. To create a mapping between a sellable product and the related services, create a product usage resource record.

Setup Commits, Grants, and Entitlements

If your sellable product provides an initial quantity of associated services—grants, configure Product Usage Grants. A product usage grant record includes details, such as the number of grants provided with the sellable product, validity of the granted quantity, a set of policies that defines the behavior of the grants, and the order in which the service units will be debited. Similarly, if you're working with a commitment-based usage product, select the Commit type while configuring the product usage grant record.

Configure Policies

The usage resources, grants, and entitlements are governed by various policies.

Usage Aggregation Policy—defines how Usage Management aggregates the consumption data.
Usage Overage Policy—defines whether overconsumed resource units are charged.
Rating Frequency Policy—defines the frequency at which rating is triggered for the ratable summary records.
Renewal and Rollover Policies—determines when the grant resets and whether the unused units carry over to the next period, respectively.
Product Usage Resource Policy—associates all policies applicable to the usage resource.
Usage Commitment Policy—defines the set of rules that determines the rate applicable for overage computation after the commitment is fulfilled. You can either select the discounted commit rate or use the rate applicable for the bounded target.
EXAMPLE

Define a usage-based product—a mobile plan; create and associate usage resources—call minutes and data; to measure these services, create units of measure—Minutes and GB and group them into units of measure classes—Time and Data. To ensure all services consumed in the accumulation period are aggregated, define the usage aggregation policy with the Sum accumulation method.

SEE ALSO
Enable Usage Management
Usage Management Setup
Validate Your Setup

=== ARTICLE: ind.qocal_set_up_usage_rating.htm ===
---
article_id: ind.qocal_set_up_usage_rating.htm
title: Set Up the Default Usage Rating Discovery Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_usage_rating.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_usage_selling.htm
fetched_at: 2026-09-04
---

# Set Up the Default Usage Rating Discovery Procedure

The final net rate of a usage source is calculated based on the default value specified for usage rating discovery procedure in Revenue Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To update the Revenue Settings in Revenue Management:	

Customize Application

AND

Manage Revenue Management

A usage rating discovery procedure must be defined in Rate Management before you can select the procedure as the default.

From Setup, in the Quick Find box, find and select Revenue Settings.
In the Quote, Order, and Configuration Settings section, find Set Up Usage Rating and select the usage rating discovery procedure.
Your changes are autosaved.
SEE ALSO
Rating Discovery Procedures

=== ARTICLE: ind.qocal_set_up_usage_selling.htm ===
---
article_id: ind.qocal_set_up_usage_selling.htm
title: Set Up Usage Selling in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_set_up_usage_selling.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling.htm
fetched_at: 2026-09-04
---

# Set Up Usage Selling in Revenue Management

Before you begin selling usage-based products and services, make sure that you’ve completed the required set up. You must define usage products, resources, and the grants, commitments, and entitlements offered with the products. Define policies that govern these products and services. Then, set up rates for each of these products and services.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Set Up Usage-Based Product and Services
The first step to sell usage-based products is to set up the product structure, its resources, and setting up the grants provided with the sellable product.
Set Up Rates for Usage-Based Products
When you sell a usage-based product, the rate definitions and the rating discovery procedure that you set up in rate management retrieves the rate for these products. These rates are available with the product details when you browse the product catalog.
Set Up the Default Usage Rating Discovery Procedure
The final net rate of a usage source is calculated based on the default value specified for usage rating discovery procedure in Revenue Management.
Add Usage Components to Usage Object Record Pages
To track consumption, rates, and grant balances, you can use a consolidated view for an object record page. You can also clone the view for your objects in a different app, such as Rate Management.
Create and Add Custom Fields for Usage-Based Products
Ensure that your custom fields are visible to users during sales transactions. By default, custom fields aren’t visible on the quote creation, manage usage resource, and asset pages.
Configure Record Sharing and Sharing Rules for Usage Selling
For users to access the data created by usage designers or catalog admins, Setup record sharing for all usage-related objects. This configuration is crucial for the seamless execution of usage selling processes within Salesforce.

=== ARTICLE: ind.qocal_specialized_asset_considerations.htm ===
---
article_id: ind.qocal_specialized_asset_considerations.htm
title: Specialized Asset Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_specialized_asset_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_assets_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Specialized Asset Considerations

Revenue Management allows you to modify assets with scheduled future transactions, such as upsells, renewals, or swaps, by using specific amendment types. Sales reps can meet precise contract requirements and manage global subscriptions by using exact time zone precision to establish accurate asset state periods. Additionally, users can negotiate and track changes to catalog or negotiated rates and grants through an asset-level audit trail during amendments and renewals

Usage-Based Assets
Learn how usage-based products enable flexible rate and grant negotiations throughout an asset's lifecycle. This understanding is essential for successfully managing usage resources before you begin amendment or renewal tasks.
Future-Dated Changes
To adjust assets that have scheduled future transactions, such as upsells, downsells, renewals, transfers, swaps, or attribute changes, use the Managed Asset viewer. This process updates assets that have more than one subsequent future-dated change recorded as an asset state period (ASP).
Backdate Asset Transactions
Apply an amendment, renewal, or cancellation to an asset with a past effective date so that the asset reflects the change from the date it took effect.

=== ARTICLE: ind.qocal_specialized_transaction_types.htm ===
---
article_id: ind.qocal_specialized_transaction_types.htm
title: Specialized Transaction Types
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_specialized_transaction_types.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_assets_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Specialized Transaction Types

Streamline sales operations by transferring asset quantities between accounts or swapping products while maintaining accurate audit trails and relationship labels. Use lot-based renewals to honor original purchase prices across multiple transactions and apply price uplifts to individual lots. You can also renew expired assets and subscriptions by choosing new start and end dates, providing flexibility for late renewals and trial extensions.

Transfer Assets Between Accounts
To maintain compliance and streamline operations, your users can move asset quantities, product licenses, or subscriptions between different accounts or contracts.
Swap, Upgrade, or Downgrade Assets
To maintain accurate records and streamline your sales process, use specific asset actions to capture the relationships between swapped-out and swapped-in assets.
Use Lot-Based Renewals to Preserve Original Prices
To honor existing prices at renewal time, use lot-based or As-Is renewals to renew asset lot quantities at their original purchase prices. For example, if a sales rep sells an asset across multiple transactions, a lot-based renewal includes both the initial sale and subsequent amendments. The system applies a price uplift individually to each lot based on the renewal uplift.
Renew Expired Assets
To maintain customer relationships and close deals faster, renew assets and subscriptions after their original end date. Enabling late renewals and trial extensions provides flexibility when customers want to repurchase products.

=== ARTICLE: ind.qocal_split_quote_into_multiple_orders.htm ===
---
article_id: ind.qocal_split_quote_into_multiple_orders.htm
title: Split Quotes into Multiple Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_split_quote_into_multiple_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_order_features.htm
fetched_at: 2026-09-04
---

# Split Quotes into Multiple Orders

Unlock greater flexibility in your sales process by creating multiple, independent orders from a single quote. Segmenting a quote helps streamline downstream operations, such as fulfillment, billing, and invoicing. For example, create separate orders by using quote groups or quote line fields like shipping locations, recipients, or start dates.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create orders from quotes:	

Create Orders from Quotes permission

AND

Product Catalog Management Viewer permission set

Prerequisites for Splitting Quotes

Perform these tasks before splitting a quote into multiple orders.

In Setup, find and select Revenue Settings.
Turn on Advanced Order Creation From Quote.
This action updates the functionality of the Create Order button on quotes.
NOTE Changes take effect after approximately 10 minutes. Log out and log back in to apply changes immediately.
In Setup, find and select Flows, and select the Create Orders From Quote flow template.
Enter a unique flow label and API name and save it as a new flow.
Configure the Order Creation method, Split field, and other elements by customizing the flow pages.
Save and activate the flow.
In Setup, find and select Revenue Settings.
Add the API name of your new flow to the Set Up Flow for Creating Orders from Quotes setting.
Save your changes.
Create Multiple Orders from a Quote

Segment a quote into multiple orders based on specific fields or groups.

From App Launcher, search for and select Quotes.
Select a quote and then click Create Order.
Select an order creation option.
Create Single Order: Creates one order.
Create Order by Group: Creates orders based on a quote line item group.
Create Order by Field: Creates orders based on a quote line item field, such as location or delivery date.
If you select the Create Order by Field option, enter a field name like Start Date in the Quote Line Item Field search and click Finish.
Click View the new Orders from the confirmation message.
New orders appear in the list view with a Draft status.
Update the new orders and save your changes.
Lightning App Builder shows supported standard fields during design time.
Supported data types for custom fields include Checkbox, Date, Text, Email, URL, Phone, Picklist, Multi-select Picklist, Foreign Key, Foreign Key + Option, and External Lookup.

=== ARTICLE: ind.qocal_split_quote_to_orders_important_considerations.htm ===
---
article_id: ind.qocal_split_quote_to_orders_important_considerations.htm
title: Considerations for Creating Multiple Orders from a Quote
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_split_quote_to_orders_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_order_features.htm
fetched_at: 2026-09-04
---

# Considerations for Creating Multiple Orders from a Quote

Familiarize yourself with these limitations and functional behaviors that use the Advanced Order Creation From Quote feature to create multiple orders from a single quote. This information helps you determine when to use the API versus the user interface and how the system handles pricing and bundled products during the split process.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Order Creation Limits and Requirements

Review these technical constraints and data handling rules before splitting quotes.

The Sales Transaction Line Editor experience excludes support for partial order creation, also known as ordering part of a quote.
The API alone supports the manual selection of specific line items that constitute a subset of a quote for a new order.
The Advanced Quote to Order API creates a partial order with a subset of lines and returns later to create more orders from that same quote.
Asset transfer source and destination quotes require the Create Single Order option.
The Transaction Management system prices and configures each created order independently.
New orders exclude cross-order pricing and tax calculations.
You can’t split bundled product components or line items that have pricing dependencies.
Splitting a quote with existing header level adjustments carries over the same pricing adjustments to the resulting orders created, but they aren’t re-applied to the orders. It’s best practice to not reprice orders when they’re created from a quote, so all pricing remains the same as the pricing from the original quote. Any further pricing operation causes those adjustments to be re-applied, which can result in over-discounted pricing.
You can’t split ramp groups.
Nested groups in quotes split into multiple orders.
A single quote supports a maximum split of 200 orders.
API Processing Behavior

The Create Orders From Quote API handles order headers and line items that use different processing methods.

ORDER TYPE	HEADER CREATION	LINE ITEM CREATION
Multiple Orders	Synchronous	Asynchronous
Single Order	Synchronous	Synchronous

=== ARTICLE: ind.qocal_start_quote_in_contract_to_use_contract_pricing.htm ===
---
article_id: ind.qocal_start_quote_in_contract_to_use_contract_pricing.htm
title: Generate a Quote or Order from a Contract
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_start_quote_in_contract_to_use_contract_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_sales_transactions_rev_cloud.htm
fetched_at: 2026-09-04
---

# Generate a Quote or Order from a Contract

Create quotes or orders from an active contract with contract-based pricing to include negotiated contract prices in your new transaction. Sales reps use existing contract-based pricing to ensure financial accuracy for specific customers.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To use contract pricing:	Salesforce Pricing Design Time User
To create quotes:	Create on Quotes
IMPORTANT
Refresh the decision table for contract pricing after activating a contract that contains contract item prices or price adjustment schedules.
Avoid removing or changing a contract ID assigned to a quote or order, as this action impacts pricing during recalculation.

Generate a new transaction record that inherits negotiated pricing directly from an active contract.

From the App Launcher, search for and select Contracts.
From the Contracts list view, select All Activated Contracts.
Select an activated contract that contains contract-based pricing.
On the Related tab, go to the quotes or orders related list and click New.
Enter a name for the quote or order and save your changes.
Add products to the quote or order.
The system applies existing contract prices, discounts, or adjustments to the added products.
Hover over the Net Unit Price to view the pricing waterfall and verify the pricing calculations.
Save your changes.

=== ARTICLE: ind.qocal_swap_upgrade_downgrade_amendments.htm ===
---
article_id: ind.qocal_swap_upgrade_downgrade_amendments.htm
title: Swap, Upgrade, or Downgrade Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_swap_upgrade_downgrade_amendments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_specialized_transaction_types.htm
fetched_at: 2026-09-04
---

# Swap, Upgrade, or Downgrade Assets

To maintain accurate records and streamline your sales process, use specific asset actions to capture the relationships between swapped-out and swapped-in assets.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create a swap, upgrade, or downgrade amendment:	Initiate Amend user permission

Before you begin, add the Type and Subtype columns to the Sales Transaction Line Table component. The Type column shows action types, while the Subtype column shows line groupings like SwapIn, SwapOut, UpgradeFrom, UpgradeTo, DowngradeFrom, and DowngradeTo. See Add and Customize the Transaction Line Editor or Sales Transaction Line Editor.

Instead of "rip and replace," this feature tracks swaps, upgrades, and downgrades across quote lines, order items, asset actions, and asset action sources.

Explicit labels for asset actions provide clarity for reports and audits. Business analysts and sales operations generate reports to differentiate products acquired through new sales versus amendments and to understand how these actions impact revenue.

From the App Launcher, find and select Accounts, click an account, and then select the Assets tab to open the Managed Assets viewer.
Select the assets to swap out and select Swap from the actions dropdown.
Select a date for the swap from the Swap Selections page.
Select the products to swap out, enter the quantity, and click Next.
Click Add for the products that you want to swap in, and click Next.
The resulting quote shows the line item for the swapped-out product with a negative price and the swapped-in product with a positive price.
Click Create Order, and then click Create Single Order to initiate the quote-to-order process.
Select the new order, activate it, and mark it as complete.

Review the asset actions to verify the transaction details.

In the Managed Assets viewer, select View for the swapped-out asset and select the Related tab.
Confirm that a new asset action exists with a Swaps Business Category and a negative quantity.
In the Managed Assets viewer, select View for the swapped-in asset and select the Related tab.
Confirm that a new asset action exists with a Swaps Business Category and a positive quantity.

=== ARTICLE: ind.qocal_swap_upgrade_downgrade_important_considerations.htm ===
---
article_id: ind.qocal_swap_upgrade_downgrade_important_considerations.htm
title: Swap, Upgrade, and Downgrade Amendments Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_swap_upgrade_downgrade_important_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Swap, Upgrade, and Downgrade Amendments Considerations

Familiarize yourself with the requirements and restrictions for processing swaps, upgrades, and downgrades as specialized types of amendments. Understanding these constraints ensures accurate lifecycle management and prevents transaction errors during asset modification.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Amendment Restrictions and Compatibility

Review these critical limitations before processing a swap, upgrade, or downgrade transaction.

Rollback Limitations: You can’t roll back swap transactions.
Product Restrictions: You can’t swap, upgrade, or downgrade the following asset types
Ramp or group ramp assets.
Expired assets.
Usage-Based assets.
Derived Price products.
Feature Incompatibility: The swaps feature doesn’t function with Dynamic Revenue Orchestration.

=== ARTICLE: ind.qocal_token_support.htm ===
---
article_id: ind.qocal_token_support.htm
title: Anchor Product with Token Commitments
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_token_support.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling_advanced_concepts.htm
fetched_at: 2026-09-04
---

# Anchor Product with Token Commitments

A token acts as a virtual currency, such as Flex credits or Salesforce credits. In the token-commitment model, your user purchases a quantity of tokens that has a standard conversion rate to a dollar for each service, such as SMS and data.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

For tokens, these terms help define the conversion rate.

Points Per Unit (PPU)—the anchor product defines how many tokens each specific service costs. For example, one SMS message equals five tokens, and 1 GB of data equals 10 tokens.
Price Per Point (PPP)—the quote defines the monetary cost of a single token, such as $0.75 per token.

When a sales rep creates a quote and adds a product or service, the resources are listed with their PPU. The system calculates the final price based on the number of tokens purchased multiplied by the PPP.

When consumption occurs, the rating engine converts the consumption, such as one SMS message, into tokens (five tokens). It then calculates the financial impact based on the token price.

Token-to-Cost Calculation for Usage Resources

The consumption of usage resources is calculated based on defined conversion rates. To calculate costs, Salesforce converts usage into a monetary value:

Consumption-to-Token Conversion—the consumption of a resource is converted into tokens based on a defined rate. For example, 1 GB of data storage = 2 tokens.
Token-to-Currency Conversion—the total number of tokens is converted into a monetary value by using the token's rate. For example: 1 token = US$0.20.
EXAMPLE To calculate the cost of cloud storage that uses an anchor rate:

Consider ACME, a cloud storage company that uses a token-based model. You purchase a product that provides 50 GB of storage data.

Total amount calculation:

QUANTITY	RATE	CALCULATION
50 GB	2 Cloud credits per GB	50 GB x 2 Cloud Credits per GB = 100 Cloud Credits
100 Cloud Credits	$0.20 per Cloud Credit	100 Cloud Credits x $0.20 per Cloud Credit = $20.00

The amount due for 50 GB of data is $20.00.

Token Calculation for Commitments

When token resources are linked to commitments, the calculation depends on the commitment policy. Commitment discounts apply only if the policy uses the lowest commitment rate.

EXAMPLE Consider a service that uses the anchor product Storage Plan for its base rate. For the anchor product, the unit-to-token rate is 10 and the token-to-currency rate is $0.50. The anchor product is linked to commitment product Storage-Per-Month, which provides a 20% PPU discount. The PPP rate for the commitment product is $0.30.

If you have a usage of 1,000 storage units, here's how the cost of the service is calculated by using a commitment discount.

QUANTITY	RATE	CALCULATION
1000 units	8 Revenue Events per unit (20% discount applied)	1000 x 8 = 8000 Revenue Events
8000 Revenue Events	$0.30 per Revenue Event	8000 x $0.30 = $2,400.00
The final charge for 1000 units is $2,400.00.

The final overage calculation depends on the commitment policy:

Lowest Commitment Rate: Uses the commitment rate for overage calculations, and commitment discounts apply.
Bounded Object Rate: Uses the anchor rate for overage calculations, and commitment discounts don't apply.
SEE ALSO
Create a Usage Resource
Create a Unit of Measure Class

=== ARTICLE: ind.qocal_transfer_assets_to_new_account.htm ===
---
article_id: ind.qocal_transfer_assets_to_new_account.htm
title: Transfer Assets Between Accounts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_transfer_assets_to_new_account.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_specialized_transaction_types.htm
fetched_at: 2026-09-04
---

# Transfer Assets Between Accounts

To maintain compliance and streamline operations, your users can move asset quantities, product licenses, or subscriptions between different accounts or contracts.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create transfer quotes and orders:	Amend Assets user permission

For example, if Account A transfers 200 of its 500 Sales Cloud licenses to Account B, this process reduces Account A’s count by 200 and creates an asset for 200 licenses on Account B. This capability ensures SOX compliance by linking a quantity reduction in one account to an increase in another, eliminating manual "rip and replace" processes.

Prerequisites

Before transferring assets, configure the environment to support the enhanced quote-to-order flow.

In Setup, find and select Revenue Settings and turn on Advanced Order Creation From Quote.
In Setup, find and select Flows and select the Create Orders From Quote flow template.
Select Save as a New Flow, enter a flow label and unique API name, and activate the flow.
You can customize flow screens to configure the Order Creation method or Split field.
In Revenue Settings, add the API name of the new flow to the Set Up Flow for Creating Orders from Quotes setting.
Save your changes.
Transfer an Asset

When you initiate a transfer, the system generates two quotes: a source quote (action: Amend, subtype: TransferFrom) and a destination quote (action: Add, subtype: TransferTo). The quote header action updates to Transfer. While quantities default to the full asset amount, users can adjust them for partial transfers.

From the App Launcher, find and select the Accounts page, then select an asset in the Managed Asset Viewer on the Assets tab.
From the Amend, Renew, Cancel dropdown list, select Transfer.
On the New Transfer Details page, enter the transfer details and click Submit.
On either the source or destination quote, select Create Order to generate both a source and a destination order.
A success message confirms the creation of both orders.
Verify that the new orders appear in Draft status on the Related tab of the Account page.
Activate the source order first, and then activate the destination order. Follow this sequence to prevent transferring more quantity than exists on the source asset.
NOTE If a quantity or date mismatch occurs during destination order activation, perform manual error correction.
Assetize the source and destination orders in any sequence.
To ensure data consistency, the system blocks other amend, renew, or cancel functions on these assets until you fully assetize both orders.

=== ARTICLE: ind.qocal_turn_on_quote_and_order_capture.htm ===
---
article_id: ind.qocal_turn_on_quote_and_order_capture.htm
title: Enabling Revenue Settings
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_turn_on_quote_and_order_capture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Enabling Revenue Settings

Give your users access to Transaction Management. Also, enable optional features to enhance the sales experience for your reps.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To turn on quote and order capture:	

Customize Application

AND

Manage Revenue Cloud

IMPORTANT The order for enabling features and assigning permissions can vary, so if you encounter an error during enablement, check that you have the required permission sets. Skip these steps if the feature is already active in your scratch org definition file.
Turn On Revenue Management

If you haven’t done it yet, enable Revenue Management Features to give your users access to Transaction Management’s object and features.

From Setup, in the Quick Find box, find and select Revenue Settings.
Verify that Enable Revenue Cloud Features is turned on.
Set Up Application Usage Type

Set up proper application tagging to support Revenue Lifecycle Management

From Setup, in the Quick Find box, find and select Revenue Settings.
Turn on Create Application Usage Type for Revenue Cloud.
Set Up Quote

Set up quotes and quote line items across your Salesforce org.

From Setup, in the Quick Find box, find and select Quote Settings.
Select the option for enabling quotes.
Then, select Create Quotes Without a Related Opportunity.
Save your changes.
Add quotes to the Opportunity page.
From Object Manager, select the Opportunity object.
On the Page Layout Selection page, select Opportunity Layout to include Quotes related list.
Set Up Order

Use the Order Settings page to control whether users in your organization have the ability to create and manage orders.

From Setup, in the Quick Find box find and select Order Settings.
Select these settings.
Enable Orders
Enable Negative Quantity
Enable Enhanced Commerce Orders
Enable Zero Quantity
Save your changes.

When you enable the Enhance Commerce Orders option, it makes the Total Line Amount field available and the Unit Price optional on order items.

The total price is calculated based on the fields that you provide.

If both Unit Price and Total Line Amount are specified, then the Total Line Amount is used as the final price.
If only Unit Price is specified, then the total price is the Unit Price multiplied by the quantity.

All final prices are automatically rounded to the currency's smallest denomination (for example, to the nearest cent for USD) based on the ISO 4217 standard, not your Salesforce org's currency settings.

Set Up Flows

Build flows for managing assets and creating contracts and orders from quotes.

From Setup, in the Quick Find box, find and select Revenue Settings.
Scroll and search for Set Up Flow for Managing Assets.
Provide the API name of the screen flow that will be used when amending, renewing, and canceling assets. To use the predefined flow, keep the default value, runtime_revenue_arcflows__arcFlow. To use a custom flow, enter the API name of the flow that you created.
Save your changes.
Scroll and search for Set Up Flow for Creating Contracts from Quotes.
Provide the API name of the screen flow that will be used when converting a quote to a contract. To use the predefined flow, keep the default value, rev_contracts__CreateCntrFromQuote. To use a custom flow, enter the API name of the flow that you created.
Save your changes.
Scroll and search for Set Up Flow for Creating Orders from Quotes.
Provide the API name of the screen flow that will be used when creating orders from a quote using the Create Order button. To use the predefined flow, keep the default value, revenue_adv_q2o__CreateOrdersFromQuote. To use a custom flow, enter the API name of the flow that you created.
Save your changes.
To assetize orders using Assetize Order flow, asset managers should follow these steps:
From Setup, in the Quick Find box, find and select Flows.
From the Flow Label column, select Assetize Order.
Click Save As New Flow and enter a new name to override the original flow.
Edit the new flow.
Users can edit the flow as needed by selecting a node and then clicking Edit.
Save and activate your flow.
Set Up Product Configurator

Simplify product configuration for your quotes and orders with these settings.

From Setup, in the Quick Find box, find and select Revenue Settings.
Turn on Configure Products at Runtime.
Set Up Salesforce Pricing

To ensure accurate pricing for your quotes and orders, enable Salesforce Pricing for your org.

From Setup, in the Quick Find box, find and select Salesforce Pricing Settings.
Turn on Salesforce Pricing.
Verify that your Salesforce org has a default pricing procedure. To learn how to select a pricing procedure, see Select a Pricing Procedure.
To give sales reps detailed insights into each step of the pricing calculation process, turn on Price Waterfall. To turn on price waterfall, see Set Up Price Waterfall.
Set Up Contract Pricing

Use custom fields beyond the default product and selling model rules.

From Setup, in the Quick Find box, find and select Revenue Settings.
Turn on Customize Contract Pricing.
Additional Quote and Order Capture Setup

Set up features that provide your sales reps, partners, and customers with the capabilities required to efficiently manage quotes and orders.

From Setup, in the Quick Find box, find and select Revenue Settings.
Turn on the following settings.
Ramp Deals for Groups in Quotes and Orders
Ramp deals for groups make it easier for sales reps to break down complex, long-term deals for multiple products into smaller, time-based segments. Ramp deals for groups are supported only in the Sales Transaction Line Editor and aren’t supported in the Transaction Line Editor.
Enable Groups in quotes and orders
Allow users to group their line items in both quotes and orders
For a better quote and order capture experience, consider enabling these optional settings.
Clone Quotes and Orders
Hide Price Refresh Notification
To process quotes and orders more efficiently by applying custom rules based on attributes like size and complexity, turn on Transaction processing for quotes and orders.
This feature can't be turned off once it's activated.
To generate quote PDFs or order forms from the UI directly, turn on Document Builder.
To provide users the ability to recalculate prices immediately when they edit a line, instead of only upon saving the transaction, turn on Instant Pricing.
Users see the Instant Pricing setting on quotes and orders. By default, the setting is turned off on quotes and orders.
To turn on the Instant Pricing setting on quotes and orders by default, turn on Instant Pricing Active by Default.
This setting is available only after you turn on the Instant Pricing setting on the Revenue Settings page. Instant Pricing Active by Default is supported only in the Sales Transaction Line Editor and isn’t supported in the Transaction Line Editor.
To make sure pricing procedures can access sensitive data, and prevent users from accessing that data, turn on Elevated Data Access for Pricing Quotes and Orders.
After you turn on this setting, set restrictive field and object permissions for users based on your business requirements.
NOTE
To hide the notification that appears when quote or order prices aren’t updated, turn on the Hide Price Refresh Notification setting. However, we recommend that you keep the notification on, because hiding it may affect saving quotes and creating orders because you could be using outdated prices. After a user modifies any price-impacting fields, to refresh the prices, they can click Reprice All. 
Set Up As-Is Renewal

Offer customers greater pricing transparency and flexibility during renewals by locking in the original price for a portion of their assets. This process makes sure that all other subscriptions are accurately repriced and extended, and correctly handles complex renewals with varying quantities and prices.

From Setup, in the Quick Find box, find and select Revenue Settings.
Turn on As-Is Renewals.
Set Up the Line Editor in Transaction Management

Set up the Transaction Line Editor or Sales Transaction Line Editor on the Quote or Order record page so sales reps can organize, edit, and review transactions efficiently.

You can add and customize the line editor to manage how quote and order line items appear in the grid. See Add and Customize the Transaction Line Editor or Sales Transaction Line Editor.

Turn On Tax Calculations for Quotes and Orders

Provide customers the estimated tax on their quotes and orders.

Set up a tax engine and create a tax policy before you enable tax configurations for Revenue Management. To learn more, see Tax Configurations in Transaction Management.

From Setup, in the Quick Find box, enter Revenue, and then select Revenue Settings.
Turn on Add Estimated Taxes to Quotes and Orders.
NOTE After you enable tax calculations, ensure accurate tax details by verifying that the tax attributes are mapped and synced to their data source in SalesTransactionContext or your extended context definition. See Upgrade Context Definition.

To proceed with the rest of the Revenue Management setup, see Set Up Revenue Management.

=== ARTICLE: ind.qocal_understand_usage_selling_rate_cards.htm ===
---
article_id: ind.qocal_understand_usage_selling_rate_cards.htm
title: Set Up Rates for Usage-Based Products
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_understand_usage_selling_rate_cards.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_usage_selling.htm
fetched_at: 2026-09-04
---

# Set Up Rates for Usage-Based Products

When you sell a usage-based product, the rate definitions and the rating discovery procedure that you set up in rate management retrieves the rate for these products. These rates are available with the product details when you browse the product catalog.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Configure Rate Cards and Rate Card Entries

Rate cards define the type of rate that you want to set for the service. A base-type rate card defines the standard per-unit cost, whereas a tier— or adjustment-type rate card defines a discounted price based on the defined tiers or volume. For more information, see Create a Rate Card Entry For Tier Rate Cards.

To define the actual rate, standard or discounted, applicable to a service, use rate card entries. These rate card entries contain the actual financial data ($1 per minute). You can mark the entries as negotiable, allowing sales reps to update the rate during the selling process.

NOTE The rate defined in the rate card entries is applicable only if these entries are set to Active. If they’re Draft or Inactive, the corresponding rates won’t appear.
NOTE If rate cards don’t appear in the Price By Usage modal, verify the required setup. For details, see Unable to See Rate Cards in Price By Usage Modal.
Configure Tier Rate Cards for Commitment-Based Usage Products

In a commitment-based business model, tier rate cards determine how discounts apply on the volume, quantity, or monetary spend a customer has promised to consume.

To apply a resource-specific discount, create a rate card entry and specify a usage resource, such as Compute Hours or API Calls. Whereas to create a blanket discount that’s common across a user's entire account, leave the usage resource field empty.

EXAMPLE

Token Commitment—you can configure both, blanket or resource-specific discounts.

Blanket discount—A customer commits to consuming 1,000 tokens. You configure a "Token Commitment Flat" product that applies a flat discount of 10% across all usage resources. In this scenario, you leave the usage resource field empty. Therefore, every resource tied to the commitment receives the 10% discount.
Resource-specific discount—A customer commits to 5,000 tokens. Instead of a flat rate, you configure tier adjustments where you select the rates for each resource separately. In this scenario, you can select the usage resource for which you want the discount to apply. For example, you can define that their token commitment grants them a 30% discount specifically on DB Storage, while other resources might receive a different discount or no discount at all. You can also select a token resource while creating a rate card entry to provide a discount on tokens.

Monetary Commitment—similar to token commitments, you can configure both, blanket or resource-specific discounts.

Blanket discount—A customer agrees to spend $10,000. You configure a "Monetary Commitment Flat" product that applies a flat discount of 10% across all usage resources. In this scenario, you leave the usage resource field empty. Therefore, every resource tied to the commitment receives the 10% discount.
Resource-specific discount: A customer agrees to spend $5,000 in exchange for special rates. When setting up the tier adjustments, you can use the Is Included checkbox to specify the resources that benefit from the discount. For example, you can set up a 5% discount for Compute Time and a 10% discount for DB Storage, marking both as included. If you don’t mark a resource, such as Text Messages as included, it doesn’t benefit from the monetary commitment and is charged at the standard, undiscounted rate.

Quantity Commitment—quantity commitments are resource-specific, as the customer promises to consume a specific quantity of a usage resource.

Resource-specific discount: A customer commits to consuming 1,000 GB of DB Storage and 1,000 minutes of Compute Time. So, you define specific tier rate card entries for each resource. A 20% discount for every unit of DB Storage consumed, and a 10% discount for every minute of Compute Time consumed. As long as the customer doesn’t exceed their 1,000-unit limit for each respective resource, the discounted rates apply.
Map Rate Card to Price Books

When a sales rep creates a quote and selects a price book, make sure that you’ve linked the selected price book to the applicable rate card. Otherwise, the usage selling process can’t retrieve accurate rates applicable to a service.

Activate the Rating Discovery Procedure

Make sure that you select the applicable Rating Discovery Procedure in Revenue Settings. The selected procedure fetches the correct rates and discounts during the quoting process. For more information, see Select Rating Discovery Procedure.

EXAMPLE

Here are some use cases on how we can set up rate cards for our usage products.

For a standard mobile plan, the setup looks like this:

PRODUCT	RESOURCE	UOM	RATE UOM	RATE	NOTE
Mobile Plan	Text Messages	Count	USD	0.75	Text Messages are counted per message, and Data is measured per GB. Both are rated in USD.
Data	GB	USD	1.25

Calculating your bill: After the customer consumes the service, the system calculates their final charge based on the overage, which is the amount of usage that goes beyond any grants included in their plan. The system then applies the rate to that overage quantity. Here's how the charges are calculated based on your consumption:

Data: The customer consumed 102 GB. Because the plan includes a 2-GB grant, payment is only for the 100-GB overage (102 - 2 = 100). At a rate of $1.25 per GB, the charge is $125 (100 x $1.25).
Text Messages: The customer consumed 4500 messages. With a 4000 message grant, there’s a 500 message overage (4500 - 4000 = 500). At a rate of $0.75 per message, your charge is $375 (500 x $0.75).

For a mobile token-based plan, here's how the setup looks:

PRODUCT	RESOURCE	UOM	RATE UOM	RATE
Mobile Plan	Tokens	Each	USD	0.75
Text Messages	Count	Token	5
Data	GB	Token	10

To use tokens with a usage-based rate card, you're essentially creating a two-step currency conversion process for your products. First, customers buy virtual currency (tokens), and then they use those tokens to pay for their usage of a product or service. In this model, your rate card has two types of entries: one for the tokens themselves and another for each resource you offer.

RESOURCE	CONSUMPTION	TOKEN RATE	FINAL TOKENS
Data	102 GB	10 tokens per GB	102 x 10 = 1020 tokens
Text Messages	5500 messages	5 tokens per message	5500 x 5 = 27500 tokens

Calculating your bill: Usage Management calculates the total number of tokens used for each resource and then converts that total into a monetary value. The total number of tokens used is 28,520. If the customer had a grant of 5,000 tokens, their final overage is 28,520 - 5,000 = 23,520 tokens. At a Product Per Point (PPP) rate of $0.75 per token, the final charge is $17,640.

SEE ALSO
Enable Rate Management
Rate Card and Rate Card Entries
Clone the Default Rating Discovery Procedure
View Applicable Rates for Individual Assets

=== ARTICLE: ind.qocal_understanding_rate_on_packs.htm ===
---
article_id: ind.qocal_understanding_rate_on_packs.htm
title: Anchor Product with Packs
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_understanding_rate_on_packs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling_advanced_concepts.htm
fetched_at: 2026-09-04
---

# Anchor Product with Packs

An anchor product represents the primary usage-based product, such as QuantumBit Database Service. A pack is an add-on product that provides additional quantities of resources or offers different rates for the resources, such as a top-up or booster pack. For a pack to function as a top-up for the anchor, you must either bind the pack to an anchor or bind both the anchor and the pack to the same binding target, such as the same account.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Usage Entitlement Buckets

After the pack is bought and assetized, Consumption Management creates a parent usage entitlement bucket for the resource, such as SMS. This bucket represents the total available balance. The anchor creates the first child bucket containing the base grant, for example, 100 SMS. The pack creates a second child bucket containing the add-on grant, for example, 50 SMS. The parent bucket shows the total age of balance, which is the sum of all active child buckets (100 + 50 = 150 SMS).

Drawdown Logic

When consumption occurs, the system looks at the usage entitlement buckets. It draws down based on the drawdown order, for example, by drawing the grants that are expiring sooner. If the pack expires sooner than the anchor, the system uses the pack's grants first.

EXAMPLE A customer buys a Standard Mobile Plan (anchor) that grants 4,000 SMS messages per month. Mid-month, the customer realizes that they need more capacity and buys a Holiday Booster Pack (pack) that grants an extra 2,000 SMS messages for 15 days. This purchase results in these changes.
The wallet shows a total balance of 6,000 SMS messages.
Consumption Management creates two child buckets—one with 4,000 messages that are valid for 30 days and one with 2,000 messages, which are valid for 15 days.
Consumption Management deducts usage from the 2,000 SMS bucket first because it expires sooner.
Rate Applicability on Pack Products

When a pack product is bound to an anchor product, to ensure the most favorable pricing throughout the contract period, Usage Management determines the applicable rate by using certain rules.

Latest—assigns priority to the rate from the most recently purchased started asset that's currently active.
Cheapest—selects the lowest rate if multiple assets share the same start date.
EXAMPLE

Imagine a streaming service, Streamverse, that offers a base subscription and various promotional packs. A customer, Alex, buys a Standard subscription for the entire year (Jan 1 - Dec 31) at the rate of $10 per month. Over the year, the sales rep adds several new promotional packs to Alex's subscription.

PACK NAME	START DATE	EXPIRY DATE	RATE
Welcome Pack	Jan 15	Mar 15	$8
New Year Promo	Jan 15	Mar 31	$9
Spring Fling Promo	Feb 1	Apr 30	$7
Summer Blockbuster Pack	Jun 1	Aug 31	$6

Here's a breakdown of Alex's monthly bill based on the latest and cheapest rules:

DATE RANGE	APPLICABLE RATE	REASON
Jan 1 - Jan 14	$10	Standard subscription is the only active anchor.
Jan 15 - Jan 31	$8	Welcome Pack and New Year Promo both start on Jan 15. Welcome Pack has the cheapest rate ($8).
Feb 1 - Mar 15	$7	Spring Fling Promo starts on Feb 1. Its rate of $7 is the latest and cheapest among all active packs.
Mar 16 - Mar 31	$7	Welcome Pack expires. Spring Fling Promo is still the latest and cheapest of the remaining active packs.
Apr 1 - Apr 30	$7	New Year Promo expires. Spring Fling Promo is still the latest and cheapest.
May 1 - May 31	$10	Spring Fling Promo expires. The rate reverts to the Standard Subscription rate.
Jun 1 - Aug 31	$6	Summer Blockbuster Pack starts on Jun 1. Its rate is the latest and cheapest.
Sep 1 - Dec 31	$10	Summer Blockbuster Pack expires. The rate returns to the Standard Subscription rate.

=== ARTICLE: ind.qocal_usage_selling.htm ===
---
article_id: ind.qocal_usage_selling.htm
title: Sell Usage-Based Products
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_usage_selling.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quote_and_order_capture.htm
fetched_at: 2026-09-04
---

# Sell Usage-Based Products

Sell products that are billed based on the consumption. When you create quotes and orders, you can view, edit, and reprice the rates, commitments, and grants for resources included in the usage-based products to fit your deal.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Set Up Usage Selling in Revenue Management
Before you begin selling usage-based products and services, make sure that you’ve completed the required set up. You must define usage products, resources, and the grants, commitments, and entitlements offered with the products. Define policies that govern these products and services. Then, set up rates for each of these products and services.
Usage Selling Advanced Concepts
Determine the scope of resource pooling with grant binding, and manage resource consumption and rating using anchors and packs. You can also define drawdown logic, rate applicability rules, and discounted commitment models.
Build a Quote for Usage-Based Products
Create quotes for usage-based products that meet your customer’s needs. Review the resources included with the product, including the granted quantity and rates.
Sell Commitment-Based Usage Products
For selling commitment-based usage products, a sales rep must follow a three-step process—creating the anchor product, creating the commitment product, and linking the anchor and commitment products together.

=== ARTICLE: ind.qocal_usage_selling_advanced_concepts.htm ===
---
article_id: ind.qocal_usage_selling_advanced_concepts.htm
title: Usage Selling Advanced Concepts
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_usage_selling_advanced_concepts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_usage_selling.htm
fetched_at: 2026-09-04
---

# Usage Selling Advanced Concepts

Determine the scope of resource pooling with grant binding, and manage resource consumption and rating using anchors and packs. You can also define drawdown logic, rate applicability rules, and discounted commitment models.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Grant Binding
Grant binding determines how the grants of resources contained in an asset are pooled and consumed. In simpler terms, the binding decides whether a purchased service (like 1,000 text messages) is related to a single asset or shared across a wider group, such as an organization or a specific contract.
Anchor Product with Packs
An anchor product represents the primary usage-based product, such as QuantumBit Database Service. A pack is an add-on product that provides additional quantities of resources or offers different rates for the resources, such as a top-up or booster pack. For a pack to function as a top-up for the anchor, you must either bind the pack to an anchor or bind both the anchor and the pack to the same binding target, such as the same account.
Anchor Product with Token Commitments
A token acts as a virtual currency, such as Flex credits or Salesforce credits. In the token-commitment model, your user purchases a quantity of tokens that has a standard conversion rate to a dollar for each service, such as SMS and data.
Anchor Product with Quantity Commitments
In a quantity commitment, the customer agrees to consume a specific number of units for a specific resource, for example, 100 GB of storage or 10,000 API calls.
Anchor Product with Monetary Commitments
In a monetary commitment, your customer agrees to spend a specific dollar amount, for example, $1,000 per month. Monetary commitment products are used when your customer wants a discount on the overall spend and doesn’t want the discount to be tied to a specific resource type, such as SMS or storage.
Saving Usage Rates for Quotes and Orders
Automatically save current usage rates by generating rate card entries when you save a quote or order. This process helps maintain rate consistency for the duration of the sale, even if the product catalog is updated later.

=== ARTICLE: ind.qocal_usageselling_record_sharing_settings.htm ===
---
article_id: ind.qocal_usageselling_record_sharing_settings.htm
title: Configure Record Sharing and Sharing Rules for Usage Selling
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_usageselling_record_sharing_settings.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_usage_selling.htm
fetched_at: 2026-09-04
---

# Configure Record Sharing and Sharing Rules for Usage Selling

For users to access the data created by usage designers or catalog admins, Setup record sharing for all usage-related objects. This configuration is crucial for the seamless execution of usage selling processes within Salesforce.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create and edit sharing settings:	

Manage Sharing

From Setup, in the Quick Find box, enter Security, and then select Sharing Settings.
Click Edit.
Set the organization-wide defaults for these Usage Selling objects.
	
Object	Organization-Wide Defaults
Quote	All Partner Users Read/Write
Opportunity	All Partner Users Read/Write
Price Book	Public Read Only
Price Book Rate Card	Public Read Only
Binding Object Custom Extension	Public Read Only
Save your changes.
In the Sharing Rules section, click New against the object’s sharing rule that you want to define a rule for.
Give your rule a label, a name, and, if necessary, a description.
Select Guest user access, based on criteria as the rule type.
Specify the field, operator, and value criteria to filter the records to be included in the sharing rule.
The fields available depend on the object selected, and the value is always a string or number.
Specify the users that you want to provide access to the data.
Save your changes.

=== ARTICLE: ind.qocal_use_default_revenue_pricing_procedure.htm ===
---
article_id: ind.qocal_use_default_revenue_pricing_procedure.htm
title: Use the Default Revenue Management Pricing Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_use_default_revenue_pricing_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-04
---

# Use the Default Revenue Management Pricing Procedure

While you can create custom pricing procedures, we strongly recommend using the predefined versions. These predefined procedures bring consistency to your org and deliver accurate calculations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User
To use pricing procedures:	Salesforce Pricing Run Time User

Predefined pricing procedures are associated with the PricingTransactionCD context definition and the Pricing usage type. If you want to change the context definition, you can clone and use the prebuilt pricing elements. However, remember that:

You can’t change the usage type.
Modifying the context definition can result in inaccurate context mappings.
From the App Launcher, find and select Expression Set Templates.
Change the list view to All Expression Set Templates.
Select the Revenue Management Default Pricing Procedure Procedure.
Clone and save the expression set template as a new pricing procedure.
Use the prebuilt pricing elements required for your scenarios. Add or delete elements based on your pricing needs.
After you modify your procedure, simulate and activate your procedure.
To use the modified pricing procedure when pricing line items in Agentforce Revenue Management, follow the steps below.
From Setup, in the Quick Find box, enter Revenue Settings, and then select Revenue Settings.
In the Set Up Salesforce Pricing section, select your custom pricing procedure.

To understand the functionality of each pricing element and relevant use cases, see Use Pricing Elements in Pricing Procedures.

SEE ALSO
Select a Pricing Procedure
Prerequisites to Build Pricing Procedures
Simple Pricing Procedure Example
Use Pricing Elements in Pricing Procedures
Unique Pricing Scenarios

=== ARTICLE: ind.qocal_use_delta_pricing_for_quotes_and_orders.htm ===
---
article_id: ind.qocal_use_delta_pricing_for_quotes_and_orders.htm
title: Set Up Delta Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_use_delta_pricing_for_quotes_and_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_set_up_quote_and_order_features_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Set Up Delta Pricing

Improve large transaction performance by enabling Delta Pricing to recalculate only modified quote or order lines and their dependencies.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

Delta Pricing optimizes performance by recalculating only modified quote or order lines and their dependent lines rather than the entire transaction. This background process requires no at run time user interface changes. The system applies Delta Pricing automatically to transaction updates that lack validation errors and follow a successful previous pricing run. If the transaction fails to meet these criteria, the system performs a full repricing.

IMPORTANT Turn off Dual Persistence mode before you use Delta Pricing, as these features are incompatible.
From Setup, in the Quick Find box, search for and select Revenue Settings.
Turn on Delta Pricing for Quotes and Orders.

=== ARTICLE: ind.qocal_use_tiered_volume_and_pricing_in_contract_pricing.htm ===
---
article_id: ind.qocal_use_tiered_volume_and_pricing_in_contract_pricing.htm
title: Set Up Tiered Contract Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_use_tiered_volume_and_pricing_in_contract_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_manage_contract_pricing_in_revenue_lifecycle_management.htm
fetched_at: 2026-09-04
---

# Set Up Tiered Contract Pricing

Negotiate prices and discounts based on purchase quantities to encourage larger sales and apply customer-specific adjustments to ongoing transactions. Managing these agreements helps you to create volume tiers against a contract item price record and view the calculations in the net unit price waterfall.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To set up tiered volume adjustments to pricing in contracts:	Salesforce Pricing Design Time User
Verify Decision Tables

Before you begin, verify that the pricing procedure uses updated decision tables.

Open your pricing procedure.
Expand the Volume Discount element and review the Lookup Table Details.
Verify that the decision table selected is Contract Pricing Volume Tiers. If it isn’t, change accordingly.
Refresh the decision tables.
From Setup, in the Quick Find box, search for and select Decision Tables.
Select Contract Pricing Volume Tiers, and click Refresh.
Apply Tiered Pricing to Quotes
From the App Launcher, find and select Contracts.
Click New to create a contract or select an existing contract from the list.
Associate the contract with the RevenueLifecycleManagement application usage assignment tag.
In the Contract Item Prices section on the Related tab, click New to create contract item price records or select an existing record.
Enter values in the fields for the contract item price, and save your work.
On the contract item price record, select the Related tab and click New in the Contract Item Price Adjustment Tiers section.
Enter values in the fields for the first tier and save your changes.
Create more tiers.
Set the value of the lower bound of the new tier to the same value as the upper bound of the previous tier.
NOTE The upper bound quantity is priced exclusively at run-time.
On the contract, select the Related tab, and then click New in the Quotes section.
Enter values in the fields for the quote, and save your changes.
Add the product as a quote line item and set the quantity.
Save your changes.
Move the quantity to the next volume tier and select the net unit price to see the price calculations change based on the product volume change.
When you save, the volume-adjusted price discount is applied to the quote.
Create an order from the quote, save your changes, and activate the order.
Volume-based price adjustments are included in the order.
EXAMPLE

This table shows how to set up tiers to apply percentage discounts based on the quantity purchased.

TIER TYPE	LOWER BOUND	UPPER BOUND	TIER VALUE
Percentage	1	10	5
Percentage	10	20	10
Percentage	20	30	15
Override Default Sequencing for Tiered or Volume Contractual Discounts

Specify the order in which the system applies tiered or volume contractual discounts to products in a transaction. By default, the system sorts transaction line items by quantity, but sales reps can define a custom order by using a field configured by contract managers.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To configure the sequencing on Transaction Line Editor for quotes and orders:	

Edit on quotes

AND

Edit on orders

Before you begin, verify that your contract manager configured a field to override the default quantity-based sorting for tiered volume discounts. See Manage Line Item Sequencing for Tiered Volume and Price Adjustments.

Open a quote or order.
For each line item in the transaction, enter a sequence number starting with one in the field configured for sequencing tiered volume discounts. If you specify partial or no sequence numbers, the system sequences line items by quantity by default.
Save your changes.

=== ARTICLE: ind.qocal_user_experience_and_customization.htm ===
---
article_id: ind.qocal_user_experience_and_customization.htm
title: User Experience and Customization
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_user_experience_and_customization.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_foundational_setup_for_quotes_and_orders.htm
fetched_at: 2026-09-04
---

# User Experience and Customization

Personalize the sales and partner experience by customizing Transaction Management visual elements and actions. Use these steps to refine the interface and streamline workflows.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
Personalize the Transaction Management Experience
Deliver an intuitive sales and partner experience by customizing Transaction Management visual elements and actions.
Manage Product Visibility with Filters
Use predefined and advanced filters to control which quote or order line items appear in the line editor. Filtering helps sales representatives manage complex quotes by focusing on specific product groups or line item statuses.

=== ARTICLE: ind.qocal_view_and_edit_orders.htm ===
---
article_id: ind.qocal_view_and_edit_orders.htm
title: View and Edit Orders in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_view_and_edit_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quotes_and_orders_in_the_revenue_cloud.htm
fetched_at: 2026-09-04
---

# View and Edit Orders in Revenue Management

The order page lists product and pricing details. Use this workspace to add, remove, and manage products within your transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To view and edit orders:	Read and Edit on orders
To configure products:	Product Catalog Management Viewer permission set
To price products:	Price and Tax Calculation for Quoting permission set
To activate orders:	Activate Orders app permission
To enter decimal quantities for order products and view unit of measure fields:	DecimalQuantityRuntime permission set
Add Products

Select a price book and add products to an order to begin the pricing process. Associate all products in a transaction—including child products—with the same price book to ensure consistent and accurate pricing.

Establish a price book when you first add products via the search field or catalog.
Find and add products by using one of these methods:
Click Browse Catalogs to find, configure, and add products from specific catalogs.
Use the Add Product search field to locate and add items quickly.
Select Add Assets to include existing assets for initial sale orders.
Review product names and catalogs that add items as unsaved transient lines. You can’t edit the items until you save your changes.
Save the order to create order products and their related attribute records.
Transaction Management copies attribute values to subsequent stages, such as when an order is assetized.
If a catalog admin turns off product attributes after this step, existing order product attributes remain unchanged.
Customize the Order Products Section

Modify the Order Products section to improve navigation before editing transactions.

Keep the Product Name or other fields visible while scrolling by clicking Freeze up to this Column on a specific field.
Show the filter row to search columns in large transactions or hide it to at no additional cost up vertical space.
Edit Transactions

Update product attributes and configurations directly within the Order Products section on the Lines tab.

Avoid editing the Net Unit Price, Net Total Price, Total Adjustment Amount, or Pricing Term Count fields if Salesforce Pricing is active.
Update line items.
Click an attribute cell to change its value and save.
To perform bulk updates, select multiple items, click the attribute on one item, and save.
Use the Sales Transaction Line Editor for bulk actions on both line items and groups.
Wait for the system to finish its tax calculation before changing the order.
Save changes promptly to avoid losing edits from a page reload or an expired session.
Enter decimal quantities.
Enter decimal values only if a product has an associated unit of measure.
Transaction Management rounds values based on the record's scale and rounding method.
The editor shows two decimal places, but the system stores the exact scale specified.
View the full decimal value by clicking the quantity cell or opening the side panel.
Open the Order Product page from the related list to delete the current discount value if the editor prevents switching between percentage and amount. Then, enter the new value and type directly in the line editor.
Manage lookups and renewals.
Click lookup fields like Legal Entity to search for records or create ones directly in the editor.
Select Automatically Renew for Term-Defined products; this status copies to assets upon assetization.
Filter and Group Lines
Expand the dropdown arrow on the top row to filter multiple columns and isolate parent line items, as the system excludes child items from results.
Build a hierarchical structure with up to five levels of line items and nested groups to show financial subtotals for every level.
Manual - Click Add Group to organize items. Move items by using Move Selected Items. Use the load more if a target group isn’t visible.
Automatic - Select Group By on a column in the Transaction Line Editor to organize items. The Sales Transaction Line Editor and Formula fields don’t support this option.
Sequence - Define the order by using the Sort Order field on the Order Product Groups related list. Groups without a value appear at the end, sorted by creation date.
Calculate and View Prices
Update prices after making edits by clicking Save to price the order.
Turn on Instant Pricing to recalculate price-impacting changes immediately, noting that the feature turns off automatically upon page reload or session expiry.
Refresh the entire transaction by clicking Reprice All, or use Refresh Prices when a warning message appears.
Project tax for the transaction by clicking Estimate Taxes.
Hover over the Net Unit Price to see the price waterfall, which shows adjustments for bundles, tiers, attributes, derived prices, and contract prices.
Hover over the Total Price to see the bundle parent price, the sum of line items, and the bundle subtotal.
SEE ALSO
Transaction Management Limits

=== ARTICLE: ind.qocal_view_and_edit_quotes.htm ===
---
article_id: ind.qocal_view_and_edit_quotes.htm
title: View and Edit Quotes in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_view_and_edit_quotes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_quotes_and_orders_in_the_revenue_cloud.htm
fetched_at: 2026-09-04
---

# View and Edit Quotes in Revenue Management

Use the Transaction Line Editor or Sales Transaction Line Editor to add, configure, and price quotes in Revenue Management (formerly Revenue Cloud). These editors provide a centralized workspace to manage product selections, apply discounts, and verify pricing details before final submission.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS
NEEDED
To use the Transaction Line Editor or Sales Transaction Line Editor:	

Manage Revenue Management

AND

Create Orders from Quotes permission set

AND

Price and Tax Calculation for Quoting


To enter decimal quantities for quote line items and view unit of measure fields:	DecimalQuantityRuntime permission set

When you add products for the first time, select a price book to establish accurate pricing. To ensure consistency, associate all products in a transaction—including child products—with the same price book. Transaction Management copies attribute values and auto-renewal statuses to subsequent stages, such as when you convert a quote into an order.

Add Products to Quotes

Select a price book and add products to a transaction to begin the pricing process. Products that use the catalog automatically relate to the same price book, ensuring consistent and accurate pricing across all items.

Establish a price book when you first add products via the search field or catalog. To learn more about price books, see Define Prices in Price Books.
Find and add products by using one of these methods.
Click Browse Catalogs to find, configure, and add products from specific catalogs.
Use the Add Product search field to locate and add items quickly.
Select Add Assets to include existing assets for initial sale quotes.
Review transient lines. The system adds products as unsaved transient lines in the quote line items section. You can’t edit these lines until you save your changes.
Save the quote. Saving creates quote line items and related attribute records.
Transaction Management automatically copies these attribute values to subsequent stages, such as when you create an order from the quote.
If a catalog admin turns off product attributes after this step, the existing quote line item’s attributes remain unchanged.
Verify product visibility. The Quote Line Items section shows all root products. Child products appear only if you leave the Quote Visibility field unselected or set it to Always or Transaction Line Editor.
Customize the Quote Line Items Section

Modify the editor workspace to improve navigation before editing your transactions.

Freeze essential columns for easier scrolling. Click Freeze up to this Column on a specific field.
For example, freeze the Product Name column to keep it visible while scrolling through pricing or attribute data.
Manage the filter row for large transactions.
Select the option to show the filter row to search or filter columns for line items.
Hide the filter row when it’s no longer needed.
Edit Transactions

Update product attributes, pricing, and configurations directly within the line editor to refine your quote. Use the Quote Line Items section on the Quote Line Items tab to apply these changes.

Review pricing and formula constraints.
Avoid editing the Net Unit Price, Net Total Price, Total Adjustment Amount, or Pricing Term Count fields if Salesforce Pricing is active.
Reference derived lookup fields only by their ID when creating custom formula fields. Spanning fields, such as Quote.AccountId and QuoteLineItem.ParentQuoteLineItemId aren’t available for use.
Update individual or multiple line items.
Click a specific attribute cell, such as Quantity, to update its value and save your changes.
To perform bulk updates, select multiple items, click the attribute on one selected item, enter the new value, and save. The editor applies the value to all selected items.
Use the Sales Transaction Line Editor to perform these bulk actions on both line items and groups.
Save changes promptly, as the system clears unsaved edits if the page reloads or the session expires.
Enter decimal quantities.
Provide decimal values only for products with an associated unit of measure record.
The editor shows values rounded to two decimal places, but Transaction Management stores the exact scale specified in the unit of measure record.
Click the Quantity cell or open the side panel to view the full decimal value.
Modify discount types.
Open the Quote Line Item page from the related list if the editor prevents switching between Discount (Percentage) and Discount (Amount).
Delete the current discount value, then enter the new value and type directly in the line editor.
Manage lookup fields and renewals.
Click a lookup field, such as Legal Entity, to search for existing records, or create a record directly within the section.
Select Automatically Renew for products by using the Term-Defined selling model. Transaction Management copies this status to subsequent stages, such as the order.
Filter Quote and Order Line Items

Apply filters to isolate specific products that meet your criteria and manage large transactions effectively.

Click the caret icon on the top row of the line editor to show the filter criteria fields.
Enter search terms or values in one or more columns to narrow the visible list.
Use the Discount column to find specific reductions.
To find amount-based discounts, enter the numeric value, such as 10.
To find percentage-based discounts, enter the value with the percent symbol, such as 10%.
Review filtered results. Filtering applies only to parent line items. If your quote contains bundles, the editor excludes child items from the filter results.
Group Quote or Order Line Items

Group lines to view transactions, create streamlined proposals, and view financial subtotals for different hierarchy levels. You can build a hierarchical structure with up to five levels containing both line items and nested groups in a single table.

From Setup, search for and select Revenue Settings. Turn on Enable Groups in quotes and orders. If you group a transaction, assign every line item to a group.
Organize lines manually from a quote record.
Click Add Group to move all existing lines into an initial group.
To create more groups, click Add Group again.
Give a name or description to each group to identify its contents.
Select specific lines or groups and click Move Selected Items to change their assignment.
Click load more at the end of the group list if your target group isn’t currently visible in the editor.
Organize lines automatically.
In the Transaction Line Editor, click the down arrow icon on a groupable column and click Group By.
For example, you can group by the Location column to organize items by their delivery site.
Automatic grouping is unavailable in the Sales Transaction Line Editor and doesn’t support formula fields.
Define the display sequence by entering values in the Sort Order field on the Quote Line Groups related list.
The system places groups without a sort order value at the end of the list, sorted by their creation date.
Click Ungroup to return the transaction to a flat list.
The system automatically carries your nested group structure over when you convert a quote into an order.
Calculate Prices and Taxes

Update your quote with the latest pricing and tax data to ensure financial accuracy.

On a quote record, update prices after making inline edits like quantity changes or manual discounts by clicking Save.
Recalculate prices immediately after every configuration or line item change by enabling Instant Pricing.
Instant Pricing only recalculates lines with price-impacting changes.
Instant Pricing turns off automatically when you reload the page or when your session expires.
Refresh the entire transaction.
Click Reprice All to refresh prices across the entire quote or order.
Click Reprice All or Refresh Prices to reprice the transaction manually when a warning message appears in the Quote Line Items section. Reprice All refreshes pricing and skips configuration. Refresh Prices refreshes pricing, configuration, and taxes for the transaction.
Calculate the transaction by clicking Estimate Taxes.
Derive Prices

Calculate the price of a product based on another pricing source, such as a percentage of the quote subtotal or the net price of a source product. This process, known as Transactional Derived Pricing Scope, helps you to automate costs for items like service charges or extended warranties.

For information on configuring a derived pricing product in Salesforce Pricing, see Implement Derived Pricing.

TIP The Derived Price feature is applicable to orders as well.
Add a derived pricing product to the quote to calculate prices based on factors like a percentage of the subtotal.
Update the derived price by clicking Save. If Instant Pricing is active, the price updates automatically when you add or delete line items.
Streamline the quoting and ordering process by turning on Add Derived Pricing Assets to a Quote or Order in the Revenue Settings page.
This setting automatically includes derived products whenever you add a contributing source product.
View Prices

Use the Quote Line Items section to review pricing details and adjustment breakdowns for your transaction.

View the price waterfall for a line item by hovering over its Net Unit Price.
Review pricing adjustments including bundle, tier, and attribute changes.
Verify discount percentages with up to two decimal places and amount adjustments based on the currency scale.
Access these details for both saved line items and transient lines.
Identify specific details for derived prices or contract prices.
Hover over the Total Price to see the bundle parent price, the sum of line items, and the bundle subtotal.
Go to the Quote Summary section to see a complete pricing breakdown, including all transaction discounts.
Group lines to see the total price for a specific field or set of items.
For example, group by Location to view the financial total for that specific site.
SEE ALSO
Transaction Management Limits

=== ARTICLE: ind.qocal_view_and_manage_assets.htm ===
---
article_id: ind.qocal_view_and_manage_assets.htm
title: Manage Assets in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_view_and_manage_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_view_and_manage_assets_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Manage Assets in Revenue Management

To track and oversee your purchased products, use the Assets tab on account and contract pages to view and edit asset records. From this centralized view, you can perform essential lifecycle tasks like changing renewal terms or enabling auto-renewal. Transaction Management copies the auto-renewal status to subsequent stages, such as copying the status from a contract's assets to corresponding quote line items.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
USER PERMISSIONS NEEDED
To view accounts:	View on Account
To view contracts:	View on Contract
To manage assets and use the Managed Asset Viewer component:	

Manage Revenue Cloud user permission set

AND

Read, Create, Edit, and Delete on Assets

IMPORTANT

The Manage Revenue Cloud user permission is granted to users via a permission set. Confirm that the permission set includes a permission set license that enables the Manage Revenue User system permission, such as the Revenue Cloud User permission set license.

Review the asset state period and specific asset actions to understand the history and the current status of your products.

NOTE Selecting the checkbox in the Managed Assets header selects only the currently loaded assets.
From the App Launcher, find and select Accounts or Contracts.
Select a record.
Open the Assets tab.
To open the side panel and view asset details, click an asset name.
To edit an asset, click  corresponding to the asset, and then click Edit.
Edit the fields and save your changes.
To see the asset state period and asset actions, click  corresponding to the asset, and then click View.

For more information, see How Lifecycle Management Works

SEE ALSO
View Applicable Rates for Individual Assets

=== ARTICLE: ind.qocal_view_and_manage_assets_in_revenue_cloud.htm ===
---
article_id: ind.qocal_view_and_manage_assets_in_revenue_cloud.htm
title: View and Manage Assets in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_view_and_manage_assets_in_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle.htm
fetched_at: 2026-09-04
---

# View and Manage Assets in Revenue Management

Use the Assets tab on account and contract pages to track and oversee purchased products and services. This centralized view helps you to perform essential lifecycle tasks, such as changing renewal terms or enabling auto-renewal.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

For usage-based products, the Asset record page includes a specialized Usage Rates tab that provides visibility into customer consumption and pricing structures. Reviewing these rate cards helps you understand the exact financial and resource parameters associated with an asset before you begin tasks like amendments or renewals.

Manage Assets in Revenue Management
To track and oversee your purchased products, use the Assets tab on account and contract pages to view and edit asset records. From this centralized view, you can perform essential lifecycle tasks like changing renewal terms or enabling auto-renewal. Transaction Management copies the auto-renewal status to subsequent stages, such as copying the status from a contract's assets to corresponding quote line items.

=== ARTICLE: ind.qocal_zero_quantity_considerations.htm ===
---
article_id: ind.qocal_zero_quantity_considerations.htm
title: Zero-Quantity Quote Detail Lines Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.qocal_zero_quantity_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: transaction_mgmt
parent_article: ind.qocal_asset_lifecycle_considerations.htm
fetched_at: 2026-09-04
---

# Zero-Quantity Quote Detail Lines Considerations

Zero-quantity quote detail lines appear when the lifecycle transaction state must be preserved even though the effective quantity for a period equals zero.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled

These instances create zero-quantity detail lines.

When an amendment changes an attribute and reduces the quantity from the current value to zero.
When an amendment shortens or extends the duration of an asset lifecycle.
When you override the default renewal term and specify a custom start date instead of waiting for automatic renewal creation. In this case, the transaction sets the quantity to zero for the renewal period to represent a pause state rather than a complete cancellation.
How to Interpret Zero-Quantity Detail Lines
Amendment and renewal transactions can create detail lines that preserve lifecycle history across original and updated periods.
Cancellation and repricing lines represent different lifecycle states, including valid zero-quantity periods.
A zero-quantity period alone doesn't mean that the asset is permanently cancelled.
Assetization records these transitions in asset state and action source data to maintain transaction continuity.

