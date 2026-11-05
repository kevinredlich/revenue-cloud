# Salesforce Help 264 — área: pricing (155 artículos)

=== ARTICLE: ind.pricing_access_your_pricing_information.htm ===
---
article_id: ind.pricing_access_your_pricing_information.htm
title: Access Your Pricing Information
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_access_your_pricing_information.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Access Your Pricing Information

View your product pricing either in a simple list view or using custom grid components making it easier to analyze and compare data. Use the discount calendar to show all applied discounts for a product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

You can view pricing data through a dynamic grid component that populates with information created to define your product pricing. For flexibility, dedicated Lightning components allow you to see this data in either the grid-like layout or switch back to a traditional list view.

For a more detailed analysis, pricing analysts can use the pricing discount calendar to easily see and understand the diverse discounts associated with a product. This calendar provides a comprehensive view by showing all applied price adjustment schedule types for a product and the range of discounts across different dates. To refine the view, users can group discounts by their respective schedule types, such as Volume, Attribute, and Bundle. It is also possible to search for a particular schedule type by using available filters.

Pricing Discount Calendar
Pricing analysts can easily see and understand the diverse discounts associated with a product through the pricing discount calendar.
View Pricing Data Using Lightning Components
Use dedicated Lightning components to view your data in either grid-like layout or move it back to list view.

=== ARTICLE: ind.pricing_add_aggregate_price_element.htm ===
---
article_id: ind.pricing_add_aggregate_price_element.htm
title: Calculate Aggregate Prices for Products
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_aggregate_price_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Calculate Aggregate Prices for Products

Determine the aggregate prices of a group of products by defining aggregation at multiple line item layers and ensuring pricing is calculated at the configured levels.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Aggregate pricing summarizes prices at different levels of your sales process, providing a clear understanding of costs for bundles, quotes, or specific quote sections. The Roll-Up feature within Aggregate Price defines how prices consolidate, allowing you to specify fields like list price, discount, or net price for inclusion. By selecting Roll Up Price, you can calculate a group's total cost by first determining each child product's price and then adding that to a parent product.

IMPORTANT

Aggregate Pricing doesn't support derived products on quote line items.

To ensure accurate calculations, we recommend placing the Aggregate Price element after the Derived Price element within your procedure. You should also include a Where condition to target only the contributing lines. This approach maintains consistency when using the Map Line Item element in discovery procedures for derived pricing.

Use the Aggregate Price Element
Aggregate and show the price of a group of products based on product categories, product types, or other groups of line items.
Roll Up Pricing Using the Aggregate Price Element
Calculate the total price of a group of products using the Roll Up Price option using the Aggregate Price element. When you enable roll up price, the element first determines the price of each child product, and then, adds the total to a parent product.

=== ARTICLE: ind.pricing_add_attribute_based_price_element.htm ===
---
article_id: ind.pricing_add_attribute_based_price_element.htm
title: Attribute-Based Discounts
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_attribute_based_price_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Attribute-Based Discounts

To calculate a product's price based on its associated attributes, use the Attribute-Based Price element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

An attribute is a characteristic of a product, such as its price, color, material, or other relevant features. When you configure this price element, attributes can influence a product's price, thereby giving businesses greater control over how they sell specific products.

For example, imagine you want to offer different configurations for your printers, such as a standard printer versus a wireless printer. The key difference here is their configuration. By designating the configuration as a price-impacting attribute, you can offer different pricing based on the customer's selection.

Set Price Impacting Attributes for Products
Simplify the selling experience for your sales reps using price-impacting attributes when selling your product.
Create Attribute Based Adjustments
Set up pricing rules that automatically adjust prices and offer discounts based on a product's price-impacting attributes by creating attribute-based adjustment records.
Calculate Attribute-Based Discounts
Determine the price of a product based on the discounts configured for selected price impacting attributes.
Attribute-Based Pricing Limits
Keep these guidelines in mind when configuring attribute-based adjustments.
Considerations for Migrating Attribute-Based Adjustments
To prevent hash mismatch issues when you migrate attribute-based adjustment records across Salesforce orgs, follow this process.

=== ARTICLE: ind.pricing_add_bundle_based_price_element.htm ===
---
article_id: ind.pricing_add_bundle_based_price_element.htm
title: Bundle-Based Price
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_bundle_based_price_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Bundle-Based Price

Define and manage bundle-based discounts for a group of products that are sold as a unit.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Bundling products and services offers significant advantages for sales representatives, streamlining the sales process and boosting revenue. By combining products into a single offering, sales reps provide a clear price advantage over individual purchases, encouraging customers to buy more than initially intended. This strategy increases sales volume and achieves a higher average order value per transaction.

Bundle-based pricing effectively drives sales and enhances the customer experience. This approach simplifies the buying process, making it easier for customers to choose and purchase multiple items. Additionally, bundling assists with inventory management by pairing slower-selling products with popular ones.

Create Bundle Based Adjustments
Define bundle based adjustments to calculate discounts for products being sold as a bundle.
Calculate Bundle-Based Discounts
Determine the price of a product based on the discounts configured for a set of products sold as a bundle.

=== ARTICLE: ind.pricing_add_calculate_price_button.htm ===
---
article_id: ind.pricing_add_calculate_price_button.htm
title: Add the Calculate Price Button
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_calculate_price_button.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_standard_pricing_actions.htm
fetched_at: 2026-09-07
---

# Add the Calculate Price Button

To make the standard button for pricing action visible on your object’s record page, configure the object’s page layout from Object Manager.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To edit page layouts:	Customize Application

Before you begin, define the pricing parameters that connect the pricing action button to your context definition, mapping, and pricing procedure. See Configure Pricing Action Parameters for Standard Objects

IMPORTANT

Salesforce Pricing doesn't work directly with the SalesTransactionContext__stdctx base context definition. To configure Standard Pricing Actions, always extend the base context. An extended context definition inherits the structure, nodes, and attributes from the base context definition while allowing you to add custom nodes, attributes, and tags for your pricing logic.

The standard Calculate Price button is only for pricing Salesforce objects and doesn't support custom data hydration.

The more complex Quotes and Orders logic, which uses custom hydration for bundles and derived products, requires a custom-built pricing button that can act on persisted (saved) data. Therefore, the standard button should not be considered a replacement for Transaction Management's pricing logic.

From Setup, in Object Manager, select any one of these objects: Quote, Order, Contract, Case, and Opportunity. For example, let’s select Opportunity.
Select Page Layouts, and then click Opportunity Layout.
In the palette, click Buttons.
Drag Calculate Price to the Opportunity Detail section under Salesforce Mobile and Lightning Experience Actions in the layout.
Save your changes.

=== ARTICLE: ind.pricing_add_context_tags_automatically_to_your_pricing_elements.htm ===
---
article_id: ind.pricing_add_context_tags_automatically_to_your_pricing_elements.htm
title: Update Context Tags to Pricing Elements with Einstein AI
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_context_tags_automatically_to_your_pricing_elements.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_einstein_generative_ai_for_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Update Context Tags to Pricing Elements with Einstein AI

On a pricing element, get gen AI to suggest and map variables to context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Salesforce Pricing is enabled
USER PERMISSIONS NEEDED
To create pricing procedures:	Salesforce Pricing Design Time
To use gen AI:	Prompt Template User
Create a pricing procedure and add a pricing element. See Configure Your Pricing Procedure.
To map your context tags, select Auto Populate Context Tags.

To check the accuracy of the updated tags, hover on the indicator next to the variable fields to see the confidence score.

NOTE Context tags can't be mapped automatically for these pricing elements:
Discount Distribution Service
Formula Based Pricing
Stop Pricing

=== ARTICLE: ind.pricing_add_list_price_element.htm ===
---
article_id: ind.pricing_add_list_price_element.htm
title: Fetch the List Price of a Product
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_list_price_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Fetch the List Price of a Product

To get the base price of a product for pricing procedure execution, use the List Price element. The list price serves as a starting point for calculating the final price before applying any discounts or adjustments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User

An organization might have different prices for the same product, depending on scenarios such as sales territories or sales cycles. These various list prices for products are tracked as price book entries within a price book.

In a pricing procedure, the list price of a product or line item is fetched from the Price Book Entries decision table. If you are calculating the derived price of a product, fetch the list price from the Price Book Entries V2 decision table.

NOTE If the decision table doesn't return a match for a line item, the List Price element retains the values that preceding elements calculated for output variables, such as List Price and Subtotal. The element doesn't reset these values to zero.

Let's explore using the List Price element in a pricing procedure:

Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Simulate and activate your pricing procedure.

=== ARTICLE: ind.pricing_add_manual_discount_element.htm ===
---
article_id: ind.pricing_add_manual_discount_element.htm
title: Manually Discount Product Prices
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_manual_discount_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Manually Discount Product Prices

Manual discounts, also known as discretionary discounts, can be applied to products to provide additional price reductions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User

Sales reps can be agile and adjust prices themselves to help their customers close strategic deals. They can also tailor pricing for unique deals, especially when situations become more complex. Manual discounts are not associated with decision tables, which makes it easy to integrate them into a pricing procedure and generate a custom discount within minutes.

For example, you could create pricing rules for a long-term user to receive an additional 10% discount on their frequent laptop purchases. Let's assume your customer has purchased over 150 laptops, and as a loyalty incentive, you want to offer them an extra 10% discount on every laptop.

Create a pricing procedure to calculate volume discounts.
Search for and add the Manual Discount element and map these variables.
Adjustment Type: AdjustmentType
Adjustment Value: AdjustmentValue
Quantity: LineItemQuantity
Input Unit Price: NetUnitPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your laptop product and click Simulate again.
The price waterfall shows the manual discounts used to calculate the final price of the laptops, confirming that your procedure is working as expected.

=== ARTICLE: ind.pricing_add_products_as_price_book_entries.htm ===
---
article_id: ind.pricing_add_products_as_price_book_entries.htm
title: Add Products as Price Book Entries
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_products_as_price_book_entries.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_get_ready_to_build_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Add Products as Price Book Entries

Record each product or service you sell as a product in Revenue Management. These products, also referred to as line items, have a specific selling price and are added as entries to a price book.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

A price book in Salesforce Pricing acts as the primary list of all your products with their base prices. This process allows businesses to maintain a comprehensive and organized catalog of their products and their corresponding prices, ensuring accurate pricing for customers.

=== ARTICLE: ind.pricing_add_the_price_adjustment_matrix_element.htm ===
---
article_id: ind.pricing_add_the_price_adjustment_matrix_element.htm
title: Dynamic Pricing With Price Adjustment Matrix
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_the_price_adjustment_matrix_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Dynamic Pricing With Price Adjustment Matrix

Determine custom discounts and adjustments that go beyond the predefined options provided by Salesforce Pricing using Price Adjustment Matrix element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

The Price Adjustment Matrix element helps businesses set dynamic prices. It goes beyond simple volume discounts, letting you create complex pricing rules for different sales situations. This can be done by creating custom decision tables that hold pricing criteria and adjustments with or without custom objects. This allows for contextual pricing, tailoring offers based on quote details, customer info, or product features, ensuring precise, scenario-based pricing.

Implementing this framework involves a few key steps.

Create custom objects or use existing Salesforce objects to hold your price adjustment data.
Define decision tables, setting criteria (like quantity or product attributes) and their adjustments (discounts or price overrides).
Integrate these tables into your pricing procedure, linking them to relevant quote fields.
Finally, when processing a quote, the quoting system uses this information to dynamically calculate and apply accurate price adjustments.
Calculate Product Prices Using Price Adjustment Matrix
Let's look at a scenario where we want to apply custom percentage-based discounts using the Price Adjustment Matrix element.

=== ARTICLE: ind.pricing_add_the_subscription_price_proration_element.htm ===
---
article_id: ind.pricing_add_the_subscription_price_proration_element.htm
title: Configure the Proration and Subscription Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_the_subscription_price_proration_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_pricing_proration.htm
fetched_at: 2026-09-07
---

# Configure the Proration and Subscription Element

To calculate time-based pricing, use the Proration and Subscription elements.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time

Let's consider a cloud storage subscription service with a standard monthly price of $150. If a customer starts their subscription mid-month, the pricing model accurately prorates the cost based on the remainder of that month.

Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Now, add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the Proration element to adjust the price for a partial pricing period and map these variables.
Input Variables
Effective From: EffectiveFrom
Effective To: EffectiveTo
Proration Period: PricingTermUnit
Start Proration Period: StartProrationPeriod
Start Proration Period Day: StartProrationPeriodDay
StartProration Period Month: StartProrationPeriodMonth
Allow Partial Proration Periods: AllowPartialProrationPeriods
Selling Model Type: ProductSellingModel
Subscription Term Unit: ItemSubscriptionTermUnit
Subscription Term: ItemSubscriptionTerm
Output Variables
Proration Multiplier: PricingTermCount
Click and select Include in Output.
Set your preferences for profile access.
Add the Subscription element to calculate the total subscription price based on the input unit price and pricing term count. Map these variables.
Input Variables
Quantity: LineItemQuantity
Proration Multiplier: PricingTermCount
Net Unit Price: ListPrice
Output Variables
Total Subscription Price: ItemNetTotalPrice
Subscription Net Unit Price: NetUnitPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure.
Enter the input values for your laptop product and click Simulate again.
SCENARIO	PERIOD(EFFECTIVE FROM TO EFFECTIVE TO)	TOTAL DAYS	MULTIPLIER	LIST PRICE	QUANTITY	CALCULATED PRICE
Full Monthly Period	Apr 18, 2021 – Dec 17, 2021	8 full months	1.0000 (each month)	$150	1	$1,200.00
Partial Period	Dec 18, 2021 – Dec 31, 2021	14/ 31	0.4516	$150	1	$67.74
Partial Period (Leap Year)	Feb 10, 2024 – May 9, 2024	81/ 90	Mixed (3 periods: 0.6897, 1.0000, 1.0000)	$150	5	$2,234.98
Full Period (Leap Year)	Jan 18, 2024 – May 17, 2024	121	1.0000 (all months)	$150	5	$3,000.00

The price waterfall shows where subscription pricing was applied based on a full leap year's pricing period, confirming your procedure is working as expected.

=== ARTICLE: ind.pricing_add_tier_discount_element.htm ===
---
article_id: ind.pricing_add_tier_discount_element.htm
title: Understand the Difference Between Volume and Tier Discounts
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_tier_discount_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_volume_discount_element.htm
fetched_at: 2026-09-07
---

# Understand the Difference Between Volume and Tier Discounts

Distinguishing between volume and tiered discounts is crucial for applying the most effective pricing strategies to your products. Both methods allow you to offer discounts based on quantity purchased, often within specified date ranges, and can be integrated into your pricing engine.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Volume Discounts
Provides a single, reduced price per unit once a customer reaches a specified quantity threshold. For example, if a customer buys 60 units and the volume discount activates at 40 units, all 60 units will be priced at the lower rate. This method offers a simple and straightforward way to apply discounts based on the total quantity purchased.
Tiered Discounts
Provides different price points to different quantity ranges. This offers more granular control over pricing, as the price per unit can change multiple times within a single purchase.

Let's illustrate with an example:

Imagine you're purchasing 25 laptops for your organization, with a unit price of $200 USD. Your manufacturer offers the following tier-based discounts.:

No discount for fewer than 10 laptops.
10% discount for every laptop when 10–19 laptops are purchased.
15% discount for every laptop when 20–29 laptops are purchased.

All tiers are included to calculate the price. Here’s how the discounts are applied and the total price is calculated for 25 laptops.

QUANTITY	DISCOUNTS APPLIED	TOTAL PRICE
For 25 laptops	

No discounts applied for the first 9 laptops

10% off for laptops 10–19

15% off for laptops 20–25

	(9 x $200) + (10 x $180) + (6 x $170) = $4620

To conclude, volume discounts offer one reduced price for all units once a quantity threshold is met, while tiered discounts apply progressively lower prices to units as the quantity purchased increases across different ranges.

=== ARTICLE: ind.pricing_add_volume_discount_element.htm ===
---
article_id: ind.pricing_add_volume_discount_element.htm
title: Volume and Tier Based Discounts
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_add_volume_discount_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Volume and Tier Based Discounts

To calculate the price of a product based on discounts configured according to the quantities purchased, use the Volume Discount or the Tier Discount element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Understand the Difference Between Volume and Tier Discounts
Distinguishing between volume and tiered discounts is crucial for applying the most effective pricing strategies to your products. Both methods allow you to offer discounts based on quantity purchased, often within specified date ranges, and can be integrated into your pricing engine.
Create Price Adjustment Tiers for Volume Discounts
Set up pricing rules that automatically adjust prices and offer discounts based on the quantities purchased by creating price adjustment tier records. You can use them to implement various strategies, including both volume or tiered discounts. This adjustment type enables you to define a product's price based on the number of items being sold.
Cumulative Pricing Using Volume or Tier Discount Elements
Customers can apply volume or tier-based discounts to a line item based on aggregated product quantities, whether from past purchases (asset quantity) or multiple line items within the same quote or order.
Calculate Volume or Tiered Discounts with Cumulative Pricing
Determine the discount of a product based on the quantity purchased. Automatically calculate discounts on volume and tier-based quantities, including discounts from past orders.

=== ARTICLE: ind.pricing_advanced_price_log_settings.htm ===
---
article_id: ind.pricing_advanced_price_log_settings.htm
title: Set Up Advanced Price Logs
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_advanced_price_log_settings.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_operations_console.htm
fetched_at: 2026-09-07
---

# Set Up Advanced Price Logs

Capture input values and exception details for complex pricing elements. Use this diagnostic data to identify and fix performance issues.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To turn on advanced price logs:	Salesforce Pricing Admin
IMPORTANT We strongly recommend that you enable advanced logging only during active troubleshooting, and turn it off immediately after debugging is complete to maintain optimal system speed and prevent other system issues.
From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
Turn on Activate Price Waterfall for API Responses and Price Waterfall Persistence.
From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Advanced Price Log Settings.
Turn on advanced logs for the elements that you want to debug, such as Attribute-Based Pricing Element, Derived Pricing Element, Price Propagation Element, and Pricing Promotion Element.
To view the logs, use the Pricing WaterfallAPI.

=== ARTICLE: ind.pricing_annual_proration_examples.htm ===
---
article_id: ind.pricing_annual_proration_examples.htm
title: Annual Proration Examples
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_annual_proration_examples.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_variables.htm
fetched_at: 2026-09-07
---

# Annual Proration Examples

Demonstrates how the system calculates pricing based on a yearly billing cycle.

Base Transaction Details (All Examples)
Effective From: 2025-03-28
Effective To: 2026-02-04
Total Duration: 314 Days
Start Proration Day: 5 (Used for DayOfPeriod examples)
Start Proration Month: February (Used for DayOfPeriod examples)
Proration Period: Annual
List Price: $800.00

1. Start Proration Period: DayOfPeriod (Feb 5) and Allow Partial Proration Periods: True

Calculation Logic: The system creates billing periods anchored to February 5th.
Period 1: 5-Feb-2025 to 4-Feb-2026
Total Days in Period: 365
Utilized Duration: 28-Mar-2025 to 4-Feb-2026 (314 Days)
Pricing Term Count: 314 / 365 = 0.860274
Subscription Price: $800 x 0.860274 = $688.22

2. Start Proration Period: DayOfPeriod (Feb 5) and Allow Partial Proration Periods: False

Pricing Term Count: 1.0
Calculation Logic: The term utilizes a single billing period (Feb 5 to Feb 4). Since the subscription falls within this specific annual cycle, the system rounds the partial usage up to 1 full unit.
Subscription Price: $800 x 1.0 = $800.00

3. Start Proration Period: Anniversary (Mar 28) and Allow Partial Proration Periods: True

Calculation Logic: The system creates periods anchored to the start date (Mar 28).
Period 1: 28-Mar-2025 to 27-Mar-2026
Total Days in Period: 365
Utilized Duration: 28-Mar-2025 to 04-Feb-2026 (314 Days)
Pricing Term Count: 314 / 365 = 0.860274
Subscription Price: $800 x 0.860274 = $688.22

4. Start Proration Period: Anniversary (Mar 28) and Allow Partial Proration Periods: False

Calculation Logic: The subscription duration sits entirely within a single anniversary year (Period 1 above); this is counted as 1 full unit.
Pricing Term Count: 1.0
Subscription Price: $800 x 1.0 = $800.00

5. Start Proration Period: AlignToCalendar (Jan 1) and Allow Partial Proration Periods: True

Calculation Logic: The system calculates the total days utilized divided by the days in the year.
Period 1: 1-Jan-2025 to 31-Dec-2025
Utilized Duration: 28-Mar-2025 to 31-Dec-2025 (279 /365)
Period 2: 1-Jan-2026 to 31-Dec-2026
Utilized Duration: 1-Jan-2026 to 04-Feb-2026 (35/365)
Total: (279/365 + 35/365) = 0.860274
Subscription Price: $800 x 0.860274 = $688.22

6. Start Proration Period: AlignToCalendar (Jan 1) and Allow Partial Proration Periods: False

Calculation Logic: The term crosses the Jan 1 boundary, touching two distinct calendar years (2025 and 2026). Each "touched" calendar year counts as 1.0.
Period 1: 2025 (Touched) = 1.0
Period 2: 2026 (Touched) = 1.0
Subscription Price: $800 x 2.0 = $1,600.00

=== ARTICLE: ind.pricing_annual_proration_examples_for_leap_years.htm ===
---
article_id: ind.pricing_annual_proration_examples_for_leap_years.htm
title: Annual Proration Examples for Leap Years
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_annual_proration_examples_for_leap_years.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_variables.htm
fetched_at: 2026-09-07
---

# Annual Proration Examples for Leap Years

Review calculations for annual billing cycles, and learn how the total days adapt to leap years. Salesforce Pricing uses a specific design convention to handle end-of-month anniversary dates. Rather than relying on simple date increments, Salesforce Pricing adjusts period end dates to accommodate the presence or absence of February 29 so that it calculates full periods logically based on date availability.

Base Transaction Details (All Examples)
Proration Period: Annual
List Price: $1,000.00

1. Start Proration Period: Anniversary (Feb 29)

Effective From: 2024-02-29
Effective To: 2025-02-27
Total Duration: 365 Days
Calculation Logic: Salesforce Pricing uses a design convention to manage leap year boundaries. Because the subscription starts on Leap Day, but the following year (2025) lacks a February 29, the next period must start on the latest available date (February 28). This forces the current full annual period to end on February 27.
Period 1: 29-Feb-2024 to 27-Feb-2025
Total Days in Period: 365
Utilized Duration: 29-Feb-2024 to 27-Feb-2025 (365 Days)
Pricing Term Count: 365 / 365 = 1.0
Subscription Price: $1,000 x 1.0 = $1,000.00

2. Start Proration Period: Anniversary (Feb 28 - Partial Period Before Leap Year)

Effective From: 2027-02-28
Effective To: 2028-02-27
Total Duration: 365 Days
Calculation Logic: This example highlights a critical distinction. Because the start date (Feb 28) is a month-end date preceding a leap year, Salesforce Pricing expects the full annual period to end on February 28, 2028 (a 366-day period). Because the subscription ends one day early on February 27, it doesn't complete the full term. Therefore, Salesforce Pricing calculates it as a partial period, resulting in a prorated charge.
Period 1: 28-Feb-2027 to 27-Feb-2028
Total Days in Period: 366 (The denominator is based on the full expected period ending 28-Feb-2028)
Utilized Duration: 28-Feb-2027 to 27-Feb-2028 (365 Days)
Pricing Term Count: 365 / 366 = 0.99726
Subscription Price: $1,000 x (365 / 366) = $997.27

3. Start Proration Period: Anniversary (Feb 28 - Preceding a Leap Year)

Effective From: 2027-02-28
Effective To: 2028-02-28
Total Duration: 366 Days
Calculation Logic: Salesforce Pricing identifies February 28 in a non-leap year as a month-end date. For annual proration, a full period ends one day before the next month-end. In 2028 (a leap year), the month-end is February 29, making the period end date February 28. By convention, the leap day (February 29) is included in the billing period when the leap year falls within the period’s end date.
Period 1: 28-Feb-2027 to 28-Feb-2028
Total Days in Period: 366
Utilized Duration: 28-Feb-2027 to 28-Feb-2028 (366 Days)
Pricing Term Count: 366 / 366 = 1.0
Subscription Price: $1,000 x 1.0 = $1,000.00

=== ARTICLE: ind.pricing_apex_hooks_best_practices.htm ===
---
article_id: ind.pricing_apex_hooks_best_practices.htm
title: Best Practices for Apex Pricing Hooks
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_apex_hooks_best_practices.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_customize_pricing_procedures_with_apex_hooks.htm
fetched_at: 2026-09-07
---

# Best Practices for Apex Pricing Hooks

Follow these best practices when implementing Apex hooks in your pricing procedure plans to optimize performance and avoid unexpected results.

Apex Governor Limits

Apex hooks in procedure plans run within the same Apex transaction, so the central processing unit timer is cumulative across all operations. Be mindful of governor limits when writing hook logic, especially for transactions with many line items.

For current limit values, see Execution Governors and Limits in the Apex Developer Guide.

Query Only the Tags You Need

Avoid querying broad entity-level tags like SalesTransactionItem, which return every attribute for every item. Instead, request only the specific tags your hook logic requires.

Not recommended: Querying broad tags


// BAD: Returns ALL attributes for every SalesTransactionItem
Map<String, Object> input = new Map<String, Object>{
    'contextId' => contextId,
    'tags' => new List<String>{ 'SalesTransactionItem' }
};
Map<String, Object> output = industriesContext.queryTags(input);
   

Recommended: Query only specific tags


// GOOD: Query only the specific tags (attributes) you need
Map<String, Object> input = new Map<String, Object>{
    'contextId' => contextId,
    'tags' => new List<String>{ 'LineItem', 'LineItemQuantity', 'ItemProductCode' }
};
Map<String, Object> output = industriesContext.queryTags(input);
   

Recommended: Combine specific tags with leanerQueryTags


// BETTER: Combine specific tags with leanerQueryTags for maximum efficiency
Map<String, Object> input = new Map<String, Object>{
    'contextId' => contextId,
    'tags' => new List<String>{ 'LineItem', 'LineItem$DmlStatus',
        'LineItemQuantity', 'ItemProductCode' }
};
Map<String, Object> output = industriesContext.leanerQueryTags(input);
   
Use leanerQueryTags Instead of queryTags

The Context.IndustriesContext class provides two methods for querying context data. Use leanerQueryTags wherever possible for better performance.

queryTags (heavy) — Returns full context nodes with nested tag-value maps and dataPath arrays. Every attribute is wrapped in a map with 6 fields (tagValue, dmlStatus, isDirty, isNodeLevelTag, tagPath, contextDataPathBuilder) per attribute per item. All attributes for the tag are returned regardless of what you need.

leanerQueryTags (lightweight) — Returns a compact structure with flat tag values and index-based record ID references. Tag values have only 3 fields (tagValue, recordIdIndexesForPath, isNodeLevelTag). Record IDs are deduplicated into a shared recordsInfo list; nodes reference them by index.

The following example shows how to call leanerQueryTags and process its output.


String contextId = request.ctxInstanceId;
Context.IndustriesContext industriesContext = new Context.IndustriesContext();

Map<String, Object> input = new Map<String, Object>{
    'contextId' => contextId,
    'tags' => new List<String>{ 'LineItem', 'ItemProductCode', 'LineItemQuantity' }
};
Map<String, Object> output = industriesContext.leanerQueryTags(input);

// Access the leaner result structure
Map<String, Object> queryResult = (Map<String, Object>)
    output.get('leanerQueryTagResult');
List<Object> recordsInfo = (List<Object>) output.get('recordsInfo');
List<Object> lineItems = (List<Object>) queryResult.get('LineItem');

// Iterate over tag values — each tag is flat
List<Object> productCodes = (List<Object>) queryResult.get('ItemProductCode');
for (Object obj : productCodes) {
    Map<String, Object> tagNode = (Map<String, Object>) obj;
    String productCode = (String) tagNode.get('tagValue');
    List<Integer> indexes = (List<Integer>) tagNode.get('recordIdIndexesForPath');
    // recordsInfo entries are maps with 'recordId' and 'dmlStatusOrdinal'
    String itemId = (String) ((Map<String, Object>)
        recordsInfo.get(indexes[1])).get('recordId');
}
   

The leanerQueryTags output structure looks like this:


{
  "isSuccess": true,
  "contextId": "...",
  "leanerQueryTagResult": {
    "LineItem": [
      { "recordIdIndexesForPath": [0, 1], "tagValue": "0QLVW000001LxvN4AS", "isNodeLevelTag": false },
      { "recordIdIndexesForPath": [0, 2], "tagValue": "0QLVW000001Lxus4AC", "isNodeLevelTag": false }
    ],
    "ItemProductCode": [
      { "recordIdIndexesForPath": [0, 1], "tagValue": "PROD-001", "isNodeLevelTag": false },
      { "recordIdIndexesForPath": [0, 2], "tagValue": "PROD-002", "isNodeLevelTag": false }
    ]
  },
  "recordsInfo": [
    { "recordId": "0Q0VW0000011qC50AI", "dmlStatusOrdinal": null },
    { "recordId": "0QLVW000001LxvN4AS", "dmlStatusOrdinal": null },
    { "recordId": "0QLVW000001Lxus4AC", "dmlStatusOrdinal": null }
  ]
}
   
NOTE Update your existing Apex pricing hooks to use leanerQueryTags instead of queryTags where possible.
Migrate from queryTags to leanerQueryTags

When migrating existing hooks from queryTags to leanerQueryTags, apply these key transforms.

Input: Use individual tags instead of broad tags


// Before (queryTags — broad tag):
Map<String, Object> input = new Map<String, Object>{
    'contextId' => contextId,
    'tags' => new List<String>{ 'SalesTransactionItem' }
};
Map<String, Object> output = industriesContext.queryTags(input);
   

// After (leanerQueryTags — specific tags):
Map<String, Object> input = new Map<String, Object>{
    'contextId' => contextId,
    'tags' => new List<String>{ 'LineItem', 'LineItem$DmlStatus',
        'ItemProductCode', 'LineItemQuantity' }
};
Map<String, Object> output = industriesContext.leanerQueryTags(input);
   

Output: Different top-level key


// Before:
Map<String, Object> queryResult = (Map<String, Object>) output.get('queryResult');
List<Object> items = (List<Object>) queryResult.get('SalesTransactionItem');
   

// After:
Map<String, Object> queryResult = (Map<String, Object>)
    output.get('leanerQueryTagResult');
List<Object> recordsInfo = (List<Object>) output.get('recordsInfo');
List<Object> lineItems = (List<Object>) queryResult.get('LineItem');
   

Node access: Flat values instead of nested maps


// Before (queryTags — nested map extraction):
for (Object itemObj : items) {
    Map<String, Object> itemNode = (Map<String, Object>) itemObj;
    Map<String, Object> tagValueMap = (Map<String, Object>) itemNode.get('tagValue');
    String productCode = (String) ((Map<String, Object>)
        tagValueMap.get('ItemProductCode')).get('tagValue');
    Decimal quantity = (Decimal) ((Map<String, Object>)
        tagValueMap.get('LineItemQuantity')).get('tagValue');
}
   

// After (leanerQueryTags — flat value, iterated per tag):
List<Object> productCodes = (List<Object>) queryResult.get('ItemProductCode');
List<Object> recordsInfo = (List<Object>) output.get('recordsInfo');

for (Object obj : productCodes) {
    Map<String, Object> tagNode = (Map<String, Object>) obj;
    String productCode = (String) tagNode.get('tagValue');
    List<Integer> indexes = (List<Integer>) tagNode.get('recordIdIndexesForPath');
    String itemId = (String) ((Map<String, Object>)
        recordsInfo.get(indexes[1])).get('recordId');
}
   

Record IDs: Index references instead of dataPath


// Before (queryTags):
List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
// dataPath = ['contextId', 'txnId', 'itemId'] — 3 elements, first is contextId
dataPath.remove(0);
String transactionId = (String) dataPath.get(0);
   

// After (leanerQueryTags):
List<Object> recordsInfo = (List<Object>) output.get('recordsInfo');
List<Integer> indexes = (List<Integer>) tagNode.get('recordIdIndexesForPath');
String transactionId = (String) ((Map<String, Object>)
    recordsInfo.get(indexes[0])).get('recordId');
String itemId = (String) ((Map<String, Object>)
    recordsInfo.get(indexes[1])).get('recordId');
   
Use the tagIdIndexMap Pattern

When processing multiple tags in a single loop, use a tagIdIndexMap to map each tag name to its position in the recordIdIndexesForPath array. This lets you correctly extract IDs at each hierarchy level:


Map<String, Integer> tagIdIndexMap = new Map<String, Integer>{
    'LineItem' => 1,            // item-level tag, ID at index 1
    'LineItem$DmlStatus' => 1,  // item-level tag, ID at index 1
    'LineItemQuantity' => 1,    // item-level tag, ID at index 1
    'BusinessUnit__c' => 0,     // transaction-level tag, ID at index 0
    'Contract' => 0             // transaction-level tag, ID at index 0
};
   
Index 0 = transaction-level (the path has one element: [txnId])
Index 1 = item-level (the path has two elements: [txnId, itemId])
Index 2 = detail-level (the path has three elements: [txnId, itemId, detailId])
Filter Deleted Items

Skip deleted items at the start of your iteration loop to avoid unnecessary processing. Request LineItem$DmlStatus as a separate tag in your query:


private static final String DML_DELETED = 'DELETED';

for (Map<String, Object> item : salesTransactionInstance.salesTransactionItems) {
    String dmlStatus = (String) item.get('LineItem$DmlStatus');

    if (dmlStatus == DML_DELETED) {
        continue; // Skip deleted items
    }

    // Process active items...
}
   
Read $DmlStatus as a Separate Tag

When querying specific tags (the recommended approach), DML status is not embedded in the tag metadata. You must request LineItem$DmlStatus as a separate tag. This applies to both queryTags and leanerQueryTags.


// Add LineItem$DmlStatus to your tags list
'tags' => new List<String>{ 'LineItem', 'LineItem$DmlStatus', 'ItemProductCode' }

// Access it like any other tag in the result
Map<String, Object> dmlNode = (Map<String, Object>) dmlStatusValues.get(i);
String dmlStatus = String.valueOf(dmlNode.get('tagValue'));

=== ARTICLE: ind.pricing_apply_policy_driven_price_revisions.htm ===
---
article_id: ind.pricing_apply_policy_driven_price_revisions.htm
title: Apply Policy-Driven Price Revisions
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_apply_policy_driven_price_revisions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_unique_pricing_scenarios.htm
fetched_at: 2026-09-07
---

# Apply Policy-Driven Price Revisions

Apply policy-driven price changes to respond to market conditions, contract terms, or inflationary trends. Pricing designers can define revision policies, track Consumer Price Index (CPI) data, and enable uplifts at set intervals, optimize revenue, and maintain business performance.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
IMPORTANT The Price Revision feature isn’t supported for Partner Community and Customer Community users.
Understand Price Revisions
Price revisions are adjustments to the price of goods or services. For a sales rep, understanding these changes is crucial, as they provide a clear and logical justification for a new price during a renewal. These changes, whether increases (uplifts) or decreases, help companies respond to market shifts, control costs, and maximize revenue. Revisions aren't random; they're typically triggered by pre-planned schedules, shifts in economic indicators, or contractual terms, which allow a sales rep to frame a price adjustment as a pre-agreed condition rather than a surprise demand.
Use the Price Revision Element in a Pricing Procedure
To maintain profitability on renewals, use the Price Revision element to automatically adjust for inflation and rising operational costs on quotes.
Use Consumer Price Index for Automated Renewal Price Uplifts
Automate the calculation of renewal price increases by using the consumer price index (CPI) and additional negotiated price uplift. With this feature, your pricing keeps pace with market conditions and maximizes your high-margin annual contract value (ACV).

=== ARTICLE: ind.pricing_apply_the_rounding_values_element.htm ===
---
article_id: ind.pricing_apply_the_rounding_values_element.htm
title: Use the Rounding Values Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_apply_the_rounding_values_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_rounding_values.htm
fetched_at: 2026-09-07
---

# Use the Rounding Values Element

Use the Rounding Values element to ensure that the output of any pricing element in a pricing procedure is rounded to the specified decimal place.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User

Let's consider a scenario where you want to set conditions to only give discounts when a customer purchases 50 or more printer bundles, and you're calculating the discounts using a formula. For this example, let's set ItemNetTotalPrice to be rounded down to the first decimal point.

IMPORTANT In a multicurrency organization, the user's personal currency setting determines the currency code used during rounding operations, not the currency code parameter passed in the procedure context.
Create a Constant for the Precision Variable
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
On the Pricing Procedure builder canvas, click .
On the Resource Manager panel, click Add Resource.
In the Add New Resource page, specify these details.
Resource Type: Constant
Resource Name: PrecisionVariable
Data Type: Number
Decimal Places: 2
Default Value: 1. This value specifies that the product's price should be rounded to one decimal place.
Save your changes.
Add the Rounding Values Element
Now, add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the List Group element.
In the list group, configure the List Operation by setting a condition that a 10% discount on the final price of the printers can only be applied if the user purchased over 50 units.
Filter Condition Requirements: All Conditions Are Met (AND)
Resource: # LineItemQuantity
Operator: Greater Than
Value: 50
Within the list container, add the Formula Based Pricing element and specify these variable values.
Calculation Formula: ItemNetTotalPrice - ( ItemNetTotalPrice * 0.10 )
Output Variable: TotalLineAmount
Outside the list container, add the Rounding Values element and specify these variables.
Fixed Input Variables
Precision: PrecisionVariable
Rounding Rules and Variables
Input Variable: ItemNetTotalPrice
Rounding Rule: Round Down.
Output Variable: ItemNetTotalPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your printer bundle product and click Simulate again.
The price waterfall shows the formula used to calculate the total cost of the printer bundles with a discount of 10%. You can also see that the rounded price has been applied to the Net Amount to the first decimal.

=== ARTICLE: ind.pricing_assignment.htm ===
---
article_id: ind.pricing_assignment.htm
title: Map Context Tag Data Using Assignment Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_assignment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Map Context Tag Data Using Assignment Element

Dynamically set or change the values of pricing variables by mapping data between context tags or from a variable directly into a context tag.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time

The Assignment element supports a wide variety of data types, including currency, numbers, date and time, and dates. You'll find this element especially useful for defining pricing procedures and managing data flows within your pricing process. It's powerful because it operates by using outputs from preceding pricing elements, all without touching the Salesforce database.

Let’s look at a scenario where if a product's Effective To date is null, you can use the Assignment element to automatically populate it with the Effective To date from the quote. Since this element relies on the output of previous pricing elements, you'll need to set a condition for the data values using the List Group element. Then, add the List Price element to fetch the product's base price using the quote's date.

Configure a pricing procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Group element to the pricing procedure and set the following condition.
Filter Condition Requirements: All Conditions are Met (AND)
Resource: EffectiveTo
Operator: Is Null
Within the List Container, add the Assignment element.
Modify the tag values of the input and output variables based on how you want the variable values to be consumed.
Input Variable: EffectiveDate
Output Variable: EffectiveTo
Add the List Price element to fetch the base price of the product based on the modified date variable.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Simulate and activate your pricing procedure.
The JSON output shows how the variables were modified to fetch the list price for your product based on the quote’s date.

The price waterfall shows the list price generated for the quote’s EffectiveTo date even though the line product’s EffectiveTo date was null.

=== ARTICLE: ind.pricing_attribute_based_pricing_limits.htm ===
---
article_id: ind.pricing_attribute_based_pricing_limits.htm
title: Attribute-Based Pricing Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_attribute_based_pricing_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_attribute_based_price_element.htm
fetched_at: 2026-09-07
---

# Attribute-Based Pricing Limits

Keep these guidelines in mind when configuring attribute-based adjustments.

When you configure adjustments by using numeric data types (Number, Currency, Percentage) or number picklists, the pricing engine automatically stores whole numbers with a decimal (for example, 10 is stored as 10.0). For the configurator to successfully match the attribute and apply the discount at run time, the input value must explicitly include the ‘.0’. If you pass a whole number without the decimal, the adjustment doesn't apply.
While attribute-based pricing supports picklists for all other data types, you can't use a picklist with a Boolean data type (for example, mapping custom text like "Available" or "N/A" to true or false values). If you try to save an adjustment configured with a Boolean picklist, you get a design-time error. Instead, create an attribute of type Checkbox or Boolean.
When configuring price-impacting attributes, use only attributes that belong directly to the selected product classification (or subclassification). While attributes inherited from a parent product classification can appear in the configuration UI, selecting them causes a validation error when you save the adjustment.
The pricing engine doesn't support attribute-based adjustments for attributes with an overridden bundle context. For a product within a bundle, define the attribute once instead of creating an overridden attribute. The override prevents the adjustment from applying.

=== ARTICLE: ind.pricing_automate_pricing_data_sync.htm ===
---
article_id: ind.pricing_automate_pricing_data_sync.htm
title: Automate Pricing Data Sync with a Scheduled Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_automate_pricing_data_sync.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_sync_pricing_data.htm
fetched_at: 2026-09-07
---

# Automate Pricing Data Sync with a Scheduled Flow

Create a scheduled flow that refreshes your pricing decision tables on a regular cadence so that Agentforce Revenue Management always uses current pricing data without requiring a manual sync.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create and activate flows:	Manage Flow
To enable data sync:	Salesforce Pricing Design Time
To ensure complete sync of decision tables:	Assetize Order

You can sync pricing data manually at any time by using the Sync Pricing Data button in Salesforce Pricing Setup. Optionally, you can also automate this process with a scheduled flow that calls the Refresh Decision Table action on a regular cadence. This ensures that decision tables stay current — for example, with a nightly refresh — without relying on an admin to run the sync after every pricing change.

Before you set up a scheduled sync, review these considerations.

Schedule refreshes during off-peak hours
Decision table refreshes consume processing resources. For orgs with large pricing catalogs (thousands of price book entries or complex tier structures), schedule the flow to run during off-peak hours when few users are actively creating quotes or orders. This minimizes the risk of pricing calculations reading stale data mid-refresh.
Pause automation during bulk data loads
Deactivate this flow before performing large data imports (for example, bulk product or price book entry loads). A refresh triggered mid-import can capture an incomplete data state. Run a manual sync after the import completes, then reactivate the flow.
Set up error notifications
If a Refresh Decision Table action fails — for example, because a decision table was deactivated or the hourly limit was reached — the flow fails without alerting anyone by default. In Flow Builder, add a fault path to the action or enable flow error email notifications in Setup so that admins are alerted to failures.
Verify successful refreshes
After activating the flow, confirm that decision tables are refreshing as expected. From Setup, navigate to the Decision Tables page and check the Last Refreshed timestamp. You can also review flow execution history in Setup under Process Automation.
Set Up Automated Pricing Data Sync
From Setup, in the Quick Find box, enter Flows, and then select Flows.
Click New Flow.
Under Scheduled Automations, select Schedule-Triggered Flow and click Create.
Click Set Schedule on the Start element and configure the schedule.
Set a start date, start time, and select Daily or Weekly from the Frequency dropdown. For most orgs, a daily frequency running during off-peak hours (for example, 2:00 AM) is sufficient. If your org serves users in multiple time zones, choose a window when the fewest users are actively generating quotes or orders. You can skip the optional Choose Object step.
Click the + icon between the Start and End elements, and select Action.
In the Search Actions field, search for and select Refresh Decision Table.
Enter a label for the action, and in the Decision Table API Name input field, enter the API name of the decision table to refresh.
To refresh multiple decision tables, add a separate Refresh Decision Table action for each one.
Save the flow and click Activate.

The flow runs at the scheduled time and refreshes the specified decision tables. Pricing calculations in Agentforce Revenue Management then use the updated data for all subsequent transactions.

=== ARTICLE: ind.pricing_calculate_attribute_based_discounts.htm ===
---
article_id: ind.pricing_calculate_attribute_based_discounts.htm
title: Calculate Attribute-Based Discounts
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_calculate_attribute_based_discounts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_attribute_based_price_element.htm
fetched_at: 2026-09-07
---

# Calculate Attribute-Based Discounts

Determine the price of a product based on the discounts configured for selected price impacting attributes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User

Let's use a scenario involving a large quantity of laptop purchases. We want to add a $10 override for any customer who purchased a laptop with a display resolution over 4K.

Create an Attribute Based Adjustment Record
Create an attribute based adjustment record.
Specify these details.
Price Adjustment Schedule: Standard Price Adjustment Tier
Product: Laptop
Adjustment Type: Override
Adjustment Value: 10
Effective From: 01-01-2025
Product Selling Model: One Time
Click Next.
Set the following condition.
Attribute: Display. (The price impacting attribute will be pre-populated)
Operator: Equals
Value: 4K Built-in Display
Save your changes.
On the Details tab, on the Standard Attribute Based Adjustment page, select Active.
Save your changes.
IMPORTANT We recommend refreshing the Attribute Discount Entries decision table to ensure that the attribute based adjustment records are available.
Create a Constant for a Attribute Based Adjustment Variable
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
On the Pricing Procedure builder canvas, click .
On the Resource Manager panel, click Add Resource.
In the Add New Resource page, specify these details.
Resource Type: Constant
Resource Name: AttributePAS
Data Type: Text
Default Value: Enter the attribute based adjustment ID from the browser.
You can locate the value of your variable by going to the associated record. For example, to locate a price adjustment schedule ID, open the price adjustment schedule record page. The price adjustment schedule ID is shown in the browser’s URL. 
Save your changes.
Add the Attribute-Based Price Element
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
To add the Attribute-Based Price element, search for and add the Attribute Discount Entries decision table and map these variables.
Input Rule Variables
Price Adjustment Schedule: AttributePAS
Product: Product
Product Selling Model: ProductSellingModel
Effective From: EffectiveFrom
Effective To: EffectiveFrom
Input Variables
Attribute Name: Attribute
Attribute Value: AttributeValue
Quantity: LineItemQuantity
Is Price Impacting: PriceImpactingAttribute
Input Unit Price: ListPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
.
Save your procedure.
Click Simulate to test your procedure.
Provide the following attribute-specific input values.
AttributeValue: 4k Built-in Display
PriceImpactingAttribute: true
Attribute: Display
Click Simulate again.
The price waterfall shows the attribute-based discounts used to calculate the final price of the laptops, confirming that your procedure is working as expected.

=== ARTICLE: ind.pricing_calculate_bundle_based_discounts.htm ===
---
article_id: ind.pricing_calculate_bundle_based_discounts.htm
title: Calculate Bundle-Based Discounts
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_calculate_bundle_based_discounts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_bundle_based_price_element.htm
fetched_at: 2026-09-07
---

# Calculate Bundle-Based Discounts

Determine the price of a product based on the discounts configured for a set of products sold as a bundle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User

Let's create a scenario where customers who purchase the Laptop Pro bundle along with the Printer Bundle receive a special discount, significantly lowering the cost of the Printer Bundle compared to when it's purchased on its own.

IMPORTANT When InclusivePrice is true for any item in a bundle, the Bundle-Based Price element sets the item's price to zero. Pricing calculation stops for that item, and subsequent pricing procedure elements don't execute because its price is already included in the bundle price.
Create a Bundle Based Adjustment Record
Create a bundle based adjustment record.
Specify these details.
Root Bundle: Laptop Pro Bundle
Root Bundle Selling Model: One Time
Parent Product: Laptop Pro Bundle
Parent Product Selling Model: One Time
Product: Printer Bundle
Product Selling Model: One Time
Adjustment Type: Override
Adjustment Value: 20
Effective From: 01-01-2025
Price Adjustment Schedule: Standard Bundle Based Adjustment
Save your changes.
On the Details tab, on the Bundle Based Adjustment page, select Active.
Save your changes.
IMPORTANT We recommend refreshing the Bundle Based Adjustment Entries decision table to ensure that the bundle based adjustment records are available for pricing.
Create a Constant for a Bundle Based Adjustment Variable
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
On the Pricing Procedure builder canvas, click .
On the Resource Manager panel, click Add Resource.
In the Add New Resource page, specify these details.
Resource Type: Constant
Resource Name: BundleBasedAdjustmentId
Data Type: Text
Default Value: Enter the bundle based adjustment ID from the browser.
You can locate the value of your variable by going to the associated record. For example, to locate a price adjustment schedule ID, open the price adjustment schedule record page. The price adjustment schedule ID is shown in the browser’s URL. 
Save your changes.
Add the Bundle-Based Price Element
Now, add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
To add the Bundle-Based Price element, search for and add the Bundle Based Adjustment Entries decision table and map these variables.
Input Rule Variables
Price Adjustment Schedule: BundleBasedAdjustmentId
Product Selling Model: ProductSellingModel
Effective From: EffectiveFrom
Effective To: EffectiveFrom
Product: Product
Parent Product: MainItemProduct
Parent Product Selling Model: MainItemProductSellingModel
Root Bundle: RootItemProduct
Root Bundle Selling Model: RootItemProductSellingModel
Input Variables
Quantity: LineItemQuantity
Input Unit Price: ListPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your laptop product and click Simulate again.
The price waterfall shows the bundle-based discounts used to calculate the final price of the printer bundle, confirming that your procedure is working as expected.

=== ARTICLE: ind.pricing_calculate_contract_based_pricing.htm ===
---
article_id: ind.pricing_calculate_contract_based_pricing.htm
title: Calculate Contract-Based Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_calculate_contract_based_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_contract_based_pricing.htm
fetched_at: 2026-09-07
---

# Calculate Contract-Based Pricing

Before you begin to calculate contracted prices, do the following.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create pricing procedures:	Salesforce Pricing Design Time
Link your products to a contract.
Calculate the base contracted prices. Use the Contract Pricing Entries decision table for this calculation.
Enable contract-based pricing. In the relevant elements, select the Use contract-based pricing option.
Set the Contract Pricing variable. When you enable contract-based pricing, you must provide a value for your Contract Pricing boolean variable. This variable determines if contracted prices will be generated.
Filter the line items. Use the List Group element to filter out the line items that aren’t configured for additional discounts on their contracted price.

Let’s consider a scenario where we provide our customer with a flat base price of $75 for every monitor purchased. We’ll provide an additional 5% manual discount if our customer purchases 100 monitors.

Define Contracts
From App Launcher, find and select Contracts.
Click New.
Specify these details.
Account Name: GenePoint (This is based on our example only)
Contract Start Date: 7/1/2025
Contract Term (months): 12
Save your changes.
Define Contract Item Prices
On the Related tab of the contract you just created, go to Contract Item Prices, and click New.
Specify these details.
Under Item, select Product.
Search for and select Monitor.
Product Selling Model: One Time
Price: $75
Start Date: 7/2/2025, 12:00 PM
End Date: 10/31/2025, 12:00 PM
Adjustment Method: Range
Save your changes.
Activate Your Contract
From App Launcher, find and select Contracts.
Select the contract you created.
On the approval flow, select Activated.
Select Mark Status as Complete.
Refresh Your Decision Tables

Refresh your decision table to ensure the latest contract-specific data is available for pricing.

To refresh your decision table, from Setup, in the Quick Find box, search for and select Decision Tables.
Select Contract Pricing Entries, and click Refresh.
Calculate the Contract-Based Price Using a Pricing Procedure
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Contract Pricing Entries decision table.
Select Use contract-based pricing.
Map these variables.
Input Rule Variables
Contract: ItemContract
Item: Product
Product Selling Model: ProductSellingModel
Selling Model Type: SellingModelType
Start Date: StartDate
Output Rule Variables
Discount Type: ItemContractDiscountType
Discount Value: ItemContractDiscountValue
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: NetUnitPrice
Contract Pricing: IsContracted
Save your changes.
Add the List Group element.
Configure the list operation to filter out all the line items with the configured contract prices. Based on our example, define a condition where if a contracted base price is found, then look for a contract based volume discount and apply it.
Filter Condition Requirements: All Conditions Are Met (AND)
Resource: IsContracted
Operator: Equals
Value: true
Within the list container, search for and add the Manual Discount element and map these variables.
Adjustment Type: AdjustmentType.
Adjustment Value: AdjustmentValue
Quantity: LineItemQuantity
Input Unit Price: NetUnitPrice
To stop pricing, within the list container, and under the Manual Discount element, add the Stop Pricing element.
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure.
Enter the input values for your monitor product and click Simulate again.
The price waterfall shows the contracted price used to calculate the monitors' final price, including the flat 5% discount applied for purchasing over 100 units, confirming that your procedure is working as expected.

=== ARTICLE: ind.pricing_calculate_cumulative_discounts_for_volume_and_tier.htm ===
---
article_id: ind.pricing_calculate_cumulative_discounts_for_volume_and_tier.htm
title: Cumulative Pricing Using Volume or Tier Discount Elements
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_calculate_cumulative_discounts_for_volume_and_tier.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_volume_discount_element.htm
fetched_at: 2026-09-07
---

# Cumulative Pricing Using Volume or Tier Discount Elements

Customers can apply volume or tier-based discounts to a line item based on aggregated product quantities, whether from past purchases (asset quantity) or multiple line items within the same quote or order.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

This ability to aggregate quantities, from current transactions or historical purchases, is crucial for effective discounting. It allows customers to receive cumulative quantity discounts based on defined rules, incentivizing larger purchases over time and honoring negotiated pricing commitments.

By using cumulative pricing, discounts are applied based on the total quantity from past purchases or multiple line items within the same transaction, rather than just individual line item quantities. This method ensures that the pricing engine considers the full scope of a customer's purchasing activity when calculating discounts.

Applying Cumulative Quantity to Volume Discounts

When you apply cumulative pricing to the Volume Discount element, the aggregated quantity is provided through the AggregatedQuantity_std context tag. This aggregated quantity is calculated from the customer's pricing contract (when the contract's aggregation strategy is set to Cumulative) and represents the sum of quantities from past purchases.

For example, if the aggregated quantity from past purchases is 6 units and the current line item quantity is 2 units, the total cumulative quantity becomes 8 units. If your discount tier offers 10% off for 5-10 units, this discount will be applied to the currently purchased 2 units, even though only 2 items were purchased in the current transaction.

Applying Cumulative Quantity to Tier Discounts

Similarly, when you apply cumulative pricing to the Tier Discount element, it exposes the Cumulative Tier Quantity input variable. This input variable is mapped to a context tag and passed by the transaction system. This value helps the pricing engine determine which tiers are relevant.

For example, let’s assume that the cumulative tier quantity is 3 units, and the current line item quantity is 6 units. If your pricing structure has an initial tier with no discount for 1 to 3 units, this tier would be filled by the cumulative quantity of 3. The current line item quantity of 6 would then be spread across subsequent tiers such as, 4-7 units and 8-10 units, potentially leading to a higher overall discount than if only the line item quantity was considered.

NOTE For active orders or assets, cumulative pricing requires Contract Pricing Volume or Tiered Discounts. However, when simulating a pricing procedure, you can use cumulative quantity independently, without Contract Pricing.

=== ARTICLE: ind.pricing_calculate_price_of_object.htm ===
---
article_id: ind.pricing_calculate_price_of_object.htm
title: Calculate Price of a Product by Using the Standard Price Action
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_calculate_price_of_object.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_standard_pricing_actions.htm
fetched_at: 2026-09-07
---

# Calculate Price of a Product by Using the Standard Price Action

After you add the Calculate Price button to the selected object, you can calculate the price of a product from the object’s record page.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To calculate the price of a product:	

Salesforce Pricing Admin

OR

Salesforce Pricing Run Time User

The Calculate Price button is visible for these objects: Quote, Order, Contract, Sales Agreement, Case, Opportunity, and Work Order. 

From , find and select Price Management.
Select the object record of any of these objects: Quote, Order, Contract, Case, and Opportunity. 
Click Calculate Price.

=== ARTICLE: ind.pricing_calculate_product_prices_using_price_adjustment_matrix.htm ===
---
article_id: ind.pricing_calculate_product_prices_using_price_adjustment_matrix.htm
title: Calculate Product Prices Using Price Adjustment Matrix
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_calculate_product_prices_using_price_adjustment_matrix.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_the_price_adjustment_matrix_element.htm
fetched_at: 2026-09-07
---

# Calculate Product Prices Using Price Adjustment Matrix

Let's look at a scenario where we want to apply custom percentage-based discounts using the Price Adjustment Matrix element.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User
Create a Custom Decision Table
From the App Launcher, search for and select Lookup Tables .
Select Decision Table.
Specify these details.
Enter a name and then press Tab to autopopulate the API Name. For our example, we’re calling the decision table, Price Adjustment Matrix Entries.
Select Pricing as the application usage.
Select Advanced as the decision table type.
Click Save & Next.
Specify these decision table details.
Source Object: Price Adjustment Tier.
Set the following condition.
Set the source object field as Name and the operator as Equals.
Set another condition for the ID.
Set the source object field as Id and the operator as Equals.
Ensure that the Condition Type is set to All conditions are met (AND).
Specify the result details.
Source Object Field: TierValue.
Column Name: TierValue.
Source Object Field: AdjustmentType.
Column Name: AdjustmentType.
Click Save & Next.
Click Save & Next again.
Click Finish.
Activate your decision table.
Map the Variables in Your Custom Decision Table
From Setup, in the Quick Find box, find and select Pricing Recipes.
Choose the pricing recipe that you want to modify. For our example, select NGPDefaultRecipe.
On the Price Adjustment Matrix tab, click Modify.
Select the custom decision table created by you. Here, select Price Adjustment Matrix Entries.
Map the following variables.
AdjustmentValue: TierValue
AdjustmentType: AdjustmentType
When creating price adjustment tier records with AdjustmentType = Percentage, enter the percentage as a whole number. For example, enter 10 for a 10% discount (not 0.10 or 10%).
Save your changes.
Use the Price Adjustment Matrix Element
Configure a pricing procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Price Adjustment Matrix element.
The input rule variables shown below are specific to this example. Your variables will differ based on the source objects you selected in your custom decision table and the conditions and results you configured.
Under Lookup Table Details, select the Price Adjustment Matrix Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Input Unit Price: ListPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your product and click Simulate again.

=== ARTICLE: ind.pricing_calculate_the_derived_price_of_product.htm ===
---
article_id: ind.pricing_calculate_the_derived_price_of_product.htm
title: Calculate the Derived Price of Product
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_calculate_the_derived_price_of_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_derived_price.htm
fetched_at: 2026-09-07
---

# Calculate the Derived Price of Product

Use the discovery procedure and the derived price element in a pricing procedure, to calculate a product’s price from another product or asset.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create pricing procedures:	Salesforce Pricing Design Time
To run pricing procedures:	Salesforce Pricing Run Time

Let's calculate the price of a laptop bag when a user purchases a Laptop Pro Bundle. Our pricing strategy is to tie the price of the laptop bag to the Laptop Pro Bundle. We'll price the laptop at 10% of the Laptop Pro Bundle's price.

Create Derived Products

Before you begin, remember these key pieces of information.

The derived and source products must belong to the same price book. In our example, we’re using the predefined Standard Price Book.
If you select Header (Quote Line) as your pricing source, you don’t need to provide a source product. You can calculate the derived price of a product from the total cart values.
From the App Launcher, find and select Products.
Under the Product Name, click Laptop Bag.
On the Related tab, under Price Books, select Add Standard Price.
Specify these details.
Is Derived: Selected
List Price: $0.00
Product Selling Model: Evergreen Yearly
Save your changes.
Create Derived Price Record

To determine the formula used to calculate the derived price of a product, you’ll need to create derived price records. The pricing data from the derived price records is stored in the Derived Pricing Entries decision table.

From the App Launcher, find and select Derived Prices.
Click New.
On the New Derived Price page, specify these details:
Derived Pricing Scope: Transactional
Pricing Source: Product
Price Book: Standard Price Book
Derived Product: Laptop Bag
Source Product: Laptop Pro Bundle
Formula: ListPrice * 0.10
Effective From: 01-01-2025
Save your changes.
IMPORTANT

Refresh the Derived Pricing Entries and the Price Book Entries V2 decision tables to ensure that the derived pricing records are available for pricing.

Configure Your Discovery Procedure
From the App Launcher, find and select Discovery Procedures.
Select the Default Discovery Procedure.
Delete the Asset Discovery element. Since our scenario is transactional, we don’t need this element.
Save the discovery procedure as new discovery procedure and provide a name.
For our example, you can name your discovery procedure as Discovery Procedure for Derived Pricing.
Click Simulate.
Provide your input values.
Remember that the Laptop Pro Bundle's DerivedPricingAttribute field must be set to false, because it is the source product. The Laptop Bag's DerivedPricingAttribute fields must be set to true because we’ll derive it's price from the source product.

You’ll not see the results in waterfall view. The purpose of simulating the discovery procedure is to fetch all the contributing factors and write them back into the context definition.

Create a Pricing Procedure for Derived Price
IMPORTANT You can’t apply discount distribution to a pricing procedure that was used to calculate a product's derived price.
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Is Derived: DerivedPricingAttribute
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries V2 decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Derived Price element to calculate the derived price. Map these input variables.
Quantity: LineItemQuantity
Contributing Net Unit Price: ContributorUnitPrice
Contributing Sub Total: ContributorTotalPrice
Contributing Source: ContributorSource
Contributing Scope: ContributorScope
Transactional List Price: ListPrice
Non-Transactional List Price: ContributorListPrice
Derived Formula: ContributorFormulaInput
Contributor: Contributor
Contributing Product: ContributorProduct
Header Total: TotalAmount
Click and select Include in Output.
Finally, set your preferences to set profile access and rank information.
Save your procedure.
Click Simulate to test your procedure.
Enter the input values for your contributor product (Laptop Pro Bundle) and the derived product (Laptop Bag). Click Simulate again.
The price waterfall shows the Laptop Bag’s price was derived from the Laptop Pro Bundle, confirming that your procedure is working as expected.

=== ARTICLE: ind.pricing_calculate_volume_or_tiered_discounts_with_cumulative_pricing.htm ===
---
article_id: ind.pricing_calculate_volume_or_tiered_discounts_with_cumulative_pricing.htm
title: Calculate Volume or Tiered Discounts with Cumulative Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_calculate_volume_or_tiered_discounts_with_cumulative_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_volume_discount_element.htm
fetched_at: 2026-09-07
---

# Calculate Volume or Tiered Discounts with Cumulative Pricing

Determine the discount of a product based on the quantity purchased. Automatically calculate discounts on volume and tier-based quantities, including discounts from past orders.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User

Calculate bulk laptop purchases by using the Volume Discount element within the pricing procedure.

SEE ALSO
Calculate Cumulative Quantity Pricing for Contractual Discounts
Create a Price Adjustment Tier Records
Create a price adjustment tier record.
Specify these details.
Price Adjustment Schedule: Standard Price Adjustment Tier
Product: Laptop
Tier Type: Percentage
Tier Value: 10
Lower Bound: 100
Upper Bound: 299
Effective From: 01-01-2025
Product Selling Model: One Time
Click Save & New.
Create another price adjustment tier record with these details.
Price Adjustment Schedule: Standard Price Adjustment Tier
Product: Laptop
Tier Type: Percentage
Tier Value: 25
Lower Bound: 300
Effective From: 01-01-2025
Product Selling Model: One Time
Save your changes.
Close the tabs for the new price adjustment tiers that you created.
On the Details tab, on the Standard Price Adjustment Tier page, select Active.
Save your changes.
IMPORTANT We recommend refreshing the Volume Discount Entries decision table to make sure that the price adjustment tier records are available for pricing.
Create a Constant for a Volume Based Adjustment Variable
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
On the Pricing Procedure builder canvas, click .
On the Resource Manager panel, click Add Resource.
In the Add New Resource page, specify these details.
Resource Type: Constant
Resource Name: VolumePriceAdjustmentScheduleId
Data Type: Text
Default Value: Enter the price adjustment tier ID from the browser.
You can locate the value of your variable by going to the associated record. For example, to locate a price adjustment schedule ID, open the price adjustment schedule record page. The price adjustment schedule ID shows in the browser’s URL. 
Save your changes.
Add the Volume Discount Element
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
To provide discounts on laptops when they’re purchased in bulk, add the Volume Discount element.
Search for and add the Volume Discount Entries decision table and map these variables.
Input Rule Variables
Price Adjustment Schedule: VolumePriceAdjustmentScheduleId
Lower Bound: LineItemQuantity
Upper Bound: LineItemQuantity
Product: Product
Product Selling Model: ProductSellingModel
Effective From: EffectiveDate
Effective To: EffectiveDate
Input Variables
Quantity: LineItemQuantity
Input Unit Price: InputUnitPrice
Output Variables
List Price: NetUnitPrice
Subtotal: ItemNetTotalPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your laptop product and click Simulate again.
The price waterfall shows the volume discounts used to calculate the final price of the laptops, confirming that your procedure is working as expected.

Using the same example, go back to the Volume Discount element and select Use Cumulative Pricing. Here, map the Lower Bound and Upper Bound input variables to the AggregatedQuantity_std context tag.

On simulation, provide values for the AggregatedQuantity_std variable to calculate the cumulative price of the laptop.

IMPORTANT Cumulative discounts calculate only when a quote is associated with a pricing contract that has the aggregation strategy set to Cumulative.

=== ARTICLE: ind.pricing_configure_decision_explainer_for_price_waterfall.htm ===
---
article_id: ind.pricing_configure_decision_explainer_for_price_waterfall.htm
title: Configure Decision Explainer for Price Waterfall
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_decision_explainer_for_price_waterfall.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_decision_explainer_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Configure Decision Explainer for Price Waterfall

Map expression set message tokens and explainability message templates to pricing elements to customize the decision explanations in the price waterfall.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To configure decision explainer:	Salesforce Pricing Design Time
Create an Expression Set Message Token

Create tokens to represent specific values (like a net unit price) that you want to display dynamically in your explanation messages.

From Setup, in the Quick Find box, enter Decision Explainer, and then select Expression Set Message Token.
Click New Expression Set Message Token.
Provide a Name, Label, and Description (optional). For example, enter NetUnitPrice as the name and label.
Save your changes to use the token in explainability messages.
Create an Explainability Message Template

Define the success and failure messages that appear in the waterfall, and embed your tokens to show dynamic values.

From Setup, in the Quick Find box, enter Decision Explainer, and then select Explainability Message Template.
Click New Explainability Message Template.
Specify these details:
Name: Enter a name, for example, Successful message.
Label: Enter a label.
Message: Enter your custom text. To use a token, follow the format ${TokenName}. Example: My net unit price is ${NetUnitPrice}.
Expression Set Step Type: Business Element.
Usage Type: Pricing.
Save your changes.
Repeat these steps to create a template for failure messages if needed.
Configure the Pricing Procedure for Decision Explainer

Enable decision explanations within your pricing procedure and map your templates to the specific pricing elements.

Open your pricing procedure in the pricing procedure builder.
If the procedure is active, deactivate it to make edits.
Refresh the procedure to ensure the latest metadata is available.
Choose an element for which you would like to enable decision explainer.
Click 'Pricing Procedure Properties (gear icon) and select the Show decision explainer checkbox to enable decision explainer for the element.
In the Element Details panel, under the Decision Explainer section, enable Show decision explanation.
Configure the output messages:
When Step Returns Output: Search for and select the Success message template you created earlier.
Map Tokens: Click the icon next to the template field to map your message token (e.g., NetUnitPrice) to the corresponding Context Definition tag.
* When Step Errors: Search for and select the Failure message template you created earlier.
Save and activate your pricing procedure.

Click Simulate to verify that the price waterfall displays your custom explanation messages and dynamic token values for each step.

=== ARTICLE: ind.pricing_configure_decision_tables.htm ===
---
article_id: ind.pricing_configure_decision_tables.htm
title: Configure Decision Tables
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_decision_tables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Configure Decision Tables

Decision tables form the foundation of your pricing logic. Salesforce Pricing evaluates complex rules and looks up specific values, such as list prices, discounts, or volume tiers, based on defined input criteria. Configure standard decision tables that pull data directly from your Salesforce objects.

Create a Decision Table
To evaluate pricing rules and return specific pricing data such as list prices, discounts, or volume tiers, configure a standard decision table.
Create and Configure a CSV-Based Decision Table
You can use CSV-based decision tables to manage medium-scale pricing logic. After you create them, map these decision tables to a pricing recipe and use them in your pricing procedures.

=== ARTICLE: ind.pricing_configure_pricing_action_button_using_LWC.htm ===
---
article_id: ind.pricing_configure_pricing_action_button_using_LWC.htm
title: Customize the Pricing Action Button by Using Lightning Components
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_pricing_action_button_using_LWC.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_action_parameters.htm
fetched_at: 2026-09-07
---

# Customize the Pricing Action Button by Using Lightning Components

Add the Pricing Calculation standard Lightning component to object record pages to make custom pricing actions available across your org and calculate the price of a product directly from the record page.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To customize an Experience Cloud site:	

Be a member of the site AND Create and Set Up Experiences

OR

Be a member of the site AND an experience admin, publisher, or builder in that site

NOTE

The Calculate Price button is only for pricing Salesforce objects and doesn't support custom data hydration.

The more complex Quotes and Orders logic, which uses custom hydration for bundles and derived products, requires a custom-built pricing button that can act on persisted (saved) data. Therefore, the standard button should not be considered a replacement for Transaction Management's pricing logic.

On any object’s record page, click , and select Edit Page.
On the Builder page, from the Components panel, drag Pricing Calculation to the position where you want it to appear on the Lightning page canvas.
Use the Page panel to give your action a name.
Select the context definition, the context mapping, and the pricing procedure.
Save your changes, and exit Lightning App Builder.

=== ARTICLE: ind.pricing_configure_pricing_action_parameters_for_standards_objects.htm ===
---
article_id: ind.pricing_configure_pricing_action_parameters_for_standards_objects.htm
title: Configure Pricing Parameters for Standard Objects
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_pricing_action_parameters_for_standards_objects.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_get_ready_to_create_pricing_actions.htm
fetched_at: 2026-09-07
---

# Configure Pricing Parameters for Standard Objects

To ensure that the standard pricing action button functions properly, define pricing parameters that connect it to a context definition, the context's mapping, and the pricing procedure for calculating product prices.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To create pricing parameters:	

Salesforce Pricing Admin

IMPORTANT This prerequisite is only applicable to the objects that have the standard pricing actions. The objects are Quote, Order, Contract, Case, and Opportunity.
From Setup, in the Quick Find box, enter Pricing Action Parameters, and then select Pricing Action Parameters.
On the Pricing Action Parameters page, click New.
Specify these details.
Select the object name. 
The list of objects displayed here are the standard objects supported by Salesforce Pricing (Quote, Order, Contract, Case, Opportunity).
Select the context definition. 
You must select an extended context definition. This context definition must have nodes, attributes, and tags. To extend base context definition, see Context Definitions.
Select context mapping. 
Map the tags to the correct Salesforce objects. To prevent pricing calculation errors, select a mapping that matches your target object type.
Select the pricing procedure that performs the pricing policies.
Set the date range. The Effective From date specifies the date and time from when the pricing parameter is applied to an object. The Effective To date is optional.
Save your changes.

=== ARTICLE: ind.pricing_configure_pricing_procedure.htm ===
---
article_id: ind.pricing_configure_pricing_procedure.htm
title: Configure Your Pricing Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_pricing_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Configure Your Pricing Procedure

Assemble a pricing procedure using pricing elements and ensure accurate pricing for your products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User
To use pricing procedures:	Salesforce Pricing Run Time User
NOTE
Before building pricing procedures, ensure that you have added decision tables, enabled context definitions on your Salesforce org, set up a product selling model, and added products to a price book.
For pricing procedures created before Winter '27, Salesforce Pricing assigns Revenue Cloud as the default subtype.
When you create or clone a pricing procedure, the Subtype field shows only the clouds that match your active org licenses.
Create a Pricing Procedure

When you create a pricing procedure, the initial version is a blank and ready-to-use template. To perform pricing calculations, you must add pricing elements and call the appropriate decision tables. The Subtype field identifies which cloud a procedure belongs to - such as Revenue Cloud, Life Sciences Cloud, Commerce, or Insurance. Each cloud can implement its own functionality and validations for procedures of that subtype. Element lookups show decision tables from all pricing recipes assigned to that procedure's subtype.

From App Launcher, find and select Pricing Procedures.
Click New.
Specify these details.
Enter a name and then press Tab to autopopulate the API Name.
Select Pricing as the usage type.
Select a usage subtype.
The dropdown only shows the subtypes available based on your org's licenses. You can change the subtype when cloning the procedure, but not while editing it.
Associate the pricing procedure with a context definition.
For the purposes of all our examples, we've used the SalesTransactionContext context definition.
Save your changes.
On the Details tab, in the Pricing Procedure Versions section, click the pricing procedure version that you want to work on.
The Pricing Procedure Builder opens as a new tab.
Click , and select a pricing element from the list.
In the Lookup Table Details field, select the decision table and enter the values.
Depending on whether you want to show or hide the pricing information in the Waterfall view, select or deselect the price waterfall view for your element.
IMPORTANT

The Exclude Price Waterfall option isn't supported by Quotes in Revenue Management.

You can't exclude price waterfall for the Pricing Setting, Aggregate Price, Price Tracking, Stop Pricing, and Discovery Procedure elements.

Select the profiles that can see the pricing information in Waterfall view after simulation.
Click , and enter 1 as the rank number.
NOTE When more than one enabled version matches a pricing procedure, choose the version with the highest rank. For example, if two enabled versions have rank values set to 1 and 2, choose the version with rank 2.
Click , select Include in Output.
Save your procedure.
Store and Reuse Values with Local List Variables

A local list variable stores a calculated value from one pricing element so you can reuse it in a another element, without creating a context tag or constant. Local list variables are a separate category from context tags, constants, and the older variables resource type. You create it directly inside Pricing Procedure Builder, as you build your procedure.

In Pricing Procedure Builder canvas, click Resource Manager to expand the side panel and click Add Resource.
In the Add New Resource dialog, select Local List Variable as the Resource Type.
Select a variable type:
Node: Restricts the variable's scope to a specific structural node, such as the main Sales Transaction node.
Attribute: Scopes the variable to a specific child field or object attribute, such as a field on a Sales Transaction Item or Sales Transaction Group node beneath your selected parent.
Select a Parent Node, for example - SalesTransactionItem and enter a Resource Name.
Click Done, or Done And New to keep creating more local list variables.
In a pricing element, map the local list variable to an output field. This initializes variable's value during execution.
In a subsequent pricing element, map the same local list variable to an input field to reuse its stored value.
Key Configuration Considerations
The Include in Output checkbox controls whether the procedure includes an element's variables in the final response. You must select this for at least one element to ensure the procedure returns data for downstream processing.
Users map both Effective From and Effective To variables to the same EffectiveFrom tag for one-time products like laptops. Conversely, subscription-based products require distinct mappings to account for specific service durations.
The Pricing Setting element automatically maps standard variables like Net Unit Price and Subtotal by default. You only need to map these variables manually when you intend to override the system’s default values.
Don't activate a pricing procedure immediately after you modify its associated decision tables. To prevent the procedure from deploying with outdated metadata, make a minor change to the pricing procedure, save it again, and then activate it.
Map your local list variable as an output in a preceding element before referencing it as an input in a downstream element. If a pricing element references a variable as an input before an element initializes it, the pricing engine resolves the variable value to null.
The pricing engine does not support passing local list variables as inputs or initializing them externally via JSON payloads. They remain strictly local to the procedure execution context.
Standard actions like renaming and modifying the variable's data type are not supported at any time. Data types can only be deleted. Deleting a local list variable automatically clears all its active mappings throughout the pricing procedure version to prevent reference errors.
The system does not support local list variables within the Map Line Item element or the Propagation element.
Local list variables migrate automatically when you deploy or migrate pricing procedures across Salesforce orgs, eliminating manual recreation steps in target orgs.
Refresh Your Decision Tables

We recommend refreshing your decision tables to ensure that the latest pricing data is available.

To refresh your decision table, from Setup, in the Quick Find box, search for and select Decision Tables.
Select the appropriate decision table. For example, select the Volume Discount Entries decision table if you’ve made changes to price adjustment tier records.
Click Refresh.
Validate Your Decision Tables

Next, verify if the decision able has been refreshed and has the latest pricing data.

From the App Launcher, search for and open Lookup Tables.
Find and select Volume Discount Entries.
You can either check the Last Refreshed Date or you can search for the newly created price adjustment tier records.

=== ARTICLE: ind.pricing_configure_product_selling_model_for_your_products.htm ===
---
article_id: ind.pricing_configure_product_selling_model_for_your_products.htm
title: Configure a Product Selling Model for Your Products
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_product_selling_model_for_your_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_get_ready_to_build_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Configure a Product Selling Model for Your Products

Product selling models define how products are sold—be it one-time, term-defined, or evergreen subscriptions. They provide flexibility in managing diverse product offerings and streamline how those products are quoted, ordered, and renewed within a revenue management system. These models are crucial for accurately representing different sales approaches for your products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

=== ARTICLE: ind.pricing_configure_proration_settings.htm ===
---
article_id: ind.pricing_configure_proration_settings.htm
title: Configure Proration Settings
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_proration_settings.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_pricing_proration.htm
fetched_at: 2026-09-07
---

# Configure Proration Settings

Set custom pricing term values to calculate product prices based on your customer's subscription length.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER
PERMISSIONS NEEDED
To configure proration settings:	Salesforce Pricing Design Time

The pricing term count determines how many billing periods are used to calculate a product's subscription price. When you use the Proration or Subscription element in a pricing procedure, the selling model type variable is automatically populated with the values you configure here. Configure default pricing term count values for two selling model types: Evergreen and One Time.

If you leave a field blank, the pricing term count is calculated dynamically from the subscription start and end dates during pricing procedure execution.

From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
Enter values for Evergreen and One Time fields and save your changes.
FIELD	DESCRIPTION	EXAMPLE
Evergreen	The default pricing term count for subscriptions with no end date. Because evergreen subscriptions recur indefinitely, this value represents how many billing periods to include in the subscription price calculation.	A value of 1 means the subscription price equals one billing period. For a monthly subscription priced at $50/month, the Subscription element calculates a total price of $50.
One Time	The default pricing term count for one-time purchases. This value determines how many billing periods the one-time price covers.	A value of 1 means the price covers a single billing period. A value of 12 means the one-time price covers 12 periods.
NOTE You can only enter numeric values. Leave a field blank to calculate the pricing term count dynamically from the subscription start and end dates during pricing procedure execution.

=== ARTICLE: ind.pricing_configure_salesforce_pricing_objects.htm ===
---
article_id: ind.pricing_configure_salesforce_pricing_objects.htm
title: Configure Salesforce Pricing Objects
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_salesforce_pricing_objects.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Configure Salesforce Pricing Objects

To optimize Salesforce Pricing, configure the page layouts for Product, Price Book Entry, and Price Adjustment Schedule objects to ensure the proper display and functionality of pricing-related fields and related lists, thereby guaranteeing accurate product and service pricing and streamlining sales processes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To update object layouts:	

Salesforce Pricing Design Time


To customize an Experience Cloud site:	

Be a member of the site AND Create and Set Up Experiences

OR

Be a member of the site AND an experience admin, publisher, or builder in that site

NOTE The standard product lookup function (used on objects such as Opportunities and Work Orders) relies heavily on the record's context to find linked price book entries. If you customize these standard page layouts or use URL-based custom buttons, the product lookup can fail because it can't retrieve the necessary object or correlation IDs. If you build a custom page layout, include the parent object (such as the Opportunity or Work Order) as a field on the layout. Additionally, use custom actions rather than URL-based buttons so that the pricing engine successfully passes the required context IDs to the product lookup plug-in.
Update the Product Page Layout
From Object manager, search for and select the Product object.
Select Page Layouts, and then click Product Layout.
In the palette, click Related Lists.
Drag and drop these related lists to the Product’s page layout:
Price Adjustment Tier
Attribute Based Adjustment
Bundle Based Adjustment
Parent Products
Derived Products
Source Products
Save your changes.
Configure Price Book Entry
From Object manager, search for and select the Price Book Entry object.
Select Page Layouts, and then click Price Book Entry Layout.
In the palette, click Fields.
Drag and drop Product Selling Model field to the Price Book Entry’s page layout.
After you create a price book entry, you can't change the Product Selling Model field. If you need the same product with a different selling model, deactivate the existing price book entry and create a new one with the desired product selling model.
Save your changes.
Configure Price Adjustment Schedule
From Object manager, search for and select the Price Adjustment Schedule object.
Select Page Layouts, and then click Price Adjustment Schedule Layout.
In the palette, click Related Lists.
Drag and drop the Attribute Based Adjustment related list to the Price Adjustment Schedule’s page layout
Save your changes.

=== ARTICLE: ind.pricing_configure_the_price_propagation_element.htm ===
---
article_id: ind.pricing_configure_the_price_propagation_element.htm
title: Configure the Price Propagation Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_configure_the_price_propagation_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_propagation.htm
fetched_at: 2026-09-07
---

# Configure the Price Propagation Element

Define the formulas and execution sequence for your hierarchical pricing logic by using the Price Propagation element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User
Define a context definition that specifically supports the nested group hierarchy structure within your quotes (for example, Sales Transaction Context).
Configure the necessary context mappings to link your pricing procedure to your data.
Configure Propagation Rules and Nodes
Open an existing pricing procedure or create a new one.
NOTE If you're using an existing procedure, make sure it doesn't already contain a price propagation, derived price, or promotion element.
Click  to add the Pricing Setting element, select Enable Propagation, and map your common variables (if not already configured).
In the Price Setting element, under Propagation Setting, select Configure Propagation Rules.
In the Configure Propagation Table window, select one of these options:
Configure a new table: Select this to define your nodes, joins, and formulas from scratch. Proceed with the steps below.
Select a template: Select the Map sales SalesTransactionItem to SalesTransactionGroup template. This template is based on the predefined Sales Transaction Context and automatically maps SalesTransactionItem records to the SalesTransactionGroup.
IMPORTANT After you enable Price Propagation in Pricing Settings, configure the propagation table before you save the pricing procedure. If you skip this step, the save can fail with the error LookUpName isn’t a valid variable name.
Select Add Nodes and select these attributes.
SalesTransactionItem:
ItemDiscountPercentage
ListPrice
ItemUnitCost__std
ItemNetTotalPrice
ItemTotalMarginAmount__std
SalesTransactionItemGroup
SalesTransactionGroup:
GroupDiscount__std
SummarySubtotal
GroupTotalMarginAmount__std
GroupSource
Under Join Nodes, define the parent-child relationship between your data levels so the procedure knows how to propagate values.
Mapping Type: Parent-Child
Parent Key: GroupSource
Child Key: SalesTransactionItemGroup
Node Identifier: Select a unique identifier (like Line Item Tag) to track these calculations in the execution logs.
Select Merge Attributes and specify these attributes.
Attribute Name: Merged_header_1
Merged Condition: Not Null
Attribute 1: GroupTotalMargin_std
Attribute 2: ItemTotalMargin_std
Define Logic for Horizontal Propagation
To define your pricing logic, select Edit Attributes.
Define your Horizontal Formulas for line-level calculations.
Select the column you want to calculate (for example, Net Unit Price).
Enter the formula (for example, UnitCost + MarginAmount).
Enter a sequence number (for example, 1, 2) to tell the procedure which formula to run first.
Configure the Use Zero for Null Values setting.
If enabled, null inputs are treated as 0 and the formula proceeds to the next step.
If disabled, any formula with a null argument is skipped.
NOTE

The Sequence field cannot be empty or negative, and two fields cannot share the same sequence number.

The system does not auto-adjust sequences. If you change the sequence of one formula, you must manually update the sequence numbers for all other formulas to ensure the correct order.

Define Logic for Ascending Propagation
Define your Ascending Propagation to roll up values to the parent.
Create a merged attribute (for example, Merge Total Cost).
Select the aggregation function Sum.
Specify the child field to roll up ( for example, Sum(!Child.ItemTotalCost)).
If needed, add up to three conditions to filter the child items included in the calculation (for example, SellingModelType = 'One Time'). All specified conditions must be met for a line item to be included. Items that don't match the criteria or contain null values in the specified fields are excluded from the rollup.
Save the propagation rules.
Add the Price Propagation Element
Add the Price Propagation element.
Save and activate the procedure.

=== ARTICLE: ind.pricing_considerations_for_importing_and_exporting_pricing_data.htm ===
---
article_id: ind.pricing_considerations_for_importing_and_exporting_pricing_data.htm
title: Considerations for Importing and Exporting Pricing Data
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_considerations_for_importing_and_exporting_pricing_data.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Considerations for Importing and Exporting Pricing Data

Use a packaged file to import and export pricing metadata from one org to another, including pricing recipes, decision tables, context definitions, and pricing procedures. These metadata components are crucial for ‌pricing processes, where pricing procedures use recipes for accurate calculations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Pricing recipes are associated with decision tables, other individual decision tables, and context definitions. A pricing procedure then calls these definitions to perform pricing calculations. When you export or import this data, you must follow certain guidelines to ensure the data is transferred successfully.

Key considerations when you export pricing data to a package file
Before you do anything else, export your context definitions and decision tables.
When you export a pricing recipe, all the decision tables and discovery procedures mapped to it are packaged together.
The default pricing recipe selected from the Setup page is packaged with the default pricing procedure.
The decision tables associated with a procedure, including the org’s default pricing procedure, are packaged with the procedure.
Key considerations when you import pricing data from a package file
Import your context definitions and decision tables before anything else.
Before you import the pricing procedures, make sure you import all pricing recipes and the decision tables associated with the procedure.
NOTE Before importing data, check your org's current decision tables to ensure you're within the limits. Importing decision tables without verifying available space may cause the data import to fail.
Export and Import Your Pricing Data
To create a new package with your pricing data to reuse them in another Salesforce org, create a new package and deploy it on another Salesforce org.

=== ARTICLE: ind.pricing_considerations_for_migrating_attribute_based_adjustments.htm ===
---
article_id: ind.pricing_considerations_for_migrating_attribute_based_adjustments.htm
title: Considerations for Migrating Attribute-Based Adjustments
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_considerations_for_migrating_attribute_based_adjustments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_attribute_based_price_element.htm
fetched_at: 2026-09-07
---

# Considerations for Migrating Attribute-Based Adjustments

To prevent hash mismatch issues when you migrate attribute-based adjustment records across Salesforce orgs, follow this process.

Always deploy records in the following order:

Attribute Based Adjustment Rules
Attribute Adjustment Conditions
Attribute Based Adjustments

Migration and batching guidance

When migrating records by using Data Loader or APIs, move all Attribute Adjustment Condition records for the same parent Attribute Based Adjustment Rule in one batch.
Do not split child condition records for the same parent rule across parallel batches. Parallel insertion can produce hash conflicts and can prevent adjustments from being applied.
If you use bulk processing, keep parent-child dependencies intact and preserve sequence. Child records must be inserted after their parent records.

Validation guidance

There is no single automated validation that checks all migrated records at once. Validate migrated records in the Pricing Operations Console before completing deployment.

Troubleshooting

In some cases, adjustments do not apply after migration even when record configuration appears correct and the decision table is refreshed. This can happen when there's a hash mismatch. To troubleshoot and resolve a hash mismatch:

Compare the hash generated in Revenue Cloud Ops Console and the hash value of the Attribute Adjustment Conditions record. If the hashes don't match, the records are out of sync.
To fix the mismatch, open any affected Attribute Adjustment Condition record and save it without making any changes. Saving the record regenerates the parent hash.

After saving, run a validation transaction to confirm the adjustment is applied as expected.

=== ARTICLE: ind.pricing_contract_based_pricing.htm ===
---
article_id: ind.pricing_contract_based_pricing.htm
title: Contract-Based Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_contract_based_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_unique_pricing_scenarios.htm
fetched_at: 2026-09-07
---

# Contract-Based Pricing

Manage and apply contact-based pricing deals on previously negotiated pricing agreements defined in a contract.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Contract-Based Pricing allows businesses to offer customers special prices agreed upon in a contract. This means that instead of standard prices, sales teams can use prices specifically negotiated with a buyer. You can also apply special deals that can override existing pricing methods, including base price calculations and various discount types.

Calculate Contract-Based Pricing
Before you begin to calculate contracted prices, do the following.

=== ARTICLE: ind.pricing_create_a_custom_procedure_plan_definition.htm ===
---
article_id: ind.pricing_create_a_custom_procedure_plan_definition.htm
title: Create a Custom Procedure Plan Definition
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_a_custom_procedure_plan_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_create_procedure_plans.htm
fetched_at: 2026-09-07
---

# Create a Custom Procedure Plan Definition

Create custom procedure plan definitions that contain only selected types of procedures. You can further filter these definitions by configuring multiple criteria and conditions within a procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create and update procedure plan definitions:	

Procedure Plan Access

AND

Salesforce Pricing Design Time User

From Setup, in the Quick Find box, enter Procedure Plan Definitions, and then select Procedure Plan Definitions.
Select New, provide the procedure plan definition details, and save the details to create your procedure.
The Primary Object field is optional. However, if you don’t provide a source object, you can’t create a procedure with rule-based criteria.
The Subtype field is optional. To apply the procedure plan to a specific industry or vertical use case, enter the information in the optional Subtype field. The plan then orchestrates only pricing procedures of the same subtype.
Open the newly created procedure plan definition.
If necessary, set the context mapping to read and save data from a mapped object.
The context definition that you select when you create the procedure plan definition record is auto-populated.
To add the procedures that you want in the Procedure Plan Sections, select Add.
Specify the procedure plan section that you want to create.
Standard	Choose from a list of default procedure plans included with Revenue Management (formerly Revenue Cloud), filtered by their usage type.
Custom	Configure your procedure without a usage type filter.
To map your procedure to different stages of the business lifecycle, associate your procedure with a phase.
Based on the procedure plan section that you selected, set a resolution type.
Default	Select a procedure from the list of procedures available in your org.
Rule-Based	Set selection criteria to verify how a procedure can be configured for a selected procedure plan section record.
IMPORTANT Ensure that the context definition related to your procedure plan definition and pricing procedures is the same.
To set the order that the procedures are executed in, select Manage Sections.
If necessary, modify the effective date ranges for this procedure plan definition record.
Save your changes and activate the definition of your procedure plan.

=== ARTICLE: ind.pricing_create_a_procedure_output_resolution_record.htm ===
---
article_id: ind.pricing_create_a_procedure_output_resolution_record.htm
title: Configure Pricing Resolution Strategies
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_a_procedure_output_resolution_record.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_output_resolution.htm
fetched_at: 2026-09-07
---

# Configure Pricing Resolution Strategies

To set a pricing resolution strategy, create a procedure output resolution record.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create procedure output resolution records:	Salesforce Pricing Design Time

The main goal of creating a strategy is to define a formula to calculate the highest and lowest prices. The resources in the Formula section are based on the pricing element you’ve selected. If you specify a comma-separated list, the variables or resources are used as tiebreakers.

For example, if you define a formula as Min(List price, Priority), and two price books return the same list price, the price book with the priority tag value of lower numerical value is selected.

From the App Launcher, find and select Price Management.
From the app navigation menu, select Procedure Output Resolutions.
Click New.
Specify these details.
Give your procedure output resolution record a name.
Select your pricing element.
You can select only the List Price, Price Tracking, and Price Adjustment Matrix elements.
To define your pricing resolution strategy, enter a formula.
To define your pricing resolution strategy, enter a formula. To define a formula, follow the steps below.
Select a function in the Search Function field.
Highlight the value within the brackets and delete it.
Place your cursor in the brackets and then, select a resource from the Select a resource field.
NOTE The Stack and Sequence formula options appear only when you select the Price Adjustment Matrix element.
Save your changes.

=== ARTICLE: ind.pricing_create_a_proration_policy.htm ===
---
article_id: ind.pricing_create_a_proration_policy.htm
title: Create a Proration Policy for a Subscription
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_a_proration_policy.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_pricing_proration.htm
fetched_at: 2026-09-07
---

# Create a Proration Policy for a Subscription

Manage charges for partial subscription periods and choose whether remainders are applied to the first or last pricing period.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create a proration policy:	Salesforce Pricing Design Time

To create a proration policy, you must have a term-defined or evergreen product selling model and a price book entry for the product.

Create a Proration Policy
From the App Launcher, find and select Proration Policies.
Click New, and enter a descriptive name.
For Proration Policy Type, select Standard Time Periods.
For Remainder Strategy, select whether the pricing engine adds the remainder from a rounded calculation to the first or last pricing period.
The remainder strategy makes sure that the sum of the pricing-period amounts equals the original amount. For example, dividing $100 equally across three pricing periods produces the round amount of $33.33 per period. The total is $99.99, with a difference of $0.01 remaining.

If you add the remainder to the first pricing period, the pricing-period amounts are $33.34, $33.33, and $33.33. If you add the remainder to the last pricing period, the pricing-period amounts are $33.33, $33.33, and $33.34.

To prorate a subscription that includes part of a pricing period, select Allow partial proration periods.
If you don't select this option, the pricing engine charges the full pricing period.
Save your changes.
Assign a Proration Policy to a Product

Connect the product, its selling model, and the proration policy.

From the App Launcher, find and select Price Books.
Select a price book.
Under Price Book Entries, select the product.
On the Related tab, in the Product Selling Model Options related list, click New.
Select a term-defined or evergreen selling model.
You can assign a proration policy only to a term-defined or evergreen product selling model.
Confirm that the Product field shows the product that you selected from the price book entry.
Select a proration policy.
To use this product selling model option as the default for the product, select Default.
Click Save.

=== ARTICLE: ind.pricing_create_a_standard_decision_table.htm ===
---
article_id: ind.pricing_create_a_standard_decision_table.htm
title: Create a Decision Table
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_a_standard_decision_table.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_configure_decision_tables.htm
fetched_at: 2026-09-07
---

# Create a Decision Table

To evaluate pricing rules and return specific pricing data such as list prices, discounts, or volume tiers, configure a standard decision table.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create and manage decision tables:	

Salesforce Pricing Design Time

When you configure decision tables for pricing, each combination of input values must resolve to a single, unique row. Salesforce Pricing doesn't support retrieving multiple outputs for the exact same input criteria. Set up your decision table to map each specific input value to only one output entry.

1. From the App Launcher, search for and select Lookup Tables.
Select Decision Table, and then click New
Enter a name for your decision table, and then press Tab to autopopulate the API Name.
Select Pricing as the application usage.
Select Advanced as the decision table type.
Click Save & Next.
In the Source Object field, select the standard or custom object that contains your pricing data.
Define your input conditions:
Select the appropriate source object fields and set their operators.
Verify that the Condition Type (for example, All conditions are met (AND)) aligns with your required pricing logic.
Specify the result details by selecting the source object fields that you want to return as outputs, and define a column name for each.
Click Save & Next.
Review your configuration, and click Save & Next again.
Click Finish.
On the decision table record page, click Activate.

=== ARTICLE: ind.pricing_create_and_configure_a_csv_based_decision_table.htm ===
---
article_id: ind.pricing_create_and_configure_a_csv_based_decision_table.htm
title: Create and Configure a CSV-Based Decision Table
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_and_configure_a_csv_based_decision_table.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_configure_decision_tables.htm
fetched_at: 2026-09-07
---

# Create and Configure a CSV-Based Decision Table

You can use CSV-based decision tables to manage medium-scale pricing logic. After you create them, map these decision tables to a pricing recipe and use them in your pricing procedures.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create and manage decision tables:	

Salesforce Pricing Design Time

NOTE All CSV-based decision tables created after the Usage 262 upgrade are automatically versioned.
CSV-Based Decision Table Limitations
Before configuring a CSV-Based Decision Table, keep these points in mind.
SEE ALSO
Considerations for Migrating Decision Tables
Create the Decision Table
From the App Launcher, find and select Lookup Tables.
Select Decision Table, and click New.
Specify the basic details, and select Pricing as the application usage.
Select Advanced as the Decision Table Type. 
For the Source Object, select CSV.
Define your input columns, such as Product and Price Book, and then define your output columns, such as Unit Price and Discount.
Click Save.
Upload Data to the Decision Table 
When you save the decision table, Salesforce Pricing creates a single, inactive version by default. For steps to upload CSV data for the decision table, see Add CSV Data to Decision Tables.
Activate and Map the Decision Table
After the data uploads successfully, activate the decision table version.
Go to Pricing Recipes, and select the recipe that you want to modify (for example, Price Adjustment Matrix).
Map your new CSV-based decision table to the recipe by specifying the relevant input, output, and discount type columns.
Save your changes. You can now select this decision table within the elements of your pricing procedure.

=== ARTICLE: ind.pricing_create_attribute_based_adjustments.htm ===
---
article_id: ind.pricing_create_attribute_based_adjustments.htm
title: Create Attribute Based Adjustments
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_attribute_based_adjustments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_attribute_based_price_element.htm
fetched_at: 2026-09-07
---

# Create Attribute Based Adjustments

Set up pricing rules that automatically adjust prices and offer discounts based on a product's price-impacting attributes by creating attribute-based adjustment records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create attribute based adjustment records:	

Salesforce Pricing Design Time


To access the Attribute Adjustment Condition object:	Salesforce Pricing Manager
IMPORTANT Before you create an attribute based adjustment record, ensure that your Salesforce org has a product selling model and has products added to a price book. Define attributes to your products and ensure that at least one is price-impacting.

Salesforce Pricing provides a predefined Standard Attribute Based Adjustment that you can use, or you can create a custom one.

From the App Launcher, find and select Price Management.
From the app navigation menu, select Price Adjustment Schedules.
Change the list view to All Price Adjustment Schedules.
Click Standard Attribute Based Adjustment.
If your price adjustment schedule is active, deactivate it before adding more records.
Select Attribute Based Adjustment.
TIP For faster record creation, you don't always need to navigate through menus. You can directly select Attribute Based Adjustments from the app launcher to create a new price adjustment tier record. Then, you can follow along from step 6.
Click New.
Specify these details to create a price adjustment tier record.
Select a product.
Select a product selling model.
Select the adjustment type.
Select Percentage if the discount on the product is applied as percentage.
Select Amount if the discount on the product is applied as a flat amount.
Select Override if the discount amount falls outside the pricing policy's rule.
Specify the adjustment value.
Enter the effective date range.
Click Next.
Set the condition for when the attribute based adjustment is applied.
Save your changes.
On the Price Adjustment Schedule’s page, select Active to activate your Attribute Based Adjustment.
SEE ALSO
Create Price Adjustment Schedules

=== ARTICLE: ind.pricing_create_bundle_based_adjustments.htm ===
---
article_id: ind.pricing_create_bundle_based_adjustments.htm
title: Create Bundle Based Adjustments
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_bundle_based_adjustments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_bundle_based_price_element.htm
fetched_at: 2026-09-07
---

# Create Bundle Based Adjustments

Define bundle based adjustments to calculate discounts for products being sold as a bundle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create bundle based adjustment records:	

Salesforce Pricing Design Time

IMPORTANT Before you create bundle based adjustments, ensure that your Salesforce org is set up with these details.
A product, its root bundles, and the parent product.
All of these products must be associated with a price book.
Product selling model and a selling model for the parent product and root bundle.
To understand more about bundled products, and how to set them, see Create Bundled Products.

Salesforce Pricing provides a predefined Standard Bundle Based Adjustment that you can use, or you can create a custom one.

From the App Launcher, find and select Price Management.
From the app navigation menu, select Price Adjustment Schedules.
Change the list view to All Price Adjustment Schedules.
Click Standard Bundle Based Adjustment.
If your price adjustment schedule is active, deactivate it before adding more records.
Select Bundle Based Adjustment.
TIP For faster record creation, you don't always need to navigate through menus. You can directly select Bundle Based Adjustments from the app launcher to create a new price adjustment tier record. Then, you can follow along from step 6.
Click New.
Specify these details to create a bundle based adjustment record.
Select a root bundle.
Select the root bundle selling model.
Select the parent product.
Select the parent product selling model.
Select a product.
Select a product selling model.
Select the adjustment type.
Select Percentage if the discount on the product is applied as percentage.
Select Amount if the discount on the product is applied as a flat amount.
Select Override if the discount amount falls outside the pricing policy's rule.
Specify the adjustment value.
Enter the effective date range.
Select the price adjustment schedule.
Save your changes.
On the Price Adjustment Schedule’s page, select Active to activate your Bundle Based Adjustment.

=== ARTICLE: ind.pricing_create_constant_resource.htm ===
---
article_id: ind.pricing_create_constant_resource.htm
title: Create Constant Resources
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_constant_resource.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_get_ready_to_build_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Create Constant Resources

If your variables lack context tags, create a constant resource to serve as a placeholder for fixed values in your pricing procedures. Constants are used for inputs, outputs, and other values passed from a pricing element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
NOTE Salesforce Pricing only supports the creation and use of constant resources.

For example, create a constant for the VolumeBasedAdjustment input variable.

Create a pricing procedure.
On the the Pricing Procedure builder canvas, click .
On the Resource Manager panel, click Add Resource.
Specify the resource type, name, data type, and default values.
When naming constants, use unique identifiers and avoid reserved keywords such as Currency, Number, or Text.
Save your changes.

=== ARTICLE: ind.pricing_create_context_definitions.htm ===
---
article_id: ind.pricing_create_context_definitions.htm
title: Context Definitions
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_context_definitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_get_ready_to_build_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Context Definitions

Context definitions contain the necessary information to run the pricing process. This includes the relationship between nodes and their structure, attributes, context tags, and mapping. Mapping defines the nodes and attributes with the correct input data from Salesforce objects. The pricing procedure runs with its associated tags and writes the results back to the context definition that the tags belong to. A crucial point to remember is that a context tag can’t have the same name as the decision table's label or API name.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

End-to-end transactions in Revenue Management run on the SalesTransactionContext context definition. This context definition links sales transactions to objects such as quotes, assets, and orders.

IMPORTANT

Salesforce Pricing doesn't work directly with the SalesTransactionContext__stdctx base context definition. To use pricing procedures, always extend the base context. An extended context definition inherits the structure, nodes, and attributes from the base context definition while allowing you to add custom nodes, attributes, and tags for your pricing logic.

=== ARTICLE: ind.pricing_create_new_pricing_recipe.htm ===
---
article_id: ind.pricing_create_new_pricing_recipe.htm
title: Create a Pricing Recipe
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_new_pricing_recipe.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_recipes.htm
fetched_at: 2026-09-07
---

# Create a Pricing Recipe

Learn how to create a custom pricing recipe to group and associate your custom decision tables, enabling precise control over pricing calculations in your Salesforce org. This task is essential when the predefined recipe doesn't meet your specific business needs. Use the Subtype field to set up the default pricing recipe and decision tables for each cloud, such as Revenue Cloud or Life Sciences Cloud. While building or editing a pricing procedure, element lookups display only the decision tables linked to the default recipe of that procedure's subtype.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To manage pricing recipes:	

Salesforce Pricing Design Time

IMPORTANT
You must set up your decision tables before you use a custom pricing recipes.
For pricing procedures created before Winter '27, Salesforce Pricing assigns Revenue Cloud as the default subtype.
When you create or clone a pricing recipe, the Subtype field shows only the clouds that match your active org licenses.
From Setup, in the Quick Find box, find and select Pricing Recipes.
Enter a name for the new recipe.
Select a subtype from the dropdown.
The Subtype field shows only the subtypes that are available based on your active cloud licenses. Each subtype can have multiple recipes, including one default recipe that you can change. You can change the subtype when cloning a recipe, but not while editing a recipe.
Save your changes.
Select the recipe that you created to open its details page.
On the recipe's detail page, select the Price Adjustment Matrix tab.
To add decision tables, click Modify and then select the decision tables you want to associate with this recipe.
When you create a pricing procedure with the usage type set to Pricing, you will see the predefined decision tables and any custom ones you associated with this recipe.
Save your changes.

=== ARTICLE: ind.pricing_create_or_use_predefined_lookup_tables.htm ===
---
article_id: ind.pricing_create_or_use_predefined_lookup_tables.htm
title: Decision Tables
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_or_use_predefined_lookup_tables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_get_ready_to_build_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Decision Tables

Decision tables are essential as they match your input values with the input rows in a decision table, returning the matching row’s output pricing element that uses it in a pricing procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Decision tables provide a structured, efficient, and maintainable way to manage complex pricing logic without needing to hardcode numerous conditional statements. You can centralize and organize these rules into a clear, tabular format using decision tables. The tabular format makes it easy to see all the conditions applied and their corresponding outcomes at a glance. This transparency helps in understanding why a particular price was derived and makes it easier to audit pricing decisions.

NOTE We recommend that you use the Advanced decision table type instead of the Standard type.

When working with decision tables, you'll map various variables.

Input Rule Variables: These refer to the input from the selected decision table.
Output Rule Variables: These refer to the output from the selected decision table.
Input Variables: These refer to the input provided by the pricing element.
Output Variables: These refer to the output generated from the pricing element.
Additional Variables: These are custom output variables reflecting a pricing change. Their values can only be added using the Advanced mode (JSON) during simulation and are visible in the waterfall view.
NOTE To enable multicurrency with active pricing procedures linked to predefined Salesforce Pricing decision tables, first deactivate the pricing procedure, then enable multicurrency, and finally reactivate the procedure. Similarly, to add the Currency field to a predefined decision table in a multicurrency org, you must deactivate the decision table, add the field, and then activate it.

=== ARTICLE: ind.pricing_create_price_adjustment_schedules.htm ===
---
article_id: ind.pricing_create_price_adjustment_schedules.htm
title: Create and Manage Price Adjustment Schedules
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_price_adjustment_schedules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_adjustment_schedules_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Create and Manage Price Adjustment Schedules

Define price adjustment schedules and set volume, attribute, or bundle-based discounts for your products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create price adjustment schedules:	

Salesforce Pricing Design Time

Salesforce Pricing comes with several predefined price adjustment schedules that you can use right out of the box, including:

Standard Attribute Based Adjustment
Standard Bundle Based Adjustment
Standard Price Adjustment Tier

You can use these, or create custom price adjustment schedules tailored to your business rules. Any existing price adjustment schedule can also be easily cloned, saving you time.

To create a price adjustment schedule record, follow these steps:

From App Launcher, find and select Price Adjustment Schedules.
Click New.
Give your price adjustment schedule a name.
Select the Adjustment Method.
Range	Select this option if you want to give all your products the same discount options. For example, you can give a flat discount of 10% when a customer purchases 10 items or more.
Slab	Select this option if you want to give different discounts based on the conditions set. For example, you can give the customer a discount of 10% for the first 10 items and 15% when they purchase 11–20 items.
Select the Schedule Type.
Volume	Select this option if you want to give a discount based on the quantity. For example, a flat discount of 10% on purchase of 50 items or more.
Attribute	Select this option if you want to give discounts based on the attributes associated with the product. For example, a discount of $50 on all red mobile phones.
Bundle	Select this option if you want to give a discount on different items sold together as a single product. For example, a discount of 10% if your customer purchases a television with a warranty.
Provide an effective date range.
The Effective From date specifies the date and time from when the discount is applied to the product. If you don’t choose an Effective To date, the discount applies indefinitely.
Save your changes.

You can modify price adjustment schedule records in two ways: by updating the fields that have the icon. If you update the price details, another record is created.

=== ARTICLE: ind.pricing_create_price_adjustment_tiers_volume_discounts.htm ===
---
article_id: ind.pricing_create_price_adjustment_tiers_volume_discounts.htm
title: Create Price Adjustment Tiers for Volume Discounts
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_price_adjustment_tiers_volume_discounts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_volume_discount_element.htm
fetched_at: 2026-09-07
---

# Create Price Adjustment Tiers for Volume Discounts

Set up pricing rules that automatically adjust prices and offer discounts based on the quantities purchased by creating price adjustment tier records. You can use them to implement various strategies, including both volume or tiered discounts. This adjustment type enables you to define a product's price based on the number of items being sold.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create price adjustment tiers:	

Salesforce Pricing Design Time

IMPORTANT Before you create a price adjustment tier record, ensure that your Salesforce org has a product selling model and has products added to a price book.

Salesforce Pricing provides a predefined Standard Price Adjustment Tier that you can use, or you can create a custom one.

From the App Launcher, find and select Price Management.
From the app navigation menu, select Price Adjustment Schedules.
Change the list view to All Price Adjustment Schedules.
Click Standard Price Adjustment Tier.
If your price adjustment schedule is active, deactivate it before adding more records.
Select Standard Price Adjustment Tier.
TIP For faster record creation, you don't always need to navigate through menus. You can directly select Price Adjustment Tiers from the app launcher to create a new price adjustment tier record. Then, you can follow along from step 6.
Click New.
Specify these details to create a price adjustment tier record.
Select a product.
Select a product selling model.
Select the price adjustment schedule that must be associated with this price adjustment tier record.
IMPORTANT You can't create standalone price adjustment tier records. Associate each record with a price adjustment schedule of type Volume.
Select the tier type.
Select Percentage if the discount on the product is applied as percentage.
Select Amount if the discount on the product is applied as a flat amount.
Select Override if the discount amount falls outside the pricing policy's rule.
Specify the tier value.
If the tier type is Percentage, the tier value is the percentage value of the discount, for example, 10%. If the tier type is Amount, the tier value is the flat amount of the discount, for example, US$100.
Enter the Lower Bound and Upper Bound values.
These values represent the minimum and maximum quantity of discount that can be applied to the product.
IMPORTANT The lower and upper bound values in the volume-based discounts decision table are inclusive, and the tiers can't overlap.
Enter the effective date range.
IMPORTANT
Price adjustment tiers with the same effective date must have consecutive lower and upper bound values, with no gaps.
To prevent calculation errors, especially when multi-currency is disabled, don't create duplicate Price Adjustment Tier records. For a unique combination of Product, Product Selling Model, Price Adjustment Schedule, Currency, and Effective Dates, make sure that the quantity ranges (Lower and Upper Bounds) don't overlap.
Save your changes.
On the Price Adjustment Schedule’s page, select Active to activate your Price Adjustment Tier adjustment schedule.
SEE ALSO
Create Price Adjustment Schedules

=== ARTICLE: ind.pricing_create_procedure_plan_defintions_templates.htm ===
---
article_id: ind.pricing_create_procedure_plan_defintions_templates.htm
title: Create Procedure Plan Definitions by Using Templates
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_procedure_plan_defintions_templates.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_create_procedure_plans.htm
fetched_at: 2026-09-07
---

# Create Procedure Plan Definitions by Using Templates

A procedure plan definition template only stores the sequence of the procedure plan sections. You can modify the template to add a context definition and appropriate procedures within the procedure plan section based on your business needs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create and update procedure plan definitions:	

Procedure Plan Access

AND

Salesforce Pricing Design Time User


To set up product discovery:	

Manage Product Index and Search

AND

View Product Catalog

For example, users of Salesforce Pricing can use the Default Procedure Plan Definition Template and Product Catalog Management users can use the Default Product Discovery Procedure Plan Definition Template. They can add their context definition and the procedures that they need and then save the context definition as a procedure definition for their organization.

From Setup, in the Quick Find box, enter Procedure Plan Definition Templates, and then select Procedure Plan Definition Templates.
Select a template.
Specify your context definition.
If necessary, set the context mapping to read and save data from a mapped object.
Modify your procedures in the Procedure Plan Sections.
To set the order that the procedures are executed in, select Manage Sections.
To set the execution order of your procedures, select  and drag your procedure sections.
Save your template as a new procedure plan definition record.

Your new procedure plan definition record appears in the Procedure Plan Definitions list. To view the list, go to Setup, in the Quick Find box, enter Procedure Plan Definitions, and then select Procedure Plan Definitions.

=== ARTICLE: ind.pricing_create_procedure_plans.htm ===
---
article_id: ind.pricing_create_procedure_plans.htm
title: Create Procedure Plans
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_create_procedure_plans.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_plan_framework.htm
fetched_at: 2026-09-07
---

# Create Procedure Plans

To create a flexible and comprehensive workflow that adapts to your business needs, use a Procedure Plan Definition to combine and sequence individual procedures into a single, unified plan. You can start quickly with a predefined template or customize one from scratch to meet your unique requirements.

NOTE Procedure plan definitions function exclusively as a metadata framework. They serve as a logical container for conditions and their associated procedures. Procedure plan definitions don’t self-orchestrate. In Revenue Management (formerly Revenue Cloud), only the PST API orchestrates a procedure plan.
Create Procedure Plan Definitions by Using Templates
A procedure plan definition template only stores the sequence of the procedure plan sections. You can modify the template to add a context definition and appropriate procedures within the procedure plan section based on your business needs.
Create a Custom Procedure Plan Definition
Create custom procedure plan definitions that contain only selected types of procedures. You can further filter these definitions by configuring multiple criteria and conditions within a procedure.

=== ARTICLE: ind.pricing_csv_based_decision_table_limitations.htm ===
---
article_id: ind.pricing_csv_based_decision_table_limitations.htm
title: CSV-Based Decision Table Limitations
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_csv_based_decision_table_limitations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_create_and_configure_a_csv_based_decision_table.htm
fetched_at: 2026-09-07
---

# CSV-Based Decision Table Limitations

Before configuring a CSV-Based Decision Table, keep these points in mind.

Salesforce Pricing doesn’t support CSV-based decision tables with pricing discovery.
Salesforce Pricing doesn’t recommend or support creating multiple versions for CSV-based decision tables. If multiple versions are created, Salesforce Pricing reads the decision table CSV version that is active on the current date.
You can’t use CSV-based decision tables with the Attribute-Based Price element or with the Price Tracking element’s Save operation. However, the Get operation continues to work.
The Enable Multiple Output Resolution checkbox isn’t supported. Don’t enable this function when you use a CSV-based decision table.
The real-time option isn’t supported for handling CSV data on a quote.
SOQL queries aren’t supported with CSV-based decision tables.
Salesforce Pricing doesn’t provide standard CSV files with this feature. Download the sample template from your specific decision table version, and populate it manually.
Salesforce Pricing doesn’t pass a custom date value to CSV-based decision tables. It uses the current system date and time. If multiple versions are valid on the current date, the highest-ranked version is selected.
CSV-based decision tables support only Datetime, Text, Boolean, and Number data types. Currency isn’t supported as an input rule variable parameter.
Previously created CSV-based decision tables remain unversioned. These tables continue to work in pricing procedures, but built-in versioning isn’t available for them.
SEE ALSO
Decision Table

=== ARTICLE: ind.pricing_customize_pricing_procedures_with_apex_hooks.htm ===
---
article_id: ind.pricing_customize_pricing_procedures_with_apex_hooks.htm
title: Customize Your Procedure Plans With Apex Hooks
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_customize_pricing_procedures_with_apex_hooks.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_plan_framework.htm
fetched_at: 2026-09-07
---

# Customize Your Procedure Plans With Apex Hooks

To support unique pricing scenarios, add custom Apex logic to your pricing procedure plans. You can use Apex hooks to apply custom business logic that modifies the pricing context after a quote line is configured. Use an Apex prehook to adjust pricing based on product attributes before it's priced, and an Apex posthook to handle pricing changes for groups and other Quote object elements after pricing. When a sales rep configures a product or changes a group of quote line items, the pricing procedure plan changes the pricing based on the instructions in Apex.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER
PERMISSIONS NEEDED
To create, update, and delete pricing procedures and procedure plans:	Salesforce Pricing Design Time User or Procedure Plan Access
To use pricing procedures:	Salesforce Pricing Run Time User
To define, edit, delete, set security, and set version settings for Apex classes:	Author Apex
IMPORTANT
When using the Revenue Management (formerly Revenue Cloud) process type, any Apex logic you add must be the first or last element in the Procedure Plan execution sequence.
External callouts from an Apex hook are supported only when the Place Sales Transaction request is triggered through the Salesforce user interface or Place Sales Transaction API. They aren’t supported when the request is triggered from Apex or Flow.
External callouts in Apex hooks aren’t supported when Double Persist mode is enabled. For additional guidance, contact Salesforce Customer Support.
External callouts in Apex hooks can affect performance. So, predictable Service Level Objectives (SLOs) can’t be guaranteed.
Apex hooks run within Apex governor limits. Querying and storing transaction data in Apex variables can increase heap usage and may result in heap size errors depending on the amount of data processed during execution. To avoid errors, retrieve only the data that your pricing logic requires.
Data Manipulation Language (DML) operations aren’t supported in Apex hooks for procedure plans because they can result in a stale transaction context. To know more about DML operations, see Apex DML Operations.
Ensure Procedure Plan Orchestration for Pricing is turned on.
From Setup, in the Quick Find box, enter Revenue Settings, then select Revenue Settings.
Find and if necessary enable the setting Procedure Plan Orchestration for Pricing.
Leave the setting Exclude Default and Sales Transaction Type Pricing Procedures disabled.
Define classes for the Apex hooks to add to your pricing procedures.
From Setup, in the Quick Find box, enter Apex, then select Apex Classes.
Select New to create a new Apex class.
In the class editor, enter the class definition.

For example, this prehook (ApexDmAttributePreHook) updates the values of dynamic attributes with the name Display_Size based on their display size. More sample classes are shown in Sample Classes for Apex Pricing Hooks at the end of these steps.

global class ApexDmlAttributePreHook implements RevSignaling.SignalingApexProcessor {

    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing PREHOOK');
        
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        // STEP 1 - Query SalesTransactionItemAttribute and extract Display_Size values
        Map<String, Object> inputQueryItemAttr = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItemAttribute' }
        };
        Map<String, Object> itemAttrQueryOutput = industriesContext.queryTags(inputQueryItemAttr);
        Map<String, Object> itemAttrQueryResult = (Map<String, Object>) itemAttrQueryOutput.get('queryResult');
        List<Object> itemAttrData = (List<Object>) itemAttrQueryResult.get('SalesTransactionItemAttribute');

        Map<String, Decimal> parentCtxIdToDisplaySize = new Map<String, Decimal>();

        for (Object attrObj : itemAttrData) {
            Map<String, Object> attrNode = (Map<String, Object>) attrObj;
            Map<String, Object> tagMap = (Map<String, Object>) attrNode.get('tagValue');

            String attributeName = null;
            String attributeValueStr = null;
            String parentCtxId = null;

            if (tagMap.containsKey('Attribute')) {
                attributeName = (String)((Map<String, Object>) tagMap.get('Attribute')).get('tagValue');
            }
            if (tagMap.containsKey('AttributeValue')) {
                attributeValueStr = (String)((Map<String, Object>) tagMap.get('AttributeValue')).get('tagValue');
            }
            if (tagMap.containsKey('SalesTransactionItemAttrParent')) {
                parentCtxId = (String)((Map<String, Object>) tagMap.get('SalesTransactionItemAttrParent')).get('tagValue');
            }

            if (attributeName == 'Display_Size' && attributeValueStr != null && parentCtxId != null) {
                Decimal sizeValue = Decimal.valueOf(attributeValueStr.split(' ')[0]);
                parentCtxIdToDisplaySize.put(parentCtxId, sizeValue);
                System.debug('DisplaySize=' + sizeValue);
                System.debug('Matched itemCtxId=' + parentCtxId);
            }
        }

        // STEP 2 - Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');

        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();

        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));

            Boolean matched = false;
            for (String ctxKey : parentCtxIdToDisplaySize.keySet()) {
                if (dataPath.contains(ctxKey)) {
                    Decimal newPrice = parentCtxIdToDisplaySize.get(ctxKey);
                    System.debug('DisplaySize match found for item ' + ctxKey);
                    dataPath.remove(0); // Remove contextId

                    itemNodeUpdates.add(new Map<String, Object>{
                        'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                        'attributes' => new List<Object>{
                            new Map<String, Object>{
                                'attributeName' => 'UnitPrice',
                                'attributeValue' => newPrice
                            }
                        }
                    });
                    matched = true;
                    break;
                }
            }

            if (!matched) {
                String itemCtxId = dataPath.size() > 1 ? String.valueOf(dataPath[1]) : 'UNKNOWN';
                System.debug('No DisplaySize match found for item ' + itemCtxId);
            }
        }

        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };

            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        //response.status = RevSignaling.TransactionStatus.FAILED;
        //response.message = 'An error occurred during the processing...';
        return response;
    }
    
}
Save the class definition.
From Setup, in the Quick Find box, enter Procedure Plan, then select Procedure Plan Definitions.
In the Definition Names column, select a procedure plan definition to edit.
From the procedure plan definition, in Procedure Plan Sections, select Add to add a new section.
Select Standard.
Name the section, for example PreApex for an Apex prehook.
In Section Type, select Apex then Save.
Expand the new section.
For Phases, select Pricing and for Resolution Type select Default.
In the Apex selection box that appears, enter the Apex class you defined above, for example ApexDmlAttributePreHook, then select Save.
Add additional prehooks and posthooks as needed.
Select Manage Sections to rearrange prehooks above the Pricing Procedure section and posthooks below it.
Save your changes to the Procedure Plan definition.
EXAMPLE Sample Classes for Apex Pricing Hooks

Prehook: Update the discount percentage to 2% on all lines in the context (for example, quote lines).


global class ApexDmlDiscountUpdatePreHook implements RevSignaling.SignalingApexProcessor {

    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing PREHOOK');
        
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        Integer randomDiscountPercentage = 2;

        // STEP 2 - Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');

        System.debug('QLI itemData=' + itemData);

        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();

        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));

            Boolean matched = false;
            dataPath.remove(0); // Remove contextId

            itemNodeUpdates.add(new Map<String, Object>{
                'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                'attributes' => new List<Object>{
                    new Map<String, Object>{
                        'attributeName' => 'Discount',
                        'attributeValue' => randomDiscountPercentage
                    }
                }
            });
            matched = true;

            if (!matched) {
                String itemCtxId = dataPath.size() > 1 ? String.valueOf(dataPath[1]) : 'UNKNOWN';
                System.debug('No DisplaySize match found for item ' + itemCtxId);
            }
        }

        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };

            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        //response.status = RevSignaling.TransactionStatus.FAILED;
        //response.message = 'An error occurred during the processing...';
        return response;
    }
}

Prehook: Call an external resource to fetch a quantity value.


global class ApexDmlQuantityCalloutPreHook implements RevSignaling.SignalingApexProcessor {

    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing PREHOOK');
        
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        // STEP 1 - External Callout Test
        Integer randomNumber = getRandomNumber();
        System.debug(' Random Number from API: ' + randomNumber);

        // STEP 2 - Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');

        System.debug('QLI itemData=' + itemData);

        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();

        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));

            Boolean matched = false;
            dataPath.remove(0); // Remove contextId
    
            itemNodeUpdates.add(new Map<String, Object>{
                'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                'attributes' => new List<Object>{
                    new Map<String, Object>{
                        'attributeName' => 'Quantity',
                        'attributeValue' => randomNumber
                    }
                }
            });
            matched = true;

            if (!matched) {
                String itemCtxId = dataPath.size() > 1 ? String.valueOf(dataPath[1]) : 'UNKNOWN';
                System.debug('No DisplaySize match found for item ' + itemCtxId);
            }
        }

        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };

            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        //response.status = RevSignaling.TransactionStatus.FAILED;
        //response.message = 'An error occurred during the processing...';
        return response;
    }
    
    // External callout
    private Integer getRandomNumber() {
        String endpoint = 'https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new';
        Http http = new Http();
        HttpRequest req = new HttpRequest();
        req.setEndpoint(endpoint);
        req.setMethod('GET');
        req.setTimeout(5000);

        try {
            HttpResponse res = http.send(req);
            if (res.getStatusCode() == 200) {
                System.debug('Fetched prices from external service');
                return Integer.valueOf(res.getBody().trim());
            } else {
                System.debug(' Callout failed: ' + res.getStatus());
            }
        } catch (Exception ex) {
            System.debug(' Exception during callout: ' + ex.getMessage());
        }
        return 10;
    }
}

Prehook: Trigger an update to the price a product if its Attribute Name is Display and its Attribute Value is 1080p Built-in Display, or if its Attribute Name is Printer and its Attribute Value is Laser.


global class ApexDmlMultiAttributePreHook implements RevSignaling.SignalingApexProcessor {

    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing PREHOOK');
        
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        // STEP 1 - Query SalesTransactionItemAttribute and extract Display_Size values
        Map<String, Object> inputQueryItemAttr = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItemAttribute' }
        };
        Map<String, Object> itemAttrQueryOutput = industriesContext.queryTags(inputQueryItemAttr);
        Map<String, Object> itemAttrQueryResult = (Map<String, Object>) itemAttrQueryOutput.get('queryResult');
        List<Object> itemAttrData = (List<Object>) itemAttrQueryResult.get('SalesTransactionItemAttribute');

        Map<String, Decimal> parentCtxIdToAttribute = new Map<String, Decimal>();

        for (Object attrObj : itemAttrData) {
            Map<String, Object> attrNode = (Map<String, Object>) attrObj;
            Map<String, Object> tagMap = (Map<String, Object>) attrNode.get('tagValue');

            String attributeName = null;
            String attributeValueStr = null;
            String parentCtxId = null;

            System.debug('TagMap ' + tagMap);
            if (tagMap.containsKey('Attribute')) {
                attributeName = (String)((Map<String, Object>) tagMap.get('Attribute')).get('tagValue');
            }
            if (tagMap.containsKey('AttributeValue')) {
                attributeValueStr = (String)((Map<String, Object>) tagMap.get('AttributeValue')).get('tagValue');
            }
            if (tagMap.containsKey('SalesTransactionItemAttrParent')) {
                parentCtxId = (String)((Map<String, Object>) tagMap.get('SalesTransactionItemAttrParent')).get('tagValue');
            }
            
            if (attributeName == 'Display' && attributeValueStr == '1080p Built-in Display' && parentCtxId != null) {
               Decimal defaultDisplayCost = 1000.00;
               parentCtxIdToAttribute.put(parentCtxId, defaultDisplayCost);
               System.debug('Display=' + defaultDisplayCost);
               System.debug('Matched itemCtxId=' + parentCtxId);
            }
            
            if (attributeName == 'Printer' && attributeValueStr == 'Laser' && parentCtxId != null) {
               Decimal defaultLaserPrinterCost = 500.00;
               parentCtxIdToAttribute.put(parentCtxId, defaultLaserPrinterCost);
               System.debug('Printer=' + defaultLaserPrinterCost);
               System.debug('Matched itemCtxId=' + parentCtxId);
            }
        }

        // STEP 2 - Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');

        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();

        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));

            Boolean matched = false;
            for (String ctxKey : parentCtxIdToAttribute.keySet()) {
                if (dataPath.contains(ctxKey)) {
                    Decimal newPrice = parentCtxIdToAttribute.get(ctxKey);
                    System.debug('Attribute match found for item ' + ctxKey);
                    System.debug('Attribue with new price ' + newPrice);
                    dataPath.remove(0); // Remove contextId

                    itemNodeUpdates.add(new Map<String, Object>{
                        'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                        'attributes' => new List<Object>{
                            new Map<String, Object>{
                                'attributeName' => 'UnitPrice',
                                'attributeValue' => newPrice
                            }
                        }
                    });
                    matched = true;
                    break;
                }
            }

            if (!matched) {
                String itemCtxId = dataPath.size() > 1 ? String.valueOf(dataPath[1]) : 'UNKNOWN';
                System.debug('No DisplaySize match found for item ' + itemCtxId);
            }
        }

        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };

            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        //response.status = RevSignaling.TransactionStatus.FAILED;
        //response.message = 'An error occurred during the processing...';
        return response;
    }
    
}



Prehook: Apply a random discount percentage for all lines in the context.


global class ApexDmlRandomDiscountPreHook implements RevSignaling.SignalingApexProcessor {

    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing PREHOOK');
        
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        Integer randomDiscountPercentage = getRandomNumber();

        // STEP 2 - Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');

        System.debug('QLI itemData=' + itemData);

        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();

        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));

            Boolean matched = false;
            dataPath.remove(0); // Remove contextId

            itemNodeUpdates.add(new Map<String, Object>{
                'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                'attributes' => new List<Object>{
                    new Map<String, Object>{
                        'attributeName' => 'Discount',
                        'attributeValue' => randomDiscountPercentage
                    }
                }
            });
            matched = true;

            if (!matched) {
                String itemCtxId = dataPath.size() > 1 ? String.valueOf(dataPath[1]) : 'UNKNOWN';
                System.debug('No DisplaySize match found for item ' + itemCtxId);
            }
        }

        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };

            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        //response.status = RevSignaling.TransactionStatus.FAILED;
        //response.message = 'An error occurred during the processing...';
        return response;
    }
        // External callout
    public static Integer getRandomNumber() {
        String endpoint = 'https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new';
        Http http = new Http();
        HttpRequest req = new HttpRequest();
        req.setEndpoint(endpoint);
        req.setMethod('GET');
        req.setTimeout(5000);

        try {
            HttpResponse res = http.send(req);
            if (res.getStatusCode() == 200) {
                System.debug('Fetched prices from external service');
                return Integer.valueOf(res.getBody().trim());
            } else {
                System.debug(' Callout failed: ' + res.getStatus());
            }
        } catch (Exception ex) {
            System.debug(' Exception during callout: ' + ex.getMessage());
        }
        return 10;
    }

}

Prehook: Update a dynamic attribute value with random value from a callout to an external resource.


global class ApexDmlAttributeExternalCalloutPreHook implements RevSignaling.SignalingApexProcessor {

    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing PREHOOK');
        
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        // STEP 1 - Query SalesTransactionItemAttribute and extract Display_Size values
        Map<String, Object> inputQueryItemAttr = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItemAttribute' }
        };
        Map<String, Object> itemAttrQueryOutput = industriesContext.queryTags(inputQueryItemAttr);
        Map<String, Object> itemAttrQueryResult = (Map<String, Object>) itemAttrQueryOutput.get('queryResult');
        List<Object> itemAttrData = (List<Object>) itemAttrQueryResult.get('SalesTransactionItemAttribute');

        Map<String, Decimal> parentCtxIdToDisplaySize = new Map<String, Decimal>();

        for (Object attrObj : itemAttrData) {
            Map<String, Object> attrNode = (Map<String, Object>) attrObj;
            Map<String, Object> tagMap = (Map<String, Object>) attrNode.get('tagValue');

            String attributeName = null;
            String attributeValueStr = null;
            String parentCtxId = null;

            if (tagMap.containsKey('Attribute')) {
                attributeName = (String)((Map<String, Object>) tagMap.get('Attribute')).get('tagValue');
            }
            if (tagMap.containsKey('AttributeValue')) {
                attributeValueStr = (String)((Map<String, Object>) tagMap.get('AttributeValue')).get('tagValue');
            }
            if (tagMap.containsKey('SalesTransactionItemAttrParent')) {
                parentCtxId = (String)((Map<String, Object>) tagMap.get('SalesTransactionItemAttrParent')).get('tagValue');
            }

            if (attributeName == 'Display_Size' && attributeValueStr != null && parentCtxId != null) {
                Decimal sizeValue = getRandomNumber();
                parentCtxIdToDisplaySize.put(parentCtxId, sizeValue);
                System.debug('DisplaySize=' + sizeValue);
                System.debug('Matched itemCtxId=' + parentCtxId);
            }
        }

        // STEP 2 - Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');

        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();

        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));

            Boolean matched = false;
            for (String ctxKey : parentCtxIdToDisplaySize.keySet()) {
                if (dataPath.contains(ctxKey)) {
                    Decimal newPrice = parentCtxIdToDisplaySize.get(ctxKey);
                    System.debug('DisplaySize match found for item ' + ctxKey);
                    dataPath.remove(0); // Remove contextId

                    itemNodeUpdates.add(new Map<String, Object>{
                        'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                        'attributes' => new List<Object>{
                            new Map<String, Object>{
                                'attributeName' => 'UnitPrice',
                                'attributeValue' => newPrice
                            }
                        }
                    });
                    matched = true;
                    break;
                }
            }

            if (!matched) {
                String itemCtxId = dataPath.size() > 1 ? String.valueOf(dataPath[1]) : 'UNKNOWN';
                System.debug('No DisplaySize match found for item ' + itemCtxId);
            }
        }

        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };

            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        //response.status = RevSignaling.TransactionStatus.FAILED;
        //response.message = 'An error occurred during the processing...';
        return response;
    }
    
        // External callout
    private Integer getRandomNumber() {
        String endpoint = 'https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new';
        Http http = new Http();
        HttpRequest req = new HttpRequest();
        req.setEndpoint(endpoint);
        req.setMethod('GET');
        req.setTimeout(5000);

        try {
            HttpResponse res = http.send(req);
            if (res.getStatusCode() == 200) {
                System.debug('Fetched prices from external service');
                return Integer.valueOf(res.getBody().trim());
            } else {
                System.debug(' Callout failed: ' + res.getStatus());
            }
        } catch (Exception ex) {
            System.debug(' Exception during callout: ' + ex.getMessage());
        }
        return 10;
    }
}

Posthook: Update the description of each line in the context.


global class ApexDmlDescriptionPostHook implements RevSignaling.SignalingApexProcessor {

    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing POSTHOOK');
        
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        String randomDescription = 'via Post Apex Pricing Hook';

        // STEP 2 - Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');

        System.debug('QLI itemData=' + itemData);

        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();

        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));

            Boolean matched = false;
            dataPath.remove(0); // Remove contextId

            itemNodeUpdates.add(new Map<String, Object>{
                'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                'attributes' => new List<Object>{
                    new Map<String, Object>{
                        'attributeName' => 'SalesTrxnItemDescription',
                        'attributeValue' => randomDescription
                    }
                }
            });
            matched = true;

            if (!matched) {
                String itemCtxId = dataPath.size() > 1 ? String.valueOf(dataPath[1]) : 'UNKNOWN';
                System.debug('No DisplaySize match found for item ' + itemCtxId);
            }
        }

        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };

            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        //response.status = RevSignaling.TransactionStatus.FAILED;
        //response.message = 'An error occurred during the processing...';
        return response;
    }
}

Preehook: Invoke Apex pricing hook from a test class

@isTest
private class ApexDmlAttributePreHookTest {
    @isTest
    static void testExecute() {
        // Build or mock the context manually
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();

        Map<String, Object> input = new Map<String, Object>();
        Map<String, String> metadata = new Map<String, String>();
        metadata.put('contextDefinitionId', '<Your_Actual_ContextDefinitionId>');
        metadata.put('mappingId', '<Your_Actual_MappingId>');

        // Create sample data (for example, a quote or related records)
       // Replace id with your Quote ID
      // If you are testing an order, replace the businessObjectType with Order
        String data = '{\'Quote\':[{' +
                      '\'id\':\'0Q0xx000003GYK0AAO\',' +
                      '\'businessObjectType\':\'Quote\'}]}';
        input.put('data', data);
        input.put('metadata', metadata);

        Map<String, Object> context = industriesContext.buildContext(input);
        String contextId = (String) context.get('contextId');

        RevSignaling.ProcedurePlan dummyPlan = new RevSignaling.ProcedurePlan();
        RevSignaling.TransactionRequest request = new RevSignaling.TransactionRequest(dummyPlan, contextId);

        Test.startTest();
        // Instantiate and execute your Apex hook class
        ApexDmlAttributePreHook processor = new ApexDmlAttributePreHook();
        RevSignaling.TransactionResponse response = processor.execute(request);

        Test.stopTest();

        System.assertEquals(RevSignaling.TransactionStatus.SUCCESS, response.status);
    }
}

global class ApexDmlAttributePreHook implements RevSignaling.SignalingApexProcessor {

    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();

        Map<String, Object> inputQuery = new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        };

        Map<String, Object> result = industriesContext.queryTags(inputQuery);
        System.debug('result==' + result);

        // Add your prehook logic here
        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        response.message = 'Prehook executed';
        return response;
    }
}


Preehook: Refactor Apex hook using an interface


// STEP 1 - Define a wrapper interface
public interface IndustriesContextInterface {
    Map<String, Object> queryTags(Map<String, Object> input);
    void updateContextAttributes(Map<String, Object> input);
}

//STEP 2 - Wrap the real IndustriesContext class
public class RealIndustriesContext implements IndustriesContextInterface {
    Context.IndustriesContext realCtx = new Context.IndustriesContext();

    public Map<String, Object> queryTags(Map<String, Object> input) {
        return realCtx.queryTags(input);
    }

    public void updateContextAttributes(Map<String, Object> input) {
        realCtx.updateContextAttributes(input);
    }
}

//STEP 3 - Inject the interface into the refactored Apex hook
global class ApexDmlAttributePreHook_Refactored implements RevSignaling.SignalingApexProcessor {
    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}

    private IndustriesContextInterface industriesContext;

    public ApexDmlAttributePreHook_Refactored() {
        this(new RealIndustriesContext());
    }

    public ApexDmlAttributePreHook_Refactored(IndustriesContextInterface ctx) {
        this.industriesContext = ctx;
    }

    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing PREHOOK');
        String contextId = request.ctxInstanceId;

        // Query attributes
        Map<String, Object> itemAttrQueryOutput = industriesContext.queryTags(new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItemAttribute' }
        });

        Map<String, Object> itemAttrQueryResult = (Map<String, Object>) itemAttrQueryOutput.get('queryResult');
        List<Object> itemAttrData = (List<Object>) itemAttrQueryResult.get('SalesTransactionItemAttribute');

        Map<String, Decimal> parentCtxIdToDisplaySize = new Map<String, Decimal>();

        for (Object attrObj : itemAttrData) {
            Map<String, Object> tagMap = (Map<String, Object>) ((Map<String, Object>) attrObj).get('tagValue');
            if (tagMap.get('Attribute') != null && tagMap.get('AttributeValue') != null && tagMap.get('SalesTransactionItemAttrParent') != null) {
                String name = (String)((Map<String, Object>) tagMap.get('Attribute')).get('tagValue');
                if (name == 'Display_Size') {
                    String valStr = (String)((Map<String, Object>) tagMap.get('AttributeValue')).get('tagValue');
                    String parentCtxId = (String)((Map<String, Object>) tagMap.get('SalesTransactionItemAttrParent')).get('tagValue');
                    Decimal displaySize = Decimal.valueOf(valStr.split(' ')[0]);
                    parentCtxIdToDisplaySize.put(parentCtxId, displaySize);
                }
            }
        }

        // Query line items
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(new Map<String, Object>{
            'contextId' => contextId,
            'tags' => new List<String>{ 'SalesTransactionItem' }
        });

        Map<String, Object> itemQueryResult = (Map<String, Object>) itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');

        List<Map<String, Object>> updates = new List<Map<String, Object>>();
        for (Object itemObj : itemData) {
            Map<String, Object> node = (Map<String, Object>) itemObj;
            List<Object> path = (List<Object>) node.get('dataPath');

            for (String ctxId : parentCtxIdToDisplaySize.keySet()) {
                if (path.contains(ctxId)) {
                    path.remove(0);
                    updates.add(new Map<String, Object>{
                        'nodePath' => new Map<String, Object>{ 'dataPath' => path },
                        'attributes' => new List<Object>{
                            new Map<String, Object>{
                                'attributeName' => 'UnitPrice',
                                'attributeValue' => parentCtxIdToDisplaySize.get(ctxId)
                            }
                        }
                    });
                    break;
                }
            }
        }

        if (!updates.isEmpty()) {
            industriesContext.updateContextAttributes(new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => updates
            });
        }

        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        response.message = 'Prehook executed';
        return response;
    }
}

//STEP 4 - Create a mock implementation for testing
@IsTest
public class MockIndustriesContext implements IndustriesContextInterface {

    public Map<String, Object> queryTags(Map<String, Object> input) {
        String tag = ((List<String>)input.get('tags'))[0];
        Map<String, Object> result = new Map<String, Object>();

        if (tag == 'SalesTransactionItemAttribute') {
            List<Object> attributes = new List<Object>();
            attributes.add(new Map<String, Object>{
                'tagValue' => new Map<String, Object>{
                    'Attribute' => new Map<String, Object>{ 'tagValue' => 'Display_Size' },
                    'AttributeValue' => new Map<String, Object>{ 'tagValue' => '14.5 Inches' },
                    'SalesTransactionItemAttrParent' => new Map<String, Object>{ 'tagValue' => 'itemCtx123' }
                }
            });
            result.put('SalesTransactionItemAttribute', attributes);
        }
        else if (tag == 'SalesTransactionItem') {
            List<Object> items = new List<Object>();
            items.add(new Map<String, Object>{
                'dataPath' => new List<Object>{ 'ctxId123', 'itemCtx123' }
            });
            result.put('SalesTransactionItem', items);
        }

        return new Map<String, Object>{ 'queryResult' => result };
    }

    public void updateContextAttributes(Map<String, Object> input) {
        System.debug('Mock updateContextAttributes called with: ' + JSON.serializePretty(input));
        // Optionally add asserts to verify this input during test execution
    }
}

//STEP 5 - Write the test class
@IsTest
private class ApexDmlAttributePreHookTest_Refactored {

    @IsTest
    static void testExecute_withValidDisplaySize() {
        IndustriesContextInterface mockCtx = new MockIndustriesContext();
        ApexDmlAttributePreHook_Refactored hook = new ApexDmlAttributePreHook_Refactored(mockCtx);

        // Build a test context
        Context.IndustriesContext industriesContexts = new Context.IndustriesContext();
        Map<String, Object> input = new Map<String, Object>();
        Map<String, String> metadata = new Map<String, String>();
        metadata.put('contextDefinitionId', '<Replace with ContextDefinitionId>');
        metadata.put('mappingId','Replace with MappingId');

        String data = '{\'Quote\':[{\'id\':\'0Q0xx000003GYK0AAO\',\'businessObjectType\':\'Quote\'}]}';
        input.put('data', data);
        input.put('metadata', metadata);

        Map<String, Object> context = industriesContexts.buildContext(input);
        System.debug(context.get('contextId'));

        RevSignaling.ProcedurePlan dummyPlan = new RevSignaling.ProcedurePlan();
        RevSignaling.TransactionRequest request = new RevSignaling.TransactionRequest(dummyPlan, context);

        RevSignaling.TransactionResponse response = hook.execute(request);

        System.debug('response==' + response);
        System.assertEquals(RevSignaling.TransactionStatus.SUCCESS, response.status);
    }
}
Configure Apex Hooks in a Product Discovery Procedure Plan
Use Apex sections in a Product Discovery procedure plan to run custom pricing logic, such as fetching prices from an external system. The order of Apex and Pricing sections determines how prices are applied. You can include multiple Pricing and Apex sections, but only one Qualification section.
Sample: Apex Class for Product Discovery External Pricing
Use this sample Apex implementation to update product prices in a Product Discovery procedure plan. The class demonstrates how to query pricing data, fetch external values, and update the transaction response when using Apex hooks.
Example: Use Apex Hooks to Extend Pricing Logic
See how Apex hooks interact with Pricing sections when configured as pre- or post-hooks in a Product Discovery procedure plan.
Best Practices for Apex Pricing Hooks
Follow these best practices when implementing Apex hooks in your pricing procedure plans to optimize performance and avoid unexpected results.

=== ARTICLE: ind.pricing_decision_explainer_salesforce_pricing.htm ===
---
article_id: ind.pricing_decision_explainer_salesforce_pricing.htm
title: Decision Explainer for Salesforce Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_decision_explainer_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Decision Explainer for Salesforce Pricing

Use Decision Explainer to customize the Salesforce Pricing waterfall structure and generate dynamic explanations for the resulting pricing outcomes.

Decision Explainer is a service that provides insights into why a pricing procedure generated a specific result. For example, it can explain to your user why the final price of the list of items that they purchased seems higher than expected. With Decision Explainer, the pricing analyst can check the discounts applied for the items and the break-up of discounts to give your user the reason for their final charges.

Salesforce Pricing sends default success or failure messages that come with the solution, but doesn’t ship predefined decision explainer messages. To create a custom message, you must first create a message token, then a template for your message, and finally, map it to the appropriate context tag or resource.

NOTE Decision Explainer is compatible with all pricing elements that appear in the price waterfall.

To learn more, see Decision Explainer.

Configure Decision Explainer for Price Waterfall
Map expression set message tokens and explainability message templates to pricing elements to customize the decision explanations in the price waterfall.

=== ARTICLE: ind.pricing_define_costs_in_cost_books.htm ===
---
article_id: ind.pricing_define_costs_in_cost_books.htm
title: Define Costs in Cost Books
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_define_costs_in_cost_books.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_books_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Define Costs in Cost Books

A cost book acts as a detailed expense tracker for your products. Think of it as the place where you record every cost associated with creating or delivering a product or service. Within a cost book, you create individual entries for each specific expense, such as the cost of raw materials, manufacturing, or shipping. These detailed cost entries are then linked directly to the corresponding product in your catalog, giving you a clear, itemized view of what it truly costs to bring that item to market.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create and manage cost books:	Salesforce Pricing Design Time User

This cost information is the foundation for building a smart and profitable pricing strategy. Once you know the true cost of a product, you can move beyond guesswork and set selling prices that ensure a healthy profit margin or markup. This allows you to accurately analyze the profitability of each item you sell, helping you make informed decisions on everything from sales promotions to product development, and ultimately ensuring your business remains profitable.

IMPORTANT Cost book entries record product costs for tracking purposes only. You can't use this cost data on quotes or orders. Salesforce Pricing doesn't pull cost book entries into quote lines, and doesn't calculate margins or markups from them. Additionally, you can't reference cost book data directly in pricing procedures.
Create a Cost Book
From App Launcher, find and select Price Management.
From the app navigation menu, select Cost Books.
On the Cost Books page, click New.
Give your cost book a name.
Set a date range to determine the cost book’s validity.
Optionally, you can designate a cost book as the default.
Save your changes.
Add Cost Book Entries

A cost book entry is each cost factor that is tracked as a product with the cost price.

From App Launcher, find and select Price Management.
From the app navigation menu, select Cost Books, and then select a cost book.
Under the Related tab, under Cost Book Entry, click New.
Search for and select a product.
Each cost factor is stored as a product record.
Enter the cost of the product.
Specify the cost currency.
Set the date range.
If necessary, enter a description.
Save your changes.
NOTE The cost book details are populated when you create the cost book entry from the cost book record. If you directly navigate to the Cost Book Entry page, you must associate the cost book entry with a cost book.

=== ARTICLE: ind.pricing_define_price_impacting_attributes.htm ===
---
article_id: ind.pricing_define_price_impacting_attributes.htm
title: Set Price Impacting Attributes for Products
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_define_price_impacting_attributes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_attribute_based_price_element.htm
fetched_at: 2026-09-07
---

# Set Price Impacting Attributes for Products

Simplify the selling experience for your sales reps using price-impacting attributes when selling your product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create price impacting attributes:	

Salesforce Pricing Design Time

OR

Salesforce Pricing Run Time

Instead of manually calculating discounts or navigating complex product catalogs, sales reps can simply select desired product characteristics like color, size, or material. The price automatically updates in real-time, even applying specific discounts—for example, a 10% markdown for a red mobile phone.

This dynamic pricing capability significantly reduces quoting errors because sales reps can quickly configure precise product pricing and instantly determine the final price.

Before implementing attribute-based pricing, you must define attributes for your products and designate at least one product attribute as price-impacting.

IMPORTANT To create a valid attribute-based pricing rule, verify that the attribute is active and has Is Price Impacting selected.

To learn how to set attributes for products, see Create Product Attributes in Revenue Management.

From App Launcher, find and select Price Management.
From the app navigation menu, select Products.
Select a product from the list. If you don’t see products on this page, change the list view to show All Products.
On the Related tab, under Overridden Inherited Attributes, select an attribute.
If the desired attribute isn't available under Overridden Inherited Attributes, from the dropdown menu on the right of the Inherited Attributes section next to the desired attribute, select Configure.
The attribute moves to the Overridden Inherited Attributes list.
On the Product Attribute Definition page, edit and select the Is Price Impacting option.

=== ARTICLE: ind.pricing_define_prices_in_price_books.htm ===
---
article_id: ind.pricing_define_prices_in_price_books.htm
title: Define Prices in Price Books
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_define_prices_in_price_books.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_books_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Define Prices in Price Books

A price book is essentially your company's master product catalog, containing a complete list of your products and services along with their specific selling prices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create and manage cost books:	Salesforce Pricing Design Time User

The main purpose of a price book is to ensure your sales team can provide consistent and accurate pricing for every customer. Businesses can maintain a standard, company-wide price book or create multiple, custom price books for different currencies, regions, or customer segments, giving them full control over their pricing strategy.

Price books work by directly connecting your products to your sales deals. When a sales representative creates a quote for a customer, they first select the appropriate price book. Then, as they add products to the deal, the correct price for each item is automatically pulled from the selected book. This simple connection streamlines the entire sales process, ensuring quotes are accurate and making it much easier to manage prices and forecast future revenue.

To ensure accurate pricing when creating a quote with bundled products, make sure all products in the bundle belong to the same price book.

Optional: Configure Price Book Page Layout

If you want to associate your price book to a cost book, you’ll need to configure your page layout to show the cost book entry field.

From the Object manager, search for and select the Price Book object.
Select Page Layouts, and then click Price Book Layout.
In the palette, click Fields.
Drag and drop the Cost Book field to the Price Book’s page layout.
Save your changes.
Create a Price Book

All Salesforce orgs include a predefined Standard Price Book. However, you can create and activate any number of custom price books based on your business needs. Once active, sales reps can select them when adding products to opportunities.

From App Launcher, find and select Price Management.
From the app navigation menu, select Price Books.
On the Price Books page, click New.
Give your price book a name.
If necessary, specify these details:
Provide a description.
Set a date range to determine the price book’s validity.
Set the price book as active.
Optionally, associate your price book with a cost book.
Save your changes.
Add Price Book Entries

A price book entry is the record of a product or service and its list price within a specific price book.

IMPORTANT You can’t change the product selling model after you associate it with a price book entry. If you migrate to Revenue Management and want to update an existing price book entry, ask your Salesforce admin to raise a support ticket.
From App Launcher, find and select Price Management.
From the app navigation menu, select Price Books, and then select a price book.
Click the Price Book Entries tab.
Click New.
Specify these details.
Search for and select a product.
Search for and select a price book.
Enter a list price for your product.
If necessary, select the product selling model.
Save your changes.

=== ARTICLE: ind.pricing_derived_price.htm ===
---
article_id: ind.pricing_derived_price.htm
title: Implement Derived Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_derived_price.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_unique_pricing_scenarios.htm
fetched_at: 2026-09-07
---

# Implement Derived Pricing

To accurately calculate a product’s price from another pricing source, such as a product or an asset, or the overall quote value, use the Derived Price feature.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Derived pricing functions by establishing clear relationships between a derived product (the product whose price is being calculated) and a source for that calculation. This source can be a source product (providing the basis for the calculation) or even the aggregate value of the entire transaction.

Before you begin implementing derived pricing, it's crucial to understand these key concepts:

The Pricing Source indicates where the pricing information originates.

PRICING SOURCE	DESCRIPTION
Product	The price is derived from one or more specific products within a transaction.
Header	The price is derived from the total cost of all products in the transaction cart.

The Pricing Scope determines the method by which the derived price is calculated, and your choice depends on the selected pricing source.

PRICING SCOPE	DESCRIPTION
Transactional	The price is derived from one or more specific products within a transaction.
Non-transactional	The price is derived from the total cost of all products in the transaction cart.
Both	Allows for a combination of both transactional and non-transactional scopes.

By setting up your derived products and defining specific pricing rules and formulas, the system automatically determines their price when added to a quote or order. This eliminates manual calculations, reduces errors, and allows for flexible, automated pricing that adapts to various business needs.

Prerequisites to Build Discovery and Derived Price Pricing Procedures
Before you begin creating discovery procedures to locate pricing data for your products and assets, or to calculate a product’s derived price, ensure you have completed the following prerequisites. A fundamental understanding of these concepts is crucial for the successful implementation and operation of your pricing strategies.
Discover Pricing Factors
To accurately calculate a product's derived price, discovery procedures gather contributing factors and store them within a defined context definition, ensuring precise data access.
Calculate the Derived Price of Product
Use the discovery procedure and the derived price element in a pricing procedure, to calculate a product’s price from another product or asset.

=== ARTICLE: ind.pricing_determine_the_best_price_using_a_pricing_procedure.htm ===
---
article_id: ind.pricing_determine_the_best_price_using_a_pricing_procedure.htm
title: Determine the Best Price for a Product Using Pricing Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_determine_the_best_price_using_a_pricing_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_output_resolution.htm
fetched_at: 2026-09-07
---

# Determine the Best Price for a Product Using Pricing Procedures

Use a pricing procedure to determine the best price for a product using a resolution strategy when multiple pricing options exist.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Example: Calculate the Lowest Price of a Product
Let’s determine the lowest price of a product using the List Price element.
Example: Apply Discounts Sequentially for a Product
In this scenario, let's apply discounts to the laptop sequentially. The first discount is calculated from the list price, and each subsequent discount is applied to the previously discounted price.

=== ARTICLE: ind.pricing_discount_distribution_service_limits.htm ===
---
article_id: ind.pricing_discount_distribution_service_limits.htm
title: Discount Distribution Service Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_discount_distribution_service_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_discount_spread_service.htm
fetched_at: 2026-09-07
---

# Discount Distribution Service Limits

Before adding the Discount Distribution Service element to your pricing procedure, keep these points in mind:

You can't apply discount distribution to a pricing procedure that was used to calculate a product's derived price.
While Proration and Subscription elements update the LineItemSubTotal variable by multiplying the ProrationMultiplier with the NetUnitPrice tag, the Discount Distribution Service only utilizes the NetUnitPrice variable for its pricing calculations. If you intend to use the total subscription price, use a Formula element and provide the formula -Proration Multiplier * NetUnitPrice. Then, use the output of this formula as the InputPrice variable for calculations within the Discount Distribution Service element.
The Discount Distribution Service element must be the last element in the pricing procedure.
Use the Discount Distribution Service element only once per pricing procedure.

=== ARTICLE: ind.pricing_discount_spread_service.htm ===
---
article_id: ind.pricing_discount_spread_service.htm
title: Discount Distribution Service
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_discount_spread_service.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_unique_pricing_scenarios.htm
fetched_at: 2026-09-07
---

# Discount Distribution Service

Apply quote-level discounts across each line item ensuring consistent and accurate pricing using the Discount Distribution Service feature in Revenue Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

During certain sales deals, sellers want to apply discretionary discounts at the quote total level, also known as header level. When these discounts are applied to the header by a sales rep, the individual line items within the quote or quote line group must be adjusted as well to ensure accounting accuracy and facilitate reconciliation. The Discount Distribution Service ensures that these discounts are applied correctly across qualifying line items.

Additionally, you can set floor price limits to safeguard profit margins and even exclude certain products or categories from discount distributions, giving you precise control over your discounting strategy.

What is Floor Price Limit?

Floor price limits represent the minimum prices a business establishes for its products, effectively preventing any discounts or price reductions from being applied below this pre-defined threshold.

This safeguards profit margins and maintains pricing integrity. These limits apply when the discount distribution is set to Net Unit Price, and any unapplied discount amounts are tracked in the Total Remainder Amount.

You can implement these limits by either including them in your context definition or creating a custom object for them and hydrating it with a Context Service. Both methods ensure that even with discretionary discounts, your profitability is protected.

EXAMPLE If the floor price limit for a mobile phone is $500 USD and a discount reduces the price to $400, the service preserves the floor price limit of $500. The remaining amount is applied to the next eligible line item. If no line items are available, any remaining amount is saved in the Total Remainder Amount tag.
Discount Distribution Service Limits

Before adding the Discount Distribution Service element to your pricing procedure, keep the following points in mind.

The Discount Distribution Service element must be the last element in the pricing procedure.
The element can only be used once within a single pricing procedure.
You can’t apply discount distribution to a pricing procedure that was used to calculate a product's derived price.
Floor price limits are only applied when the distribution type is set to the NetUnitPrice variable.
Amend and renew processes don’t account for intended price values, as they assume that (NetUnitPrice * Quantity = ItemNetTotal). In the Discount Distribution Service element, when a discount is applied to ItemNetTotal, the NetUnitPrice isn't recalculated; it’s intended as a one-time discount.
While Proration and Subscription elements update the LineItemSubTotal variable by multiplying the ProrationMultiplier with the NetUnitPrice tag, the Discount Distribution Service only utilizes the NetUnitPrice variable for its pricing calculations.
If you intend to use the total subscription price, use a Formula element and provide the formula - Proration Multiplier * NetUnitPrice. Then, use the output of this formula as the InputPrice variable for calculations within the Discount Distribution Service element.
Understand Discount Distribution Service Terms
Familiarize yourself with the variables and terminology you'll encounter when you configure a pricing procedure to calculate discounts using the Discount Distribution Service element.
Use the Discount Distribution Service Element
To calculate discounts that can be spread evenly across all line items or specifically across a subsection of line items, use the Discount Distribution Service element.
Discount Distribution Service Limits
Before adding the Discount Distribution Service element to your pricing procedure, keep these points in mind:

=== ARTICLE: ind.pricing_discover_and_explore.htm ===
---
article_id: ind.pricing_discover_and_explore.htm
title: Begin Using Salesforce Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_discover_and_explore.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Begin Using Salesforce Pricing

Enable Salesforce Pricing to efficiently set up, manage, and implement pricing strategies. Tailor the experience of using Salesforce Pricing for all users using permission sets to give them precise access to what they need.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Turn On Salesforce Pricing
If you haven’t done it yet, enable Salesforce Pricing to give your users access to Salesforce Pricing’s object and features.
Salesforce Pricing Editions, Permission Sets, and Personas
Salesforce Pricing uses permission sets to ensure different user roles have the specific access they need. By assigning the right permission set licenses, organizations can securely manage pricing functionalities, giving each user the necessary access to complete their tasks.

=== ARTICLE: ind.pricing_discovery_procedure_for_pricing.htm ===
---
article_id: ind.pricing_discovery_procedure_for_pricing.htm
title: Discover Pricing Factors
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_discovery_procedure_for_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_derived_price.htm
fetched_at: 2026-09-07
---

# Discover Pricing Factors

To accurately calculate a product's derived price, discovery procedures gather contributing factors and store them within a defined context definition, ensuring precise data access.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Derived pricing often requires specific, disparate data from various sources like products, assets, or quotes. Discovery procedures are essential for finding, collecting, and organizing this vital information into a structured format, making it readily available for the pricing engine.

Understand Discovery Procedure Elements

Every discovery procedure comes with three default elements, each serving a distinct purpose in locating pricing data for products or assets. Configuring a discovery procedure is the crucial first step in calculating a product's derived price.

DISCOVERY ELEMENT	DESCRIPTION
Fetch Pricing Rules	Retrieves derived pricing rules from the Derived Pricing Entries decision table and writes them to the context definition's Contributor node. The Contributor node stores the product IDs, formulas, scope (transactional or non-transactional), and source (header or product) needed to calculate derived prices.
Map Product	Matches contributing products from the fetched pricing rules with products on the current quote or order. If conditions are specified, only matching products are selected. If no conditions are specified, all contributing products present in both the pricing rules and the quote are selected.
Asset Discovery	Used for non-transactional derived pricing calculations. Retrieves pricing data from the customer's existing assets by querying the Asset Action Source Entries V2 decision table for each contributing product's active assets. The calculated prices are stored in the context definition's Contributor node for use in the pricing procedure. Product2Id is automatically passed from the Contributor node populated by Map Product.

Beyond the default elements, you can use the Map Line Item element in your discovery procedure to map tags for individual line item details using parent tags. When doing so, ensure that the Discovery Settings element is placed first, immediately followed by the Map Line Item element. For more information, refer to the Map Line Item section in Map Context Tags in Pricing Procedures.

Configure a Discovery Procedure
To calculate a product's derived price, configure a discovery procedure with the elements required to gather all contributing factors.

=== ARTICLE: ind.pricing_einstein_generative_ai_for_salesforce_pricing.htm ===
---
article_id: ind.pricing_einstein_generative_ai_for_salesforce_pricing.htm
title: Automate Context Tag Mapping with Einstein Generative AI
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_einstein_generative_ai_for_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Automate Context Tag Mapping with Einstein Generative AI

Map context tags with ease and greater accuracy by embedding Einstein generative AI in your pricing elements.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To enable Einstein generative AI:	Customize Application

Optimizing the pricing application setup, especially configuring a pricing procedure, requires a deep understanding of context variables and their tag mapping. Incorrect tags in an element can lead to incorrect pricing calculations. If certain pricing calculations depend on the pricing output from the previous element, incorrect tag mapping can lead to flawed pricing calculations and disrupt business flows.

To help avoid these errors and speed up context tag mapping, Einstein Generate AI can suggest context tags along with confidence scores. You can review and approve the suggestions before they're deployed into your context definitions.

Set Up Einstein Generative AI for Salesforce Pricing
Enable Einstein generative AI and give users the required permissions to access the generative AI capabilities.
Update Context Tags to Pricing Elements with Einstein AI
On a pricing element, get gen AI to suggest and map variables to context tags.

=== ARTICLE: ind.pricing_enable_price_waterfall.htm ===
---
article_id: ind.pricing_enable_price_waterfall.htm
title: Configure Price Waterfall
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_enable_price_waterfall.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_price_waterfall_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Configure Price Waterfall

Understand the reasons behind every step of your pricing process by using Price Waterfall. By configuring waterfall, you get a detailed breakdown of every addition or deduction, giving you clear understanding of your pricing process.

From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
Activate Price Waterfall for API responses.

=== ARTICLE: ind.pricing_ensure_price_transparency_using_the_price_tracking_element.htm ===
---
article_id: ind.pricing_ensure_price_transparency_using_the_price_tracking_element.htm
title: Ensure Price Transparency Using the Price Tracking Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_ensure_price_transparency_using_the_price_tracking_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_tracking_actions.htm
fetched_at: 2026-09-07
---

# Ensure Price Transparency Using the Price Tracking Element

Verify if your product prices are tracked, monitored, and captured using the Price Tracking element.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User

Let's consider a scenario where an e-commerce channel wants to fetch the LaptopPro Bundle’s tracked maximum price from a transaction. You can use the Price Tracking element to fetch the tracked maximum price for the LaptopPro Bundle along with its price book, product selling model, and currency combination. This can then be displayed or used in evaluations.

Configure a pricing procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Manual Discount element and map these variables.
Adjustment Type: AdjustmentType
Adjustment Value: AdjustmentValue
Quantity: LineItemQuantity
Input Unit Price: NetUnitPrice
Add the Price Tracking element.
Under Lookup Table Details, select the Price Book Entries V2 decision table and specify the following details.
Select Get as the Action Type.
Map these input rule variables.
Price Book: PriceBooks
Product: Product
Product Selling Model: ProductSellingModel
Map these output variables.
Saved Min Recorded Price: ItemRecordedPrice
Saved Max Recorded Price: ItemMaxRecordedPrice_std
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your laptop product and click Simulate again.
The price waterfall shows the manual discounts used to calculate the final price of the laptops. However to track the saved recorded price is visible in the JSON format only. 

When a pricing procedure runs or is simulated, every result is saved in the Product Price History Log entity. For each pricing calculation, if the new price is higher than the previously stored maximum price for maximum price tracking, the existing entry in the Product Price History Log entity for that specific product, product selling model, and price book combination is overwritten. This ensures that at the end of each day, only the highest price for a given product and its combination is recorded in the Product Price History Log entity.

The Product Price Range entity then stores this maximum price for a specified duration, specifically for a product, product selling model, and price book combination. This table is the primary source used when fetching price history using the Get or Get & Save actions within the system.

=== ARTICLE: ind.pricing_essentials.htm ===
---
article_id: ind.pricing_essentials.htm
title: Salesforce Pricing Essentials
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_essentials.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.revenue_impl_glossary.htm
fetched_at: 2026-09-07
---

# Salesforce Pricing Essentials

Browse through this collection of terms, key objects, and key concepts. This collection is designed to give Salesforce admins, sales reps, and developers a clear and consistent understanding of pricing concepts and helps them navigate the Salesforce Pricing landscape.

Aggregate Price
Aggregate Price is the pricing element that allows users to combine or aggregate prices based on a specific set of rules for multiple products within a transaction.
Assignment Element
Assignment element is the pricing element used to assign values from one context tag to another based on business needs.
Attribute-Based Adjustment
Attribute-Based Adjustment refers to a definition where a product is eligible for discounts if its attribute values meet certain criteria within a specified time frame. You can define this rule for multiple products.
Attribute-Based Price
Attribute-Based Price is the pricing element where attribute-based discounts are applied to a product if the product meets the eligibility criteria, and calculations are performed accordingly.
Bundle-Based Adjustment
Bundle-Based Adjustment refers to a definition where a product is eligible for discounts if it’s part of a specific bundle within a designated time frame. You can define this rule for multiple products.
Bundle-Based Price
Bundle-Based Price is the pricing element where bundle-based discounts are applied to a product if the product meets the eligibility criteria, and calculations are performed accordingly.
Contract-Based Pricing
Contract-Based Pricing is a pricing element that determines prices based on a specific contract associated with a product in a transactionThis pricing type is applied only when the Use Contract-based Pricing option is enabled for the pricing element.
Cost Book
A cost book is a centralized storage location where a group of products and their base costing details are defined.
Cost Book Entry
A cost book entry defines each product's cost during a specific time frame.
Cumulative Quantity Pricing
Apply Cumulative Pricing to generate discounts for both volume and tier-based quantities of different line items, including historical purchases.
Delta Pricing
Use Delta Pricing to reprice only the modified line items in quotes and orders.
Derived Pricing
Derived Pricing calculates the price of a product based on the prices of another set of products, headers, or historical prices—both transactional and non-transactional—of those products.
Discount Distribution Service
The Discount Distribution Service makes sure that discounts are applied fairly across qualifying line items. You can also set floor price limits to protect profit margins and exclude specific products or categories from discount spreads.
Discovery Pricing Procedure
The Discovery Pricing Procedure is another pricing procedure that determines the set of assets required to derive the pricing of a product. This procedure is primarily intended for derived pricing use cases.
Dynamic Output Mapping
Dynamic Output Mapping is the process of linking a custom decision table to the required Pricing Recipe and mapping its outputs to the appropriate pricing elements for use.
Element Parallelisation
Use Parallel Element Execution to process elements concurrently during the execution of a pricing procedure. This improves the performance of pricing APIs and their simulations.
Enable Compound Uplift
Enable Compound Uplift lets you calculate compounding uplifts for group-ramped lines when a price revision element applies flat and index rate uplifts to non-ramped lines. Each uplift percentage is calculated by compounding the preceding segment's uplift percentage.
Formula Pricing
Formula Pricing is the pricing element that allows users to define a custom pricing formula that they can apply to the prices of specified products. Formulas support arithmetic operators (+, -, *, /), comparison operators (==, !=, <, >, <=, >=), and the IF() function for conditional logic. You can add up to five formulas within a single Formula-Based Pricing element. For more information, see Build Pricing Rules with Formula-Based Pricing. For a complete list of formula functions supported on the Salesforce platform, see All Formula Operators and Functions.
Get List Price
Get List Price is the pricing element where the base price of a product is calculated in the pricing procedure.
List Group
The List Group is part of the pricing procedure where you can establish specific conditions, and define a set of pricing elements based on these rules.
List Price
The List Price is the pricing element that calculates the base price of a product within the pricing procedure.
Local List Variables
Local List Variables are the variables created within a Pricing Procedure and cease to exist after the Pricing Procedure execution completes. Local List Variables support both nodes and attributes.
Manual Discount
Manual Discount refers to the pricing element where any manual adjustments such as percentage, amount, or override, are applied to a product during a specific transaction. This discount is applied at run time and isn't established during the definition phase.
Map Line Items
Map Line Items is a pricing element that maps a parent to a child node in the context definition. It's primarily used to define pricing for the breakdown lines and calculate the sublines in amend, renew, and cancel scenarios.
Pricing Action
Pricing Action is a pricing feature that allows users to define context definitions and pricing procedures to execute any object. You can apply this feature to any Salesforce object in Salesforce for price calculation. Users can create custom context definitions, establish pricing procedures, and use pricing actions to price any item.
Price Adjustment Matrix
The Price Adjustment Matrix is a pricing element that executes ‌custom pricing rules, enabling adjustments to be applied to a specific product.
Price Adjustment Schedule
The Price Adjustment Schedule is a grouping mechanism that users can define adjustments for a specific set of products, categorized based on type Volume, Attribute, Custom, and Bundle. You can also define this group within a specific time frame during which all adjustments can be leveraged.
Price Adjustment Tier
The Price Adjustment Tier defines volume-based adjustments, enabling users to define the adjustment such as Percentage, Amount, Override for a specific quantity range. If the product's quantity falls within this range during a specified time frame, the product becomes eligible for discounts. You can define this rule by using the Price Adjustment Tier.
Price Book
A centralized storage location where a group of products and their base prices are defined.
Price Book Entry
A price book entry defines each product's base price or list price. This price can also be considered the starting price.
Price Revision
The Price Revision element applies an appropriate price revision policy to adjust the price of a product using formulas based on various price adjustments.
Price Revision Policy
Represents the guidelines and methods used to modify product or service prices, often incorporating formulas based on price revision entries and various adjustments.
Procedure Output Resolution
Use Procedure Output Resolution to determine the best price for a product when a pricing rule produces multiple outcomes. The resolution can be applied to list price and price tracking elements.
Pricing Discount Calendar
The Pricing Discount Calendar shows all discounts and adjustments for a product over specific time frames. You can view and edit the details of individual discounts.
Pricing Element
A Pricing Element is a structure within a Pricing Procedure. Each pricing solution is represented as a pricing element that you can drag and drop to address various business use cases.
Pricing Logs Capture
Enable Pricing Logs Capture to capture pricing logs in the Pricing Operations Console for improved debugging.
Pricing Operations Console
The Pricing Operations Console helps your company use price logs to troubleshoot and resolve issues caused by pricing APIs.
Pricing Procedure
A Pricing Procedure is the price orchestration or pricing policy that users can define how to price their products or services. Users can also define custom logic and solutions to implement pricing strategies in any org.
Pricing Propagation
The Propagation element automatically applies discounts, margins, and custom calculations from groups to line items and rolls them up into accurate totals.
Pricing Recipe
A Pricing Recipe is a collection of decision tables used in pricing procedures for pricing calculations.
Pricing Simulation
Pricing Simulation is a feature that users can simulate the orchestration and pricing policy after they set up a Pricing Procedure. By using real data and validating the pricing waterfall, users can determine the expected price and discount for products, as well as validate the procedure.
Price Waterfall
Price Waterfall provides detailed information about the outcome of pricing execution for any transaction. It outlines the step-by-step process of how the products or services are priced and details any discounts or adjustments that the transaction underwent.
Procedure Plan Framework
The Procedure Plan Framework, serves as a one-stop solution where users can define the context for an end-to-end transaction and also define multiple procedures based on Qualification, Pricing, and Asset Discovery rules.
Promotion Execution
The Promotion element evaluates and applies promotion-based discounts to transaction lines during the pricing process.
Propagation table
The Propagation Table is a calculation table used to set up formulas for quote line item and group level fields, define group level aggregates across the nested structure, and define the sequence of execution.
Proration Element
The Proration element determines the proration value of a product for a specific time period and specific terms and term units.
Subscription Pricing
Subscription Pricing is the pricing element that calculates the subscription price of a product by considering the proration value.
Tiered Discount
Tiered Discount is the pricing element where tiered adjustments, also known as slab-based discounts, are calculated for products in the pricing procedure.
Volume Discount
Volume Discount is the pricing element where volume-based adjustments are calculated for products in the pricing procedure.

=== ARTICLE: ind.pricing_example_apply_discounts_sequentially_for_a_product.htm ===
---
article_id: ind.pricing_example_apply_discounts_sequentially_for_a_product.htm
title: "Example: Apply Discounts Sequentially for a Product"
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_example_apply_discounts_sequentially_for_a_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_determine_the_best_price_using_a_pricing_procedure.htm
fetched_at: 2026-09-07
---

# Example: Apply Discounts Sequentially for a Product

In this scenario, let's apply discounts to the laptop sequentially. The first discount is calculated from the list price, and each subsequent discount is applied to the previously discounted price.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create pricing procedures:	Salesforce Pricing Design Time

Implementing this discount involves a few key steps.

Create price adjustment tier records.
Create custom or use existing Salesforce objects to hold your price adjustment data.
Define decision tables, setting criteria (like product, price adjustment tiers) and their adjustments (types and values).
Map these custom decision tables to the org’s pricing recipe.
Create a procedure output resolution record to build a strategy to calculate discounts sequentially.
Use the Price Adjustment Matrix to calculate these discounts.
Create Price Adjustment Tier Records

Since we’re creating a custom decision table using the Price Adjustment Tier Salesforce object to hold your price adjustment data, create a few price adjustment tiers to apply your discounts.

Create a price adjustment tier record.
Specify these details.
Price Adjustment Schedule: Standard Price Adjustment Tier
Product: Laptop
Tier Type: Amount
Tier Value: 100
Lower Bound: 10
Upper Bound: 20
Effective From: 01-03-2025
Product Selling Model: One Time
Click Save & New.
Create another price adjustment tier record with these details.
Price Adjustment Schedule: Standard Price Adjustment Tier
Product: Laptop
Tier Type: Amount
Tier Value: 150
Lower Bound: 21
Upper Bound: 40
Effective From: 01-03-2025
Product Selling Model: One Time
Click Save & New.
Create a third price adjustment tier record with these details.
Price Adjustment Schedule: Standard Price Adjustment Tier
Product: Laptop
Tier Type: Amount
Tier Value: 200
Lower Bound: 41
Effective From: 01-03-2025
Product Selling Model: One Time
Save your changes.
Close the tabs for the new price adjustment tiers that you just created.
On the Details tab, on the Standard Price Adjustment Tier page, select Active.
Save your changes.
Create a Custom Decision Table

Each attribute value on a line item must resolve to a single unique row in the decision table. Salesforce Pricing doesn't support retrieving multiple outputs for the same attribute value. Set up your decision table to map each specific input value to only one discount entry.

From the App Launcher, search for and select Lookup Tables .
Select Decision Table.
Specify these details.
Enter a name and then press Tab to autopopulate the API Name. For our example, we’re calling the decision table, Procedure Output Resolution.
Select Pricing as the application usage.
Select Advanced as the decision table type.
Click Save & Next.
Specify these decision table details.
Source Object: Price Adjustment Tier.
Set the following condition.
Set the source object field as Product2Id and the operator as Equals.
Set another condition for the name.
Set the source object field as Name and the operator as Equals.
Ensure that the Condition Type is set to All conditions are met (AND).
Specify the result details.
Source Object Field: TierValue.
Column Name: TierValue.
Source Object Field: AdjustmentType.
Column Name: AdjustmentType.
Click Save & Next.
Click Save & Next again.
Click Finish.
Activate your decision table.
Configure Lookup Relationships for Multi-Value Attributes

To apply multiple discounts to a single line item, you must establish a relationship between your transaction object and your adjustment data.

From Setup, in the Quick Find box, find and select Object Manager.
From Object Manager, find and select the object holding your adjustment data (e.g., Price Adjustment Tier).
Under Fields & Relationships, create a custom field with the Lookup field type.
Select your primary transaction object (e.g., Quote Line Item) as the reference object. This mapping allows a single line item to associate with multiple adjustment records.
In your Context Definition, create a node to represent the adjustment object.
Complete the Context Mapping to link the fields from your adjustment object to the context attributes.
Map these new context tags to the variables in your Pricing Procedure to allow the engine to retrieve the list of values.
On a record's Related tab, verify that you can associate multiple adjustment records with one line item.
In the Pricing Procedure, click Simulate. The engine should now resolve all associated values for the line item and apply the discounts according to your sequence.
Map the Variables in Your Custom Decision Table
From Setup, in the Quick Find box, find and select Pricing Recipes.
Choose the pricing recipe that you want to modify. For our example, select NGPDefaultRecipe.
On the Price Adjustment Matrix tab, click Modify.
Select the custom decision table created by you. Here, select Procedure Output Resolution.
Map the following variables.
AdjustmentValue: TierValue
AdjustmentType: AdjustmentType
Save your changes.
Create a Procedure Output Resolution Record
From the App Launcher, find and select Price Management.
From the app navigation menu, select Procedure Output Resolution.
Click New.
Specify these details.
Name: Sequential_Pricing
Pricing Element: Price Adjustment Matrix
Resolution Formula: SEQUENCE(TierValue)
Activate your procedure output resolution record.
Save your changes.
Create a Constant for a Resolution Strategy
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
On the Pricing Procedure builder canvas, click .
On the Resource Manager panel, click Add Resource.
In the Add New Resource page, specify these details.
Resource Type: Constant
Resource Name: ResolutionStrategySequence
Data Type: Text
Default Value: Sequential_Pricing. This is the procedure output resolution record that you created in the step above.
Save your changes.
Use the Price Adjustment Matrix Element to Apply Discounts Sequentially
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries V2 decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Price Adjustment Matrix element.
Under Lookup Table Details, select the Procedure Output Resolution decision table. This is the custom decision table that we created.
Select Enable Output Resolution.
Map these variables.
Input Rule Variables
Product: Product
Price Adjustment Tier Name: Contributor
We’ve mapped the Price Adjustment Tier Name variable to a generic tag called Contributor. This field identifies which price adjustment tier schedule the pricing engine should evaluate. If you want to define a custom tag, you can edit your context definition and add a tag and map it accordingly.
Input Variables
Quantity: LineItemQuantity
Input Unit Price: ListPrice
Resolution Variables
Resolution Strategy: ResolutionStrategySequence
Use As List: Price Adjustment Tier Name
IMPORTANT If you want to select multiple rows for a line item, the input rows in the selected decision table should have at least one column with unique values. The value in that column is what we’ll use in tag associated with the Use As List resolution variable.
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter these input values and click Simulate again:
Product: Laptop
Quantity: 15
Product Selling Model: One Time
Contributor: Standard Price Adjustment Tier
The price waterfall shows that the pricing engine has sequentially applied all the discounts associated with different price adjustment tiers for the Laptop product, confirming that your procedure is working as expected.

=== ARTICLE: ind.pricing_example_calculate_the_lowest_price_of_a_product.htm ===
---
article_id: ind.pricing_example_calculate_the_lowest_price_of_a_product.htm
title: "Example: Calculate the Lowest Price of a Product"
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_example_calculate_the_lowest_price_of_a_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_determine_the_best_price_using_a_pricing_procedure.htm
fetched_at: 2026-09-07
---

# Example: Calculate the Lowest Price of a Product

Let’s determine the lowest price of a product using the List Price element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create pricing procedures:	Salesforce Pricing Design Time
Create a Procedure Output Resolution Record
From the App Launcher, find and select Price Management.
From the app navigation menu, select Procedure Output Resolution.
Click New.
Specify these details.
Name: BestPrice
Pricing Element: List Price
Resolution Formula: MIN(ListPrice)
Activate your procedure output resolution record.
Save your changes.
Create a Constant for a Resolution Strategy
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
On the Pricing Procedure builder canvas, click .
On the Resource Manager panel, click Add Resource.
In the Add New Resource page, specify these details.
Resource Type: Constant
Resource Name: ResolutionStrategyMinPrice
Data Type: Text
Default Value: BestPrice. This is the procedure output resolution record that you created in the step above.
Save your changes.
Use the List Price Element to Calculate the Lowest Price
Add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries V2 decision table
Select Enable Output Resolution.
Map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Resolution Variables
Resolution Strategy: ResolutionStrategyMinPrice
Use As List: Price Book
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your laptop product and click Simulate again.
The price waterfall shows that the pricing engine has looked through all the available price books in the org and found the best (minimum) price for the Laptop product, confirming that your procedure is working as expected.

=== ARTICLE: ind.pricing_execute_failed_pricing_batch_jobs.htm ===
---
article_id: ind.pricing_execute_failed_pricing_batch_jobs.htm
title: Fix and Execute Failed Pricing Adjustment Batch Jobs
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_execute_failed_pricing_batch_jobs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_adjustment_batch_jobs.htm
fetched_at: 2026-09-07
---

# Fix and Execute Failed Pricing Adjustment Batch Jobs

You can resolve issues with your failed records by making the necessary edits and running the pricing batch job again. For example, a pricing adjustment batch job may fail when an adjustment relies on a product attribute that is missing or invalid.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To view pricing adjustment batch job logs:	Salesforce Pricing Design Time
From App Laucher, search and select Price Adjustment Batch Jobs.
Open a failed or partially completed pricing adjustment batch job.
In the Related tab, see the list of failed records under Pricing Adjustment Batch Job Log.
TIP To see the entire list of failed or partially completed jobs, select View All under Pricing Adjustment Batch Log. The entire list appears in a new tab, making it easier to filter through the records.
Select  against each record and make your edits.
To execute the pricing adjustment batch job again, select Rerun.

=== ARTICLE: ind.pricing_execute_pricing_elements_in_parallel.htm ===
---
article_id: ind.pricing_execute_pricing_elements_in_parallel.htm
title: Set Up Parallel Pricing Element Execution
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_execute_pricing_elements_in_parallel.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Set Up Parallel Pricing Element Execution

Run multiple pricing procedures concurrently or use parallel processing within a single pricing procedure to ensure faster and more efficient pricing, especially in complex scenarios.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To run pricing elements in parallel:	Salesforce Pricing Design Time

When enabled, all active pricing procedures invoked from Headless or Pricing APIs will undergo parallel execution, meaning independent elements will be processed simultaneously.

NOTE The Map Line Item element doesn't support parallel execution. To use the Map Line Item element in your pricing procedure, disable parallel execution.
From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
Turn on Parallel Execution.
When Parallel Execution is turned on:
The sequence tag value in the waterfall changes, but the order of the execution remains the same.
The elements run in parallel when there are no dependencies, such as when the output of one element is not the input of another.
The list filters run sequentially, but the elements within the list filters run in parallel.

=== ARTICLE: ind.pricing_export_and_import_procedure_plans.htm ===
---
article_id: ind.pricing_export_and_import_procedure_plans.htm
title: Export and Import Procedure Plans
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_export_and_import_procedure_plans.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_plan_framework.htm
fetched_at: 2026-09-07
---

# Export and Import Procedure Plans

Package procedure plans to export and import them across Salesforce orgs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To deploy and use a procedure plan package:	

Procedure Plan Access

AND

Salesforce Pricing Design Time

Key considerations before exporting a procedure plan:

You can't deploy a packaged procedure plan by using an installation URL.
When packaging a Procedure Plan or Pricing Procedure, include only the specific plan or procedure in the package.xml file. Remove all other dependencies from the file to ensure a successful import to the target org.
Second-Generation Packaging isn't supported.
The state of the source Salesforce org takes precedence over the target org.
Before importing the procedure plan, make sure you package, export, and import all dependencies in this order: Context definitions > Decision tables > Pricing procedure.
The minimum API version required is 66.0.
Package a Procedure Plan
From Setup, in the Quick Find box, find and select Package Manager.
Click New.
In the Create a Package window, specify a package name, and, if needed, a description.
Save your changes.
In the Package Detail window, on the Components tab, click Add.
Select the component type as Procedure Plan Definition.
Click Add to Package.
Make a note of the package name.
Retrieve the Packaged Procedure Plan
Open Salesforce Bench Press and connect it to your source org.
Under Metadata, go to Retrieve, and then paste the package name.
Click Retrieve.
When the retrieval succeeds, first click Fetch, and then click Download.
Unzip the downloaded package.
Open the package.xml file, and remove all dependencies except the procedure plan.
Save the package.xml file.
Compress the package folder.
Import the Packaged Procedure Plan
Log in to the target Salesforce org.
Go back to Workbench and connect it to your target org.
Select the Deploy tab.
Upload the packaged procedure plan.
Check Single Package.
Select Deploy.

From Setup, in the Quick Find box, enter Procedure Plan Definitions, and then select Procedure Plan Definitions. Verify if the procedure plan was imported successfully.

=== ARTICLE: ind.pricing_export_and_import_your_pricing_data.htm ===
---
article_id: ind.pricing_export_and_import_your_pricing_data.htm
title: Export and Import Your Pricing Data
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_export_and_import_your_pricing_data.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_considerations_for_importing_and_exporting_pricing_data.htm
fetched_at: 2026-09-07
---

# Export and Import Your Pricing Data

To create a new package with your pricing data to reuse them in another Salesforce org, create a new package and deploy it on another Salesforce org.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To deploy and use a package:	Salesforce Pricing Design Time
IMPORTANT Before importing data, check your org's current decision tables to ensure you're within the limits. Importing decision tables without verifying available space may cause the data import to fail.
Log in to your Salesforce org that you want to export pricing data.
From Setup, in the Quick Find box, find and select Package Manager.
Click New.
In the Create a Package window, give your package a name and, choose to add details in the optional Description field.
Save your changes.
In the Package Detail window, select the Components tab and click Add.
Select a Component Type. You can select one or more component names from the displayed list.
Click Add to Package.
On the Package Detail page, click Upload.
Enter a Version Name. Edit the Version Number or use the auto-populated value. If needed, enter a description and set a password to protect the package.
Click Upload, again.
After you upload the package, the installation URL is available in the Version Detail.
Click the installation URL on the Version Detail window or copy and paste the URL on a browser window.
The installation URL prompts the user to log in to the subscriber org and then enables them to install the package in any org and enable it when ready.
Enter the username and password of the org where you want to install your package.
Select one of these options.
Install for admins only
Install for all users
Install for specific profiles
Click Install.
Your pricing metadata is now available on your new org.

=== ARTICLE: ind.pricing_formula_based_pricing.htm ===
---
article_id: ind.pricing_formula_based_pricing.htm
title: Build Pricing Rules with Formula-Based Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_formula_based_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Build Pricing Rules with Formula-Based Pricing

Perform functions and mathematical calculations to generate the price of a product. Solve complex pricing scenarios by defining multiple formulas within a single Formula-Based Pricing element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time

Formula-based pricing offers a dynamic approach to price calculation that moves beyond static price lists and discounts. Businesses can define sophisticated pricing rules by using custom formulas and functions within pricing procedures. By leveraging various factors such as product attributes, customer segments, and real-time market conditions, organizations can create highly flexible and responsive pricing strategies.

Formula-Based Pricing is a powerful tool for implementing complex pricing models. It enables greater adaptability to changing business needs and market dynamics compared to traditional, less agile pricing methods. For supported operators and functions in Formula Based Pricing elements, see Operators and Functions in Expression Sets.

Let’s use the Formula Based Pricing element to calculate the final cost for an order of 5 printers at US $200 each by applying a $40 discount, a 10% delivery charge, a 5% per-unit bulk discount, and a $20 rebate.

NOTE Formula Based Pricing doesn't support derived products on quote line items.
Configure a pricing procedure.
To add the Pricing Setting element, click , and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Formula-Based Pricing element, specify your formulas, and map the variables.
You can add up to five formulas.
SCENARIO	FORMULA	OUTPUT VARIABLE	FORMULA LOGIC
Apply promotional discount	

(ListPrice * LineItemQuantity) - 40

	ItemNetTotalPrice	Calculates the base price and applies a $40 discount.
Provide bulk purchase discounts	

ItemNetTotalPrice * 0.05

	ItemDiscountAmount	Applies a 5% discount on the net price.
Calculate the base cost and promotional discount	

ItemNetTotalPrice - ItemDiscountAmount

	ItemNetTotalPrice	Calculates the net price of each line item.
Adjust delivery charges	

ItemNetTotalPrice * 0.10

	ItemTotalAdjDistAmount	Adds a 10% delivery charge.
The quantity of the purchased product	LineItemQuantity	ItemProductAmount	Adds item quantities.
Add rebate to the final amount	ItemNetTotalPrice + ItemTotalAdjDistAmount - 20	TotalLineAmount	Applies a flat discount of $20.
To test your procedure, click Simulate. Enter the input values for your printer product, and click Simulate again.
The price waterfall shows the formulas used to apply discounts and determine the price of the printers, confirming your procedure is working as expected.

=== ARTICLE: ind.pricing_get_ready_to_build_pricing_procedures.htm ===
---
article_id: ind.pricing_get_ready_to_build_pricing_procedures.htm
title: Prerequisites to Build Pricing Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_get_ready_to_build_pricing_procedures.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Prerequisites to Build Pricing Procedures

Before you begin creating pricing procedures and adding elements to them, ensure you have completed these prerequisites. Understanding the fundamentals is crucial for successful implementation and operation of your pricing strategies.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create context definitions:	

Salesforce Pricing Design Time


To create, edit, and activate a decision table in Salesforce Pricing:	Salesforce Pricing Design Time
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time
Decision Tables
Decision tables are essential as they match your input values with the input rows in a decision table, returning the matching row’s output pricing element that uses it in a pricing procedure.
Context Definitions
Context definitions contain the necessary information to run the pricing process. This includes the relationship between nodes and their structure, attributes, context tags, and mapping. Mapping defines the nodes and attributes with the correct input data from Salesforce objects. The pricing procedure runs with its associated tags and writes the results back to the context definition that the tags belong to. A crucial point to remember is that a context tag can’t have the same name as the decision table's label or API name.
Add Products as Price Book Entries
Record each product or service you sell as a product in Revenue Management. These products, also referred to as line items, have a specific selling price and are added as entries to a price book.
Configure a Product Selling Model for Your Products
Product selling models define how products are sold—be it one-time, term-defined, or evergreen subscriptions. They provide flexibility in managing diverse product offerings and streamline how those products are quoted, ordered, and renewed within a revenue management system. These models are crucial for accurately representing different sales approaches for your products.
Create Constant Resources
If your variables lack context tags, create a constant resource to serve as a placeholder for fixed values in your pricing procedures. Constants are used for inputs, outputs, and other values passed from a pricing element.

=== ARTICLE: ind.pricing_get_ready_to_calculate_the_derived_price.htm ===
---
article_id: ind.pricing_get_ready_to_calculate_the_derived_price.htm
title: Prerequisites to Build Discovery and Derived Price Pricing Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_get_ready_to_calculate_the_derived_price.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_derived_price.htm
fetched_at: 2026-09-07
---

# Prerequisites to Build Discovery and Derived Price Pricing Procedures

Before you begin creating discovery procedures to locate pricing data for your products and assets, or to calculate a product’s derived price, ensure you have completed the following prerequisites. A fundamental understanding of these concepts is crucial for the successful implementation and operation of your pricing strategies.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Since you're gathering data from pricing sources (products, assets, quotes), it's necessary to designate your products as both source products and derived products.
A source product is the product from which the price is derived. This product must be added as a price book entry with a list price to a price book.
A derived product is the product for which the price is being calculated. This product must also be added as a price book entry, but its list price must be set to 0. The Derived Price feature will then determine its actual price.
You must create a derived price record where you set up the rules and formulas for calculating a product's price. Think of it as the master plan for figuring out a derived price.
When creating a discovery procedure, the Usage Type must be set to Pricing Discovery. Pricing Discovery identifies and writes pricing data into a context definition using context nodes populated by the pricing discovery function.
Ensure that the same context definition is used in both your discovery procedure and the pricing procedure to calculate a product’s derived price.
If you're locating products in a discovery procedure, use the Derived Price Entries decision table within the Fetch Pricing Rules element in the discovery procedure.
If you’re locating assets, use the Asset Action Source Entries V2 decision table within the Asset Discovery element in the discovery procedure.

When you clone or modify the Default Discovery Procedure for use, you’ll need to ensure that you change the decision table to Asset Action Source Entries V2 and map the new variables.

You can also clone a pricing discovery procedure from the Salesforce Pricing Discovery Procedure expression set template.

When you use the List Price element in a pricing procedure to fetch your products, you must use the Price Book Entries V2 decision table or your custom decision table. This decision table was built primarily for derived pricing scenarios.
When you use both discovery procedures and a pricing procedure to calculate the derived price of a product, you must add the Assetize Order permission set to refresh all the decision tables used.
The Derived Price element can't be used in a pricing procedure that includes the Promotion Execution, Price Propagation, or the Discount Distribution Service elements.

=== ARTICLE: ind.pricing_get_ready_to_create_pricing_actions.htm ===
---
article_id: ind.pricing_get_ready_to_create_pricing_actions.htm
title: Get Ready to Create Pricing Actions
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_get_ready_to_create_pricing_actions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_action_parameters.htm
fetched_at: 2026-09-07
---

# Get Ready to Create Pricing Actions

Before you create pricing actions, complete these prerequisites.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Create Context Definitions with Mapping

Context definitions contain the information required to execute the pricing process. A context definition includes the relationship between nodes and their structure, attributes, context tags, and mapping. Mapping ensures that the nodes and attributes are updated with the right input data from the Salesforce objects. See Context Definitions and Map Context Definitions.

Create Pricing Procedures

Build pricing procedures by using pricing elements where each element forms a step in a pricing procedure. When a pricing procedure is executed with the associated context tags, the results of the pricing procedures are written back to the context definition that the tags belong to. See Build Your Pricing Procedures .

Configure Pricing Parameters for Standard Objects
To ensure that the standard pricing action button functions properly, define pricing parameters that connect it to a context definition, the context's mapping, and the pricing procedure for calculating product prices.

=== ARTICLE: ind.pricing_limits.htm ===
---
article_id: ind.pricing_limits.htm
title: Salesforce Pricing Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Salesforce Pricing Limits

Review the default limits for Salesforce Pricing’s components and their usage. To modify the set default values, ask your Salesforce administrator to raise a support ticket.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Discovery Procedures
VALUE	DEFAULT	MINIMUM	MAXIMUM
The number of discovery procedures in an org	2000	1	10000
The duration that a discovery procedure can remain active	10 seconds	1 second	60 seconds
Pricing Procedures
VALUE	DEFAULT	MINIMUM	MAXIMUM
The number of pricing procedures in an org	2000	1	10000
The duration that a pricing procedure can remain active	1 minute	1 second	2 minutes
Pricing Elements
VALUE	DEFAULT	MINIMUM	MAXIMUM
The number of pricing elements in a discovery procedure	50	2	100
The number of pricing elements in a pricing procedure	200	2	200
The duration that a pricing element can remain active	60 seconds	4 milliseconds	80 seconds
The number of mappings the Map Line Item element can have	70	-	100
The number of context tag mappings the Assignment element can have	20	-	50
Price Impacting Attributes
VALUE	DEFAULT	MINIMUM	MAXIMUM
The number of price impacting attributes that can be associated with a product in an org	25	1	50
Contributing Products or Assets
VALUE	DEFAULT	MINIMUM	MAXIMUM
The number of products that can be associated with a contributing product in an org	40	1	

50

This limit is the total number of contributors for a derived product. Both Transactional and Non Transactional


The number of assets that can be associated with a contributing asset in an org	-	-	50
Other Limitations
Pricing procedures don't support the children of sibling nodes for any context definition. For example, in the Sales Transaction context, children or descendants of a sibling node, Sales Transaction Item aren’t supported.
Pricing element functionality is restricted to context tags at the Transaction Item and Transaction Header levels. Descendant and sibling node attributes are unsupported.
For values of the Number data type that are 10,000,000 or greater, the Connect REST API returns standard decimal notation instead of scientific notation. For example, the API returns 10000000 instead of 1.0E7. Additionally, standard decimal values do not include a trailing .0. For example, the API returns 10000000 instead of 10000000.0.
The Invocable Headless API returns values smaller than 0.000001 in scientific notation, while other Connect REST API endpoints return them in standard decimal notation
For stored values with trailing zeros, the API always returns the value at its full stored precision. For example, as 10.000 instead of trimming the zeros to 10.0.

=== ARTICLE: ind.pricing_list_group_list_operation.htm ===
---
article_id: ind.pricing_list_group_list_operation.htm
title: List Group and List Operation
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_list_group_list_operation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# List Group and List Operation

Efficiently process lists of data and implement complex pricing logic and calculations by enabling filtering, value lookups, and various computations on line items.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time

The List Group element serves as a container for processing individual line items within a list variable. It's a fundamental step element in the pricing procedure that facilitates iterating through a list and performing operations on its elements. Every list group must begin with a List Filter, which defines the initial criteria for narrowing down the list. Following the List Filter, a List Group can incorporate multiple calculation and lookup table components to further process the refined list.

The List Filter, as the initial element within a List Group, is solely responsible for filtering items in the input list based on predefined conditions, utilizing list variables to establish these criteria. For supported operators and functions in List Filter element, see Operators and Functions in Expression Sets.

Let's consider a scenario where you want to set conditions to only give discounts when a customer purchases 50 or more printer bundles. You can also set a limit to stop price calculations once this condition has been met. If your customer purchases less than 50 printer bundles, it doesn’t meet the condition, then the pricing procedure skips this step altogether.

IMPORTANT Only one list filter can exist within a given list group.
Configure a pricing procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the List Group element.
In the list group, configure the List Operation by setting a condition that a 10% discount on the final price of the printers can only be applied if the user purchased over 50 units.
Filter Condition Requirements: All Conditions Are Met (AND)
Resource: # LineItemQuantity
Operator: Greater Than
Value: 50
Within the list container, add the Formula Based Pricing element and specify these variable values.
Calculation Formula: ItemNetTotalPrice - ( ItemNetTotalPrice * 0.10 )
Output Variable: TotalLineAmount
To stop pricing, within the list container, and under the Formula Based Pricing element, add the Stop Pricing element.
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your printer bundle product and click Simulate again.
The price waterfall shows the formula used to calculate the total cost of the printer bundles with a discount of 10%. You also see that since the condition of over 50 printer bundles were met, the price calculation stopped, confirming that your procedure is working as expected.
IMPORTANT

We recommend adding another filter condition to your List Group element, specifying that the value of the context tag isn’t a null. When pricing is executed on a quote or an order, if the tag doesn’t have a value or is null, the procedure will return an error.

For example, if you add a filter condition to a line item indicating that the line item’s value is 100, then you must add a condition indicating that the line item’s value is not a null value. Your condition would look like this: {LineItem equals isNotNull} AND {LineItem equals 100}.

=== ARTICLE: ind.pricing_map_context_tags_in_pricing_procedures.htm ===
---
article_id: ind.pricing_map_context_tags_in_pricing_procedures.htm
title: Map Context Tags
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_map_context_tags_in_pricing_procedures.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Map Context Tags

Simplify context tag mapping by using pricing elements to streamline variable mapping, ensuring accurate and straightforward pricing configurations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Context tags connect pricing procedure variables to fields in your context definition. Without these mappings, the pricing procedure can't read input data from the transaction or write calculated values back to it.

IMPORTANT When price waterfall is enabled in your pricing settings, you must map the price_water_fall context tag in both the Pricing Setting and Map Line Item elements. If the Map Line Item element doesn't include this mapping, you receive the error: "Specify a context tag for the Price Waterfall variable in the Map Line Item element when price waterfall is enabled and setup in the Pricing Settings element."

Two pricing elements handle context tag mapping.

Pricing Setting
The Pricing Setting element serves as the initial element for any pricing procedure. They're used to map common variables in a pricing procedure to context tags.
Map Line Item
The Map Line Item element is used for precise mapping of variables. It maps variables at the main line item level and sub-line item levels, which are created when multiple transactions occur on the same line item within different pricing elements.
Map Line Item Limits
Before you add the Map Line Item element to a pricing procedure, review these limitations and configuration requirements.

=== ARTICLE: ind.pricing_map_line_item_element.htm ===
---
article_id: ind.pricing_map_line_item_element.htm
title: Map Line Item
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_map_line_item_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_map_context_tags_in_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Map Line Item

The Map Line Item element is used for precise mapping of variables. It maps variables at the main line item level and sub-line item levels, which are created when multiple transactions occur on the same line item within different pricing elements.

This element is valuable for mapping variables in both discovery and pricing processes. It must be placed second in line, immediately following either the Discovery Settings or Pricing Settings element.

Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Click to add the Map Line Item element to map your variables to the appropriate context tags at both the context node level and the child node level.

=== ARTICLE: ind.pricing_map_line_item_limits.htm ===
---
article_id: ind.pricing_map_line_item_limits.htm
title: Map Line Item Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_map_line_item_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_map_context_tags_in_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Map Line Item Limits

Before you add the Map Line Item element to a pricing procedure, review these limitations and configuration requirements.

Use the Map Line Item element only for standard mapping. Adding custom logic or using the element primarily to persist values can degrade performance during pricing execution.
The Map Line Item element doesn't support parallel execution. To use this element, disable parallel execution for the pricing procedure.
Don't use the Map Line Item element together with delta pricing in the same use case.
The Map Line Item element doesn't support derived pricing.
In both pricing and discovery procedures, place the Map Line Item element second in the procedure, immediately after the Pricing Setting element or the Discovery Settings element.
To map values to a quote line item detail, place the Map Line Item element second in the procedure, immediately after the Pricing Setting element. Use the Assignment element after the Map Line Item element to initialize the tags used in the Map Line Item element.
If you add custom fields to entities such as quote line items, quote line item details, order products, or order product details, update the context definition accordingly.
Map the custom field from the line item to the detail item. Don't write the value directly to the custom detail field. The element saves the value to the detail item when a detail item exists; otherwise, it saves the value to the line item.
For mapping limits for this element, see Salesforce Pricing Limits.

=== ARTICLE: ind.pricing_modify_price_adjustment_matrices.htm ===
---
article_id: ind.pricing_modify_price_adjustment_matrices.htm
title: Modify Price Adjustment Matrices
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_modify_price_adjustment_matrices.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_recipes.htm
fetched_at: 2026-09-07
---

# Modify Price Adjustment Matrices

Customize your pricing recipes by associating them with decision tables, allowing you to offer customers discounts based on specific conditions.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To manage pricing recipes:	

Salesforce Pricing Design Time

From Setup, in the Quick Find box, find and select Pricing Recipes.
Choose the pricing recipe that you want to modify.
On the Price Adjustment Matrix tab, click Modify.
Select or deselect the decision tables you want to associate or disassociate with this recipe.
If necessary, set the default mapping to the output variables for your pricing elements.
Select a pricing component type.
Map the rule variables associated with the decision table.
Save your changes.

=== ARTICLE: ind.pricing_monthly_proration_examples.htm ===
---
article_id: ind.pricing_monthly_proration_examples.htm
title: Monthly Proration Examples
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_monthly_proration_examples.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_variables.htm
fetched_at: 2026-09-07
---

# Monthly Proration Examples

Demonstrates how the system calculates pricing based on a monthly billing cycle.

Base Transaction Details (All Examples)
Effective From: 2025-03-28
Effective To: 2026-02-04
Total Duration: 314 Days
Start Proration Day: 5 (Used for DayOfPeriod examples)
Start Proration Month: February (Used for DayOfPeriod examples)
Proration Period: Monthly
List Price: $90.00

1. Start Proration Period: DayOfPeriod (Day 5) and Allow Partial Proration Periods: True

Calculation Logic: The billing cycles run from the 5th of one month to the 4th of the next.
Period 1 (Partial): 5-Mar-2025 to 4-Apr-2025
Total Days in Period: 31
Utilized Duration: 28-Mar-2025 to 4-Apr-2025 (8 Days)
Pricing Term Count: 8 / 31 = 0.258065
Period 2 (Full): 5-Apr-2025 to 4-May-2025
Pricing Term Count: 1.0
... (Periods 3 through 10 are full months) ...
Period 11 (Full): 5-Jan-2026 to 4-Feb-2026
Utilized Duration: 5-Jan-2026 to 4-Feb-2026 (Full Period)
Pricing Term Count: 1.0
Total Pricing Term Count:: 0.258065 (Period 1) + 10 (Periods 2-11) = 10.258065
Price: $90 x 10.258065 = $923.23

2. Start Proration Period: DayOfPeriod (Day 5) and Allow Partial Proration Periods: False

Pricing Term Count: 1.0
Calculation Logic: The term spans 10 full monthly periods (Apr–Jan) plus 1 partial period (March 28–Apr 4). The partial period is rounded up to 1 unit.
Total: 1 (Partial) + 10 (Full) = 11.0
Subscription Price: $90 x 11.0 = $990.00

3. Start Proration Period: AlignToCalendar (1st of Month) and Allow Partial Proration Periods: True

Calculation Logic: Billing cycles align with the calendar month (1st to 30th/31st).
Period 1 (partial): 1-Mar-2025 to 31-Mar-2025
Total Days in Period: 31
Utilized Duration: 28-Mar-2025 to 31-Mar-2025 (4 Days)
Pricing Term Count: 4 / 31 = 0.129032
Period 2 (Full): 1-Apr-2025 to 30-Apr-2025
Pricing Term Count: 1.0
... (Periods 3 through 11 are full months)...
Period 12 (Partial): 1-Feb-2026 to 28-Feb-2026
Total Days in Period: 28
Utilized Duration: 1-Feb-2026 to 4-Feb-2026 (4 Days)
Pricing Term Count: 4 / 28 = 0.142857
Total Pricing Term Count: 0.129032 + 10 (Full Months) + 0.142857 = 10.271889
Price: $90 x 10.271889 = $924.47

4. Start Proration Period: AlignToCalendar (1st of Month) and Allow Partial Proration Periods: False

Calculation Logic: The term touches 12 distinct calendar months (Mar 2025 through Feb 2026).
March 2025 (Touched) = 1.0
April 2025 through Jan 2026 (10 Full Months) = 10.0
February 2026 (Touched) = 1.0
Total: 12.0
Price: $90 x 12.0 = $1,080.00

5. Start Proration Period: AlignToCalendar (Jan 1) and Allow Partial Proration Periods: True

Calculation Logic: The system calculates the total days utilized divided by the days in the year.
Period 1: 1-Jan-2025 to 31-Dec-2025
Utilized Duration: 28-Mar-2025 to 31-Dec-2025 (279 /365)
Period 2: 1-Jan-2026 to 31-Dec-2026
Utilized Duration: 1-Jan-2026 to 04-Feb-2026 (35/365)
Total: (279/365 + 35/365) = 0.860274
Subscription Price: $800 x 0.860274 = $688.22

6. Start Proration Period: AlignToCalendar (Jan 1) and Allow Partial Proration Periods: False

Calculation Logic: The term crosses the Jan 1 boundary, touching two distinct calendar years (2025 and 2026). Each "touched" calendar year counts as 1.0.
Period 1: 2025 (Touched) = 1.0
Period 2: 2026 (Touched) = 1.0
Subscription Price: $800 x 2.0 = $1,600.00

=== ARTICLE: ind.pricing_monthly_proration_examples_for_leap_years.htm ===
---
article_id: ind.pricing_monthly_proration_examples_for_leap_years.htm
title: Monthly Proration Examples for Leap Years
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_monthly_proration_examples_for_leap_years.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_variables.htm
fetched_at: 2026-09-07
---

# Monthly Proration Examples for Leap Years

Review calculations for monthly billing cycles, and learn how the total days adapt to leap years and varying month lengths. For a monthly product selling model, Salesforce Pricing anchors exactly to the numerical start date. If an anniversary subscription starts on the 29th, 30th, or 31st, and that exact date doesn't exist in the following month, Salesforce Pricing uses a design convention: it aligns the next period to the latest available day of that subsequent month. All full periods behave as "month-end to month-end minus one.

Base Transaction Details (All Examples)
Proration Period: Monthly
List Price: $150.00

1. Start Proration Period: Anniversary (Feb 28)

Effective From: 2027-02-28
Effective To: 2027-03-27
Total Duration: 28 Days
Calculation Logic: For start dates on or before the 28th, the calculation is straightforward. Salesforce Pricing anchors to the 28th. The full period is defined strictly from the 28th of the current month to the 27th of the next month.
Period 1: 28-Feb-2027 to 27-Mar-2027
Total Days in Period: 28
Utilized Duration: 28-Feb-2027 to 27-Mar-2027 (28 Days)
Pricing Term Count: (28 / 28) = 1.0
Subscription Price: $150 x 1.0 = $150.00

2. Start Proration Period: Anniversary (Jan 29)

Effective From: 2025-01-29
Effective To: 2025-02-27
Total Duration: 30 Days
Calculation Logic: Salesforce Pricing anchors to the 29th. Because February doesn't have a 29th in a standard year, the next period must start on the latest available date (February 28). This forces Period 1 to end on February 27 to maintain the full month convention.
Period 1: 29-Jan-2025 to 27-Feb-2025
Total Days in Period: 30
Utilized Duration: 29-Jan-2025 to 27-Feb-2025 (30 Days)
Pricing Term Count: (30 / 30) = 1.0
Subscription Price: $150 x 1.0 = $150.00

3. Start Proration Period: Anniversary (Jan 30)

Effective From: 2025-01-30
Effective To: 2025-03-29
Total Duration: 59 Days
Calculation Logic: Salesforce Pricing anchors to the 30th. Since February lacks a 30th, Period 1 ends on February 27 so the next period can start on the latest available date (February 28). Because March does have a 30th, Period 2 resumes starting on March 30, which forces Period 2 to end on March 29.
Period 1: 30-Jan-2025 to 27-Feb-2025
Total Days in Period: 29
Utilized Duration: 30-Jan-2025 to 27-Feb-2025 (29 Days)
Period 2: 28-Feb-2025 to 29-Mar-2025
Total Days in Period: 30
Utilized Duration: 28-Feb-2025 to 29-Mar-2025 (30 Days)
Pricing Term Count: (29 / 29) + (30 / 30) = 1.0 + 1.0 = 2.0
Subscription Price: $150 x 2.0 = $300.00

4. Start Proration Period: Anniversary (Jan 31)

Effective From: 2025-01-31
Effective To: 2025-03-30
Total Duration: 59 Days
Calculation Logic: Salesforce Pricing anchors to the 31st and adjusts for months with fewer days. Period 1 ends on February 27 so Period 2 can start on February 28. For the transition to April (which lacks a 31st), Period 2 must end on March 30 so Period 3 can start on the latest available date (April 30).
Period 1: 31-Jan-2025 to 27-Feb-2025
Total Days in Period: 28
Utilized Duration: 31-Jan-2025 to 27-Feb-2025 (28 Days)
Period 2: 28-Feb-2025 to 30-Mar-2025
Total Days in Period: 31
Utilized Duration: 28-Feb-2025 to 30-Mar-2025 (31 Days)
Pricing Term Count: (28 / 28) + (31 / 31) = 1.0 + 1.0 = 2.0
Subscription Price: $150 x 2.0 = $300.00

=== ARTICLE: ind.pricing_operations_console.htm ===
---
article_id: ind.pricing_operations_console.htm
title: Monitor and Troubleshoot Pricing Issues
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_operations_console.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.revenue_operations_console.htm
fetched_at: 2026-09-07
---

# Monitor and Troubleshoot Pricing Issues

Using the Revenue Cloud Operations Console, get valuable insights into how your organization uses pricing data and the information generated by pricing operations. Resolve operational issues quickly by viewing price logs to troubleshoot and fix errors caused by pricing APIs.

Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.

The Revenue Cloud Operations Console offers a centralized hub for debugging your pricing procedures and configurations. It helps you monitor for configuration issues and conduct a root cause analysis of any pricing outcome.

Understand Your Pricing Data
The Revenue Cloud Operations Console has four sections that show you how your pricing data is used.
Investigate and Analyze Pricing API Execution Logs
Open price logs to resolve errors by using the log information in the Revenue Cloud Operations Console app. All headless pricing and pricing API executions, including discovery and pricing procedures performed within an API call, are recorded as pricing logs. This includes successful and unsuccessful executions.
Resolve API Execution Errors
Use the Debug Details tab to troubleshoot errors in the executed API.
Set Up Advanced Price Logs
Capture input values and exception details for complex pricing elements. Use this diagnostic data to identify and fix performance issues.

=== ARTICLE: ind.pricing_perform_pricing_adjustment_batch_job.htm ===
---
article_id: ind.pricing_perform_pricing_adjustment_batch_job.htm
title: Perform a Pricing Adjustment Batch Job
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_perform_pricing_adjustment_batch_job.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_adjustment_batch_jobs.htm
fetched_at: 2026-09-07
---

# Perform a Pricing Adjustment Batch Job

Before you begin a pricing adjustment batch job, remember the following.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To view pricing adjustment batch job logs:	Salesforce Pricing Design Time
All bulk updates are made to a product's price. So, you can make a bulk update to any price adjustment schedule or price book.
You can update up to 200 pricing records in a batch.
Don’t run multiple batch jobs simultaneously. Wait for each job to complete before starting the next one.

Let’s consider a scenario where we need to make a bulk update of increasing the price by $10 of all products whose product selling model is set to Evergreen.

From App Launcher, find and select Price Management.
From the app navigation menu, select Price Books.
Select Standard Price Book.
On the Related tab, under the Price Book Entries section, click View All.
A list of all the price book entries associated with the Standard Price Book are displayed.
Based on our example, select all the entries whose product selling model is Evergreen.
Select Pricing Adjustment Batch Job.
In the Update Price Book Entries window, specify these details.
Update Type: Amount
Update Value: $10
NOTE
The update value depends on the update type selected. There are three types of updates - Amount, Percentage, and Override.
To increase the value of your record, add a whole number. To decrease the value of a record, add a negative value. If the update type is Amount, and you want to increase the dollar value of your records, enter 10, and to decrease the adjustment value, enter -10.
If you’re making changes to a price adjustment schedule, then you’ll need to provide effective dates.
Price book entries only store the price of a product and don’t have effective dates associated with their records.
Save your changes.

=== ARTICLE: ind.pricing_permissions_salesforce_pricing.htm ===
---
article_id: ind.pricing_permissions_salesforce_pricing.htm
title: Salesforce Pricing Editions, Permission Sets, and Personas
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_permissions_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_discover_and_explore.htm
fetched_at: 2026-09-07
---

# Salesforce Pricing Editions, Permission Sets, and Personas

Salesforce Pricing uses permission sets to ensure different user roles have the specific access they need. By assigning the right permission set licenses, organizations can securely manage pricing functionalities, giving each user the necessary access to complete their tasks.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Before you being creating users and profiles, and assigning them, we recommend checking out these resources.

View and Manage Users
Create or Clone Profiles
View and Manage Your Permission Set Licenses
User Interface

Salesforce Pricing is available in Lightning Experience.

Supported Products and Editions

Here's a list of products that provide access to Salesforce Pricing.

PRODUCT	EDITIONS
Health Cloud	Enterprise, Performance, and Unlimited
Communications Cloud	Enterprise, Performance, and Unlimited
Energy & Utilities Cloud	Enterprise, Performance, and Unlimited
Insurance Cloud	Enterprise, Performance, and Unlimited
Financial Services Cloud	Enterprise, Performance, and Unlimited
Media Cloud	Enterprise, Performance, and Unlimited
Asset Service Lifecycle Management	Enterprise, Performance, and Unlimited
Revenue Management	Enterprise, Performance, and Unlimited
Create Users and Profiles

To begin, create users for Salesforce Pricing. Then assign users the appropriate permission sets. To help you plan, refer to the Salesforce Pricing Personas table.

When you create a user, you must also assign a profile. Profiles define default settings for users. Some organizations create their own profiles, while others choose to use profiles included with Salesforce.

Remember, users can have only one profile, but can have many permission sets assigned to them.

Assign Permission Sets

Assign permission sets to your users. Refer to this table for guidance on what permission sets are required for common Salesforce Pricing personas.

PERSONA	DESCRIPTION	PERMISSION SET LICENSE NAME
Pricing Admin	

The pricing admin can:

Turn on Salesforce Pricing
Create and manage all Salesforce Pricing objects and features
Manage pricing recipes and decision tables and their mappings in a pricing recipe
Turn on Price Waterfall and Price Waterfall Persistence
	

Salesforce Pricing Admin

Salesforce Pricing Design Time User


Pricing Design Time User	The pricing designer has access to all pricing elements and the pricing procedure feature.
Salesforce Pricing Run Time	The pricing run time designer has read-only access to pricing data and can call Salesforce Pricing APIs.	

Salesforce Pricing Run Time User


Pricing Analyst	The pricing analyst can access the Price Management app. They also have the create, read, update, and delete access to the records created on Salesforce Pricing.

=== ARTICLE: ind.pricing_price_adjustment_schedules_salesforce_pricing.htm ===
---
article_id: ind.pricing_price_adjustment_schedules_salesforce_pricing.htm
title: Explore Price Adjustment Schedules
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_price_adjustment_schedules_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Explore Price Adjustment Schedules

Implement dynamic pricing strategies by automating price calculations and adjustments based on various factors like quantity or product attributes. Build flexible pricing models that optimize revenue and adapt to specific market conditions or customer needs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Price Adjustment Schedules are a key feature within Salesforce Pricing, designed to facilitate dynamic pricing models. They move beyond static, fixed pricing by allowing for the automatic calculation and adjustment of prices based on various criteria. This enables businesses to implement flexible pricing strategies tailored to specific conditions.

For instance, you can set up tiered pricing based on the quantity purchased, apply adjustments based on specific features or characteristics of a product, or define special pricing for combined products within a bundle. Ultimately, Price Adjustment Schedules help determine the final price of a product or service by applying relevant discounts, overrides, or other adjustments under specified conditions.

There are three types of price adjustment schedules.

Price Adjustment Tiers: Use this adjustment to define a product’s price based on the number of items being sold. 
Attribute Based Adjustments: Use this adjustment to define a product’s price based on its attributes or the configuration of a product.
Bundle Based Adjustments: Use this adjustment to define a product’s price when it's being sold as a bundle or a combination of different products.
Create and Manage Price Adjustment Schedules
Define price adjustment schedules and set volume, attribute, or bundle-based discounts for your products.
Pricing Adjustment Batch Jobs
Utilizing pricing adjustment batch jobs is key for efficient, accurate bulk pricing updates. You can initiate these operations directly from the Related List and List View components of Price Book Entry, Attribute Based Adjustment, Bundle Based Adjustment, and Price Adjustment Tier objects.

=== ARTICLE: ind.pricing_price_books_salesforce_pricing.htm ===
---
article_id: ind.pricing_price_books_salesforce_pricing.htm
title: Cost Books and Price Books
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_price_books_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Cost Books and Price Books

Track the expenses associated with manufacturing a product in a cost book, and record the product's selling price in a price book. You can have multiple price books and cost books in your Salesforce org.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Salesforce Pricing provides a predefined standard price book; however, you can create your own standard price book using the Price Management app. An organization must have a price book to track its products, but a cost book is optional.

It’s important to distinguish between cost books and price books. The primary difference is:

Cost Books focus on internal expenses incurred by the business.
Price Books define the selling prices of products and services for various customer segments or channels.
Define Costs in Cost Books
A cost book acts as a detailed expense tracker for your products. Think of it as the place where you record every cost associated with creating or delivering a product or service. Within a cost book, you create individual entries for each specific expense, such as the cost of raw materials, manufacturing, or shipping. These detailed cost entries are then linked directly to the corresponding product in your catalog, giving you a clear, itemized view of what it truly costs to bring that item to market.
Define Prices in Price Books
A price book is essentially your company's master product catalog, containing a complete list of your products and services along with their specific selling prices.

=== ARTICLE: ind.pricing_price_propagation.htm ===
---
article_id: ind.pricing_price_propagation.htm
title: Price Propagation
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_price_propagation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Price Propagation

Enable complex, hierarchical pricing logic by propagating values across different levels of a transaction from line items to groups and back. Use the Price Propagation element to perform sequential calculations and roll up totals from children to parents.

Key capabilities in Price Propagation

Price Propagation handles nested structures where a change at one level automatically updates related levels. Unlike standard bundle pricing, propagation supports flexible relationships between entities, such as group-to-group or group-to-item.

Horizontal Propagation: Calculate fields sequentially within a single line or group. For example, ensuring Net Price is calculated only after unit cost and margin are determined.
Ascending Propagation (Rollup): Aggregate values from child lines to parent groups. For example, calculating a Group Total by summing the Net Price of all items in that group.
Example of Group-to-Item Hierarchy

This example illustrates a multilevel hierarchy where the building node acts as the top-level parent, containing nested subgroups for floors and rooms and the corresponding line items.

Building (Group)
Floor (Subgroup)
Room (Subgroup)
Panel 001 (Line Item)
Panel 002 (Line Item)
Key Terms Used in Price Propagation
TERM	EXPLANATION	EXAMPLE
Group	A parent entity used to group and organize related quote line items.	Building (a group containing Floors and Rooms).
Subgroup	A group nested within another group, allowing multilevel structures in a quote.	Floor (subgroup under Building), Room (subgroup under Floor).
Node	A data source added in the propagation setup representing a specific level of data.	SalesTransactionItem (representing Panel 001), SalesTransactionGroup (representing Building).
Attribute	A field or a context tag on a node that can be used in formulas.	Net Price, Cost, Discount of Panel 001.
Merged Attribute	A unified column name created to map data between parent and child nodes for calculation.	MergedTotalCost (used to roll up Panel costs into the Room/Building cost).
Horizontal Calculation	Formulas applied sequentially within the same line or group level.	Panel Net Price = List Price – Discount
Ascending Propagation	The flow of values upward by rolling up totals from children to parent groups.	The Net Price of Panel 001 and Panel 002 rolls up to calculate the room total, which rolls up to floor, and then the building.
Add Nodes	Action to bring in data sources and their attributes into the propagation table.	Add the SalesTransactionItem node to access the Net Price of the Panel.
Join Nodes	Action to create relationships between nodes by using ID fields.	Join Room (Child Group) with Panel (Line Item) using a Parent ID to establish hierarchy.
Sequence	A mandatory numeric value that determines the strict order in which horizontal formulas are calculated.	Assign Sequence 1 to Panel Net Price, ensure it's calculated before it is used in Sequence 2 to calculate the Panel Margin.
Price Propagation Limits
Before adding the Price Propagation element to your pricing procedure, keep these points in mind:
Configure the Price Propagation Element
Define the formulas and execution sequence for your hierarchical pricing logic by using the Price Propagation element.

=== ARTICLE: ind.pricing_price_propagation_limits.htm ===
---
article_id: ind.pricing_price_propagation_limits.htm
title: Price Propagation Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_price_propagation_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_propagation.htm
fetched_at: 2026-09-07
---

# Price Propagation Limits

Before adding the Price Propagation element to your pricing procedure, keep these points in mind:

You can add only one Price Propagation element per pricing procedure.
The Price Propagation element is not compatible with Derived Pricing, Map Line Item, and Promotions elements. Do not include these elements in the same pricing procedure.
The Price Propagation element is not supported inside a list group.
If delta pricing is enabled, copy the net unit price value before the propagation element runs and save it in a separate tag. Use the tag in your propagation table and formulas.
Do not use the propagation element in pricing procedures for amend, renew, or cancel transactions. Doing so may result in inaccurate pricing.
Do not use the propagation element as a substitute for formula or aggregate elements. It is designed for specific roll-up logic and behaves differently than standard calculation elements.
Deselecting Enable Propagation doesn't delete the propagation configuration. The settings remain in the Pricing Setting JSON to prevent data loss if you re-enable the feature. To reset the configuration, remove the Pricing Setting element and add it again.

=== ARTICLE: ind.pricing_price_tracking.htm ===
---
article_id: ind.pricing_price_tracking.htm
title: Track Price Ranges for Products
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_price_tracking.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Track Price Ranges for Products

Ensure transparent pricing policies and comply with regional directives by tracking a product's minimum and maximum prices over time using the Price Tracking element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

By tracking and showcasing a product's historical price fluctuations, like its lowest and highest price points over the last 30 days, customers gain a comprehensive understanding, empowering them to make informed purchasing decisions.

When you use the Price Tracking element, the fetched minimum and maximum prices are stored in the Product Price Range object. If a product's price frequently changes within a day, its daily price range is recorded in the Product Price History Log object. A product's price is determined by its combination with an associated price book, its product selling model, and the transaction currency.

Configure Price Tracking History
Track the minimum and maximum prices of a product over a period to help your users make well-informed buying decisions.
Update Your Product Price Range Entries Decision Table
For users who previously enabled minimum price tracking, update your decision table to include the newly introduced option for tracking maximum prices. If you enable maximum price in Price Tracking History settings without this update, your pricing procedure will fail during execution.
Price Tracking Actions
The price tracking element performs actions to help you fetch and record your product’s price range. Based on your business needs you can perform the required action using a pricing procedure.

=== ARTICLE: ind.pricing_price_tracking_actions.htm ===
---
article_id: ind.pricing_price_tracking_actions.htm
title: Price Tracking Actions
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_price_tracking_actions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_tracking.htm
fetched_at: 2026-09-07
---

# Price Tracking Actions

The price tracking element performs actions to help you fetch and record your product’s price range. Based on your business needs you can perform the required action using a pricing procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
ACTION TYPE	DESCRIPTION
Get	This action type fetches the price of the product during a transaction.
Save	This action type saves the price of a product during a transaction that can be used as an input variable in the pricing procedure.
Save & Get	This action type fetches and saves the current recorded price of the product, as configured.

To run the Get action type again, you must manually refresh the decision table.

Ensure Price Transparency Using the Price Tracking Element
Verify if your product prices are tracked, monitored, and captured using the Price Tracking element.

=== ARTICLE: ind.pricing_pricing_action_parameters.htm ===
---
article_id: ind.pricing_pricing_action_parameters.htm
title: Pricing Action Parameters
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_pricing_action_parameters.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_unique_pricing_scenarios.htm
fetched_at: 2026-09-07
---

# Pricing Action Parameters

To calculate the price of products directly from any object’s record page, use the Calculate Price button. All pricing actions are associated with a context definition and a pricing procedure so that the pricing data that is processed during the pricing process is stored directly in the Salesforce object.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

There are two types of pricing action buttons.

Standard Pricing Action button: Configure objects such as Quote, Order, Contract, Case, and Opportunity to show the pricing action button on their record page by editing their page layout.
Custom Pricing Action button: Add the pricing action button as a Lightning component by editing the page directly from the object’s record page.
Get Ready to Create Pricing Actions
Before you create pricing actions, complete these prerequisites.
Standard Pricing Actions
To view the pricing action button on the object’s record page, edit the page layout of the object.
Customize the Pricing Action Button by Using Lightning Components
Add the Pricing Calculation standard Lightning component to object record pages to make custom pricing actions available across your org and calculate the price of a product directly from the record page.

=== ARTICLE: ind.pricing_pricing_adjustment_batch_jobs.htm ===
---
article_id: ind.pricing_pricing_adjustment_batch_jobs.htm
title: Pricing Adjustment Batch Jobs
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_pricing_adjustment_batch_jobs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_adjustment_schedules_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Pricing Adjustment Batch Jobs

Utilizing pricing adjustment batch jobs is key for efficient, accurate bulk pricing updates. You can initiate these operations directly from the Related List and List View components of Price Book Entry, Attribute Based Adjustment, Bundle Based Adjustment, and Price Adjustment Tier objects.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

For failed requests, a detailed report with error messages is available via the related list of the batch job record. This allows you to quickly identify issues, make necessary edits, and re-execute the job to ensure all adjustments are applied successfully.

Let’s explore the primary tasks you can perform using the Pricing Adjustment Batch Jobs feature.

Perform a Pricing Adjustment Batch Job
Before you begin a pricing adjustment batch job, remember the following.
View Pricing Adjustment Batch Job Logs
After your pricing adjustment batch job record is created, you can check the status and details of the job. If your batch job has failed or partially failed, you can review the generated logs to find out the reason for the failure.
Fix and Execute Failed Pricing Adjustment Batch Jobs
You can resolve issues with your failed records by making the necessary edits and running the pricing batch job again. For example, a pricing adjustment batch job may fail when an adjustment relies on a product attribute that is missing or invalid.

=== ARTICLE: ind.pricing_pricing_discount_calendar.htm ===
---
article_id: ind.pricing_pricing_discount_calendar.htm
title: Pricing Discount Calendar
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_pricing_discount_calendar.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_access_your_pricing_information.htm
fetched_at: 2026-09-07
---

# Pricing Discount Calendar

Pricing analysts can easily see and understand the diverse discounts associated with a product through the pricing discount calendar.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

The Pricing Discount calendar shows all the applied price adjustment schedule types for a product and the range of discounts over different dates. To better analyze this information, users can group discounts based on their respective schedule types, such as Volume, Attribute, and Bundle. They can also search for a particular schedule type by using available filters.

To help you easily identify their date range and status, pricing discounts are color-coded. Green indicates that the pricing discount applied is a volume-based discount, Red indicates an attribute-based discount, and Blue indicates that the pricing discount applied is a bundle-based discount.

The calendar is available from the product record in the Price Management app and requires either the Salesforce Pricing Design Time User or Salesforce Pricing Run Time User permission.

How to Use the Pricing Discount Calendar?

There are various options available to view specific discounts for a product.

COMPONENT	HOW IT HELPS	HOW TO USE IT
Today	View the calendar from the current date.	If you’re on a viewing period in the future or in the past, click Today to view the discounts for the current date.
Start Date	Select the date that you want to view the calendar from.	To view discounts applied to a product for a specific period, select the start date.
Period	Select the date range of the calendar. Use to change the dates on the calendar for the date range that you selected. 	To view discounts for a specific date range, for example, a month, select Month from the dropdown.
Group By	Select how you want the discounts grouped.	To group pricing discounts based on the price adjustment schedule, select Schedule Type.
Filter	Use filters to find a specific pricing discount applied to your product.	Use filters to find discounts based on the schedule type, the selling model type, and the pricing term unit.
Refresh	Refresh the calendar after you add a discount or price adjustment method against a product to see it on the calendar.	For example, if you can’t find a discount that another user created while you were viewing the calendar, refresh the calendar.

=== ARTICLE: ind.pricing_pricing_element.htm ===
---
article_id: ind.pricing_pricing_element.htm
title: Use Pricing Elements in Pricing Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_pricing_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Use Pricing Elements in Pricing Procedures

Pricing elements are the fundamental building blocks used to construct a pricing procedure. Use these elements to define how prices are calculated and applied in Revenue Management (formerly Revenue Cloud).

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

When a pricing procedure is executed, most elements query relevant decision tables based on input parameters to retrieve pricing rules and values. Other elements rely on formulaic calculations, or assist with mapping relevant context tags within a procedure.

Pricing elements enable comprehensive and flexible pricing strategies. They ensure accurate pricing of products, whether in their simple form, using attributes as pricing parameters, or as complex product bundles. Furthermore, these elements facilitate the design of various product selling models, such as one-time sales or subscriptions. They also utilize price adjustment schedules to automatically adjust prices based on your unique pricing strategies, helping sales representatives offer their customers the best price for their products.

Map Context Tags
Simplify context tag mapping by using pricing elements to streamline variable mapping, ensuring accurate and straightforward pricing configurations.
Fetch the List Price of a Product
To get the base price of a product for pricing procedure execution, use the List Price element. The list price serves as a starting point for calculating the final price before applying any discounts or adjustments.
Volume and Tier Based Discounts
To calculate the price of a product based on discounts configured according to the quantities purchased, use the Volume Discount or the Tier Discount element.
Manually Discount Product Prices
Manual discounts, also known as discretionary discounts, can be applied to products to provide additional price reductions.
Attribute-Based Discounts
To calculate a product's price based on its associated attributes, use the Attribute-Based Price element.
Bundle-Based Price
Define and manage bundle-based discounts for a group of products that are sold as a unit.
Manage Pricing Using Proration and Subscription Elements
Use the Proration and Subscription elements in Salesforce Pricing to apply time-based pricing when a customer starts, cancels, or changes a subscription mid-cycle. These elements ensure customers are charged only for the time they ‌use your product or service.
Dynamic Pricing With Price Adjustment Matrix
Determine custom discounts and adjustments that go beyond the predefined options provided by Salesforce Pricing using Price Adjustment Matrix element.
Build Pricing Rules with Formula-Based Pricing
Perform functions and mathematical calculations to generate the price of a product. Solve complex pricing scenarios by defining multiple formulas within a single Formula-Based Pricing element.
List Group and List Operation
Efficiently process lists of data and implement complex pricing logic and calculations by enabling filtering, value lookups, and various computations on line items.
Map Context Tag Data Using Assignment Element
Dynamically set or change the values of pricing variables by mapping data between context tags or from a variable directly into a context tag.
Calculate Aggregate Prices for Products
Determine the aggregate prices of a group of products by defining aggregation at multiple line item layers and ensuring pricing is calculated at the configured levels.
Apply Price Rounding Values
Precisely calculate the price of your product using Rounding Values in your pricing procedure to ensure accurate pricing amounts.
Track Price Ranges for Products
Ensure transparent pricing policies and comply with regional directives by tracking a product's minimum and maximum prices over time using the Price Tracking element.
Stop Pricing
Use the Stop Pricing element to stop the execution of the pricing procedure for a particular line item. This element acts as a conditional flow control mechanism. With it, you can create pricing logic where certain conditions trigger an early exit from the pricing procedure.
Price Propagation
Enable complex, hierarchical pricing logic by propagating values across different levels of a transaction from line items to groups and back. Use the Price Propagation element to perform sequential calculations and roll up totals from children to parents.

=== ARTICLE: ind.pricing_pricing_operations_console_sections.htm ===
---
article_id: ind.pricing_pricing_operations_console_sections.htm
title: Understand Your Pricing Data
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_pricing_operations_console_sections.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_operations_console.htm
fetched_at: 2026-09-07
---

# Understand Your Pricing Data

The Revenue Cloud Operations Console has four sections that show you how your pricing data is used.

Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
Console Sections
SECTION	DESCRIPTION
Price Waterfall Storage	Shows the amount of data consumed by the Price Waterfall.
Decision Tables	Shows the number of decision tables that Salesforce Pricing uses to run the pricing processes.
API Calls	Shows the number of API calls you’ve used out of your allotted limit.
Pricing API Executions	Shows the list of logs that are generated after a pricing API is run.
Pricing API Execution Log Details

When a pricing API is run, a log is generated with the following details:

LOG DETAIL	DESCRIPTION
Execution ID	The ID generated every time a pricing API runs.
Created Date	The date the API execution log was created.
Status	The status of the API response, whether it succeeded or failed.
API Endpoint	The unique API endpoint that is called during the execution.
Reference Key	The reference ID that a consuming functional area must pass in the API to search for specific logs in the Revenue Management Operations Console.
Created By ID	The user who executed the API.

=== ARTICLE: ind.pricing_pricing_procedures.htm ===
---
article_id: ind.pricing_pricing_procedures.htm
title: Build Your Pricing Procedures Using Salesforce Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_pricing_procedures.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Build Your Pricing Procedures Using Salesforce Pricing

Pricing procedures are fundamental to all pricing strategies in Revenue Management (formerly Revenue Cloud), enabling businesses to implement dynamic pricing rules and efficiently calculate a product's final net price. They act as the core engine for pricing calculations in Salesforce Pricing, providing a flexible and powerful way to manage both simple and complex pricing scenarios.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Pricing procedures calculate prices using your data. They pull information from wherever the relevant data is, for example, from decision tables, formulas, and custom objects. These procedures are made up of rules, conditions, and formulas, and you can easily configure them to create smart, flexible pricing strategies that change as your business does. Furthermore, they provide a visual representation of calculations using Price Waterfall, simplifying the understanding and management of complex pricing scenarios.

While you technically can create custom pricing procedures, we strongly recommend leveraging the predefined pricing procedures. They are designed to ensure consistency across all your pricing, and deliver accurate pricing calculations every time.

NOTE For help troubleshooting pricing procedure issues, see Troubleshooting Pricing Procedure Issues.
Understand Pricing Elements
Pricing elements are the primary components that make up a pricing procedure in Salesforce Pricing within Revenue Management. They are the building blocks, where each element represents a step in the calculation of a product's final price. Understanding pricing elements is essential for successfully defining and calculating product prices and creating customized pricing strategies.
Prerequisites to Build Pricing Procedures
Before you begin creating pricing procedures and adding elements to them, ensure you have completed these prerequisites. Understanding the fundamentals is crucial for successful implementation and operation of your pricing strategies.
Configure Your Pricing Procedure
Assemble a pricing procedure using pricing elements and ensure accurate pricing for your products.
Simulate and Activate Your Pricing Procedure
Test and validate that your pricing rules and values added to your pricing procedure return accurate results. If your procedure doesn’t work as expected, edit your values or variables, and try again. When you’re satisfied, activate your pricing procedure.
Simple Pricing Procedure Example
Let’s configure and simulate a simple pricing procedure using some common pricing elements to calculate discounts for a laptop.
Use the Default Revenue Management Pricing Procedure
While you can create custom pricing procedures, we strongly recommend using the predefined versions. These predefined procedures bring consistency to your org and deliver accurate calculations.
Automate Context Tag Mapping with Einstein Generative AI
Map context tags with ease and greater accuracy by embedding Einstein generative AI in your pricing elements.
Set Up Parallel Pricing Element Execution
Run multiple pricing procedures concurrently or use parallel processing within a single pricing procedure to ensure faster and more efficient pricing, especially in complex scenarios.
Decision Explainer for Salesforce Pricing
Use Decision Explainer to customize the Salesforce Pricing waterfall structure and generate dynamic explanations for the resulting pricing outcomes.

=== ARTICLE: ind.pricing_pricing_recipes.htm ===
---
article_id: ind.pricing_pricing_recipes.htm
title: Pricing Recipes Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_pricing_recipes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Pricing Recipes Setup

Pricing Recipes in Salesforce Pricing enable you to create and manage detailed pricing strategies. These recipes associate data from selected objects with decision tables to develop comprehensive pricing procedures. Understanding pricing recipes is crucial for successfully leveraging Salesforce Pricing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
How Pricing Recipes Work

A pricing recipe groups decision tables that serve as a data source for your pricing infrastructure. Pricing recipes also provide a one-point configuration for how decision tables are used within procedures.

Salesforce Pricing offers you flexible, data-model independent pricing, retrieving values from any field. You can map a pricing recipe to a decision table, then use Dynamic Output Mapping to define custom outputs for your elements. This provides precise control over pricing calculations. We simplify setup with a predefined recipe and standard decision tables, accelerating your procedure creation.

Select a Pricing Recipe for Your Salesforce Org
Every Salesforce org requires a pricing recipe to define its pricing strategy. When Salesforce Pricing is activated, your org is automatically set up with a predefined recipe, though you can only have one active pricing recipe at a time. This recipe is essential for managing detailed pricing procedures.
Create a Pricing Recipe
Learn how to create a custom pricing recipe to group and associate your custom decision tables, enabling precise control over pricing calculations in your Salesforce org. This task is essential when the predefined recipe doesn't meet your specific business needs. Use the Subtype field to set up the default pricing recipe and decision tables for each cloud, such as Revenue Cloud or Life Sciences Cloud. While building or editing a pricing procedure, element lookups display only the decision tables linked to the default recipe of that procedure's subtype.
Modify Price Adjustment Matrices
Customize your pricing recipes by associating them with decision tables, allowing you to offer customers discounts based on specific conditions.
Sync Decision Tables in a Pricing Recipe
To sync decision tables for a specific pricing recipe:

=== ARTICLE: ind.pricing_pricing_setting.htm ===
---
article_id: ind.pricing_pricing_setting.htm
title: Pricing Setting
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_pricing_setting.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_map_context_tags_in_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Pricing Setting

The Pricing Setting element serves as the initial element for any pricing procedure. They're used to map common variables in a pricing procedure to context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Build the rest of your procedure.

=== ARTICLE: ind.pricing_procedure_output_resolution.htm ===
---
article_id: ind.pricing_procedure_output_resolution.htm
title: Establish Procedure Output Resolution
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_procedure_output_resolution.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_unique_pricing_scenarios.htm
fetched_at: 2026-09-07
---

# Establish Procedure Output Resolution

To select the definitive price for a product when pricing rules generate multiple outcomes, implement Procedure Output Resolution.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

To determine the best price, you must first configure your pricing strategies and then select the option to enable output resolution within a pricing element of a pricing procedure. There are four common best price practices that we can determine using the Procedure Output Resolution feature.

Minimum Price: The lowest price available for the selected product.
Maximum Price: The highest price available for the selected product.
Stack: The application of discounts cumulatively for a product.
Sequence: The application of discounts individually, one after another, for a product.

Procedure output resolution elegantly handles scenarios where a single product has multiple potential prices. This complexity arises whether a product, like a laptop, is listed in several price books with different list prices, or when various adjustments like volume discounts and promotions stack on top of each other to create conflicting calculations. To solve this, you define a single resolution strategy to automatically determine the final price. For instance, a strategy can be set to simply select the lowest (minimum) or highest (maximum) price from all possibilities, or it can apply the adjustments sequentially based on a specific priority, ensuring a predictable and accurate final price is always offered to the customer.

Currently, Salesforce Pricing only supports output resolution in the List Price, Price Tracking, and Price Adjustment Matrix elements. The Stack and Sequence formula options appear only when you use the Price Adjustment Matrix element of a pricing procedure.

NOTE When you enable multi-output resolution for a List Price or Price Tracking element, make sure that every product has a matching entry in the Price Book (Decision Table). If the pricing engine doesn't find any matching records, the element treats this as a configuration error and stops the pricing process for that line item. The element doesn't default to zero or skip the step.
Understand Your Resolution Variables
When you enable output resolution in your pricing element, you’ll see a new Resolution Variables section that will consume the details of the resolution strategy you’ve created. The variables in the Resolution Variables section must be mapped to accurate context tags.
Configure Pricing Resolution Strategies
To set a pricing resolution strategy, create a procedure output resolution record.
Determine the Best Price for a Product Using Pricing Procedures
Use a pricing procedure to determine the best price for a product using a resolution strategy when multiple pricing options exist.

=== ARTICLE: ind.pricing_procedure_plan_framework.htm ===
---
article_id: ind.pricing_procedure_plan_framework.htm
title: Build and Manage Your Procedure Execution
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_procedure_plan_framework.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
fetched_at: 2026-09-07
---

# Build and Manage Your Procedure Execution

Use the Procedure Plan Setup framework to set up your procedures, configure the procedure execution settings, and relate them to a context definition in one centralized location. You can use the predefined templates to build your procedure plan definitions or create a custom definition for your unique use cases.

Procedure plan definitions consist of various sections that you can organize in any order. Each section must have at least one procedure or contain a set of procedures that can be executed based on specific criteria. You can configure these criteria by using default settings or rule-based criteria that best fit your business needs.

Before you create a procedure plan, understand these key terms.

TERM	DESCRIPTION
Procedure Plan Definition	A procedure plan definition combines multiple procedures into a single, unified plan. You can arrange these procedures in any order to meet your business needs. Each plan contains sections and subsections that are configured using simple decision tables or complex, rule-based criteria.
Procedure Plan Section	The various sections added to define a procedure plan. Each section allows you to set up a specific type of procedure.
Phase	A phase represents a stage in your business lifecycle, used to organize procedures and link them to the correct business context.
Resolution Type	A resolution type determines how a procedure is selected for a section of your plan. You can either set it to Default, which allows you to manually pick a procedure from a list, or you can choose Rule-Based, which lets the system automatically select the correct procedure by evaluating a set of predefined criteria.
Read Context Mapping	This mapping is used at the start of the procedure. It reads necessary input data from a Salesforce object such as Quote or Order the to the context definition to set the context for pricing logic execution.
Save Context Mapping	This mapping is used at the end of the procedure. It saves the calculated results from the context definition such as prices or discounts back to the fields in the associated Salesforce objects storing in the final output.
IMPORTANT
Before you begin creating your procedure plan definitions, you must enable Context Service in your org. To enable Context Service, go to Setup, in the Quick Find box, search and select Context Service Settings. Turn on Context Definitions.
Understand the Order of Execution for Place Sales Transaction
When you create or update a quote or order using the Place Sales Transaction API, Revenue Management (formerly Revenue Cloud)processes the request through a defined order of execution. This order describes how configuration, pricing, Apex hooks, and automation run during transaction processing. Understanding this order helps you determine where pricing logic runs and how context data is processed when using Place Sales Transaction.
Create Procedure Plans
To create a flexible and comprehensive workflow that adapts to your business needs, use a Procedure Plan Definition to combine and sequence individual procedures into a single, unified plan. You can start quickly with a predefined template or customize one from scratch to meet your unique requirements.
Customize Your Procedure Plans With Apex Hooks
To support unique pricing scenarios, add custom Apex logic to your pricing procedure plans. You can use Apex hooks to apply custom business logic that modifies the pricing context after a quote line is configured. Use an Apex prehook to adjust pricing based on product attributes before it's priced, and an Apex posthook to handle pricing changes for groups and other Quote object elements after pricing. When a sales rep configures a product or changes a group of quote line items, the pricing procedure plan changes the pricing based on the instructions in Apex.
Use the Procedure Plan Framework
To ensure your procedures run in the correct order and pricing is applied consistently to a quote, create a new procedure plan.
Export and Import Procedure Plans
Package procedure plans to export and import them across Salesforce orgs.
Procedure Plan Limits
Don't stitch multiple pricing procedures together within a single procedure plan. Sequencing multiple procedures can result in data loss and calculation errors. If you need to configure multiple procedures sequentially, consider these limitations.

=== ARTICLE: ind.pricing_procedure_plan_limits.htm ===
---
article_id: ind.pricing_procedure_plan_limits.htm
title: Procedure Plan Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_procedure_plan_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_plan_framework.htm
fetched_at: 2026-09-07
---

# Procedure Plan Limits

Don't stitch multiple pricing procedures together within a single procedure plan. Sequencing multiple procedures can result in data loss and calculation errors. If you need to configure multiple procedures sequentially, consider these limitations.

The Price Waterfall displays execution results for only the last pricing procedure in the sequence. Sales reps can't view the end-to-end history of a line item. The final waterfall view overwrites or loses access to the logic, calculations, and intermediate values from the first procedure, making it difficult to explain the final price derivation.
Derived pricing calculations don't capture the complete pricing context when a contributing product's calculation spans across multiple procedures. For example, a product receives a volume discount in Procedure 1 and an attribute-based discount in Procedure 2. If the Derived Price element is in Procedure 1, it calculates the price based only on the Net Unit Price available at the end of Procedure 1. The calculation ignores the attribute discount applied in Procedure 2 because context isn't shared between procedures.
For bundled products configured with an Inclusive Price, the instruction to skip pricing doesn't persist between procedures. In the first procedure, the Bundle Based Adjustment element sets the child item's list price to zero and skips further calculations. However, when the quote moves to the second procedure, the line item loses the flag to skip calculation. Consequently, the second procedure treats the child item as a standard line item and sometimes incorrectly applies manual discounts or other adjustments.

Workaround: Configure the second procedure to check if InclusivePrice is true and stop pricing for those lines.

When parallelization is enabled, the pricing procedure caches metadata about custom tag mappings during activation. If you modify custom tag mappings in a rule library version after a procedure is activated, deactivate and reactivate the procedure to refresh this metadata. Otherwise, the procedure might apply promotions incorrectly during execution.

=== ARTICLE: ind.pricing_promotion_execution_element.htm ===
---
article_id: ind.pricing_promotion_execution_element.htm
title: Promotion Execution Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_promotion_execution_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_unique_pricing_scenarios.htm
fetched_at: 2026-09-07
---

# Promotion Execution Element

To apply promotions, add the Promotion Execution element to your pricing procedure. This element connects Global Promotions Management with Revenue Management, executing applicable promotions for your transaction line items.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

To learn how to use the element within a pricing procedure, see Configure Your Pricing Procedure for Promotions in Revenue Cloud.

=== ARTICLE: ind.pricing_proration_variables.htm ===
---
article_id: ind.pricing_proration_variables.htm
title: Learn About the Proration Multiplier
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_proration_variables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_pricing_proration.htm
fetched_at: 2026-09-07
---

# Learn About the Proration Multiplier

The proration multiplier is used to adjust the price of a product or service based on a customer’s usage. This multiplier can be calculated when a customer subscribes to a service partway through a pricing period or when there are changes to the service, such as upgrades, downgrades, or cancellations. The multiplier calculation is based on how long the customer uses the service during the pricing period.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
TIP Salesforce Pricing supports month-plus-day ‌proration types for any frequency term.

Here's how Salesforce Pricing calculates prorated subscription costs.

SUBSCRIPTION PRORATE PRECISION	CALCULATE THE PRORATE MULTIPLIER	EXAMPLE
Month	Calculate the duration of the subscription term in full months and divide it by the product’s subscription term. If the duration includes a partial month, Salesforce Pricing adjusts the total number of months to the nearest whole number.	

A service costs $50 per month. If a customer subscribes on the 15th of the month and the month ends on the 30th, the customer only uses the service for half the month (15 days out of 30).

To calculate the proration multiplier, use this formula - Proration Multiplier = Time Used/ Total Time in Period

In this case: 15 days/ 30 days = 0.5

To calculate the adjusted price: $50 X 0.5 = $25.

=== ARTICLE: ind.pricing_quarterly_proration_examples.htm ===
---
article_id: ind.pricing_quarterly_proration_examples.htm
title: Quarterly Proration Examples
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_quarterly_proration_examples.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_variables.htm
fetched_at: 2026-09-07
---

# Quarterly Proration Examples

Demonstrates how the system calculates pricing based on 3-month billing intervals.

Base Transaction Details (All Examples)
Effective From: 2025-03-28
Effective To: 2026-02-04
Total Duration: 314 Days
Start Proration Day: 5 (Used for DayOfPeriod examples)
Start Proration Month: February (Used for DayOfPeriod examples)
Proration Period: Quarterly
List Price: $200.00

1. Start Proration Period: AlignToCalendar (1st of Month) and Allow Partial Proration Periods: True

Calculation Logic: Periods align with calendar quarters (Jan-Mar, Apr-Jun, etc.). Average days in a quarter = 91.25.
Period 1 (Partial - Q1): 1-Jan-2025 to 31-Mar-2025
Utilized Duration: 28-Mar-2025 to 31-Mar-2025 (4 Days)
Pricing Term Count: 4 / 91.25 (Avg) = 0.043836
Period 2 (Full - Q2): 1-Apr-2025 to 30-Jun-2025
Pricing Term Count: 1.0
Period 3 (Full - Q3): 1-Jul-2025 to 30-Sep-2025
Pricing Term Count: 1.0
Period 4 (Full - Q4): 1-Oct-2025 to 31-Dec-2025
Pricing Term Count: 1.0
Period 5 (Partial - Q1): 1-Jan-2026 to 31-Mar-2026
Utilized Duration: 1-Jan-2026 to 4-Feb-2026 (35 Days)
Pricing Term Count: 35 / 91.25 (Avg) = 0.383562
Total Pricing Term Count:: 0.043836 + 3.0 + 0.383562 = 3.427 (approx 3.436464 using exact day counts per specific quarter logic).
Price: $200 x 3.436464 = $687.29

2. Start Proration Period: AlignToCalendar (1st of Month) and Allow Partial Proration Periods: False

Calculation Logic: The term touches 5 distinct calendar quarters. Each touched quarter counts as 1.0 unit.
Period 1: Q1 2025 (Touched)
Period 2: Q2 2025 (Full)
Period 3: Q3 2025 (Full)
Period 4: Q4 2025 (Full)
Period 5: Q1 2026 (Touched)
Price: $200 x 5.0 = $1,000.00

=== ARTICLE: ind.pricing_record_sharing_pricing.htm ===
---
article_id: ind.pricing_record_sharing_pricing.htm
title: Configure Record Sharing for Salesforce Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_record_sharing_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Configure Record Sharing for Salesforce Pricing

For runtime users to access the data created by product designers or catalog admins, set up record sharing for all Salesforce Pricing objects. This configuration is crucial for the seamless execution of pricing processes within Salesforce.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create and edit sharing settings:	

Manage Sharing

From Setup, in the Quick Find box, enter Security, and then select Sharing Settings.
Click Edit.
Set Public Read Only as the organization-wide defaults for your users for all Pricing objects based on your security requirements.
Ensure that all Runtime users have Read access to these objects:
Price Book - View Only
Expression Set (for Pricing Procedures) - Public Read Only
Price Adjustment Schedule - Public Read Only
Save your changes.
NOTE Pricing API access is managed via permission sets, which grant read access to entities and allow execution of pricing logic. This makes sharing rules optional for API calls, though sharing rules are still needed for UI access. Run time users have Run Decision Matrices and Run Expression Sets permissions by default.

This completes the basic setup for Salesforce Pricing. To enable other features, see Understand Advanced Pricing Setup.

=== ARTICLE: ind.pricing_roll_up_pricing_using_the_aggregate_price_element.htm ===
---
article_id: ind.pricing_roll_up_pricing_using_the_aggregate_price_element.htm
title: Roll Up Pricing Using the Aggregate Price Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_roll_up_pricing_using_the_aggregate_price_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_aggregate_price_element.htm
fetched_at: 2026-09-07
---

# Roll Up Pricing Using the Aggregate Price Element

Calculate the total price of a group of products using the Roll Up Price option using the Aggregate Price element. When you enable roll up price, the element first determines the price of each child product, and then, adds the total to a parent product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time

Let's look at a scenario where we want to roll up the prices of individual (child) products into the parent product of a bundle. With the Roll Up Price feature, we can determine the total price of the entire bundle, both child and parent products, using the Aggregate element. Here, the parent bundle is LaptopPro bundle and the child products are laptop and mouse.

IMPORTANT When calculating the roll up price for a group of products, you can't use the Write Back condition to override the pricing output of a variable.
Configure a pricing procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Aggregate Price element.
Select Roll Up Price.
Set the variable for the Parent Product as ParentReference.
Specify the formula variables.
Formula: SUM (NetUnitPrice)
Output Variable: ItemNetTotalPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your products and click Simulate again.

Aggregate pricing changes can't be viewed in the waterfall view. However, the JSON output provides insight into how the aggregate price of the bundle of products was calculated. Based on our example, the aggregate price of products belonging to the LaptopPro Bundle is the total price of the Laptop, the Mouse, and the Laptop Pro Bundle itself.

The sum of these products ($1,049 + $7.99 + $1,150) is stored in the ItemNetTotalPrice variable, which displays the amount as $2,206.99. This confirms that your procedure is working as expected.

=== ARTICLE: ind.pricing_rounding_values.htm ===
---
article_id: ind.pricing_rounding_values.htm
title: Apply Price Rounding Values
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_rounding_values.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Apply Price Rounding Values

Precisely calculate the price of your product using Rounding Values in your pricing procedure to ensure accurate pricing amounts.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

Rounding ensures that financial calculations use the correct number of decimal places for the currency, rounding results up or down based on the applied rounding rule. The rounding rules applied are:

Round Up: This rule rounds the currency value of an item to the nearest higher value. For example, if a pen costs US$1.60, applying this rule adjusts the price to $2.
Round Down: This rule rounds the currency value of an item to the nearest lower value. For example, if a pen costs $1.60, applying this rule adjusts the price to $1.
Half Up: This rule rounds the currency value of an item to the nearest number based on its decimal value. For example, if a pen costs $1.45 and you select the Half Up rule, the price adjusts to $1.50. However, if the pen costs $1.20, the price adjusts to $1.00.

For single-currency orgs, the Rounding Values element sets the rounding precision by using the precision input parameter. If no precision value is passed, the element returns the input value unchanged, without rounding. If multicurrency is enabled, the Rounding Values element ignores the precision input parameter and automatically applies the decimal places defined in your Manage Currencies settings. The element uses the decimal places defined for the currency passed through CurrencyIsoCode context. If CurrencyIsoCode isn't passed, the element automatically applies the decimal places defined for each currency in your Manage Currencies settings. See Manage Multiple Currencies.

In addition to setting overall precision, the Rounding Values element also plays a crucial role in determining the final currency outputs from preceding pricing elements, such as Manual Discount and Volume Discount.

Use the Rounding Values Element
Use the Rounding Values element to ensure that the output of any pricing element in a pricing procedure is rounded to the specified decimal place.

=== ARTICLE: ind.pricing_salesforce_pricing.htm ===
---
article_id: ind.pricing_salesforce_pricing.htm
title: Design Your Pricing Model in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
fetched_at: 2026-09-07
---

# Design Your Pricing Model in Revenue Management

Salesforce Pricing provides a unified platform for consistent, compliant, and accurate pricing for your products. Businesses can define standard prices for their products and apply discounts through price adjustments for a range of scenarios including volume discounts, subscription pricing, bundle pricing, and more.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.

Sales reps benefit from real-time access to precise pricing and the ability to directly apply relevant discounts, giving them clear visibility into the final price. This is especially valuable for negotiating large quotes and winning complex deals. Sales reps also get the information they need to explain quotes to customers through a detailed price adjustment log (the price waterfall), enhancing transparency and trust.

Salesforce Pricing also offers prebuilt integrations with other Revenue Management (formerly Revenue Cloud)components like Transaction Management, and allows for custom pricing actions and third-party API integrations.

To get started with Salesforce Pricing, refer to these resources. We recommend working through these sections in order.

Begin Using Salesforce Pricing
Enable Salesforce Pricing to efficiently set up, manage, and implement pricing strategies. Tailor the experience of using Salesforce Pricing for all users using permission sets to give them precise access to what they need.
Salesforce Pricing Basic Setup
Salesforce Pricing provides the key tools to manage your pricing infrastructure. To leverage these tools effectively, you must first complete the basic setup detailed in this section. This process represents our recommended base configuration and is a prerequisite for building any custom solution. It ensures essential pricing configuration can be transferred, procedures can be customized, and data can be synced for accuracy. Complete all of the following steps before continuing on to design your pricing solution.
Salesforce Pricing Advanced Setup
Salesforce Pricing provides advanced setup options to customize and extend its core functionalities that is crucial for leveraging the product's full power and tailoring it to specific business needs.
Considerations for Importing and Exporting Pricing Data
Use a packaged file to import and export pricing metadata from one org to another, including pricing recipes, decision tables, context definitions, and pricing procedures. These metadata components are crucial for ‌pricing processes, where pricing procedures use recipes for accurate calculations.
Cost Books and Price Books
Track the expenses associated with manufacturing a product in a cost book, and record the product's selling price in a price book. You can have multiple price books and cost books in your Salesforce org.
Explore Price Adjustment Schedules
Implement dynamic pricing strategies by automating price calculations and adjustments based on various factors like quantity or product attributes. Build flexible pricing models that optimize revenue and adapt to specific market conditions or customer needs.
Build Your Pricing Procedures Using Salesforce Pricing
Pricing procedures are fundamental to all pricing strategies in Revenue Management (formerly Revenue Cloud), enabling businesses to implement dynamic pricing rules and efficiently calculate a product's final net price. They act as the core engine for pricing calculations in Salesforce Pricing, providing a flexible and powerful way to manage both simple and complex pricing scenarios.
Use Pricing Elements in Pricing Procedures
Pricing elements are the fundamental building blocks used to construct a pricing procedure. Use these elements to define how prices are calculated and applied in Revenue Management (formerly Revenue Cloud).
Unique Pricing Scenarios
Learn how complex pricing scenarios, from product interdependencies to honoring long-term customer agreements, impact sales efficiency and customer satisfaction. Discover how Salesforce Pricing provides the sophisticated capabilities needed to manage these unique challenges and drive revenue.
Access Your Pricing Information
View your product pricing either in a simple list view or using custom grid components making it easier to analyze and compare data. Use the discount calendar to show all applied discounts for a product.
Salesforce Pricing Limits
Review the default limits for Salesforce Pricing’s components and their usage. To modify the set default values, ask your Salesforce administrator to raise a support ticket.

=== ARTICLE: ind.pricing_semi_annual_proration_examples.htm ===
---
article_id: ind.pricing_semi_annual_proration_examples.htm
title: Semi-Annual Proration Examples
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_semi_annual_proration_examples.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_variables.htm
fetched_at: 2026-09-07
---

# Semi-Annual Proration Examples

Demonstrates how the system calculates pricing based on 6-month billing intervals.

Base Transaction Details (All Examples)
Effective From: 2025-03-28
Effective To: 2026-02-04
Total Duration: 314 Days
Start Proration Day: 5 (Used for DayOfPeriod examples)
Start Proration Month: February (Used for DayOfPeriod examples)
Proration Period: Semi-Annual
List Price: $400.00

1. Start Proration Period: DayOfPeriod (Day 5) and Allow Partial Proration Periods: True

Calculation Logic: Periods are 6 months long, anchored to Feb 5th.
Period 1 (Partial): 5-Feb-2025 to 4-Aug-2025
Total Days in Period: 181
Utilized Duration: 28-Mar-2025 to 4-Apr-2025 (130 Days)
Pricing Term Count: 130 / 181 = 0.718232
Period 2 (Full): 5-Aug-2025 to 4-Feb-2026
Utilized Duration: 5-Aug-2025 to 4-Feb-2026 (Full Period)
Pricing Term Count: 1.0
Total Pricing Term Count: 0.718232 + 1.0 = 1.718232
Price: $400 x 1.718232 = $687.29

2. Start Proration Period: DayOfPeriod (Day 5) and Allow Partial Proration Periods: False

Calculation Logic: The term spans parts of 3 distinct 6-month blocks anchored to Feb 5.
Period 1: Feb '25 - Aug '25 (Touched) = 1.0
Period 2: Aug '25 - Feb '26 (Touched) = 1.0
Period 3: Feb '26 - Aug '26 (Touched, because the term ends on Feb 4, effectively completing the previous block, but systems often count the boundary touch. Note: Based on the provided user text saying "3.0", the logic assumes the term touches a 3rd period or the system rounds up heavily. Based on the dates (Mar '25 to Feb '26), it sits primarily in 2 periods. If 3.0 is the result, it implies the system sees the end date falling into a 3rd cycle or counts the anchor start/end inclusively across boundaries).
Price: $400 x 3.0 = $1,200.00

=== ARTICLE: ind.pricing_set_default_pricing_procedure.htm ===
---
article_id: ind.pricing_set_default_pricing_procedure.htm
title: Select a Pricing Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_set_default_pricing_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Select a Pricing Procedure

To apply pricing rules and logic to calculate the final net price of a product, you must first clone a predefined pricing procedure available with Salesforce Pricing or build a custom one. This is necessary because Salesforce ships a predefined template, not an executable procedure, meaning templates can’t be directly configured for use.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create, update, delete, and clone pricing procedures:	Salesforce Pricing Design Time User
IMPORTANT Before you start working with pricing procedures, you'll need to understand the different pricing procedures used in Revenue Management.
The pricing procedure selected in Product Discovery Settings is used to calculate the list price of a product.
The pricing procedure selected in Salesforce Pricing Setup is used to make headless calls only.
The pricing procedure selected in Revenue Settings is used to determine accurate pricing for quotes and orders.

Here are some important things to remember when you're cloning your procedure.

When saving the cloned expression set as a new pricing procedure, you can assign a custom context definition.
You can only provide a version name and version number to a cloned expression set when you save it as a new pricing procedure version.
The cloned procedure's start date must be later than the Effective From date of it's context definition.
Let's start by cloning an expression template.
From the App Launcher, find and select Expression Set Templates.
Select the expression set template that you want to clone.
NOTE To price quotes and orders, use the Revenue Management Default Pricing Procedure.
Click Save As.
The template can be cloned and saved as a new pricing procedure or a new version of a pricing procedure. You can find the newly cloned pricing procedure in the Pricing Procedures list.
To select a pricing procedure in the Product Discovery Settings page.
From Setup, in the Quick Find box, enter Product Discovery, and then select Product Discovery Settings. 
In the Select a Pricing Procedure section, select the pricing procedure.
To select a pricing procedure in the Salesforce Pricing Setup page.
From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup. 
In the Select a Pricing Procedure section, select the pricing procedure.
To set a default pricing procedure for your Revenue Management org, do the following: 
From Setup, in the Quick Find box, enter Revenue Settings, and then select Revenue Settings..
In the Set Up Salesforce Pricing section, select the pricing procedure.
SEE ALSO
Pricing Procedures
Configure Your Pricing Procedure
Simulate and Activate Your Pricing Procedure
Create Procedure Plan Definitions by Using Templates

=== ARTICLE: ind.pricing_set_price_history_tracking.htm ===
---
article_id: ind.pricing_set_price_history_tracking.htm
title: Configure Price Tracking History
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_set_price_history_tracking.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_tracking.htm
fetched_at: 2026-09-07
---

# Configure Price Tracking History

Track the minimum and maximum prices of a product over a period to help your users make well-informed buying decisions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To turn on price tracking history:	Salesforce Pricing Admin
IMPORTANT Avoid frequent changes to this setting, as it resets the daily jobs calculating price history. Altering the duration can negatively impact price history and product price calculations.
From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
Select the options to enable minimum and maximum price.
Select your duration in days.
You can track a product's price for a maximum of 30 days, with a default of 7.

=== ARTICLE: ind.pricing_set_price_waterfall_persistence.htm ===
---
article_id: ind.pricing_set_price_waterfall_persistence.htm
title: Set Price Waterfall Persistence
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_set_price_waterfall_persistence.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_price_waterfall_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Set Price Waterfall Persistence

Enhance transparency and auditability in your pricing processes by enabling Price Waterfall Persistence. This feature stores detailed logs of each pricing calculation step, making it easier to understand and manage your pricing strategies.

From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
Turn on Price Waterfall Persistence.

=== ARTICLE: ind.pricing_set_up_einstein_generative_ai_for_salesforce_pricing.htm ===
---
article_id: ind.pricing_set_up_einstein_generative_ai_for_salesforce_pricing.htm
title: Set Up Einstein Generative AI for Salesforce Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_set_up_einstein_generative_ai_for_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_einstein_generative_ai_for_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Set Up Einstein Generative AI for Salesforce Pricing

Enable Einstein generative AI and give users the required permissions to access the generative AI capabilities.

From Setup, in the Quick Find box, enter Einstein Setup, and then select Einstein Setup.
Turn on Einstein.

=== ARTICLE: ind.pricing_set_up_price_logs_capture.htm ===
---
article_id: ind.pricing_set_up_price_logs_capture.htm
title: Set Up Price Logs Capture
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_set_up_price_logs_capture.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Set Up Price Logs Capture

To collect logs captured by pricing APIs, turn on Price Logs Capture.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To turn on price logs capture:	Salesforce Pricing Design Time

The pricing logs provide a comprehensive view of the pricing procedures being executed and are helpful in measuring the performance of the pricing APIs and for troubleshooting any issues.

When you enable Price Logs Capture, the Price Waterfall and Price Waterfall Persistence options are automatically enabled because the generated price logs are derived from waterfall data.

From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
Turn on Price Logs Capture.

=== ARTICLE: ind.pricing_set_up_price_waterfall_salesforce_pricing.htm ===
---
article_id: ind.pricing_set_up_price_waterfall_salesforce_pricing.htm
title: Set Up Price Waterfall
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_set_up_price_waterfall_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Set Up Price Waterfall

To ensure transparency and accuracy in final product price determination, utilize Price Waterfall to understand and verify your pricing calculations at each step. This is particularly valuable when tracking complex pricing structures, including volume discounts and other tiered adjustments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To turn on price waterfall and price waterfall persistence:	Salesforce Pricing Design Time
Configure Price Waterfall
Understand the reasons behind every step of your pricing process by using Price Waterfall. By configuring waterfall, you get a detailed breakdown of every addition or deduction, giving you clear understanding of your pricing process.
Set Price Waterfall Persistence
Enhance transparency and auditability in your pricing processes by enabling Price Waterfall Persistence. This feature stores detailed logs of each pricing calculation step, making it easier to understand and manage your pricing strategies.
Understand the Setup Objects Used for Price Waterfall
Price Waterfall uses setup objects to capture logs for how a pricing procedure ran, making it easy for your users to explain and check pricing calculations at each step. For example, pricing analysts can check the number of discounts applied at various tiers while calculating volume discounts.

=== ARTICLE: ind.pricing_set_up_salesforce_pricing.htm ===
---
article_id: ind.pricing_set_up_salesforce_pricing.htm
title: Salesforce Pricing Basic Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_set_up_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Salesforce Pricing Basic Setup

Salesforce Pricing provides the key tools to manage your pricing infrastructure. To leverage these tools effectively, you must first complete the basic setup detailed in this section. This process represents our recommended base configuration and is a prerequisite for building any custom solution. It ensures essential pricing configuration can be transferred, procedures can be customized, and data can be synced for accuracy. Complete all of the following steps before continuing on to design your pricing solution.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Configure Decision Tables
Decision tables form the foundation of your pricing logic. Salesforce Pricing evaluates complex rules and looks up specific values, such as list prices, discounts, or volume tiers, based on defined input criteria. Configure standard decision tables that pull data directly from your Salesforce objects.
Pricing Recipes Setup
Pricing Recipes in Salesforce Pricing enable you to create and manage detailed pricing strategies. These recipes associate data from selected objects with decision tables to develop comprehensive pricing procedures. Understanding pricing recipes is crucial for successfully leveraging Salesforce Pricing.
Select a Pricing Procedure
To apply pricing rules and logic to calculate the final net price of a product, you must first clone a predefined pricing procedure available with Salesforce Pricing or build a custom one. This is necessary because Salesforce ships a predefined template, not an executable procedure, meaning templates can’t be directly configured for use.
Sync Pricing Data in Revenue Management
Regularly sync your pricing data in Salesforce Revenue Management to ensure the latest information is available in decision tables that are mapped to a pricing recipe and have their usage type set to Pricing.
Set Up Price Waterfall
To ensure transparency and accuracy in final product price determination, utilize Price Waterfall to understand and verify your pricing calculations at each step. This is particularly valuable when tracking complex pricing structures, including volume discounts and other tiered adjustments.
Set Up Price Logs Capture
To collect logs captured by pricing APIs, turn on Price Logs Capture.
Configure Salesforce Pricing Objects
To optimize Salesforce Pricing, configure the page layouts for Product, Price Book Entry, and Price Adjustment Schedule objects to ensure the proper display and functionality of pricing-related fields and related lists, thereby guaranteeing accurate product and service pricing and streamlining sales processes.
Configure Record Sharing for Salesforce Pricing
For runtime users to access the data created by product designers or catalog admins, set up record sharing for all Salesforce Pricing objects. This configuration is crucial for the seamless execution of pricing processes within Salesforce.

=== ARTICLE: ind.pricing_set_up_your_discovery_procedure.htm ===
---
article_id: ind.pricing_set_up_your_discovery_procedure.htm
title: Configure a Discovery Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_set_up_your_discovery_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_discovery_procedure_for_pricing.htm
fetched_at: 2026-09-07
---

# Configure a Discovery Procedure

To calculate a product's derived price, configure a discovery procedure with the elements required to gather all contributing factors.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To create discovery procedures:	

Salesforce Pricing Design Time User


To run discovery procedures:	Salesforce Pricing Run Time
From the App Launcher, find and select Discovery Procedures.
Click New.
Specify these details.
Enter a name and then press Tab to autopopulate the API name.
Select Pricing Discovery as the usage type.
Associate the discovery procedure with a context definition.
In all our examples, we’ll use the SalesTransactionContext context definition. We also recommend using the predefined Default Discovery Procedure, or you can modify it with a context definition of your choice.
Save your changes.
On the Details tab, in the Discovery Procedure Versions section, click the discovery procedure version that you want to work on.
The Discovery Procedure Builder opens in a new tab.
To add your discovery elements, click .
If you want to map commonly used input variables, such as line items or net unit price, add the Discovery Settings element, followed by the Map Line Item element. These are optional.
Add the Fetch Pricing Rules element and enter your values.
Ensure that the Fetch Pricing Rules element is the first element in your pricing procedure.
Add the Map Products element.
The Map Products element uses the fixed input variables in the Fetch Pricing Rules element.
For example, to derive the price of a contributing product within a single bundle in the quote line, use the Map Product element. Validate that the contributing product's parent bundle has the same ID by checking if the RootItem matches. If the contributing products share the same root product, then the derived price for the product is calculated.
If your derived price record has set the pricing scope as Non-Transactional or Both, add the Asset Discovery element and map your variables.
Non-transactional scope indicates that you can derive a product's derived from assets.
Click , and enter 1 as the rank number.
NOTE When more than one enabled version matches a discovery procedure, choose the version with the highest rank. For example, if two enabled versions have rank values set to 1 and 2, choose the version with rank 2.
Click , select Include in Output, and save your pricing procedure.
Save your changes.
Simulate your procedure to verify the queried data.
On the Input tab, enter your values and click Simulate again.
Activate your discovery procedure.

=== ARTICLE: ind.pricing_simple_pricing_procedure_example.htm ===
---
article_id: ind.pricing_simple_pricing_procedure_example.htm
title: Simple Pricing Procedure Example
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_simple_pricing_procedure_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Simple Pricing Procedure Example

Let’s configure and simulate a simple pricing procedure using some common pricing elements to calculate discounts for a laptop.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User
To use pricing procedures:	Salesforce Pricing Run Time User

To follow this example, make sure your organization is set up with the following.

Decision tables
Context Service enabled, with a defined context definition. You can also use one from Revenue Management.
Two simple products called Laptop and Printer configured with necessary attributes and classifications. To learn how to create a simple product see, Create Simple Products.
Added the products as a price book entries to a price book. To learn more about price books and price book entries, see Cost Books and Price Books.
The required price adjustment schedule record created. To create a price adjustment schedule record, see Create Price Adjustment Schedules.
A constant resource created. To learn how to create constant resources, see Create Constant Resources.
Create a pricing procedure and associate it with a context definition. Ensure that the usage type is set to Pricing and save your procedure. Provide these details:
Name: Laptop Sales
Usage Type: Pricing
Context Definition: SalesTransactionContext
Open your pricing procedure and add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice
Subtotal: ItemNetTotalPrice
Let’s start by fetching the base price of the laptop using the List Price element. Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product:Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice. You can also leave this variable blank because you've already mapped the Subtotal variable in step 2.
To provide discounts on laptops when they’re purchased in bulk, add the Volume Discount element.
To the Volume Discount element, search for and add the Volume Discount Entries decision table and map these variables.
Input Rule Variables
Price Adjustment Schedule: VolumePriceAdjustmentScheduleId
Lower Bound: LineItemQuantity
Upper Bound: LineItemQuantity
Product: Product
Product Selling Model: ProductSellingModel
Effective From: EffectiveFrom
Effective To: EffectiveFrom
Input Variables
Quantity: LineItemQuantity
Input Unit Price: ListPrice
To empower sales reps to apply discretionary discounts and encourage sales of laptops to longtime customers, use the Manual Discount element. This discount type can be applied as a percentage or an amount. Map these input variables.
Adjustment Type: AdjustmentType
Adjustment Value: AdjustmentValue
Quantity: LineItemQuantity
Input Unit Price: NetUnitPrice
To calculate the aggregate price of a group of products, define the Aggregate Price element. In our example, let’s calculate the aggregate price of a laptop and printer at the line item level.
In the Group By field, search for and select ProductSellingModel to group both the laptops and printers.
Set a condition to decide the product quantities. Here, set:
Where: LineItemQuantity
Operator: Greater Than
Output Value: 2
Enter the aggregation formula as:
Formula: SUM(ItemNetTotalPrice)
Output Variable: NetUnitPrice
Click  and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your laptop product and click Simulate again.
The price waterfall shows the volume and manual discounts used to calculate the final price of the laptop and printer, confirming that your procedure is working as expected. 
IMPORTANT If your simulation fails or you can't see the waterfall view, we recommend refreshing your decision tables and verifying if the input values entered are accurate.

Looking for a hands-on way to practice with Pricing Procedures? We've got just the thing! We recommend checking out this Trailhead resource: Price Management with Revenue Management.

=== ARTICLE: ind.pricing_simulate_activate_pricing_procedure.htm ===
---
article_id: ind.pricing_simulate_activate_pricing_procedure.htm
title: Simulate and Activate Your Pricing Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_simulate_activate_pricing_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Simulate and Activate Your Pricing Procedure

Test and validate that your pricing rules and values added to your pricing procedure return accurate results. If your procedure doesn’t work as expected, edit your values or variables, and try again. When you’re satisfied, activate your pricing procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User
To use pricing procedures:	Salesforce Pricing Run Time User
Open a pricing procedure in the Pricing Procedure builder.
Add your elements, map them to the appropriate tags, choose a rank, enable the option to include the output, and then save your pricing procedure.
Click Simulate.

To view the Simulate button, users may need to deactivate, save, and reactivate procedures that include List Price or Price Adjustment Matrix elements.

Select an input mode to pass simulation data to the pricing procedure.
Simplified: Enter values for the variables defined in the pricing procedure.
Advanced: Enter the values for the variables in JSON format in the JSON Input box. Modify the values directly or download the JSON input file, modify its values, and paste it back in the box.
To verify if the pricing procedure can be simulated with various context definition data, select a context definition from the list.
If you want to pass line item details automatically as input variables, select Auto-fill line items and provide the object ID.
NOTE Only tags with sObject mapping and a corresponding field value in the record will auto-fill the line items.
You can locate the value of your variable by going to the associated record. For example, to locate a price adjustment schedule ID, open the price adjustment schedule record page. The price adjustment schedule ID is shown in the browser’s URL.
If you make more edits, click Simulate again.
The Waterfall View shows every step of the pricing calculation from the list price, the discounts applied, and the changes or taxes on the product to arrive at its final net price. If you’ve set up profile access, only the profiles that you selected at the element-level can see the pricing information displayed.
When you’re happy with the simulation result, click Activate.
SEE ALSO
Set Up Price Waterfall in Salesforce Pricing

=== ARTICLE: ind.pricing_standard_pricing_actions.htm ===
---
article_id: ind.pricing_standard_pricing_actions.htm
title: Standard Pricing Actions
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_standard_pricing_actions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_action_parameters.htm
fetched_at: 2026-09-07
---

# Standard Pricing Actions

To view the pricing action button on the object’s record page, edit the page layout of the object.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Add the Calculate Price Button
To make the standard button for pricing action visible on your object’s record page, configure the object’s page layout from Object Manager.
Calculate Price of a Product by Using the Standard Price Action
After you add the Calculate Price button to the selected object, you can calculate the price of a product from the object’s record page.

=== ARTICLE: ind.pricing_stop_pricing.htm ===
---
article_id: ind.pricing_stop_pricing.htm
title: Stop Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_stop_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Stop Pricing

Use the Stop Pricing element to stop the execution of the pricing procedure for a particular line item. This element acts as a conditional flow control mechanism. With it, you can create pricing logic where certain conditions trigger an early exit from the pricing procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

When a line item reaches a Stop Pricing element:

The pricing procedure stops processing that line item immediately.
No subsequent pricing elements are executed for that line item.
The current pricing values are used as the final price.
During simulation, the Waterfall view shows where the pricing procedure stopped.
NOTE Stop Pricing only affects the specific line item that hits it. Other line items in the same transaction continue through the full pricing procedure normally.
When to Use Stop Pricing

Use the Stop Pricing element to implement exclusive pricing logic where certain conditions should prevent further pricing calculations.

=== ARTICLE: ind.pricing_subscription_pricing_proration.htm ===
---
article_id: ind.pricing_subscription_pricing_proration.htm
title: Manage Pricing Using Proration and Subscription Elements
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_subscription_pricing_proration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_element.htm
fetched_at: 2026-09-07
---

# Manage Pricing Using Proration and Subscription Elements

Use the Proration and Subscription elements in Salesforce Pricing to apply time-based pricing when a customer starts, cancels, or changes a subscription mid-cycle. These elements ensure customers are charged only for the time they ‌use your product or service.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

The Subscription element calculates the total subscription price based on the input unit price and the pricing term count. When a subscription starts, changes, or ends mid-period, the Proration element calculates a multiplier based on the portion of the period used. This multiplier then adjusts the subscription price, ensuring customers are only priced based on their subscription time.

For example, if a customer starts a subscription to a software service in the middle of a pricing period, they are charged only for the time they ‌use it. If the pricing period is monthly and the customer begins their subscription on the 15th of the month, they are charged only for the remaining 15 days. The full monthly charge is then applied on the first day of the next month.

Configure Proration Settings
Set custom pricing term values to calculate product prices based on your customer's subscription length.
Learn About the Proration Multiplier
The proration multiplier is used to adjust the price of a product or service based on a customer’s usage. This multiplier can be calculated when a customer subscribes to a service partway through a pricing period or when there are changes to the service, such as upgrades, downgrades, or cancellations. The multiplier calculation is based on how long the customer uses the service during the pricing period.
Common Proration Examples
These examples demonstrate how various proration settings impact the final subscription price for a product with a Selling Model Type of TermDefined.
Configure the Proration and Subscription Element
To calculate time-based pricing, use the Proration and Subscription elements.
Create a Proration Policy for a Subscription
Manage charges for partial subscription periods and choose whether remainders are applied to the first or last pricing period.

=== ARTICLE: ind.pricing_subscription_variables.htm ===
---
article_id: ind.pricing_subscription_variables.htm
title: Common Proration Examples
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_subscription_variables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_pricing_proration.htm
fetched_at: 2026-09-07
---

# Common Proration Examples

These examples demonstrate how various proration settings impact the final subscription price for a product with a Selling Model Type of TermDefined.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
Key terminologies
AlignToCalendar: The billing period starts on the first day of the calendar period (e.g., the 1st of the month for monthly subscriptions, or January 1st for annual subscriptions). If a business wants all monthly subscriptions to be billed from the 1st of the month, they would set this to AlignToCalendar.
Anniversary: The billing period starts on the subscription start date (the Effective From date).
DayOfPeriod: The billing period starts on a specific day of the month (and specific month for annual subscriptions) defined by the administrator. The parameters Start Proration Day and Start Proration Month are relevant and used only if Start Proration Period = DayOfPeriod.
EndOfPeriod: The billing period starts on the last day of the period.
Annual Proration Examples
Demonstrates how the system calculates pricing based on a yearly billing cycle.
Semi-Annual Proration Examples
Demonstrates how the system calculates pricing based on 6-month billing intervals.
Quarterly Proration Examples
Demonstrates how the system calculates pricing based on 3-month billing intervals.
Monthly Proration Examples
Demonstrates how the system calculates pricing based on a monthly billing cycle.
Annual Proration Examples for Leap Years
Review calculations for annual billing cycles, and learn how the total days adapt to leap years. Salesforce Pricing uses a specific design convention to handle end-of-month anniversary dates. Rather than relying on simple date increments, Salesforce Pricing adjusts period end dates to accommodate the presence or absence of February 29 so that it calculates full periods logically based on date availability.
Monthly Proration Examples for Leap Years
Review calculations for monthly billing cycles, and learn how the total days adapt to leap years and varying month lengths. For a monthly product selling model, Salesforce Pricing anchors exactly to the numerical start date. If an anniversary subscription starts on the 29th, 30th, or 31st, and that exact date doesn't exist in the following month, Salesforce Pricing uses a design convention: it aligns the next period to the latest available day of that subsequent month. All full periods behave as "month-end to month-end minus one.
Weekly Proration Examples
Demonstrates how the system calculates pricing based on a 7-day billing cycle, for subscription and consumption products.

=== ARTICLE: ind.pricing_sync_decision_tables_in_a_pricing_recipe.htm ===
---
article_id: ind.pricing_sync_decision_tables_in_a_pricing_recipe.htm
title: Sync Decision Tables in a Pricing Recipe
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_sync_decision_tables_in_a_pricing_recipe.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_recipes.htm
fetched_at: 2026-09-07
---

# Sync Decision Tables in a Pricing Recipe

To sync decision tables for a specific pricing recipe:

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To manage pricing recipes:	

Salesforce Pricing Design Time

From Setup, in the Quick Find box, enter Pricing Recipes, and then select Pricing Recipes.
Locate the recipe that you want to update, and then select the Sync action.

=== ARTICLE: ind.pricing_sync_pricing_data.htm ===
---
article_id: ind.pricing_sync_pricing_data.htm
title: Sync Pricing Data in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_sync_pricing_data.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Sync Pricing Data in Revenue Management

Regularly sync your pricing data in Salesforce Revenue Management to ensure the latest information is available in decision tables that are mapped to a pricing recipe and have their usage type set to Pricing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS
NEEDED
To enable data sync:	Salesforce Pricing Design Time
To ensure complete sync of decision tables:	Assetize Order

You should sync pricing data whenever there are updates to your product prices, discounts, or any other pricing-related data that decision tables consume. Syncing pricing data is crucial for accurate pricing calculations. This ensures consistency across your sales processes and supports features like derived pricing. Without it, inconsistencies could impact final net price calculations.

IMPORTANT For an accurate sync, set the Usage Type to Pricing for any decision table containing source objects. If a complete sync fails, we recommend using the System Admin permission set.

The sync operation is a manual process.

From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
In the Sync Pricing Data section, click Sync.

The sync refreshes all decision tables that are mapped to a pricing recipe and have their usage type set to Pricing.

After refreshing or cloning a sandbox, you must manually re-run Sync Pricing Data and refresh each decision table individually. Pricing data doesn't automatically carry over from the source org.

Automate Pricing Data Sync with a Scheduled Flow
Create a scheduled flow that refreshes your pricing decision tables on a regular cadence so that Agentforce Revenue Management always uses current pricing data without requiring a manual sync.

=== ARTICLE: ind.pricing_turn_on_salesforce_pricing.htm ===
---
article_id: ind.pricing_turn_on_salesforce_pricing.htm
title: Turn On Salesforce Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_turn_on_salesforce_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_discover_and_explore.htm
fetched_at: 2026-09-07
---

# Turn On Salesforce Pricing

If you haven’t done it yet, enable Salesforce Pricing to give your users access to Salesforce Pricing’s object and features.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To enable Salesforce Pricing:	System Admin
From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Settings.
Turn on Salesforce Pricing.

=== ARTICLE: ind.pricing_understand_advanced_pricing_setup.htm ===
---
article_id: ind.pricing_understand_advanced_pricing_setup.htm
title: Salesforce Pricing Advanced Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_understand_advanced_pricing_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Salesforce Pricing Advanced Setup

Salesforce Pricing provides advanced setup options to customize and extend its core functionalities that is crucial for leveraging the product's full power and tailoring it to specific business needs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

These advanced setup activities involve additional, configuration steps beyond basic setup, which are essential for successful feature adoption and enabling specific pricing behaviors or integrations.

Configure Price Tracking History Settings
Configure Proration Settings
Set Up Parallel Pricing Element Execution
Set Up Einstein Generative AI for Salesforce Pricing
Configure Pricing Parameters for Standard Objects
Advanced Price Log Settings

=== ARTICLE: ind.pricing_understand_and_resolve_api_execution_messages.htm ===
---
article_id: ind.pricing_understand_and_resolve_api_execution_messages.htm
title: Resolve API Execution Errors
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_understand_and_resolve_api_execution_messages.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_operations_console.htm
fetched_at: 2026-09-07
---

# Resolve API Execution Errors

Use the Debug Details tab to troubleshoot errors in the executed API.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To view price logs:	Salesforce Pricing Design Time

Here are some of the most common issues when your pricing API call fails.

If the failed pricing API was used to calculate a product's price, find the error details under the Debug Details tab.
Under Debug Details, click Pricing Procedure.
To find the reasons for success or failure of a line item, expand the line item.
To resolve the error for a failed line item, follow the troubleshooting steps under the respective line item.
In a typical pricing API call, pricing is calculated for multiple line items. Sometimes, one line item fails, but the others succeed. For example, if you use a Manual Discount element and enter an incorrect value for the Adjustment Type variable, the API call for that specific line item fails, while the other line items succeed.
If the failed API was used to calculate a product's derived price, check whether the error occurred in the discovery procedure, pricing procedure, or both.
To identify and resolve the issue, under Debug Details, click Discovery Procedure and check the error message.
The Discovery Procedure tab shows the details in JSON format.
To check the issues based on source and derived products, and their execution information under Debug Details, click Pricing Procedure and follow the troubleshooting steps.
When a pricing procedure is executed, you may see an error status even if the error log is empty. This happens because a line item has not been executed for pricing.
SEE ALSO
Derived Price
Discovery Procedures for Pricing

=== ARTICLE: ind.pricing_understand_discount_distribution_service_terms.htm ===
---
article_id: ind.pricing_understand_discount_distribution_service_terms.htm
title: Understand Discount Distribution Service Terms
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_understand_discount_distribution_service_terms.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_discount_spread_service.htm
fetched_at: 2026-09-07
---

# Understand Discount Distribution Service Terms

Familiarize yourself with the variables and terminology you'll encounter when you configure a pricing procedure to calculate discounts using the Discount Distribution Service element.

Here are the variables that are specific to and important to know when you use the Discount Distribution Service element in your pricing procedure.

VARIABLE	DESCRIPTION
Header Distribution Type	This variable indicates the discount amount to be removed from the ItemNetTotalPrice or NetUnitPrice variable.
Header Discount Type	

This variable indicates the type of discount that can be applied. There are three possible values: Amount, Percentage, and Override.

If you select the Override option, you'll also need to provide a variable for the Header Subtotal. The Header Subtotal variable contains the subtotal amount from which the target discounts are deducted.


Header Distribution Logic	This variable defines the distribution method for the discount. The values you can apply are Equal or Proportionate.
IMPORTANT Map the Input Unit Price input variable when the Net Unit Price variable is mapped (either in the Pricing Setting element or here). If you don't, the service will return an empty value, and as a result, the Waterfall view will display a null value for the Net Unit Price of the line item.

You can control the distribution logic of the discounts as follows:

LOGIC	DESCRIPTION
Equal	In this distribution logic, the discount is applied equally across all line items.
Proportionate	In this distribution logic, the discount applied at the quote level (header) is allocated to individual line items based on their respective list prices. Basically, items with higher values receive a larger portion of the discount compared to those with lower values. This ensures the discount is distributed proportionally to each line item’s contribution to the total quote value.

When you set floor limits, you’ll need to map these tags in the procedure.

VARIABLE	DESCRIPTION
Minimum Net Unit Price	This variable indicates the minimum net unit price that can be set for a line item. No discount can be applied below this price. This must be of currency type.
Total Remainder Amount	This variable stores the remainder amount after applying all the discounts. This must be of currency type.

=== ARTICLE: ind.pricing_understand_price_revisions.htm ===
---
article_id: ind.pricing_understand_price_revisions.htm
title: Understand Price Revisions
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_understand_price_revisions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_apply_policy_driven_price_revisions.htm
fetched_at: 2026-09-07
---

# Understand Price Revisions

Price revisions are adjustments to the price of goods or services. For a sales rep, understanding these changes is crucial, as they provide a clear and logical justification for a new price during a renewal. These changes, whether increases (uplifts) or decreases, help companies respond to market shifts, control costs, and maximize revenue. Revisions aren't random; they're typically triggered by pre-planned schedules, shifts in economic indicators, or contractual terms, which allow a sales rep to frame a price adjustment as a pre-agreed condition rather than a surprise demand.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

A common economic trigger is the Consumer Price Index (CPI), which gives a sales rep a powerful, objective tool for these discussions. Adjusting prices based on CPI is a primary way for businesses to handle inflation, ensuring their pricing keeps pace with the rising costs of goods and labor. By referencing a shared economic reality like the national CPI, a sales rep can depersonalize the price increase, anchoring the conversation in factual data and turning a potentially difficult negotiation into a transparent discussion about sustainability and fair value.

To make informed decisions about price revisions, you must understand two key entities.

Price Revision Policies. A price revision policy is a company's formal set of guidelines and formulas for modifying the prices of its products or services. It ensures that price adjustments are applied consistently and are based on predefined business rules rather than arbitrary decisions.

This policy can be applied at different levels: either granularly to a specific product or line item, or comprehensively across all products and services within an entire contract or quote. The policy's core is its formula, which often uses the Consumer Price Index (CPI) to account for inflation. These adjustments are typically made upon contract renewal, though they can also be performed annually on a separate schedule.

Index Rates. Using an index rate in pricing is a structured way to automatically adjust prices based on an external economic benchmark, most commonly the Consumer Price Index (CPI), which measures inflation. This data-driven approach ensures price changes are accurate and consistent. Its implementation depends on two key factors: using an official data source, like that from a national agency, and setting an update frequency. While annual updates offer predictability, more frequent adjustments, such as monthly, are common in high-inflation economies to keep pace with rising costs.

NOTE Custom profiles may not have access to these entities or its’ associated fields. Contact your Salesforce admin for help.

=== ARTICLE: ind.pricing_understand_pricing_elements.htm ===
---
article_id: ind.pricing_understand_pricing_elements.htm
title: Understand Pricing Elements
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_understand_pricing_elements.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_procedures.htm
fetched_at: 2026-09-07
---

# Understand Pricing Elements

Pricing elements are the primary components that make up a pricing procedure in Salesforce Pricing within Revenue Management. They are the building blocks, where each element represents a step in the calculation of a product's final price. Understanding pricing elements is essential for successfully defining and calculating product prices and creating customized pricing strategies.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

A new pricing procedure starts as a blank canvas, and each pricing element added forms a step in the procedure. These elements contain variables crucial for defining and calculating product prices. These variables are mapped to context tags, which are dynamic placeholders that facilitate data transfer between the pricing elements and the overall pricing procedure.

Essentially, pricing procedures are created by combining various pricing elements, with each element performing a specific calculation or adjustment. The culmination of these calculations and adjustments applied to the list price results in the net unit price. Salesforce Revenue Cloud leverages these pricing elements to enable flexible pricing models.

=== ARTICLE: ind.pricing_understand_the_order_of_execution_for_place_sales_transaction.htm ===
---
article_id: ind.pricing_understand_the_order_of_execution_for_place_sales_transaction.htm
title: Understand the Order of Execution for Place Sales Transaction
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_understand_the_order_of_execution_for_place_sales_transaction.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_plan_framework.htm
fetched_at: 2026-09-07
---

# Understand the Order of Execution for Place Sales Transaction

When you create or update a quote or order using the Place Sales Transaction API, Revenue Management (formerly Revenue Cloud)processes the request through a defined order of execution. This order describes how configuration, pricing, Apex hooks, and automation run during transaction processing. Understanding this order helps you determine where pricing logic runs and how context data is processed when using Place Sales Transaction.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.

When Place Sales Transaction processes a request, Revenue Management performs these steps in sequence.

Saves the sales transaction header.
Executes triggers associated with the transaction header.
Synchronizes supported context data back into the transaction context when context data is included in the request payload.
Hydrates the transaction with data required for configuration and pricing.
Applies applicable configuration logic to the transaction.
Resolves Amend, Renew, and Cancel (ARC) data required for the transaction.
Validates the transaction using ARC validation rules.
IMPORTANT ARC validation runs before the pre-pricing Apex hook. If you use Apex hooks to modify fields such as Start Date or Quantity, those changes bypass ARC validation and can produce unexpected results. To ensure proper validation, update fields like Date and Quantity in the request payload before calling Place Sales Transaction.
Performs pricing.
Runs the pre-pricing Apex hook, if defined.
Runs pricing logic.
Runs the post-pricing Apex hook, if defined.
Persists data from the transaction context.
Executes triggers for affected records.
Synchronizes supported context data back into the response when context data is included in the request payload.
Executes record-triggered flows and other custom logic based on the persisted data.

=== ARTICLE: ind.pricing_understand_your_resolution_variables.htm ===
---
article_id: ind.pricing_understand_your_resolution_variables.htm
title: Understand Your Resolution Variables
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_understand_your_resolution_variables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_output_resolution.htm
fetched_at: 2026-09-07
---

# Understand Your Resolution Variables

When you enable output resolution in your pricing element, you’ll see a new Resolution Variables section that will consume the details of the resolution strategy you’ve created. The variables in the Resolution Variables section must be mapped to accurate context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
ELEMENTS	RESOLUTION VARIABLE	DESCRIPTION


List Price

Price Tracking

Price Adjustment Matrix

	Resolution Strategy	Specifies the pricing resolution strategy you’ve previously defined and saved as a procedure output resolution record. If you've not created a resolution strategy, see Configure Pricing Resolution Strategies.


List Price

Price Tracking

Price Adjustment Matrix

	Use As List	

Specifies the input variable that the pricing engine uses to determine the resolution for identifying the best price.

For example, if your input variable is a price book, the pricing engine finds the relevant value in the decision table and calculates the best price from the list of available price books.




List Price

Price Tracking

	Candidate Priority	If there is a tie in the available list of prices, then you can assign a priority to determine which one is selected.


List Price

Price Tracking

	Final Price Sequence	The final tiebreaker for determining a line item's price when a priority-based resolution strategy results in a tie. The Final Price Sequence typically selects the lowest price.

You can also use the Write Back section to store the final result of the output resolution process directly into a tag.

=== ARTICLE: ind.pricing_unique_pricing_scenarios.htm ===
---
article_id: ind.pricing_unique_pricing_scenarios.htm
title: Unique Pricing Scenarios
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_unique_pricing_scenarios.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Unique Pricing Scenarios

Learn how complex pricing scenarios, from product interdependencies to honoring long-term customer agreements, impact sales efficiency and customer satisfaction. Discover how Salesforce Pricing provides the sophisticated capabilities needed to manage these unique challenges and drive revenue.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.

When customers purchase a product, the price of dependent services or add-ons often changes based on the main item. This means sales reps must calculate prices manually, causing mistakes and slowing down sales. The inability to offer adaptive pricing options makes customers unhappy and costs organizations deals.

With Salesforce Pricing, you can track negotiated discounts and prices using contracts, derive one product's price from another, and distribute discounts programmatically.

Discount Distribution Service
Apply quote-level discounts across each line item ensuring consistent and accurate pricing using the Discount Distribution Service feature in Revenue Management.
Implement Derived Pricing
To accurately calculate a product’s price from another pricing source, such as a product or an asset, or the overall quote value, use the Derived Price feature.
Contract-Based Pricing
Manage and apply contact-based pricing deals on previously negotiated pricing agreements defined in a contract.
Establish Procedure Output Resolution
To select the definitive price for a product when pricing rules generate multiple outcomes, implement Procedure Output Resolution.
Apply Policy-Driven Price Revisions
Apply policy-driven price changes to respond to market conditions, contract terms, or inflationary trends. Pricing designers can define revision policies, track Consumer Price Index (CPI) data, and enable uplifts at set intervals, optimize revenue, and maintain business performance.
Promotion Execution Element
To apply promotions, add the Promotion Execution element to your pricing procedure. This element connects Global Promotions Management with Revenue Management, executing applicable promotions for your transaction line items.
Pricing Action Parameters
To calculate the price of products directly from any object’s record page, use the Calculate Price button. All pricing actions are associated with a context definition and a pricing procedure so that the pricing data that is processed during the pricing process is stored directly in the Salesforce object.
Use Advanced Transaction Detail Line Pricing to Map Custom Fields
Users can update custom fields on sales transaction items or sales transaction item details through pricing procedures by using the Advanced Detail Line Pricing feature. With this feature, users no longer need to use custom triggers or flows to update those fields. This feature is useful for amendment, renewal, and cancellation use cases.

=== ARTICLE: ind.pricing_update_your_product_price_range_entries_decision_table.htm ===
---
article_id: ind.pricing_update_your_product_price_range_entries_decision_table.htm
title: Update Your Product Price Range Entries Decision Table
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_update_your_product_price_range_entries_decision_table.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_price_tracking.htm
fetched_at: 2026-09-07
---

# Update Your Product Price Range Entries Decision Table

For users who previously enabled minimum price tracking, update your decision table to include the newly introduced option for tracking maximum prices. If you enable maximum price in Price Tracking History settings without this update, your pricing procedure will fail during execution.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To edit decision tables:	Salesforce Pricing Design Time User

If you're using the Price Tracking feature for the first time and have enabled both maximum and minimum price settings, you can use the predefined Product Price Range Entries V2. This will automatically map to record both the minimum and maximum price of a product.

From App Launcher, search for and select Lookup Tables.
Select the Product Price Range Entries decision table.
Deactivate the decision table.
Click Edit.
Click Save & Next.
To record the maximum price of a product, under Results, click +Add Results.
In the Source Object Field, enter and select MaxRecordedPrice.
Click Save & Next.
Click Save & Next again.
Click Finish.
Activate your decision table.

=== ARTICLE: ind.pricing_use_the_aggregate_price_element.htm ===
---
article_id: ind.pricing_use_the_aggregate_price_element.htm
title: Use the Aggregate Price Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_use_the_aggregate_price_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_add_aggregate_price_element.htm
fetched_at: 2026-09-07
---

# Use the Aggregate Price Element

Aggregate and show the price of a group of products based on product categories, product types, or other groups of line items.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time
IMPORTANT When using the Aggregate Price element, be careful not to create pricing loops by incorrectly mapping values in your pricing procedure. For instance, a circular dependency forms when the Net Unit Price is set by Input Unit Price, but then Input Unit Price is changed by an aggregate element that also relies on Net Unit Price. This creates a never-ending loop where Net Unit Price keeps updating, preventing it from settling on a final value and causing performance problems or wrong calculations.

Let's look at a scenario where we group products by their category. We'll add three products: laptops, printers, and Quip software. Laptops and printers will be assigned to the Electronics category, while Quip's category will be Software. Using this data, we'll calculate the aggregate price for each product category.

NOTE
In the Aggregate Price element, the Output and GroupBy tags must belong to the same hierarchical level within the context.
When you use the Aggregate Price element to calculate an average for the Currency data type, the average value can have up to 16 decimal places.
Configure a pricing procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Aggregate Price element and specify these variable values.
Group By: ProductCategory
The Group By field sets your grouping criteria by searching for the criteria according to which the aggregation is performed.
Formula: SUM (ItemNetTotalPrice)
This is the aggregation formula used to calculate the pricing.
Output Variable: ItemGroupSummarySubtotal
The output variable contains the context tag that stores the output derived from the aggregation formula. 
To override the pricing output of a variable use the Write Back condition.
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure. Enter the input values for your products and click Simulate again.
Aggregate pricing changes can't be viewed in the waterfall view. However, the JSON output provides insight into how the aggregate prices were calculated based on the product category. Based on our example, the aggregate price of products belonging to the Electronics category is calculated by summing their individual prices ($141,615 + $4,975), resulting in an ItemGroupSummarySubtotal of $146,590. This confirms that your procedure is working as expected.

=== ARTICLE: ind.pricing_use_the_discount_spread_service_element.htm ===
---
article_id: ind.pricing_use_the_discount_spread_service_element.htm
title: Use the Discount Distribution Service Element
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_use_the_discount_spread_service_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_discount_spread_service.htm
fetched_at: 2026-09-07
---

# Use the Discount Distribution Service Element

To calculate discounts that can be spread evenly across all line items or specifically across a subsection of line items, use the Discount Distribution Service element.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To create pricing procedures:	Salesforce Pricing Design Time

Let’s look at a scenario where we are applying a $300 discount equally across a laptop and a printer on their net unit price.

NOTE To configure header adjustments that apply discounts to an entire quote or order using the Discount Distribution Service element, see Header Adjustments Overview.
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Click to add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Remember, Discount Distribution Service doesn't support derived products on quote line items, so don't map your Is Derived variable.
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Discount Distribution Service element.
IMPORTANT You can only add the Rounding Values and Aggregate Price element after the Discount Distribution Service element in a pricing procedure.
Select the line items that must be eligible for a discount. In our example, we aren't selecting any because we want all input line items in the quote to be considered for calculation.
If you've selected either of the options, this is how the procedure would read the information.
Lookup Table	

Discounts are distributed across all line items based on the decision table you select to retrieve data from.


Define participating conditions	

Discounts are applied to quotes based on the conditions you set. For example, you could set a condition to apply discounts to quotes where the product category is Electronics and the product's Net Unit Price doesn't exceed $150.

Map these variables.
Input Variables
Header Discount Type: HeaderDiscountType
Header Discount Value: HeaderDiscountValue
Header Distribution Logic: HeaderDistributionLogic
Header Distribution Type: HeaderDistributionType
List Price: ListPrice
Quantity: LineItemQuantity
Line Item: Lineitem
Input Unit Price: ListPrice
Minimum Net Unit Price: MinimumNetUnitPrice
Output Variables
Discount Value: LineItemDiscountValue
Distribution Type: LineItemDistributionType
Discount Type: LineItemDiscountType
Net Unit Price: NetUnitPrice
Subtotal: ItemNetTotalPrice
Click and select Include in Output.
Finally, set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Click Simulate to test your procedure.
Specify the input values for a laptop and printer along with the header discount details which is a $300 discount that must be equally or proportionally applied across all line items.
Test your input values by specifying the discount distribution logic as Equals and click Simulate again.
Now, change your input values by specifying the discount distribution logic as Proportionate and click Simulate again.

Now, let's use the same scenario to learn how floor limits are set and how you can store the remainder amount for future use. Go back to the Discount Distribution Service element and select Set floor price limit. Here, under the Floor Price Limit section, select Store remainder amount and map the TotalRemainderAmount tag to the Total Remainder Amount variable.

Let's simulate this scenario. In your input value, change the HeaderDiscountValue as $900 instead of $300.

Upon simulation, since we've provided floor prices (the Minimum Net Unit Price) for the printer and laptop, after applying discounts equally across the products, you'll see a remainder amount after the system honors their floor prices. This remainder amount value is then written back to the TotalRemainderAmount tag.

=== ARTICLE: ind.pricing_use_the_price_revision_element_in_a_pricing_procedure.htm ===
---
article_id: ind.pricing_use_the_price_revision_element_in_a_pricing_procedure.htm
title: Use the Price Revision Element in a Pricing Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_use_the_price_revision_element_in_a_pricing_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_apply_policy_driven_price_revisions.htm
fetched_at: 2026-09-07
---

# Use the Price Revision Element in a Pricing Procedure

To maintain profitability on renewals, use the Price Revision element to automatically adjust for inflation and rising operational costs on quotes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create pricing procedures:	Salesforce Pricing Design Time
NOTE After your Salesforce org updates to Winter ’26, users who have Price Tracking enabled may be unable to use the Price Revision feature because the Index Rate decision table may be deactivated. To activate the Index Rate decision table, from Setup, search for and select Decision Tables. Select the Index Rate decision table and activate it.

Let’s consider a scenario where a business wants to adapt its pricing to frequent inflationary effects in a country that we’ll call ABC. To achieve this, it secures an agreement with its customers for an annual price increase equivalent to the Consumer Price Index (CPI) plus 5%, while ensuring the total adjustment is capped at 10%.

Calculating the revised price of a product involves a few key steps.

Add picklist values to the Region field on the Index Rate entity.
Create a price revision policy record.
Define the index rates.
Add the Price Revision element to a pricing procedure to calculate the adjusted prices due to inflation.
Modify the Index Rate Record Page

Before you create an index rate record, you’ll need to add Region picklist values to the Index Rate entity's Region field.

From Setup, in Object Manager, search for and select Index Rate.
Select Fields & Relationships, and then click Region.
In the Region Picklist Values section, click New.
Enter country names. For our use case, specify ABC.
Save your changes.
Create a Price Revision Policy Record

Configure an inflation policy for the country of ABC to enable sales reps to apply specific price uplifts to quotes and deals based on its defined inflation rate.

Before creating a price revision policy, you need to understand the two policy types:

Flat. This policy type uses a manually entered uplift value (a policy adjustment). The system doesn't reference a decision table to find the value.
Price Index. This policy type automatically retrieves the uplift value from the Index Rate decision table, ensuring the rate matches the input criteria.
From the App Launcher, find and select Price Revision Policies.
Click New.
Specify these details.
Name: ABC CPI
Type: Price Index
Effective From: 1/1/2025
Effective To: 12/31/2025
Region: ABC
Formula: MAX(10, PriceIndex + 5)
To define a formula, follow the steps below.
Select a function in the Search functions… field. Here, select MAX.
Highlight the value within the brackets and delete it.
Place your cursor in the brackets and then, enter 10,.
Select a resource from the Select a resource... field. Here, select PriceIndex.
Select an operator from the Enter an operator… field. Here, select +.
Enter 5. All numerical values as treated as a percentage.
Save your changes.
IMPORTANT Effective date ranges for the same region can’t overlap, unless you’re on a multi-currency organization.
Define Index Rates

The index rates entity stores inflation rates for various periods of time based on different time periods.

From the App Launcher, find and select Index Rates.
Click New.
Specify these details.
Name: ABC CPI 2025
Rate: 8
Valid Start Date: 1/1/2025
Valid End Date: 12/31/2025
Region: ABC
Usage Type: Pricing
Save your changes.
IMPORTANT Effective date ranges for the same region can’t overlap, unless you’re on a multi-currency organization.
Add the Price Revision Element
Create a pricing procedure. To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Add the Pricing Setting element and map these variables.
Input Variables
Line Item: LineItem
Output Variables
Price Waterfall: price_water_fall
Net Unit Price: NetUnitPrice.
Subtotal: ItemNetTotalPrice
Add the List Price element to fetch the base price of the product.
Under Lookup Table Details, select the Price Book Entries V2 decision table and map these variables.
Input Rule Variables
Product: Product
Price Book: PriceBooks
Product Selling Model: ProductSellingModel
Input Variables
Quantity: LineItemQuantity
Output Variables
List Price: ListPrice
Subtotal: ItemNetTotalPrice
Add the Price Revision element to adjust prices for a product.
Under Lookup Table Details, select the Index Rate decision table and map these variables.
Input Rule Variables
Valid Start Date: ItemConsumerPriceIndexDate_std. This is the date for your price revision that must fall within the effective date range specified in the index rate record.
Region: ItemPriceRevisionPolicyRegion_std. This is the region where you’re verifying the inflation rate.
Input Variables
Quantity: LineItemQuantity
Price Revision Policy: ItemPriceRevisionPolicyName_std. This is the name of the price revision policy record.
Input Unit Price: ListPrice
Policy Type: ItemPriceRevisionPolicyType_std. This is the policy type you’ve selected in the price revision policy record, which can be either Flat or Price Index.
Price Revision Formula: ItemPriceRevisionPolicyFormula_std. This is the formula you’ve provided in the price revision policy record.
To calculate each ramp segment's price uplift from the previous segment's uplift percentage instead of the original list price, select Enable Compound Uplift.
This checkbox appears only after you select a lookup table and exposes these fields. Select this option only if the transaction includes ramp segments. If you select **Enable Compound Uplift** on a transaction that doesn't include ramp segments, the element calculates those lines using the standard, non-compounding calculation instead.
Ramp Identifier: Groups line items into the same ramp so that its segments compound independently of other ramps on the same transaction. The pricing engine calculates prices for lines without a Ramp Identifier independently.
Base Price Multiplier: The starting multiplier for the ramp. Leave this field blank for a new sale to default the value to 1. For an amendment or renewal, enter the ramp's compounded multiplier from the prior transaction.
Uplift Method: Determines whether a segment's uplift compounds or uses the standard, noncompounding calculation. Leave this field blank to default to standard.
Effective From and Effective To: The date range for the segment. Every segment in a compounding ramp group requires a unique Effective From date, which the element uses to determine the calculation order.

If you later change or remove the selected lookup table, the system automatically clears enable compound uplift and hides the related fields.

Click and select Include in Output.
Save your procedure.
Click Simulate
Specify the input values for subscriptions to Slack along with the additional uplift of 5% that must be added to maintain gross margins. Click Simulate again.
The price waterfall shows the Price Revision updates, confirming that your procedure is working as expected.

When you simulate a pricing procedure, you can enter the formula manually to verify if the adjusted prices are reflected for a given product. However, when a sales rep creates a quote, they'll see this information on the quote itself, along with the option to enter additional uplift data.

IMPORTANT
If your waterfall doesn’t reflect the right values, we recommend refreshing your Index Rate decision table.
Compound uplifts require a unique Effective From date on every segment in a ramp group. If any segment is missing this date, or if two segments share the same date, pricing calculations fail for the entire ramp group rather than only the affected segment.
Mix compounding and standard-uplift lines in the same transaction. Standard-uplift lines calculate independently and do not compound.
If the pricing procedure uses delta pricing and you enable Compound Uplift, the Price Revision element reprices every line in the ramp group each time it runs, regardless of the delta pricing setting. This behavior applies only to lines that use Compound Uplift. Delta pricing behaves normally for lines that do not use it.
To use compound uplifts, create a new pricing procedure. Existing pricing procedures do not support this capability.
When you select Enable Compound Uplift, the Policy Type and Price Revision Formula fields no longer require values.

=== ARTICLE: ind.pricing_use_the_procedure_plan_framework.htm ===
---
article_id: ind.pricing_use_the_procedure_plan_framework.htm
title: Use the Procedure Plan Framework
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_use_the_procedure_plan_framework.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_procedure_plan_framework.htm
fetched_at: 2026-09-07
---

# Use the Procedure Plan Framework

To ensure your procedures run in the correct order and pricing is applied consistently to a quote, create a new procedure plan.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To create and update procedure plan definitions:	

Procedure Plan Access

AND

Salesforce Pricing Design Time User


To create, update, and delete pricing procedures:	

Procedure Plan Access

OR

Salesforce Pricing Design Time User


To use pricing procedures:	Salesforce Pricing Run Time User
To define, edit, delete, set security, and set version settings for Apex classes:	Author Apex

Imagine that you work at an airline and assist business travelers. Now, let’s book a flight! We want our pricing to reflect real-time market conditions and show prices in the customer's local currency.

Before calculating the price, we’ll automatically fetch a dynamic base fare from an external system to ensure competitive pricing. We'll also apply the booking platform’s discounts and add a convenience fee.

Once we build our procedure plan, we’ll create a quote. Then, based on the user's location (for example, India), we’ll convert the total price from USD to INR.

Before you begin, ensure that you:

Have enabled Salesforce Pricing.
Have permissions to create procedures, procedure plans, products, and quotes.
Understand how to create pricing procedures. To learn more about pricing procedures, see Build Your Pricing Procedures Using Salesforce Pricing.
Understand and know how to use Context Definitions. To learn more about context definitions, see Context Definitions.
Use the same context definition across your pricing procedures and procedure plans.

Procedure plan definitions can be complex, especially when they involve Apex classes and different pricing procedures. Follow these steps to create a quote and learn how to make your pricing dynamic and accurate without complicating the procedure itself.

Turn on Procedure Plan Orchestration for Pricing
From Setup, in the Quick Find box, enter Revenue Settings, then select Revenue Settings.
Find and enable Procedure Plan Orchestration for Pricing.
Find and enable Exclude Default and Sales Transaction Type Pricing Procedures.
Create a Commercial Product
From the App Launcher, find and select Products.
Create a commercial product called Delhi - New York.
To learn how to create a product, see Create Simple Products and ensure that the Product Record Type is set as Commercial.
Add your product to the catalog and create a price book entry for it.
From Setup, in the Quick Find box, search for and select Salesforce Pricing Setup.
In the Sync Pricing Data section, click Sync.
Build Your Pricing Procedure
Create a pricing procedure and name it Flight Booking Pricing Procedure.
To create a pricing procedure, follow the first 5 steps in Configure Your Pricing Procedure.
Create constants. These constants will serve as placeholders for fixed values in your pricing procedure.
CONSTANT NAME	DATA TYPE	DEFAULT VALUE
AdjType	TEXT	Percentage
AdjValue	NUMBER	5
Override	TEXT	Override
ConvFeeAdjType	TEXT	Amount
ConvFeeAdjValue	NUMBER	-250
Add the following elements.
Pricing Setting
List Price. Use the Price Book Entries V2 decision table.
Manual Discounts. You’ll need to add three manual discount elements.
The first Manual Discount element is added to calculate the dynamic base fare of the flight. Map these variables.
Input Variables
Adjustment Type: Override
Adjustment Value: PartnerUnitPrice
Quantity: LineItemQuantity
Input Unit Price: ListPrice
Output Variable
Net Unit Price: NetUnitPrice
The second Manual Discount element is added to calculate the platform discount for the flight booking. Map these variables.
Input Variables
Adjustment Type: AdjType
Adjustment Value: AdjValue
Quantity: LineItemQuantity
Input Unit Price: PartnerUnitPrice
Output Variable
Net Unit Price: NetUnitPrice
And the last Manual Discount element is added to calculate the convenience fee to charge your customer for the flight booking.
Input Variables
Adjustment Type: ConvFeeAdjType
Adjustment Value: ConvFeeAdjValue
Quantity: LineItemQuantity
Input Unit Price: NetUnitPrice
Output Variable
Net Unit Price: NetUnitPrice
Set your preferences to view pricing information, profile access, and rank information.
Save your procedure.
Activate your procedure.

Your procedure should look like this. For the sake of clarity, we’ve renamed each Manual Discount element to show the pricing calculation it will perform. To rename an element, click and enter your desired name.

Define Classes for Apex Hooks
From Setup, in the Quick Find box, enter Apex, then select Apex Classes.
Click New.
The first Apex class is a prehook that fetches all Sales Transaction Items from the Pricing context and overrides their PartnerUnitPrice tag with a dynamic random base fare between 990 and 1200 before pricing execution from an external database.
public class DynamicFlightBasePriceApex implements RevSignaling.SignalingApexProcessor {

    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing PREHOOK');
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        //Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
                'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>)itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');
        System.debug('QLI itemData=' + itemData);

        // Generate random price between 990 and 1200
        Decimal minPrice = 990;
        Decimal maxPrice = 1200;
        Decimal range = maxPrice - minPrice;

        // Use Crypto.getRandomInteger() to generate a secure random number
        Integer randomInt = Math.abs(Crypto.getRandomInteger());
        Decimal randomPrice = minPrice + Math.mod(randomInt, range.intValue() + 1);

        System.debug('Generated Random Price: ' + randomPrice);
        
        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();
        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));
			dataPath.remove(0); // Remove contextId
			itemNodeUpdates.add(new Map<String, Object>{
                'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                'attributes' => new List<Object>{
                    new Map<String, Object>{
                        'attributeName' => 'PartnerUnitPrice',
                        'attributeValue' => randomPrice
                   }
                }
            });
        }
               
        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };
            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        // Return the response
        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        response.message = 'Apex executed successfully with Random Price: ' + randomPrice;
        return response;
    }
}

Create another Apex Class.
This Apex class is a posthook that fetches the NetUnitPrice tag after pricing and converts it to the local currency, INR (Indian Rupees) using a simulated dynamic conversion rate between 85–86. It then updates the Sales Transaction Item description with the new INR fare, providing localized pricing visibility for Indian customers.
public class ConvertFareToINRApex implements RevSignaling.SignalingApexProcessor {

    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('Executing POSTHOOK');
        String contextId = request.ctxInstanceId;
        Context.IndustriesContext industriesContext = new Context.IndustriesContext();
        
        //Query SalesTransactionItem nodes
        Map<String, Object> inputQueryItem = new Map<String, Object>{
            'contextId' => contextId,
                'tags' => new List<String>{ 'SalesTransactionItem' }
        };
        Map<String, Object> itemQueryOutput = industriesContext.queryTags(inputQueryItem);
        Map<String, Object> itemQueryResult = (Map<String, Object>)itemQueryOutput.get('queryResult');
        List<Object> itemData = (List<Object>) itemQueryResult.get('SalesTransactionItem');
        System.debug('QLI itemData=' + itemData);
        
        //Query NetUnitPrice nodes
        Map<String, Object> inputQueryItem2 = new Map<String, Object>{
            'contextId' => contextId,
                'tags' => new List<String>{ 'NetUnitPrice' }
        };
        Map<String, Object> itemQueryOutput2 = industriesContext.queryTags(inputQueryItem2);
        Map<String, Object> itemQueryResult2 = (Map<String, Object>)itemQueryOutput2.get('queryResult');
        List<Object> itemData2 = (List<Object>) itemQueryResult2.get('NetUnitPrice');
        System.debug('NetUnitPrice itemData=' + itemData2);
        Map<String, Object> netUnitTagData = (Map<String, Object>) itemData2.get(0);
        Decimal netUnitPrice = (Decimal) netUnitTagData.get('tagValue');
        netUnitPrice = netUnitPrice.setScale(2);
        System.debug('NetUnitPrice Tag Value=' + netUnitPrice);

        // Generate random price between 85.00 and 86.00 with decimals
        Decimal minPrice = 85.00;
        Decimal maxPrice = 86.00;
        Decimal range = maxPrice - minPrice; 
        Integer randomInt = Math.abs(Crypto.getRandomInteger());
        Integer randomDecimalInt = Math.mod(randomInt, 100);
        Decimal randomFraction = Decimal.valueOf(randomDecimalInt) / 100;
        Decimal usdToInrRate = minPrice + randomFraction;
        if (usdToInrRate > maxPrice) { 
            usdToInrRate = maxPrice;
        }
        
        // Calculate NetUnitPrice in INR
        Decimal fareInInr = (netUnitPrice * usdToInrRate).setScale(2);
        
        String fareMessage = 'The Flight fare in INR is: ' + fareInInr + 
                     ' (USD ' + netUnitPrice + 
                     ' at rate ' + usdToInrRate + ')';
        System.debug(fareMessage);
        
        // STEP 3 - Build update list
        List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();
        for (Object itemObj : itemData) {
            Map<String, Object> itemNode = (Map<String, Object>) itemObj;
            List<Object> dataPath = (List<Object>) itemNode.get('dataPath');
            System.debug('Full item dataPath: ' + JSON.serialize(dataPath));
			dataPath.remove(0); // Remove contextId
			itemNodeUpdates.add(new Map<String, Object>{
                'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                'attributes' => new List<Object>{
                    new Map<String, Object>{
                        'attributeName' => 'SalesTrxnItemDescription',
                        'attributeValue' => fareMessage
                   }
                }
            });
        }
            
        
        // STEP 4 - Submit context update
        if (!itemNodeUpdates.isEmpty()) {
            Map<String, Object> updateInput = new Map<String, Object>{
                'contextId' => contextId,
                'nodePathAndAttributes' => itemNodeUpdates
            };
            System.debug('--- PREHOOK: SUBMITTING CONTEXT UPDATE ---');
            System.debug(JSON.serializePretty(updateInput));
            industriesContext.updateContextAttributes(updateInput);
        }

        // Return the response
        RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
        response.status = RevSignaling.TransactionStatus.SUCCESS;
        response.message = 'Apex executed successfully with Price in INR: ' + fareInInr;
        return response;
    }
}

Configure a Custom Procedure Plan Definition
From Setup, in the Quick Find box, search for and select Procedure Plan Definitions.
Click New
Specify these details.
Title: Flight Booking Procedure Plan.
Press Tab to autopopulate the Developer Name.
Process Type: Revenue Cloud.
Primary Object: Quote.
Context Definition: <Context Definition Name>.
You’ll need to choose a context definition that’s been designed for your use case. However, ensure that this is the same context definition you used when you built your pricing procedure.
Save your changes.
Open the newly created procedure plan definition record.
To add the procedures that you want in the Procedure Plan Sections, select Add.
Add the first section to get the dynamic base price of our flight. Specify these details.
Type: Standard.
Name: DynamicBasePriceApex.
Section Type: Apex.
Once the section is added, click  and specify these details.
Phases: Pricing
Resolution Type: Default
Apex: DynamicFlightBasePriceApex
It should look something like this:
Similarly, add another section to perform the pricing calculation and override the base price with the price we generated using the Apex prehook. Specify these values.
Type: Standard.
Name: FlightPriceCalculation.
Section Type: Pricing Procedure .
Click  and specify these details.
Phases: Pricing
Resolution Type: Default
Procedure: Flight_Booking_Pricing_Procedure
Finally, add a section to convert the price from USD to INR (US Dollar to Indian Rupee) by adding this Apex posthook for users whose Billing Country is set to India
Type: Standard.
Name: ConvertFareToINR.
Section Type: Apex.
Click  and specify these details.
Phases: Pricing
Resolution Type: Rule-Based
Condition Requirements: All Conditions Are Met (AND)
Resource: Bill To Country
Operator: Equals
Output Value: India
Apex: ConvertFareToINRApex
Save and then, activate your procedure plan definition.
Verify Your Procedure Plan Execution

To verify if the procedure plan is executed in the order we set and the pricing is accurate, we’ll need to create a quote.

Create a quote.
In the Bill To Country field, enter India.
Save your changes.
Click Browse Catalogs and add the Delhi - New York product to the quote.
Hover on the Net Unit Price value to see the price waterfall details.
You’ll see the application of your procedure plan and the discounts and additions that you configured in your pricing procedure.
To view the converted rate for your quote line item, click in the quote line item row, and select View.
The Line Item Description shows the localized price for your flight.

=== ARTICLE: ind.pricing_view_pricing_adjustment_batch_job_logs.htm ===
---
article_id: ind.pricing_view_pricing_adjustment_batch_job_logs.htm
title: View Pricing Adjustment Batch Job Logs
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_view_pricing_adjustment_batch_job_logs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_adjustment_batch_jobs.htm
fetched_at: 2026-09-07
---

# View Pricing Adjustment Batch Job Logs

After your pricing adjustment batch job record is created, you can check the status and details of the job. If your batch job has failed or partially failed, you can review the generated logs to find out the reason for the failure.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To view pricing adjustment batch job logs:	Salesforce Pricing Design Time
From App Launcher, find and select Pricing Adjustment Batch Jobs.
Select the pricing adjustment batch job record you want to check.
The Related tab shows Pricing Adjustment Batch Job Log with details of incomplete or failed batch jobs.
You see logs only if a batch job fails or is partially completed. No logs are created for a successful batch job.

=== ARTICLE: ind.pricing_view_pricing_api_execution_logs.htm ===
---
article_id: ind.pricing_view_pricing_api_execution_logs.htm
title: Investigate and Analyze Pricing API Execution Logs
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_view_pricing_api_execution_logs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_operations_console.htm
fetched_at: 2026-09-07
---

# Investigate and Analyze Pricing API Execution Logs

Open price logs to resolve errors by using the log information in the Revenue Cloud Operations Console app. All headless pricing and pricing API executions, including discovery and pricing procedures performed within an API call, are recorded as pricing logs. This includes successful and unsuccessful executions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Advanced license.
USER
PERMISSIONS NEEDED
To view price logs:	Salesforce Pricing Design Time
From the App Launcher, find and select Revenue Cloud Operations Console.
From the list of pricing API executions, find and select the pricing log you want to check.
To check the success and failure status of the API, check the Details and the Debug Details tabs.
A successful API call shows a Success status along with relevant details, such as information about a pricing procedure executed through the API.
A failed call shows an Error status along with the reason for the failure and the troubleshooting steps.
To see the name, status, execution key, API type, and endpoint information about the API, select Details.
To see the details on each successful line item, the elements involved, and the success status, select Debug Details.
NOTE If you delete an execution log record, it's removed from the Pricing API Execution and Pricing Process Execution objects. However, the API execution details remain available in the Price Waterfall view of the pricing procedure.
SEE ALSO
PricingAPIExecution
PricingProcessExecution

=== ARTICLE: ind.pricing_view_pricing_data.htm ===
---
article_id: ind.pricing_view_pricing_data.htm
title: View Pricing Data Using Lightning Components
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_view_pricing_data.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_access_your_pricing_information.htm
fetched_at: 2026-09-07
---

# View Pricing Data Using Lightning Components

Use dedicated Lightning components to view your data in either grid-like layout or move it back to list view.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license.
USER PERMISSIONS NEEDED
To customize an Experience Cloud site:	

Be a member of the site AND Create and Set Up Experiences

OR

Be a member of the site AND an experience admin, publisher, or builder in that site

By default, the data displayed on the price book entry and the price adjustment record pages are set to grid view.

From App Launcher, find and select Price Management.
Open any price book entry or price adjustment record page.
TIP For faster access to price books, search for and select Price Books from the App Launcher. To access price adjustment schedules, search for and select Price Adjustment Schedules.
Click and select Edit Page.
On the Builder app, select the Pricing List View component on the canvas.
NOTE The Pricing List View component is the section that contains the list of entries in your record page. Refer to the image for more clarity.
Under the Pricing List View details, the checkbox to enable grid view is set by default. 
To view your pricing data in list view mode, deselect Show Grid View.
SEE ALSO
Standard Components for LWR Templates

=== ARTICLE: ind.pricing_view_pricing_recipes.htm ===
---
article_id: ind.pricing_view_pricing_recipes.htm
title: Select a Pricing Recipe for Your Salesforce Org
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_view_pricing_recipes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_pricing_recipes.htm
fetched_at: 2026-09-07
---

# Select a Pricing Recipe for Your Salesforce Org

Every Salesforce org requires a pricing recipe to define its pricing strategy. When Salesforce Pricing is activated, your org is automatically set up with a predefined recipe, though you can only have one active pricing recipe at a time. This recipe is essential for managing detailed pricing procedures.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To manage pricing recipes:	

Salesforce Pricing Design Time

From Setup, in the Quick Find box, enter Salesforce Pricing, and then select Salesforce Pricing Setup.
In the Select a Pricing Recipe section, select the pricing recipe.
The default NGPDefaultRecipe, included with the Salesforce Pricing solution, is associated with all predefined decision tables shipped with Salesforce Pricing.

To customize and build a pricing recipe that suits your organization's business needs, proceed further.

=== ARTICLE: ind.pricing_view_setup_objects_price_waterfall.htm ===
---
article_id: ind.pricing_view_setup_objects_price_waterfall.htm
title: Understand the Setup Objects Used for Price Waterfall
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_view_setup_objects_price_waterfall.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_set_up_price_waterfall_salesforce_pricing.htm
fetched_at: 2026-09-07
---

# Understand the Setup Objects Used for Price Waterfall

Price Waterfall uses setup objects to capture logs for how a pricing procedure ran, making it easy for your users to explain and check pricing calculations at each step. For example, pricing analysts can check the number of discounts applied at various tiers while calculating volume discounts.

Salesforce Pricing has predefined Price Waterfall objects.

Pricing Waterfall Subtype Definition
Defines the types of applications by using the Price Waterfall component.
Pricing Waterfall Business Process Type Definition
Defines the types of business processes that are applied to the pricing procedure.
Pricing Waterfall Explainability Action Definition
Defines where the metadata of your pricing procedure is stored.
Pricing Waterfall Explainability Action Version
Defines and stores versions of the explainability actions used by pricing procedures.

To view the pricing waterfall setup objects, from Setup, in the Quick Find box, search and select Decision Explainer. The Price Waterfall setup objects are visible with the associated Decision Explainer objects.

=== ARTICLE: ind.pricing_weekly_proration.htm ===
---
article_id: ind.pricing_weekly_proration.htm
title: Weekly Proration Examples
source_url: https://help.salesforce.com/s/articleView?id=ind.pricing_weekly_proration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pricing
parent_article: ind.pricing_subscription_variables.htm
fetched_at: 2026-09-07
---

# Weekly Proration Examples

Demonstrates how the system calculates pricing based on a 7-day billing cycle, for subscription and consumption products.

NOTE For the DayOfPeriod boundary field, 1 represents Monday, 2 represents Tuesday, and 7 represents Sunday. The system calculates weekly prices based on this boundary, starting each week on the selected day.
Base Transaction Details (All Examples)
Effective From: 2025-01-01
Effective To: 2025-03-17
Total Duration: 75 Days
Proration Period: Weekly
List Price: $12.01
Quantity: 12

Calculation Logic: The system divides the total duration by 7 to get the number of weeks in the term, including any partial week, then multiplies the unit price by the quantity and by that number of weeks.

Pricing Term Count: 75 / 7 = 10.71
Subscription Price: $12.01 x 12 x 10.71 = $1,543.36

