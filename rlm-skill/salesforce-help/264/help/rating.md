# Salesforce Help 264 — área: rating (70 artículos)

=== ARTICLE: ind.rm_add_negotiated_tierbased_rate_adjustment.htm ===
---
article_id: ind.rm_add_negotiated_tierbased_rate_adjustment.htm
title: Add Negotiated Tier-Based Rate Adjustment
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_add_negotiated_tierbased_rate_adjustment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_negotiated_tierbased_adjustment.htm
fetched_at: 2026-09-07
---

# Add Negotiated Tier-Based Rate Adjustment

Here’s how you can add the Negotiated Tier-based Rate Adjustment element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
IMPORTANT Make sure that you complete these prerequisites before you calculate a usage resource’s volume discount.
Add Rating Setting as the first element in the rating procedure.
Add the Negotiated Rate Card Entries element before the Negotiated Tier-Based Adjustment element, as the Rate Card Entry ID output from the former is used as an input in the latter.
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element. See Rating Element.
Click , and then find and select the Negotiated Tier-Based Rate Adjustment element from the list.
In the Lookup Table Details field, search for and select the Asset Tier-based Rate Adjustment lookup table.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
On the Input tab, enter the variables to simulate and verify your calculations,
Enter variable values either in JSON format (Advanced) or in the fields (Simplified).
Click Simulate and verify that the calculations are per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.
EXAMPLE JSON input values:
{
  "UsageRatableSummary": [
    {
      "ProductSellingModel": "",
      "UsageRatableSummaryId": "1Guxx0000004CIiCAM",
      "TierRateCardEntry": "",
      "OverageQuantity": "1",
      "UsageResource": "1BRDU0000000UjC4AU",
      "NetUnitRateUom": "0hEDU0000000UlK2AU",
      "Asset": "02iDU0000005hosYAA",
      "RatingDecisionDateTime": "2024-12-19T00:00:00.000Z",
      "TierRateCard": "",
      "IsTierNegotiated": "",
      "BaseRateCard": "",
      "SellableProduct": ""
    }
  ]
}

=== ARTICLE: ind.rm_add_negotiated_volumebased_rate_adjustment_.htm ===
---
article_id: ind.rm_add_negotiated_volumebased_rate_adjustment_.htm
title: Add Negotiated Volume-Based Rate Adjustment
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_add_negotiated_volumebased_rate_adjustment_.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_negotiated_volumebased_rate_adjustment.htm
fetched_at: 2026-09-07
---

# Add Negotiated Volume-Based Rate Adjustment

Here’s how you can add the Negotiated Volume-Based Adjustment Rate element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
IMPORTANT Ensure that you complete these prerequisites before you calculate a usage resource’s volume negotiated rate.
Add Rating Setting as the first element in the rating procedure.
Add the Negotiated Rate Card Entries element before the Negotiated Volume-Based Adjustment element, as the Rate Card Entry ID output from the former is used as an input in the latter.
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element and the Negotiated Rate Card Entries . See Rating Element and Negotiated Rate Card Entries.
Click , and then find and select the Negotiated Volume-Based Rate Adjustment element from the list.
In the Lookup Table Details field, search for and select the Asset Volume-based Rate Adjustment lookup table.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
On the Input tab, enter the variables to simulate and verify your calculations,
Enter variable values either in JSON format (Advanced) or in the fields (Simplified).
Click Simulate and verify that the calculations are per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.
EXAMPLE JSON input values:
{
  "UsageRatableSummary": [
    {
      "ProductSellingModel": "",
      "UsageRatableSummaryId": "1Guxx0000004CIiCAM",
      "TierRateCardEntry": "",
      "OverageQuantity": "1",
      "UsageResource": "1BRDU0000000UjC4AU",
      "NetUnitRateUom": "0hEDU0000000UlK2AU",
      "Asset": "02iDU0000005hosYAA",
      "RatingDecisionDateTime": "2024-12-19T00:00:00.000Z",
      "TierRateCard": "",
      "IsTierNegotiated": "",
      "BaseRateCard": "",
      "SellableProduct": ""
    }
  ]
}

=== ARTICLE: ind.rm_add_rating_get_rate_cards.htm ===
---
article_id: ind.rm_add_rating_get_rate_cards.htm
title: Add Get Rate Cards Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_add_rating_get_rate_cards.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_element_get_rate_cards.htm
fetched_at: 2026-09-07
---

# Add Get Rate Cards Element

Here’s how you can add the Get Rate Cards element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element. See Rating Element.
Click , and then find and select the Get Rate Cards element from the list.
In the Lookup Table Details field, search for and select your custom made lookup table.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
On the Input tab, enter the variables to simulate and verify your calculations,
Enter variable values either in JSON format (Advanced) or in the fields (Simplified).
Click Simulate and verify that the calculations are per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.

=== ARTICLE: ind.rm_clone_the_default_rating_discovery_procedure.htm ===
---
article_id: ind.rm_clone_the_default_rating_discovery_procedure.htm
title: Clone the Default Rating Discovery Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_clone_the_default_rating_discovery_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_discovery_procedures.htm
fetched_at: 2026-09-07
---

# Clone the Default Rating Discovery Procedure

Clone the predefined rating discovery procedure available with Rate Management and customize it. You can also build a custom rating discovery procedure to meet your business’s unique needs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create, update, delete, and clone rating discovery procedures:	

Pricing Discovery

AND

Rate Management Design Time User

IMPORTANT The default rating procedure uses the Usage Ratable Summary object, which isn't generally available. Get access to the object by contacting your Salesforce account executive or create your own mappings by using your own context definition.
From the App Launcher, find and select Expression Set Templates.
Select Default Rating Discovery Procedure.
Salesforce shows the rating discovery procedure in the Rating Procedure builder.
Click Save As | New Rating Discovery Procedure.
Enter a name and description for the rating procedure.
Save your changes.

Salesforce clones and saves the new rating discovery procedure. You can find the newly cloned rating discovery procedure in the Rating Discovery Procedures list.

=== ARTICLE: ind.rm_clone_the_default_rating_procedure.htm ===
---
article_id: ind.rm_clone_the_default_rating_procedure.htm
title: Create a Rating Procedure by Cloning the Expression Set Template
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_clone_the_default_rating_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management_setup.htm
fetched_at: 2026-09-07
---

# Create a Rating Procedure by Cloning the Expression Set Template

Clone a predefined rating procedure template, such as the Default Rating Procedure and the Negotiable Rating Procedure, available with Rate Management. You can also build a custom rating procedure to meet your business’s unique needs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, delete, and clone rating procedures:	Rate Management Design Time User
IMPORTANT Turn on Transaction Management to view and invoke asset-based lookup tables involved in the negotiable rating procedure. Alternatively, create your own custom lookup tables.
From the App Launcher, find and select Expression Set Templates.
Select an expression set template, for example, Default Rating Procedure or the Negotiable Rating Procedure.
On the Details tab, in the Rating Procedure Versions section, click the rating procedure version that you want to work on.
Salesforce opens the Rating Procedure builder in a new tab.
Click Save As | New Rating Procedure.
Enter a name and description for the rating procedure.
Save your changes.
SEE ALSO
Enabling Revenue Settings

=== ARTICLE: ind.rm_commitment_rate_adjustment.htm ===
---
article_id: ind.rm_commitment_rate_adjustment.htm
title: Commitment Rate Adjustment
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_commitment_rate_adjustment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Commitment Rate Adjustment

The Commitment Rate Adjustment element applies rate adjustments and calculates rates for commitment-based products.

REQUIRED EDITIONS
Commitment Rate Adjustment Variables

Map the variables in the Commitment-based Rate Adjustment lookup table to the relevant context tags.

Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Asset Rate Card Entry: Asset ID	Asset	The ID of the asset record that's related to the sellable product that the usage resource is associated with.
Asset Rate Card Entry: Start Date	RatingDecisionDateTime	The start date of the transaction.
Asset Rate Card Entry: End Date	RatingDecisionDateTime	The end date of the transaction.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	Create a custom tag	Enter the adjustment type applicable to the usage resource.
Adjustment Value	Create a custom tag	Enter the adjustment value applicable to the usage resource.
Rate Card Entry: Usage Resource ID	Create a custom tag	The ID of the usage resource.
Rate Card Entry: Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Input Unit Rate	NetUnitRate	The total rate of the usage resource.
Output Usage Resource Field Name	Create a custom tag	The name of the usage resource.
Usage Resource	UsageResource	The ID of the usage resource.
Usage Category	UsageResourceCategory__std	The category of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	CommitRate_std	The rate that's applicable to the usage resource consumed post the application of commitment discount.

=== ARTICLE: ind.rm_configure_your_rating_discovery_procedure.htm ===
---
article_id: ind.rm_configure_your_rating_discovery_procedure.htm
title: Configure Your Rating Discovery Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_configure_your_rating_discovery_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_discovery_procedures.htm
fetched_at: 2026-09-07
---

# Configure Your Rating Discovery Procedure

To retrieve rate cards, rate card entries, and related adjustments based on the filter criteria for the context input, use Rating discovery procedures.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
To use rating procedures:	Rate Management Run Time User
From the App Launcher, find and select Rating Discovery Procedures.
Click New.
Specify these details.
Enter a name and then press Tab to autopopulate the API Name.
Select Rating Discovery as the usage type.
Select a context definition.
Save your changes.
Salesforce shows the record page of the new rating discovery procedure.
On the Details tab, in the Rating Discovery Procedure Versions section, click the rating discovery procedure version that you want to work on.
Salesforce opens the Rating Discovery Procedure builder in a new tab.
Click , and select a rating discovery element from the list in this order.
Get Rate Cards
Get Rate Card Entries
Get Tier-Based Rate Adjustments or Get Attribute-Based Rate Adjustments
Alternatively, you can also drag the rating element from the Elements panel to the builder canvas. To open the Elements panel, click .
In the Lookup Table Details field, select the lookup table.
Enter the values for input and output variables.
Save your procedure.

=== ARTICLE: ind.rm_create_a_base_rate_card_entry.htm ===
---
article_id: ind.rm_create_a_base_rate_card_entry.htm
title: Create a Rate Card Entry for Base Rate Cards
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_create_a_base_rate_card_entry.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_card_entries.htm
fetched_at: 2026-09-07
---

# Create a Rate Card Entry for Base Rate Cards

Define a per-unit rate applicable to the usage resource. When creating a new rate card entry for Base Rate Cards, you define the per-unit rate that will be applied to the usage resource. This per-unit rate specifies the cost or charge for each unit of the resource consumed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create rate cards entries:	Rate Management Design Time
From the App Launcher, find and select Rate Management.
From the app navigation menu, select Rate Cards.
Open a rate card record of type base.
Click Rate Card Entries, and then click New.
Search for and select a usage resource, a sellable product and select its product selling model.
Specify the rate and its unit of measure, such as currency or token.
Choose if the rate is negotiable or non-negotiable.
Select the status.
Draft	Indicates that the rate card entry is open for modifications. This is the default value.
Active	Indicates that the rate card entry is in use for rating the usage-based products and you can make limited modifications, such as the status of the record.
Inactive	

Indicates that the rate card entry is not in use anymore.

Set the date range, and then save your changes.
SEE ALSO
Create Usage Resources

=== ARTICLE: ind.rm_create_a_rate_card.htm ===
---
article_id: ind.rm_create_a_rate_card.htm
title: Create a Rate Card
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_create_a_rate_card.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_cards_and_rate_card_entries.htm
fetched_at: 2026-09-07
---

# Create a Rate Card

A rate card defines the group of rules that are applicable to rate the usage resources granted with the sold product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create rate cards:	Rate Management Design Time
From the App Launcher, find and select Rate Management.
From the app navigation menu, select Rate Cards.
Click New.
Enter a rate card name and a description.
Select a rate card type.
Base	To define a flat rate for the consumption of usage resources.
Tier	To define rate adjustments based on the consumption quantity of the usage resource.
Set a date range.
Save your changes.

=== ARTICLE: ind.rm_create_a_tier_rate_card_entry.htm ===
---
article_id: ind.rm_create_a_tier_rate_card_entry.htm
title: Create a Rate Card Entry For Tier Rate Cards
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_create_a_tier_rate_card_entry.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_card_entries.htm
fetched_at: 2026-09-07
---

# Create a Rate Card Entry For Tier Rate Cards

Define different tiers of consumption for a usage resource and set a rate for each of these tiers. With tier-based adjusted rates, provide discounts to customers who have varying consumptions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create rate cards entries:	Rate Management Design Time
From the App Launcher, find and select Rate Management.
From the app navigation menu, select Rate Cards.
Open a rate card record of type tier.
Click Rate Card Entries, and then click New.
Search for and select a usage resource, a sellable product and select its product selling model.
Select the status.
Draft	Indicates that the rate card entry is open for modifications. This is the default value.
Active	Indicates that the rate card entry is in use for rating the usage-based products and you can make limited modifications, such as the status of the record.
Inactive	

Indicates that the rate card entry is not in use anymore.

Search for and select a unit of measure for the rate, such as currency or token.
Choose if the rate is negotiable or non-negotiable.
Set the date range, and then click Next.
Enter the Lower Bound and Upper Bound values.
These values represent the minimum and maximum consumption quantity for a usage resource.
IMPORTANT Values are inclusive and the tiers can’t overlap.
Select an adjustment type.
Percentage	Applies discounts on the usage resource’s consumption in percentage.
Amount	Applies a flat discount amount on the usage resource’s consumption.
Override	Overrides the net unit rate calculated for the usage resource.
Specify the adjustment value.
If the tier type is Percentage, the tier value is the percentage value of the discount, for example, 10%. If the tier type is Amount, the tier value is the flat amount of the discount, for example, $100.
To add more tier-based adjustment rates, click Add Tier.
Save your changes.
SEE ALSO
Create Usage Resources

=== ARTICLE: ind.rm_create_price_book_rate_cards.htm ===
---
article_id: ind.rm_create_price_book_rate_cards.htm
title: Create Price Book Rate Cards
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_create_price_book_rate_cards.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management_setup.htm
fetched_at: 2026-09-07
---

# Create Price Book Rate Cards

To determine the rates for a usage resource, map the price book related to the sellable product with a rate card that’s related to the corresponding usage resource. Create a Price Book Rate Card record for each rate card type, such as Base or Tier.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create rate cards:	Rate Management Design Time
From the App Launcher, find and select Price Book Rate Cards.
Click New.
Select a price book and a rate card.
Save your changes.

=== ARTICLE: ind.rm_discover_and_explore.htm ===
---
article_id: ind.rm_discover_and_explore.htm
title: Explore Rate Management in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_discover_and_explore.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management.htm
fetched_at: 2026-09-07
---

# Explore Rate Management in Revenue Management

Learn about the licenses required to use rate management and the personas each license supports. Understand the key terms and things to consider when you implement rate management for your organization.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Rate Management Permission Set Licenses
Manage the Rate Management functionality easily and securely by using permission set licenses. Add permissions so that specific user personas can complete the work that's assigned to their role.
Key Roles in Rate Management
Multiple users who work in various capacities within an organization can use and manage a usage resource’s rates.
External Objects Used in Rate Management
Rate management is part of a larger suite of products under Revenue Management. Because these products are closely integrated, rate management uses several objects that belong to other products within Industries and Revenue Management.
Implementation Considerations for Rate Management
Learn about the limitations in Rate Management and the points to keep in mind when you plan your implementation.

=== ARTICLE: ind.rm_element_add_assignment.htm ===
---
article_id: ind.rm_element_add_assignment.htm
title: Assignment
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_assignment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Assignment

Use the Assignment element to set and change the context tag values of variables.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time
IMPORTANT The Assignment element needs the outputs of the preceding rating elements. This requirement doesn’t apply to the Rating Setting, Rounding Values, and Stop Rating elements.

Input variable provides data to your Assignment element. Identify which variables you want to use as inputs. Similarly, identify output elements that form the results.

From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element.
Add an element whose output value you want to assign to another variable by using the Assignment element.
Click  and add the Assignment element.
Modify the tag values of the input and output variables based on how you want the variable values to be consumed.
Save, simulate, and activate your rating procedure.
EXAMPLE Override the calculated net unit rate when the quantity consumed is over a specific limit. Let’s assume the customer was granted 100 SMS with the mobile plan. By the end of the month, the user consumed 250 SMS. In this scenario, you want to override the net unit rate for the SMS consumed beyond 100 SMS.

To override the net unit rate, use the List Operation element and create a condition to verify whether the value in the OverageQuantity context tag is greater than 100. When the condition is met, the assignment element copies the OVERRIDE_NET_RATE constant value and assigns it to the NetUnitRate variable.

=== ARTICLE: ind.rm_element_add_base_rate_element.htm ===
---
article_id: ind.rm_element_add_base_rate_element.htm
title: Add the Base Rate Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_base_rate_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_base_rate.htm
fetched_at: 2026-09-07
---

# Add the Base Rate Element

Here’s how you can add the Base Rate element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element. See Rating Element.
Click , and then find and select the Base Rate element from the list.
In the Lookup Table Details field, search for and select the Rate Card Entries 2 lookup table.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
NOTE When more than one enabled version matches a rating procedure, choose the version with the highest rank. For example, if two enabled versions have rank values set to 1 and 2, choose the version with rank 2.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
On the Input tab, enter variable values.
You can enter the values either in JSON format (Advanced) or in the fields (Simplified).
In the Input tab, click Simulate.
Verify that the calculations are as per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.
EXAMPLE Sample JSON input values:
{
  "UsageRatableSummary": [
    {
      "RatingDecisionDateTime": "2024-08-07T12:59:47.403Z",
      "OverageQuantity": "5",
      "NetUnitRateUom": "0hEDU00000000Vf2AI",
      "ProductSellingModel": "",
      "UsageResource": "1BRDU00000000UP4AY",
      "SellableProduct": "",
      "BaseRateCard": "1CIDU00000000SJ4AY",
      "UsageRatableSummaryId": "1GuDU00000000My4AI"
    }
  ]
}

=== ARTICLE: ind.rm_element_add_manual_rate_discount.htm ===
---
article_id: ind.rm_element_add_manual_rate_discount.htm
title: Add the Manual Rate Discount Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_manual_rate_discount.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_manual_rate_discount.htm
fetched_at: 2026-09-07
---

# Add the Manual Rate Discount Element

Here’s how you can add the Manual Rate Discount element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
IMPORTANT Ensure that you complete these prerequisites before you calculate a usage resource’s volume discount.
Add Rating Setting as the first element in the rating procedure.
To set rates for your usage resource, use the Base Rate element or set the adjustment type for the rate card entries to Override.
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element and the base rate of the usage resource.
See Rating Setting and Base Rate.
Click , and then select the Manual Rate Discount element from the list.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
NOTE When more than one enabled version matches a rating procedure, choose the version with the highest rank. For example, if two enabled versions have rank values set to 1 and 2, choose the version with rank 2.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
Salesforce shows the Simulation Details with the input mode selected as Simplified by default.
In the Input tab, enter variable values.
You can enter the values either in JSON format (Advanced) or in the fields (Simplified).
In the Input tab, click Simulate.
Verify that the calculations are as per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.
EXAMPLE Sample JSON input values:
{
  "UsageRatableSummary": [
    {
      "RatingDecisionDateTime": "2024-08-07T12:59:47.403Z",
      "OverageQuantity": "5",
      "NetUnitRateUom": "0hEDU00000000Vf2AI",
      "ProductSellingModel": "",
      "UsageResource": "1BRDU00000000UP4AY",
      "SellableProduct": "",
      "BaseRateCard": "1CIDU00000000SJ4AY",
      "UsageRatableSummaryId": "1GuDU00000000My4AI"
    }
  ]
}

=== ARTICLE: ind.rm_element_add_negotiated_base_rate.htm ===
---
article_id: ind.rm_element_add_negotiated_base_rate.htm
title: Add the Negotiated Base Rate Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_negotiated_base_rate.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_negotiated_base_rate.htm
fetched_at: 2026-09-07
---

# Add the Negotiated Base Rate Element

Here’s how you can add the Negotiated Base Rate element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element. See Rating Element.
NOTE To access and view asset-based lookup tables, make sure Transaction Management is enabled. Alternatively, create and use custom lookup tables.
Click , and then find and select the Negotiated Base Rate element from the list.
In the Lookup Table Details field, search for and select the Asset Rate lookup table.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
On the Input tab, enter the variables to simulate and verify your calculations,
Enter variable values either in JSON format (Advanced) or in the fields (Simplified).
Click Simulate and verify that the calculations are per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.
EXAMPLE Sample JSON input values:
{
  "UsageRatableSummary": [
    {
      "ProductSellingModel": "",
      "UsageRatableSummaryId": "1Guxx0000004CIiCAM",
      "TierRateCardEntry": "",
      "OverageQuantity": "1",
      "UsageResource": "1BRDU0000000UjC4AU",
      "NetUnitRateUom": "0hEDU0000000UlK2AU",
      "Asset": "02iDU0000005hosYAA",
      "RatingDecisionDateTime": "2024-12-19T00:00:00.000Z",
      "TierRateCard": "",
      "IsTierNegotiated": "",
      "BaseRateCard": "",
      "SellableProduct": ""
    }
  ]
}

=== ARTICLE: ind.rm_element_add_negotiated_rate_card_entries_element.htm ===
---
article_id: ind.rm_element_add_negotiated_rate_card_entries_element.htm
title: Add the Negotiated Rate Card Entries Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_negotiated_rate_card_entries_element.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_negotiated_rate_card_entries.htm
fetched_at: 2026-09-07
---

# Add the Negotiated Rate Card Entries Element

Here’s how you can add the Negotiated Rate Card Entries element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element. See Rating Element.
NOTE To access and view asset-based lookup tables, make sure that Transaction Management is enabled. Alternatively, create and use custom lookup tables.
Click , and then find and select the Negotiated Rate Card Entries element from the list.
In the Lookup Table Details field, search for and select the Asset Rate Card Entry lookup table.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
On the Input tab, enter the variables to simulate and verify your calculations,
Enter variable values either in JSON format (Advanced) or in the fields (Simplified).
Click Simulate and verify that the calculations are per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.
EXAMPLE JSON input values:
{
  "UsageRatableSummary": [
    {
      "ProductSellingModel": "",
      "UsageRatableSummaryId": "1Guxx0000004CIiCAM",
      "TierRateCardEntry": "",
      "OverageQuantity": "1",
      "UsageResource": "1BRDU0000000UjC4AU",
      "NetUnitRateUom": "0hEDU0000000UlK2AU",
      "Asset": "02iDU0000005hosYAA",
      "RatingDecisionDateTime": "2024-12-19T00:00:00.000Z",
      "TierRateCard": "",
      "IsTierNegotiated": "",
      "BaseRateCard": "",
      "SellableProduct": ""
    }
  ]
}

=== ARTICLE: ind.rm_element_add_rate_adjustment_matrix.htm ===
---
article_id: ind.rm_element_add_rate_adjustment_matrix.htm
title: Add the Rate Adjustment Matrix Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_rate_adjustment_matrix.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_rate_adjustment_matrix.htm
fetched_at: 2026-09-07
---

# Add the Rate Adjustment Matrix Element

Here’s how you can add the Rate Adjustment Matrix element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
IMPORTANT Ensure that you complete these prerequisites before you calculate a usage resource’s volume discount.
Add Rating Setting as the first element in the rating procedure.
To set rates for your usage resource, use the Base Rate element or set the adjustment type for the rate card entries to Override.
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element and the base rate of the usage resource.
See Rating Setting and Base Rate.
Click , and then select the Rate Adjustment Matrix element from the list.
In the Lookup Table Details field, search for and select your custom rate adjustment matrix.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
NOTE When more than one enabled version matches a rating procedure, choose the version with the highest rank. For example, if two enabled versions have rank values set to 1 and 2, choose the version with rank 2.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
Salesforce shows the Simulation Details with the input mode selected as Simplified by default.
In the Input tab, enter variable values.
You can enter the values either in JSON format (Advanced) or in the fields (Simplified).
In the Input tab, click Simulate.
Verify that the calculations are as per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.

=== ARTICLE: ind.rm_element_add_rounding_values.htm ===
---
article_id: ind.rm_element_add_rounding_values.htm
title: Add the Rounding Values Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_rounding_values.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_rounding_values.htm
fetched_at: 2026-09-07
---

# Add the Rounding Values Element

Use the Rounding Values element to ensure that all rating elements added to the rating procedure work for different currencies in a single currency org.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
IMPORTANT Create a rating procedure to calculate the rate of a product by using the Manual Rate Discount or Volume-Based Rate Discount elements.
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element and the base rate of the usage resource.
See Rating Setting and Base Rate.
Click , and then select the Rounding Values element from the list.
If you’re on a single currency org, specify a value for the Precision variable.
If you don’t map the Precision variable to the correct context tag or constant resource, the rounding rule isn't applied to the resource’s final rate.
Assign an input variable, such as TotalAmount, to an output variable and select the rounding rule.
To add more rules and variables, select Add more variables and rules.
Save your procedure and then simulate it.
The rate details in the Waterfall View show the rounded rate for the usage resource.

=== ARTICLE: ind.rm_element_add_tier_based_rate_discount.htm ===
---
article_id: ind.rm_element_add_tier_based_rate_discount.htm
title: Add the Tier-Based Rate Discount Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_tier_based_rate_discount.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_tier_based_rate_discount.htm
fetched_at: 2026-09-07
---

# Add the Tier-Based Rate Discount Element

Here’s how you can add the Tier-Based Rate Discount element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
IMPORTANT Ensure that you complete these prerequisites before you calculate a usage resource’s volume discount.
Add Rating Setting as the first element in the rating procedure.
To set rates for your usage resource, use the Base Rate element or set the adjustment type for the rate card entries to Override.
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element and the base rate of the usage resource.
See Rating Setting and Base Rate.
Click , and then select the Tier-Based Rate Discount element from the list.
In the Lookup Table Details field, search for and select a lookup table.
NOTE To calculate non-negotiable rates, use the Rate Adjustment by Tier Entries 2 lookup table. For negotiable rates, use the Tier-based Rate Adjustment by Rate Card Entry ID.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
NOTE When more than one enabled version matches a rating procedure, choose the version with the highest rank. For example, if two enabled versions have rank values set to 1 and 2, choose the version with rank 2.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
Salesforce shows the Simulation Details with the input mode selected as Simplified by default.
In the Input tab, enter variable values.
You can enter the values either in JSON format (Advanced) or in the fields (Simplified).
In the Input tab, click Simulate.
Verify that the calculations are as per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.
EXAMPLE Sample JSON input values:
{
  "UsageRatableSummary": [
    {
      "RatingDecisionDateTime": "2024-08-07T12:59:47.403Z",
      "OverageQuantity": "5",
      "NetUnitRateUom": "0hEDU00000000Vf2AI",
      "ProductSellingModel": "",
      "UsageResource": "1BRDU00000000UP4AY",
      "SellableProduct": "",
      "BaseRateCard": "1CIDU00000000SJ4AY",
      "UsageRatableSummaryId": "1GuDU00000000My4AI",
      "TierRateCard": "1CIDU00000000SO4AY"
    }
  ]
}

=== ARTICLE: ind.rm_element_add_volume_based_rate_discount.htm ===
---
article_id: ind.rm_element_add_volume_based_rate_discount.htm
title: Add the Volume-Based Rate Discount Element
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_add_volume_based_rate_discount.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_volume_based_rate_discount.htm
fetched_at: 2026-09-07
---

# Add the Volume-Based Rate Discount Element

Here’s how you can add the Volume-Based Rate Discount element to your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
IMPORTANT Ensure that you complete these prerequisites before you calculate a usage resource’s volume discount.
Add Rating Setting as the first element in the rating procedure.
To set rates for your usage resource, use the Base Rate element or set the adjustment type for the rate card entries to Override.
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version.
Define the Rating Setting element and the base rate of the usage resource.
See Rating Setting and Base Rate.
Click , and then select the Volume-Based Rate Discount element from the list.
In the Lookup Table Details field, search for and select a lookup table.
NOTE To calculate non-negotiable rates, use the Rate Adjustment by Volume Entries 2 lookup table. For negotiable rates, use the Volume-based Rate Adjustment by Rate Card Entry ID.
Map your variables to the appropriate context tags.
Click , and enter 1 as the rank number.
NOTE When more than one enabled version matches a rating procedure, choose the version with the highest rank. For example, if two enabled versions have rank values set to 1 and 2, choose the version with rank 2.
Click , select Include in Output, and save your rating procedure.
Click Simulate.
Salesforce shows the Simulation Details with the input mode selected as Simplified by default.
In the Input tab, enter variable values.
You can enter the values either in JSON format (Advanced) or in the fields (Simplified).
In the Input tab, click Simulate.
Verify that the calculations are as per your rating settings.
The Waterfall View shows every step of the rating calculation.
When you’re happy with the simulation result, click Activate.
EXAMPLE Sample JSON input values:
{
  "UsageRatableSummary": [
    {
      "RatingDecisionDateTime": "2024-08-07T12:59:47.403Z",
      "OverageQuantity": "5",
      "NetUnitRateUom": "0hEDU00000000Vf2AI",
      "ProductSellingModel": "",
      "UsageResource": "1BRDU00000000UP4AY",
      "SellableProduct": "",
      "BaseRateCard": "1CIDU00000000SJ4AY",
      "UsageRatableSummaryId": "1GuDU00000000My4AI",
      "TierRateCard": "1CIDU00000000SO4AY"
    }
  ]
}

=== ARTICLE: ind.rm_element_base_rate.htm ===
---
article_id: ind.rm_element_base_rate.htm
title: Base Rate
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_base_rate.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Base Rate

To calculate the base rate of a usage resource based on the rate card type, use the Base Rate element.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

An organization can have different rates for the same resource based on a customer’s consumption. They can track these rates by using rate cards. The Base Rate element can track the resource rates entered into rate cards.

Base Rate Variables
To monitor rates, use the RateManagementContext context definition and associate the Base Rate element with the Rate Card Entries lookup table.
Add the Base Rate Element
Here’s how you can add the Base Rate element to your rating procedure.

=== ARTICLE: ind.rm_element_base_rate_variables.htm ===
---
article_id: ind.rm_element_base_rate_variables.htm
title: Base Rate Variables
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_base_rate_variables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_base_rate.htm
fetched_at: 2026-09-07
---

# Base Rate Variables

To monitor rates, use the RateManagementContext context definition and associate the Base Rate element with the Rate Card Entries lookup table.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Map the variables in the lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card	BaseRateCard	The ID of the rate card of type base.
Usage Resource	UsageResource	The ID of the usage resource.
Product	SellableProduct	The ID of the sellable product related to the usage resource.
Rate Unit Of Measure	NetUnitRateUom	The standard unit of measure related to the rate card.
Product Selling Model	ProductSellingModel	The method used to sell a product.
Effective From	RatingDecisionDateTime	The start date of the transaction.
Effective To	RatingDecisionDateTime	The end date of the transaction.
Status	Predefined Constant	Specify whether the rate card entry is draft, active, or inactive.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate	Create a custom tag	Enter the base rate applicable to the usage resource.
Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Quantity	OverageQuantity	Specify the quantity of the line items used in the transaction.
Base Rate Field	Predefined constant	The field name refers to the rate column of the selected base rate.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Base Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.

=== ARTICLE: ind.rm_element_bora.htm ===
---
article_id: ind.rm_element_bora.htm
title: Get Binding Object Rate Adjustment
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_bora.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_discovery_procedure_elements.htm
fetched_at: 2026-09-07
---

# Get Binding Object Rate Adjustment

To retrieve the binding object rate adjustment ID(s) and map the variables to the relevant context tags, use the Binding Object Rate Adjustment Resolution Entries lookup table.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	BindingObjectRateAdjustmentType__std	The adjustment type for the tier adjustment.
Adjustment Value	BindingObjectRateAdjustmentValue__std	The adjustment value for the adjustment type.
Binding Object Rate Adjustment ID	BindingObjectRateAdjustmentId__std	The ID of the binding object rate adjustment.
Lower Bound	BindingObjectRateAdjustmentLowerBound__std	The minimum number of units for a usage product.
Upper Bound	BindingObjectRateAdjustmentUpperBound__std	The maximum number of units for a usage product.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Card Entry ID	BindingObjectRateCardEntryId__std	The ID of the binding object rate card entry.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Adjustment ID	BindingObjectRateAdjustmentId__std	The ID of the binding object rate adjustment.

To retrieve the asset rate adjustment IDs and map the variables to the relevant context tags, use the Asset Rate Adjustment Resolution Entries lookup table.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Asset Rate Card Entry	AssetRateCardEntryId__std	The ID of the asset rate card entry.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	AssetRateAdjustmentType__std	The adjustment type for the tier adjustment.
Adjustment Value	AssetRateAdjustmentValue__std	The adjustment value for the adjustment type.
Asset Rate Adjustment ID	AssetRateAdjustmentId__std	The ID of the asset rate adjustment.
Lower Bound	AssetRateAdjustmentLowerBound__std	The minimum number of units for a usage product.
Upper Bound	Create a custom tag	The maximum number of units for a usage product.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Card Entry ID	AssetRateCardEntryId__std	The ID of the asset rate card entry.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Adjustment ID	AssetRateAdjustmentId__std	The ID of the asset rate adjustment.

=== ARTICLE: ind.rm_element_formula_based_rating.htm ===
---
article_id: ind.rm_element_formula_based_rating.htm
title: Formula-Based Rating
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_formula_based_rating.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Formula-Based Rating

The Formula-Based Rating element performs functions and mathematical calculations to generate the rate of a usage resource.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
EXAMPLE Provide a formula to update the net unit rate of the usage products by adding a constant number (3) to it.
Add the Formula-Based Rating element to your rating procedure.
In the Input Variable section, in the Calculation Formula field, add a mathematical formula by using context tags or constant resources.
In the Output Variable field, specify the context tag that stores the calculation formula’s result.

Here, we're using the NetUnitRate context tag used to update the net unit rate of the usage resource by 3 units.

=== ARTICLE: ind.rm_element_get_borce.htm ===
---
article_id: ind.rm_element_get_borce.htm
title: Get Binding Object Rate Card Entries
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_get_borce.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_discovery_procedure_elements.htm
fetched_at: 2026-09-07
---

# Get Binding Object Rate Card Entries

To retrieve the binding object rate card entry IDs and map the variables to the relevant context tags, use the Binding Object Rate Card Entry Resolution Entries 2 lookup table.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Usage Resource	FilterNodeUsageResourceId__std	The ID of the usage resource related to the binding object rate card entry.
Rate Unit Of Measure	FilterNodeRateUnitofMeasureId__std	The unit of measure of the rate defined for the usage resource.
Effective From	FilterNodeEffectiveFrom__std	The date when the binding object rate card entry becomes active.
Effective To	FilterNodeEffectiveFrom__std	The date when the binding object rate card entry becomes active.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Order	Create a custom tag	It determines the applicable binding object rate when multiple rates are defined for an Anchor target within an effective period.
Binding Object Rate Card Entry ID	BindingObjectRateCardEntryRateCardId__std	The ID of the binding object rate card entry.
Negotiated Rate	BindingObjectRateCardEntryNegotiatedRate__std	The negotiated rate associated with the binding object rate card entry.
Rate Card Type	BindingObjectRateCardEntryRateCardType__std	The type of rate card, such as attribute or tier.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object ID	FilterNodeBindingObjectId__std	The ID of the binding object related to the rate card entry.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card Entry ID	RateCardEntryId	The ID of the rate card entry associated with the binding object.
Binding Object Rate Card Entry ID	BindingObjectRateCardEntryId__std	The ID of the binding object rate card entry.

To retrieve the asset rate card entry IDs and map the variables to the relevant context tags, use the Asset Rate Card Entry Resolution Entries lookup table.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Formula	FilterNodeBindingObjectId__std	The formula that returns the ID of the associated binding object, if specified. If binding object isn't added, the formula returns the asset ID of the asset related to this asset rate card entry.
Usage Resource ID	FilterNodeUsageResourceId__std	The ID of the usage resource related to the binding object rate card entry.
Start Date	FilterNodeEffectiveFrom__std	The date when the binding object rate card entry becomes active.
End Date	FilterNodeEffectiveFrom__std	The date when the binding object rate card entry becomes active.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Order	Create a custom tag	It determines the applicable binding object rate when multiple rates are defined for an Anchor target within an effective period.
Asset Rate Card Entry ID	AssetRateCardEntryId__std	The ID of the asset rate card entry.
Negotiated Rate	AssetRateCardEntryNegotiatedRate__std	The negotiated rate associated with the asset rate card entry.
Rate Card Type	Create a custom tag	The type of rate card, such as Base and Tier.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object ID	FilterNodeBindingObjectId__std	The binding object associated with the asset rate card entry.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card Entry ID	RateCardEntryId	The ID of the rate card entry.
Binding Object Rate Card Entry ID	AssetRateCardEntryId__std	The ID of the asset rate card entry.

=== ARTICLE: ind.rm_element_get_rate_card_entries.htm ===
---
article_id: ind.rm_element_get_rate_card_entries.htm
title: Get Rate Card Entries
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_get_rate_card_entries.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_discovery_procedure_elements.htm
fetched_at: 2026-09-07
---

# Get Rate Card Entries

Select the Rate Card Entry Resolution Entries 2 lookup table to fetch the rate card entries related to the rate card fetched by using the Get Rate Card element. Then, map the variables to the relevant context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Effective From	FilterEffectiveFrom	The date when the rate card entry becomes active.
Effective To	FilterEffectiveFrom	The date when the rate card entry becomes active.
Usage Resource	FilterUsageResource	The ID of the usage resource related to the rate card entry.
Product	FilterProduct	The ID of the sellable product.
Product Selling Model	FilterProductSellingModel__std	The method used to sell a product.
Rate Unit Of Measure	FilterRateUoM	The unit of measure of the rate defined for the usage resource.
Status	Predefined Constant	Specify whether the rate card entry is draft, active, or inactive.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Default Unit Of Measure	DefaultUnitOfMeasure	The default unit of measure applicable to the usage resource.
Rate Card Entry ID	RateCardEntryId	The ID of the rate card entry.
Rate	Rate	The rate defined for the rate card.
Rate Card Type	RCType	The type of rate card, such as attribute or tier.
Rate Unit Of Measure Name	RateUnitOfMeasureName	The unit of measure applicable for the rate defined in the rate card.
Usage Product	UsageProduct	The ID of the usage product that the rates are defined for.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card ID	RateCardId	The ID of the rate card.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card Entry ID	RateCardEntryId	The ID of the rate card entry.

=== ARTICLE: ind.rm_element_get_rate_cards.htm ===
---
article_id: ind.rm_element_get_rate_cards.htm
title: Get Rate Cards
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_get_rate_cards.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_discovery_procedure_elements.htm
fetched_at: 2026-09-07
---

# Get Rate Cards

Select the Pricebook Rate Card Entries lookup table to fetch the rate card and map the variables to the relevant context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card Type	RCType	The type of rate card, such as attribute or tier.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Price Book	PricebookId	The ID of the pricebook.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card ID	RateCardId	The ID of the rate card.

=== ARTICLE: ind.rm_element_get_tier_based_rate_adjustments.htm ===
---
article_id: ind.rm_element_get_tier_based_rate_adjustments.htm
title: Get Tier-Based Rate Adjustments
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_get_tier_based_rate_adjustments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_discovery_procedure_elements.htm
fetched_at: 2026-09-07
---

# Get Tier-Based Rate Adjustments

Select the Rate Adjustment by Tier Resolution Entries lookup table to fetch the tier-based adjustments, and then map the variables to the relevant context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	TierAdjustmentType	The adjustment type for the tier adjustment.
Adjustment Value	TierAdjustmentValue	The adjustment value for the adjustment type.
Rate Adjustment By Tier ID	RateAdjustmentByTierID	The ID of the rate adjustment by tier record associated with the rate card entry.
Lower Bound	TierLowerBound	The minimum number of units for a usage resource.
Upper Bound	TierUpperBound	The maximum number of units for a usage resource.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card Entry ID	RateCardEntryId	The ID of the rate card entry.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Adjustment By Tier ID	RateAdjustmentByTierID	The ID of the rate adjustment by tier record.

=== ARTICLE: ind.rm_element_list_group_list_operation.htm ===
---
article_id: ind.rm_element_list_group_list_operation.htm
title: List Group and List Operation
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_list_group_list_operation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# List Group and List Operation

A list group element filters items in a list based on the filter conditions and then performs further operations on the filtered lists. A list operation is always the first step in the list group and defines how items in the list are filtered.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

When you create a list group, your first element, List Operation, defines how items in the list are filtered. The rating elements added later within the list group depend on the conditions applied.

EXAMPLE Create a List Group element and filter the base rate based on the consumption over the base limit. For consumption over 100 units, give a 10% discount. Here’s how to configure your list group element and rating procedure.
Ensure that you already created your rating procedure and configured rating settings.
Add the List Group rating element to the procedure.
In the list group, configure the list operation to filter consumption over 100 units.
Add a calculation step and calculate the updated base rate after applying the 10% discount.

In this image, we see that the list operation applied has the condition that the overage quantity must be greater than 100 units. When this condition is met, the rating procedure moves to the Formula-Based Rating element to calculate the net unit rate for the usage resource.

If a customer consumes fewer than 100 units of the usage resource, it doesn’t meet the condition, and the rating procedure skips this step altogether. When a customer consumes more than 100 units of usage resource, the procedure applies a discount of 10% to the net unit rate.

Simulate and verify the data that’s queried. When you activate the rating procedure, the Waterfall view shows every step of the rating calculation and the discounts applied.

=== ARTICLE: ind.rm_element_manual_rate_discount.htm ===
---
article_id: ind.rm_element_manual_rate_discount.htm
title: Manual Rate Discount
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_manual_rate_discount.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Manual Rate Discount

The Manual Rate Discount element calculates the final price of a product after you manually enter the external discounts.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Manual discounts support adjustment types such as number, percentage, and currency. The adjustment type determines the type of calculation performed. For example, if you select the Amount adjustment type and the adjustment value is 10, a discount of US$10 is applied to the usage resource. Similarly, a 10% discount is applied to the usage resource's value if you select the Percentage adjustment type.

For example, create rating rules for users with a voucher that makes them eligible to receive an additional discount of 10% on all their consumption.

Manual Rate Discount Variables
To calculate discounts, use the RateManagementContext context definition and map the variables to the relevant context tags.
Add the Manual Rate Discount Element
Here’s how you can add the Manual Rate Discount element to your rating procedure.

=== ARTICLE: ind.rm_element_manual_rate_discount_variables.htm ===
---
article_id: ind.rm_element_manual_rate_discount_variables.htm
title: Manual Rate Discount Variables
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_manual_rate_discount_variables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_manual_rate_discount.htm
fetched_at: 2026-09-07
---

# Manual Rate Discount Variables

To calculate discounts, use the RateManagementContext context definition and map the variables to the relevant context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Map the variables in the lookup table to the relevant context tags.

Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	Create a custom tag	The adjustment type.
Adjustment Value	Create a custom tag	The adjustment value.
Quantity	OverageQuantity	Specify the quantity that’s consumed over the granted quantity.
Input Unit Rate	

NetUnitRate

This context tag is populated based on the output generated from the previous element.

	The rate details of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.

=== ARTICLE: ind.rm_element_negotiated_base_rate.htm ===
---
article_id: ind.rm_element_negotiated_base_rate.htm
title: Negotiated Base Rate
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_negotiated_base_rate.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Negotiated Base Rate

To calculate the negotiated rates applied on the base rate of the usage resource, use the Negotiated Base Rate element. The negotiated base rate element uses the Asset Rate lookup table to determine if rates were negotiated. If rates weren't negotiated, the element uses base rates.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Negotiated Base Rate Variables

Map the variables in the Asset Rate 2 lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Asset Rate Card Entry ID	Asset	The ID of the asset record that's related to the sellable product that the usage resource is associated with.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Negotiated Rate	Create a custom tag	The negotiated rate applied to the base rate of the usage resource under the asset.
Rate Card Entry: Rate	Create a custom tag	The original rate derived from the rate card entry.
Rate Card Entry: Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Base Rate Field	Predefined constant	The field name refers to the rate column of the selected base rate.
Quantity	OverageQuantity	Specify the quantity of the line items used in the transaction.
Negotiated Rate Field	Predefined Constant	The field name refers to the negotiated rate column of the selected base rate.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Base Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.
Add the Negotiated Base Rate Element
Here’s how you can add the Negotiated Base Rate element to your rating procedure.

=== ARTICLE: ind.rm_element_negotiated_baserate_bindingobject.htm ===
---
article_id: ind.rm_element_negotiated_baserate_bindingobject.htm
title: Negotiated Base Rate for Binding Object
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_negotiated_baserate_bindingobject.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Negotiated Base Rate for Binding Object

Use the Negotiated Base Rate element to calculate the negotiated target-specific rates. The negotiated base rate element uses the Binding Object Rate lookup table to determine if rates were negotiated. If rates weren't negotiated, the element uses base rates.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Negotiated Base Rate Variables

Map the variables in the Binding Object Rate 2 lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Card Entry ID	BindingObject__std	The ID of the binding object rate card entry record that's related to the sellable product that the usage resource is associated with.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Negotiated Rate	Create a custom tag	The negotiated rate applied to the base rate of the usage resource under the asset.
Rate Card Entry: Rate	Create a custom tag	The original rate derived from the rate card entry.
Rate Card Entry: Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Base Rate Field	Predefined constant	The field name refers to the rate column of the selected base rate.
Quantity	OverageQuantity	Specify the quantity of the line items used in the transaction.
Negotiated Rate Field	Predefined Constant	The field name refers to the negotiated rate column of the selected base rate.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Base Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.

=== ARTICLE: ind.rm_element_negotiated_rate_card_entries.htm ===
---
article_id: ind.rm_element_negotiated_rate_card_entries.htm
title: Negotiated Rate Card Entries
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_negotiated_rate_card_entries.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Negotiated Rate Card Entries

Use the Negotiated Rate Card Entries element to determine the Rate Card Entry ID from the Asset ID.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Negotiated Rate Card Entries Variables

Map the variables in the Asset Rate Card Entry 2 lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Formula	Asset	The ID of the asset record that's related to the sellable product that the usage resource is associated with.
Usage Resource ID	UsageResource	The ID of the usage resource that's negotiated.
Unit of Measure ID	NetUnitRateUom	The ID of the standard unit of measure related to the rate card.
Start Date	RatingDecisionDateTime	The start date of the transaction.
End Date	RatingDecisionDateTime	The end date of the transaction.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Order	Create a custom tag	The order that determines the applicable binding object rate when multiple rates are defined for an Anchor target within an effective period.
Asset Rate Card Entry ID	Create a custom tag	The Asset Rate Card Entry ID associated with the Asset ID.
Rate Card Entry ID	Create a custom tag	The Rate Card Entry ID associated with the Asset ID.
Rate Card Entry: Rate Card Type	Create a custom tag	Specify if the rate card type is Attribute, Base, or Tier.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Tier Rate Card Entry ID	TierRateCardEntry	The ID of the Rate Card Entry of type Tier.
Base Rate Card Entry ID	BaseRateCardEntry	The ID of the Rate Card Entry of type Tier.
Binding Object Base Rate Card Entry	BindingObjectBaseRateCardEntry__std	The Binding Object Rate Card Entry of type Base.
Binding Object Tier Rate Card Entry	BindingObjectTierRateCardEntry__std	The Binding Object Rate Card Entry of type Tier.
Add the Negotiated Rate Card Entries Element
Here’s how you can add the Negotiated Rate Card Entries element to your rating procedure.

=== ARTICLE: ind.rm_element_negotiated_tierbased_adjustment.htm ===
---
article_id: ind.rm_element_negotiated_tierbased_adjustment.htm
title: Negotiated Tier-Based Rate Adjustment
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_negotiated_tierbased_adjustment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Negotiated Tier-Based Rate Adjustment

The Negotiated Tier-Based Rate Adjustment element calculates the negotiated rate for a usage resource based on the defined tiers, applying either a discount or a surcharge.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
EXAMPLE Let’s assume that you’re consuming 100-GB data for your organization. The unit rate of 1-GB data is US$0.5, and your service provider offers you these tier-based discounts.
No discount for data consumption of fewer than 10 GB.
1% discount for each GB consumed when 11–60 GB of data is consumed.
2% discount for each GB consumed when 61–100 GB of data is consumed.

Here’s how the post-negotiation, the discounts are applied and the total amount is calculated.

QUANTITY	POST NEGOTIATION	TOTAL
RATE
First 10 GB	No discounts applied for the first 10 GB	10 x 0.5 = $5
Next 50 GB	10% off for licenses 11–60 GB	50 x 0.45 = $22.5
Last 40 GB	20% off for licenses 61–100 GB	40 x 0.4 = $16
Negotiated Tier-Based Adjustment Variables
Map the variables in the Asset Tier-Based Rate Adjustment 2 lookup table to the relevant context tags.
Add Negotiated Tier-Based Rate Adjustment
Here’s how you can add the Negotiated Tier-based Rate Adjustment element to your rating procedure.

=== ARTICLE: ind.rm_element_negotiated_tierbased_rate_adjustment.htm ===
---
article_id: ind.rm_element_negotiated_tierbased_rate_adjustment.htm
title: Negotiated Tier-Based Adjustment Variables
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_negotiated_tierbased_rate_adjustment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_negotiated_tierbased_adjustment.htm
fetched_at: 2026-09-07
---

# Negotiated Tier-Based Adjustment Variables

Map the variables in the Asset Tier-Based Rate Adjustment 2 lookup table to the relevant context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT
TAG
DESCRIPTION
Asset ID	Asset	The ID of the asset record that's related to the sellable product with which the usage resource is associated.
Rate Card Entry ID	

TierRateCardEntry

This context tag is populated based on the output generated from the Negotiated Rate Card Entries element.

	The ID of the Rate Card Entry of type tier.
Start Date	RatingDecisionDateTime	The start date of the transaction.
End Date	RatingDecisionDateTime	The end date of the transaction.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	Create a custom tag	The adjustment type.
Adjustment Value	Create a custom tag	The adjustment value.
Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Quantity	OverageQuantity	Specify the quantity of the line items used in the transaction.
Input Unit Rate	NetUnitRate	The rate details of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.
Is Tier Negotiated	IsTierNegotiated	Specify if the Rate Card Entry of type tier is negotiated.

=== ARTICLE: ind.rm_element_negotiated_tierbasedadjustment_bindingobject.htm ===
---
article_id: ind.rm_element_negotiated_tierbasedadjustment_bindingobject.htm
title: Negotiated Tier-Based Rate Adjustment for Binding Object
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_negotiated_tierbasedadjustment_bindingobject.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Negotiated Tier-Based Rate Adjustment for Binding Object

Use the Negotiated Tier-Based Rate Adjustment element to fetch the tier-based rate adjustment with bound range related to the binding object ID specified in the decision table along with other input values.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Negotiated Tier-Based Adjustment Variables

Map the variables in the Binding Object Tier-based Rate Adjustment 2 lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Card Entry: Binding Object ID	BindingObject__std	The ID of the binding object record that's related to the sellable product that the usage resource is associated with.
Rate Card Entry ID	TierRateCardEntry	The ID of the Rate Card Entry of type Tier.
Start Date	RatingDecisionDateTime	The start date of the transaction.
End Date	RatingDecisionDateTime	The end date of the transaction.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	Create a custom tag	The adjustment type.
Adjustment Value	Create a custom tag	The adjustment value.
Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Quantity	OverageQuantity	Specify the quantity of the line items used in the transaction.
Input Unit Rate	NetUnitRate	The rate details of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.
Is Tier Negotiated	IsTierNegotiated	Specify if the Rate Card Entry of type Tier is negotiated.

=== ARTICLE: ind.rm_element_negotiatedratecardentries_bindingobject.htm ===
---
article_id: ind.rm_element_negotiatedratecardentries_bindingobject.htm
title: Negotiated Rate Card Entries for Binding Object
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_negotiatedratecardentries_bindingobject.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Negotiated Rate Card Entries for Binding Object

Use the Negotiated Rate Card Entries element to determine the Rate Card Entry ID from the Binding Object Rate Card Entry ID.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Negotiated Rate Card Entries Variables

Map the variables in the Binding Object Rate Card Entry 2 lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object ID	BindingObject__std	The ID of the binding object record that's related to the sellable product that the usage resource is associated with.
Usage Resource ID	UsageResource	The ID of the usage resource that's negotiated.
Unit of Measure ID	NetUnitRateUom	The ID of the standard unit of measure related to the rate card.
EffectiveFrom	RatingDecisionDateTime	The start date of the transaction.
EffectiveTo	RatingDecisionDateTime	The end date of the transaction.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Binding Object Rate Order	Create a custom tag	Determines the applicable binding object rate when multiple rates are defined for an Anchor target within an effective period.
Binding Object Rate Card Entry ID	Create a custom tag	The ID of the Binding Object Rate Card Entry.
Rate Card Entry ID	Create a custom tag	The Rate Card Entry ID associated with the Binding Object ID.
Rate Card Type	Create a custom tag	Specify if the rate card type is Attribute, Base, or Tier.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Tier Rate Card Entry ID	TierRateCardEntry	The ID of the Rate Card Entry of type Tier.
Base Rate Card Entry ID	BaseRateCardEntry	The ID of the Rate Card Entry of type Base.
 	 	 
Binding Object Base Rate Card Entry	BindingObjectBaseRateCardEntry__std	The ID of the Binding Object Rate Card Entry of type Base.
Binding Object Tier Rate Card Entry	BindingObjectTierRateCardEntry__std	The ID of the Binding Object Rate Card Entry of type Tier.

=== ARTICLE: ind.rm_element_negotited_volumebasedadjustment_bindingobject.htm ===
---
article_id: ind.rm_element_negotited_volumebasedadjustment_bindingobject.htm
title: Negotiated Volume-Based Rate Adjustment for Binding Object
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_negotited_volumebasedadjustment_bindingobject.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Negotiated Volume-Based Rate Adjustment for Binding Object

Use the Negotiated Volume-Based Rate Adjustment element to fetch the volume-based rate adjustment related to the binding object ID specified in the decision table along with other input values.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Negotiated Volume-Based Adjustment Variables

Map the variables in the Binding Object Volume-Based Rate Adjustment 2 lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
 	 	 
Binding Object Rate Card Entry ID	BindingObjectTierRateCardEntry__std	The ID of the rate card entry of type Tier.
Lower Bound	OverageQuantity	The minimum number of units for a usage product.
Upper Bound	OverageQuantity	The maximum number of units for a usage product.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	Create a custom tag	Enter the adjustment type applicable to the usage resource.
Adjustment Value	Create a custom tag	Enter the adjustment value applicable to the usage resource.
Rate Card Entry: Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Quantity	OverageQuantity	Specify the quantity that’s consumed over the granted quantity.
Input Unit Rate	NetUnitRate	The rate details of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.
Is Tier Negotiated	IsTierNegotiated	Specify whether the Rate Card Entry of type Tier is negotiated.

=== ARTICLE: ind.rm_element_rate_adjustment_matrix.htm ===
---
article_id: ind.rm_element_rate_adjustment_matrix.htm
title: Rate Adjustment Matrix
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_rate_adjustment_matrix.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Rate Adjustment Matrix

The Rate Adjustment Matrix element calculates the rate of a usage resource based on the discounts configured for a set of custom conditions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Create rating rules for a usage resource rated differently in different parts of the world. For example, data storage can be rated differently in Europe compared to the rest of the world, depending on service costs, taxes, and other government regulations.

Rate Adjustment Matrix Variables
To calculate discounts, use the RateManagementContext context definition and relate it to a custom rate adjustment matrix.
Add the Rate Adjustment Matrix Element
Here’s how you can add the Rate Adjustment Matrix element to your rating procedure.

=== ARTICLE: ind.rm_element_rate_adjustment_matrix_variables.htm ===
---
article_id: ind.rm_element_rate_adjustment_matrix_variables.htm
title: Rate Adjustment Matrix Variables
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_rate_adjustment_matrix_variables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_rate_adjustment_matrix.htm
fetched_at: 2026-09-07
---

# Rate Adjustment Matrix Variables

To calculate discounts, use the RateManagementContext context definition and relate it to a custom rate adjustment matrix.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Map the variables in the lookup table to the relevant context tags.

NOTE Based on your custom adjustment matrix, you can have dynamic input and output rule variables. In this task, we’re describing only the fixed input and output variables.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type Field	AttributeKey	The field name refers to the adjustment type column of the selected rate adjustment matrix.
Adjustment Value Field	AttributeValue	The field name refers to the adjustment value column of the selected rate adjustment matrix.
Quantity	OverageQuantity	Specify the quantity that’s consumed over the granted quantity.
Input Unit Rate	

NetUnitRate

This context tag is populated based on the output generated from the previous element.

	The rate details of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.

=== ARTICLE: ind.rm_element_rating_setting.htm ===
---
article_id: ind.rm_element_rating_setting.htm
title: Rating Setting
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_rating_setting.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Rating Setting

Use the Rating Setting element to map commonly used variables in a rating procedure to context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Some of the variables within the Rating Setting element are mandatory. By setting tags in the Rating Setting element, you save the time required for entering the same information for later elements. When you build a rating procedure, you must add the Rating Setting element as the first rating element.

NOTE You can modify the set context tags for the subsequent rating elements in your rating procedure. The tag in the rating element precedes the tags in the Rating Setting element.

=== ARTICLE: ind.rm_element_rounding_values.htm ===
---
article_id: ind.rm_element_rounding_values.htm
title: Rounding Values
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_rounding_values.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Rounding Values

The Rounding Values element assists in precisely calculating the rate of a usage resource by using rounding rules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
IMPORTANT
The Rounding Values element sets the rounding precision for an org that doesn’t have multicurrency enabled. When multicurrency is enabled, the org's settings determine the precision, and you can adjust decimal places for each currency through Manage Currencies in Setup. See Manage Multiple Currencies.
The Rounding Values element determines the currency values for the outputs of preceding rating elements such as Manual Rate Discount and Volume-Based Rate Discount.

Here are the rounding rules.

Round Up
Apply this rule to round up the currency value of a resource to the nearest higher value. For example, if a storage unit costs US$1.7, use the round up rule to adjust the rate to $2.
Round Down
Apply this rule to round down the currency value of a resource to the nearest lower value. For example, if a storage unit costs $1.30, use the round down rule to adjust the rate to $1.
Half Up
Apply this rule to round up the currency value of a resource to the nearest number based on the decimal value. For example, if a storage unit costs $1.45 and you select the Half Up rule, the rate is adjusted to $1.5. However, if the storage unit costs $1.20, then the rate is adjusted to $1.
Add the Rounding Values Element
Use the Rounding Values element to ensure that all rating elements added to the rating procedure work for different currencies in a single currency org.

=== ARTICLE: ind.rm_element_stop_rating.htm ===
---
article_id: ind.rm_element_stop_rating.htm
title: Stop Rating
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_stop_rating.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Stop Rating

Use the Stop Rating element to stop the execution of the rating procedure for a particular line item. During simulation, the Waterfall view shows the element that the rating procedure stopped at.

=== ARTICLE: ind.rm_element_tier_based_rate_discount.htm ===
---
article_id: ind.rm_element_tier_based_rate_discount.htm
title: Tier-Based Rate Discount
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_tier_based_rate_discount.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Tier-Based Rate Discount

The Tier-Based Rate Discount element determines the discount for a usage resource based on the quantity consumed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

The tier-based rate discount element is similar to the volume-based rate discount element in terms of usage. The primary difference is that a standard flat discount rate is applied to all usage resources when you use the volume-based rate discount element. When you use the tier-based rate discount method, you define a range-based discount for the usage resource based on the quantity consumed.

EXAMPLE Let’s assume that you’re consuming 100-GB data for your organization. The unit rate of 1-GB data is US$0.5, and your service provider offers you these tier-based discounts.
No discount for data consumption of fewer than 10 GB.
10% discount for each GB data consumed when 11–60 GB are consumed.
20% discount for each GB data consumed when 61–100 GB are consumed.

Here’s how the discounts are applied, and the total amount is calculated.

QUANTITY	DISCOUNTS APPLIED	TOTAL RATE
First 10 GB	No discounts applied for the first 10 GB	10 x 0.5 = $5
Next 50 GB	10% off for licenses 11–60 GB	50 x 0.45 = $22.5
Last 40 GB	20% off for licenses 61–100 GB	40 x 0.4 = $16
Add the Tier-Based Rate Discount Element
Here’s how you can add the Tier-Based Rate Discount element to your rating procedure.

=== ARTICLE: ind.rm_element_volume_based_rate_discount.htm ===
---
article_id: ind.rm_element_volume_based_rate_discount.htm
title: Volume-Based Rate Discount
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_volume_based_rate_discount.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Volume-Based Rate Discount

The Volume-Based Rate Discount element calculates the usage resource rate based on the discounts configured for the quantities consumed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

For example, create rating rules for a usage resource that’s eligible for a 25% discount for 100 MBs or more units consumed over the granted limits. And a customer consumes 150 MBs.

Volume-Based Rate Discount Variables for Non-Negotiable Rates
To calculate non-negotiable rates, use the RateManagementContext context definition and relate the Volume-Based Rate Discount element with the Rate Adjustment by Volume Entries 2 lookup table.
Volume-Based Rate Discount Variables for Negotiable Rates
To calculate negotiable rates, relate the Volume-Based Rate Discount element with the Volume-based Rate Adjustment by Rate Card Entry ID lookup table.
Add the Volume-Based Rate Discount Element
Here’s how you can add the Volume-Based Rate Discount element to your rating procedure.

=== ARTICLE: ind.rm_element_volume_based_rate_discount_variables.htm ===
---
article_id: ind.rm_element_volume_based_rate_discount_variables.htm
title: Volume-Based Rate Discount Variables for Non-Negotiable Rates
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_volume_based_rate_discount_variables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_volume_based_rate_discount.htm
fetched_at: 2026-09-07
---

# Volume-Based Rate Discount Variables for Non-Negotiable Rates

To calculate non-negotiable rates, use the RateManagementContext context definition and relate the Volume-Based Rate Discount element with the Rate Adjustment by Volume Entries 2 lookup table.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Map the variables in the lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card	TierRateCard	The ID of the selected rate card of type tier.
Usage Resource	UsageResource	The ID of the usage resource.
Product	SellableProduct	The ID of the sellable product related to the usage resource.
Rate Unit Of Measure	NetUnitRateUom	The standard unit of measure related to the rate card.
Product Selling Model	ProductSellingModel	The method used to sell a product.
Effective From	RatingDecisionDateTime	The start date of the transaction.
Effective To	RatingDecisionDateTime	The end date of the transaction.
Lower Bound	OverageQuantity	The minimum number of units for a usage product for a tier.
Upper Bound	OverageQuantity	The maximum number of units for a usage product for a tier.
Rate Card Entry Status	Predefined Constant	Specify whether the rate card entry is draft, active, or inactive.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	Create a custom tag	The adjustment type.
Adjustment Value	Create a custom tag	The adjustment value.
Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Quantity	OverageQuantity	Specify the quantity that’s consumed over the granted quantity.
Input Unit Rate	

NetUnitRate

This context tag is populated based on the output generated from the previous element.

	The rate details of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.

=== ARTICLE: ind.rm_element_volume_based_rate_discount_variables_negotiable_rates.htm ===
---
article_id: ind.rm_element_volume_based_rate_discount_variables_negotiable_rates.htm
title: Volume-Based Rate Discount Variables for Negotiable Rates
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_element_volume_based_rate_discount_variables_negotiable_rates.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_element_volume_based_rate_discount.htm
fetched_at: 2026-09-07
---

# Volume-Based Rate Discount Variables for Negotiable Rates

To calculate negotiable rates, relate the Volume-Based Rate Discount element with the Volume-based Rate Adjustment by Rate Card Entry ID lookup table.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Map the variables in the lookup table to the relevant context tags.

Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card Entry	TierRateCardEntry	The ID of the selected rate card entry of type tier.
Lower Bound	OverageQuantity	The minimum number of units for a usage product for a tier.
Upper Bound	OverageQuantity	The maximum number of units for a usage product for a tier.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	Create a custom tag	The adjustment type.
Adjustment Value	Create a custom tag	The adjustment value.
Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Quantity	OverageQuantity	Specify the quantity that’s consumed over the granted quantity.
Input Unit Rate	

NetUnitRate

This context tag is populated based on the output generated from the previous element.

	The rate details of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.

=== ARTICLE: ind.rm_enable_rate_management.htm ===
---
article_id: ind.rm_enable_rate_management.htm
title: Enable Rate Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_enable_rate_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management_setup.htm
fetched_at: 2026-09-07
---

# Enable Rate Management

Give your users access to the Rate Management objects and features.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To enable Rate Management:	Customize Application
In Setup, find and select Usage Management | Usage Management Settings.
Turn on Rate Management.

=== ARTICLE: ind.rm_enable_rating_waterfall_persistence.htm ===
---
article_id: ind.rm_enable_rating_waterfall_persistence.htm
title: Enable Rating Waterfall Persistence
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_enable_rating_waterfall_persistence.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management_setup.htm
fetched_at: 2026-09-07
---

# Enable Rating Waterfall Persistence

Waterfall persistence stores the rating logs in a structured manner within the Salesforce database. Rating waterfall logs capture the sequence of rating decisions applied during execution for efficient tracking and retrieval of rating information.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To turn on rating waterfall persistence:	Rate Management Admin

If you turn on the rating waterfall without enabling waterfall persistence, keep these things in mind:

The active session or API responses shows the rating logic. However, after the transaction is finalized, the steps behind rating disappear. If your user disputes a charge three months later, you can only see the final price because the step-by-step logs aren’t available.

Rating waterfall persistence stores detailed rating execution logs for every transaction. Over time, this increasing data storage usage can have a minor impact on overall system performance, especially in high-volume environments. If you process numerous transactions and don’t require historical step-level traceability for audits or dispute resolution, keep persistence turned off to avoid unnecessary storage pile up.
From Setup, in the Quick Find box, enter Usage Management, and then select Rate Management Setup.
Turn on Rating Waterfall Persistence.
SEE ALSO
Revenue Cloud Developer Guide: Line Item Waterfall Response

=== ARTICLE: ind.rm_external_objects_used_in_rate_management.htm ===
---
article_id: ind.rm_external_objects_used_in_rate_management.htm
title: External Objects Used in Rate Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_external_objects_used_in_rate_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_discover_and_explore.htm
fetched_at: 2026-09-07
---

# External Objects Used in Rate Management

Rate management is part of a larger suite of products under Revenue Management. Because these products are closely integrated, rate management uses several objects that belong to other products within Industries and Revenue Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Here’s the list of the external objects used in Rate Management and their descriptions.

OBJECT	DESCRIPTION
Usage Resource	An entitlement or service that’s granted with the product sold to your customer. Typically, usage resources are consumables, such as data storage or computing power. Customers are charged based on the quantity that they use over the granted limit or specified period.
Product	Any item or service sold to your customer. To create products, see Products.
Product Classification	A template that you use to create similar products. Typically, products that are based on a product classification inherit all attributes of the product classification. To create product classifications, see Product Classifications.
Attribute Definition	A product has characteristics or properties known as attributes. You can use attributes to determine or calculate discounts. To create attributes, see Dynamic Attributes.
Attribute Based Adjustment	An attribute-based discount for a product within a date range. See Attribute Based Adjustments.
Product Selling Model	Define how you sell your products through product selling models. You can sell products one time or through subscription plans. To create a product selling model, see Product Selling Model.
Unit of Measure Class	A standard unit of measure dimension, such as currency, volume, or length.
Unit of Measure	A unit of measure that rates are defined in, such as USD or EUR.
Price Book	A list of products and their prices. See Manage Price Books.

To view the list of objects that rate management supports, see the Rate Management object documentation.

In addition to other Industries and Revenue Management objects, Rate Management relies on the use of decision tables. Decision tables are complex lookup tables that read business rules with multiple inputs and return multiple outputs. See Decision Table.

=== ARTICLE: ind.rm_implementation_considerations.htm ===
---
article_id: ind.rm_implementation_considerations.htm
title: Implementation Considerations for Rate Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_implementation_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_discover_and_explore.htm
fetched_at: 2026-09-07
---

# Implementation Considerations for Rate Management

Learn about the limitations in Rate Management and the points to keep in mind when you plan your implementation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
To create Unit of Measure records for Rate Management, you must add picklist values for the Type field on the Unit Of Measure object.
Rate card entry uses the same default unit of measure that’s defined in the related usage resource record.
Only Salesforce admins can create and run batch jobs for Rate Management.
Starting in Summer ’25, admins can choose between decision tables and real-time data for rating procedures. The real-time data option ensures accuracy but impacts performance. Conversely, not using real-time data can enhance performance but requires manual updates of decision tables when base rates, tiers, or adjustments change, or during the quote capture and order lifecycle. To avoid the overhead of manual refreshes and to ensure precise data retrieval, we recommend that you select the data retrieval method that most closely meets your unique needs and performance criteria.
Real-time data doesn't support the "not matches" or "contains" operators. If you’re using customized decision tables that include these operators, we recommend manually syncing the decision tables.
Rate Management provides real-time data support for these elements available in the respective procedures.
Rating Discovery Procedure
Get Binding Object Rate Adjustment
Get Binding Object Rate Card Entries
Negotiable Rating Procedure
Negotiated Rate Card Entries
Negotiated Base Rate
Negotiated Volume-Based Rate Adjustment
Commitment Rate Adjustment
For optimized data retrieval while running rating procedures, make sure that the number of decision tables in your org is within the specified limits. To know the maximum number of decision tables supported in an org, see Business Rules Engine Default Limits.

=== ARTICLE: ind.rm_key_roles_in_rate_management.htm ===
---
article_id: ind.rm_key_roles_in_rate_management.htm
title: Key Roles in Rate Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_key_roles_in_rate_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_discover_and_explore.htm
fetched_at: 2026-09-07
---

# Key Roles in Rate Management

Multiple users who work in various capacities within an organization can use and manage a usage resource’s rates.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
ROLE	WHAT THEY CAN DO
Rate Management Admin	
Turn on Rate Management
Create and manage all Rate Management objects and features.

Rate Management Manager	
Access the Rate Management app
Create, read, update, and delete access to the records created on Rate Management, such as rate card and rate card entries.

Rate Management Design Time User	Access the rating procedure feature and all rating elements.
Rate Management Run Time User	Read rate management data and can call Rate Management APIs.
NOTE The System Admin can create and manage Rate Management batch features and assign permissions to control access to these features.

=== ARTICLE: ind.rm_map_line_item.htm ===
---
article_id: ind.rm_map_line_item.htm
title: Map Line Item
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_map_line_item.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Map Line Item

Use the Map Line Item element for precise mapping of variables. This element maps variables at the level of the main line item and the level of the sub-line items, which are created when multiple transactions occur on the same line item.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Map Line Item Variables

Map your variables to the appropriate context tags at both the context node level and the child node level.

Input variables:
UsageRatableSummary
Asset
UsageRatableSummaryId
CommitRate__std
RatingDecisionDateTime
Output Variables:
UsageRatableSummaryCommitmemtAssetRate__std
URSCARCommitmentAsset__std
URSCARId__std
URSCARNetUnitRate__std
URSCARRatingDecisionDateTime__std

=== ARTICLE: ind.rm_negotiated_volumebased_rate_adjustment.htm ===
---
article_id: ind.rm_negotiated_volumebased_rate_adjustment.htm
title: Negotiated Volume-Based Rate Adjustment
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_negotiated_volumebased_rate_adjustment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Negotiated Volume-Based Rate Adjustment

Ensure consistent surcharges or discounting across all relevant usage with the Negotiated Volume-Based Rate Adjustment element. The Negotiated Volume-Based Rate Adjustment element is similar to the Negotiated Tier-Based Rate Adjustment element. However, in volume-based rate adjustment, negotiated rates are applied uniformly to all quantities of the usage resource so that it's easier to uniformly manage volume-based negotiations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Negotiated Volume-Based Rate Adjustment Variables
Map the variables in the Asset Volume-based Rate Adjustment 2 lookup table to the relevant context tags.
Add Negotiated Volume-Based Rate Adjustment
Here’s how you can add the Negotiated Volume-Based Adjustment Rate element to your rating procedure.

=== ARTICLE: ind.rm_negotiated_volumebased_rate_adjutment_variables.htm ===
---
article_id: ind.rm_negotiated_volumebased_rate_adjutment_variables.htm
title: Negotiated Volume-Based Rate Adjustment Variables
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_negotiated_volumebased_rate_adjutment_variables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_negotiated_volumebased_rate_adjustment.htm
fetched_at: 2026-09-07
---

# Negotiated Volume-Based Rate Adjustment Variables

Map the variables in the Asset Volume-based Rate Adjustment 2 lookup table to the relevant context tags.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Input Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG DESCRIPTION
Asset Rate Card Entry: Asset ID	BindingObjectTierRateCardEntry__std	The ID of the Binding Object Rate Card Entry of type Tier.
Lower Bound	OverageQuantity	The minimum number of units for a usage product for a tier.
Upper Bound	OverageQuantity	The maximum number of units for a usage product for a tier.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Adjustment Type	Create a custom tag	Enter the adjustment type applicable to the usage resource.
Adjustment Value	Create a custom tag	Enter the adjustment value applicable to the usage resource.
Rate Card Entry: Rate Unit of Measure Name	Create a custom tag	Enter the standard unit of measure related to the rate card entry.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Quantity	OverageQuantity	Specify the quantity that’s consumed over the granted quantity.
Input Unit Rate	NetUnitRate	The rate details of the usage resource.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Net Unit Rate	NetUnitRate	The total rate of the usage resource.
Subtotal	TotalAmount	The subtotal rate for a usage resource.
Is Tier Negotiated	IsTierNegotiated	Specify whether the Rate Card Entry of type Tier is negotiated.

=== ARTICLE: ind.rm_prereqs_to_build_rating_procedures.htm ===
---
article_id: ind.rm_prereqs_to_build_rating_procedures.htm
title: Prerequisites for Building Rating Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_prereqs_to_build_rating_procedures.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_procedures.htm
fetched_at: 2026-09-07
---

# Prerequisites for Building Rating Procedures

Before you create rating procedures and add elements to them, complete these prerequisites.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Users must have the Rate Management Design Time user permission to:

Create context definitions.
Create, edit, and activate a decision table in Rate Management.
Create, update, and delete rating procedures.
NOTE Rate Management doesn't support CSV based decision tables and decision matrices.

Create custom lookup tables or use the predefined tables in the Rate Management solution. See Lookup Tables. By default, Salesforce provides these lookup tables.

To create, update, and delete rating procedures when rates are non negotiable, use these lookup tables:

Rate Card Entries 2
Rate Adjustment by Volume Entries 2
Rate Adjustment by Tier Entries 2
Rate Adjustment by Attribute Entries 2

To create, update, and delete rating procedures when rates are negotiable, use these lookup tables:

Rate Card Entries 2
Rate Adjustment by Volume Entries 2
Rate Adjustment by Tier Entries 2
Asset Rate Card Entry 2
Asset Rate 2
Asset Volume-based Rate Adjustment 2
Asset Tier-based Rate Adjustment 2
Tier-based Rate Adjustment by Rate Card Entry ID
Volume-based Rate Adjustment by Rate Card Entry ID
Binding Object Rate Card Entry 2
Binding Object Rate 2
Binding Object Volume-based Rate Adjustment 2
Binding Object Tier-based Rate Adjustment 2
Commitment-based Rate Adjustment
IMPORTANT Enable Transaction Management to view and invoke the asset-based lookup tables involved in the negotiable rating procedure. Alternatively, create your own lookup tables.
Enable the use of context definitions. The Rate Management solution includes its own predefined context definition called RateManagementContext for mapping the Usage Ratable Summary object. To customize parts of this context definition for reuse, extend or clone it, and make modifications. See Create Context Definitions.
To map the variables that don’t have context tags, create a constant resource. Constants are resource types that act as placeholders for fixed values in rating procedures for inputs, outputs, and other values passed from a rating element. See Create a Constant Resource.
SEE ALSO
Enabling Revenue Settings

=== ARTICLE: ind.rm_rate_card_entries.htm ===
---
article_id: ind.rm_rate_card_entries.htm
title: Rate Card Entries
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rate_card_entries.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_cards_and_rate_card_entries.htm
fetched_at: 2026-09-07
---

# Rate Card Entries

Use rate card entries to set rates and rate adjustments that are used to calculate and control the final net rate of each usage resource. The setup ensures that your deals are accurately rated. To make sure products are accurately charged during usage selling, define the pricing for your products in both standard currency and tokens.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management Advanced

You can configure Rate Card Entries (RCEs) by using either a currency or tokens. However, the Product Usage Resource (PUR) settings for a sellable product determine which rate (currency or token-based) is used during the Usage Selling process. Make sure your PUR configuration aligns with how you want to price the product for sale.

For tokens, create two Rate Card Entries (RCEs).

To convert usage to tokens, make sure the Rate Unit of Measures is the token unit.
To convert tokens to currency, make sure the Rate UoM is the currency.
Create a Rate Card Entry for Base Rate Cards
Define a per-unit rate applicable to the usage resource. When creating a new rate card entry for Base Rate Cards, you define the per-unit rate that will be applied to the usage resource. This per-unit rate specifies the cost or charge for each unit of the resource consumed.
Create a Rate Card Entry For Tier Rate Cards
Define different tiers of consumption for a usage resource and set a rate for each of these tiers. With tier-based adjusted rates, provide discounts to customers who have varying consumptions.

=== ARTICLE: ind.rm_rate_cards_and_rate_card_entries.htm ===
---
article_id: ind.rm_rate_cards_and_rate_card_entries.htm
title: Rate Cards and Rate Card Entries
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rate_cards_and_rate_card_entries.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management_setup.htm
fetched_at: 2026-09-07
---

# Rate Cards and Rate Card Entries

Define the rules that are used to rate the consumption of a group of usage resources within a product. If the customer consumes the usage resource beyond the granted limits or period, specific rates are applied.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

To define rates on the consumption quantity based on consumption tiers and the rate-impacting attributes of the usage resource, use rate card entries. Each entry is linked to one rate card and these rate card entries are effective until the specified effective dates. Manage the lifecycle of your rate card entries using the Status field, which allows you to set entries as draft, active, or inactive. You can transition draft entries to either active or inactive. Additionally, you can deactivate active entries or reactivate them as needed.

Create a Rate Card
A rate card defines the group of rules that are applicable to rate the usage resources granted with the sold product.
Rate Card Entries
Use rate card entries to set rates and rate adjustments that are used to calculate and control the final net rate of each usage resource. The setup ensures that your deals are accurately rated. To make sure products are accurately charged during usage selling, define the pricing for your products in both standard currency and tokens.

=== ARTICLE: ind.rm_rate_management.htm ===
---
article_id: ind.rm_rate_management.htm
title: Configure Rate Pricing Calculations in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rate_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
fetched_at: 2026-09-07
---

# Configure Rate Pricing Calculations in Revenue Management

Use Rate Management to easily define the rates for usage resources granted with the sellable product. Set up rates based on consumption of a usage resource. Define rate adjustments based on the consumption quantity of a usage resource. Use rating procedures to create precise formulas for calculating the final net rate and use the rating waterfall view to understand the rate breakup steps of the rating calculation process.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.
Explore Rate Management in Revenue Management
Learn about the licenses required to use rate management and the personas each license supports. Understand the key terms and things to consider when you implement rate management for your organization.
Rate Management Setup
Rate Management provides the key tools to manage rates for consumption-based products. To leverage these tools effectively, you must first complete the setup detailed in this section. This process represents our recommended base configuration and is a prerequisite for building any custom solution. It ensures essential procedures can be customized and data can be synchronized for accuracy. Complete all of the following steps before continuing to design your rating solution.
Rating Procedures
Rating procedures are customizable, ordered stacks of rating elements that are used to calculate the final net rate of a usage resource. Each rating element forms a step in a rating procedure. Rating elements call appropriate lookup tables to perform the rating calculations.
Rating Discovery Procedures
Rating discovery procedures fetch the binding objects, rate cards, rate card entries, and rate adjustments associated with multiple sellable products and usage resources related to a price book. Use the retrieved rate information to provide quotes for usage-based products to customers by using Quote and Order Capture and Asset Lifecycle.
Rate Management Limits
Review the default limits for Rate Management components and their usage. To modify the set default values, ask your Salesforce admin to raise a support ticket.

=== ARTICLE: ind.rm_rate_management_psls.htm ===
---
article_id: ind.rm_rate_management_psls.htm
title: Rate Management Permission Set Licenses
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rate_management_psls.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_discover_and_explore.htm
fetched_at: 2026-09-07
---

# Rate Management Permission Set Licenses

Manage the Rate Management functionality easily and securely by using permission set licenses. Add permissions so that specific user personas can complete the work that's assigned to their role.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Create Users and Profiles

To begin, create users for Rate Management. Then assign users the appropriate permission sets. To help you plan, refer to the permission set table for Rate Management.

When you create a user, you must also assign a profile. Profiles define default settings for users. Some organizations create their own profiles, while others choose to use profiles included with Salesforce.

Remember, users can have only one profile, but can have many permission sets assigned to them.

Assign Permissions
PERMISSION SET LICENSE NAME	DESCRIPTION	PERSONAS
Rate Management Design Time	Provide create, read, update, and delete access for all design time rate management objects.	

Rate Management Admin

Rate Management Design Time User


Rate Management Run Time	Provide read access for all run time rate management features.	

Rate Management Manager

Rate Management Run Time User

To view the count of the Rate Management permission set licenses that are available in your org, go to Company Information in Setup.

If you need permission set licenses in addition to the ones provided by the Rate Management license enabled in your org, contact your Salesforce account executive.

SEE ALSO
View and Manage Users
Create or Clone Profiles
Permission Set Licenses

=== ARTICLE: ind.rm_rate_management_setup.htm ===
---
article_id: ind.rm_rate_management_setup.htm
title: Rate Management Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rate_management_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management.htm
fetched_at: 2026-09-07
---

# Rate Management Setup

Rate Management provides the key tools to manage rates for consumption-based products. To leverage these tools effectively, you must first complete the setup detailed in this section. This process represents our recommended base configuration and is a prerequisite for building any custom solution. It ensures essential procedures can be customized and data can be synchronized for accuracy. Complete all of the following steps before continuing to design your rating solution.

Enable Rate Management
Give your users access to the Rate Management objects and features.
Enable Rating Waterfall
Rating Waterfall provides insights and reasons for every step of the rating process. Let's say that while calculating the final net rate of a usage resource, you find out that the discount is less than anticipated. With Waterfall View, you can view the rate breakups at every step along with the reason for the addition or deduction.
Enable Rating Waterfall Persistence
Waterfall persistence stores the rating logs in a structured manner within the Salesforce database. Rating waterfall logs capture the sequence of rating decisions applied during execution for efficient tracking and retrieval of rating information.
Create Price Book Rate Cards
To determine the rates for a usage resource, map the price book related to the sellable product with a rate card that’s related to the corresponding usage resource. Create a Price Book Rate Card record for each rate card type, such as Base or Tier.
Rate Cards and Rate Card Entries
Define the rules that are used to rate the consumption of a group of usage resources within a product. If the customer consumes the usage resource beyond the granted limits or period, specific rates are applied.
Create a Rating Procedure by Cloning the Expression Set Template
Clone a predefined rating procedure template, such as the Default Rating Procedure and the Negotiable Rating Procedure, available with Rate Management. You can also build a custom rating procedure to meet your business’s unique needs.
Simulate and Activate Your Rating Procedure
Before you activate your rating procedure, run simulations to test if the variables that you entered are accurate. If your rating procedure doesn’t work as expected, edit the values that you entered and try again. When you’re satisfied, activate the rating procedure version.
Select Rating Discovery Procedure
To select a rating discovery procedure, you must first clone the predefined rating discovery procedure available with Salesforce Rate Management. You can also build a custom rating procedure to meet the unique needs of your business.
Record Sharing for Rate Management
For runtime users to access the data created by rating designers, managers or catalog admins, set up record sharing for all the Rate Management entities.

=== ARTICLE: ind.rm_rate_mngmnt_limits.htm ===
---
article_id: ind.rm_rate_mngmnt_limits.htm
title: Rate Management Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rate_mngmnt_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management.htm
fetched_at: 2026-09-07
---

# Rate Management Limits

Review the default limits for Rate Management components and their usage. To modify the set default values, ask your Salesforce admin to raise a support ticket.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Rating Procedures
VALUE	DEFAULT	MINIMUM	MAXIMUM
The duration that a rating procedure can remain active	10000 milliseconds	1000 milliseconds	60000 milliseconds
The duration that a rating element can remain active	5000 milliseconds	4 milliseconds	10000 milliseconds
The number of rating elements in a rating procedure	70	2	100
The number of active decision tables in an org	50	0	1000
The maximum number of simultaneous lookup inputs allowed per HBPO-based decision table	1000	1	8000
Rating Discovery Procedures
VALUE	DEFAULT	MINIMUM	MAXIMUM
The duration that a rating discovery procedure can remain active	10000 milliseconds	1000 milliseconds	60000 milliseconds
The duration that a rating discovery element can remain active	5000 milliseconds	4 milliseconds	10000 milliseconds
The number of rating discovery elements in a rating discovery procedure	50	1	100
The number of active decision tables in an org	40	0	1000
The maximum number of simultaneous lookup inputs allowed for an org’s HBPO-based decision tables of the usage type Rating Discovery	2000	1	8000
Rate Card Entries
VALUE	LIMIT
The number of rate card entries	1200
The number of adjustment records associated with tier rate card entries	3000
Other Limitations
Rate Management isn’t supported on mobile devices.
Rate Management objects don't support the creation of records in Data Cloud.
Rate Management doesn't support CSV-based decision tables and decision matrices.
Attribute-based rate cards aren't supported in Usage Selling and Consumption Management. Avoid creating attribute-based rate cards or related customizations.

=== ARTICLE: ind.rm_rating_discovery_procedure_elements.htm ===
---
article_id: ind.rm_rating_discovery_procedure_elements.htm
title: Elements in a Rating Discovery Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rating_discovery_procedure_elements.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_discovery_procedures.htm
fetched_at: 2026-09-07
---

# Elements in a Rating Discovery Procedure

Use Rating Discovery Procedure to get rates for your usage resource based on the specified Binding Object ID or Pricebook ID.

REQUIRED EDITIONS

Here’s a list of the variables and the associated context tags of the Rating Discovery Procedure elements used to create a rating discovery procedure.

Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
NOTE If you use all the elements in a rating discovery procedure and provide the value of the output for an element in simulation, then that element isn’t considered for fetching the results. For example, you use the Get Rate Cards, Get Rate Card Entries, and Get Tier-Based Rate Adjustments elements in a sequence. If you provide a valid Pricebook ID and Rate Card ID record when you simulate the procedure, Rating Discovery Procedure skips the Get Rate Cards element from the procedure and fetches the rate card entries and rate adjustments related to the provided rate card record.
Get Binding Object Rate Adjustment
To retrieve the binding object rate adjustment ID(s) and map the variables to the relevant context tags, use the Binding Object Rate Adjustment Resolution Entries lookup table.
Get Binding Object Rate Card Entries
To retrieve the binding object rate card entry IDs and map the variables to the relevant context tags, use the Binding Object Rate Card Entry Resolution Entries 2 lookup table.
Get Rate Cards
Select the Pricebook Rate Card Entries lookup table to fetch the rate card and map the variables to the relevant context tags.
Get Rate Card Entries
Select the Rate Card Entry Resolution Entries 2 lookup table to fetch the rate card entries related to the rate card fetched by using the Get Rate Card element. Then, map the variables to the relevant context tags.
Get Tier-Based Rate Adjustments
Select the Rate Adjustment by Tier Resolution Entries lookup table to fetch the tier-based adjustments, and then map the variables to the relevant context tags.

=== ARTICLE: ind.rm_rating_discovery_procedures.htm ===
---
article_id: ind.rm_rating_discovery_procedures.htm
title: Rating Discovery Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rating_discovery_procedures.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management.htm
fetched_at: 2026-09-07
---

# Rating Discovery Procedures

Rating discovery procedures fetch the binding objects, rate cards, rate card entries, and rate adjustments associated with multiple sellable products and usage resources related to a price book. Use the retrieved rate information to provide quotes for usage-based products to customers by using Quote and Order Capture and Asset Lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license

Rating discovery procedure uses the predefined context definition called RatingDiscoveryContext that is used to map the Rate Management objects, such as Rate Card, Rate Card Entries, and Rate Adjustment by Tier. However, if you want to customize parts of this context definition for reuse, extend or clone it and make modifications. See Context Definitions.

Use these lookup tables for the rating discovery procedure:

Binding Object Rate Adjustment Resolution Entries
Binding Object Rate Card Entry Resolution Entries
Pricebook Rate Card Entries
Rate Card Entry Resolution Entries 2
Rate Adjustment by Tier Resolution Entries
Rate Adjustment by Attribute Resolution Entries
Clone the Default Rating Discovery Procedure
Clone the predefined rating discovery procedure available with Rate Management and customize it. You can also build a custom rating discovery procedure to meet your business’s unique needs.
Configure Your Rating Discovery Procedure
To retrieve rate cards, rate card entries, and related adjustments based on the filter criteria for the context input, use Rating discovery procedures.
Elements in a Rating Discovery Procedure
Use Rating Discovery Procedure to get rates for your usage resource based on the specified Binding Object ID or Pricebook ID.

=== ARTICLE: ind.rm_rating_element_get_rate_cards.htm ===
---
article_id: ind.rm_rating_element_get_rate_cards.htm
title: Get Rate Cards
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rating_element_get_rate_cards.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_elements.htm
fetched_at: 2026-09-07
---

# Get Rate Cards

Use the Get Rate Cards element to fetch the rate cards that you need for your rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Note: Use the existing Pricebook Rate Card Entries lookup table to create a new lookup table for the Get Rate Cards element. Use the get rate card element to fetch the rate card and map the variables to the relevant context tags.
Output Rule Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card Type	RCType	The type of rate card, such as attribute or tier.
Input Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Price Book	PricebookId	The ID of the pricebook.
Output Variables
PARAMETER NAME	MAPPED CONTEXT TAG	CONTEXT TAG’S DESCRIPTION
Rate Card ID	RateCardId	The ID of the rate card.
Add Get Rate Cards Element
Here’s how you can add the Get Rate Cards element to your rating procedure.

=== ARTICLE: ind.rm_rating_elements.htm ===
---
article_id: ind.rm_rating_elements.htm
title: Explore Available Rating Elements in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rating_elements.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rating_procedures.htm
fetched_at: 2026-09-07
---

# Explore Available Rating Elements in Revenue Management

Rating elements are the building blocks of a rating procedure. A new rating procedure is always blank, and each added element forms a step in the rating procedure. Use the available rating elements to form logical steps in the rating procedure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Rating Setting
Use the Rating Setting element to map commonly used variables in a rating procedure to context tags.
Base Rate
To calculate the base rate of a usage resource based on the rate card type, use the Base Rate element.
Volume-Based Rate Discount
The Volume-Based Rate Discount element calculates the usage resource rate based on the discounts configured for the quantities consumed.
Tier-Based Rate Discount
The Tier-Based Rate Discount element determines the discount for a usage resource based on the quantity consumed.
Negotiated Rate Card Entries
Use the Negotiated Rate Card Entries element to determine the Rate Card Entry ID from the Asset ID.
Negotiated Rate Card Entries for Binding Object
Use the Negotiated Rate Card Entries element to determine the Rate Card Entry ID from the Binding Object Rate Card Entry ID.
Negotiated Base Rate
To calculate the negotiated rates applied on the base rate of the usage resource, use the Negotiated Base Rate element. The negotiated base rate element uses the Asset Rate lookup table to determine if rates were negotiated. If rates weren't negotiated, the element uses base rates.
Negotiated Base Rate for Binding Object
Use the Negotiated Base Rate element to calculate the negotiated target-specific rates. The negotiated base rate element uses the Binding Object Rate lookup table to determine if rates were negotiated. If rates weren't negotiated, the element uses base rates.
Negotiated Tier-Based Rate Adjustment
The Negotiated Tier-Based Rate Adjustment element calculates the negotiated rate for a usage resource based on the defined tiers, applying either a discount or a surcharge.
Negotiated Tier-Based Rate Adjustment for Binding Object
Use the Negotiated Tier-Based Rate Adjustment element to fetch the tier-based rate adjustment with bound range related to the binding object ID specified in the decision table along with other input values.
Negotiated Volume-Based Rate Adjustment
Ensure consistent surcharges or discounting across all relevant usage with the Negotiated Volume-Based Rate Adjustment element. The Negotiated Volume-Based Rate Adjustment element is similar to the Negotiated Tier-Based Rate Adjustment element. However, in volume-based rate adjustment, negotiated rates are applied uniformly to all quantities of the usage resource so that it's easier to uniformly manage volume-based negotiations.
Negotiated Volume-Based Rate Adjustment for Binding Object
Use the Negotiated Volume-Based Rate Adjustment element to fetch the volume-based rate adjustment related to the binding object ID specified in the decision table along with other input values.
Commitment Rate Adjustment
The Commitment Rate Adjustment element applies rate adjustments and calculates rates for commitment-based products.
Map Line Item
Use the Map Line Item element for precise mapping of variables. This element maps variables at the level of the main line item and the level of the sub-line items, which are created when multiple transactions occur on the same line item.
Manual Rate Discount
The Manual Rate Discount element calculates the final price of a product after you manually enter the external discounts.
Rate Adjustment Matrix
The Rate Adjustment Matrix element calculates the rate of a usage resource based on the discounts configured for a set of custom conditions.
Assignment
Use the Assignment element to set and change the context tag values of variables.
Formula-Based Rating
The Formula-Based Rating element performs functions and mathematical calculations to generate the rate of a usage resource.
List Group and List Operation
A list group element filters items in a list based on the filter conditions and then performs further operations on the filtered lists. A list operation is always the first step in the list group and defines how items in the list are filtered.
Rounding Values
The Rounding Values element assists in precisely calculating the rate of a usage resource by using rounding rules.
Stop Rating
Use the Stop Rating element to stop the execution of the rating procedure for a particular line item. During simulation, the Waterfall view shows the element that the rating procedure stopped at.
Get Rate Cards
Use the Get Rate Cards element to fetch the rate cards that you need for your rating procedure.

=== ARTICLE: ind.rm_rating_procedures.htm ===
---
article_id: ind.rm_rating_procedures.htm
title: Rating Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_rating_procedures.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management.htm
fetched_at: 2026-09-07
---

# Rating Procedures

Rating procedures are customizable, ordered stacks of rating elements that are used to calculate the final net rate of a usage resource. Each rating element forms a step in a rating procedure. Rating elements call appropriate lookup tables to perform the rating calculations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
Know Your Rating Procedures
Understanding the distinctions between Default Rating Procedure and Negotiable Rating Procedure is key to optimizing your billing processes in Salesforce. Each procedure caters to different scenarios, from straightforward volume-based pricing to complex, usage-driven negotiations.
Prerequisites for Building Rating Procedures
Before you create rating procedures and add elements to them, complete these prerequisites.
Explore Available Rating Elements in Revenue Management
Rating elements are the building blocks of a rating procedure. A new rating procedure is always blank, and each added element forms a step in the rating procedure. Use the available rating elements to form logical steps in the rating procedure.

=== ARTICLE: ind.rm_simulate_activate_rating_procedure.htm ===
---
article_id: ind.rm_simulate_activate_rating_procedure.htm
title: Simulate and Activate Your Rating Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.rm_simulate_activate_rating_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: rating
parent_article: ind.rm_rate_management_setup.htm
fetched_at: 2026-09-07
---

# Simulate and Activate Your Rating Procedure

Before you activate your rating procedure, run simulations to test if the variables that you entered are accurate. If your rating procedure doesn’t work as expected, edit the values that you entered and try again. When you’re satisfied, activate the rating procedure version.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create, update, and delete rating procedures:	Rate Management Design Time User
To use rating procedures:	Rate Management Run Time User
From the App Launcher, find and select Rating Procedures.
To open the rating procedure record, click the procedure name.
To open the rating procedure in the Rating Procedure builder, click the rating procedure version name.
Add your elements, map them to the appropriate tags, choose a rank, enable the option to include in output, and then save your rating procedure.
Click Simulate.
Salesforce shows the Simulation Details with the input mode selected as Simplified by default.
If necessary, change the input mode.
Simplified	To define values for the variables in the fields corresponding to each variable.
Advanced	To define values for the variables in the JSON format. You can modify the values directly or download the JSON input file, modify its values, and paste the file back in the JSON Input box.
Enter values for the input variables.
To locate the value of a variable, go to the related record. For example, to locate a rate card ID, open the rate card record page. The rate card ID appears in the browser’s URL.
In the Input tab, click Simulate.
The Waterfall View shows every step of the rating calculation that determine the resource's final net rate.
When you’re happy with the simulation result, click Activate.

