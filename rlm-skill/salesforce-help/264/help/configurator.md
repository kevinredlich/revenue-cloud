# Salesforce Help 264 — área: configurator (83 artículos)

=== ARTICLE: ind.product_configurator_advanced.htm ===
---
article_id: ind.product_configurator_advanced.htm
title: Rules and Constraints in Configurator With Constraint Rules Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_advanced.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_introduction.htm
fetched_at: 2026-09-04
---

# Rules and Constraints in Configurator With Constraint Rules Engine

To create configuration rules and constraints that can validate large and complex product configurations, use Constraint Rules Engine.

REQUIRED EDITIONS
NOTE Constraint Rules Engine services aren’t available in Government Cloud. For more information, contact your Salesforce account executive.
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Use Constraint Builder With Constraint Rules Engine
Use Constraint Builder to create constraint models that manage complex configuration and validation for your products. Constraint models describe real-world entities and define their relationships with one another. Constraint Builder uses constraints in addition to if-then rules to customize complex products quickly and accurately.
Convert Rules from Business Rules Engine into CML Code
Export rules from Business Rules Engine, then convert them to CML code and import them into Constraint Rules Engine.
Sync Constraint Models with Product Definitions
Sync product definition changes from Product Catalog Management (PCM) to the constraint modeling language (CML) for a constraint model, to make sure that the CML reflects the latest product definition.
Run Rules with the Run Config Rules Action
Use the Run Config Rules invocable action to run Hide/Disable, Message, and Recommend rules.

=== ARTICLE: ind.product_configurator_attribute_display_flow.htm ===
---
article_id: ind.product_configurator_attribute_display_flow.htm
title: Configure Attribute Display on Product Option Cards
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_attribute_display_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_flow.htm
fetched_at: 2026-09-04
---

# Configure Attribute Display on Product Option Cards

Show product attributes on the product option cards, where sales reps can edit them during bundle configurations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create and edit a product configuration flow:	Product Configurator
From Setup, in the Quick Find box, enter Flow, and then select Flows.
Open your product configurator flow.
Edit the screen element and select the Product Configurator Option Groups component.
To show product attributes on the option cards, for the Display Option Card Attributes attribute, select {!$GlobalConstant.True}.
For the Option Card Attributes Limit attribute, specify the number of product attributes that you want to show on the option cards.
You can show up to 5 attributes.
Save your changes and activate the flow.

The attributes that appear on each option card are determined by the sequence you define for the product attributes. Set the sequence by updating the Sequence field in the Attribute Definition Information section when you edit the product attribute or the product classification attribute. For example, if you set the attributes limit to 5, only the product attributes with sequence numbers 1 through 5 appear on the option card.

=== ARTICLE: ind.product_configurator_build_custom_configurator_using_first_party_configurator_api.htm ===
---
article_id: ind.product_configurator_build_custom_configurator_using_first_party_configurator_api.htm
title: Custom Configurator Development with First-Party Configurator APIs
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_build_custom_configurator_using_first_party_configurator_api.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator.htm
fetched_at: 2026-09-04
---

# Custom Configurator Development with First-Party Configurator APIs

As a third-party user, build a custom configurator UI by using the public Configurator APIs. Incorporate the existing first-party configurator UI components for a familiar look and feel, and deliver a personalized experience by using the configurator API functionalities.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

The configurator API includes Revenue Management services such as Context Service, Business Rules Engine, Constraint Rules Engine, and Salesforce Pricing. Third-party users can turn on or turn off the Revenue Management features. The configurator API is available as a Connect API or a wire adapter. For more information on the configurator API, see Product Configurator in the Revenue Management Developer Guide.

Apart from the first-party configurator APIs, third-party users can also build a custom configurator by using the elements of the first-party configurator UI.

=== ARTICLE: ind.product_configurator_bundled_products_instance_quantity.htm ===
---
article_id: ind.product_configurator_bundled_products_instance_quantity.htm
title: Calculate End Quantity and Instance Quantity in Bundled Products
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_bundled_products_instance_quantity.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configure_bundled_products.htm
fetched_at: 2026-09-04
---

# Calculate End Quantity and Instance Quantity in Bundled Products

By default, when you calculate the quantity of a child product in a bundle, the constraint engine returns the end quantity, which is the total quantity of the child product across all parent instances. You can also calculate instance quantity, the quantity of the child product per instance of the parent product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To configure a product:	Product Configurator

When you turn on the Constraint Instance Quantity setting in Revenue Settings, the constraint engine returns the instance quantity of the child product. For example, if a customer orders 3 generator sets and each set requires 2 alternators, the instance quantity is 2, the quantity per bundle. The end quantity of alternators is 6.

From Setup, in the Quick Find box, find and select Revenue Settings.
Turn on Constraint Instance Quantity.

=== ARTICLE: ind.product_configurator_clone_the_default_product_configurator_flow.htm ===
---
article_id: ind.product_configurator_clone_the_default_product_configurator_flow.htm
title: Clone and Customize the Default Product Configurator Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_clone_the_default_product_configurator_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_flow.htm
fetched_at: 2026-09-04
---

# Clone and Customize the Default Product Configurator Flow

Use the Default Product Configurator Flow as a template to design a product configurator flow that determines the layout for presenting customizable product-related information in the user interface.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To clone the default product configurator flow:	Product Configurator
From Setup, in the Quick Find box, enter Flow, and then select Flows.
Click Default Product Configurator Flow.
In the Default Product Configurator Flow Builder, click Save As New Flow.
Enter a label for the flow.
The flow API name automatically populates.
To change the default configurations of the flow, edit the screen element, select the relevant component, and update the necessary attributes.

For example, select the Product Configurator Product Attributes component and update the necessary attributes. You can update the Attribute Categorization, Attribute Display, and Columns Attribute Display Style attributes of the Product Configurator Product Attributes component.

Save your changes, and activate the flow.

After you clone and customize the default configuration of the flow, you can customize the flow further to show context fields and product attributes on product option cards. You can then define the product configuration flows for products and product classifications.

SEE ALSO
Flow Builder Tour

=== ARTICLE: ind.product_configurator_configuration_rule_details.htm ===
---
article_id: ind.product_configurator_configuration_rule_details.htm
title: Configuration Rules in Business Rules Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_configuration_rule_details.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configuration_rules.htm
fetched_at: 2026-09-04
---

# Configuration Rules in Business Rules Engine

Configuration rules streamline the product configuration experience and reduce configuration errors.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Rule Scope

You can apply configuration rules at three levels.

When the rule scope is Product, the rule applies to the attributes of a single product, irrespective of its hierarchy in the quote or order.
When the rule scope is Bundle, the rule applies to all the child products within the root product of a bundle.
When the rule scope is Transaction, the configuration rule applies across all the line items in a transaction, such as a quote or an order.

For example, you create a transaction-level rule stating that the Standard Warranty product can't be included with the Premium Support Package product in the same order or quote. Your quote includes the Server Configuration bundle and the Network Equipment bundle. The Network Equipment bundle contains the Premium Support Package product. So, if a sales rep tries to add the Standard Warranty product to the Server Configuration bundle, a warning appears because the Standard Warranty and Premium Support Package can't be in the same quote.

Actions

Product Configurator supports different actions based on the rule scope of the configuration rule.

ACTION	DESCRIPTION	RULE SCOPE	EXAMPLE
Auto-Add	Automatically add a product to the bundle when the rule runs.	Bundle, Transaction	If a sales rep adds 5 laptops and the customer is a gold status customer, then automatically add a keyboard.
Auto-Remove	Automatically remove a product from the bundle when the rule runs.	Bundle, Transaction	If a sales rep selects a laptop with Refurbished as the type, then automatically remove the 1 Year Warranty product.
Disable Product	Disable the product from the user interface when the rule runs.	Bundle	If a sales rep selects a laptop with Basic as the configuration type, then disable the 1 Year Warranty product.
Disable Attribute Value	Disable one or more attribute values from the user interface when the rule runs.	Product, Bundle	If a sales rep selects a laptop with Basic as the configuration type, then disable the Wireless value for the Mouse attribute.
Exclude	Exclude a product along with its attributes and show a message to the user.	Bundle, Transaction	Sales reps can't select USB-C chargers when they select Micro-USB phones in a bundle.
Hide Product	Hide the product from the user interface when the rule runs.	Bundle	If a sales rep selects a laptop with Basic as the configuration type, then hide the 1-Year Warranty product.
Hide Attribute	Hide the attribute from the user interface when the rule runs.	Product, Bundle	If a sales rep selects a laptop with Basic as the configuration type, then hide the Storage attribute.
Hide Attribute Value	Hide one or more attribute values from the user interface when the rule runs.	Product, Bundle	If a sales rep selects a laptop with Basic as the configuration type, then hide the Wireless value for the Mouse attribute.
Require	Include a product along with its attributes and show a message to the user.	Bundle, Transaction	Sales reps user must select a specific ink cartridge when they select a specific printer as part of the printer bundle.
Set Attribute	Set one or more attributes of a product to the appropriate value.	Product, Bundle	If a sales rep selects a laptop with Advanced as the configuration type, then set the value of the Power Adapter attribute to 96 W.
Set Quantity	Set the quantity of a product to a certain numerical value.	Product, Bundle	If a sales rep selects a limited edition laptop, then automatically set the quantity of the product to 1.
Set Default Attribute	Set a default attribute for a product.	Product	If a sales rep selects a laptop, then select the 15-inch display by default in the display option group. Users can still choose the 13-inch or 17-inch display.
Set Default Attribute Value	Set a default value for a specific attribute of a product.	Bundle	If a sales rep selects a laptop bundle, then automatically set the RAM attribute to a default value of 16GB.
Set Default Product	Set a product within a bundle to be automatically included when the user adds the bundle. This configuration is useful to make sure that a preferred product is selected by default.	Bundle	If a sales rep selects a laptop pro bundle, then automatically include the Premium Support product in the bundle by default.
Validate	Validate whether a product and its attributes are correctly configured and show a message to the user.	Product, Bundle, Transaction	If a sales rep selects a laptop of brand Apex as part of a laptop bundle, then the docking station must be brand Vertex, and the headphones must be brand SoundPro. If the bundled product doesn't meet these criteria, then the user sees a validation error message.

You eliminate fallout due to faulty product configurations when you use the validation, exclusion, and require rules. A perfect product configuration ensures accurate quotes and orders, and a smooth customer experience.

Messages

When you set up configuration rules, you can also define the messages that your sales reps see when the rule runs. Your sales reps can use the messages to rectify product selections and significantly reduce the time to market of the product.

=== ARTICLE: ind.product_configurator_configuration_rules.htm ===
---
article_id: ind.product_configurator_configuration_rules.htm
title: Define Configuration Rules with Business Rules Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_configuration_rules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_introduction.htm
fetched_at: 2026-09-04
---

# Define Configuration Rules with Business Rules Engine

When you configure products for sale, make sure that all your products have valid attributes and are compatible with other products in the offering. With configuration rules, make sure that the product configuration aligns with the business needs and standards and that your sales reps select the right set of products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Configuration Rules in Business Rules Engine
Configuration rules streamline the product configuration experience and reduce configuration errors.
Manage Configuration Rules with Business Rules Engine
Reduce configuration errors, and easily manage product validation and compatibility by using configuration rules.
Validate Configuration Rules in Business Rules Engine
Rules are complex and can become outdated due to catalog changes. To maintain rule integrity, validate a configuration rule and identify the potential errors caused by catalog changes.

=== ARTICLE: ind.product_configurator_configure_bundled_products.htm ===
---
article_id: ind.product_configurator_configure_bundled_products.htm
title: Configure Bundled Products
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_configure_bundled_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configure_products.htm
fetched_at: 2026-09-04
---

# Configure Bundled Products

Configure a bundled product to update the quantity of products, and view the default options within option groups and the default values of attributes. You can select attributes for the parent bundle and child products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To configure a product:	Product Configurator
NOTE When you create a configuration rule on a product bundle to apply on a product, such as adding the product to the bundle, the configuration rule fails if the product has default attribute values that prevent the user from configuring the product.
NOTE If you amend and cancel a child product, the line item quantity doesn’t update.
From the App Launcher, find and select Quotes or Orders.
From the list view, open the record that contains the line item that you want to configure.
If necessary, edit the record to change the transaction type. The selected type determines which rules engine runs product configuration rules. The Transaction Type field is available only if Transaction processing for quotes and orders is turned on.
To view the line item that you want to configure, perform one of these actions based on your selection.
On the quote record details page, go to the Quote Line Items tab.
On the order record details page, go to the Lines tab.
From the quick action menu of the line item that you want to configure, select Configure.

The Product Configurator appears.

To reduce screen clutter and see key information at a glance, turn on Compact Mode.
Configure the product by using one of these methods.
To reuse a saved configuration, click , and then select Load Configuration. From the list of saved configurations, select the configuration that you want to load. See Save and Reuse Configurations.
Specify the configuration manually.
Add products dynamically to the configuration.
From the product component group tab that you want to add products from, click Add <Product Component Group Name>.
Select the products, specify the number of instances you want to add for each product, and then click Add.

You can add the same product multiple times with a unique name attribute identifier.

If you've added a product dynamically and want to create multiple instances with the current configuration, use one of these options.
Click Select <Product Component Group Name>, select the products, specify the number of instances that you want to create for each, and then click Add.
Click Clone on the respective product option card, specify the number of instances you want to create, and then click Clone.

For the Clone option to appear, your Salesforce admin must update the product configuration flow with the Display Clone Option attribute of the Input type on the Product Configurator Option Groups flow component.

On cloning the product, its quantity isn’t cloned.

NOTE Product Configurator doesn't persist state. If you deselect a child product after configuration and then reselect it, the system creates a new quote or order line item with default values. It doesn't restore the previous configuration.
EXAMPLE Configure a Laptop Pro bundle with Laptop as the parent product, and Mouse, Printer Bundle, and Warranty as the child products. Update the quantity of the bundle, and editable attributes of the parent and child products. For Laptop, if the available attribute groups include display, graphics, processor, storage, and memory, choose a display with the perfect size and resolution, pick a processor for your needs, select the graphics card, and find the storage and memory that match your requirements.
Calculate End Quantity and Instance Quantity in Bundled Products
By default, when you calculate the quantity of a child product in a bundle, the constraint engine returns the end quantity, which is the total quantity of the child product across all parent instances. You can also calculate instance quantity, the quantity of the child product per instance of the parent product.

=== ARTICLE: ind.product_configurator_configure_products.htm ===
---
article_id: ind.product_configurator_configure_products.htm
title: Configure Products with Product Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_configure_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_introduction.htm
fetched_at: 2026-09-04
---

# Configure Products with Product Configurator

Create complex product configurations with ease by using Product Configurator. Define attributes, variants, and metadata. Test and verify your product configurations with the built-in run-time experience. Your users can use the Product Configurator to easily configure the product options during the purchase process and view the relevant pricing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Products are all the items and services that you sell to customers. There are two types of products: simple products and bundled products. Simple products don’t have an associated product hierarchy while bundled products generally have one.

Bundled products are a group of products that are sold together as one unit. A bundled product consists of a parent product and child products. The child products are listed as options in the Product Configurator. The product bundle definition determines the option group that is shown during product configuration.

Simple and bundled products are further classified into static or configurable products, depending on whether the products can be configured at run time.

The Type and Configure During Sale fields are available during the creation of product records.

The Product Type field determines whether the product is a simple product or a bundled product.
The Configure During Sale field determines whether the product is static or configurable.
EXAMPLE

Static Simple Product: A 10 GBPS SFP+ transceiver is a single, standalone component with one specification. A customer buys it as-is to plug into a switch.

Simple Configurable Product: A fiber optic patch cable is a single product. However, customers must select a specific length and connector type before adding it to the cart.

Static Product Bundle: A quick-start rack mounting kit is a bundle that always contains the same fixed items: two steel rails, a bag of M6 screws, a cable management arm, and a physical installation guide. There are no choices for the buyer. It’s a pre-packaged set of items sold under one SKU.

Configurable Product Bundle: A next-gen rack server has a chassis comes with a pre-selected motherboard and a base cooling system. Customers must choose the CPU and RAM capacity. They can also add redundant power supplies, an enterprise RAID controller, or an extended 3-year Mission-Critical support tier.

Configure Simple Products
Configure a simple product to update its quantity and default attribute values.
Configure Bundled Products
Configure a bundled product to update the quantity of products, and view the default options within option groups and the default values of attributes. You can select attributes for the parent bundle and child products.
Get the Latest Pricing
Use Instant Pricing to control the pricing calls made for each configuration change. When you change product selections, the prices shown in the summary component change immediately.
Validate Product Configuration
Product validation rules enhance the performance and address potential errors before saving a configuration.
Save and Reuse Configurations
After you configure simple and bundled products, you can save the configurations and reuse them. You can also edit and delete saved configurations.

=== ARTICLE: ind.product_configurator_configure_simple_products.htm ===
---
article_id: ind.product_configurator_configure_simple_products.htm
title: Configure Simple Products
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_configure_simple_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configure_products.htm
fetched_at: 2026-09-04
---

# Configure Simple Products

Configure a simple product to update its quantity and default attribute values.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To configure a product:	Product Configurator
From the App Launcher, find and select Quotes or Orders.
From the list view, open the record that contains the line item that you want to configure.
If necessary, edit the record to change the transaction type. The selected type determines which rules engine runs product configuration rules. The Transaction Type field is available only if Transaction processing for quotes and orders is turned on.
To view the line item that you want to configure, perform one of these actions based on your selection.
On the quote record details page, go to the Quote Line Items tab.
On the order record details page, go to the Lines tab.
From the quick action menu of the line item that you want to configure, select Configure.

The Product Configurator appears.

To reduce screen clutter and see key information at a glance, turn on Compact Mode.
Configure the product by using one of these methods.
To reuse a saved configuration, click , and then select Load Configuration. From the list of saved configurations, select the configuration that you want to load. See Save and Reuse Configurations.
Specify the configuration manually.
Save your changes.
EXAMPLE Configure the Laptop product to mention its display and screen size, and the required quantity of laptops.

=== ARTICLE: ind.product_configurator_considerations_configuring_products_with_ramp_deals.htm ===
---
article_id: ind.product_configurator_considerations_configuring_products_with_ramp_deals.htm
title: Add Products to a Ramp Deal
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_considerations_configuring_products_with_ramp_deals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.qocal_ramp_deals_complex_long_term_multiple_products.htm
fetched_at: 2026-09-04
---

# Add Products to a Ramp Deal

After creating the ramp structure, add products to segments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To manage ramp deals for quote line item groups:	Create on Quotes
To manage ramp deals for order product groups:	Create on Orders
IMPORTANT Before you begin, complete steps 5 to 7 in Prerequisites: Ramp Deals for Groups to select a catalog and then add products from the catalog to their associated record pages.
Click Show more actions on the segment, then click Browse Catalogs.
Select a catalog, and then click Next.
Add products, and then click Next.
Select the group ramp segments to add products to:
Current Segment Only: Adds products as non-ramped lines.
Current and Subsequent Segments: Adds rampable products as ramped lines and other products as non-ramped lines.
NOTE You see the options to select segments only after your admin configures the Discover Products flow.

After adding products, update quantities, discounts, and configurations on each line. Configuration changes propagate to subsequent segments automatically.

=== ARTICLE: ind.product_configurator_considerations_to_save_and_reuse_configurations.htm ===
---
article_id: ind.product_configurator_considerations_to_save_and_reuse_configurations.htm
title: Save and Reuse Configurations
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_considerations_to_save_and_reuse_configurations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configure_products.htm
fetched_at: 2026-09-04
---

# Save and Reuse Configurations

After you configure simple and bundled products, you can save the configurations and reuse them. You can also edit and delete saved configurations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To save and reuse product configurations:	Product Configurator
Save a Configuration

Each user can save up to 80 configurations for each product reference record ID.

Configure a product.
See Configure Simple Products and Configure Bundled Products.
Click , and then select Save as New Configuration.
Enter a name and description for the saved configuration.
Save your changes.
Load a Saved Configuration
Open the Product Configurator.
To use a saved configuration, click , and then select Load Configuration.
Select the saved configuration that you want to use.
Click Load Favorite.
Manage Saved Configurations
Open the Product Configurator.
Update the saved configurations as necessary.
To update a saved configuration, load it, make changes, and click . You can also update the name and description.
To update a saved configuration and save as a new configuration, click , and then select Save as New Configuration.
To update or delete saved configurations, click , and then select Manage Saved Configurations.
Overwrite a Saved Configuration
Open the Product Configurator.
To save the current configuration as an existing saved configuration, click , and then select Overwrite Saved Configuration.
Select the saved configuration that you want to overwrite.
Enter a description.
Click Overwrite.

=== ARTICLE: ind.product_configurator_constraint_builder.htm ===
---
article_id: ind.product_configurator_constraint_builder.htm
title: Use Constraint Builder With Constraint Rules Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_constraint_builder.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_advanced.htm
fetched_at: 2026-09-04
---

# Use Constraint Builder With Constraint Rules Engine

Use Constraint Builder to create constraint models that manage complex configuration and validation for your products. Constraint models describe real-world entities and define their relationships with one another. Constraint Builder uses constraints in addition to if-then rules to customize complex products quickly and accurately.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Constraint Builder Interfaces

To define a constraint model, you add constraints and rules. The Constraint Builder uses Constraint Modeling Language (CML), the domain-specific language of the Constraint Rules Engine, to represent the constraint model. To work in the Constraint Builder, you can choose between two interfaces:

In the Visual Builder, use point-and-click tools to define constraints and rules, without needing to work directly with code.
In the CML Editor, write and edit CML code to define constraints and rules. For more information on CML, see the Constraint Modeling Language (CML) User Guide.

You can work in either of the interfaces. You can also switch between the Visual Builder and the CML Editor as you work. For example, you can define constraints and rules in the Visual Builder, and then view the code in the CML Editor to make additional changes.

Considerations and Limitations

Keep these limitations and considerations in mind when defining constraint models.

The maximum execution time for constraints is 10 seconds.
Constraint models don't support datetime attributes.
Constraint models don't support product variants.
Constraint Builder only supports unicode letters, numeric characters, and underscores. Using other characters can cause errors.
Configurator with Constraint Rules Engine doesn't support decimal quantities. Rules or constraints defined with decimal quantities can't be enforced precisely, and rules that set quantities to decimal values can pass incorrect quantities to downstream processes. For example, rules like "If quantity > 1.5 then..." or "If... then quantity = 1.5" won't be processed accurately.
Create a Constraint Model
To create a constraint model, in the Constraint Models app, name the constraint model and specify a context definition.

=== ARTICLE: ind.product_configurator_constraint_model_variables_relationships_associations.htm ===
---
article_id: ind.product_configurator_constraint_model_variables_relationships_associations.htm
title: Variables, Relationships, and Associations in Constraint Models
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_constraint_model_variables_relationships_associations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_create_a_constraint_model.htm
fetched_at: 2026-09-04
---

# Variables, Relationships, and Associations in Constraint Models

To define how a constraint model configures products, create variables, relationships, and associations for the constraint model.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Constraint models use constraint modeling language (CML) to define variables, relatioships, and associations. For more information on CML, see the Constraint Modeling Language (CML) User Guide.

Variables

Variables are the properties or characteristics that you define within a type. Variables can hold different kinds of data, such as strings, numbers, or lists. You can also calculate variables from other values. A variable can be a product attribute, a sales transaction item such as a product on an order, or a sales transaction such as an order or a cart. You can also create a custom variable.

Create a standalone variable and select a data type and a value type to define the variable. For decimal or double data types, select a scale. You can also apply an automatically generated variable and select a reference library and a product to define the variable.

Relationships

Define a relationship between types to make one type a child of another. The child inherits the constraints and rules that are applied to the parent. For example, to create a type for a laptop bundle that includes a laptop, a mouse, and a keyboard, create relationships to make the laptop, mouse, and keyboard children of the laptop bundle.

In the Import Relationships window, select a reference library and product to see the automatically generated relationships available for the product. To import relationships without the product component group structure from PCM, turn off the Import with Product Component Groups option. Select the product relationships you want to import to make them child types of the selected type.

NOTE You can reference the imported product component groups when you write your constraints. You can also write constraints on items within a product component group so that they apply only at the group level, and not at the bundle level.
Associations

Assocations are required in constraint models. Create an association to connect a type with a product record. Use associations to connect a constraint model to a product, product classification, or product component group in your product catalog. For example, create an association between a type called laptop and the laptop product in your catalog, so that the constraint model in the type applies to the product in the Configurator.

To create a type association, in the Add Type Association window, select the object category (product, product classification, or product component group), and then select the product record that you want to connect to the type. After you create the type association, the type association data table displays the ID for the type and the associated product record.

With relationship associations, you can connect a relationship of the type you’re modifying to a product or product classification within a bundle in the catalog. In the Add Relationship Association window, select the type relationship (one of the types that has a relationship with the type you're modifying). Then, select a product or product classification from the bundle for the type you’re modifying. After you create a relationship association, the relationship association data table displays the ID for the type relationship and the associated product records.

=== ARTICLE: ind.product_configurator_context_fields_flow_setup.htm ===
---
article_id: ind.product_configurator_context_fields_flow_setup.htm
title: Configure Editable Context Fields for Product Option Cards
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_context_fields_flow_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_flow.htm
fetched_at: 2026-09-04
---

# Configure Editable Context Fields for Product Option Cards

Enable sales reps to edit context fields directly from the product option cards during bundle configurations. Context fields are derived from the configured context definition and differ from product attribute fields.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create and edit a product configuration flow:	Product Configurator

Before you select the context fields to be shown on the product option cards, verify that these fields are mapped to an object field and that the object field is editable. Only the context fields that meet this criteria are editable in Product Configurator.

Verify Object Mapping for Editable Context Fields
From Setup, in the Quick Find box, enter Context Service, and then select Context Definitions.
Open the extended SalesTransactionContext context definition that's configured for your default pricing procedure, and go to the Map Data tab.
From the quick action menu of QuoteEntitiesMapping, select Edit SObject Mapping, and then click Map.
Make sure that you are on the Object Mapping tab, and then select the SalesTransactionItem node.
From the list of mapped attributes, search for the attribute that you want to add to the product option cards and check if it’s mapped to an object field.
Go to the object management settings for the mapped field’s object and verify that the field is editable.
To make a context field non-editable on the option card, you can revoke edit access for the mapped field.
NOTE If a context field is mapped to an object field with a different data type, Configurator ignores the data type of the object field that's defined in the Object Manager. Instead, Configurator uses the data type defined for the context field in the context definition.
Select a Context Definition and Add Context Fields
From Setup, in the Quick Find box, enter Flow, and then select Flows.
Open your product configurator flow.
Edit the screen element and select the Product Configurator Option Groups component.
For the Context Definition attribute, select the extended SalesTransactionContext context definition that's configured for your default pricing procedure.
Add the context fields that you want to show on the product option card.
You can add 10 context fields in total.
Select up to 5 context fields from the first Available fields section. These fields appear on the first row of the option card. 
Additionally, you can select 5 more context fields from the second Available fields section. These fields appear on the second row of the product option card.
The Name, Quantity, Product Selling Model, and Price fields have fixed positions and always appear on top of the option card, regardless of the Available fields section from which you add them in the flow setup. Name is a mandatory field and is always displayed.
Save your changes and activate the flow.

=== ARTICLE: ind.product_configurator_convert_bre_rules_to_cml.htm ===
---
article_id: ind.product_configurator_convert_bre_rules_to_cml.htm
title: Convert Rules from Business Rules Engine into CML Code
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_convert_bre_rules_to_cml.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_advanced.htm
fetched_at: 2026-09-04
---

# Convert Rules from Business Rules Engine into CML Code

Export rules from Business Rules Engine, then convert them to CML code and import them into Constraint Rules Engine.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To import rules to Constraint Rules Engine:	Product Configuration Constraints Designer permission set

To migrate rules from Business Rules Engine (BRE) to CML, first add all relevant products with related classes, attributes, product components, product component groups, and bundle definitions to Product Catalog Management (PCM).

Go to https://www.npmjs.com/ and install the plugins @salesforce/plugin-data and @salesforce/plugin-bre-to-cml. For detailed instructions on importing rules to Constraint Rules Engine, see information in plugin-bre-to-cml.
To export rules from Business Rules Engine and save as a JSON file, in plugin-data, use the sf data export bulk command in the source org, as in this example. The ConfigurationRuleDefinition field contains the JSON representation of the BRE rule. To confirm that a rule exports successfully, in the WHERE clause add a search on Name = "myBreRuleToTest".
sf sf data export bulk -o srcOrg --query "SELECT ApiName, ConfigurationRuleDefinition,Description, EffectiveFromDate, EffectiveToDate, Id, IsDeleted, Name, ProcessScope, RuleSubType, RuleType, Sequence, Status FROM ProductConfigurationRule WHERE RuleType = 'Configurator' AND Status = 'Active'" --output-file ./data/ProductConfigurationRules_Active.json --result-format json --wait 10 --all-rows
To convert the rules from the JSON file to CML code and save the code as a pair of CML and association files, in plugin-bre-to-cml, run the sf cml convert prod-cfg-rules command in the source org, as in this example. The value you pass as —cml-api is the API name for each generated CML constraint model. A 0-based index appends to that value with "_" as a separator. To make sure that the rules convert successfully, inspect the CML rules before you import them to the target org.
sf cml convert prod-cfg-rules --pcr-file data/ProductConfigurationRules_Active.json --cml-api CML_API --workspace-dir data --target-org srcOrg
To import the CML into the target org, run the import command for each CML rule that was generated during conversion. All classes, attributes, product components, product component groups, and bundle definitions must be present in the target org. You can select which CML rules to import, and import them in any order. If the conversion generates only one CML rule, import the rule for CML_API_0. See these examples.
sf cml import as-expression-set --cml-api CML_API_0 --context-definition PricingTransactionCD2 --workspace-dir data --target-org tgtOrg   sf cml import as-expression-set --cml-api CML_API_N --context-definition PricingTransactionCD2 --workspace-dir data --target-org tgtOrg
Activate and test each imported CML rule.

The CML code for the imported rules uses a similar structure as that used to import bundle products from PCM into CML Editor. For detailed instructions on importing rules to Constraint Rules Engine, see information in plugin-bre-to-cml.

To edit the imported CML rules, such as creating new types or adding annotations, use the CML Editor in Product Configurator. To avoid unexpected outcomes, don’t make changes directly in the CML code. If you edit the CML rules in the target org and import the rules again, the later import overwrites the earlier import.

These behaviors are different in CML than in Business Rules Engine:

In CML, conditional defaults for Set Default Attribute Value and Set Default Product aren’t supported.

In CML, auto-adding multiple instances of a product isn’t supported. For example, consider this rule: if product == A and quantity > 5, auto-add B. In the Business Rules Engine, if there are 2 line items of product A with quantity greater than 5, two instances of product B are added. In CML, only 1 instance of product B is added.

In CML, a message persists as long as a condition is true.

=== ARTICLE: ind.product_configurator_create_a_configuration_rule.htm ===
---
article_id: ind.product_configurator_create_a_configuration_rule.htm
title: Manage Configuration Rules with Business Rules Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_create_a_configuration_rule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configuration_rules.htm
fetched_at: 2026-09-04
---

# Manage Configuration Rules with Business Rules Engine

Reduce configuration errors, and easily manage product validation and compatibility by using configuration rules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To manage configuration rules:	Manage Configurator with Business Rules Engine

Before you create configuration rules, make sure that your Salesforce admin has set up Business Rules Engine for Product Configurator.

Keep these considerations in mind when defining configuration rules.

If you deactivate a child product, remove all the references to the product in configuration rules to prevent errors.
If you have an active rule on a product attribute or product bundle, and modify the attribute or bundle in the product catalog, the Product Configurator fails if the rule and the catalog are out of sync. To correct this error, deactivate the rule, update it to be consistent with product catalog data, and then activate the rule.
If you create a configuration rule on a product bundle to run on a product, such as adding the product to the bundle, the configuration rule fails if the product has default attribute values that prevent the user from configuring the product.
For configuration rules created before Summer '25 and containing a condition with the NetUnitPrice sub-condition, the name of the NetUnitPrice sub-condition appears as ItemDetailNetUnitPrice from Summer '25.
Create a Rule

Create rules to validate configurations of products, product bundles, or transactions.

From the home page of the Product Catalog Management app, click Product Configuration Rules.
Click New.
In the Rules Details page, specify these details:
Enter a name for the configuration rule.
The API name automatically populates.
Enter a description for the configuration rule.
Enter the rule duration.
Select the rule status.
To determine when this rule runs, enter the rule sequence.
When multiple rules trigger together, rules with lower numbers run first.
Click Next.
In the Rule Criteria page, specify these details:
Select the rule scope. See Rule Scope.
Specify the conditions to run the rule.
The resource for each condition is either a product or product classification. Each rule supports up to three conditions and eight sub-conditions. Currently, the system supports only the AND logical operand between conditions. So, the rule runs only when all the conditions are met.
Specify the action to take when the conditions are met. See Actions.
Each rule supports up to three actions. You can add a message for each action. The type of message depends on the type of action.
Save your changes.
Edit a Rule

To add, update, or delete rule conditions and actions, modify the rule details or the rule criteria.

From the home page of the Product Catalog Management app, click Product Configuration Rules.
From the quick action menu next to the configuration rule that you want to edit, select Edit Rule.
On the Rule Details page, update the necessary details.
Click Next.
On the Rule Criteria page, update the necessary details.
Save your changes.
Delete a Rule

Delete a configuration rule when you no longer need it.

From the home page of the Product Catalog Management app, click Product Configuration Rules.
From the quick action menu next to the configuration rule that you want to delete, select Delete, and confirm your action.

After you create configuration rules, make sure that you validate them to maintain rule integrity.

=== ARTICLE: ind.product_configurator_create_a_constraint_model.htm ===
---
article_id: ind.product_configurator_create_a_constraint_model.htm
title: Create a Constraint Model
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_create_a_constraint_model.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_constraint_builder.htm
fetched_at: 2026-09-04
---

# Create a Constraint Model

To create a constraint model, in the Constraint Models app, name the constraint model and specify a context definition.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create a constraint model:	Product Configuration Constraints Designer permission set

Complete the steps for Constraint Rules Engine setup before you create a constraint model. See Set Up Configurator With Constraint Rules Engine.

From the App Launcher, find and select Constraint Models.
Click New Constraint Model.
Enter a name and API name for the constraint model.
Select the active sales transaction context definition that the cfgStatus node is mapped to.
Save the constraint model.
NOTE Deleting or restoring constraint models isn't currently supported.
Define Constraints and Rules with the Visual Builder
In the Constraint Builder, use point-and-click tools in the Visual Builder to define the constraints and rules for a constraint model. Add constraints and rules to easily configure products or product bundles.
Constraint and Rule Types in the Visual Builder
The Visual Builder provides point-and-click tools for you to easily define constraints and rules for a constraint model. Use the basic logic constraint, the conditional logic constraint, the message rule, the require rule, the exclude rule, the hide/disable rule, and the preference rule to author complex configurations for products and product bundles in your catalog.
Use Code to Define Constraints and Rules in the CML Editor
In the Constraint Builder, use Constraint Modeling Language (CML) code to define constraints and rules for a constraint model.
Variables, Relationships, and Associations in Constraint Models
To define how a constraint model configures products, create variables, relationships, and associations for the constraint model.
Set Up Custom Labels for Run-Time Message Translation
Enable translations for run-time messages defined in your constraint model by creating unique, translatable custom labels for the messages. The labels you set up replace the original static message text in the CML to facilitate translation. During run time, the messages appear in different languages, based on the sales reps’ locale and the translation settings of their Salesforce org. With this support, sales reps can see important configuration information in their local languages, which accelerates troubleshooting and improves usability.
Import Data from Salesforce Objects to Use in Constraint Models
Import data from a standard or custom Salesforce object to use in a table constraint in a constraint model. The imported data populates the columns and rows in the table constraint in CML, and saves you the step of manually entering the data.
Load Product Defaults from PCM to a Constraint Model
Include product defaults defined in Product Catalog Management (PCM), such as attributes, attribute values, and custom and standard fields, when you import products to a Constraint Modeling Language (CML) constraint model.

=== ARTICLE: ind.product_configurator_create_a_product_configuration_flow.htm ===
---
article_id: ind.product_configurator_create_a_product_configuration_flow.htm
title: Define Product Configuration Flows
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_create_a_product_configuration_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_explore_the_product_configurator_flow.htm
fetched_at: 2026-09-04
---

# Define Product Configuration Flows

The product configuration flow provides a layout for configuring the products and previewing the user experience in real time. The flow provides a simple layout for defining attribute details, ensuring a smooth buying experience for your customers.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To create a product configuration flow, and assign products and product classifications to the flow:	Product Configurator
Create a Product Configuration Flow

Define the flow that's used for configuring products or product classifications.

From the App Launcher, find and select Product Configuration Flows.
Click New.
For Flow Identifier, enter the API name of the flow that you want to use as the product configuration flow.
Select a status.
You can assign only active product configuration flows to products and product classifications.
To set this flow as the default product configuration flow for your org, select Default.
Products and product classifications without an assigned product configuration flow use the default product configuration flow.
Save your changes.
Assign Products to a Product Configuration Flow

Configure the product configuration flow for products. You can assign only one product configuration flow to a product.

From the App Launcher, find and select Product Configuration Flows.
Open the product configuration flow that you want to assign products to.
On the Related tab, in the Product Configuration Flow Assignment related list, click New.
Find and select the product that you want to assign to the product configuration flow.
Save your changes.

Similarly, assign other products to the product configuration flow. To unassign a product from the product configuration flow, delete the corresponding Product Configuration Flow Assignment record.

For products assigned to a flow, verify the product configuration experience seen during run time.

Assign Product Classifications to a Product Configuration Flow

Configure the product configuration flow for product classifications. You can assign only one product configuration flow to a product classification.

From the App Launcher, find and select Product Configuration Flows.
Open the product configuration flow that you want to assign product classifications to.
On the Related tab, in the Product Configuration Flow Assignment related list, click New.
Find and select the product classification that you want to assign to the product configuration flow.
Select the assignment type.
To use the selected product configuration flow as the flow for the primary product or classification, select Primary Configurator Flow. For a multilevel product bundle, the product configuration flow assigned to the bundle root product is used at all levels, even if a child product in the bundle has a different Primary Configurator Flow assigned.
To use the selected product configuration flow as the flow for only the dynamic components within a product bundle, select Dynamic Addition Flow.
Save your changes.

Similarly, assign other product classifications to the product configuration flow. To unassign a product from the product configuration flow, delete the corresponding Product Configuration Flow Assignment record.

For product classifications assigned to a flow, verify the product configuration experience seen during run time.

=== ARTICLE: ind.product_configurator_data_types_for_configurator_user_interface.htm ===
---
article_id: ind.product_configurator_data_types_for_configurator_user_interface.htm
title: Data Types for Configurator User Interface
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_data_types_for_configurator_user_interface.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator.htm
fetched_at: 2026-09-04
---

# Data Types for Configurator User Interface

The Apex classes contain data accessible through the user interface. The Configurator’s Data Manager acts as the primary user interface component that exports data to other components. As a third-party user you can pass the data into your own user interface component without the need for separate queries to fetch data.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

The effective method to interact with the user interface is to import data through the Flow user interface properties that the Data Manager exports.

The effective way to modify quantities, attribute values, product options, and other state changes is to trigger LMS events for any updates your user interface component makes.

The Data Manager simplifies data management in your user interface component. It constantly updates and sends the latest information whenever changes occur. This creates a seamless flow where you don't need to actively listen for updates. Instead, you can simply import or watch the data directly from the flow properties.

The Configurator User Interface Data Manager exports the following Apex data types. This data is readily available for use by third-party configurators in the user interface, eliminating the need for them to query the data separately.

Apex Data Type: ProductConfig__Product
ProductConfig__Product
FIELD NAME	TYPE
id	String
quantity	Double
isConfigurable	Boolean
isActive	Boolean
quantityReadOnly	Boolean
isAssetizable	Boolean
isQuantityEditable	Boolean
isSelected	Boolean
isPersisted	Boolean
isHidden	Boolean
disabled	Boolean
isSoldOnlyWithOtherProds	Boolean
name	String
nodeType	String
productCode	String
productType	String
productComponentGroups	List<OptionGroup>
attributeCategories	List<AttributeCategory>
productKey	List<String>
additionalFields	Map<String, Object>
prices	List<Price>
productClassification	ProductClassification
productSellingModelOptions	List<ProductSellingModelOption>
qualificationContext	QualificationContext
minOptions	Integer
maxOptions	Integer
sequence	Integer
Apex Data Type: ProductConfig__Attribute
ProductConfig__Attribute
FIELD NAME	TYPE
id	String
name	String
label	String
attributeCategoryId	String
attributeNameOverride	String
code	String
dataType	String
defaultValue	String
description	String
productKey	List<String>
isCloneable	Boolean
isConfigurable	Boolean
isHidden	Boolean
isPriceImpacting	Boolean
isReadOnly	Boolean
isRequired	Boolean
assetAttributeValue	String
attributeValue	String
attributeKey	String
attributePicklistValue	String
businessObjectType	String
Apex Data Type: ProductConfig__AttributeCategory
ProductConfig__AttributeCategory
FIELD NAME	TYPE
code	String
id	String
name	String
attributes	List<Attribute>
Apex Data Type: ProductConfig__ConfiguratorContext
ProductConfig__ConfiguratorContext
FIELD NAME	TYPE
transactionLineId	String
parentName	String
origin	String
transactionId	String
addedNodes	List<SalesTransactionItem>
Apex Data Type: ProductConfig__Message
ProductConfig__Message
FIELD NAME	TYPE
text	String
type	String
Apex Data Type: ProductConfig__NavigationInfo
ProductConfig__NavigationInfo
FIELD NAME	TYPE
index	Integer
name	String
productKey	List<String>
Apex Data Type: ProductConfig__OptionGroup
ProductConfig__OptionGroup
FIELD NAME	TYPE
id	String
name	String
minOptions	Integer
maxOptions	Integer
sequence	Integer
components	List<Product>
productKey	List<String>
classifications	List<ProductClassification>
parentProductId	String
pricebookId	String
parentProductName	String
Apex Data Type: ProductConfig__Price
ProductConfig__Price
FIELD NAME	TYPE
pricebookEntryId	String
pricebookId	String
unitPrice	Double
pricingModel	PricingModel
Apex Data Type: ProductConfig__PricingModel
ProductConfig__PricingModel
FIELD NAME	TYPE
id	String
name	String
pricingModelType	String
Apex Data Type: ProductConfig__PricingSummary
ProductConfig__PricingSummary
FIELD NAME	TYPE
id	String
name	String
sequence	Integer
quantity	Double
hasErrors	Boolean
productRelatedComponentId	String
productKey	List<String>
prices	List<SummaryPrice>
transactionLineAttributes	List<Attribute>
transactionLineGroups	List<OptionGroup>
Apex Data Type: ProductConfig__ProductClassification
ProductConfig__ProductClassification
FIELD NAME	TYPE
id	String
Apex Data Type: ProductConfig__ProductSellingModel
ProductConfig__ProductSellingModel
FIELD NAME	TYPE
id	String
name	String
sellingModelType	String
status	String
Apex Data Type: ProductConfig__ProductSellingModelOption
ProductConfig__ProductSellingModelOption
FIELD NAME	TYPE
id	String
productId	String
productSellingModelId	String
productSellingModel	ProductSellingModel
Apex Data Type: ProductConfig__QualificationContext
ProductConfig__QualificationContext
FIELD NAME	TYPE
reason	String
isQualified	Boolean
Apex Data Type: ProductConfig__SalesTransactionItem
ProductConfig__SalesTransactionItem
FIELD NAME	TYPE
id	String
salesTransactionItemSource	String
pricebookEntry	String
productSellingModel	String
sellingModelType	String
subscriptionTerm	Integer
pricingTermUnit	String
unitPrice	Double
quantity	Double
product	String
productCode	String
productName	String
productBasedOn	String
businessObjectType	String
Apex Data Type: ProductConfig__SummaryPrice
ProductConfig__SummaryPrice
FIELD NAME	TYPE
netAmount	Double
netUnitPrice	Double
isInclusive	Boolean
pricingTermUnit	String
Apex Data Type: ProductConfig__TransactionRecord
ProductConfig__TransactionRecord
FIELD NAME	TYPE
parentId	String
parentName	String
origin	String
pricingTermUnit	String

=== ARTICLE: ind.product_configurator_enable_product_configurator.htm ===
---
article_id: ind.product_configurator_enable_product_configurator.htm
title: Enable Product Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_enable_product_configurator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_get_started.htm
fetched_at: 2026-09-04
---

# Enable Product Configurator

Give users the ability to configure products at run time and access all Product Configurator features.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To enable Product Configurator:	Product Configurator
From Setup, in the Quick Find box, enter Revenue Settings, and then select Revenue Settings.
Turn on Configure Products at Runtime.

After you turn on Configure Products at Runtime, assign the required permission sets to users.

=== ARTICLE: ind.product_configurator_essentials.htm ===
---
article_id: ind.product_configurator_essentials.htm
title: Product Configurator Essentials
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_essentials.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.revenue_impl_glossary.htm
fetched_at: 2026-09-04
---

# Product Configurator Essentials

Browse through this collection of terms, key objects, and key concepts. This collection is designed to give Salesforce admins, sales reps, and developers a clear and consistent understanding of product configurator concepts and helps them navigate the Product Configuration landscape.

Action Rule
Use the rule to define simple conditions and action rules. When the conditions are met, the constraint solver engine raises the action with parameters, and the caller executes the action with those parameters. The action can be anything that the caller defines.
Actionable Rules
Rule outcomes that take programmatic action at the time of execution, such as auto-add and auto-remove.
Configuration Rule
A rule that includes a condition and an action block, where conditions are based on a product or a product class, and various actions are taken on one or more products and their attributes.
Configuration Logs
Diagnostic records that capture configuration behavior. Review these logs to validate CML code, analyze configuration clarity and accuracy, and troubleshoot constraints to make sure your constraint models perform as expected. The Product Configuration Constraints Designer permission set is required to enable configuration logs.
Constraint Engine
The engine that compiles Constraint Model Language (CML) code into a constraint model and uses the model to construct a product configuration that complies with the specified constraints.
Constraint Model
For product configuration, constraint models describe real-world entities and their relationships to each other. They enforce business logic without needing extensive coding, by using a special language designed for this purpose, Constraint Modeling Language.
Constraint Model Language (CML)
A domain-specific language that defines models for complex systems.
Constraint Type
In CML, you define types to represent the entities or objects in the model. Types are the foundational building blocks of CML. It consists of the property, relationships, constraints and rules for the entities. They’re similar to the classes in object-oriented programming.
Conditional Operator
Specifies the conditions that determine a result.
Constraint Relationship
Defines how different types are associated with one another.
Constraint Variable
Variables are the properties or characteristics defined within a type. Variables can hold different kinds of data, such as strings, numbers, and lists, and can be calculated from other values.
Default Product Configurator Flow
A predefined flow that's used as a template to create a customized product configuration flow based on business requirements.
Distinct Constraint
The constraint enforces unique values for a set of variables.
Equal Constraint
The constraint enforces equal values for all variables referred inside the constraint.
Error Component
The component serves as a central location for all errors, warnings, and informational messages related to the product that you’re configuring.
Exclude Rule
The rule is used to automatically remove a specific type in a relationship if a certain condition is met.
Exclusion Constraint
The constraint excludes certain values from a relationship variable. A relationship variable is a set of variables that define how different types, such as products and attributes, are connected or interact with each other within a relationship.
Flow Components
The predefined Configuration Flow Template is a collection of composable components, such as options, prices, quantities, and summaries. These components are extensible.
Flow Template Association
Associating the flow template to products or product classes for rendering during run time.
Implication Operator (→)
Enforces that if a precondition is true, the postcondition must also be true. If the precondition is false, the postcondition isn’t required.
In Set Operator
The operator enforces a constraint in which a variable value must be one of the defined values in the given domain.
Inclusion Constraint
The constraint enforces a relationship variable to include certain values. A relationship variable is a set of variables that define how different types (such as products and attributes) are connected or interact with each other within a relationship.
Indistinct Constraint
The constraint enforces non-uniqueness for variable values.
Instant Pricing
Toggle in the run-time sales rep experience to control the pricing calls made for each configuration change. Turning on Instant Pricing results in an instant change of prices shown in the summary component when any changes are made to product selections.
Logical Constraint
Defines a statement that must hold true logically. The constraint can be any logical expression that uses one of these logical operators: AND (&&), Conditional (?), Implication (→), Logical equivalent (<->), OR (||), XOR (^).
Logical Equivalence Operator (↔)
The conditional operator that specifies that two statements are logically equivalent, that is, they have the same truth value under all possible conditions. This operator is equivalent to the statement. If one statement is true, then the other must be true, and vice versa.
Message Component
The UI component that shows messages for warnings and errors that occur during configuration. The messages convey information, an error, an alert, or a warning.
Message Rule
The rule shows messages to users based on specified conditions.
Named Constraint
You can name a constraint, similar to naming a variable, and reference it later in the model.
Null Constraint
The constraint determines whether a variable is bound to a value (true) or not (false). The configurable annotation for the variable must be set to false, or the engine assigns a value to the variable, and the null constraint is false.
Option Cards
Individual product details are presented to the sales rep as part of a card that you can further expand for focused product configuration in the Configurator.
Option Group
A collection of products and components that are logically grouped together.
Preference Rule
The rule encourages the constraint solver to satisfy the condition, but doesn’t enforce it if the condition can’t be met.
Product Validation
Toggle in the runtime sales rep experience to validate that the current product configuration is accurate. Turning on Product Validation triggers qualification, Product Catalog Management validation, and configuration rules. Validating the configuration against product definitions and rule governance on-demand, rather than automatically with every selection, optimizes performance and enables users to resolve errors before saving.
Regular Expression Constraint
Use the constraint to determine if a string matches a regular expression.
Relationships
Create relationships to define how different types are connected to each other. For example, a relationship can specify a range for a type (in a constraint model for a house design, use a relationship to specify that the house must have between one and five rooms) or cardinality (the house must have exactly one bathroom) or order (the first room in the house design must be a living room, followed by one or more bedrooms). Relationships can have default quantities and variables.
Require Rule
The rule requires certain components in a relationship when specified conditions are met. Required components can have attributes and quantity specified. The Require rule can include an optional explanation message for failure explanation.
Rule Scope
The radius within which the rule condition is applied can be a product, bundle, or transaction.
Rule Sequence
A numerical sequence of rules that determines how they're executed at run time, also known as rule rank or rule priority.
Selected or Unselected Constraint
Use the constraint to determine if given values are selected or unselected for multiple selection variables.
Sequential Rule
This rule increments a relationship variable by an integer value, X, which is another variable of the same type. It's like a simplified loop. Use it to solve slotting issues, which involve arranging components efficiently in server setups.
Summary Component
The UI component that provides a comprehensive, real-time summary of the configured product bundle, reflecting updates instantly as selections are made. Sales reps get a focused view of the overall bundle structure, where selections are categorized by product to illustrate the hierarchy clearly. Beyond attributes, the component also shows a detailed pricing breakdown, including quantities and a full price waterfall for the specific configuration.
Table Constraint
 The constraints enforce value combinations for variables. The table constraint defines valid combinations of values, specified in rows.
Unequal Constraint
The constraint enforces unequal values for the given variables.
Untable Constraint
 The constraints enforce value combinations for variables. The untable constraint is the negation of the table constraint. It specifies that the variable values from different rows aren't valid in combination with each other.
Variables
The properties or characteristics that you define within a type. Variables can hold different kinds of data, such as strings, numbers, and lists.
Visibility Rules
Rule outcomes make visual updates to the configured product, for example, hide, disable, or exclude.

=== ARTICLE: ind.product_configurator_explore_the_product_configurator_flow.htm ===
---
article_id: ind.product_configurator_explore_the_product_configurator_flow.htm
title: Explore the Product Configurator Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_explore_the_product_configurator_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_introduction.htm
fetched_at: 2026-09-04
---

# Explore the Product Configurator Flow

The product configurator flow outlines the layout for presenting customizable product information in the user interface.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Product Configurator Flow Screen Components
Product Configurator provides a sample flow, Default Product Configurator Flow. The default flow contains a screen element with components that collect and display information in Product Configurator. For information on each screen component, including its responsibilities and properties, see the topics linked here.
Set Up Your Product Configuration Flow
Clone the Default Product Configurator Flow and customize it according to your business needs to manage the Product Configurator interface layout and the product information shown on it. Maintain your customized configuration flows and update them with the latest attributes to make sure new features work as expected, and you retain a smooth configuration experience.
Define Product Configuration Flows
The product configuration flow provides a layout for configuring the products and previewing the user experience in real time. The flow provides a simple layout for defining attribute details, ensuring a smooth buying experience for your customers.
Preview the Product Configurator
See how the product configurator looks and functions for your users.
Set Up a Custom Dynamic Addition Screen Flow
Build a screen flow that replaces the default add-products experience for a product classification during bundle configurations. When a product classification uses a Dynamic Addition Flow, Product Configurator can open your own flow with a custom interface and logic. Publish the product selections back to the Configurator as an addedNodes payload with Lightning Message Service (LMS) so that your quote or order lines stay in sync.

=== ARTICLE: ind.product_configurator_flow_breadcrumbs.htm ===
---
article_id: ind.product_configurator_flow_breadcrumbs.htm
title: Breadcrumbs
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_breadcrumbs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Breadcrumbs

Breadcrumbs shows the navigation path through the product bundle hierarchy in Product Configurator. The component displays clickable breadcrumb links so users can move between levels, such as root product → option group → option. Breadcrumbs has no output properties and doesn’t listen to any events.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Breadcrumbs Responsibilities
Show breadcrumbs of the current path through the bundle hierarchy
Provide clickable breadcrumbs for users to go to a specific level
Use an overflow menu when a bundle hierarchy has four or more breadcrumb levels
Show the search bar when multiple searchable products exist
Publish Lightning Message Service (LMS) navigation events to Data Manager when a breadcrumb is clicked
Breadcrumbs API Name

S01_BreadCrumbs

Input Properties

Breadcrumbs accepts data from parent or flow component properties, set by users.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
navigationRoute	Array	No	Current navigation path
searchInfo	Array	No	Searchable products for the catalog. Shows the search bar when more than one product is available.
isApiInProgress	Boolean	No	Whether an API call is in progress. Locks the component while the call runs.
isNonBlockingEnabled	Boolean	No	Whether non-blocking mode is turned on.
Types of Events Breadcrumbs Fires

Breadcrumbs fires the LMS event shown in this table.

EVENT ACTION	WHEN IS IT FIRED	PURPOSE
navigate	User clicks a breadcrumb link	Go to selected root product

=== ARTICLE: ind.product_configurator_flow_data_manager.htm ===
---
article_id: ind.product_configurator_flow_data_manager.htm
title: Data Manager
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_data_manager.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Data Manager

Data Manager is the state management and orchestration component for Product Configurator. This component stores product data and uses flow events to propagate the data to other components on the flow screen.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Data Manager Responsibilities
Maintain the transaction context and configuration state
Invoke the Configurator API and process responses
Process Lightning Message Service (LMS) events from UI components
Provide data to UI and expose reactive properties to child components
Support saving and loading favorite configurations
Data Manager API Name

S01_DataManager

Data Manager Input Properties

Data Manager accepts data from parent or flow component properties set by users.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
transactionLineId	String	Yes	Root product or transaction line ID
currentTransactionLineId	String	Yes	Current line being viewed
transactionId	String	Yes	Sales Transaction ID (Quote, Order, and so on)
parentName	String	Yes	Name or title of the parent transaction that the configuration pertains to.
origin	String	Yes	Name of the transaction record's parent object. Example: 'Opportunity', 'Quote', 'Order', 'Asset', and so on. This identifies which Salesforce object type launches the configuration. Used for navigation, UI label and so on.
addedNodes	Array	No	Flow resource that contains a collection of Apex ProductConfig__SalesTransactionItem records associated with the parent record transaction.
isNonBlockingEnabled	Boolean	No	Turn on non-blocking mode. When turned on, this allows users to continue interacting with the UI while API calls are processing in the background. Changes are queued and processed asynchronously without blocking the UI. When turned off, the UI is locked during API calls.
areMessagesFixed	Boolean	No	Whether messages component has a fixed position. When true, the messages component stays fixed at the top of the screen and remains visible while scrolling (sticky positioning). When false, the messages component scrolls with the page content (relative positioning). Useful for keeping validation errors/warnings always visible during configuration
contextId	String	No	ID of the transaction context specified for Product Configurator
enableARCValidation	Boolean	No	Indicates whether ARC (Asset Renewal Configuration) validation runs during product configuration
transactionLineGroupId	String	No	ID of the group that contains the current transaction line being configured. For Quotes, this is the Quote Line Group ID. For Orders, this is the Order Item Group ID.
explainabilityEnabled	Boolean	No	When Explainability is enabled, Product Configurator provides detailed explanations for why products are hidden, disabled, or recommended. Shows rule execution details and business logic reasoning to help users understand configuration constraints.
userContext	Object	No	

API name of a flow variable that contains user qualification data. This variable is of type ProductConfig__UserContext and determines product eligibility based on user-specific attributes.

1. In Flow Builder, create a variable API name, for example, userContextData.

2. Use an Assignment or Get Records element to populate the variable, and set fields such as role, region, accountType, and so on. For example, {!userContextData.role} = {!$User.UserRole.Name}

3. In Data Manager, for User Context, select {!userContextData}. The Configurator API uses this data to evaluate qualification rules and filter which products are available. For example, if you have rules like "Show Enterprise Products only to Enterprise Sales reps", the API checks the user's role from this context.

Select a user context only if you have product qualification rules that depend on user-specific attributes like role, territory, and so on. If all products are available to all users, leave this field empty.

Data Manager Output Properties

Data Manager writes output properties that customers can read. An internal method generates data, and the FlowAttributeChangeEvent dispatches the data to the relevant property, as shown in this example.

this.dispatchEvent(
   new FlowAttributeChangeEvent(FLOW_REACTIVITY_MESSAGES, messages)
);


This table shows what data Data Manager provides to other components. The Data Source column identifies the internal process that generates the data.

PROPERTY	DATA TYPE	DESCRIPTION	DATA SOURCE
header	Object	Current product header information	mergeContexts()
messages	Array	Validation/error messages	API response + rules
optionGroups	Array	Product component groups (options)	mergeContexts()
attributeCategories	Array	Product attribute categories	mergeContexts()
summary	Object	Configuration summary (merged transaction tree)	mergeContexts()
navigationRoute	Array	Current navigation path, or breadcrumbs	buildNavigationInfo()
searchInfo	Array	Search data for product catalog	buildSearchInfo()
tabs	Array	Available tabs for multi-root bundles	buildTabs()
currencyCode	String	Currency code for pricing	API response
transactionRecord	Object	Transaction record details	populateTransactionRecord()
headerTitle	String	Header title text	generateHeaderTitle()
isInstantPricingToggleEnabled	Boolean	Whether instant pricing toggle is shown	setToggleStates()
isInstantPricingEnabled	Boolean	Current instant pricing state	Toggle/API
isProductValidationEnabled	Boolean	Current validation state	Toggle/API
showPrices	Boolean	Whether to show prices	State logic
showSummaryTotalSection	Boolean	Whether to show summary total section	Insurance override
favoriteData	

String (JSON)

	Configuration data for favorites	getFavoriteData()
isConfiguratorDisabled	Boolean	Whether configurator is disabled	UI state
isApiInProgress	Boolean	Whether API call is in progress	API lifecycle
isPriceRampEnabled	Boolean	Whether price ramps are enabled	Context check
isGroupRampEnabled	Boolean	Whether group ramps are enabled	Group calculation
salesTransactionItems	Array	All transaction items	API response
layoutMode	String	Layout mode (standard or compact)	Toggle
searchResultOptionId	String	Selected search result option ID	Search navigation
rootProductId	String	Root product ID	Catalog data
currentGroupName	String	Current group name	getCurrentGroupName()
contextMetadata	Object	Context metadata for customizable Sales Transaction Item attributes. Contains field definitions (labels, data types, picklist values) for custom attributes that can be displayed in the UI.	Context parsing
eligiblePromotions	Array	Eligible promotions list	Promotion API
Events Data Manager Listens To

Data Manager listens to Lightning Message Service (LMS) events and wire adapters.

To listen to LMS events, Data Manager subscribes to the message channel and receives LMS events that other components published there. This table shows LMS event actions, their handler methods, and what the actions do.

EVENT ACTION	HANDLER METHOD	WHAT IT DOES
valueChange	setState()	Updates configuration state (selections, quantities, attributes)
navigate	navigate()	Navigates through bundle hierarchy
closePreview	closePreview()	Closes preview window
toggleInstantPricing	setInstantPricing()	Toggles instant pricing on/off
toggleExplainability	setExplainability()	Toggles explainability on/off
toggleRulesValidation	setProductValidation()	Toggles validation on/off
updatePrices	updatePrices()	Manually triggers pricing
validateProduct	validateProduct()	Manually triggers validation
cloneItems	cloneItems()	Clones transaction items
toggleCompactLayout	setLayoutModeOnToggle()	Toggles layout mode
contextDefinitionChanged	setContextDefinition()	Updates context definition
saveFavConfiguration	handleSaveConfiguration()	Saves configuration as favorite
loadFavorite	handleLoadFavorite()	Loads favorite configuration

Wire adapters automatically listen for data changes from Salesforce's platform, and pass the data changes to Data Manager. This table shows the wire adapter events Data Manager listens to.

WIRE ADAPTER	SOURCE	WHAT IT LISTENS FOR	HANDLER METHOD	PURPOSE
MessageContext	lightning/messageService	Message context for LMS	

Not applicable (provides context)

	Enables LMS communication
getContextServiceDefinition	lightning/industriesContextApi	Context definition changes	

gotContextDefinition()

	Listens for context definition data
getObjectInfos (2nd)	lightning/uiObjectInfoApi	Transaction item object info	getObjectInfos()	Listens for transaction item metadata
Events Data Manager Fires

Data Manager fires custom events, toast events, and flow attribute change events.

This table shows custom events Data Manager fires, including bubbling and composed events.

EVENT NAME	BUBBLES	COMPOSED	WHEN IT FIRES	PURPOSE
loading	Yes	Yes	During initial load	Notify parent of loading state
proceed	Yes	Yes	Cancel at root OR close window	Close configurator without saving
save	Yes	Yes	Save and exit navigation	Save configuration and exit
close_modal	Yes	Yes	Close preview	Close preview window
showConflictToast	Yes	Yes	Non-blocking API conflicts detected	Show conflict warning toast

This table shows the toast event Data Manager fires.

EVENT NAME	WHEN IS IT FIRED	PURPOSE
ShowToastEvent	After loading favorite successfully	Notify user of successful favorite load

Data Manager dispatches FlowAttributeChange events for all reactive properties on every UI update.

=== ARTICLE: ind.product_configurator_flow_footer.htm ===
---
article_id: ind.product_configurator_flow_footer.htm
title: Footer
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_footer.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Footer

Footer is the action bar at the bottom of Product Configurator. The component shows validation messages and action buttons. Footer publishes Lightning Message Service (LMS) events to Data Manager when users click these actions. Button visibility depends on context, such as nested product, preview mode, instant pricing, validation, and so on. Footer has no output properties and doesn’t listen to any events.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Footer Responsibilities
Show buttons including Cancel, Save & Exit, Done, Update Prices, and Validate Product based on context
Show validation alerts, warnings, and error messages from Product Configurator
Adjust button labels and variants based on navigation depth. For example, the Done button and the Save & Exit button labels change from one to the other depending on context
Publish LMS events for navigation, pricing, validation, and preview to Data Manager when a user clicks an action
Prompt the user for confirmation to cancel an action and close Product Configurator
Show Close button instead of Save & Exit button in preview mode
Footer API Name

S01_Actions

Input Properties

Footer accepts data from parent or flow component properties, set by users.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
navigationRoute	Array	No	Current navigation path
isClassContext (True when the record being previewed is a product classification (not a regular product)	Boolean	No	Whether the record is a product classification in preview mode.
isApiInProgress	Boolean	No	Whether an API call is in progress. Locks the component while the call runs.
isNonBlockingEnabled	Boolean	No	Whether non-blocking mode is enabled.
isDesignTime (General preview mode. True when any product or product classification is viewed in preview, for example, from App Builder or record page preview.)	Boolean	No	Whether the product or product classification is in preview mode.
isInstantPricingEnabled	Boolean	No	Whether instant pricing is enabled. If false, the Update Prices button is shown.
isInstantPricingToggleEnabled	Boolean	No	Whether the instant pricing toggle is shown.
isProductValidationEnabled	Boolean	No	Whether product validation is enabled.
messages	Array	No	Validation messages (alerts, warnings, errors) from the configurator.
Types of Events Footer Fires

Footer fires the LMS events shown in this table.

EVENT ACTION	WHEN IS IT FIRED	PURPOSE
navigate (type: done)	User clicks Done	Navigate up one level
navigate (type: cancel)	User confirms cancel	Close configurator without saving
navigate (type: save_and_exit)	User clicks Save & Exit	Save configuration and exit
updatePrices	User clicks Update Prices	Manually trigger pricing
validateProduct	User clicks Validate Product	Manually trigger validation
closePreview	User clicks Close in preview mode	Close preview window

=== ARTICLE: ind.product_configurator_flow_header.htm ===
---
article_id: ind.product_configurator_flow_header.htm
title: Header
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_header.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Header

Header, also called Config Header, is a control panel component that displays the configuration header with toggles, tabs, and informational banners at the top of Product Configurator. The component provides controls for users to toggle instant pricing, validation, and layout modes, and to navigate between multiple root products via tabs. Header has no output properties, and doesn’t listen to any events.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Header Responsibilities
Show the configuration title
Provide toggle controls for instant pricing, validation, and layout modes
Show tabs for multi-root bundle configurations
Show banners for outdated prices, validation, and price ramps
Send toggle and navigation Lightning Message Service (LMS) events to Data Manager
Show Favorites button, when it’s enabled
Header API Name

S01_ConfigHeader

Input Properties

Header accepts data from these parent and flow component properties, set by users.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
isDesignTime	Boolean	No	Whether in design or preview mode
isApiInProgress	Boolean	No	Whether API call is in progress
layoutMode	String	No	Layout mode: "standard" or "compact"
isPriceRampEnabled	Boolean	No	Whether price ramps are enabled
title	String	No	Configuration title
tabs	Array	No	Array of tabs for multi-root bundles
isInstantPricingToggleEnabled	Boolean	No	Whether instant pricing toggle is visible
isInstantPricingEnabled	Boolean	No	

Indicates whether Instant Pricing is enabled by default.

Use only the system default value for this property. If you enter any other value, the instant pricing functionality doesn't work.


rootProductId	String	No	Root product ID
explainabilityEnabled	Boolean	No	Whether the explainability toggle is enabled (explainability log collected during configuration).
showPrices	Boolean	No	Whether to show pricing information at run time
favoriteData	String	No	Configuration data for favorites
isNonBlockingEnabled	Boolean	No	Whether non-blocking mode is enabled
isGroupRampEnabled	Boolean	No	Whether group ramp deals are enabled for the product
currentGroupName	String	No	Name of the current group for the transaction item being configured.
Events Header Fires

Header fires the LMS events shown in this table.

EVENT ACTION	WHEN IS IT FIRED	PURPOSE
toggleInstantPricing	User toggles instant pricing	Toggle instant pricing on or off
toggleCompactLayout	User toggles compact layout	Toggle layout mode
toggleRulesValidation	User toggles validation	Toggle validation on/off
updatePrices	User clicks "Update Prices" link	Manually trigger pricing
navigate	User selects a tab	Go to selected root product

=== ARTICLE: ind.product_configurator_flow_messages.htm ===
---
article_id: ind.product_configurator_flow_messages.htm
title: Messages
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_messages.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Messages

Messages is a UI display component that renders validation messages to Product Configurator users. The component shows messages in an expandable accordion and filters messages by severity, either Error, Warning, or Info. Messages has no output properties, and doesn’t listen to or fire any events.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Messages Responsibilities
Display validation messages as Error, Warning, or Info, in an expandable accordion interface
Sort messages by severity
Show count badges for each message type
Allow users to filter messages by severity
Dynamically track accordion height
Support fixed or relative positioning for messages in the user interface
API Name

S01_Messages

Input Properties

Messages accepts data from these parent and flow component properties, set by users.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
messages	Array	Yes	Array of message objects from DataManager
areMessagesFixed	Boolean	No	

Whether messages have fixed position (scroll with UI) or relative position

=== ARTICLE: ind.product_configurator_flow_option_groups.htm ===
---
article_id: ind.product_configurator_flow_option_groups.htm
title: Option Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_option_groups.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Option Groups

Option Groups is the container component that shows child products organized into groups. The component manages option selection, dynamic option addition, cloning, and search navigation. Option Groups has no output properties.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Option Groups Responsibilities
Show product options organized by groups
Support tabs and accordion display
Process selection changes from child option components
Show window for browsing and adding dynamic options
Show window for cloning existing transaction items
Handle navigation to searched options
Publish Lightning Message Service (LMS) events to send selection changes, clone requests, and navigation to Data Manager
Manage context definition changes for customizable fields
Option Groups API Name

S01_OptionGroups

Input Properties

Option Groups receives input from parent or flow components, set by the customer.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
optionGroups	Array	Yes	Array of option groups from DataManager
salesTransactionItems	Array	No	Transaction items data
contextDefinition	String	No	Context definition ID
contextMetadata	String/Object	No	Metadata for STI attributes
portion1SelectedFields	String/Array	No	Custom fields for portion 1
portion2SelectedFields	String/Array	No	Custom fields for portion 2
currencyCode	String	No	Currency code for price display
isDesignTime	Boolean	No	Whether in design or preview mode
disabled	Boolean	No	Disables all option selection controls (checkboxes, radio buttons, quantity inputs, configure buttons).
isApiInProgress	Boolean	No	Whether API call is in progress
variant	String	No	Display mode: "tabs" or "accordions"
layoutMode	String	No	Layout mode: "standard" or "compact"
isNonBlockingEnabled	Boolean	No	Enable non-blocking mode
isGroupRampEnabled	Boolean	No	Enable group ramp functionality
showInlineAttributes	String	No	Whether to show inline attributes
numberOfInlineAttributes	Number	No	Number of inline attributes to display
searchResultOptionId	String	No	PRC ID of search result option
origin	string	No	Name of the transaction record's parent object.
Events Option Groups Listens To

Option Groups listens to the getProductFlowByProductId wire adapter. When a user selects Add Options for a dynamic option group, the wire adapter fetches the associated Flow API name to open the dynamic option flow window.

WIRE ADAPTER	SOURCE	WHAT IT LISTENS FOR	HANDLER METHOD	PURPOSE
getProductFlowByProductId	lightning/industriesEpcApi	Product flow data for dynamic options	setFlowId()	Retrieves flow API name for dynamic option window
Events Option Groups Fires

Option Groups fires LMS events and the FlowAttributeChange event.

Option Groups fires the LMS events shown in this table.

EVENT ACTION	WHEN IS IT FIRED	PURPOSE
LMS_EVENTS.VALUE_CHANGE	User changes attribute value	Notify DataManager of the changes to the options
cloneItems	User clones transaction items	Notify DataManager to clone STIs
contextDefinitionChange	Context definition changes	Notify DataManager of context definition change
navigate (search)	User cancels search mode	Notify DataManager to clear search result

This table shows the LMS_EVENTS.VALUE_CHANGE payload field types for Option Groups.

FIELD	WHEN IS IT FIRED	PURPOSE
isSelected	When a product is selected or deselected	Notify DataManager of the changes to the options for selecting a product
Quantity	When quantity is changed	Notify DataManager of the changes to the options for changing the quantity
AttributeField	When the attribute value in option card is changed	Notify DataManager of the changes to the options for changing the attribute value
ProductSellingModel	When ProductSellingModel value is changed	Notify DataManager of the changes to the Product Selling Model value change
CustomProductName	When a custom product name is changed	Notify DataManager of the changes to the options - changing the product name
ContextFields	When Context field values is changed in option card	Notify DataManager of the changes to the options change in context value
addedNodes	When there’s a change in addedNodes	Notify DataManager of the changes to the addedNodes
PromotionAdd	When promotion is added	Notify DataManager of promotion add
PromotionRemove	When promotion is removed	Notify DataManager of promotion remove

Option Groups fires the FlowAttributeChange event shown in this table.

EVENT ACTION	WHEN IS IT FIRED	PURPOSE
FLOW_ATTRIBUTE_CHANGE	User changes inline attribute	Notify flow of attribute change

=== ARTICLE: ind.product_configurator_flow_product_attributes.htm ===
---
article_id: ind.product_configurator_flow_product_attributes.htm
title: Product Attributes
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_product_attributes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Product Attributes

Product Attributes is the container component that shows product attributes in Product Configurator. The component organizes attributes by category and supports multiple display modes, including tabs, sections, and accordions. Product Attributes has no output properties and doesn’t listen to any events.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Product Attribute Responsibilities
Receive attributeCategories data from Data Manager
Support multiple display modes including tabs, sections, and accordions, and organize attributes by category
Render child components and creates attributeList components for each category
Publish Lightning Message Service (LMS) events and send attribute changes to Data Manager
Fire FlowAttributeChangeEvent for flow integration
Product Attributes API Name

S01_AttributesPanel

Input Properties

Product Attributes receives input from parent or flow components set by the customer.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
attributes	Array	Yes	Array of attribute categories from DataManager
variant	String	No	Display mode: "tabs", "sections", "accordions", or "scoped"
categorize	String	No	Whether to categorize attributes: "true" or "false"
columns	String	No	Number of columns: "1" or "2"
uncatAttrsLabel	String	No	Label for uncategorized attributes
disabled	Boolean	No	Disables all attribute input fields, preventing users from editing any attribute values.
isApiInProgress	Boolean	No	Whether an API call is in progress
Events Product Attributes Fires

Product Attributes fires Lightning Message Service (LMS) events and FlowAttributeChange events.

Product Attributes fires the LMS event shown in this table.

EVENT ACTION	WHEN IS IT FIRED	PURPOSE
LMS_EVENTS.VALUE_CHANGE	User changes attribute value	Notify Data Manager of the changes

Product Attributes fires the FlowAttributeChange event shown in this table.

EVENT ACTION	WHEN IS IT FIRED	PURPOSE
FLOW_ATTRIBUTE_CHANGE	User changes attribute value	Notify flow of attribute change

=== ARTICLE: ind.product_configurator_flow_product_header.htm ===
---
article_id: ind.product_configurator_flow_product_header.htm
title: Product Header
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_product_header.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Product Header

Product Header shows product information at the top of each product or option in Product Configurator. The component shows product name, description, image, quantity input, pricing, and Product Selling Model (PSM) selection. It's a UI presentation component that publishes user changes via Lightning Message Service (LMS) events. Product Header has no output properties.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Product Header Responsibilities
Display product information including name, description, image, quantity, and price
Handle user input including quantity changes, PSM selection, and custom product name editing
Send user input to Data Manager via LMS events
Show configurable fields in the top and bottom regions of the configurator
Support standard and compact layout modes
Validate quantity input and custom product names
Product Header API Name

S01_Header

Product Header Input Properties

The Product Header receives input from parent or flow components, set by the customer.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
header	Object	No	Main product header data (quantity, price, name, PSM)
currencyCode	String	No	Currency code for price display
quantityReadOnly	Boolean	No	Makes quantity field read-only
isClassContext (Product Classification Preview Mode)	Boolean	No	Whether the component is in class context mode
isApiInProgress (isApiInProgress)	Boolean	No	Whether an API call is in progress
isDesignTime (isDesignTime)	Boolean	No	Whether in design or preview mode
disabled	Boolean	No	Disables all inputs
layoutMode	String	No	Layout mode (standard or compact)
contextMetadata	String	No	Metadata for STI attributes (labels, data types) as a JSON String
eligiblePromotions	Array	No	List of promotions available for this product
isNonBlockingEnabled	Boolean	No	Whether non-blocking is enabled
Events the Product Header Listens To

Product Header listens to Lightning Message Service (LMS) events and wire adapters.

Product Header subscribes to the message channel to receive state updates as LMS events from the Data Manager. The Product Header listens to the LMS events shown in this table.

EVENT ACTION	HANDLER METHOD	WHAT IT DOES
valueChange	handleLmsMessage()	Tracks which field is being changed
navigate (type='cancel')	handleLmsMessage()	Tracks cancel navigation

The Product Header listens to the wire adapter event shown in this table.

WIRE ADAPTER	SOURCE	WHAT IT LISTENS FOR	HANDLER METHOD	PURPOSE
MessageContext	lightning/messageService	Message context for LMS	Not applicable (provides context)	Enables LMS communication
Events the Product Header Fires

The Product Header fires the Lightning Message Service (LMS) event shown in this table.

EVENT ACTION	WHEN IS IT FIRED	PURPOSE
LMS_EVENTS.VALUE_CHANGE	User changes fields	Notify Data Manager of the changes

=== ARTICLE: ind.product_configurator_flow_screen_components.htm ===
---
article_id: ind.product_configurator_flow_screen_components.htm
title: Product Configurator Flow Screen Components
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_screen_components.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_explore_the_product_configurator_flow.htm
fetched_at: 2026-09-04
---

# Product Configurator Flow Screen Components

Product Configurator provides a sample flow, Default Product Configurator Flow. The default flow contains a screen element with components that collect and display information in Product Configurator. For information on each screen component, including its responsibilities and properties, see the topics linked here.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Breadcrumbs
Breadcrumbs shows the navigation path through the product bundle hierarchy in Product Configurator. The component displays clickable breadcrumb links so users can move between levels, such as root product → option group → option. Breadcrumbs has no output properties and doesn’t listen to any events.
Data Manager
Data Manager is the state management and orchestration component for Product Configurator. This component stores product data and uses flow events to propagate the data to other components on the flow screen.
Footer
Footer is the action bar at the bottom of Product Configurator. The component shows validation messages and action buttons. Footer publishes Lightning Message Service (LMS) events to Data Manager when users click these actions. Button visibility depends on context, such as nested product, preview mode, instant pricing, validation, and so on. Footer has no output properties and doesn’t listen to any events.
Header
Header, also called Config Header, is a control panel component that displays the configuration header with toggles, tabs, and informational banners at the top of Product Configurator. The component provides controls for users to toggle instant pricing, validation, and layout modes, and to navigate between multiple root products via tabs. Header has no output properties, and doesn’t listen to any events.
Messages
Messages is a UI display component that renders validation messages to Product Configurator users. The component shows messages in an expandable accordion and filters messages by severity, either Error, Warning, or Info. Messages has no output properties, and doesn’t listen to or fire any events.
Option Groups
Option Groups is the container component that shows child products organized into groups. The component manages option selection, dynamic option addition, cloning, and search navigation. Option Groups has no output properties.
Product Attributes
Product Attributes is the container component that shows product attributes in Product Configurator. The component organizes attributes by category and supports multiple display modes, including tabs, sections, and accordions. Product Attributes has no output properties and doesn’t listen to any events.
Product Header
Product Header shows product information at the top of each product or option in Product Configurator. The component shows product name, description, image, quantity input, pricing, and Product Selling Model (PSM) selection. It's a UI presentation component that publishes user changes via Lightning Message Service (LMS) events. Product Header has no output properties.
Summary
Summary is a UI display component that renders the pricing summary section in Product Configurator. The component displays the current product's pricing information, including one-time, monthly, and annual totals, along with a hierarchical breakdown of child products and their prices. Summary has no output properties, and doesn’t listen to or fire any events.
Transaction Header
Transaction Header is a navigation and control component that displays a header with a dynamic Back or Cancel button at the top of Product Configurator. The component allows users to exit the configurator and navigate back to the parent transaction record. Transaction Header has no output properties and doesn’t listen to any events.

=== ARTICLE: ind.product_configurator_flow_summary.htm ===
---
article_id: ind.product_configurator_flow_summary.htm
title: Summary
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_summary.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Summary

Summary is a UI display component that renders the pricing summary section in Product Configurator. The component displays the current product's pricing information, including one-time, monthly, and annual totals, along with a hierarchical breakdown of child products and their prices. Summary has no output properties, and doesn’t listen to or fire any events.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Summary Responsibilities
Display prices, including one-time, monthly, and annual
Display nested product pricing structure
Update pricing data based on the user’s current navigation route
Calculate and display subtotals for product groups
Support custom fields in pricing footer and pane
Handle Asset Renewal Configuration (ARC), also called delta pricing
Switch between standard and custom layouts
Summary API Name

S01_Summary

Input Properties

Summary accepts data from these parent and flow component properties, set by users.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
summary	Object	Yes	Summary data from DataManager (merged transaction tree)
salesTransactionItems	Array	No	Transaction items data
navigationRoute	Array	No	Current navigation route (breadcrumb path)
currencyCode	String	No	Currency code for price display
isDesignTime	Boolean	No	Whether in design or preview mode
layoutMode	String	No	

Layout mode (standard or compact)

=== ARTICLE: ind.product_configurator_flow_transaction_header.htm ===
---
article_id: ind.product_configurator_flow_transaction_header.htm
title: Transaction Header
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_flow_transaction_header.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_flow_screen_components.htm
fetched_at: 2026-09-04
---

# Transaction Header

Transaction Header is a navigation and control component that displays a header with a dynamic Back or Cancel button at the top of Product Configurator. The component allows users to exit the configurator and navigate back to the parent transaction record. Transaction Header has no output properties and doesn’t listen to any events.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Transaction Header Responsibilities
Show the Back/Cancel button with dynamic label
Navigate back to parent transaction record
Show confirmation dialog before canceling, when the user isn’t in preview mode
Handle preview mode without confirmation
Fire CustomEvent to close Product Configurator
Transaction Header API Name

S01_TransactionHeader

Input Properties

Transaction Header accepts data from this property, set by users.

PROPERTY	TYPE	REQUIRED	DESCRIPTION
transactionRecord	Object	Yes	Transaction record data (parentId, parentName, origin)
Events Transaction Header Fires

Transaction Header fires this custom event to close Product Configurator.

EVENT NAME	BUBBLES	COMPOSED	WHEN IS IT FIRED	PURPOSE
proceed	Yes	Yes	User confirms cancel (non-preview mode)	Close configurator without saving

=== ARTICLE: ind.product_configurator_get_latest_pricing.htm ===
---
article_id: ind.product_configurator_get_latest_pricing.htm
title: Get the Latest Pricing
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_get_latest_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configure_products.htm
fetched_at: 2026-09-04
---

# Get the Latest Pricing

Use Instant Pricing to control the pricing calls made for each configuration change. When you change product selections, the prices shown in the summary component change immediately.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To turn on instant pricing:	Product Configurator
NOTE Product Configurator shows amounts in the currency unit selected in your personal settings without converting the amounts.
From the App Launcher, find and select Quotes or Orders.
From the list view, open the record that contains the line item that you want to configure.
If necessary, edit the record to change the transaction type. The selected type determines which rules engine runs product configuration rules. The Transaction Type field is available only if Transaction processing for quotes and orders is turned on.
To view the line item that you want to configure, perform one of these actions based on your selection.
On the quote record details page, go to the Quote Line Items tab.
On the order record details page, go to the Lines tab.
From the quick action menu of the line item that you want to get the latest price for, select Configure.
Turn on Instant Pricing.

The summary component automatically shows the latest pricing for every change in the product configuration. If instant pricing is turned off, the summary component isn’t updated with the latest price for the selected products.

To get the latest price manually, click Update Price.
Click Save and Exit.

=== ARTICLE: ind.product_configurator_get_started.htm ===
---
article_id: ind.product_configurator_get_started.htm
title: Get Started with Product Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_get_started.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_introduction.htm
fetched_at: 2026-09-04
---

# Get Started with Product Configurator

Enable Product Configurator to set up and customize the product configuration experience efficiently. Then, assign the required permission sets to users to tailor their access.

Enable Product Configurator
Give users the ability to configure products at run time and access all Product Configurator features.
Product Configurator Permission Sets
Product Configurator is managed by users with varying roles and expertise. Give users appropriate access by assigning prebuilt permission sets or custom permission set groups.

=== ARTICLE: ind.product_configurator_import_object_data.htm ===
---
article_id: ind.product_configurator_import_object_data.htm
title: Import Data from Salesforce Objects to Use in Constraint Models
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_import_object_data.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_create_a_constraint_model.htm
fetched_at: 2026-09-04
---

# Import Data from Salesforce Objects to Use in Constraint Models

Import data from a standard or custom Salesforce object to use in a table constraint in a constraint model. The imported data populates the columns and rows in the table constraint in CML, and saves you the step of manually entering the data.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To import object data:	Product Configuration Constraints Designer permission set

Only the first 10,000 records with a maximum of 10 custom fields from the Salesforce object are imported.

In Setup, enter Permission Sets in Quick Find and select Permission Sets.
Select the Constraint Rules Engine Licenseless permission set. If the Constraint Rules Engine Licenseless permission set for the Platform Integration User isn't available in your org, contact Salesforce Customer Support.
In the Apps section of the setup page for Constraint Rules Engine Licenseless permission set, select Object Settings.
Locate and select the object whose data you want to import to a table constraint.
On the Object Settings page for the object, select Edit. Enable Read, Create, Edit, Delete, View All Records, and View All Fields permissions, then save your changes.
To confirm that the permissions are enabled, open Object Manager and select the object whose data you want to import.
Select Object Access. On the Permission Sets tab, confirm that the Constraint Rules Engine Licenseless permission set is listed, with Read, Create, Edit, and Delete permissions enabled.
To load the imported data into a constraint, in CML Editor, write an expression in the constraint model code. Use the SalesforceTable keyword and include the table name and column names.
EXAMPLE

In this example, data is imported to a table with four columns. The suffix __c indicates that the data is from a Salesforce custom object.

constraint(table(attr1, attr2, attr3, attr4, SalesforceTable("tablename__c","column1name__c,column2name__c,column3name__c,column4name__c")));

NOTE If the table data is deployed when the constraint model is activated, and you add records to the table after constraint model activation, to fetch the new table data at runtime you must deactivate and reactivate the constraint model.

=== ARTICLE: ind.product_configurator_integrate_third_party_configurator_ui_components_into_first_party_configurator.htm ===
---
article_id: ind.product_configurator_integrate_third_party_configurator_ui_components_into_first_party_configurator.htm
title: Third-Party Configurator UI Component Integration into First-Party Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_integrate_third_party_configurator_ui_components_into_first_party_configurator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator.htm
fetched_at: 2026-09-04
---

# Third-Party Configurator UI Component Integration into First-Party Configurator

As a third-party user, apart from replacing the first-party configurator, you can also create a custom Lightning Flow UI configurator component and integrate the UI component to the first-party configurator UI. This approach provides a functional enhancement to the existing first-party configurator UI.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

To add a widget, include the Lightning Web Component (LWC) in the ISV managed package. After the LWC component is available, the product catalog admin modifies the default first-party configurator to add the third-party user’s custom LWC components. The widgets can interact with the first-party configurator data, including:

Product details and bundle configurations.
Product pricing and pricing results.
Product attributes and their specified values.
EXAMPLE Consider a map widget that a third-party user develops by using the LWC platform’s map UI component. When you select a location on the map, the widget automatically updates the latitude and longitude coordinates stored as product attributes. Sales reps can use this widget to configure the location for a specific product.

=== ARTICLE: ind.product_configurator_introduction.htm ===
---
article_id: ind.product_configurator_introduction.htm
title: Configure Your Products in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_introduction.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
fetched_at: 2026-09-04
---

# Configure Your Products in Revenue Management

Use the Product Configurator tool to customize the components and attributes of a product so that the final configured product meets the business requirement expectations. Product configuration entails customizing a product to align with the specific requirements of a customer.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.

By using the Product Configurator, present complex product offerings to customers efficiently. The Product Configurator tool provides users with an optimized and intuitive interface making it simple and easy to select the most suitable combination of features for a complex product. The Product Configurator not only facilitates the configuration of product bundles, but it also facilitates the customization of individual product attributes.

With Product Configurator, your sales representatives can validate product selections instantly and get immediate cost insights with real-time pricing updates. The Product Configurator proves to be a valuable asset for businesses that offer complex products. It contributes to saving time and resources, enhancing accuracy, and elevating the customer experience.

Some of the key features of the Product Configurator tool are:

Customize the product configurator flow: The product configurator flow with purpose-built user interface components offers a ready-made foundation for your product configurator. Customize and extend the Product Configurator flow to create a unique look and feel that aligns with your brand.
Preview runtime experience: Assign multiple products or product classes to a product configurator flow and preview the user experience in real-time.
Build complex product bundles with ease: Product Configurator's intuitive interface and headless APIs support multi-level product bundle structures. Users can effortlessly configure quantities, attributes, and options while receiving real-time pricing updates.
Customizable configuration rules: Manage the attribute structure in the product bundle with cardinality check, product selection validations, and messages.
Get Started with Product Configurator
Enable Product Configurator to set up and customize the product configuration experience efficiently. Then, assign the required permission sets to users to tailor their access.
Set Up Product Configurator
Product Configurator provides a framework to define and apply rules and constraints when configuring products. It features two rules engines: Constraint Rules Engine and Business Rules Engine.
Explore the Product Configurator Flow
The product configurator flow outlines the layout for presenting customizable product information in the user interface.
Configure Products with Product Configurator
Create complex product configurations with ease by using Product Configurator. Define attributes, variants, and metadata. Test and verify your product configurations with the built-in run-time experience. Your users can use the Product Configurator to easily configure the product options during the purchase process and view the relevant pricing.
Rules and Constraints in Configurator With Constraint Rules Engine
To create configuration rules and constraints that can validate large and complex product configurations, use Constraint Rules Engine.
Define Configuration Rules with Business Rules Engine
When you configure products for sale, make sure that all your products have valid attributes and are compatible with other products in the offering. With configuration rules, make sure that the product configuration aligns with the business needs and standards and that your sales reps select the right set of products.
Third-Party Configurator
Revenue Management (formerly Revenue Cloud) provides extensibility options to third-party users seeking to build integrations with the Revenue Management product. Revenue Management supports various third-party use cases. The support includes replacing the first-party configurator with the third-party configurator, integrating third-party UI components into the first-party configurator, and creating custom configurator UI using headless configurator APIs.
Product Configurator Limits
Review the default limits for Product Configurator before you configure products, define configuration rules, or create constraint models.

=== ARTICLE: ind.product_configurator_invocable_action_apex_call.htm ===
---
article_id: ind.product_configurator_invocable_action_apex_call.htm
title: Use an Apex Call to Run the Run Config Rules Action
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_invocable_action_apex_call.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_invocable_action_to_run_rules.htm
fetched_at: 2026-09-04
---

# Use an Apex Call to Run the Run Config Rules Action

Use an Apex call to run the Run Config Rules invocable action with the Hide/Disable, Message, or Recommend rule.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To work with configuration rules	Manage Configurator with Constraint Rules Engine
To use the Run Config Rules invocable action	Product Configuration Rules User
To work with Apex	Apex Author

For information on the Run Config Rules invocable action, see Run Config Rules Action in the Revenue Management Developers Guide.

Make an Apex call to create, debug, and execute the Run Config Rules invocable action, similar to this example.

EXAMPLE
public class RunConfigRulesDebugger {
    public static void debugRunConfigRules(String quoteId) {
        try {
            // Create the invocable action with namespace
            Invocable.Action action = Invocable.Action.createStandardAction('runConfigRules');
            
            System.debug('Setting transactionContextId parameter with value: ' + quoteId);
            
            action.setInvocationParameter('transactionId', quoteId);
            
            // Debug the action parameters
            System.debug('Action parameters: ' + action);
            
            // Execute the action
            System.debug('Invoking action...');
            List<Invocable.Action.Result> results = action.invoke();
            
            System.debug('Number of results: ' + results.size());
            
            // Process the results
            if (!results.isEmpty()) {
                Invocable.Action.Result result = results[0];
                System.debug('Is Success: ' + result.isSuccess());
                System.debug('Results are: ' + results);
                
            } 
         } catch (Exception e) {
            System.debug('=== EXCEPTION ===');
            System.debug('Exception occurred: ' + e.getMessage());
            System.debug('Stack trace: ' + e.getStackTraceString());
        }
       }
}

=== ARTICLE: ind.product_configurator_invocable_action_api_call.htm ===
---
article_id: ind.product_configurator_invocable_action_api_call.htm
title: Use an API Call to Run the Run Config Rules Action
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_invocable_action_api_call.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_invocable_action_to_run_rules.htm
fetched_at: 2026-09-04
---

# Use an API Call to Run the Run Config Rules Action

Use an API call to run the Run Config Rules invocable action with the Hide/Disable, Message, or Recommend rule.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To work with configuration rules:	Manage Configurator with Constraint Rules Engine
To use the Run Config Rules invocable action:	Product Configuration Rules User
To use the Revenue Management REST API:	Product Configurator API User

For information on the Run Config Rules invocable action, see Run Config Rules Action in the Revenue Management Developers Guide.

Use the Revenue Management REST API to send a POST request to this endpoint. /services/data/v65.0/actions/standard/runConfigRules

Use a JSON object for the request body with a top-level key named inputs that contains the method parameters, as in this example.

EXAMPLE
{
  "inputs": [
    {
      "transactionId": "order or quote"
    }
  ]
}

=== ARTICLE: ind.product_configurator_invocable_action_screen_flow.htm ===
---
article_id: ind.product_configurator_invocable_action_screen_flow.htm
title: Use a Screen Flow to Run the Run Config Rules Action
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_invocable_action_screen_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_invocable_action_to_run_rules.htm
fetched_at: 2026-09-04
---

# Use a Screen Flow to Run the Run Config Rules Action

Use a screen flow to run the Run Config Rules invocable action with the Hide/Disable, Message, or Recommend rule.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To work with configuration rules:	Manage Configurator with Constraint Rules Engine
To use the Run Config Rules invocable action:	Product Configuration Rules User
To create a flow:	Manage Flow

For information on the Run Config Rules invocable action, see Run Config Rules Action in the Revenue Management Developers Guide. For information on working with flows, see Define Product Configuration Flows.

Create a screen flow.
Add the Run Config Rules action and give it a name.
Pass the quote Transaction ID.
To identify any errors, turn on debug options and run the flow. See Debug a Screen Flow with the Debugger Example.

=== ARTICLE: ind.product_configurator_invocable_action_to_run_rules.htm ===
---
article_id: ind.product_configurator_invocable_action_to_run_rules.htm
title: Run Rules with the Run Config Rules Action
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_invocable_action_to_run_rules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_advanced.htm
fetched_at: 2026-09-04
---

# Run Rules with the Run Config Rules Action

Use the Run Config Rules invocable action to run Hide/Disable, Message, and Recommend rules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Use an Apex call, an API call, or a screen flow to run the Run Config Rules invocable action.

Run the action with the Hide/Disable rule to hide an element or to prevent a user from selecting it ins the selection menu in Product Configurator.
Run the action with the Message rule to show a message to users in Product Configurator.
Run the action with the Recommend rule to show recommended products associated with the product the user is configuring in Product Configurator.

For more information on working with these rules, see the section for each rule in the CML User Guide. For more information on the invocable action, see Run Config Rules Action in the Revenue Management Developers Guide.

Use an Apex Call to Run the Run Config Rules Action
Use an Apex call to run the Run Config Rules invocable action with the Hide/Disable, Message, or Recommend rule.
Use an API Call to Run the Run Config Rules Action
Use an API call to run the Run Config Rules invocable action with the Hide/Disable, Message, or Recommend rule.
Use a Screen Flow to Run the Run Config Rules Action
Use a screen flow to run the Run Config Rules invocable action with the Hide/Disable, Message, or Recommend rule.

=== ARTICLE: ind.product_configurator_limits.htm ===
---
article_id: ind.product_configurator_limits.htm
title: Product Configurator Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_introduction.htm
fetched_at: 2026-09-04
---

# Product Configurator Limits

Review the default limits for Product Configurator before you configure products, define configuration rules, or create constraint models.

Transaction Line Item Limits

Keep the limits associated with quote and order line items in mind while configuring your products.

See Transaction Management Limits.

Product and Bundle Limits

Keep the limits associated with products and bundles in mind while working on your product configurations.

See Product Catalog Management Limits.

Constraint Rules Engine and Constraint Model Limits
The size of a constraint model can be up to 6MB.
Table constraints can support a maximum of 10,000 records with a maximum of 10 custom fields in the Salesforce object. Only the first 10,000 records are imported from the object.
The maximum execution time for constraints is 10 seconds.
Large Transaction Limits

When you configure products in a large transaction, Product Configurator processes the transaction's line items and attributes together. Keep these limits in mind when you work with large transactions.

Each configuration request supports up to 5,000 changes from user input and up to 5,000 changes generated by rules, where a change is an added, updated, or removed line item or attribute.
The maximum response size for a single configuration request can be up to 10 MB. This maximum is set by your org's synchronous Apex heap size limit, which is defined by the Apex platform. To increase this limit, contact Salesforce Customer Support.
The gateway timeout for a configuration request is 31 seconds.
Other Limits

The number of saved configurations is limited to 80 per user per product reference record ID.

=== ARTICLE: ind.product_configurator_load_product_defaults.htm ===
---
article_id: ind.product_configurator_load_product_defaults.htm
title: Load Product Defaults from PCM to a Constraint Model
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_load_product_defaults.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_create_a_constraint_model.htm
fetched_at: 2026-09-04
---

# Load Product Defaults from PCM to a Constraint Model

Include product defaults defined in Product Catalog Management (PCM), such as attributes, attribute values, and custom and standard fields, when you import products to a Constraint Modeling Language (CML) constraint model.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To import object data:	Product Configuration Constraints Designer permission set

When you use a constraint tag to read a value from a SalesTransactionItem field, such as “ProductCode__c”, the value is fetched at runtime and passed to the constraint engine. You can use the product field name to directly fetch the field value from Product2. The value is cached at the time of model activation. Changes made to the value after model activation aren’t reflected at runtime. You must deactivate and reactivate the model to update the field value.

To load referenced product field values into CML constraints, turn on Read access to the Product object for the Constraint Rules Engine Licenseless permission set.

In Setup, enter Permission Sets in Quick Find and select Permission Sets.
Select the Constraint Rules Engine Licenseless permission set.
NOTE If the Constraint Rules Engine Licenseless permission set for the Platform Integration User isn't available in your org, contact Salesforce Customer Support.
In the Apps section of the setup page for Constraint Rules Engine Licenseless permission set, select Object Settings.
For the Products object, turn on Read permission for Object Permissions and for the fields that you want to reference in the CML constraint.
To reference product field values in a constraint by using CML Editor, include the productField attribute annotation in the constraint to map a CML attribute to the corresponding product field.
NOTE When you use Visual Builder to import products from PCM, Constraint Rules Engine automatically includes field values.

=== ARTICLE: ind.product_configurator_make_product_names_editable.htm ===
---
article_id: ind.product_configurator_make_product_names_editable.htm
title: Make Product Names Editable in Product Option Cards
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_make_product_names_editable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_flow.htm
fetched_at: 2026-09-04
---

# Make Product Names Editable in Product Option Cards

Give sales reps access to edit product names from the product option cards during bundle configurations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create and edit a product configuration flow:	Product Configurator
To change field accessibility:	Customize Application AND Manage Profiles and Permission Sets

If you cloned the Default Product Configurator flow after Winter ’27, product names are read-only by default. To make them editable, grant edit access to the Custom Product Name field on the transaction line item objects and set the Read-Only Product Name flow attribute to false in your custom product configurator flow. Only child product names are editable.

Provide Edit Access to the Custom Product Name Field

Set field-level security on the Custom Product Name field on the Quote Line Item and Order Product (OrderItem) objects. Product Configurator shows the edit icon next to the product name on an option card only to users who have edit access to this field.

Go to the object management settings of the Quote Line Item and Order Product objects, and edit the field-level security of the Custom Product Name field.

Select Visible and deselect Read-Only for user profiles of that require edit access.

See Modify Field Access Settings.

Set the Read-Only Product Name Flow Attribute
From Setup, in the Quick Find box, enter Flow, and then select Flows.
Open your product configurator flow.
Edit the screen element and select the Product Configurator Option Groups component.
To enable editing of product names on option cards, for the Read-Only Product Name attribute, select {!$GlobalConstant.False}.
Save your changes and activate the flow.

=== ARTICLE: ind.product_configurator_non_blocking_enabled.htm ===
---
article_id: ind.product_configurator_non_blocking_enabled.htm
title: Enable Non-Blocking Behavior in the Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_non_blocking_enabled.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_flow.htm
fetched_at: 2026-09-04
---

# Enable Non-Blocking Behavior in the Configurator

Enable non-blocking behavior so that configurator users can change multiple attribute and option values on a product asynchronously. The configuration page loads the changes without waiting for the constraint engine to process each setting individually. After processing is complete, the user can save the configuration.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To enable non-blocking behavior:	Product Configuration Constraints Designer permission set

When you turn on Non Blocking Enabled, if the configurator user selects values for attributes or options that violate rules on the constraint model, a warning message appears. For most rules, the constraint engine overrides the user selection that violates a rule, and replaces it with a valid value. For hide/disable rules, the value that the user selects overrides the constraint engine, even if the value violates the rule.

From Setup, in the Quick Find box, enter Flow, and then select Flows.
Open your product configurator flow.
Edit the screen element and select the Product Configurator Data Manager component.
To enable non-blocking behavior, for the Non Blocking Enabled attribute, select {!$GlobalConstant.True}.
If you’re using the default Configurator flow, continue to step 6. For a custom flow, repeat steps 3-4 to set the Non Blocking Enabled attribute for all the screen components.
When you've finished setting the attribute values, select Done.
To activate the changes, select Save as New Version, then select Activate.

=== ARTICLE: ind.product_configurator_place_quote_api_for_data_transfer.htm ===
---
article_id: ind.product_configurator_place_quote_api_for_data_transfer.htm
title: Use Place Sales Transaction API for Data Transfer
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_place_quote_api_for_data_transfer.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator.htm
fetched_at: 2026-09-04
---

# Use Place Sales Transaction API for Data Transfer

Transfer data from a custom configurator to a quote or order in Revenue Management by using the Place Sales Transaction API.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

The Place Sales Transaction API offers flexibility to either include or exclude the first-party configurator logic. Further, third-party users can use the first-party configurator API tasks such as validating the bundle structure, applying Salesforce Pricing rules, or implementing qualification rules.

EXAMPLE

"configurationInput": ["skip" / "runAndAllowErrors" / "runAndBlockErrors"], // Default runAndBlockErrors
"configurationOptions": {
"validateProductCatalog": true,
"validateAmendRenewCancel": true,
"executeConfigurationRules": true,
"addDefaultConfiguration": true
}
// rest of Place Sales Transaction API payload
}

=== ARTICLE: ind.product_configurator_preview_the_product_configurator.htm ===
---
article_id: ind.product_configurator_preview_the_product_configurator.htm
title: Preview the Product Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_preview_the_product_configurator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_explore_the_product_configurator_flow.htm
fetched_at: 2026-09-04
---

# Preview the Product Configurator

See how the product configurator looks and functions for your users.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To preview the product configurator:	Product Configurator

Products and product classifications with an assigned product configuration flow use that flow. Products and product classifications without an assigned product configuration flow use the default product configuration flow.

From the App Launcher, find and select Products.
Open the product that you want to preview the configurator for.
From the quick action menu, select Preview.

Similarly, open the product classification that you want to preview the configurator for.

=== ARTICLE: ind.product_configurator_product_configurator_permissions.htm ===
---
article_id: ind.product_configurator_product_configurator_permissions.htm
title: Product Configurator Permission Sets
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_product_configurator_permissions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_get_started.htm
fetched_at: 2026-09-04
---

# Product Configurator Permission Sets

Product Configurator is managed by users with varying roles and expertise. Give users appropriate access by assigning prebuilt permission sets or custom permission set groups.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Create Users and Profiles

To begin, create users for Product Configurator. Then assign users the appropriate permission sets. To help you plan, refer to the permission set table for Product Configurator.

When you create a user, you must also assign a profile. Profiles define default settings for users. Some organizations create their own profiles, while others choose to use profiles included with Salesforce.

Remember, users can have only one profile, but can have many permission sets assigned to them.

Assign Permission Sets

These prebuilt permission sets are based on user personas. Assigning these permission sets automatically grants the necessary user permissions and permission set license, and access to the features, objects, and fields needed to set up and use Product Configurator.

All these permission sets are available with the Product Configuration User permission set license.

Permission Sets
PERMISSION SET	INCLUDED PERMISSIONS
Product Configurator	Assign this permission set to users who need read and edit access to Product Configurator objects and APIs.
Product Configuration Rules Designer	Assign this permission set to users who create and manage product configuration rules in Product Configurator with Business Rules Engine.
Product Configuration Constraints Designer	Assign this permission set to users who create and manage constraint types and rules in Product Configurator with Constraint Rules Engine.
Assign User Permissions

If you require more granular control and flexibility over user access, create a custom permission set and assign these individual user permissions based on the specific tasks that users must perform.

User Permissions
USER PERMISSION	INCLUDED PERMISSIONS
Product Configurator	Assign this user permission to users who need read and edit access to Product Configurator objects.
Product Configurator API User	Assign this user permission to users who need read and edit access to Headless Configurator APIs.
Manage Configurator with Business Rules Engine	Assign this user permission to users who need to create, read, edit, and delete configuration rules in Product Configurator with Business Rules Engine.
Manage Configurator with Constraint Rules Engine	Assign this user permission to users who need create, read, edit, and delete constraint types and rules in Product Configurator with Constraint Rules Engine.
SEE ALSO
View and Manage Users
Create or Clone Profiles
Manage Permission Set Assignments
Permission Set Groups
Manage Muting Permission Sets

=== ARTICLE: ind.product_configurator_product_validation_enable.htm ===
---
article_id: ind.product_configurator_product_validation_enable.htm
title: Validate Product Configuration
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_product_validation_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configure_products.htm
fetched_at: 2026-09-04
---

# Validate Product Configuration

Product validation rules enhance the performance and address potential errors before saving a configuration.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To turn on product validation:	Product Configurator permission set
From the App Launcher, find and select Quotes or Orders.
From the list view, open the record that contains the line item that you want to configure.
If necessary, edit the record to change the transaction type. The selected type determines which rules engine runs product configuration rules. The Transaction Type field is available only if Transaction processing for quotes and orders is turned on.
To view the line item that you want to configure, perform one of these actions based on your selection.
On the quote record details page, go to the Quote Line Items tab.
On the order record details page, go to the Lines tab.
From the quick action menu of the line item that you want to validate, select Configure.
Turn on Product Validation.

The validation rules run automatically for every change in the product selection.

To validate the product configuration manually, click Validate.
Click Save and Exit.

=== ARTICLE: ind.product_configurator_select_context_attributes.htm ===
---
article_id: ind.product_configurator_select_context_attributes.htm
title: Select Context Attributes to Improve Configurator Performance
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_select_context_attributes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_flow.htm
fetched_at: 2026-09-04
---

# Select Context Attributes to Improve Configurator Performance

Select specific context attributes that you want the Configuration API to query and return, instead of it returning all of them by default. Your selection narrows the query and the response to the data that your configurations need, so Product Configurator responds faster, even for large transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create and edit a product configuration flow:	Product Configurator

If you don't select any context attributes, the Configuration API continues to query all context attributes. Your existing flows keep working with the same performance as before.

From Setup, in the Quick Find box, enter Flow, and then select Flows.
Open your product configurator flow.
Edit the screen element and select the Product Configurator Data Manager component.
For the Context Definition attribute, select the context definition that defines the data structure for the Configuration API to query. The context definition determines which context nodes and attributes you can select.
For the Context Node attribute, select a context node that contains context attributes for the Configuration API to query. You can select context attributes from multiple nodes as needed. Your selections persist when you switch nodes.
In the Context Attributes section, from the Available Attributes list, select the context attributes that you want the Configuration API to query. To improve performance, select only the attributes that you need.
NOTE Context attributes that are essential to the user interface functionality are preselected and locked.
Repeat steps 5 and 6 for every context node that you want to select attributes from.
Save your changes and activate the flow.

=== ARTICLE: ind.product_configurator_set_up_a_custom_dynamic_addition_screen_flow.htm ===
---
article_id: ind.product_configurator_set_up_a_custom_dynamic_addition_screen_flow.htm
title: Set Up a Custom Dynamic Addition Screen Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_set_up_a_custom_dynamic_addition_screen_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_explore_the_product_configurator_flow.htm
fetched_at: 2026-09-04
---

# Set Up a Custom Dynamic Addition Screen Flow

Build a screen flow that replaces the default add-products experience for a product classification during bundle configurations. When a product classification uses a Dynamic Addition Flow, Product Configurator can open your own flow with a custom interface and logic. Publish the product selections back to the Configurator as an addedNodes payload with Lightning Message Service (LMS) so that your quote or order lines stay in sync.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To clone the default product configurator flow and create a product configuration flow:	Product Configurator
Clone and customize the Default Product Configurator Flow, add a new screen flow, and then define these input attributes:
ATTRIBUTE	DATA TYPE	FLOW COMPONENT
Transaction ID	String	Product Configurator Data Manager
Option Groups	Apex-Defined (ProductConfig__OptionGroup)	Product Configurator Option Groups
Sales Transaction Items	Apex-Defined (ProductConfig__SalesTransactionItem)	Product Configurator Option Groups

The Product Configurator passes the transaction ID, the option group data, and the parent sales transaction items to your flow through these attributes.

In the flow, create the addedNodes payload to be passed back to Configurator.

The addedNodes value is an array of objects. Each object has a path in the form [transactionId, nodeId] and an addedObject, such as a quote line item or a quote line item relationship.

{
  "addedNodes": [
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589"
      ],
      "addedObject": {
        "id": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemSource": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "SalesTransactionItemParent": "0Q0xx0000004EvcCAE",
        "PricebookEntry": "01uxx00000090VuAAI",
        "ProductSellingModel": "0jPxx00000001KHEAY",
        "UnitPrice": 15.26,
        "Quantity": 1,
        "Product": "01txx0000006lfHAAQ",
        "businessObjectType": "QuoteLineItem"
      }
    },
    {
      "path": [
        "0Q0xx0000004EvcCAE",
        "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ref_d85b036d_d305_4bb6_aba8_a1dff645a664"
      ],
      "addedObject": {
        "id": "ref_d85b036d_d305_4bb6_aba8_a1dff645a664",
        "MainItem": "0QLxx0000004QdRGAU",
        "AssociatedItem": "ref_d3a3f8d2_e031_4517_ae28_69ce16cb6589",
        "ProductRelatedComponent": "0dSxx00000001p6EAA",
        "ProductRelationshipType": null,
        "AssociatedItemPricing": "NotIncludedInBundlePrice",
        "AssociatedQuantScaleMethod": "Proportional",
        "businessObjectType": "QuoteLineRelationship"
      }
    }
  ]
}
Publish the addedNodes to the Product Configurator with Lightning Message Service (LMS). From a custom Lightning Web Component (LWC) in your screen flow, publish a valueChanged event with the field set to addedNodes.
import MessageChannel from "@salesforce/messageChannel/lightning__productConfigurator_notification";

publish(createMessageContext(), MessageChannel, {
  action: "valueChanged",
  data: [{
    field: "addedNodes",
    addedNodes: this.addedNodes
  }]
});

The Product Configurator reads the field as STATE_FIELDS.ADDED_NODES and applies the nodes.

Save and activate the flow, and then copy the flow API name.
Create a product configuration flow and specify these:
For Flow Identifier, enter the flow API name that you copied in step 4.
Set the status as Active.
In the product configuration flow, create a new Product Configuration Flow Assignment for a product classification with these specifications:
Select the product classification that you want to assign to the product configuration flow.
Select the Assignment Type as Dynamic Addition Flow.

When sales reps dynamically add child components during bundle configurations, your custom screen flow opens for the product classifications you assigned the flow to.

=== ARTICLE: ind.product_configurator_set_up_advanced_configurator.htm ===
---
article_id: ind.product_configurator_set_up_advanced_configurator.htm
title: Enable Constraint Rules Engine and Create Transaction Processing Types
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_set_up_advanced_configurator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_constraints_engine.htm
fetched_at: 2026-09-04
---

# Enable Constraint Rules Engine and Create Transaction Processing Types

Enable rule designers to create advanced configuration rules and constraints, and help sales reps run the rules for quotes and orders.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER
PERMISSIONS NEEDED
To set up Constraint Rules Engine:	Product Configuration Constraints Designer permission set
NOTE

Constraint Rules Engine services aren’t available in Government Cloud or in orgs within the EU Operating Zone (OZ). For more information, contact your Salesforce account executive.

Enable Constraint Rules Engine

Grant users the access to set up product configuration rules by using Constraint Rules Engine.

From Setup, in the Quick find box, enter Revenue Settings, and then select Revenue Settings.
Turn on Set Up Configuration Rules and Constraints with Constraints Engine.
Create Transaction Processing Type Records for Constraint Rules Engine

Create a transaction processing type and specify AdvancedConfigurator as the rule engine.

See Define Rules Engine with Transaction Processing Types.

After you create a transaction processing type, set up context definitions.

=== ARTICLE: ind.product_configurator_set_up_business_rules_engine.htm ===
---
article_id: ind.product_configurator_set_up_business_rules_engine.htm
title: Set Up Business Rules Engine for Product Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_set_up_business_rules_engine.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_setup.htm
fetched_at: 2026-09-04
---

# Set Up Business Rules Engine for Product Configurator

Before you define product configuration rules by using Business Rules Engine, set up Business Rules Engine for Product Configurator.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To set up Business Rules Engine for Product Configurator:	Product Configuration Rules Designer permission set
Create a Rule Library

Rule creation requires a rule library to store and run rules in Business Rules Engine.

Before you create a rule library, select a default pricing procedure on the Revenue Settings page. This pricing procedure uses a context definition that's extended from the SalesTransactionContext context definition.

From the App Launcher, find and select Rule Libraries.
Click New.
Enter a name and API name for the rule library.
Select Configurator as the usage type.
Enter the developer name of the extended SalesTransactionContext context definition that's configured for your default pricing procedure on the Revenue Settings page.
Save your changes.
Go to the Rule Library Versions related list and open the version that you want to activate.
From the action dropdown, click Activate.
Refresh the page.
The rule library version is now activated.
NOTE If you change the extended SalesTransactionContext context definition used by your default pricing procedure, create a new rule library with the latest context definition, or create a rule library version.
Enable Configuration Rules with Business Rules Engine

Grant users the access to set up product configuration rules by using Business Rules Engine.

From Setup, in the Quick find box, enter Revenue Settings, and then select Revenue Settings.
Turn on Set Up Configuration Rules with Business Rules Engine.
Create Transaction Processing Type Records for Business Rules Engine

Create a transaction processing type and specify StandardConfigurator as the rule engine.

See Define Rules Engine with Transaction Processing Types.

This completes the setup of Business Rules Engine for Product Configurator. To learn about creating product configuration rules by using Business Rules Engine, see Define Configuration Rules with Business Rules Engine.

This completes the setup for Product Configurator. To proceed with the rest of the Revenue Cloud setup, see Set Up Revenue Management.

=== ARTICLE: ind.product_configurator_set_up_constraint_engine_context_definitions.htm ===
---
article_id: ind.product_configurator_set_up_constraint_engine_context_definitions.htm
title: Set Up Context Definitions
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_set_up_constraint_engine_context_definitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_constraints_engine.htm
fetched_at: 2026-09-04
---

# Set Up Context Definitions

Update the extended SalesTransactionContext context definition and set up a custom asset context definition.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Update the Extended SalesTransactionContext Context Definition

To use the custom ConstraintEngineNodeStatus field, update the extended SalesTransactionContext context definition ​that's configured for the default pricing procedure on the Revenue Settings page.

Add Attributes

Edit the extended SalesTransactionContext context definition and add these attributes.

ADD ATTRIBUTE TO	ATTRIBUTE NAME	TYPE	DATA TYPE
SalesTransactionItem node	ConstraintEngineNodeStatus	INPUTOUTPUT	STRING
AssetActionSource	AssetConstraintEngineNodeStatus	INPUTOUTPUT	STRING

See Edit Context Definitions and Add Attributes.

Map Attributes

If you're using Business Rules Engine and want to set up Constraint Rules Engine, or want to use both engines, the TransactionType attribute mapping switches between the rules engines at the transaction level.

Open the extended SalesTransactionContext context definition, go to the Map Data tab, and map the necessary attributes.

Before you map these attributes, turn on Transaction processing for quotes and orders on the Revenue Settings page.

MAPPING NAME	ATTRIBUTE	MAP TO
QuoteEntitiesMapping	ConstraintEngineNodeStatus	ConstraintEngineNodeStatus__c field on the QuoteLineItem object
QuoteEntitiesMapping	TransactionType on the SalesTransaction node	TransactionType field on the Quote object
OrderEntitiesMapping	ConstraintEngineNodeStatus	ConstraintEngineNodeStatus__c field on the OrderItem object
OrderEntitiesMapping	TransactionType on the SalesTransaction node	TransactionType field on the Order object
AssetEntitiesMapping	AssetConstraintEngineNodeStatus	ConstraintEngineNodeStatus__c field on the AssetActionSource object

Then, edit AssetToSalesTransactionMapping. Select the data source as Context Definition, select your extended Sales Transaction context definition, and find the SalesTransactionItem node listed. Then, map the AssetConstraintEngineNodeStatus attribute to the ConstraintEngineNodeStatus__c field on the SalesTransactionItem node.

See Add Context Mapping.

Activate Context Definition

Activate the updated SalesTransactionContext context definition.

See Activate a Context Definition.

Set Up Custom Asset Context Definition

Set up an asset context definition to get asset data based on the selected context. Use this asset data when you configure asset-based rules and constraints in the CML Editor, and apply other filters on the data as needed.

An asset context is required to create asset-based configuration rules and constraints. If you don't define one, Constraint Rules Engine doesn't fetch any asset data.

NOTE You can set up a custom asset context definition only from Summer ’25 and onwards.
Create Custom Asset Context Definitions

To fetch assets for a specific account, product, or a custom or standard field of the asset, define a custom asset context definition.

Extend the standard AssetContext__stdctx context definition.
Customize the mappings according to your requirements.

See Extend a Context Definition and Edit Context Definitions.

Select an Asset Context for Constraint Rules Engine

Select the asset context for Constraint Rules Engine to apply asset-based configuration rules and constraints.

NOTE Select an asset context for Product Configurator only if your constraint model uses assets.
From Setup, in the Quick find box, enter Revenue Settings, and then select Revenue Settings.
In the Set Up Asset Context for Product Configurator section, select the asset context definition that you want to use.

After you select the asset context definition, filter the asset data directly in the CML Editor based on your requirements when you define configuration rules and constraints.

To learn about creating rules and constraints by using Constraint Rules Engine, see Use Constraint Builder With Constraint Rules Engine.

=== ARTICLE: ind.product_configurator_set_up_constraint_engine_prerequisites.htm ===
---
article_id: ind.product_configurator_set_up_constraint_engine_prerequisites.htm
title: Create Custom Field and Define Apex Triggers
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_set_up_constraint_engine_prerequisites.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_set_up_constraints_engine.htm
fetched_at: 2026-09-04
---

# Create Custom Field and Define Apex Triggers

Create the necessary custom fields and define Apex triggers on the Quote Line Item and Order Product (OrderItem) objects.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
Create the ConstraintEngineNodeStatus Custom Field

Create a custom field on the Quote Line Item, Order Product, and Asset Action Source objects to store data that Constraint Rules Engine uses for internal processing.

Go to the object management settings of these objects, and create a custom field with these values:

Select Text Area (Long) as the data type.
Enter Constraint Engine Node Status as the field label.
Enter 131072 as the length.
Enter ConstraintEngineNodeStatus as the field name.
Select Visible access and deselect Read-Only access for the profiles of the users who'll use Constraint Rules Engine, and Customer Community and Partner Community users.
Deselect the page layouts.

See Create a Custom Field.

Define Apex Triggers for Quote and Order Line Items

Define triggers for the Quote Line Item and Order Product (OrderItem) objects by using Apex code.

Use this Apex code for the Quote Line Item object.

trigger QuoteItemTrigger on QuoteLineItem (before insert) {
   //collect QuoteActionIds 
   Set<Id> quoteActionIds = new Set<Id>();
   
   for (QuoteLineItem qi : Trigger.new) {
   if (qi.QuoteActionId != null && qi.ConstraintEngineNodeStatus__c == null) {
   quoteActionIds.add(qi.QuoteActionId);
   }
   }
   
   if (!quoteActionIds.isEmpty()) {
   // Step 1: Get QuoteAction → SourceAsset
   Map<Id, Id> quoteActionToAssetId = new Map<Id, Id>();
   for (QuoteAction qAction : [
   SELECT Id, SourceAssetId 
   FROM QuoteAction 
   WHERE SourceAssetId != null 
   AND Id IN :quoteActionIds
   ]) {
   quoteActionToAssetId.put(qAction.Id, qAction.SourceAssetId);
   }
   
   // Step 2: Get AssetActions
   List<AssetAction> assetActions = [
   SELECT Id, AssetId, ActionDate 
   FROM AssetAction 
   WHERE AssetId IN :quoteActionToAssetId.values()
   ];
   
   // Step 3: Get latest AssetAction per Asset
   Map<Id, AssetAction> assetIdToLatestAction = new Map<Id, AssetAction>();
   for (AssetAction aAction : assetActions) {
   AssetAction existing = assetIdToLatestAction.get(aAction.AssetId);
   if (existing == null || aAction.ActionDate > existing.ActionDate) {
   assetIdToLatestAction.put(aAction.AssetId, aAction);
   }
   }
   
   // Step 4: Get related AssetActionSource records
   Map<Id, Id> assetIdToActionId = new Map<Id, Id>();
   for (Id assetId : assetIdToLatestAction.keySet()) {
   assetIdToActionId.put(assetId, assetIdToLatestAction.get(assetId).Id);
   }
   
   List<AssetActionSource> assetActionSources = [
   SELECT ConstraintEngineNodeStatus__c, AssetAction.AssetId 
   FROM AssetActionSource 
   WHERE AssetActionId IN :assetIdToActionId.values() ORDER BY CreatedDate DESC
   ];
   // Step 5: Map AssetId → Status
   Map<Id, String> assetIdToStatus = new Map<Id, String>();
   for (AssetActionSource actionSource : assetActionSources) {
   if (!assetIdToStatus.containsKey(actionSource.AssetAction.AssetId) && 
   actionSource.ConstraintEngineNodeStatus__c != null) {
   assetIdToStatus.put(
   actionSource.AssetAction.AssetId, 
   actionSource.ConstraintEngineNodeStatus__c
   );
   }
   }
   List<QuoteLineItem> toUpdate = new List<QuoteLineItem>();
   // Step 6: Set ConstraintEngineNodeStatus__c directly on Trigger.new records
   for (QuoteLineItem qi : Trigger.new) {            
   if (qi.QuoteActionId != null && qi.ConstraintEngineNodeStatus__c == null) {
   Id assetId = quoteActionToAssetId != null ? quoteActionToAssetId.get(qi.QuoteActionId) : null;
   if (assetId != null && assetIdToStatus != null) {
   String status = assetIdToStatus.get(assetId);
   if (status != null) {
   qi.ConstraintEngineNodeStatus__c = status;
   }
   }
   }
   }
   }
   }

Use this Apex code for the Order Product (OrderItem) object.

trigger OrderItemTrigger on OrderItem  (before insert) {
  //collect orderActionIds
  Set<Id> orderActionIds = new Set<Id>();
 
  for (OrderItem oi : Trigger.new) {
  if (oi.OrderActionId != null && oi.ConstraintEngineNodeStatus__c == null) {
  orderActionIds.add(oi.OrderActionId);
  }
  }
 
  if (!orderActionIds.isEmpty()) {
  // Step 1: Get OrderAction → SourceAsset
  Map<Id, Id> orderActionToAssetId = new Map<Id, Id>();
  for (OrderAction oAction : [
  SELECT Id, SourceAssetId
  FROM OrderAction
  WHERE SourceAssetId != null
  AND Id IN :orderActionIds
  ]) {
  orderActionToAssetId.put(oAction.Id, oAction.SourceAssetId);
  }
 
  // Step 2: Get AssetActions
  List<AssetAction> assetActions = [
  SELECT Id, AssetId, ActionDate
  FROM AssetAction
  WHERE AssetId IN :orderActionToAssetId.values()
  ];
 
  // Step 3: Get latest AssetAction per Asset
  Map<Id, AssetAction> assetIdToLatestAction = new Map<Id, AssetAction>();
  for (AssetAction aAction : assetActions) {
  AssetAction existing = assetIdToLatestAction.get(aAction.AssetId);
  if (existing == null || aAction.ActionDate > existing.ActionDate) {
  assetIdToLatestAction.put(aAction.AssetId, aAction);
  }
  }
 
  // Step 4: Get related AssetActionSource records
  Map<Id, Id> assetIdToActionId = new Map<Id, Id>();
  for (Id assetId : assetIdToLatestAction.keySet()) {
  assetIdToActionId.put(assetId, assetIdToLatestAction.get(assetId).Id);
  }
 
  List<AssetActionSource> assetActionSources = [
  SELECT ConstraintEngineNodeStatus__c, AssetAction.AssetId
  FROM AssetActionSource
  WHERE AssetActionId IN :assetIdToActionId.values() ORDER BY CreatedDate DESC
  ];
  // Step 5: Map AssetId → Status
  Map<Id, String> assetIdToStatus = new Map<Id, String>();
  for (AssetActionSource actionSource : assetActionSources) {
  if (!assetIdToStatus.containsKey(actionSource.AssetAction.AssetId) &&
  actionSource.ConstraintEngineNodeStatus__c != null) {
  assetIdToStatus.put(
  actionSource.AssetAction.AssetId,
  actionSource.ConstraintEngineNodeStatus__c
  );
  }
  }
  List<OrderItem> toUpdate = new List<OrderItem>();
  // Step 6: Set ConstraintEngineNodeStatus__c directly on Trigger.new records
  for (OrderItem oi : Trigger.new) {           
  if (oi.OrderActionId != null && oi.ConstraintEngineNodeStatus__c == null) {
  Id assetId = orderActionToAssetId != null ? orderActionToAssetId.get(oi.OrderActionId) : null;
  if (assetId != null && assetIdToStatus != null) {
  String status = assetIdToStatus.get(assetId);
  if (status != null) {
  oi.ConstraintEngineNodeStatus__c = status;
  }
  }
  }
  }
  }
  }


See Define Apex Triggers.

After you define the Apex triggers, set up constraint rules engine.

=== ARTICLE: ind.product_configurator_set_up_constraints_engine.htm ===
---
article_id: ind.product_configurator_set_up_constraints_engine.htm
title: Set Up Constraint Rules Engine for Product Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_set_up_constraints_engine.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_setup.htm
fetched_at: 2026-09-04
---

# Set Up Constraint Rules Engine for Product Configurator

Before you define product configuration rules and constraints by using Constraint Rules Engine, set up Constraint Rules Engine for Product Configurator.

NOTE

Constraint Rules Engine services aren’t available in Government Cloud or in orgs within the EU Operating Zone (OZ). For more information, contact your Salesforce account executive.

Create Custom Field and Define Apex Triggers
Create the necessary custom fields and define Apex triggers on the Quote Line Item and Order Product (OrderItem) objects.
Enable Constraint Rules Engine and Create Transaction Processing Types
Enable rule designers to create advanced configuration rules and constraints, and help sales reps run the rules for quotes and orders.
Set Up Context Definitions
Update the extended SalesTransactionContext context definition and set up a custom asset context definition.

=== ARTICLE: ind.product_configurator_set_up_flow.htm ===
---
article_id: ind.product_configurator_set_up_flow.htm
title: Set Up Your Product Configuration Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_set_up_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_explore_the_product_configurator_flow.htm
fetched_at: 2026-09-04
---

# Set Up Your Product Configuration Flow

Clone the Default Product Configurator Flow and customize it according to your business needs to manage the Product Configurator interface layout and the product information shown on it. Maintain your customized configuration flows and update them with the latest attributes to make sure new features work as expected, and you retain a smooth configuration experience.

Clone and Customize the Default Product Configurator Flow
Use the Default Product Configurator Flow as a template to design a product configurator flow that determines the layout for presenting customizable product-related information in the user interface.
Configure Editable Context Fields for Product Option Cards
Enable sales reps to edit context fields directly from the product option cards during bundle configurations. Context fields are derived from the configured context definition and differ from product attribute fields.
Configure Attribute Display on Product Option Cards
Show product attributes on the product option cards, where sales reps can edit them during bundle configurations.
Make Product Names Editable in Product Option Cards
Give sales reps access to edit product names from the product option cards during bundle configurations.
Select Context Attributes to Improve Configurator Performance
Select specific context attributes that you want the Configuration API to query and return, instead of it returning all of them by default. Your selection narrows the query and the response to the data that your configurations need, so Product Configurator responds faster, even for large transactions.
Enable Non-Blocking Behavior in the Configurator
Enable non-blocking behavior so that configurator users can change multiple attribute and option values on a product asynchronously. The configuration page loads the changes without waiting for the constraint engine to process each setting individually. After processing is complete, the user can save the configuration.

=== ARTICLE: ind.product_configurator_set_up_translation_labels.htm ===
---
article_id: ind.product_configurator_set_up_translation_labels.htm
title: Set Up Custom Labels for Run-Time Message Translation
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_set_up_translation_labels.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_create_a_constraint_model.htm
fetched_at: 2026-09-04
---

# Set Up Custom Labels for Run-Time Message Translation

Enable translations for run-time messages defined in your constraint model by creating unique, translatable custom labels for the messages. The labels you set up replace the original static message text in the CML to facilitate translation. During run time, the messages appear in different languages, based on the sales reps’ locale and the translation settings of their Salesforce org. With this support, sales reps can see important configuration information in their local languages, which accelerates troubleshooting and improves usability.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create or edit a constraint model:	Product Configuration Constraints Designer permission set
To create and manage custom labels:	Customize Application

Before creating custom labels:

Enable translations in your org by enabling Translation Workbench and adding the languages for which you want to support translations.
Save your constraint model with the messages you want to translate. The Add Labels button is enabled only after you save your model. All the run-time messages defined in your saved constraint model are extracted and listed for custom label definition.
From the App Launcher, find and select Constraint Models.
From the constraint models list view page, click the model you want to add custom labels for.
In the constraint model details page, select the version of the model you want to open.
On the Constraint Builder, click Add Labels.
In the Add Translation Labels for Messages window, specify a unique custom label for each message that you want to translate.
Messages that don’t have a custom label associated with them aren’t translated to the user’s chosen language during run time.
Custom labels must start with a letter and contain only alphanumeric characters and underscores. Labels are case-insensitive.

The custom labels that you assign to the messages replace the message text in your CML code. Manage all future changes to these labels from the Custom Labels page in Setup. See Custom Labels.

Reuse Existing Custom Labels

If you have existing custom labels that you want to reuse in your constraint model, add the label reference by using the type-ahead functionality or by providing the full label syntax in the CML Editor or Visual Builder.

In the Visual Builder, search for and select the custom label from the Run-time Message field on the constraint components.
In the CML Editor, use the $Label.labelName syntax to reference a custom label in your CML code.

=== ARTICLE: ind.product_configurator_setup.htm ===
---
article_id: ind.product_configurator_setup.htm
title: Set Up Product Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_introduction.htm
fetched_at: 2026-09-04
---

# Set Up Product Configurator

Product Configurator provides a framework to define and apply rules and constraints when configuring products. It features two rules engines: Constraint Rules Engine and Business Rules Engine.

Use Product Configurator with Constraint Rules Engine for large and complex product configuration rules and constraints.
Use Product Configurator with Business Rules Engine for simple product configuration rules.
NOTE

Constraint Rules Engine services aren’t available in Government Cloud or in orgs within the EU Operating Zone (OZ). For more information, contact your Salesforce account executive.

Set Up Constraint Rules Engine for Product Configurator
Before you define product configuration rules and constraints by using Constraint Rules Engine, set up Constraint Rules Engine for Product Configurator.
Set Up Business Rules Engine for Product Configurator
Before you define product configuration rules by using Business Rules Engine, set up Business Rules Engine for Product Configurator.
Define Rules Engine with Transaction Processing Types
Create Transaction Processing Type records to define the rules engine that you want to use to process configuration rules. Then, specify the default transaction processing type on the Revenue Settings page.

=== ARTICLE: ind.product_configurator_specify_which_rule_engine_to_use.htm ===
---
article_id: ind.product_configurator_specify_which_rule_engine_to_use.htm
title: Define Rules Engine with Transaction Processing Types
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_specify_which_rule_engine_to_use.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_setup.htm
fetched_at: 2026-09-04
---

# Define Rules Engine with Transaction Processing Types

Create Transaction Processing Type records to define the rules engine that you want to use to process configuration rules. Then, specify the default transaction processing type on the Revenue Settings page.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
NOTE

Constraint Rules Engine services aren’t available in Government Cloud or in orgs within the EU Operating Zone (OZ). For more information, contact your Salesforce account executive.

Configure the transaction processing type with the appropriate RuleEngine value:

To use Business Rules Engine, specify StandardConfigurator as the RuleEngine value.
To use Constraint Rules Engine, specify AdvancedConfigurator as the RuleEngine value.

Sales reps can’t see the fields in Transaction Processing Type records. If necessary, append the name of the rules engine to the Transaction Processing Type record name.

Set the default transaction processing type only if you plan to use Business Rules Engine. When you enable Constraint Rules Engine, AdvancedConfigurator automatically becomes the default rules engine.

When users create quotes and orders, the Transaction Type field is automatically populated with the default Transaction Processing Type record. The Transaction Type field on a quote or order determines the rule engines that's used to validate product configurations, and to execute configuration rules and constraints.

ENABLED FEATURE	RULES ENGINE USED	CONDITIONS
Only Constraint Rules Engine is enabled	Constraint Rules Engine	Configuration rules are run by using Constraint Rules Engine.
Only Business Rules Engine is enabled	Business Rules Engine	StandardConfigurator is specified as the rule engine in the associated Transaction Processing Type record.
Only Business Rules Engine is enabled	No rules engine used	There's no Transaction Type value on quotes and orders, or no Rule Engine value on the Transaction Processing Type record.
Both rules engines are enabled	Business Rules Engine	StandardConfigurator is specified as the rule engine in the associated Transaction Processing Type record.
Both rules engines are enabled	Constraint Rules Engine	StandardConfigurator is not specified as the rule engine in the associated Transaction Processing Type record.

=== ARTICLE: ind.product_configurator_sync_cml_and_pcm.htm ===
---
article_id: ind.product_configurator_sync_cml_and_pcm.htm
title: Sync Constraint Models with Product Definitions
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_sync_cml_and_pcm.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_advanced.htm
fetched_at: 2026-09-04
---

# Sync Constraint Models with Product Definitions

Sync product definition changes from Product Catalog Management (PCM) to the constraint modeling language (CML) for a constraint model, to make sure that the CML reflects the latest product definition.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

In Constraint Builder, use the Sync button to update the product’s CML. Syncing updates data for product components, attributes, and attribute values. This table shows configuration changes in PCM and the result in the constraint model CML when you sync the changes.

CHANGE IN PRODUCT CATALOG MANAGEMENT	RESULT IN CONSTRAINT MODEL CML
Product Component Changes	 
Delete a child product from a bundle	Relation and associations for the relation for the child product are removed from the bundle
Change product cardinality	Cardinality for the product is changed
Set product as required	Cardinality for the product is updated
Attribute Changes	 
Delete a product attribute	Attribute variable is removed
Set attribute to inactive	Attribute variable is removed from the attribute domain
Attribute Value Changes	 
Delete attribute value	Attribute value is removed
Create attribute value	Attribute value is added to the attribute domain
Update default attribute value	If the default value annotation exists in the CML, the default value is updated
Set attribute value to inactive	Attribute value is removed from the attribute domain
Default attribute value added	Default attribute value is added to the attribute domain.
Default attribute value removed	Default attribute is removed from the attribute domain

These changes in PCM don’t sync to the constraint model CML.

Constraint, require, or exclude keywords that contain outdated attribute or product usage
An attribute inside a parent type
Relations inside a virtual container
Product component groups
A product added to or removed from a product class
Changes to attributes or attribute values defined under a product class
Product context tags and their values
Newly added components or attributes

=== ARTICLE: ind.product_configurator_third_party_configurator.htm ===
---
article_id: ind.product_configurator_third_party_configurator.htm
title: Third-Party Configurator
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_third_party_configurator.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_introduction.htm
fetched_at: 2026-09-04
---

# Third-Party Configurator

Revenue Management (formerly Revenue Cloud) provides extensibility options to third-party users seeking to build integrations with the Revenue Management product. Revenue Management supports various third-party use cases. The support includes replacing the first-party configurator with the third-party configurator, integrating third-party UI components into the first-party configurator, and creating custom configurator UI using headless configurator APIs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Product catalog admin uses the product configuration flows to link different configurators (first-party or third-party) to specific products and product classifications. By integrating third-party configurators, the product catalog admins can determine the appropriate configurator for each product, whether it's a first-party or a specialized third-party configurator. The product catalog admin can set the third-party configurator as the default configurator for all the products.

EXAMPLE

Within the same organization, a Product Catalog admin can make these assignments:

Assign the Laptop Pro Bundle product to use the ABC third-party configurator.
Assign the Excavator 3000 product to use the xyz third-party three-dimensional configurator.
Set all products in the Cellphone product classification to use a customized lightning flow configurator, based on the standard Revenue Management configurator components.
All other products to use the first-party configurator.
Create a Third-Party Configurator UI Component
Create a Lighting web component (LWC) to use as a custom third-party configurator UI component and add the custom component to the product configuration flow.
Third-Party Configurator UI Component Files
A Lightning web component that renders UI must include an HTML file, a JavaScript file, and a metadata configuration file.
Third-Party Configurator Lightning Flows
Third-party users can build a third-party configurator as a replacement to the first-party configurator using the screen-based lightning flows. The screen-based lightning flow is either included in the managed package or custom built in the org.
Third-Party Configurator UI Component Integration into First-Party Configurator
As a third-party user, apart from replacing the first-party configurator, you can also create a custom Lightning Flow UI configurator component and integrate the UI component to the first-party configurator UI. This approach provides a functional enhancement to the existing first-party configurator UI.
Custom Configurator Development with First-Party Configurator APIs
As a third-party user, build a custom configurator UI by using the public Configurator APIs. Incorporate the existing first-party configurator UI components for a familiar look and feel, and deliver a personalized experience by using the configurator API functionalities.
Use Third-Party Configurator for Specific Products or Classifications
Configure product or classifications by using the third-party configurator instead of the default configurator.
Use Place Sales Transaction API for Data Transfer
Transfer data from a custom configurator to a quote or order in Revenue Management by using the Place Sales Transaction API.
Data Types for Configurator User Interface
The Apex classes contain data accessible through the user interface. The Configurator’s Data Manager acts as the primary user interface component that exports data to other components. As a third-party user you can pass the data into your own user interface component without the need for separate queries to fetch data.

=== ARTICLE: ind.product_configurator_third_party_configurator_lightning_flows.htm ===
---
article_id: ind.product_configurator_third_party_configurator_lightning_flows.htm
title: Third-Party Configurator Lightning Flows
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_third_party_configurator_lightning_flows.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator.htm
fetched_at: 2026-09-04
---

# Third-Party Configurator Lightning Flows

Third-party users can build a third-party configurator as a replacement to the first-party configurator using the screen-based lightning flows. The screen-based lightning flow is either included in the managed package or custom built in the org.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Both first-party and third-party configurators receive the same data when the screen-based Lightning Flow launches during a configuration process.

"configuratorContext": {
"transactionId": <the quote/order ID being configured>,
"transactionLineId": <the quote/order item ID being configured>,
"parentName": <the quote/order name>,
"origin": <"Quote" | "Order">,
"addedNodes": [{
"id": <a synthetic quote/order item Id>,
"pricebookEntry": <Pricebook Entry Id>,
"productSellingModel": <Product Selling Model Id>,
"unitPrice": <Unit Price>,
"quantity": <Quantity>,
"product": <Product2 Id>,
"businessObjectType": <QuoteLineItem or OrderItem>
}]
}


When the screen-based Lightning Flow built with the required data format, the screen-based Lightning Flow can be assigned to specific products, product classifications, or even entire organizations, where it functions as the designated configurator.

Third-party configurators offer greater flexibility. Third-party configurators can have their own solutions from scratch, bypassing features like Salesforce Pricing, Context Service, Configurator API, and Business Rules Engine. Third-party configurators can use any Salesforce APIs that are required. There’s no obligation to use any of the Revenue Management specific APIs.

SEE ALSO
Define Product Configuration Flows

=== ARTICLE: ind.product_configurator_third_party_configurator_ui_component_create.htm ===
---
article_id: ind.product_configurator_third_party_configurator_ui_component_create.htm
title: Create a Third-Party Configurator UI Component
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_third_party_configurator_ui_component_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator.htm
fetched_at: 2026-09-04
---

# Create a Third-Party Configurator UI Component

Create a Lighting web component (LWC) to use as a custom third-party configurator UI component and add the custom component to the product configuration flow.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To add a custom component to a product configuration flow	Product Configurator
Use Salesforce Developer Experience (Salesforce DX) to create an LWC to use as a custom UI component. See Create Lightning Web Components.
To add the custom component to the product configuration flow and define the logic for sending and receiving data, in the custom component folder add the required HTML, JavaScript, and js-meta.xml files.
To enable the custom component to communicate with the Data Manager component in the product configuration flow, trigger Lightning Message Service (LMS) events. Make sure that the custom component doesn't directly call the configurator API or any Save APIs. See Communicate Across the DOM with Lightning Message Service.
In Flow Builder, drag the custom component from the sidebar to the Product Configurator Flow layout. See Flow Builder Tour.
In the Flow Builder sidebar, open the Data Manager component to view the available outputs, and then link the appropriate data manager outputs to the custom component.
SEE ALSO
Third-Party Configurator UI Component HTML File
Third-Party Configurator UI Component JavaScript File
Third-Party Configurator UI Component Metadata Configuration File

=== ARTICLE: ind.product_configurator_third_party_configurator_ui_component_files.htm ===
---
article_id: ind.product_configurator_third_party_configurator_ui_component_files.htm
title: Third-Party Configurator UI Component Files
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_third_party_configurator_ui_component_files.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator.htm
fetched_at: 2026-09-04
---

# Third-Party Configurator UI Component Files

A Lightning web component that renders UI must include an HTML file, a JavaScript file, and a metadata configuration file.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Developer, Enterprise, and Unlimited Editions of Revenue Management where Product Configurator is enabled
Third-Party Configurator UI Component HTML File
Every UI Lightning web component (LWC) has an HTML file with the root tag <template>. The HTML file follows the naming convention componentName.html, for example, myComponent.html.
Third-Party Configurator UI Component JavaScript File
Every component has a JavaScript file. For the third-party configurator UI component, this file contains all the logic for sending and receiving data and interacting with the configurator.
Third-Party Configurator UI Component Metadata Configuration File
The configuration file defines the metadata values for the component, including supported targets and the design configuration.

=== ARTICLE: ind.product_configurator_third_party_configurator_ui_component_html_file.htm ===
---
article_id: ind.product_configurator_third_party_configurator_ui_component_html_file.htm
title: Third-Party Configurator UI Component HTML File
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_third_party_configurator_ui_component_html_file.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator_ui_component_files.htm
fetched_at: 2026-09-04
---

# Third-Party Configurator UI Component HTML File

Every UI Lightning web component (LWC) has an HTML file with the root tag <template>. The HTML file follows the naming convention componentName.html, for example, myComponent.html.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

This example shows the basic structure for an HTML file for a component.

<template>
  <p>My third party configurator flow component</p>
</template>
SEE ALSO
Create a Third-Party Configurator UI Component

=== ARTICLE: ind.product_configurator_third_party_configurator_ui_component_javascript_file.htm ===
---
article_id: ind.product_configurator_third_party_configurator_ui_component_javascript_file.htm
title: Third-Party Configurator UI Component JavaScript File
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_third_party_configurator_ui_component_javascript_file.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator_ui_component_files.htm
fetched_at: 2026-09-04
---

# Third-Party Configurator UI Component JavaScript File

Every component has a JavaScript file. For the third-party configurator UI component, this file contains all the logic for sending and receiving data and interacting with the configurator.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

This JavaScript example uses Lightning Message Service events to send and receive data.

import {api, LightningElement} from 'lwc';

import {MessageContext, publish} from 'lightning/messageService';

import CONFIGR_CHANNEL from "@salesforce/messageChannel/lightning__productConfigurator_notification";

const LMS_EVENTS = Object.freeze({
    VALUE_CHANGE: "valueChanged",
    NAVIGATE: "navigate",
    CLOSE_PREVIEW: "closePreview",
    TOGGLE_INSTANT_PRICING: "toggleInstantPricing",
    TOGGLE_RULES_VALIDATION: "toggleRulesValidation",
    TOGGLE_COMPACT_LAYOUT: "toggleCompactLayout",
    UPDATE_PRICES: "updatePrices",
    VALIDATE_PRODUCT: "validateProduct",
    CLONE_ITEMS: "cloneItems",
});

export const STATE_FIELDS = Object.freeze({
    IS_SELECTED: "isSelected",
    QUANTITY: "Quantity",
    ATTRIBUTE_FIELD: "AttributeField",
    PRODUCT_SELLING_MODEL: "ProductSellingModel",
    PRICING_TERM_UNIT: "PricingTermUnit",
    SUBSCRIPTION_TERM: "SubscriptionTerm",
    SELLING_MODEL_TYPE: "SellingModelType",
    PRICE_BOOK_ENTRY: "PricebookEntry",
    IS_DELETED: "Deleted",
    UNIT_PRICE: "UnitPrice",
    CUSTOM_PRODUCT_NAME: "CustomProductName"
});

export default class MyComponent extends LightningElement {
    
    @api transactionId;
    @api transactionLineId;
    @api currentTransactionLineId;
    @api parentName;
    @api origin;
    @api messages;
    @api header;
    @api optionGroups;
    @api summary;
    @api navigationRoute;
    @api searchInfo;
    @api currencyCode;
    @api transactionRecord;
    @api headerTitle;
    @api isDesignTime;
    // ... do @api annotations for each of the input properties you want from
    // Data Manager
    
    subscription = null; // Stores the subscription to the message service
    
    // Lifecycle hook that subscribes to the message channel when the component is initialized
    connectedCallback() {
       this.subscribeToMessageChannel();
    }

    // Subscribes to the Lightning Message Service channel to receive message
    subscribeToMessageChannel() {
       if (!this.subscription) {
           this.subscription = subscribe(
               this.messageContext,
               CONFIGR_CHANNEL,
               (message) => this.handleMessage(message)
           );
       }
    }
    
    handleMessage(message) {}
    
    // Send the message to LMS
    sendMessageToDataManager() {
        const bulkMessagePayload = {
            action: LMS_EVENTS.VALUE_CHANGE,
            data: [
                // Change 1: update the root product's quantity field
                {
                    key: ["0QLxx0000004jGGGAY"],
                    field: STATE_FIELDS.QUANTITY,
                    value: 100
                },
                // Change 2: update the root product's attribute
                {
                    key: ["0QLxx0000004jGGGAY"],
                    field: STATE_FIELDS.ATTRIBUTE_FIELD,
                    attributeId: "0tjxx0000000001AAA",
                    value: "New Value"
                },
                // Change 3: update another one of root product's attributes
                {
                    key: ["0QLxx0000004jGGGAY"],
                    field: STATE_FIELDS.ATTRIBUTE_FIELD,
                    attributeId: "0tjxx0000000001AAB",
                    value: "0xxxx0000000001AAB"
                },
                // Change 4: create a picklist attribute that does not exist (non-defaulted picklist)
                {
                    key: ["0QLxx0000004jGGGAY"],
                    field: STATE_FIELDS.ATTRIBUTE_FIELD,
                    attributeId: "0tjxx0000000001AAC",
                    value: "0xxxx0000000001AAB"
                },
                // Change 5: select a static child product
                {
                    key: ["0QLxx0000004jGGGAY"],
                    productRelatedComponentId: '0dSxx00000000XtEAI', // the static child PRC to select
                    field: STATE_FIELDS.IS_SELECTED,
                    value: true
                },
                // Change 6: select a dynamic option with a child option below it
                {
                    field: STATE_FIELDS.IS_SELECTED,
                    selectedDynamicOptions: dynamicOptionsForInputPayload,
                    productRelatedComponent: prcForInputPayload
                },
                // Change 7: change the PSM for the root product from onetime to termed
                {
                    key: ["0QLxx0000004jGGGAY"],
                    field: STATE_FIELDS.PRODUCT_SELLING_MODEL,
                    value: {
                        psmId: "0jPxx00000002JZEAX",
                        pbeId: "01uxx000000A0tKAAX"
                    }
                },
                // Change 8: deselect a child static option
                {
                    key: ["0QLxx0000004jGGGAY", '0QLxx0000004jGHGAY'],
                    field: STATE_FIELDS.IS_SELECTED,
                    value: false
                }
            ]
        };

        publish(MessageContext, CONFIGR_CHANNEL, bulkMessagePayload);
    }
}


Lightning Message Service for Third-Party Configurator UI Components
Use Lightning Message Service (LMS) events to enable a third-party component to communicate with the Data Manager component in the product configurator flow. Add LMS events to the JavaScript file for the component to send and receive data.
SEE ALSO
Create a Third-Party Configurator UI Component

=== ARTICLE: ind.product_configurator_third_party_configurator_ui_component_lightning_message_service.htm ===
---
article_id: ind.product_configurator_third_party_configurator_ui_component_lightning_message_service.htm
title: Lightning Message Service for Third-Party Configurator UI Components
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_third_party_configurator_ui_component_lightning_message_service.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator_ui_component_javascript_file.htm
fetched_at: 2026-09-04
---

# Lightning Message Service for Third-Party Configurator UI Components

Use Lightning Message Service (LMS) events to enable a third-party component to communicate with the Data Manager component in the product configurator flow. Add LMS events to the JavaScript file for the component to send and receive data.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

This example shows available LMS events.

export const LMS_EVENTS = Object.freeze({
    VALUE_CHANGE: "valueChanged",
    NAVIGATE: "navigate",
    CLOSE_PREVIEW: "closePreview",
    TOGGLE_INSTANT_PRICING: "toggleInstantPricing",
    TOGGLE_RULES_VALIDATION: "toggleRulesValidation",
    TOGGLE_COMPACT_LAYOUT: "toggleCompactLayout",
    UPDATE_PRICES: "updatePrices",
    VALIDATE_PRODUCT: "validateProduct",
    CLONE_ITEMS: "cloneItems",
});

You can use LMS events to update a specific set of supported fields on a sales transaction item, including selection, quantity, attribute, pricing, and promotion fields. Each field must be set up as editable. An LMS event can't update a read-only field or a field outside the supported set.

NOTE To update a field that isn't in the supported set, use a flow, formula field, or trigger as a workaround.

To update a field, pass in the attribute name of the field and the new value, as shown here.

{
key: ["0QLxx0000004jGGGAY"],
field: "SalesTrxnItemDescription"
value: "Updated description"
}

This example shows the supported modifiable fields.

export const STATE_FIELDS = Object.freeze({
    IS_SELECTED: "isSelected",
    QUANTITY: "Quantity",
    ATTRIBUTE_FIELD: "AttributeField",
    PRODUCT_SELLING_MODEL: "ProductSellingModel",
    PRICING_TERM_UNIT: "PricingTermUnit",
    SUBSCRIPTION_TERM: "SubscriptionTerm",
    SELLING_MODEL_TYPE: "SellingModelType",
    PRICE_BOOK_ENTRY: "PricebookEntry",
    IS_DELETED: "Deleted",
    UNIT_PRICE: "UnitPrice",
    CUSTOM_PRODUCT_NAME: "CustomProductName",
    ADDED_NODES: "<TBD>",
    PROMOTION_ADD: "<TBD>",
    PROMOTION_REMOVE: "<TBD>",
    CONTEXT_FIELDS: "<TBD>",
});

This example shows the payload for the valueChanged event.

NOTE For custom fields, use this payload format in place of the standard format:
{
action: LMS_EVENTS.VALUE_CHANGE,
data: [
{
key: ["<id>"],
values: [
{
field: <field api name>,
value: <value>,
}
]
}
]
}
const bulkMessagePayload = {
    action: LMS_EVENTS.VALUE_CHANGE,
    data: [
        // Change 1: update the root product's quantity field
        {
            key: ["0QLxx0000004jGGGAY"],
            field: STATE_FIELDS.QUANTITY,
            value: 100
        },
        // Change 2: update the root product's attribute
        {
            key: ["0QLxx0000004jGGGAY"],
            field: STATE_FIELDS.ATTRIBUTE_FIELD,
            attributeId: "0tjxx0000000001AAA",
            value: "New Value"
        },
        // Change 3: update another one of root product's attributes
        {
            key: ["0QLxx0000004jGGGAY"],
            field: STATE_FIELDS.ATTRIBUTE_FIELD,
            attributeId: "0tjxx0000000001AAB",
            value: "0xxxx0000000001AAB"
        },
        // Change 4: create a picklist attribute that does not exist (non-defaulted picklist)
        {
            key: ["0QLxx0000004jGGGAY"],
            field: STATE_FIELDS.ATTRIBUTE_FIELD,
            attributeId: "0tjxx0000000001AAC",
            value: "0xxxx0000000001AAB"
        },
        // Change 5: select a static child product
        {
            key: ["0QLxx0000004jGGGAY"],
            productRelatedComponentId: '0dSxx00000000XtEAI', // the static child PRC to select
            field: STATE_FIELDS.IS_SELECTED,
            value: true
        },
        // Change 6: select a dynamic option with a child option below it
        {
            field: STATE_FIELDS.IS_SELECTED,
            selectedDynamicOptions: dynamicOptionsForInputPayload,
            productRelatedComponent: prcForInputPayload
        },
        // Change 7: change the PSM for the root product from onetime to termed
        {
            key: ["0QLxx0000004jGGGAY"],
            field: STATE_FIELDS.PRODUCT_SELLING_MODEL,
            value: {
                psmId: "0jPxx00000002JZEAX",
                pbeId: "01uxx000000A0tKAAX"
            }
        },
        // Change 8: deselect a child static option
        {
            key: ["0QLxx0000004jGGGAY", '0QLxx0000004jGHGAY'],
            field: STATE_FIELDS.IS_SELECTED,
            value: false
        }
    ]
};

publish(MessageContext, MessageChannel, bulkMessagePayload);

=== ARTICLE: ind.product_configurator_third_party_configurator_ui_component_metadata_file.htm ===
---
article_id: ind.product_configurator_third_party_configurator_ui_component_metadata_file.htm
title: Third-Party Configurator UI Component Metadata Configuration File
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_third_party_configurator_ui_component_metadata_file.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator_ui_component_files.htm
fetched_at: 2026-09-04
---

# Third-Party Configurator UI Component Metadata Configuration File

The configuration file defines the metadata values for the component, including supported targets and the design configuration.

REQUIRED EDITIONS

The configuration file follows the naming convention componentName.js-meta.xml, such as myComponent.js-meta.xml.

Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Set up the js-meta.xml file to expose the component to Lightning Flow and add it to the Product Configurator flow template.

This example includes the input properties you can import from the Data Manager component or other variables on the default product configurator flow. If you create a custom configurator flow with other properties, you can add those to your js-meta.xml file.

<?xml version="1.0" encoding="UTF-8"?>
<!--
  ~ Copyright 2024 salesforce.com, inc. 
  ~ All Rights Reserved 
  ~ Company Confidential
  -->

<LightningComponentBundle xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>60.0</apiVersion>
    <isExposed>true</isExposed>
    <masterLabel>My Third Party Configurator Component</masterLabel>
    <description>My custom component that I will use in the 
        Configurator UI</description>
    <targets>
        <target>lightning__FlowScreen</target>
    </targets>
    <targetConfigs>
        <targetConfig targets="lightning__FlowScreen">
            <!-- INPUT PROPERTIES -->
            <property
                    name="transactionLineId"
                    type="String"
                    required="true"
                    label="Line Item ID"
                    description="Enter the ID of the transaction line to configure."
                    role="inputOnly" />
            <property
                    name="currentTransactionLineId"
                    type="String"
                    required="true"
                    label="Current Line Item ID"
                    description="The ID of the transaction line to launch the configurator."
                    role="inputOnly" />
            <property
                    name="transactionId"
                    type="String"
                    required="true"
                    label="Transaction ID"
                    description="Enter the ID of the transaction to configure."
                    role="inputOnly" />
            <property
                    name="addedNodes"
                    type="apex://ProductConfig.SalesTransactionItem[]"
                    label="Added Nodes"
                    description="Enter the API name of the flow resource that contains a collection of Apex ProductConfig__SalesTransactionItem records associated with the parent record transaction."
                    role="inputOnly" />
            <property
                    name="parentName"
                    type="String"
                    required="true"
                    label="Parent Name"
                    description="Enter the name or title of the parent transaction that the configuration pertains to."
                    role="inputOnly" />
            <property
                    name="origin"
                    type="String"
                    required="true"
                    label="Object Name"
                    description="Enter the API name of the transaction record's parent object."
                    role="inputOnly" />
            <property
                    name="messages"
                    type="apex://ProductConfig.Message[]"
                    label="Messages"
                    description="A collection of Apex ProductConfig__Message records that contain alerts, warnings, and errors encountered by the component."
                    role="inputOnly" />
            <property
                    name="optionGroups"
                    type="apex://ProductConfig.OptionGroup[]"
                    label="Option Groups"
                    description="A collection of ProductConfig__OptionGroup records that contain product option data grouped by product category."
                    role="inputOnly" />
            <property
                    name="summary"
                    type="apex://ProductConfig.PricingSummary"
                    label="Transaction Summary"
                    description="An Apex ProductConfig__PricingSummary record that contains summary information for the specified transaction ID, including all price-related details."
                    role="inputOnly" />
            <property
                    name="attributeCategories"
                    type="apex://ProductConfig.AttributeCategory[]"
                    label="Attribute Categories"
                    description="A collection of Apex ProductConfig__AttributeCategory records that contain details about the attributes groups that are grouped by attribute category."
                    role="inputOnly" />
            <property
                    name="header"
                    type="apex://ProductConfig.Product"
                    label="Product Details"
                    description="An Apex ProductConfig__Product record that contains details about the root-level product, including product name, description, and pricing."
                    role="inputOnly" />
            <property
                    name="navigationRoute"
                    type="apex://ProductConfig.NavigationInfo[]"
                    label="Navigation Information"
                    description="A collection of Apex ProductConfig__NavigationInfo records that contain breadcrumb navigation information for the UI."
                    role="inputOnly" />
            <property
                    name="searchInfo"
                    type="apex://ProductConfig.SearchItemInfo[]"
                    label="Search Info"
                    description="A collection of Apex ProductConfig__SearchItemInfo records that contain option information for the search bar."
                    role="inputOnly" />
            <property
                    name="currencyCode"
                    type="String"
                    label="Currency Code"
                    description="The currency code used for the transaction."
                    role="inputOnly" />
            <property
                    name="transactionRecord"
                    type="apex://ProductConfig.TransactionRecord"
                    label="Transaction Record"
                    description="An Apex ProductConfig__TransactionRecord record that contains transaction record details, including transaction origin, parent name, and ID."
                    role="inputOnly"/>
            <property
                    name="isClassContext"
                    type="Boolean"
                    label="Product Classification Preview Mode"
                    description="A Boolean value that indicates whether the record being previewed was a product classification record."
                    role="inputOnly" />
            <property
                    name="isDesignTime"
                    type="Boolean"
                    label="Preview Mode"
                    description="A Boolean value that indicates whether a product or product classification record was viewed in preview mode."
                    role="inputOnly" />
            <property
                    name="headerTitle"
                    type="String"
                    label="Configurator Title"
                    description="The title that was used for the configurator screen heading."
                    role="inputOnly" />
            <property
                    name="isInstantPricingToggleEnabled"
                    type="Boolean"
                    label="Show Instant Pricing Toggle"
                    description="A Boolean value that indicates whether the instant pricing toggle was shown."
                    role="inputOnly" />
            <property
                    name="isCompactLayoutEnabled"
                    type="Boolean"
                    label="Compact Mode"
                    description="A boolean value that indicates whether compact mode is enabled."
                    role="inputOnly" />
            <property
                    name="isInstantPricingEnabled"
                    type="Boolean"
                    label="Instant Pricing"
                    description="A Boolean value that indicates whether the instant pricing toggle was enabled. If false, the Update Prices button is shown for manual price refresh."
                    role="inputOnly" />
            <property
                    name="isProductValidationEnabled"
                    type="Boolean"
                    label="Product Validation"
                    description="A Boolean value that indicates whether product validation was enabled."
                    role="inputOnly" />
            <property
                    name="showPrices"
                    type="Boolean"
                    label="Price Visibility"
                    description="A Boolean value that indicates whether pricing information was shown at runtime."
                    role="inputOnly" />
            <property
                    name="isConfiguratorDisabled"
                    type="Boolean"
                    label="Disabled"
                    description="A Boolean value that indicates whether this component was disabled."
                    role="inputOnly" />
            <property
                    name="isApiInProgress"
                    type="Boolean"
                    label="API Call Status"
                    description="A Boolean value that indicates whether the API call is in progress."
                    role="inputOnly" />
            <property
                    name="isPriceRampEnabled"
                    type="Boolean"
                    label="Ramp Deals Enabled"
                    description="A Boolean value that indicates whether Ramp Deals are enabled for this product."
                    role="inputOnly" />
            <property
                    name="tabs"
                    type="apex://ProductConfig.NavigationInfo[]"
                    label="Navigation Tabs"
                    description="A collection of Apex ProductConfig__NavigationInfo records to display tabs in the Configurator."
                    role="inputOnly" />
            <property
                    name="salesTransactionItems"
                    type="apex://ProductConfig.SalesTransactionItem[]"
                    label="Sales Transaction Items"
                    description="A collection of Apex ProductConfig__SalesTransactionItem records that contain sales transaction item details."
                    role="inputOnly" />
            <property
                    name="searchResultOptionId"
                    type="String"
                    label="Search Result Option Id"
                    description="The ID of the option selected from the search bar."
                    role="inputOnly" />
        </targetConfig>
    </targetConfigs>
</LightningComponentBundle>
SEE ALSO
Create a Third-Party Configurator UI Component

=== ARTICLE: ind.product_configurator_use_the_cml_editor.htm ===
---
article_id: ind.product_configurator_use_the_cml_editor.htm
title: Use Code to Define Constraints and Rules in the CML Editor
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_use_the_cml_editor.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_create_a_constraint_model.htm
fetched_at: 2026-09-04
---

# Use Code to Define Constraints and Rules in the CML Editor

In the Constraint Builder, use Constraint Modeling Language (CML) code to define constraints and rules for a constraint model.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create a constraint model:	Product Configuration Constraints Designer permission set

Complete the steps for Constraint Rules Engine setup before you work with constraint models. See Set Up Configurator With Constraint Rules Engine.

In the CML Editor, you add types for a constraint model to define constraints and rules. A type corresponds mainly to a product, product bundles, or product classification. There are also special types that work differently from the main types —  imported types from linked constraint models, and types corresponding to product component groups imported from Product Catalog Management (PCM). The CML Editor uses constraint modeling language (CML) to define constraint models. For more information on CML, see the Constraint Modeling Language (CML) User Guide.

You can import data from Salesforce objects to include in CML code. See Import Data from Salesforce Objects to Use in Constraint Models.

Create a constraint model.
In the Constraint Models app, select the constraint model you want to modify.
On the Details page, select the version name of the constraint model.
In the Constraint Builder header in the upper left corner, select CML Editor.
To create a new constraint model, select New Type.
Give the type a name that refers to the product, product bundle, or product classification it modifies, such as Laptop. To make the new type a child of an existing type, select a parent type.
Select Create.
In the left pane, select the type name.
To define variables, relationships, or associations for the selected type, go to the tabs for Variables, Relationships, or Associations, and follow the prompts to enter and save the required information.
To edit existing variables, relationships, or associations in the respective tabs, from the quick-action menu, click Edit, and then make the needed changes.
To write or edit CML code directly and define your constraints and rules, work in the CML Editor code window.
Save your changes.
To make the constraint model available for use, select Activate.

After you save a constraint model, you can switch back and forth between the CML Editor and the Visual Builder. Use the Visual Builder to add or edit constraints and rules with point-and-click tools.

NOTE Some constraints and rules that you create in the CML Editor can't be edited in the Visual Builder because they're not part of the Visual Builder tools. If you try to edit one of those constraints or rules in the Visual Builder, a message prompts you to return to the CML Editor.

=== ARTICLE: ind.product_configurator_use_the_visual_builder.htm ===
---
article_id: ind.product_configurator_use_the_visual_builder.htm
title: Define Constraints and Rules with the Visual Builder
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_use_the_visual_builder.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_create_a_constraint_model.htm
fetched_at: 2026-09-04
---

# Define Constraints and Rules with the Visual Builder

In the Constraint Builder, use point-and-click tools in the Visual Builder to define the constraints and rules for a constraint model. Add constraints and rules to easily configure products or product bundles.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS NEEDED
To create a constraint model:	Product Configuration Constraints Designer permission set

Complete the steps for Constraint Rules Engine setup before you work with constraint models. See Set Up Configurator With Constraint Rules Engine.

When you import a bundle with the Visual Builder, product classes are imported, but the class attributes aren't imported. You can add attributes manually in the CML Editor. For more information on working in the CML Editor, see Use Code to Define Constraints and Rules in the CML Editor.

Create a constraint model.
In the Constraint Models app, select the constraint model you want to modify.
On the Details page, select the version name of the constraint model.
To add a new item, click Add Item, select Product, and then click Next.
Select the item or items that you want to add to the constraint model, and then save your changes.
When you add a bundle, its product component groups and their cardinality are automatically imported from Product Catalog Management (PCM). The entire bundle structure is visible in the left panel, with child products and product classifications grouped into the respective product component groups. However, you can’t define constraints or rules at the group level.
Under Products, select the item that you want to add a constraint or rule to.
In the Visual Builder window, click .
Select a constraint or rule type.
To define the constraint or rule for the selected item, add one or more expressions.
To create more advanced conditions, you can also group multiple expressions. To do this, define a grouping logic. Use expression numbers within parentheses ‘()’ to form groups, and connect them with 'and', 'or', or 'xor' operators.
For example, (1 and 2) or (3 and 4).
If you don’t define a specific grouping logic, all expressions are by default combined using an ‘and’ operator.
Add more constraints or rules as needed, and add expressions to them.
Save the constraint model.
To make the constraint model available for use, select Activate.

After you save a constraint model, you can switch back and forth between the Visual Builder and the CML Editor. Use the CML Editor to view and edit code for the constraint model. For more information on CML, see the Constraint Modeling Language (CML) User Guide.

NOTE Some constraints and rules you create in the CML Editor can't be changed in the Visual Builder because they aren't part of the Visual Builder tools. These are labeled in the Visual Builder as not editable.

=== ARTICLE: ind.product_configurator_use_third_party_configurator_for_specific_products_or_classifications.htm ===
---
article_id: ind.product_configurator_use_third_party_configurator_for_specific_products_or_classifications.htm
title: Use Third-Party Configurator for Specific Products or Classifications
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_use_third_party_configurator_for_specific_products_or_classifications.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_third_party_configurator.htm
fetched_at: 2026-09-04
---

# Use Third-Party Configurator for Specific Products or Classifications

Configure product or classifications by using the third-party configurator instead of the default configurator.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Specify the use of a third-party configurator by assigning a Product Configuration Flow linked to the third-party configurator to products or classifications. As a result, the third-party configurator is launched when you configure these products.

SEE ALSO
Define Product Configuration Flows

=== ARTICLE: ind.product_configurator_validate_a_configuration_rule.htm ===
---
article_id: ind.product_configurator_validate_a_configuration_rule.htm
title: Validate Configuration Rules in Business Rules Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_validate_a_configuration_rule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_configuration_rules.htm
fetched_at: 2026-09-04
---

# Validate Configuration Rules in Business Rules Engine

Rules are complex and can become outdated due to catalog changes. To maintain rule integrity, validate a configuration rule and identify the potential errors caused by catalog changes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
USER PERMISSIONS
NEEDED
To validate a rule:	Manage Configurator with Business Rules Engine
From the home page of the Product Catalog Management app, click Product Configuration Rules.
Open the rule that you want to validate.
On the rule details page, click Validate.
After the validation is complete, identified errors are visible in the Rule Validation Error window. To fix the errors, click Edit Rule.

=== ARTICLE: ind.product_configurator_visual_builder_basic_logic_constraint.htm ===
---
article_id: ind.product_configurator_visual_builder_basic_logic_constraint.htm
title: Basic Logic Constraint in the Visual Builder
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_visual_builder_basic_logic_constraint.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_visual_builder_constraint_and_rule_types.htm
fetched_at: 2026-09-04
---

# Basic Logic Constraint in the Visual Builder

Enforce a specific condition on a product, product bundle, or attribute with the basic logic constraint. Users must adhere to the defined condition to configure the associated product or product bundle successfully.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

In the basic logic constraint window, add an expression to define a condition for a parameter that must be true. Add more expressions as needed. Include an optional message that's shown if the user doesn't meet the required condition and prompts the user to fix the error.

=== ARTICLE: ind.product_configurator_visual_builder_conditional_logic_constraint.htm ===
---
article_id: ind.product_configurator_visual_builder_conditional_logic_constraint.htm
title: Conditional Logic Constraint in the Visual Builder
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_visual_builder_conditional_logic_constraint.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_visual_builder_constraint_and_rule_types.htm
fetched_at: 2026-09-04
---

# Conditional Logic Constraint in the Visual Builder

The conditional logic constraint defines a constraint in which, if one or more conditions are true, another condition is also true. If you define a conditional constraint,users must adhere to the defined conditions in order to configure products successfully.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

In the conditional logic constraint window, add one or more expressions to define a condition or conditions that must be true. Then, add an expression to define a condition that is true if the previous condition or conditions are true. For example, use a logical constraint condition to say that, when an order has six or more laptops, the shipping address must be in the United States.

Include an optional message that's shown if the user doesn't meet the required condition and prompts the user to fix the error.

=== ARTICLE: ind.product_configurator_visual_builder_constraint_and_rule_types.htm ===
---
article_id: ind.product_configurator_visual_builder_constraint_and_rule_types.htm
title: Constraint and Rule Types in the Visual Builder
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_visual_builder_constraint_and_rule_types.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_create_a_constraint_model.htm
fetched_at: 2026-09-04
---

# Constraint and Rule Types in the Visual Builder

The Visual Builder provides point-and-click tools for you to easily define constraints and rules for a constraint model. Use the basic logic constraint, the conditional logic constraint, the message rule, the require rule, the exclude rule, the hide/disable rule, and the preference rule to author complex configurations for products and product bundles in your catalog.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

You add expressions to constraints and rules to define the conditions that they enforce.

Build an expression by defining these parts: a left-hand side element, an operator, and a right-hand side element. Your choice for each part of the expression dynamically filters the options available to you in the next part. First, select your left-hand side element. Depending on the item you’re building your expression for, you can choose from flexible options such as individual products, product bundles, child products within the product bundle, attributes, fields, variables defined in CML Editor, and sales transaction header. Next, select the operator. For the right-hand side element field, select another dynamic element or parameter to compare against or select the Value option to enter a static value or pick the value from a predefined list.

To create more complex conditions, you can control how multiple expressions relate to each other by grouping them. In the Grouping Logic field, define a syntax that combines your expressions. Group expressions by referencing their numbers within parentheses ‘()’ and connecting them with the logical operators ‘and’, ‘or’, or ‘xor’. For example, the logic "(1 and 2) or 3" requires that either the conditions defined in expressions 1 and 2 are both true, or that the condition in expression 3 is true.

For your grouping logic to be valid, follow these guidelines.

Use only valid characters: Your logic can contain only expression numbers, parentheses ‘()’, and the operators ‘and’, ‘or’, or ‘xor’.
Group expressions clearly when there are mixed operators: When the logic contains mixed operators, always group expressions by using '()' to define the exact evaluation order.

For example, a grouping logic such as “1 and 2 or (3 or 4) and 5” isn’t valid. To fix it, clarify the intended order of operations. Change the logic to “1 and ((2 or 3) or (4 and 5))” or “(1 and (2 or 3)) or (4 and 5)”.

Use only numbers that correspond to defined expressions: Make sure that all expression numbers that you use in the logic correspond to an expression. For example, if you have four expressions defined, you can use only the numbers 1, 2, 3, and 4. 
Reference each expression once: Every expression number can be used only once in the logic. Also, make sure that the numbers corresponding to all the defined expressions are a part of the logic.

Add a name to the constraint to make it easy to find when you work with multiple constraints in a model. Add an optional run-time message that configurator users see if their input violates the constraint conditions. Run-time messages are mandatory for the Dynamic Message Rule type.

This dynamic message rule, with the name Optional Bundle Discount, shows an informational message to the sales reps about an optional discount they can apply if the defined conditions are true.

When you define a constraint or rule in Visual Builder, the constraint rules engine generates the Constraint Modeling Language (CML) code for the configuration. You can view and edit the code in CML Editor, and switch between Visual Builder and CML Editor as you work. If you name the constraint in Visual Builder, the name appears as a code comment in CML Editor.

In this example, the code message((megapackagegroup.laptop[Laptop].Display_Size == "15 Inch" && megapackagegroup.laptop[Laptop].Display == "1080p Built-in Display") || megapackagegroup.laptop[Laptop].ItemNetTotalPrice > 1000, "This item is eligible for a 5% discount.", "Info"); defines the dynamic message rule that shows an informational message to the sales reps. The code comment identifies the constraint name as Optional Bundle Discount.

Basic Logic Constraint in the Visual Builder
Enforce a specific condition on a product, product bundle, or attribute with the basic logic constraint. Users must adhere to the defined condition to configure the associated product or product bundle successfully.
Conditional Logic Constraint in the Visual Builder
The conditional logic constraint defines a constraint in which, if one or more conditions are true, another condition is also true. If you define a conditional constraint,users must adhere to the defined conditions in order to configure products successfully.
Dynamic Message Rule in the Visual Builder
The dynamic message rule shows a message to users if the specified condition is true. Include a message to provide the user with information about an item, such as a promotional offer on a selected product.
Require Rule in the Visual Builder
The require rule automatically adds a specified product to a configuration if certain conditions are true. Use the require rule to make sure that certain products are sold together.
Exclude Rule
The exclude rule excludes an item from a quote or order when certain conditions are true. For example, use an exclude rule to specify that an order with a laptop can’t include a mouse.
Hide/Disable Rule
Hide or disable a component in a bundle, an attribute, or an attribute value when certain conditions are true, to remove the element from view, or to disable selections for it.
Preference Rule
The preference rule applies a constraint when certain conditions are true, but allows the constrainte engine to override the constraint if the user input violates the constraint conditions. For example, use the preference rule to specify that, when laptop display is 2K, the display size should be 15 inch or larger, but allow the configuration to continue without failing if the user selects a smaller display size, and deliver an error message indicating that display size should be 15 inch or larger.

=== ARTICLE: ind.product_configurator_visual_builder_dynamic_message_rule.htm ===
---
article_id: ind.product_configurator_visual_builder_dynamic_message_rule.htm
title: Dynamic Message Rule in the Visual Builder
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_visual_builder_dynamic_message_rule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_visual_builder_constraint_and_rule_types.htm
fetched_at: 2026-09-04
---

# Dynamic Message Rule in the Visual Builder

The dynamic message rule shows a message to users if the specified condition is true. Include a message to provide the user with information about an item, such as a promotional offer on a selected product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

In the dynamic message rule window, add one or more expressions to define a condition or conditions that, if true, show a message to the user. Then, enter the message in the Run-time Message field. You can also apply a message severity type to change the message's appearance and convey the level of urgency to the user.

The informational message type has a gray banner. An informational message doesn't require the user to take any action.
The warning type has a yellow banner. A warning message allows the user to continue working on the current task, but blocks them from taking the next step on the configuration page until they take action to address the issue described in the message.
The error type has a red banner. An error message blocks the user from continuing with the current task on the configuration page until they fix the error described in the message.
NOTE An error message doesn't block a user working in the Transaction Line Editor (Transaction Line Table, or TLT). In that component, the user can still make changes and save the quote, even when the quote contains conditions that trigger an error message.

=== ARTICLE: ind.product_configurator_visual_builder_exclude_rule.htm ===
---
article_id: ind.product_configurator_visual_builder_exclude_rule.htm
title: Exclude Rule
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_visual_builder_exclude_rule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_visual_builder_constraint_and_rule_types.htm
fetched_at: 2026-09-04
---

# Exclude Rule

The exclude rule excludes an item from a quote or order when certain conditions are true. For example, use an exclude rule to specify that an order with a laptop can’t include a mouse.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Write one or more expressions to define conditions that exclude an item, then select the item that is excluded when the conditions are true.

=== ARTICLE: ind.product_configurator_visual_builder_hide_disable_rule.htm ===
---
article_id: ind.product_configurator_visual_builder_hide_disable_rule.htm
title: Hide/Disable Rule
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_visual_builder_hide_disable_rule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_visual_builder_constraint_and_rule_types.htm
fetched_at: 2026-09-04
---

# Hide/Disable Rule

Hide or disable a component in a bundle, an attribute, or an attribute value when certain conditions are true, to remove the element from view, or to disable selections for it.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license
On a bundle, hide a component to remove it from the selection menu, or disable a component to preserve it in the menu but prevent users from selecting options for it.
On an individual product, hide an attribute to remove it from the selection menu, or disable an attribute to preserve it in the menu but prevent users from selecting options for it.
On an attribute, hide an attribute value to preserve it in the menu but prevent users from selecting options for it.
NOTE In Visual Builder, for attribute values, only the hide rule is enabled. When you apply the hide rule to an attribute value in Visual Builder, the value appears in the menu but selections are disabled. In CML code in CML Editor, for attribute values, the hide and disable rules have the same behavior.

=== ARTICLE: ind.product_configurator_visual_builder_preference_rule.htm ===
---
article_id: ind.product_configurator_visual_builder_preference_rule.htm
title: Preference Rule
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_visual_builder_preference_rule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_visual_builder_constraint_and_rule_types.htm
fetched_at: 2026-09-04
---

# Preference Rule

The preference rule applies a constraint when certain conditions are true, but allows the constrainte engine to override the constraint if the user input violates the constraint conditions. For example, use the preference rule to specify that, when laptop display is 2K, the display size should be 15 inch or larger, but allow the configuration to continue without failing if the user selects a smaller display size, and deliver an error message indicating that display size should be 15 inch or larger.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

Enter one or more expressions to define the conditions to be met, then enter one or more expressions to defined the preferred outcome. This outcome is overridden if the user enters input that violates the conditions to be met. Include an optional run-time message to show to the user when their input violates the rule conditions.

NOTE If a preference rule auto-adds a product that has one or more Product Selling Model Options (PSMOs), set one PSMO on the product to Default. The system uses the default PSMO to determine which pricebook entry to use for the auto-added product. For more information on Product Selling Model Options, see Manage Product Selling Model in Revenue Management.

=== ARTICLE: ind.product_configurator_visual_builder_require_rule.htm ===
---
article_id: ind.product_configurator_visual_builder_require_rule.htm
title: Require Rule in the Visual Builder
source_url: https://help.salesforce.com/s/articleView?id=ind.product_configurator_visual_builder_require_rule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: configurator
parent_article: ind.product_configurator_visual_builder_constraint_and_rule_types.htm
fetched_at: 2026-09-04
---

# Require Rule in the Visual Builder

The require rule automatically adds a specified product to a configuration if certain conditions are true. Use the require rule to make sure that certain products are sold together.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license or the Revenue Cloud Advanced license

In the require rule window, add one or more expressions to define conditions. Then, select an item that must be included if those conditions are true. Specify the quantity and default attribute values for the included item as needed. For example, use the require rule to specify that a laptop must always include a blue laptop bag.

NOTE If a require rule auto-adds a product that has one or more Product Selling Model Options (PSMOs), set one PSMO on the product to Default. The system uses the default PSMO to determine which pricebook entry to use for the auto-added product. For more information on Product Selling Model Options, see Manage Product Selling Model in Revenue Management.

