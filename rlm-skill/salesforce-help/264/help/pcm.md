# Salesforce Help 264 — área: pcm (142 artículos)

=== ARTICLE: ind.product_catalog_activate_dt_for_a_product.htm ===
---
article_id: ind.product_catalog_activate_dt_for_a_product.htm
title: Activate a Decision Table in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_activate_dt_for_a_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_decision_tables_for_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Activate a Decision Table in Revenue Management

Before you use decision tables in qualification rule procedure elements, you must set the decision tables to active.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To create, edit, and activate a decision table:	

Manage Product Catalog

AND

Rules Engine Designer

AND

Context Service Runtime


To use a decision table:	Rules Engine Runtime
From the Product Catalog Management app’s home page, click Qualification Rules.
From the Qualification Decision Tables list view, click the product decision table that you want to activate.
On the decision table page, click Activate.
TIP A decision table takes time to activate. To view the updated status, refresh the browser page.

=== ARTICLE: ind.product_catalog_add_components_to_a_configurable_product_bundle.htm ===
---
article_id: ind.product_catalog_add_components_to_a_configurable_product_bundle.htm
title: Add Components to a Configurable Product Bundle
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_add_components_to_a_configurable_product_bundle.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_creation_of_a_bundled_product_structure.htm
fetched_at: 2026-09-04
---

# Add Components to a Configurable Product Bundle

You can add multiple groups, multiple product components, or one product classification component under a product group in configurable bundles.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To add components to the product bundle:	Manage Product Catalog
To use the Structure tab:	ARC Access permission set
Groups are mandatory components in a configurable product bundle. Child components must be added only under Groups and not directly under the root product.
Product groups are structured hierarchically, where a root group acts as the parent and can contain multiple child groups. While a root group can include multiple child product groups, multiple product components, or a single product classification, this hierarchy is limited to two levels; child groups can’t contain further nested groups, and these elements can’t be mixed at the same level within a child group. For example, a child group can’t contain both product components and a product classification. A product classification can only be added once per group.
When you delete a group, all components under the group, such as products and product classifications, are deleted.
You can add simple and bundled products of type static or configurable as child components of a configurable bundle.
When adding a child component with a defined unit of measure to a configurable product bundle, the Quantity, Min Quantity, and Max Quantity fields automatically inherit the scaling and rounding method of the child component.

To dynamically add all products based on a product classification to a product bundle, add a product classification component under the group. Product Catalog Management dynamically makes all products based on the classification available at the time of selection at run time. We refer to adding a product classification component to a product bundle as Dynamic Options.

From the Product Catalog Management app’s home page, click Products.
From the product list view page, click the bundled product.
Navigate to the Structure tab.
To add a group, click under the root product or the parent group, and select Product Group.
You can add a group under a parent group only when the parent group doesn’t have a product classification component or product components. Product groups are mandatory in a configurable bundle hierarchy.
Specify these details:
Enter a group name and description.
Parent Group is the group under which you add a child group. If you’re adding the group under the root product, leave the Parent Group field blank.
Enter the minimum and maximum number of product components that users can select in the run time.
Save your changes.
To add product components under a group, click  under a group, select Product, and specify these details:
Select one or more products, and click Next.
If necessary, change the default product quantity.
Bundle to Bundle Component Relationship is the default Product Relationship Type for product components
To make the component a required component in the bundle, select Require this component. To add an optional component to a bundle, deselect Require this component .
If a component is required, the Structure tab shows a solid line between the parent component and child component. If the component is optional, the Structure tab shows a dotted line between the parent component and the child component.
To include a component in the bundle by default, select Include component by default.
To allow users to change product quantities during run time, select Allow quantity changes.
If Allow Quantity Changes is deselected, you can’t enter a minimum quantity and maximum quantity.
Enter the minimum number of product components that users can select in the bundle at run time under Min Quantity.
Enter the maximum number of product components that users can select in the bundle at run time under Max Quantity.
To add a product classification under the group, click  under a group, select Product Classification, and specify these details:
Select a product classification, and click Next.
NOTE You can select only an active product classification.
If necessary, change the default quantity.
When you add a product classification under a group, you automatically add all the products based on the classification to the run-time cart. The number of products you can select in runtime depends on the group cardinality. The number of selected products you can add depends on the product classification cardinality. Bundle to Product Classification Component Relationship is the default Product Relationship Type for product classification components.
Ensure that Require this component and Include component by default are deselected for the product classification component.
To allow users to change product quantities during run time, select Allow quantity changes.
If you don’t select Allow Quantity Changes, you can’t enter a minimum and maximum quantity.
Under Min Quantity, enter the minimum number of product components that users can select in the bundle at run time .
Under Max Quantity, enter the maximum number of product components that users can select in the bundle at run time .
Save your changes.

In addition to adding components and building the bundle hierarchy, you can also override attributes, define local product cardinality, define group cardinality, and edit product relationships. After you create a product, you can optionally assign the product to catalog categories and subcategories.

SEE ALSO
Local Cardinality and Group Cardinality
Product Relationships
Override Product Component Attributes In Bundles
Assign Products to Catalog Categories and Subcategories

=== ARTICLE: ind.product_catalog_add_components_to_a_static_product_bundle.htm ===
---
article_id: ind.product_catalog_add_components_to_a_static_product_bundle.htm
title: Add Components to a Static Product Bundle
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_add_components_to_a_static_product_bundle.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_creation_of_a_bundled_product_structure.htm
fetched_at: 2026-09-04
---

# Add Components to a Static Product Bundle

Static products are non-configurable at run time. That means you can’t add or remove child products, alter product quantities, or configure product attributes at run time. You can add product and product group components to a static product bundle. Product Group components are optional.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create bundled products:	Manage Product Catalog
To use the Structure tab:	ARC Access permission set
IMPORTANT When you add a product under a new static bundle, ensure that you select None under the parent product selling model. Additionally, don’t select any component selling model.
You can optionally add Product Group (1) components to the static bundle hierarchy.
If you delete a group, all components under the group, such as products and product classifications, are deleted.
Add only static simple products or static bundled products as child components of static bundled products. You can’t add configurable simple products or configurable bundle products as child components of static bundled products.
When you add child components to a static product bundle, make sure that the field Include component by default is selected on the child components. Also ensure that the field Allow Quantity Changes isn’t selected on the child components.
If your static simple product is based on a product classification, then all attributes for all components in the static bundle must have default values.
When adding a child component with a defined unit of measure to a static product bundle, the Quantity, Min Quantity, and Max Quantity fields automatically inherit the scaling and rounding method of the child component.
From the Product Catalog Management app’s home page, click Products.
From the product list view page, click the static bundle product.
Navigate to the Structure tab.
Click the plus icon under the root product, and select Product or Product Group. Product groups are optional in a static bundle hierarchy.
To add a group, specify these details:
Enter a group name and description.

If you’re adding this group directly under the root product, the parent group field is blank. If this group is a nested group, then the parent group is the group under which you’re adding this group.

Enter the minimum and maximum number of product components that users can select in runtime.
Save your changes.
To add a product, specify these details:
Select None under parent product selling model, and click Next.
Select one or more static simple or static bundle products, and click Next.
If necessary, change the default product quantity.
Don’t select any component selling model.

If you’re adding the product under the root product, leave the Group field blank. If you’re adding the product under a group, the Group field contains the group name.

To make the component a required component in the bundle, select Require this component.
If a component is required, the Structure tab shows a solid line between the parent component and child component. If the component is optional, the Structure tab shows a dotted line between the parent component and the child component.
Ensure that Include component by default is selected.
It’s mandatory to include the product component in the static bundle by default.
Ensure that Allow quantity changes is deselected.
When Allow Quantity Changes is deselected, you can’t enter a minimum and maximum quantity.
If the price of the bundled product includes the price of this product component, select Price Includes component. In this case, ensure that you deselect Allow quantity changes.
Save your changes.

=== ARTICLE: ind.product_catalog_assign_a_product_selling_model_to_a_product.htm ===
---
article_id: ind.product_catalog_assign_a_product_selling_model_to_a_product.htm
title: Assign a Product Selling Model to a Product
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_assign_a_product_selling_model_to_a_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_selling_model.htm
fetched_at: 2026-09-04
---

# Assign a Product Selling Model to a Product

After you create a product selling model, assign it to your products.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To assign product selling models to product:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Products.
On the Products list view page, click a product and navigate to the product’s related list.
In the Product Selling Model Options section, click New.
In the New Product Selling Model Option window, specify these properties:
Search and select a product selling model for this product.
If the product selling model is term-defined or evergreen, search and select a proration policy.
A proration policy indicates whether a customer can start a subscription partway through the pricing period and pay only for the time that they’ve subscribed for, rather than for the entire period. It also indicates whether any leftover amount from pricing term calculations is added to the beginning or to the end of the subscription.
You can optionally make this product selling model the default selling model for the product, by selecting Default.
Save your changes.

=== ARTICLE: ind.product_catalog_assign_attributes_to_a_product_classification.htm ===
---
article_id: ind.product_catalog_assign_attributes_to_a_product_classification.htm
title: Assign Attributes to a Product Classification
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_assign_attributes_to_a_product_classification.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_classifications.htm
fetched_at: 2026-09-04
---

# Assign Attributes to a Product Classification

After you create a Product Classification, assign attributes to it. You can assign individual attributes to a product classification or a collection of attributes through attribute categories.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To assign attributes to a product classification:	Manage Product Catalog

Here’s an example. Consider a product classification called “Beds Classification”. There’s an attribute category called “Bed” that has attributes such as material, finish, size, and model name. There’s another attribute category called “General” that has attributes such as Warranty in Months, and Country of Origin. The attributes Availability and Net Quantity don’t belong to any attribute category.

You can assign attributes that belong to the attribute categories “Bed” and “General” to the product classification “Beds Classification”. You can also assign individual attributes “Net Quantity” and “Availability” to the product classification. The product classification “Beds Classification” now has all of these attributes.

To assign attributes, follow these instructions:

From the Product Catalog Management app’s home page, click Product Classifications.
On the Product Classifications list view page, click the product classification to which you want to assign attributes.
Navigate to the Attributes tab.
In the Attributes section, click Assign.
To assign a collection of attributes to the product classification, select Assign Attributes by category. To assign individual attributes to the product classification, select Assign individual attributes.
Click Next.
If you selected Assign Attributes by category, then select one or more attribute categories, and click Assign.
NOTE You can assign only the active attributes of an attribute category to product classifications.
If you selected Assign individual attributes, then select one or more attributes from the Categorized and Uncategorized tabs and click Assign.
NOTE You can assign only active attributes to product classifications.

You can unassign attributes from a product classification. If you unassign an attribute from a product classification, the status of the attribute changes to “Inactive”.

To delete an attribute assigned to a product classification, click  next to the attribute, and click Delete.

To activate an inactive product classification attribute, click Edit, and change the status to Active.

You can preview a product classification to see how it will look and function for your users, if you have the Product Configuration User permission set license.

Considerations While Assigning Attributes to Product Classifications
Here are a few scenarios you can run into when assigning attributes to product classifications.

=== ARTICLE: ind.product_catalog_assign_products_to_catalog_cat_and_subcategories.htm ===
---
article_id: ind.product_catalog_assign_products_to_catalog_cat_and_subcategories.htm
title: Assign Products to Catalog Categories in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_assign_products_to_catalog_cat_and_subcategories.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_catalogs.htm
fetched_at: 2026-09-04
---

# Assign Products to Catalog Categories in Revenue Management

Organize products by assigning them to catalog categories and subcategories. You must create your product records first before assigning products to catalogs or categories.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To assign products to categories:	Manage Product Catalog
NOTE If you haven't created any products yet, see Create Products and Product Bundles in Revenue Management.

To assign products to catalogs and product categories, follow these instructions:

From the Product Catalog Management app’s home page, click Catalogs.
From the catalogs list view, click the catalog with the catalog category or subcategory to which you want to assign one or more products.
From the Catalog page, click Categories.
From the Categories section, click the catalog category or the catalog subcategory.
From the Category page, click Related.
In the Products section, click Assign Products.
 Select one or more products.
Click Next.
Save your changes.
NOTE If you receive error code -265738217 when assigning products, verify that the Category Page Layout is added to the user's profile. For details, see Error Assigning Products to Catalog Categories.
SEE ALSO
Create a Catalog
Create Catalog Categories and Subcategories
Products

=== ARTICLE: ind.product_catalog_attribute_fields.htm ===
---
article_id: ind.product_catalog_attribute_fields.htm
title: Working with Product Attribute Fields
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_attribute_fields.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_dynamic_attributes.htm
fetched_at: 2026-09-04
---

# Working with Product Attribute Fields

Learn more about the fields used in product attribute definitions. Some fields simply define an attributes, while others affect runtime when your sales reps are working with quotes and orders.

REQUIRED EDITIONS
View supported products and editions.
Attribute fields and descriptions
FIELD	DESCRIPTIONS
Name	The name of the attribute.
Product	The name of the product. This field is available when you edit inherited product attributes. This field isn’t editable.
Product Classification	The name of the product classification. This field is available when you edit the product classification attribute. This field isn’t editable.
Attribute	The attribute associated with the product classification or product. This field isn’t editable.
Attribute Category	The attribute category associated with the product classification or product. This field isn’t editable.
Status	The lifecycle status of the attribute.
Help Text	This field stores useful information for runtime users.
Default Value	The default value of an attribute for a product classification or product.
Attribute Name Override	The name that’s displayed for the product classification attribute or product attribute instead of the specified attribute name. The Attribute Name Override overrides the name on the attribute. For example, you can override the attribute “Color” to display as “Laptop Color” for a product classification or a product.
Value Description	The description of the value defined for the product classification attribute or the product attribute.
Description	The description of the product classification attribute or the product attribute.
Is Price Impacting	Select if this attribute dictates the price of a product.
Sequence	The display sequence of the attribute when you configure the attribute during runtime.
Minimum Value	The minimum value that you can enter for attributes of type number, currency, and percent in run time. The minimum value must be less than or equal to the maximum value.
Maximum Value	The maximum value that you can enter for attributes of type number, currency, and percent in run time.
Minimum Character Count	The minimum number of alphanumeric characters that you can enter for attributes of type number and text in run time. The minimum character count must be less than or equal to the maximum character count.
Maximum Character Count	The maximum number of alphanumeric characters that you can enter for attributes of type number and text in run time.
Run Time Settings
SETTING	DESCRIPTION
Is Required	Select the field if this attribute requires a value when you assign it to a parent object.
Is Hidden	Select the field if you want to hide the attribute from users in the run time.
Is ReadOnly	Select the field if the attribute is read only for users in the run time.
Display Type	Select how attributes of a specific data type are displayed in the user interface at run time. For example, attributes of a checkbox data type can be displayed as checkboxes or toggles in the user interface.
Step Value	You can display attributes of the currency, number, and percent data types as sliders in the user interface at run time. Instead of typing in a number, or using increment buttons, drag the slider on a predefined scale to adjust the attribute values. The slider is positioned at the default value. You can slide the attribute value in increments or decrements of the step value. The step value must be greater than zero. Additionally, the difference between the maximum value and minimum value must be exactly divisible by the step value. You must always define the default value, minimum value, and maximum value for an attribute when the attribute’s display type is slider.
Examples for run-time attribute settings
ATTRIBUTE	IS REQUIRED	IS HIDDEN	IS READ ONLY	RESULT
Color	Yes	No	Yes	This is a required attribute and is visible in the run time. It has a default value, however the value isn’t editable.
Quantity	Yes	No	No	This is a required attribute and is visible in the run time. It has a default value, and the value is editable.
Assembly Required	No	Yes	Yes or No	This is an optional attribute that isn’t visible in the run time.
Country of Origin	No	No	Yes	This is an optional attribute that’s visible in the run time. However, the attribute value isn’t editable.
Check Availability in Zip Code	No	No	No	This is an optional attribute that’s visible in the run time. The attribute value is editable, but it's not mandatory to enter a value.
Considerations while updating attribute field values
If you update attribute field values in the attribute definition, review and update the corresponding attribute values on the product classification attributes and product attributes.
If you update these attribute field values in the product classification attributes, review and update the corresponding attribute values on the product attributes.
If you update attribute field values in the product attributes, review and update the corresponding attribute value overrides in the context of any bundles the product is a part of.

=== ARTICLE: ind.product_catalog_attribute_mapping_in_qualification_rule_procedures.htm ===
---
article_id: ind.product_catalog_attribute_mapping_in_qualification_rule_procedures.htm
title: Attribute Mapping in Qualification Rule Procedures
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_attribute_mapping_in_qualification_rule_procedures.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_qual_rule_procedure_for_product.htm
fetched_at: 2026-09-04
---

# Attribute Mapping in Qualification Rule Procedures

In your qualification rule procedures, you must map specific attributes from the context definition to the corresponding decision table fields based on the type of the qualification element. In addition, you must map your custom attributes that must be used to evaluate qualification.

REQUIRED EDITIONS
View supported products and editions.

Here’s a table that lists the attributes that you must map based on the type of the qualification element.

TYPE	NODE NAME	ATTRIBUTE NAME	DESCRIPTION
Product Category Qualification or Disqualification	Category	CategoryID	Is mapped to the Category field of the input parameter of the custom element in the procedure.
IsCategoryQualified	Is mapped to the Qualified or Disqualified field of the output parameter of the custom element in the procedure. The product category is qualified when the value is True or Null, and disqualified when the value is False. The CategoryDisqualificationReason field populates the disqualification reason when this attribute is False.
CategoryDisqualificationReason	Is mapped to the Reason field of the output parameter of the custom element in the procedure.
CurrentDate	Is mapped to the EffectiveFromDate and EffectiveToDate field of the input parameter of the custom element in the procedure. The CurrentDate attribute is of the format ‘YYYY-MM-DD’.
Product Qualification or Disqualification	CategoryProduct	ProductId	Is mapped to the Product field of the input parameter of the custom element in the procedure.
RootProductId	Is mapped to the Root Product field of the input parameter of the custom element in the procedure.
ParentProductId	Is mapped to the Parent Product field of the input parameter of the custom element in the procedure.
IsQualified	Is mapped to the Qualified or Disqualified field of the output parameter of the custom element in the procedure. The product is qualified when the value is True or Null, and disqualified when the value is False. The Reason field stores the disqualification reason when this attribute is False.
Reason	Is mapped to the Reason field of the output parameter of the custom element in the procedure.
CurrentDate	Is mapped to the EffectiveFromDate and EffectiveToDate field of the input parameter of the custom element in the procedure. The CurrentDate attribute is of the format ‘YYYY-MM-DD’.

=== ARTICLE: ind.product_catalog_begin_using_product_catalog_management.htm ===
---
article_id: ind.product_catalog_begin_using_product_catalog_management.htm
title: Begin Using Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_begin_using_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Begin Using Product Catalog Management

Review the supported products, editions, and permission sets for Product Catalog Management (PCM). Tailor the experience of using PCM for all users using permission sets to give them precise access to what they need.

REQUIRED EDITIONS
View supported products and editions.
Product Catalog Management Editions and Permission Sets
Give users access to Product Catalog Management features. Review the supported products, editions, and permission sets for Product Catalog Management. Assign the prebuilt permission sets or custom permission set groups.
Product Catalog Management Personas for Revenue Management
Explore the different types of users who work with Product Catalog Management and the permission sets they need.

=== ARTICLE: ind.product_catalog_bundled_product_validations.htm ===
---
article_id: ind.product_catalog_bundled_product_validations.htm
title: Manage Validations for Product Bundles
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_bundled_product_validations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_bundled_products.htm
fetched_at: 2026-09-04
---

# Manage Validations for Product Bundles

As product bundles grow over time, tracking the number of components and ensuring that every component meets the cardinality and structural requirements can become challenging. Validate Product Definition runs on-demand checks against your entire bundled product to ensure compliance. The validations also suggest corrective actions to help maintain the integrity and accuracy of your product configurations.

REQUIRED EDITIONS
View supported products and editions.
Configurable Product Validations

Here’s what’s validated for configurable parent products:

The number of products in a group must be greater than or equal to the minimum number of components in the group.
The number of required products in a group must be less than or equal to the maximum number of components in the group.
The number of child groups under a parent group must be greater than or equal to the minimum number of components in the parent group.
The number of child groups that have required product components must be less than or equal to the maximum number of components in the parent group.
EXAMPLE Consider a parent group PG that has this cardinality:
Minimum number of components: 2
Maximum number of components: 4

The parent group has only one child group CG1.

The validation fails because the parent group must have a minimum of 2 child groups but only one child group exists.

EXAMPLE Consider a parent group PG that has this cardinality:
Minimum number of components: 1
Maximum number of components: 1

The parent group has two child groups with these components:

Child group CG1 has one optional product
Child group CG2 has one optional product

The validation succeeds because both the child groups have optional products, and users can select a product from either of these groups at runtime. The number of required products is 0, which is less than the maximum number of components in the group, which is 1.

EXAMPLE Consider a parent group PG that has this cardinality:
Minimum number of components: 1
Maximum number of components: 1

The parent group has two child groups with these components:

Child group CG1 has one required product
Child group CG2 has one required product

The validation fails because both the child groups have required products. The number of required products in a group is 2, which is greater than the maximum number of components in the group, which is 1.

Example of a Static Product Validation

Here’s what’s validated for static parent products:

The default number of components in a group must be greater than or equal to the minimum number of components in the group.
The default number of components must be less than or equal to the maximum number of components in the group.
The number of child groups under a parent group must be greater than or equal to the minimum number of components in the parent group.
The number of child groups under a parent group must be less than or equal to the maximum number of components in the parent group.
EXAMPLE Consider a parent group PG that has this cardinality:
Minimum number of components: 2
Maximum number of components: 5

The parent group has two child groups with these components:

Child group CG1 has one required product.
Child group CG2 has one optional product.

The validation succeeds because the number of child groups under PG is equal to the minimum number of components but less than the maximum number of components.

Validate the Product Definition
Use Validate Product Definition to check the integrity of your product bundles.

=== ARTICLE: ind.product_catalog_cardinality_examples.htm ===
---
article_id: ind.product_catalog_cardinality_examples.htm
title: Group Cardinality Examples
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_cardinality_examples.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_group_cardinality.htm
fetched_at: 2026-09-04
---

# Group Cardinality Examples

To better understand how group cardinality works in Product Catalog Management, refer to these examples.

REQUIRED EDITIONS
View supported products and editions.

These examples demonstrate how the group cardinality and the product component relationship settings dictate how many products you can add to the run-time cart.

EXAMPLE Example 1

Group

Min Number of Components: 3
Max Number of Components: 5
 	Min Quantity	Max Quantity	Default Quantity	Is Component Required	Is Default Component
Child 1	1	20	4	No	No

This is an invalid configuration because the group requires at least three distinct components and the user can add only one distinct component in the run time.

EXAMPLE Example 2

Group

Min Number of Components: 3
Max Number of Components: 5
 	Min Quantity	Max Quantity	Default Quantity	Is Component Required	Is Default Component
Child 1	1	20	4	No	No
Child 2	1	20	4	No	No
Child 3	1	20	4	No	No
Child 4	1	20	4	No	No
Child 5	1	20	4	No	No
Child 6	1	20	4	No	No

All the child components here are distinct. This is a valid configuration if a minimum of three and a maximum of five child components are added to the cart during run time.

EXAMPLE Example 3

This example explains the scenario when the Minimum Number of Components and Maximum Number of Components fields are left blank.

Group

Min Number of Components: Null
Max Number of Components: Null

This is a valid configuration and users can add a child component to this group. When the Min Components field is left blank it implies that the minimum number of distinct components in the group can be zero. When the Max Components field is left blank it implies that the maximum number of distinct components in the group can be infinite.

EXAMPLE Example 4

Group

Min Number of Components: 3
Max Number of Components: 5
 	Min Quantity	Max Quantity	Default Quantity	Is Component Required	Is Default Component
Child 1	1	20	4	Yes	Yes
Child 2	1	20	4	Yes	Yes
Child 2	1	20	4	Yes	Yes
Child 3	1	20	4	Yes	Yes
Child 3	1	20	4	Yes	Yes
Child 4	1	20	4	Yes	Yes

This configuration violates the group cardinality because a user can only add a maximum of five distinct and required child components to the bundle.

Group Cardinality and Product Classification Component Cardinality

Here are a few examples that demonstrate how the group and product classification cardinalities determine how many products you can add in your cart at run time.

EXAMPLE Example 1

Group A cardinality:

Min Number of Components: 2
Max Number of Components: 2

Product Classification B cardinality:

Min Quantity: 1
Max Quantity: 5
Quantity: 2

Products based on Product Classification B:

Product 1
Product 2
Product 3
Product 4
Product 5

At run time, the user can select exactly two products out of the five, because the group cardinality allows a minimum and maximum of two product components. Let’s suppose the user selects Product 3 and Product 5 in the runtime.

The default quantity for Product 3 is two. However, the user can change the quantity of Product 3 to a minimum of one and a maximum of five. The user must select between one and five numbers of Product 3 products because the product classification cardinality allows a minimum of one and a maximum of five products.

The default quantity for Product 5 is two. However, the user can change the quantity of Product 5 to a minimum of one and a maximum of five. The user must select between one and five numbers of Product 5 products because the product classification cardinality allows a minimum of one and a maximum of five products.

EXAMPLE Example 2

Group X cardinality:

Min Number of Components: 2
Max Number of Components: 5

Product Classification YY cardinality:

Min Quantity: 2
Max Quantity: 4
Quantity: 3

Products based on Product Classification YY

ProductYY 1
ProductYY 2
ProductYY 3
ProductYY 4
ProductYY 5
ProductYY 6

At run time, the user can select between two and five products because the group cardinality allows a minimum of two and a maximum of five product components. Let’s suppose the user selects Product YY1 and Product YY4 in the runtime.

The default quantity for Product YY1 is three. However, the user can change the quantity of Product YY1 to a minimum of two and a maximum of four. The user must select between two and four numbers of Product YY1 products because the product classification cardinality allows a minimum of two and a maximum of four products.

The default quantity for Product YY4 is three. However, the user can change the quantity of Product YY4 to a minimum of two and a maximum of four. The user must select between two and four numbers of Product YY4 products because the product classification cardinality allows a minimum of two and a maximum of four products.

=== ARTICLE: ind.product_catalog_catalogs.htm ===
---
article_id: ind.product_catalog_catalogs.htm
title: Organize Your Products with Catalogs and Categories
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_catalogs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Organize Your Products with Catalogs and Categories

A catalog is a collection of the products that you sell, organized into categories for easier browsing. You must create a catalog before you create catalog categories and assign products to the categories.

REQUIRED EDITIONS
View supported products and editions.
EXAMPLE Imagine a catalog called Furniture. This catalog can have several categories such as Outdoor Furniture, Dining, Wardrobes, Sofas, Beds, and Tables. You can then create a subcategories for the catalog categories. For example, the Beds category can have subcategories such as Beds with Storage, Single Beds,Double Beds, and so on.

To get started with product catagories, refer to these instructions:

Create a Catalog
Define your product offerings in Product Catalog Management with product catalogs. Catalogs enable efficient organization and management of all the products your business sells. You must create at least one product catalog.
Create Catalog Categories and Subcategories
Organize and group products in your catalog by creating catalog categories and catalog subcategories. Assign products to more than one catalog category and subcategory.
Sort Categories in a Catalog
Make the browsing experience consistent and predictable for your buyers by defining category display order in Product Catalog Management (PCM) at design time. The same order appears in Product Discovery (PD) at runtime.
Assign Products to Catalog Categories in Revenue Management
Organize products by assigning them to catalog categories and subcategories. You must create your product records first before assigning products to catalogs or categories.
Set a Default Product Catalog
Set a default catalog for your product list page to show the most relevant products for your users. For complex orders, configure your product list page in Lightning App Builder or flows to help users to easily switch catalogs.

=== ARTICLE: ind.product_catalog_change_a_configurable_bundle_product_to_a_static_bundle_product.htm ===
---
article_id: ind.product_catalog_change_a_configurable_bundle_product_to_a_static_bundle_product.htm
title: Change a Configurable Bundle Product to a Static Bundle Product
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_change_a_configurable_bundle_product_to_a_static_bundle_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_conversion_of_bundle_products.htm
fetched_at: 2026-09-04
---

# Change a Configurable Bundle Product to a Static Bundle Product

You can change a configurable bundle product to a static product bundle when you don’t want to configure the bundle during run time. You can't configure products in a static product bundle during run time. Every bundle component is present in the bundle by default and can’t be removed. You can’t change the child component quantity in the run time. Every attribute of every product component has a default value.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To convert bundled products from configurable to static:	Manage Product Catalog
To use the Structure tab:	ARC Access permission set

To change a configurable bundle product to a static bundle product, these requirements must be met:

All root and child product attributes have default values.
Configure During Sale for the root product and every child product is set to Not Allowed or None.
Include component by default is selected for every child product.
Allow Quantity Changes is deselected for every child product component.
Product classification components must not exist in the configurable product bundle.
From the Product listing page, click the root configurable bundle product.
Navigate to the Attributes tab for this product.
Ensure that every inherited and configured attribute for all product components in the bundle has a default value.
From the Inherited Attributes section, configure every attribute, and enter a default value for attributes that don’t have one.
Save your changes.
From the Overridden Inherited Attributes related list, edit every attribute, and enter a default value for attributes that don’t have one.
Save your changes.
Perform these steps for all product components in this configurable bundle.
Navigate to the Structure tab for the root configurable bundle product.
Ensure that every child product component is static.
Click the name of every product child component.
From the Product page, edit the product.
Change the value of the ConfigureDuringSale field to Not Allowed or None.
Save your changes.
Set the ConfigureDuringSale field of every child product of this product component to Not Allowed or None. You can access the child components of this product component from its Structure tab.
Ensure that there are no product classification components in the bundle hierarchy.
Click the Product Classification component tile.
Click Delete. 
Perform these steps for every product component in the bundle:
Navigate to the Structure tab of the root configurable product.
Click every product component tile.
In the right panel, navigate to the Cardinality tab.
Select Include component by default.
Deselect Allow Quantity Changes.
Save your changes.
Finally, edit the root product bundle.
To change the root product to type static, change the value of Configure During Sale to Not Allowed or None.
Save your changes.

After you convert the configurable product bundle to a static product bundle, click Validate Product Definition to determine if the static bundle has any product components without default attribute values. If the validation results return such attributes, assign a default value to each of them and validate the product definition again.

=== ARTICLE: ind.product_catalog_change_a_static_bundle_product_to_a_configurable_bundle_product.htm ===
---
article_id: ind.product_catalog_change_a_static_bundle_product_to_a_configurable_bundle_product.htm
title: Change a Static Bundle Product To a Configurable Bundle Product
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_change_a_static_bundle_product_to_a_configurable_bundle_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_conversion_of_bundle_products.htm
fetched_at: 2026-09-04
---

# Change a Static Bundle Product To a Configurable Bundle Product

You can change a static product bundle to a configurable product bundle when you want to configure the bundle during run time. Configurable product bundles have products under a group. Additionally, the parent product is always configurable in the run time.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To convert static bundle to a configurable bundle:	Manage Product Catalog
To use the Structure tab:	ARC Access permission set

To change a static bundle product to a configurable bundle product, these requirements must be met:

All child product components are present under groups and not directly under the root product.
Configure During Sale for the root product is set to Allowed.
From the Product listing page, click the root static bundle product.
Navigate to the Structure tab for this product.
Ensure that all products are under a product group and not directly under the root static product.
From the Structure tab, add a Product Group component under the root bundle product.
Click every product that is directly under the root product.
In the right panel, click Edit Relationship.
On the Edit PRC page, in the Group field, select the newly created product group or another group to which this product can be added.
Save the changes.
Perform these steps for all the products that are directly under the root product and not under a group.
Refresh the Structure tab.
Ensure that all products are now under groups.
Finally, edit the root product bundle.
Change the value of Configure During Sale to Allowed.
Save your changes.

=== ARTICLE: ind.product_catalog_configure_apex_hooks_in_a_product_discovery_procedure_plan.htm ===
---
article_id: ind.product_catalog_configure_apex_hooks_in_a_product_discovery_procedure_plan.htm
title: Configure Apex Hooks in a Product Discovery Procedure Plan
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_apex_hooks_in_a_product_discovery_procedure_plan.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.pricing_customize_pricing_procedures_with_apex_hooks.htm
fetched_at: 2026-09-04
---

# Configure Apex Hooks in a Product Discovery Procedure Plan

Use Apex sections in a Product Discovery procedure plan to run custom pricing logic, such as fetching prices from an external system. The order of Apex and Pricing sections determines how prices are applied. You can include multiple Pricing and Apex sections, but only one Qualification section.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create, update, and delete pricing procedures:	Salesforce Pricing Design Time User or Procedure Plan Access
To use pricing procedures:	Salesforce Pricing Run Time User
To define, edit, delete, set security, and set version settings for Apex classes:	Author Apex
Make sure the Apex class implements RevSignaling.SignalingApexProcessor.
Confirm that the class is packaged and available in your org namespace.
Make sure the External ID field is populated for your Product2 records if used in pricing.
Only one Qualification section is supported. You can include multiple Pricing and Apex sections.
To create a procedure plan and add base sections, see Creating Procedure Plan Definitions Using Templates.
From Setup, in the Quick Find box, enter Apex, then select Apex Classes.
Select New to create a new Apex class.
In the class editor, enter the class definition and save the definition. When you activate a procedure plan, Salesforce checks the order of Qualification, Pricing, and Apex sections. Activation fails if the order doesn’t follow the supported sequence.
EXAMPLE

Examples of supported and unsupported section orders:

Supported: Apex , Pricing , Apex
Supported: Apex , Apex , Pricing
Supported: Apex , Apex , Pricing , Apex , Apex
Supported: Apex , Apex , Pricing , Pricing , Apex , Apex
Unsupported: Apex , Pricing , Apex , Pricing , Apex
Unsupported: Apex , Pricing , Apex , Apex , Pricing , Apex

=== ARTICLE: ind.product_catalog_configure_decimal_support_for_unit_level_prices.htm ===
---
article_id: ind.product_catalog_configure_decimal_support_for_unit_level_prices.htm
title: Configure Decimal Support for Unit-Level Prices
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_decimal_support_for_unit_level_prices.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Configure Decimal Support for Unit-Level Prices

Improve pricing accuracy by configuring up to six decimal places for unit-level rate and currency fields. Show precise values for unit prices, list prices, and discounts across product discovery, quote, and order pages. Standard summary and total fields retain their default decimal settings.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To configure decimal support:	Product Catalog Management Designer
From Setup, in the Quick Find box, enter Revenue Settings, and then select Revenue Settings.
Turn on Decimal Places for Unit Price.
Enter the number of decimal places to show in unit-level price fields. The default is 2. Supported values are 2 through 6.
EXAMPLE :

How this setting works:

Trailing zeros are removed: If a price doesn't need the extra decimal places, the system will not pad it with zeros. For example, 2.85 is shown as 2.85, not 2.8500000.
Editing vs. Viewing: When you click a price field to edit it, you see the full, exact value stored in the database. When you click out (view mode), the system applies your decimal display setting.
Nearest rounding rule: If the actual value in your database has more decimal places than your configured Decimal Value the shown number rounds to the nearest decimal (rounding up or down as appropriate).

How the prices appear when the Decimal Value is six.

How This Setting Works
ACTUAL VALUE	DISPLAY VALUE	EXPLANATION
88.12	88.12	No trailing zeros: The system doesn't add extra zeros to reach six decimal places.
88.1	88.10	Minimum decimals enforced: The system requires a minimum of two decimal places, so a zero is added.
88.123456	88.123456	Exact match: The value has exactly six decimal places.
88.1234567	88.123457	Round up: The seventh decimal is seven, so the sixth decimal rounds up.
88.1234564	88.123456	Round down: The seventh decimal is four, so the sixth decimal remains the same.

Here's a list of fields that support the extended decimal value for unit prices, list prices, and discounts across product discovery, quote, and order pages.

Supported Fields
PAGE	FIELDS
Quote	
Applied Discount
Applied Discount Amount
Discount

Quote Line Group	
Discount
Discount Amount
Margin
Margin Amount
Unit Price Uplift

Quote Line Item	
Discount (Amount)
Discount (Percentage)
List Price
Margin Amount
Net Unit Price
Partner Discount Percent
Partner Unit Price
Unit Cost
Sales Price
Unit Price Uplift

Order	
Applied Discount
Applied Discount Amount
Discount Percent

Order Item Group	
Discount
Discount Amount
Margin
Margin Amount
Unit Price Uplift

Order Item	
Discount (Amount)
Discount (Percentage)
List Price
Margin
Margin Amount
Gross Unit Price
Net Unit Price
Pro Forma Billing Period Amount
Partner Unit Price
Partner Discount Percent
Unit Cost
Reference Price
Unit Price Uplift

=== ARTICLE: ind.product_catalog_configure_dynamic_product_facets.htm ===
---
article_id: ind.product_catalog_configure_dynamic_product_facets.htm
title: Configure Dynamic Product Facets
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_dynamic_product_facets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_faceted_search.htm
fetched_at: 2026-09-04
---

# Configure Dynamic Product Facets

With Dynamic Product Facets, your users can find products faster on the Product Discovery List page. Dynamic Product Facets automatically selects, orders, and shows the most relevant facets, including the category facet.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To configure dynamic facets:	

Manage Product Index and Search

AND

View Product Catalog

From Setup, in the Quick Find box, enter Product Discovery, and then select Product Discovery Settings.
Enable dynamic product facets.

=== ARTICLE: ind.product_catalog_configure_filterable_fields_attributes.htm ===
---
article_id: ind.product_catalog_configure_filterable_fields_attributes.htm
title: Configure Filterable Fields & Attributes
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_filterable_fields_attributes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_faceted_search.htm
fetched_at: 2026-09-04
---

# Configure Filterable Fields & Attributes

Specify the fields and attributes that your sales reps can use as filters on the product discovery product list page. By configuring filterable fields and attributes, you help sales reps quickly narrow down search results to find the products they need.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To build and rebuild indexes:	

Manage Product Index and Search

AND

View Product Catalog

Let us explore faceted search by taking an example. The following products and attributes are identified as filterable.

Sun Compound: Powder Weight

Zon Compound: Powder Weight and Gel Quantity

Kyocea Compound Premium: Powder Weight and Gel Quantity

From the Product Catalog Management app’s home page, click Index and Search Configuration.
Click Manage Fields & Attributes tab.
Click Edit.
Select Gel quantity and Powder Widget attributes as Filterable.
You can select a combined total of up to 87 searchable and filterable fields and attributes. There is no specific limit for each type, provided the combined total doesn't exceed 87.
Click Next.
Select the fields and adjust the filter order using the respective arrows. Use the left and right arrows to select or deselect fields. Use the up and down arrows to adjust the filter order. The order that you select is the order in which the facets are displayed on the product discovery product list page.
Save your changes.

You must rebuild the index after you set up, update, or delete the field browse options.

Click Indexes tab and click Rebuild Index.
Select Full Index Rebuild and click Rebuild.
Enable Use Indexed Data for Product Listing and Search.
From Setup, in the Quick Find box, enter Product Discovery Settings and select it.
Enable Use Indexed Data For Product Listing and Search.

=== ARTICLE: ind.product_catalog_configure_partial_search.htm ===
---
article_id: ind.product_catalog_configure_partial_search.htm
title: Configure Partial Search
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_partial_search.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_partial_search.htm
fetched_at: 2026-09-04
---

# Configure Partial Search

Find products more efficiently by searching with partial product codes or product SKUs.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To edit a product:	Manage Product Catalog
From the Product Catalog Management app's home page, click Index and Search Configuration.
Click the Index Settings tab.
In the Search section, turn on Partial Search.
Save your changes.
Rebuild the index to apply these changes.
Click the Indexes tab, and then click Rebuild Index.
Select Full Index Rebuild, and then click Rebuild.

=== ARTICLE: ind.product_catalog_configure_prodoct_catalog_management_cache.htm ===
---
article_id: ind.product_catalog_configure_prodoct_catalog_management_cache.htm
title: Configure the Product Catalog Management Cache
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_prodoct_catalog_management_cache.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Configure the Product Catalog Management Cache

Store frequently requested product details in a dedicated cache for faster retrieval. You can then access product details without reloading them from the source every time. When product details change, the system detects the updates and regenerates the cache. If a user requests information for a product that isn’t in the cache, the system fetches the information from the database and saves it to the cache for future requests.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To configure the product catalog management cache:	Product Catalog Management Designer with the Product Catalog Management permission set

Before you begin:

You have disabled Data Translation, see Set Up Data Translation in Product Catalog Management
From Setup, in the Quick Find box, enter Product Discovery, and then select Product Discovery Settings.
Enable product catalog management cache.

When product details change, the system automatically detects the updates and recursively identifies all impacted products. It then invalidates their cache, ensuring subsequent requests retrieve the latest information and regenerate the cache automatically.

IMPORTANT If your changes impact a small number of products, rely on the automated cache to detect and regenerate those records. If you import or update products in bulk, or if your changes impact a large number of products, use Refresh Existing Products or Cache All Products instead. These options let you manage cached product details manually so you see your changes immediately. The time to automatically regenerate the cache increases as the number of impacted products grows.
Manage Product Details in the Cache

Store frequently requested product details in a dedicated caching layer to ensure faster retrieval. Manage the cached product details by either refreshing, updating, or clearing the cache.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To manage product details in the cache:	Product Catalog Management Designer
From Setup, in the Quick Find box, enter Flows, and then select Flows.
Create a flow, and add Runtime_industries_epc_ProductCatalogCacheRefresh batch job as an action element.

For example, Create a Schedule-Triggered Flow. Add an Action element and edit the element to add Runtime_industries_epc_ProductCatalogCacheRefresh batch job.

To manage the product details, click the action element to view the cache management options. Select Clear Cache to empty the cache, Refresh Existing Products to refresh current records, or Cache All Products to sync all products from the database, including new ones. Use these options to resolve data discrepancies or see the latest product changes.

Save and activate the flow.

To check the flow status, from Setup, in the Quick Find box, find and select Monitor Workflow Services. For more information, see Monitor Your Batch Jobs

When a user requests information for a specific product, the system first checks the cache. If the details are found there, they are retrieved instantly. If not, the system fetches the information from the database and saves it to the cache, ensuring the data loads much faster for future requests.

=== ARTICLE: ind.product_catalog_configure_product_attributes.htm ===
---
article_id: ind.product_catalog_configure_product_attributes.htm
title: Configure Product Attributes in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_product_attributes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_products.htm
fetched_at: 2026-09-04
---

# Configure Product Attributes in Revenue Management

Products that are based on a product classification inherit all the attributes from the product classification. You can configure the inherited attributes to make them product-specific. You can override the configured and inherited attributes in the context of a product bundle.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To configure product attributes:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Products.
From the product list view page, click the product.
Navigate to the Attributes tab.
To configure a product attribute that is inherited from the product classification, click  next to an inherited attribute, and then click Configure.
In the New Product Attribute Definition window, edit the fields as necessary.
To display attributes of currency, number, and percent data types as sliders at run time, configure product attributes of these data types and specify these details:
Select Slider under Display Type.
Enter a minimum value.
Enter a maximum value.
Enter a step value.
You can display attributes of the currency, number, and percent data types as sliders in the user interface at run time. Instead of typing in a number, or using increment buttons, drag the slider on a predefined scale to adjust the attribute values. The slider is positioned at the default value. You can slide the attribute value in increments or decrements of the step value. The step value must be greater than zero. Additionally, the difference between the maximum value and minimum value must be exactly divisible by the step value. You must always define the default value, minimum value, and maximum value for an attribute when the attribute’s display type is slider.
Enter a default value.
Save your changes.
EXAMPLE Consider an iPhone that has attributes such as model, color, and display. The iPhone has inherited all these attributes from the product classification Phones. When a user purchases this iPhone as part of the Apple phones product bundle, you want the iPhone to be available in red color by default. To create this configuration, you can override the default attribute value of color and set it to red for iPhone in the context of the Apple Phones bundle.

=== ARTICLE: ind.product_catalog_configure_product_field_search.htm ===
---
article_id: ind.product_catalog_configure_product_field_search.htm
title: Configure Product Field Search
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_product_field_search.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_field_search_in_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Configure Product Field Search

Give your users the option to quickly search for catalogs having more than 4 million products.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To build and rebuild indexes:	

Product Catalog Management Designer

From Setup, in the Quick Find box, enter Product Discovery, and then select Product Discovery Settings.
Enable product field search.

=== ARTICLE: ind.product_catalog_configure_search_options.htm ===
---
article_id: ind.product_catalog_configure_search_options.htm
title: Configure Searchable Fields & Attributes
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_search_options.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_index_and_search_of_product_catalog.htm
fetched_at: 2026-09-04
---

# Configure Searchable Fields & Attributes

Specify the indexed fields and attributes you want to be searchable by sales reps and customers to find relevant products.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To build and rebuild indexes:	

Manage Product Index and Search

AND

View Product Catalog

From the Product Catalog Management app’s home page, click Index and Search Configuration.
Click Manage Fields & Attributes tab.
Click Edit.
To enable users search for products by a specific field, choose the Searchable option next to that field.
Select the required fields in the Filterable column.
Only Picklist and Boolean fields can be filterable.
Click Next.
Select the fields and adjust the filter order using the respective arrows: use the left and right arrows to select or deselect fields, and the up and down arrows to adjust the filter order.
Save your changes.

You must rebuild the index after you set up, update, or delete the field browse options.

To rebuild the index after you update the field browse options:

Click Indexes tab and click Rebuild Index.
Select Full Index Rebuild and click Rebuild.
Search Limitations

Standard or custom fields on the Product object can be ‌searchable. Additionally, you can make the fields that are common to the Product Attribute Definition object and Product Classification Attribute objects ‌searchable.

You can select a combined total of up to 87 searchable and filterable fields and attributes. There is no specific limit for each type, provided the combined total doesn't exceed 87.

You can't make fields of these data types searchable:

Geolocation
Lookup Relationship
External Lookup Relationship
Auto Number
Formula
Checkbox
Date
Date/Time
Time
Text Area (Rich)
Text (Encrypted)

You can't make dynamic attributes of these data types searchable:

Checkbox
Date
Date/Time
Time
Use Indexed Data for Product Listing and Search

To use indexed information when users browse and search for products, enable the Use Indexed Data For Product Listing and Search setting.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To enable using indexed data from product listing and search:	
Customize Application system permission
Product Catalog Management Designer permission set

From Setup, in the Quick Find box, enter Product Discovery Settings and select it.
Enable Use Indexed Data For Product Listing and Search.

=== ARTICLE: ind.product_catalog_configure_the_number_of_facets_displayed.htm ===
---
article_id: ind.product_catalog_configure_the_number_of_facets_displayed.htm
title: Configure the Number of Facets Displayed
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_configure_the_number_of_facets_displayed.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_faceted_search.htm
fetched_at: 2026-09-04
---

# Configure the Number of Facets Displayed

You can now define a facet limit to control the number of dynamic facets shown on your Product Discovery list page. In addition, you can also define the number of values shown for each facet. This feature overrides the default display, ensuring only the specified number of facets are visible.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To build and rebuild indexes:	

Manage Product Index and Search

AND

View Product Catalog

Before You Begin:

Check if the CommercesearchHighFacetlimit permission is set to true or false. If the permission is set to true, you can show a maximum of 35 facets. If the permission is set to false, you can show a maximum of 10 facets.

From Setup, in the Quick Find box, enter Flows and select it.
Select Discover Products.
In the flow builder, select Product List screen element.
Select Product List Page Container component. Update the Maximum number of Facets and Maximum Values per Facet fields to specify the number of facets and values per facet respectively. 
Save the changes.

=== ARTICLE: ind.product_catalog_considerations_custom_flow_for_browsing_and_adding_products.htm ===
---
article_id: ind.product_catalog_considerations_custom_flow_for_browsing_and_adding_products.htm
title: Customize the Product Browsing Experience
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_considerations_custom_flow_for_browsing_and_adding_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_discovery.htm
fetched_at: 2026-09-04
---

# Customize the Product Browsing Experience

To specify the information and options shown to your users during product discovery, override a preconfigured flow or use the Lightning App Builder to customize the experience.

REQUIRED EDITIONS
View supported products and editions.

Be sure to follow all the instructions in each section. To track your progress, bookmark this page for easy reference.

Override Flow for Product Discovery
Use the Discover Products flow to select a catalog and then add products from the catalog to their associated record pages. The Discover Products flow is readily available with Product Discovery, and you can customize the flow beyond the available capabilities to meet your business needs.
Customize Product Discovery in Lightning App Builder
Add product discovery components to supported pages and customize them to show only the information and options that your users need. For example, customize the Product List component to show additional fields that your users are interested in.
Product Discovery Component Properties
Use the Product Discovery component properties to show only the information and options that your users need.

=== ARTICLE: ind.product_catalog_considerations_while_assigning_attributes_to_product_classifications.htm ===
---
article_id: ind.product_catalog_considerations_while_assigning_attributes_to_product_classifications.htm
title: Considerations While Assigning Attributes to Product Classifications
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_considerations_while_assigning_attributes_to_product_classifications.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_assign_attributes_to_a_product_classification.htm
fetched_at: 2026-09-04
---

# Considerations While Assigning Attributes to Product Classifications

Here are a few scenarios you can run into when assigning attributes to product classifications.

ERROR	SCENARIO	REMEDIATION
We couldn’t assign the selected Attribute Categories to the Product Classification. Select a single category for attributes that are duplicated across categories.	No attributes have been assigned to the product classification so far. You’re now assigning attributes through attribute categories. The selected attribute categories have a few attributes in common.	Select one category that’s the preferred category for the common attributes and assign that category to the product classification. If the preferred category is different for multiple common attributes, resolve conflicts by first assigning individual common attributes to the product classification, and then by assigning the remaining attributes via an attribute category.
Some attributes from the attribute category were already assigned to this product classification. The unassigned attributes are now assigned to the product classification.	A few attributes (via some attribute categories) have already been assigned to the product classification. You’re now assigning more attributes through attribute categories. The selected attribute categories include attributes that have already been assigned to the product classification through other attribute categories. 	The attributes from the attribute category that weren’t already assigned to the product classification are now assigned to the product classification.
We couldn’t assign the selected attributes because they belong to more than one category. Select a single attribute to an attribute category combination.	A few attributes have already been assigned to the product classification. You’re assigning individual attributes to the product classification, but the selected attributes belong to more than one category. 	Select a single attribute to an attribute category combination and assign it to the product classification.

=== ARTICLE: ind.product_catalog_context_definitions_for_product_catalog_management.htm ===
---
article_id: ind.product_catalog_context_definitions_for_product_catalog_management.htm
title: Configure a Context Definition for Qualification Rules
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_context_definitions_for_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_qualification_rules.htm
fetched_at: 2026-09-04
---

# Configure a Context Definition for Qualification Rules

For qualification rules, context definitions pass product or product catagory data to your qualification rule procedures. The qualification procedure then evaluates the qualification of products or product categories and returns the qualification or disqualification results back to the context definition.

REQUIRED EDITIONS
View supported products and editions.

When building a qualification rule, you must map your evaluation criteria in the qualification context definition. However, before you can map the data, you must extend the built-in ProductDiscoveryContext context definition.

TIP

Before you extend the built-in context definition, check to see if there's an extended context definition you can use. Some organizations already have a customizable context definition called BrowseProductsCtxDefinition.

You can view your existing context definitions in Setup | Context Service | Context Definitions.

To configure a context definition for your qualification rules, follow these instructions:

Extend the ProductDiscoveryContext Context Definition
To add the nodes, attributes, mappings, and tags for your qualification procedure, extend the ProductDiscoveryContext context definition.
Nodes and Attributes in the ProductDiscoveryContext Context Definition
The ProductDiscoveryContext context definition contains nodes and attributes that are used by and populated by Product Discovery, pricing procedure, qualification procedure, and object mapping.

=== ARTICLE: ind.product_catalog_conversion_of_bundle_products.htm ===
---
article_id: ind.product_catalog_conversion_of_bundle_products.htm
title: Convert Static and Configurable Product Bundles
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_conversion_of_bundle_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_bundled_products.htm
fetched_at: 2026-09-04
---

# Convert Static and Configurable Product Bundles

Change a static bundled product to a configurable bundled product when you want to configure the product bundle during run time. You can also change a configurable bundled product to a static bundled product when you don’t want users to configure the product bundle during run time.

REQUIRED EDITIONS
View supported products and editions.
NOTE

While you can change a static bundled product to a configurable bundled product (or vice versa), you can’t change a simple products to bundled products (or vice versa).

Also, changes to the Configure During Sale field value affects the run-time configurability behavior of the product. Ensure that you correctly configure your products.

Change a Static Bundle Product To a Configurable Bundle Product
You can change a static product bundle to a configurable product bundle when you want to configure the bundle during run time. Configurable product bundles have products under a group. Additionally, the parent product is always configurable in the run time.
Change a Configurable Bundle Product to a Static Bundle Product
You can change a configurable bundle product to a static product bundle when you don’t want to configure the bundle during run time. You can't configure products in a static product bundle during run time. Every bundle component is present in the bundle by default and can’t be removed. You can’t change the child component quantity in the run time. Every attribute of every product component has a default value.

=== ARTICLE: ind.product_catalog_create_a_catalog.htm ===
---
article_id: ind.product_catalog_create_a_catalog.htm
title: Create a Catalog
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_catalog.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_catalogs.htm
fetched_at: 2026-09-04
---

# Create a Catalog

Define your product offerings in Product Catalog Management with product catalogs. Catalogs enable efficient organization and management of all the products your business sells. You must create at least one product catalog.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To create a catalog:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Catalogs.
From the catalogs list view page, click New.
In the New Catalog window, enter these field values:
Enter a name and description for the catalog.
Enter a unique catalog code.
Select an effective start and end date.
The effective start date is the date and time when the catalog becomes available to users. The effective end date is the date and time after which the catalog is no longer available to users.
Select the type of catalog: Sales or Service Process. A Sales catalog is a catalog for products, while a Service Process is a catalog for a suite of services.
Save your changes.
SEE ALSO
Create Catalog Categories and Subcategories

=== ARTICLE: ind.product_catalog_create_a_product_classification.htm ===
---
article_id: ind.product_catalog_create_a_product_classification.htm
title: Create a Product Classification
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_product_classification.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_classifications.htm
fetched_at: 2026-09-04
---

# Create a Product Classification

A product classification is a template that you use to create products with similar characteristics. Product classifications are the primary tool for assigning attributes to products.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create a product classification:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Product Classifications.
On the Product Classifications list view page, click New.
In the New Product Classification window, enter the product classification name, code, and status.
NOTE You can change the status of a draft product classification to active, however you can change the status of an active product classification only to inactive.
Save your changes.

After you create a product specification, you can assign attributes to it. See Assign Attributes to a Product Classification.

SEE ALSO
Products
Dynamic Attributes

=== ARTICLE: ind.product_catalog_create_a_product_ramp_segment.htm ===
---
article_id: ind.product_catalog_create_a_product_ramp_segment.htm
title: "Prerequisites: Ramp Deals for Lines"
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_product_ramp_segment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.setting_up_ramp_deals.htm
fetched_at: 2026-09-04
---

# Prerequisites: Ramp Deals for Lines

Complete these essential setup steps before configuring your legacy line-item ramp deals.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To create a product ramp segment:	Manage Product Catalog Management
In Setup, find and select Revenue Settings. Turn on Ramp Deals for Lines in Quotes and Orders.
For each product you want to make eligible for ramp deals, create a product ramp segment in Product Catalog Management.
You can only use static simple and configurable simple products.
Assign a term-defined product selling model to the product first.
Segment types are Yearly, Custom, and Free Trial.
A product can have only one ramp segment of the same segment type.

=== ARTICLE: ind.product_catalog_create_a_product_selling_model.htm ===
---
article_id: ind.product_catalog_create_a_product_selling_model.htm
title: Create a Product Selling Model
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_product_selling_model.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_selling_model.htm
fetched_at: 2026-09-04
---

# Create a Product Selling Model

Create product selling models for your products from the Product Catalog Management home page.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To create product selling models:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Product Selling Models.
On the Product Selling Model list view page, click New.
In the New Product Selling Model window, specify these details:
The product selling model name.
The selling model type.
If you selected Term-Defined or Evergreen selling model type, enter the length of the term and the unit of time.
To define a one year term-defined product selling model:
Selling Model Type: Term-Defined
Pricing Term: 1
Pricing Term Unit: Year
To define a monthly recurring evergreen product selling model:
Selling Model Type: Evergreen
Pricing Term: 1
Pricing Term Unit: Month
If you selected the Term-Defined selling model type and want the product to be renewed automatically, select Automatically Renew Asset by Default.

When sales reps or customers add a product to a quote or an order, this auto-renewal status is stored in the line item created for the product.

Sales reps and customers can edit the line item to adjust the auto-renewal status.

Transaction Management passes the status to subsequent stages. For example, when sales reps create an order from a quote, the auto-renewal status of quote line items is passed to the corresponding order line items.

Select a status for the selling model.
You can’t change the status of a product selling model back to draft after you’ve set the status to active or inactive.
Save your changes.

=== ARTICLE: ind.product_catalog_create_a_product_subclassification.htm ===
---
article_id: ind.product_catalog_create_a_product_subclassification.htm
title: Create a Product Subclassification
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_product_subclassification.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_classifications.htm
fetched_at: 2026-09-04
---

# Create a Product Subclassification

Create and manage product classification hierarchies up to three levels deep to enhance the product catalog’s structure. Subclassifications automatically inherit attributes from their parent, simplifying attribute management and reducing redundant work.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create a product subclassification:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Product Classifications.
From the Product Classifications list, select the product classification to which you want to add a subclassification.
Click the Subclassification tab, and then click New.
In the New Product Classification page, enter the product classification name, code, and status.
NOTE You can change the status of a draft product classification to active, however you can change the status of an active product classification only to inactive.
Save your changes.

After you create a product specification, you can assign attributes to it. See Assign Attributes to a Product Classification.

=== ARTICLE: ind.product_catalog_create_a_qual_rule_for_product.htm ===
---
article_id: ind.product_catalog_create_a_qual_rule_for_product.htm
title: Create Qualification Rule Criteria
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_qual_rule_for_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_qualification_rules.htm
fetched_at: 2026-09-04
---

# Create Qualification Rule Criteria

Create criteria using field data on your chosen Salesforce object that you want to use for qualification rules. The object can be one that you create, or one of the included qualification or disqualification objects.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To create a qualification rule:	Manage Product Catalog

To help illustrate how qualification rule criteria works, let's use an example. Imagine that we need to restrict sales of a certain chemical called PEST-1X to customers in California. We can use the Billing State field on the Account object as the qualification rule.

Therefore, we need a field for Billing State on our evaluation object. We can use the Product Disqualification object that's already included in our org.

Create the Product Disqualification Field

To create the custom field for Billing State on the Product Disqualification object:

Go to the Object Manager in Setup.
Find the Product Disqualification object.
Create a new text field called BillingState.
Set field visibility for your profiles and select a page layout to display the field.
Save your changes.

Now that you have a field to record your criteria, you must create Product Disqualification records for each product that you want to include in the rule evaluation.

Create a Product Disqualification Record

To create a Product Disqualification record to use in the rule evaluation:

Open the App Launcher and find Product Disqualifications.
Click New, and enter this field data:
Enter a product you wish to use in the Product field.
In our example scenario, you would enter PEST-1X.
For Effective Date, enter the current date.
For Effective To, eneter a date in the future.
Enter CA for the BillingState.
Save the record.

You now have a product disqualification record ready to use in your qualification rule. This record is referenced by the qualification rule decision table.

=== ARTICLE: ind.product_catalog_create_a_unit_of_measure.htm ===
---
article_id: ind.product_catalog_create_a_unit_of_measure.htm
title: Create a Unit of Measure
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_unit_of_measure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_decimal_quantity_support_in_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Create a Unit of Measure

Capture accurate product quantities by defining the number of decimal places the product supports, with specific rounding methodologies.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To create a Unit of Measure:	DecimalQuantityDesigntime

For billing purposes, the system converts all units of measure in the unit of measure class to the default unit of measure. The conversion factor equates one unit of measure to another and helps with conversion. For example, for the Weight unit of measure class, the default unit of measure is pounds (lbs). Then, all units of measure records with the Weight unit of measure class are converted to equate 1 unit to 1 pound. If the unit of measure is kilogram, the conversion factor is 2.2 as 1 pound consists ‌of 2.2 kilograms.

From the App launcher, find and select Units of Measure.
Click New.
In the Unit of Measure field, find and select New Unit of Measure.
Enter a name for the unit of measure.

It's recommended to assign meaningful names as they'll be displayed to users.

Enter a unit code and type.
Here are some sample unit code and type values that you can enter.
SAMPLE UNIT CODE	SAMPLE TYPE
Length	meters, feet, inches, and centimeters
Weight	kilograms, pounds, and ounces
Volume	liters, gallons, and cubic meters
Time	seconds, minutes, and hours, days
Digital	bytes, kilobytes, and megabytes
Enter the scale.
The scale specifies the number of decimal places.
Select a rounding method.
Available rounding methods are Up, Down, and Nearest.
Save your changes.

=== ARTICLE: ind.product_catalog_create_a_variation_attribute_set_in_product_catalog_management.htm ===
---
article_id: ind.product_catalog_create_a_variation_attribute_set_in_product_catalog_management.htm
title: Create a Variation Attribute Set in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_variation_attribute_set_in_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_product_variants_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Create a Variation Attribute Set in Product Catalog Management

Group product attributes, such as size or color, into an attribute set to apply them to products efficiently. Because a product can have multiple attributes, applying a set to one or more products rather than assigning individual attributes provides consistency across products.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create a variation attribute set:	Manage Product Catalog

To create an attribute set, first create the individual product attributes, and then group them. For example, if your variation parent is a phone that uses the attributes color, memory, and display. Grouping these attributes means that you only assign a single attribute set to the product instead of three separate attributes.

NOTE
You can include up to 5 variation attributes in an attribute set.
You can't modify an attribute set after adding it to a product.
Create a product attribute set.
From the object management settings for product attributes, go to Fields and Relationships.
Click New.
Select Picklist, and then click Next.
Enter the details.
Enter a name. For example, color.
Select Enter values, each value separated by a new line.
Enter the attribute values. For example, red, green, and blue.
Click Next.
Set field-level security for the picklist field, and then click Next.
Save your work.

To create more product attributes, repeat step 1.

Create a variation attribute set.
From the Product Catalog Management home page, click Variation Attribute Set.
Click New.
Enter the details.
Enter a name. For example, phone specifications.
Select the fields that you want to add to the attribute set. For example, select color and memory.
For Group By, select None.
Save your work.
SEE ALSO
Create a Variation Parent
Create a Variation Product

=== ARTICLE: ind.product_catalog_create_a_variation_parent.htm ===
---
article_id: ind.product_catalog_create_a_variation_parent.htm
title: Create a Variation Parent
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_variation_parent.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_product_variants_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Create a Variation Parent

Group related product variants and simplify your catalog management. The parent variant stores shared attributes across a product’s different variants to eliminate redundant data entry for admins. Sales reps go to this parent variant in product discovery before selecting the exact specifications a customer needs.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create a variation parent:	Manage Product Catalog
From the Product Catalog Management home page, click Products.
Click New Variation Parent.
Select the Product Attribute Set that you want to add to this variation parent.
Enter a name.
Save your work.

=== ARTICLE: ind.product_catalog_create_a_variation_product.htm ===
---
article_id: ind.product_catalog_create_a_variation_product.htm
title: Create a Variation Product
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_a_variation_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_product_variants_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Create a Variation Product

Define specific, sellable configurations of a parent product. Each variation product represents a unique set of attribute values and has its own product code.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create a variation parent:	Manage Product Catalog

Consider a variation product that is a child of a Phone variation parent. The variation product uses the Phone specification attribute set, which includes these attributes: color (Red, Green, Blue), Memory (128 GB. 256 GB, 512 GB), and display (1024 pixels, 2048 pixels). An example of a variation product can be a phone with the values Red, 128 GB, and 1024pixels.

From the Product Catalog Management home page, click Products.
Click the variation parent that you want to create variation products for.
Click the Variations tab.
Click Create Variation.
Select the variation attributes. For example, Red, 256 GB, 1024 pixels.
Enter a name. For example, Phone red-128GB.
Save your work.
To create more variation products, repeat steps 4 through 7. For example, you can add more variations, such as Phone green-128GB, phone blue-256GB, and many more.

=== ARTICLE: ind.product_catalog_create_and_deploy_assessment_forms_guided_product_selection.htm ===
---
article_id: ind.product_catalog_create_and_deploy_assessment_forms_guided_product_selection.htm
title: Create and Deploy Requirement Assessment Forms for Guided Product Selection
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_and_deploy_assessment_forms_guided_product_selection.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_guided_product_selection.htm
fetched_at: 2026-09-04
---

# Create and Deploy Requirement Assessment Forms for Guided Product Selection

For each requirement that you want to provide guidance for, create a set of questions, add the questions to a form, add logic to the form, and deploy the form. When your users (such as sales reps and customers) answer these questions, Guided Product Selection uses the answers to show the most suitable products.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create and deploy assessment forms:	
Product Catalog Management Designer permission set
Create Assessment Questions
From the Product Catalog Management app’s home page, click Assessment Questions.
Create questions with Select as the data type. See Create Questions.
IMPORTANT It’s recommended that you add up to 4 response values.
Create a Form
Create a form by using one of these methods.
From the Assessment Questions page, select the assessment questions, and then click Select Questions. Then define the assessment steps.
From the Product Catalog Management app’s home page, click Create Form. Then select the assessment questions and define the assessment steps.
See Create a Form.
Click Build Omniscript.
In the Select Discovery Framework Usage Type window, select Guided Product Selection and then click Save.
IMPORTANT When users use guided product selection, only activated forms whose usage type is Guided Product Selection appear.
The form is created and appears on the Omniscripts tab.
Configure and Deploy a Form
From the Product Catalog Management app’s home page, click Omniscripts.
To add a description that appears to users when they use Guided Product Selection, click Edit and then enter a description.
NOTE All the Omniscript forms are available to users from all the catalogs. So, in the description, it’s recommended that you specify the name of the catalog from which a form must be used.
Configure the Omniscript form to specify the necessary logic. See Build the Layout of a Form.
IMPORTANT We recommend that you configure logic such that a maximum of 5 questions appear to users at run time.
For each step, in the Step Properties section of the Properties tab, deselect Allow Save for Later.
At run time, Guided Product Selection doesn’t support saving partially complete Omniscript forms and completing them later.
Delete the Save-Responses remote action element.
From the Build tab, in the Omniscript section, drag the ProductGuidedSelectionIntegration Omniscript to the canvas and ensure that it’s the last element.
The ProductGuidedSelectionIntegration Omniscript saves responses, and makes sure that the message framework and remote class are configured properly.
If needed, preview the form. See Preview a Form.
Activate and deploy the form. See Activate and Deploy the Form.

After the form is activated and deployed, it’s available to users when they click the Guide Me button on the Product List component. For example, users click the View Catalogs quick action to open the Product List component, and then click the Guide Me button to access the forms.

=== ARTICLE: ind.product_catalog_create_bundled_products.htm ===
---
article_id: ind.product_catalog_create_bundled_products.htm
title: Create Bundled Products
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_bundled_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_products.htm
fetched_at: 2026-09-04
---

# Create Bundled Products

Bundled products are a group of products that are sold together as one unit. You can create static or configurable bundled products.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To create products:	Manage Product Catalog
To use the Structure tab:	ARC Access permission set

For static products, you can’t add or remove child products, alter product quantities, or configure product attributes at run time. For configurable products, you can add or remove child products, alter product quantities, and configure product attributes at run time.

To create a bundled product, follow these instructions:

From the Product Catalog Management app’s home page, click Products.
From the product list view page, click New.
Select a record type. The record type options appear only if your product designer has set up product specification types and product specification record types. The specification type field in the product takes the value of the product specification type associated with the record type.
In the New Product window, specify the following values:
Enter a name and description for the product.
Select Bundle under Product Type. This is what makes the product a bundled product.
To make the product available for purchase, select Active.
To create a configurable product bundle, select Allowed under Configure During Sale.
To create a static product bundle, select Not Allowed.
To add a unit of measure, select a unit of measure.
If you can sell this product only when it's combined with other products, select Sell only with other products.
To assign product attributes, select a product classification using the Based On field.
NOTE You can select only an active product classification.
In the Display URL field, enter a URL that leads to a product image linked to an external data source. The product image appears on the product list and product details page.
Select Is Assetizable if the product instance must persist and become a customer asset after the customer purchases it. The default value is true.

The value of Is Assetizable on the root product of a product bundle applies to all child products in the bundle. For example, if Is Assetizable is selected on the root product, then every child product in the bundle is assetizable irrespective of the Is Assetizable value on the child product.

Select the date and time when the product becomes available for sale under Availability Date.
Select a date and time after which the product can’t be sold under End Of Life Date.
Select a date and time after which a product isn’t supported, ordered, or maintained under Discontinued Date.
Select a decomposition scope that determines the number of instances of fulfillment order line items to generate for the product when the order is submitted.
If you want the quantity of the fulfillment order line items to always be one, select Always One under Fulfillment Quantity Calculation Method. If you want the quantity of fulfillment order line items to be aggregated from the source line items, select Aggregate under Fulfillment Quantity Calculation Method.
If needed, select a type of usage model for a product or service. Anchor is the main subscription product or service. Pack is the add-on product or service that grants additional usage resources for consumption.
Save your changes.

After you create a product, you can assign it to catalog categories and subcategories. You can also configure product attributes. You can also add components to the bundle structure.

Create a Bundled Product Structure
After you create a bundled product (static or configurable), use the Structure tab in the bundled product to add child components such as groups, products, and product classifications.
Override Product Component Attributes in Bundles
You can override the attributes of product components in the context of the product bundle.
Include or Exclude Picklist Values in Overridden Product Attributes
Override product attributes to create the override in the context of a product bundle. To include or exclude specific picklist values for overridden product attributes of the data type picklist, use Include or Exclude Picklist Values. The included picklist values are available at run time while excluded picklist values are unavailable at run time.
Define Quantity Limits for Bundled Products
For bundled products businesses can limit, or require, the quantity of items purchased. For example, an airline that offers up to two companion fares for each frequent flyer customer. In Product Catalog Management, use local and group cardinality to create these quantity limitation rules.
Exclude Bundle Components From Product Selection at Run Time
To make certain products, groups, or classifications unavailable for selection at run time, you can exclude them from the product bundle. This exclusion doesn’t delete the product, it only hides the product from the user at run time. Exclusions are in the context of the root product bundle that you’re in.
Manage Validations for Product Bundles
As product bundles grow over time, tracking the number of components and ensuring that every component meets the cardinality and structural requirements can become challenging. Validate Product Definition runs on-demand checks against your entire bundled product to ensure compliance. The validations also suggest corrective actions to help maintain the integrity and accuracy of your product configurations.
Convert Static and Configurable Product Bundles
Change a static bundled product to a configurable bundled product when you want to configure the product bundle during run time. You can also change a configurable bundled product to a static bundled product when you don’t want users to configure the product bundle during run time.
Manage and View Constraints for a Product
Maintain a unified user experience for product definitions and constraint rules. Manage, view, and activate all constraints associated with a product from a single location.
SEE ALSO
Creation Of a Bundled Product Structure
Assign Products to Catalog Categories and Subcategories
Configure Product Attributes
Preview the Product Configurator

=== ARTICLE: ind.product_catalog_create_catalog_categories_and_subcategories.htm ===
---
article_id: ind.product_catalog_create_catalog_categories_and_subcategories.htm
title: Create Catalog Categories and Subcategories
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_catalog_categories_and_subcategories.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_catalogs.htm
fetched_at: 2026-09-04
---

# Create Catalog Categories and Subcategories

Organize and group products in your catalog by creating catalog categories and catalog subcategories. Assign products to more than one catalog category and subcategory.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create catalog categories and subcategories:	Manage Product Catalog

Use the Categories tab for a hierarchical view of categories. To create a product category, follow these instructions:

From the Product Catalog Management app’s home page, click Catalogs.
From the catalogs list view page, click the catalog that you want to create a catalog category for. 
Click Categories.
Click Create Category.
In the New Category window, enter these field values:
Enter a name and description for the catalog category.
The Catalog field is auto-populated with the catalog name.
Select a parent category for the catalog category.
If the category you’re creating is the first category in the hierarchy, leave the parent category field blank.
To show the catalog category as a navigational breadcrumb at runtime, select Show In Menu.
This functionality isn't available in the Product Discovery user interface, however, the Product Discovery APIs can access this field.
Enter the sort order of the category in the hierarchy.
The sort order determines the order in which the categories are shown to users as part of the purchase flow.
Enter a category code.
Save your changes.
You can create more categories from the Categories tab. To update the category order, click Sort .
To add a subcategory, click  next to the category and click Add Subcategory.
Enter a name, description, code, and sort order for the subcategory.
The Catalog and Parent Category fields populate automatically.
To show the subcategory as a navigational breadcrumb at runtime, select Show In Menu.
Save your changes.
To reorganize the order in which subcategories appear under a category, click  next to a category and click Update Subcategory Order.
Drag and drop the subcategories into the order you want.
Save your changes.
SEE ALSO
Assign Products to Categories and Subcategories

=== ARTICLE: ind.product_catalog_create_decision_table_that_uses_custom_evaluation_object.htm ===
---
article_id: ind.product_catalog_create_decision_table_that_uses_custom_evaluation_object.htm
title: Create a Decision Table That Uses a Custom Evaluation Object
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_decision_table_that_uses_custom_evaluation_object.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_decision_tables_for_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Create a Decision Table That Uses a Custom Evaluation Object

If you use a custom object to store the evaluation criteria, create a decision table without using the templates.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create a qualification rule:	Manage Product Catalog
To use a decision table:	Rules Engine Runtime

Before you create a decision table that uses a custom evaluation object, ensure that the object has certain mandatory fields. You use the mandatory fields to populate the rule criteria and create decision tables. You also use the mandatory fields in the qualification rule procedure. Based on the qualification rule type, the required mandatory fields are:

Product Qualification: ProductId of type FOREIGNKEY(Product2) and IsQualified of type BOOLEAN.
Product Disqualification: ProductId of type FOREIGNKEY(Product2) and IsDisqualified of type BOOLEAN.
Product Category Qualification: CategoryId of type FOREIGNKEY(Category) and IsQualified of type BOOLEAN
Product Category Disqualification: CategoryId of type FOREIGNKEY(Category) and IsDisqualified of type BOOLEAN
From the Product Catalog Management app’s home page, click Qualification Rules.
From the Qualification Decision Tables page, click New.
The Basic Details page appears.
On the Basic Details page:
Enter a name, API name, and description.
TIP Add the purpose of the decision table to the decision table name to specify whether the decision table is meant for qualification or disqualification. For example, if you’re creating a qualification decision table for furniture, name the decision table FurnitureQualify.
Select an application usage type.
To create a decision table for product qualification or disqualification, select Product Qualification. To create a decision table for product category qualification or disqualification, select Product Category Qualification.
Based on the number of records in your decision table, select a decision table type.
If the number of records in the decision table is less than 100,000, select

Standard

. If the number of records in the decision table exceeds 100,000, select

Advanced

.
Click Save & Next.
The Conditions & Results page appears.
Select a source object.
Skip the Related Objects field because rules are defined on only the source object.
To narrow down rows from the source object, add filters.
Click Source Filter.
To add a filter, click Add Filter, and then select a source object field, operator, and a value.
If you add more than one filter, use the Filter Logic field to specify the logic by using AND or OR.
To use the decision table for product qualification or disqualification, add the ProductId field with Equals as the operator. To use the decision table for product category qualification or disqualification, add CategoryId with Equals as the operator. In addition, add other fields that you want to use as input. In the Conditions section, add the fields that you want to use as input. To add a field as input:
Click Add Condition.
For Source Object Field, select the field name.
Select an operator.
The operator determines how a particular field from the business rule evaluates a record or a user-specified value.
If necessary, set the condition as optional.
To know about the permissible number of input and output fields, see Considerations for Creating Decision Tables.
Select a condition type.
When you use custom logic, the Number column indicates the sequence number of the fields. For example, if you have three input fields and you want to use custom logic that provides output when fields 1 and 2 match or when field 3 matches, specify the condition as: (1 AND 2) OR 3.
To use the decision table for product or category qualification, add the IsQualified field. To use the decision table for product or category disqualification, add the IsDisqualified field. In addition, add other fields that you want to use as the output. In the Results section, add all the fields that you want in the decision table output. To add a field as output:
Click Add Results.
In the Source Object Field, select the field name.
 Click Save & Next.
The Behaviours page appears.
In the Filter Result By field, select First Match.
If necessary, select an input or output field by which records must be sorted and then select the sort order.
To consider columns with null values during lookup, select Consider Null Values for Lookup.
See How Null Values Work in Decision Tables.
NOTE The Consider Null Values for Lookup option is available only when the decision table type is standard.
Click Save & Next.
The Preview & Save page appears.
On the Preview & Save page, review the information including the conditions and preview records, and then click Finish.
NOTE If you used custom fields in decision tables, then use change sets or package manager to first deploy the custom fields to your destination org before you deploy the decision tables.

=== ARTICLE: ind.product_catalog_create_dt_for_product.htm ===
---
article_id: ind.product_catalog_create_dt_for_product.htm
title: Create a Decision Table That Uses a Standard Evaluation Object
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_dt_for_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_decision_tables_for_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Create a Decision Table That Uses a Standard Evaluation Object

If you use Product Qualification, Product Disqualification, Product Category Qualification, or Product Category Disqualification objects to store the evaluation criteria, use predefined templates to easily create decision tables.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To create a decision table:	

Manage Product Catalog

AND

Rules Engine Designer


To use a decision table:	Rules Engine Runtime
From the Product Catalog Management app’s home page, click Qualification Rules.
From the Qualification Decision Tables page, click New.
The Basic Details page appears.
On the Basic Details page:
Enter a name, API name, and description.
TIP Add the purpose of the decision table to the decision table name to specify whether the decision table is meant for qualification or disqualification. For example, if you’re creating a qualification decision table for furniture, name the decision table FurnitureQualify.
Select an application usage type.
To create a decision table for product qualification or disqualification, select Product Qualification. To create a decision table for product category qualification or disqualification, select Product Category Qualification.
Select a template.
Click Save & Next.
On the Preview & Save page, click Finish.
Click Edit.
The Basic Details page appears.
Based on the number of records in your decision table, select a decision table type.
If the number of records in the decision table is less than 100,000, select Standard. If the number of records in the decision table exceeds 100,000, select Advanced.
Retain the application usage type.
Click Save & Next.
The Condition & Results page appears.
Retain the default source object.
NOTE Skip the Related Objects field because rules are defined on only the source object.
To narrow down rows from the source object, add filters.
Click Source Filter.
To add a filter, click Add Filter, and then select a source object field, operator, and a value.
If you add more than one filter, use the Filter Logic field to specify the logic by using AND or OR.
In the Conditions section, add the fields that you want to use as input. To add a field:
Click Add Condition.
In the Source Object Field, select the field name.
Select an operator.
The operator determines how a particular field from the business rule evaluates a record or a user-specified value.
If necessary, set the condition as optional.
To know about the permissible number of input and output fields, see Considerations for Creating Decision Tables.
Select a condition type.
When you use custom logic, the Number column indicates the sequence number of the fields. For example, you have three input fields and you want to use custom logic that provides output when fields 1 and 2 match or when field 3 matches, specify the condition as: (1 AND 2) OR 3.
In the Results section, ensure that the IsQualified field or the IsDisqualified field is available.
For a decision table used for product or category qualification, ensure that IsQualified is available. For a decision table used for product or category disqualification, ensure that IsDisqualified is available.
In the Results section, add other fields that you want in the decision table output. To add a field:
Click Add Results.
In the Source Object Field, select the field name.
Click Save & Next.
The Behaviours page appears.
In the Filter Result By field, select First Match.
If necessary, select an input or output field by which records must be sorted and then select the sort order.
To consider columns with null values during lookup, select Consider Null Values for Lookup.
See How Null Values Work in Decision Tables.
NOTE The Consider Null Values for Lookup option is available only when the decision table type is standard.
Click Save & Next.
The Preview & Save page appears.
On the Preview & Save page, review the information, including the conditions and preview records, and then click Finish.
NOTE If you used custom fields in decision tables, use change sets or package manager to first deploy the custom fields to your destination org before you deploy the decision tables.
SEE ALSO
Create a Decision Table
Decision Tables for Business Rules Engine
Decision Table Limits
Input Field Conditions in Decision Tables
Supported Data Types and Operators in Decision Tables

=== ARTICLE: ind.product_catalog_create_product_specification_type_and_product_specification_record_type.htm ===
---
article_id: ind.product_catalog_create_product_specification_type_and_product_specification_record_type.htm
title: Create Product Specification Type and Product Specification Record Type
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_product_specification_type_and_product_specification_record_type.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_specification.htm
fetched_at: 2026-09-04
---

# Create Product Specification Type and Product Specification Record Type

Ensure that your products have the terminology that’s unique to your industry. Use Product Catalog Management to define a specification type for the products that are specific to your industry and create corresponding product record types.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To create product specification type and product specification record type:	Manage Product Catalog
IMPORTANT Only Salesforce Admins can set up Specification Types.

See:

Create Record Types
Create Page Layouts

While you can use the specification types that are shipped out-of-the-box for your industry, you can also create custom product specification types. Additionally, you can use APIs to query products by product specification type.

Product specification types and product specification record types are optional configurations. You can create them while you set up Product Catalog Management.

NOTE

Products with a Commercial Product Specification Type, or with a null Product Specification Type, can be viewed in the Product Discovery flow.

Perform these steps only if you aren’t using an out-of-the-box specification type that your industry license provides.
From Setup, in the Quick Find box, enter Product Specification Type, and then select Product Specification Type.
Click New Product Specification Type.
Enter a name, description, and label for the product specification type and save your work.
NOTE You can translate the values of the label and description fields in the Product Specification Type Object.
From Setup, in the Quick Find box, search for Product Specification Record Type, and then click Product Specification Record Type.
Click New Product Specification Record Type.
Enter these details:
Enter a name and a label for the product specification record type.
Select the Product Specification Type that this record type is associated with.
Select None for products that don’t have a specification type.
Select a Record Type. If you haven’t created any record types on the Product object, see Create Record Types.
Ensure that the Record Type, Product Specification Type, and the Name are unique. You can associate only one product specification record type with a record type.
NOTE You can’t delete a product specification type that’s related to a record type on the product object.
Select Is Commercial when your product specification is commercial type. Keep Is Commercial deselected when the product specification is non-commercial type. When you create a product and select an associated record type, the correct specification type is updated on the product record.
NOTE You can’t update the IsCommercial field after creating the product specification record type.
Save your changes. 
SEE ALSO
Translate Metadata Labels
Create Simple Products
Create Bundled Products
Create Bundled Products

=== ARTICLE: ind.product_catalog_create_product_variants_in_revenue_cloud.htm ===
---
article_id: ind.product_catalog_create_product_variants_in_revenue_cloud.htm
title: Create Product Variants in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_product_variants_in_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Create Product Variants in Revenue Management

Use product variants to group related products that share a common identity but differ by specific characteristics. Instead of creating separate, disconnected entries in your catalog for every minor difference, variants help you organize these options logically under a single umbrella record.

REQUIRED EDITIONS
View supported products and editions.
Why Use Product Variants?

Managing a complex product catalog is overwhelming. Product variants offer several key benefits.

Streamlined catalog management: Avoid cluttering your catalog with hundreds of standalone entries. You can manage shared details in one place, such as the product descriptions or core features.

Accurate tracking and quoting: Every distinct variation maintains its own unique stock keeping unit (SKU) to ensure precise tracking for inventory, pricing, quoting, and revenue recognition.

Simplifed buyer experience: Users can configure a product by selecting the required options from a single interface, rather than searching through a massive catalog for a specific product.
Primary Components

A product variant structure consists of four primary components.

Variation Parent: The overarching record that groups the variations together. Variation parent is a structural template that holds shared information. A variation parent can’t be purchased. It only serves to organize its children.

Attributes: The defining characteristics that distinguish the variations from one another. Common attributes include size, color, storage capacity, or material.

Variation Attribute Set: A logical grouping of individual attributes (up to 5) that you apply to a variation parent. Rather than assigning individual attributes one by one, bundling them into a set ensures efficiency and structural consistency across your catalog.

Variation Product: The actual, purchasable record. It’s a child of the variation parent and represents one specific, unique combination of attribute values. Every variation product requires its own distinct SKU.

EXAMPLE : Selling a phone.

To understand how these constituents work together, consider a catalog offering a new smartphone.

Variation Parent: Phone (non-purchasable umbrella record)

Attributes: Individual traits such as memory (128 GB, 256 GB) and color (red, green)

Variation Attribute Set: Phone specifications (a grouping that contains the memory and color attributes, applied directly to the phone variation parent)

Variation Products: Based on the parent and the applied attribute set, the system houses the specific, purchasable child records. Each has its own SKU.

Phone - Red - 128 GB

Phone - Red - 256 GB

Phone - Green - 128 GB

Phone - Green - 256 GB

Turn On Product Variants
Enable product variation to create and manage variant products in Product Catalog Management and make them available for product discovery.
Create a Variation Attribute Set in Product Catalog Management
Group product attributes, such as size or color, into an attribute set to apply them to products efficiently. Because a product can have multiple attributes, applying a set to one or more products rather than assigning individual attributes provides consistency across products.
Create a Variation Parent
Group related product variants and simplify your catalog management. The parent variant stores shared attributes across a product’s different variants to eliminate redundant data entry for admins. Sales reps go to this parent variant in product discovery before selecting the exact specifications a customer needs.
Create a Variation Product
Define specific, sellable configurations of a parent product. Each variation product represents a unique set of attribute values and has its own product code.

=== ARTICLE: ind.product_catalog_create_qual_rule_procedure_for_product.htm ===
---
article_id: ind.product_catalog_create_qual_rule_procedure_for_product.htm
title: Create a Qualification Rule Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_qual_rule_procedure_for_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_qualification_rules.htm
fetched_at: 2026-09-04
---

# Create a Qualification Rule Procedure

A qualification rule procedure contains qualification procedure elements that evaluate the rules in a decision table. The procedure accepts a list of categories and products as input and returns the list of products and categories along with their qualification or disqualification information as output.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To create a qualification rule procedure:	Manage Product Catalog
To use a decision table:	Rules Engine Runtime
To create a context definition:	Context Service Admin

As part of your qualification rule design, you can choose to use an existing qualification rule procedure. Many organizations have an existing qualification rule that you can add to. Alternatively, you can choose to create a new qualification rule.

Before you begin, ensure that the context tags for all input variables (required and optional) and all output variables in the decision tables are mapped to the right objects in your context definition. See Add Context Mapping.

To create a qualification rule procedure, follow these instructions:

From the Product Catalog Management app’s home page, click Qualification Rules Procedures.
From the Qualification Procedures list view page, click New.
In the New Qualification Procedure window, specify these details:
Enter a name for the qualification procedure.
Select a usage type. To qualify and disqualify both products and product categories, select Product Qualification. To qualify or disqualify only product categories, select Product Category Qualification.
If you’re creating a qualification procedure for Product Discovery, select Product Qualification as the usage type. You can’t select procedures with Product Category Qualification in Product Discovery Settings. To qualify or disqualify categories in Product Discovery, add category-level elements to a Product Qualification procedure.
Select a context definition. Use the context definition selected on the Product Discovery Settings page.
Save your changes.
To open your qualification procedure in Expression Set Builder, on the Details tab, in the Qualification Procedure Versions section, click the name of the qualification procedure version.
For each element that you want to add, perform these steps.
To improve readability, we recommend that you add the elements for product category qualification and disqualification before the elements for product qualification and disqualification.
On the Expression Set Builder canvas, click the  and then select the element. You can also drag an element from the Elements panel.
TIP You can add multiple elements depending on the available decision tables. Make sure you add the correct decision table to the appropriate element. For example, if you have a qualification decision table Product Qualification DT, then associate the decision table with the Evaluate Qualification element.
Find and select the required lookup table, and then select the input and output attributes.
See Attribute Mapping in Qualification Rule Procedures.
Select the element, click , and make sure that Include in Output is selected.
Click , and enter a rank.
Enter a start date and time that’s later than or same as the effective from date and time of the context definition.
Save your changes.
To check if the variables that you entered are accurate, simulate the qualification rule procedure.
See Simulate and Activate a Qualification Rule Procedure.
Activate the qualification procedure.
Attribute Mapping in Qualification Rule Procedures
In your qualification rule procedures, you must map specific attributes from the context definition to the corresponding decision table fields based on the type of the qualification element. In addition, you must map your custom attributes that must be used to evaluate qualification.
SEE ALSO
Simulate and Active a Qualification Rule Procedure

=== ARTICLE: ind.product_catalog_create_simple_products.htm ===
---
article_id: ind.product_catalog_create_simple_products.htm
title: Create Simple Products
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_create_simple_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_products.htm
fetched_at: 2026-09-04
---

# Create Simple Products

Learn how to create simple products for your product catalog. Simple products are products that aren't bundled with other products. You can create static or configurable simple products.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To create a simple product:	Manage Product Catalog

For static products, you can’t add or remove child products, alter product quantities, or configure product attributes at run time. For configurable products, you can add or remove child products, alter product quantities, and configure product attributes at run time.

To create a simple product, follow these instructions:

From the Product Catalog Management app’s home page, click Products.
From the product list view page, click New.
Select a record type. The record type options appear only if your product designer has set up product specification types and product specification record types.
In the New Product window, specify these details:
Enter a name and description for the product.
Enter a product code.
Select None under Product Type. This makes the product a simple product.
IMPORTANT The Product Type field can't be changed after the record is created. If you select the wrong product type, you must create a new product with the correct type.
To create a configurable simple product, select Allowed under Configure During Sale.
To create a static simple product, select Not Allowed under Configure During Sale.
If you can only sell this product when it's combined with other products, select Sell only with other products.
To make the product available for purchase, select Active.
To add a unit of measure, select a unit of measure.
To assign product attributes, select a product classification using the Based On field.
In Display URL, enter a URL that leads to a product image linked to an external data source. The product image is displayed in the runtime.
If you want the product instance to persist and become a customer asset after purchase, select Is Assetizable. This option is selected by default.
Select the date and time when the product becomes available for sale under Availability Date.
Select a date and time after which the product can’t be sold under Discontinued Date.
Select a date and time after which a product isn’t supported, ordered, or maintained under End Of Life Date.
Select a decomposition scope that determines the number of instances of fulfillment order line items to generate for the product when the order is submitted.
If you want the quantity of the fulfillment order line items to always be one, select Always One under Fulfillment Quantity Calculation Method. If you want the quantity of fulfillment order line items to be aggregated from the source line items, select Aggregate under Fulfillment Quantity Calculation Method.
If needed, select a type of usage model for a product or service. Anchor is the main subscription product or service. Pack is the add-on product or service that grants additional usage resources for consumption. Commit is an agreement by a customer to use a minimum quantity of a product or service in a defined period.
Save your changes.

After you create a product, you can choose to assign it to catalog categories and subcategories. You can also configure product attributes if the product is based on a product classification.

SEE ALSO
Assign Products to Catalog Categories and Subcategories
Configure Product Attributes
Preview the Product Configurator

=== ARTICLE: ind.product_catalog_creation_of_a_bundled_product_structure.htm ===
---
article_id: ind.product_catalog_creation_of_a_bundled_product_structure.htm
title: Create a Bundled Product Structure
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_creation_of_a_bundled_product_structure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_bundled_products.htm
fetched_at: 2026-09-04
---

# Create a Bundled Product Structure

After you create a bundled product (static or configurable), use the Structure tab in the bundled product to add child components such as groups, products, and product classifications.

REQUIRED EDITIONS
View supported products and editions.
Product Bundle Components

Here's a product bundle structure with home furniture as the example, along with a description of each of the bundle components.

BUNDLE COMPONENTS	THINGS TO NOTE
Product Group (1)	
A group is mandatory in a configurable product bundle.
A group is optional in a static product bundle.
The root product can have multiple root groups or multiple products as its immediate level-one child components. A root group can have either multiple child groups, or multiple products, or a single product classification component as its immediate child component. A child group can contain a single product classification or multiple products.
A group under a configurable product bundle can contain multiple product components or one product classification component.
A group under a static product bundle can contain only multiple product components.

Product Components (2)	
You can add a product component under a product or under a product group.
A static product bundle can only have these child product components:
Static simple product
Static bundle product
A configurable product bundle can have these child product components:
Static simple product
Static bundle product
Configurable simple product
Configurable bundle product

Product Classification Components (3)	
You can add product classification components only under product groups.
You can add only one product classification under a product group.

When you add a product classification component to a group, all products that are based on the product classification are automatically added to the product bundle at run time. If you have multiple products based on a product classification, you don’t need to add each product as a product component to a group. Instead, you can add the product classification component that automatically adds all the products at run time.

To create a product bundle structure, follow these instructions:

Add Components to a Static Product Bundle
Static products are non-configurable at run time. That means you can’t add or remove child products, alter product quantities, or configure product attributes at run time. You can add product and product group components to a static product bundle. Product Group components are optional.
Add Components to a Configurable Product Bundle
You can add multiple groups, multiple product components, or one product classification component under a product group in configurable bundles.
Product Relationship Management in Revenue Management
Bundle products consist of components such as groups, products, and product classifications. These components are related to each other through product relationships.

=== ARTICLE: ind.product_catalog_customize_and_extend_the_product_catalog_management_home_page.htm ===
---
article_id: ind.product_catalog_customize_and_extend_the_product_catalog_management_home_page.htm
title: Customize and Extend the Product Catalog Management Home Page
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_customize_and_extend_the_product_catalog_management_home_page.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Customize and Extend the Product Catalog Management Home Page

Manage attributes, products, catalogs, and rules on the Product Catalog Management app’s home page. Your admin can use the Lightning App Builder to customize and extend the home page for your users.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To customize the Lightning App Builder Home page:	Manage Product Catalog
From the Product Catalog Management Home page, click Setup, and then click Edit Page.
In the Lightning App Builder, drag the Tabs standard component from the palette on the left, and drop it on the Lightning App Builder Canvas area in the middle.
Add and customize tabs as necessary. See Add and Customize Tabs on Lightning Pages Using the Lightning App Builder.
Drag the Grid (2) component onto the customized tab. Customize the number of grid columns, their width, and padding in the right panel.
Drag the Object Quick Links (3) component onto the grid columns.
In the panel on the right, enter the title, description, and Object API name for the object whose tile will appear on the Home Page. Keep the tile title and description short so that an increased grid column count doesn't impact readability. To determine the object API name, follow these steps:
In Lightning Experience, from Setup, open Object Manager, and search for the object that you want to add to the home page.
Copy the API name for that object and paste it in the Lightning App Builder.
In this example, the admin has added Account and Cases objects in the Grid columns.
Save your changes. 
As a Salesforce Admin, check that the intended users have appropriate access (create, read, update, and delete) to the object that you’ve added to the custom tile. 

To see the additional tab groups and any customizations you’ve made in your production home page, click Activate.

You can customize tabs such as Catalogs, Products, Attributes, and Rules in Product Catalog Management. You can also customize their grid components and object link components as necessary.

SEE ALSO
Lightning App Builder

=== ARTICLE: ind.product_catalog_customize_products_list_view.htm ===
---
article_id: ind.product_catalog_customize_products_list_view.htm
title: Customize Product Discovery in Lightning App Builder
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_customize_products_list_view.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_considerations_custom_flow_for_browsing_and_adding_products.htm
fetched_at: 2026-09-04
---

# Customize Product Discovery in Lightning App Builder

Add product discovery components to supported pages and customize them to show only the information and options that your users need. For example, customize the Product List component to show additional fields that your users are interested in.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To add and customize components:	Customize Application

When you customize pages on Salesforce Lightning Service Console, you can add components to only the supported pages.

The Product List component is supported only on catalog pages.
The Product Details, Product Bundle Details, and Product Attribute Details are supported only on product pages.

When you customize Experience Cloud sites, make sure that you create sites by using one of these templates.

Build Your Own (Aura)
Customer Service
Customer Account Service
Open the page editor.
If you’re using the Salesforce Lightning Service Console, open the supported page, and then from Setup, click Edit Page to open the Lightning App Builder.
If you’re using Experience Cloud sites, open Experience Builder and select the page that you want to add the component to. See Find Your Way Around Experience Builder.
From the Components panel, drag the component onto the page.
If you’re using Experience Builder, enter the record ID, if necessary.
The Record Id field is populated with {!recordId} by default.
If you add a component to a supported page and want the Record Id value to be automatically populated at run time based on the user-selected catalog, retain {!recordId} as the value.
If you add the component to any other page, enter the unique ID of a catalog in the Record Id field. See Locate the Unique ID of a Record in Salesforce.
To view the properties pane, click the component.
Specify the values for the properties.
Save your changes.
SEE ALSO
Activate Lightning Experience Record Pages
Product Discovery Component Properties

=== ARTICLE: ind.product_catalog_data_import_by_using_csv_files.htm ===
---
article_id: ind.product_catalog_data_import_by_using_csv_files.htm
title: Data Import Through CSV Files in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_data_import_by_using_csv_files.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_products.htm
fetched_at: 2026-09-04
---

# Data Import Through CSV Files in Product Catalog Management

Catalog admins and product designers can create records by importing CSV files into Product Catalog Management.

REQUIRED EDITIONS
View supported products and editions.

Summary of Steps

Clone the predefined Data Processing Engine templates that map column headers in CSV files to the object fields.
Allow the import of custom fields, customize the Data Processing Engine definitions. Catalog admins and product designers can download the predefined CSV templates, add columns for custom fields, and add data to the CSV template.
After the CSV file is ready, import the file to Product Catalog Management by using the definitions.
Set Up Data Processing Engine Definitions for Product Catalog Management

Product Catalog Management provides data processing engine definition templates that map columns in the CSV file templates to various Product Catalog Management objects. Use the templates to create data processing engine definitions. Import data to custom fields by customizing the data processing engine definitions to map the custom fields to the object fields.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To manage Data Processing Engine definitions:	
Customize Application
Modify All Data
Advanced CSV Data Import permission set

Before you begin:

Make sure that your org supports CSV import feature from Product Catalog Management.
Turn on Data Cloud.
To import data to custom fields, create custom fields on the objects. See Create Custom Fields.
To set up data cloud in sandbox, see Data Cloud in a Sandbox

To set up Data Processing Engine definitions, follow these instructions:

From Setup, in the Quick Find box, enter Data Processing Engine and select it.
Click the data process engine definition template that you want to use.
From the Save dropdown, select Save as.
Select Standard as the process type.
Save your changes.
To import custom fields:
In the Data Source node, add the column headers for custom fields as source fields.
See Use a CSV File as a Data Source.
NOTE The column header name can’t exceed 35 characters.
In each Writeback Object node, map the column headers from the CSV file to the custom fields of the object.
See Writeback Objects.
Save your changes.
Activate the Data Processing Engine definition.
Use CSV Files to Import Data in Product Catalog Management

Catalog admins and product designers can easily create records by importing data to Product Catalog Management by using CSV files and data processing engine definitions.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To download CSV templates:	Advanced CSV Data Import permission set
To upload CSV files:	Advanced CSV Data Import permission set
From the Product Catalog Management app’s home page, click Download CSV Templates, and then download the necessary template.
To import data into custom fields, add the field names used in the data source element of the data processing engine definition as the column headers.
Add data to the CSV template.
From the Product Catalog Management app’s home page, click Import Data.
The CSV File Import page appears. If you encounter an error on clicking Import Data, then the CSV File Import tab is likely hidden. Contact your Salesforce Admin to adjust the tab's visibility settings. See Make the CSV File Import Option Visible in Existing Orgs
From the Import dropdown, select Import using DPE Template.
Upload the CSV file, select the corresponding data processing engine definition, and then click Start Import.
NOTE  A Data Processing Engine definition processes data from each row. If a CSV file contains multiple objects with varying record counts, empty cells are sent to the Writeback Object node, and result in errors.
 If a CSV file has 30 product qualification records and 20 product disqualification records, then empty values are sent to the Product Disqualification Writeback Object node 10 times, and 10 errors are written to the failure log.
The import process begins. After the import process is complete, a log is generated and appears on the CSV File Import page.

=== ARTICLE: ind.product_catalog_data_translation.htm ===
---
article_id: ind.product_catalog_data_translation.htm
title: Translate Product Catalog Data
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_data_translation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Translate Product Catalog Data

Display product catalog data in the user’s configured language with data translation. Localize key Product Catalog Management (PCM) objects so buyers and sales teams can search, filter, and browse in their preferred language, improving accuracy and adoption.

PCM shows product and catalog data only in the org’s base language. This can make it difficult for international teams and customers who expect localized content.

Data translation solves this by letting admins add translated values for products, categories, and attributes. At runtime, users see product names, descriptions, and filters in their configured language, and they can search using local terms.

Data translation improves the global buying experience, reduces errors, and helps organizations expand into new markets with localized catalogs.

Translatable PCM Objects and Fields

OBJECT	TRANSLATABLE FIELDS
Product2	Name, Description, Help Text, and Picklist values
Product Category	Name and Description
Product Classification Attributes	Attribute name, Help text, and Picklist values
Dynamic Attributes (Picklist type only)	Display values of picklist entries

How Data Translation Works

Add translations in bulk (export, edit, and import files) or manually on each record.
Translations are included in the search index after a full reindex.
Localized values appear in product listings, filters, and search results.
Users can search with translated terms. For example, a French user can enter portable and see matching products.
IMPORTANT To use data translation, the Use Indexed Data for Product Listing and Search setting must be turned on in Index and Search Configuration. See Configure Search Options.
Set Up Data Translation in Product Catalog Management
Enable data translation and add supported languages so you can translate PCM entities into multiple languages. After you enable data translation, you can configure which languages to support and make them available in Product Catalog Management (PCM). Translations appear at runtime only after you configure Index Settings and run a full reindex.
Bulk Export and Import Translation Files
Export Product Catalog Management (PCM) translation data into STF or XLIFF files, add your localized values, and import the files back into Salesforce. Use this method to update large volumes of product, category, and attribute translations at once. After import, reindex the catalog so users see the localized values in product listings and search results.
Enter Translations Manually in the Translations Tab
Add translations directly on product, category, or attribute records using the Translations tab. Use this method for quick updates or small sets of localized values. After saving translations, reindex the catalog so users see the localized values in product listings and search results.
Use Flow Metadata to Enable Translated Product Catalogs
One method for enabling translated product catalogs is to download an updated version of the Discover Products flow and use its metadata to create a new flow.
Example: Provide a Localized French Buying Experience
This example shows how data translation changes the runtime experience for French users. See how translated values appear in catalogs, categories, products, and search results. Deliver localized catalogs without duplicate configurations. Buyers benefit from intuitive search and browsing in their preferred language, reducing confusion and improving adoption.
Data Translation Limits
There are limitations to where translated product details appear when you use data translation in Product Catalog Management.

=== ARTICLE: ind.product_catalog_data_translations_limitations.htm ===
---
article_id: ind.product_catalog_data_translations_limitations.htm
title: Data Translation Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_data_translations_limitations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_data_translation.htm
fetched_at: 2026-09-04
---

# Data Translation Limits

There are limitations to where translated product details appear when you use data translation in Product Catalog Management.

REQUIRED EDITIONS
View supported products and editions.
When you use Browse Catalog from quotes and orders, the last modified date isn’t shown for any catalogs.
Asset names aren’t translated in the Managed Asset Viewer when a translated catalog is enabled.
If a Product Attribute Definition (PAD) override is present, translations aren’t supported for that attribute. Searches use only the base value.
For dynamic attributes, only picklist types support translations. Attributes of other types (such as text) use only base values.
A full reindex is required in these cases:
When partial indexing is disabled. The system automatically determines when this applies.
When translations for custom field labels are added, removed, or updated.
When translations for enum fields (dynamic, static, or multi-select) are added, removed, or updated.
In all other scenarios, partial indexing can be used.
When translations aren’t available for a language, search results fall back to the base values.

=== ARTICLE: ind.product_catalog_decimal_quantity_support_in_product_catalog_management.htm ===
---
article_id: ind.product_catalog_decimal_quantity_support_in_product_catalog_management.htm
title: Decimal Quantity Support in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_decimal_quantity_support_in_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_products.htm
fetched_at: 2026-09-04
---

# Decimal Quantity Support in Product Catalog Management

Define accurate product quantities for products that support decimal values. Based on the product's unit of measure (UOM), define the number of decimal places the product supports, with specific rounding methodologies.

REQUIRED EDITIONS
View supported products and editions.

Accurately measure product quantities in different units of measure, such as grams, kilograms, meters, feet, seconds and minutes. Each unit of measure belongs to a particular class, such as weight, height, and size. The decimal quantity of product values honors the scale or rounding methodology defined on the unit of measure. You can specify the decimal value and rounding methodologies for product quantities based on their UOM.

Using decimal quantities to define products makes product management more effective, especially in industries such as processing, manufacturing, and healthcare, where precise measurements are crucial.

EXAMPLE

In manufacturing and processing industry, accurate decimal quantities are critical. For example, a metal fabrication bundle may require 2.558 meters of steel, 1.25 kg of welding wire, and 0.8 liters of coating. Accurately managing these quantities ensures product quality, minimizes waste, and optimizes resource utilization.

Pharmacies and healthcare providers often manage fractional dosages like 0.5 tablets or 1.75 ml. Ability to handle accurate decimal quantities are crucial for patient safety and treatment efficacy.

Scaling and Rounding Methodology

Optimize numerical data by reducing the number of decimal places. Scaling specifies the limit on the number of decimal places and the rounding methodology adjusts the number accordingly. The rounding methods available are Up, Down, and Nearest.

NOTE

The value of scale must be greater than or equal to zero. If the scale is defined, then defining the rounding method is required, and vice versa.

If you receive an error when entering decimal values for quote line item quantities, verify that the DecimalQuantityDesigntime permission set is assigned and that the product has a unit of measure defined. For more details, see How to Update Quote Line Item Quantity with Decimal Values.

EXAMPLE



ROUNDING METHOD


	


EXAMPLE





​​Up: If the number of decimals in the original value exceeds the specified scale, this method rounds up the final decimal within the specified scale to the next higher value.

.	

Number = 2.54632

Scale = 3

Final = 2.547.

Here, the value of the third decimal place is increased to the next higher value.




Down: If the number of decimals in the original value exceeds the specified scale, this method retains the value of the final decimal within the specified scale.

	

Number = 2.54632

Scale = 3

Final = 2.546.

Here, the value of the third decimal place didn't change.




Nearest: If the number of decimals in the original value exceeds the specified scale, this method either rounds up the final decimal within the specified scale to the next higher value, or retains the value of the final decimal within the specified scale.

	

Number = 2.54632

Scale = 3

Final = 2.546.

Here, the value of the third decimal place didn't change because the value of the fourth decimal place was less than or equal to four.

Number = 2.54689

Scale = 4

Final = 2.5469.

Here, the value of the fourth decimal place is increased because the value of the fifth decimal place is greater than or equal to five.

Create a Unit of Measure
Capture accurate product quantities by defining the number of decimal places the product supports, with specific rounding methodologies.
SEE ALSO
View and Edit Quotes in Revenue Cloud
View and Edit Orders in Revenue Cloud
Unit Of Measure Inheritance and Rounding Values

=== ARTICLE: ind.product_catalog_decision_tables_for_product_catalog_management.htm ===
---
article_id: ind.product_catalog_decision_tables_for_product_catalog_management.htm
title: Decision Tables for Qualification Rules
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_decision_tables_for_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_qualification_rules.htm
fetched_at: 2026-09-04
---

# Decision Tables for Qualification Rules

A decision table contains the criteria used for qualification and disqualification of products and product categories. Create a decision table for every type of qualification and disqualification that you want to configure.

REQUIRED EDITIONS
View supported products and editions.

As part of your qualification rule design, you can choose to use an existing qualification or disqualification decision table. Many organizations have existing decision tables for qualification rules that you can add to. Alternatively, you can chose to create a new decision table from a template.

To get started with decision tables for qualification rules, refer to these instructions:

Create a Decision Table That Uses a Standard Evaluation Object
If you use Product Qualification, Product Disqualification, Product Category Qualification, or Product Category Disqualification objects to store the evaluation criteria, use predefined templates to easily create decision tables.
Create a Decision Table That Uses a Custom Evaluation Object
If you use a custom object to store the evaluation criteria, create a decision table without using the templates.
Activate a Decision Table in Revenue Management
Before you use decision tables in qualification rule procedure elements, you must set the decision tables to active.

=== ARTICLE: ind.product_catalog_deep_clone_a_product.htm ===
---
article_id: ind.product_catalog_deep_clone_a_product.htm
title: Deep Clone a Product
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_deep_clone_a_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_deep_clone_in_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Deep Clone a Product

Create a complete and ‌independent copy of a product, including all related entities such as attributes, child components, and selling models.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To deep clone a product:	Product Designer
From the Product Catalog Management app’s home page, click Products.
In the product list page, from the quick action menu dropdown list, select Deep Clone.
In the Deep Clone Product window, provide a name for the product and click Deep Clone.

The product is deep cloned. The deep clone summary provides information on the number of records created for each object. To view the cloned product, click View Cloned Product.

=== ARTICLE: ind.product_catalog_deep_clone_in_product_catalog_management.htm ===
---
article_id: ind.product_catalog_deep_clone_in_product_catalog_management.htm
title: Deep Clone Products in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_deep_clone_in_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_products.htm
fetched_at: 2026-09-04
---

# Deep Clone Products in Product Catalog Management

Create products by cloning existing products and their related information such as attributes, child components, and selling models. Use deep cloning to reduce manual effort and quickly create products that are similar to the existing products. Leverage context service capabilities to customize the deep clones of custom objects and fields that are not included in the available default context definition.

REQUIRED EDITIONS
View supported products and editions.
Set Up Product Deep Cloning
Customize the product deep clone settings to add the appropriate context definition and expression set.
Deep Clone a Product
Create a complete and ‌independent copy of a product, including all related entities such as attributes, child components, and selling models.

=== ARTICLE: ind.product_catalog_dyn_create_attribute_categories.htm ===
---
article_id: ind.product_catalog_dyn_create_attribute_categories.htm
title: Create Attribute Categories in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_dyn_create_attribute_categories.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_dynamic_attributes.htm
fetched_at: 2026-09-04
---

# Create Attribute Categories in Revenue Management

Organize product attributes into logical groups called attribute categories. Attribute categories help users easily find and use the right attributes when they create product classifications. You can assign attributes individually or through an attribute category to product classifications.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To create attribute categories:	Manage Product Catalog

Attribute categories aren't required, but they can help you to organize complex sets of attributes. Let's explore an example.

Computer memory comes in all kinds of RAM chips like 8GB DDR3, 16GB DDR4, and so on. Imagine you have dozens of these options availabe to sell. To help your sales reps locate these attributes quickly, create an attribute category called Memory and assign all the individual attibutes for memory to it. That way your reps can find all memory options in one conveinent place.

Now that you've seen an example, here's how to create an attribute category:

From the Product Catalog Management app’s home page, click Attribute Categories.
From the Attribute Categories list view, click New.
In the New Attribute Category window, enter these field values:
Enter a name and description for the attribute category.
Enter a unique code for the attribute category.
Save your changes.
Assign Attributes to Attribute Categories in Revenue Management

After creating your attributes, you can group attributes by assigning them to attribute categories. You can then assign these attribute categories to product classifications to quickly assign the entire group of attributes.

From the Product Catalog Management app’s home page, click Attribute Categories.
From the Attribute Categories list view, click the attribute category to which you want to assign attributes.
In the related list for an attribute category, from the Attributes section, click Assign.
Select one or more attributes from the list or search for attributes and then click Assign.
NOTE You can assign only active attributes to an attribute category.
You can also use the Attributes section within the Attribute Category related list to unassign attributes from an attribute category.
NOTE Before you unassign attributes from an attribute category, make sure that the attribute to attribute category combination isn’t used by any product classification or product.
Use Related Product Classification Attributes and Related Product Attributes related lists to determine the product classifications or products to which such attributes are assigned.
Delete these attributes from the product classification or products, and then unassign the attributes from the category.

=== ARTICLE: ind.product_catalog_dyn_create_attributes.htm ===
---
article_id: ind.product_catalog_dyn_create_attributes.htm
title: Create Product Attributes in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_dyn_create_attributes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_dynamic_attributes.htm
fetched_at: 2026-09-04
---

# Create Product Attributes in Revenue Management

Create attributes to capture the characteristics or properties of products. You can define details such as attribute name, label, data type while creating an attribute.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create dynamic attributes:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Attributes.
From the Attribute Definitions list view, click New.
In the New Attribute Definition window, enter these field values:
For Label enter the attribute label that runtime systems can use as a display name for the attribute.
For Source System ID, enter a unique identifier for the attribute in an external system that stores the attribute definitions.
For Data Type, select the type of data that the attribute holds. If you select Picklist, select a picklist from the Picklist field.
If this attribute is a required attribute, select Required. You can override this property when you assign the attribute to a product classification, or when a product inherits the attribute.
To activate an attribute select Active.
You can assign only active attributes to Product Classifications and Attribute Categories.
NOTE Before you deactivate any attribute, ensure that it isn’t in use in any Products or Product Classifications.
Enter a description for the attribute.
Enter a description for the attribute value.
Enter a Default Help Text. This field can store useful information for runtime users.
Save your changes.

=== ARTICLE: ind.product_catalog_dyn_create_picklists.htm ===
---
article_id: ind.product_catalog_dyn_create_picklists.htm
title: Create Attribute Picklists
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_dyn_create_picklists.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_picklists.htm
fetched_at: 2026-09-04
---

# Create Attribute Picklists

Follow these instructions to create an attribute picklist. You must create your picklists first before you create attributes of type picklist.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To create picklists:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Picklists.
On the Attribute Picklists list view page, click New.
In the New Attribute Picklist window, enter these values:
Enter a name and description for the picklist.
Select a data type.
The default data type is Boolean.
Select a status for the picklist.
You can use only active picklists for attributes.
NOTE Before you deactivate a picklist, ensure that it isn’t in use by any attribute of a product or an attribute of a product classification.
Save your changes.
Click the Related tab for the newly created picklist.
In the Attribute Picklist Values section, click New.
In the New Attribute Picklist Value window, enter these values:
Enter a name for the picklist value.
If necessary, enter an abbreviation for the picklist value.
Enter a unique code for the picklist value within the org.
Select a status for the picklist value.
You can use only active picklist values for attributes.
NOTE Before you deactivate a picklist value, ensure that it isn’t in use by any attribute of a product or an attribute of a product classification.
Select Default to make this picklist value the default value for the associated picklist. Only one value can be the default for a picklist.
Enter a display value. This picklist value is displayed at run time. Use this field when the display value is different from the actual value. For example, for the number value ‘5’, the display value is ‘Five’. The display value must be unique within a picklist.
Enter a value for the picklist item.
NOTE Ensure that you use a value that you haven’t used as a display value for this picklist.
Enter the sequence to determine the order in which this picklist value appears during the purchase.
Save your changes.

=== ARTICLE: ind.product_catalog_dynamic_attributes.htm ===
---
article_id: ind.product_catalog_dynamic_attributes.htm
title: Manage Dynamic Attributes in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_dynamic_attributes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Manage Dynamic Attributes in Revenue Management

Attributes are the key characteristics or properties of products. Define your attributes, and then assign them to your products using product classifications.

REQUIRED EDITIONS
View supported products and editions.
EXAMPLE A mobile phone product can have attributes like size, weight, storage capacity, display size, and camera specifications. A television can have a different set of characteristics like display type, connectivity, sound output, and smart TV.

When working with attributes, you can:

Create attributes as text, number, date, datetime, checkbox, picklist, currency, and percent.
Organize attributes into logical groups called attribute categories.
Assign attributes to products using product classifications.
Override an attribute assignment if you need to specify a different attribute for that product.
NOTE The primary method for assigning attributes to products is through Product Classifications. To learn more, see Create Product Templates Using Product Classifications.

To get started with managing dynamic attributes, refer to these instructions:

Create Product Attributes in Revenue Management
Create attributes to capture the characteristics or properties of products. You can define details such as attribute name, label, data type while creating an attribute.
Manage Attribute Picklists in Revenue Management
Picklists allow you to define multiple values for a given attribute. For example, colors for t-shirts or sizes of pants. To use picklists with your attributes, you must define your picklists first before creating the attributes.
Working with Product Attribute Fields
Learn more about the fields used in product attribute definitions. Some fields simply define an attributes, while others affect runtime when your sales reps are working with quotes and orders.
Create Attribute Categories in Revenue Management
Organize product attributes into logical groups called attribute categories. Attribute categories help users easily find and use the right attributes when they create product classifications. You can assign attributes individually or through an attribute category to product classifications.
Reorder Attribute Categories and Attributes
Control the order in which attribute categories and attributes appear when reps configure products. Organize attributes into a logical sequence that matches your business process instead of relying on alphabetical order.

=== ARTICLE: ind.product_catalog_edit_group_cardinality.htm ===
---
article_id: ind.product_catalog_edit_group_cardinality.htm
title: Edit Group Cardinality
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_edit_group_cardinality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_group_cardinality.htm
fetched_at: 2026-09-04
---

# Edit Group Cardinality

Edit group cardinality to change the minimum and maximum number of distinct components in the group that users can add to the run-time cart.

REQUIRED EDITIONS
USER
PERMISSIONS NEEDED
To edit cardinality:	Manage Product Catalog
To use the structure tab:	ARC Access permission set
From the Product Catalog Management app’s home page, click Products.
From the product list view page, click the bundled product.
Navigate to the Structure tab.
To edit group cardinality, perform these steps:
The first product in the bundle hierarchy is the root product. The products, groups, and product classifications at the first level are the immediate child components of the root product. You can edit the cardinality of products, groups, and product classifications only at the first level. You can override the cardinality of products, groups, and product classifications only at the second level and beyond.
Click a group tile at the first level in the product hierarchy. The right panel shows the group details and cardinality.
Navigate to the Cardinality tab.
Edit the minimum and maximum number of components as necessary.
Save your changes.

=== ARTICLE: ind.product_catalog_edit_local_cardinality.htm ===
---
article_id: ind.product_catalog_edit_local_cardinality.htm
title: Edit Local Cardinality
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_edit_local_cardinality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_local_cardinality.htm
fetched_at: 2026-09-04
---

# Edit Local Cardinality

To define the default, minimum, and maximum quantity of a product that’s permissible in the product bundle, edit the local cardinality of the product component and the product classification component.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To edit the local cardinality:	Manage Product Catalog
To use the structure tab:	ARC Access permission set
From the Product Catalog Management app’s home page, click Products.
From the Product list view page, click the bundled product that contains the product component or product classification component whose cardinality you want to edit.
Navigate to the Structure tab.
Click the product tile for a product at the first level in the product hierarchy.
The first product in the bundle hierarchy is the root product. The products, groups, and product classifications at the first level are the immediate child components of the root product. You can edit the cardinality of products, groups, and product classifications only at the first level. You can override the cardinality of products, groups, and product classifications only at the second level and beyond.
In the right pane, click  next to More, and click Cardinality.
Click Edit.
Edit the local cardinality as necessary.
Save your changes.

=== ARTICLE: ind.product_catalog_einstein_generate_product_description.htm ===
---
article_id: ind.product_catalog_einstein_generate_product_description.htm
title: Write Product Descriptions with Einstein Generative AI
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_einstein_generate_product_description.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_description_generation.htm
fetched_at: 2026-09-04
---

# Write Product Descriptions with Einstein Generative AI

Einstein generative AI uses your instructions to generate revised product descriptions. Product descriptions support instructions only in English but you can generate descriptions in all supported languages. Any user can generate product descriptions by using Einstein but only the Salesforce admin and Product Catalog Designer can accept or reject the recommendations.

REQUIRED EDITIONS
View supported products and editions.
IMPORTANT This tool uses generative AI, which is known to include incorrect or harmful responses. Before using externally, review the output for accuracy and safety. You assume responsibility for the output when making business decisions.
Set Up Einstein Generative AI in Product Discovery

Before you can generate product descriptions by using generative AI, enable Einstein in your org.

Set Up Einstein generative AI.
In Setup, find and select Product Discovery Settings.
Turn on Generate Product Descriptions with Einstein AI.
Add the Einstein Generative AI Recommendation component to the product page layout, and then configure it.
See Create and Configure Lightning Experience Record Pages.
Add a tab to the Product record page.
Drag the Einstein Generative AI Recommendation component onto the new tab.
To edit the properties of the component, click the Einstein Generative AI Recommendation component.
Enter PCM as the app name.
To add a default instruction text for your product description, enter your instructions in the Product Description Instructions field.
Save your changes.
Generate a Product Description
Open a product record page.
To generate a product description, go to the tab that has the Einstein Generative AI Recommendation component.
If the Current field is blank, enter a draft product description.
In Instructions, use the default instruction, or enter a new instruction for your product.
If data translations are set up for your organization, select Translate to all languages.
To generate a description, click Create.
You can edit or accept the text, or regenerate a description.
To save and update the description for the product, click Accept.

=== ARTICLE: ind.product_catalog_enable_guided_product_selection.htm ===
---
article_id: ind.product_catalog_enable_guided_product_selection.htm
title: Enable Guided Product Selection
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_enable_guided_product_selection.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_guided_product_selection.htm
fetched_at: 2026-09-04
---

# Enable Guided Product Selection

Before you configure Guided Product Selection to help users find the right products, you must enable Product Discovery, Discovery Framework, Omnistudio, and Guided Product Selection. Then, deploy a predefined template to create an Omniscript that’s used to configure questionnaires.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To set up Guided Product Selection:	

Product Catalog Management Designer permission set

AND

OmniStudio Admin permission set

Complete the Prerequisites for Guided Product Selection Setup
Make sure that you have access to Omnistudio.
NOTE Omnistudio isn’t available with Product Catalog Management by default. Omnistudio is available as a part of other products such as Revenue Management or as a standalone Omnistudio license.
The Omniscript for Guided Product Selection can be accessed by using the Omnistudio managed package designer or the Omnistudio standard designer.
To use the Omnistudio managed package designer, enable the Managed Package Runtime setting, and then enable the Managed Package Designer setting. If needed, enable the Deploy Custom Lightning Web Components setting. See Omnistudio Settings.
To use the Omnistudio standard designer, disable the Managed Package Runtime setting, and then disable the Managed Package Designer setting. See Omnistudio Standard Designer.
Enable Discovery Framework and then turn on the Import or Export setting. See Enable Discovery Framework and Configure Import or Export Settings.
Turn on the Use Indexed Data for Product Listing and Search setting. See Product Index and Search in Product Catalog Management.
Enable the necessary Product Discovery settings. See Configure Product Discovery Settings.
Enable Guided Product Selection
From Setup, find and select Product Discovery Settings.
Enable Guided Product Selection.
Deploy the ProductGuidedSelectionIntegration Omniscript

The ProductGuidedSelectionIntegration Omniscript generates a Pub/Sub event—containing the discovery framework response ID—which initiates a search on the Product List component. In Discovery Framework, the Omniscript also saves user responses, which are used by the Guided Product Selection API to search for products. When designing Omniscripts for assessments, include the ProductGuidedSelectionIntegration Omniscript as the final step to configure these essential settings automatically.

From Setup, in the Quick Find box, enter Discovery Framework, and then, under Discovery Framework, select General Settings.
Enable Sample Templates.
In the Sample Templates section, click the Discovery Framework Sample Template page link. The Discovery Framework Sample Templates page appears.
Deploy the Guided Product Selection template.
Access Omnistudio: From the App Launcher, find and select the Omnistudio app. The Omniscripts tab appears.
Expand ProductGuidedSelection/Integration.
Click ProductGuidedSelectionIntegration.
IMPORTANT Don’t change the ProductGuidedSelectionIntegration omniscript. On the Setup tab, the message framework must be Pub/Sub. On the Properties tab, the remote class must be Store Responses and the remote method must be invokeMethod.
Click Activate Version.

To users (sales reps and customers) who use Guided Product Selection, assign the necessary permission sets and provide record access. See Permissions to Access Product Discovery.

=== ARTICLE: ind.product_catalog_enable_semantic_search_for_product_discovery.htm ===
---
article_id: ind.product_catalog_enable_semantic_search_for_product_discovery.htm
title: Enable Semantic Search for Product Discovery
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_enable_semantic_search_for_product_discovery.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_semantic_search.htm
fetched_at: 2026-09-04
---

# Enable Semantic Search for Product Discovery

Enable Einstein semantic search in Product Discovery to interpret search intent and surface relevant results based on synonyms, variations, and attributes.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To enable semantic search:	

Manage Product Index and Search

AND

View Product Catalog

Semantic search works across product names, descriptions, categories, and up to 12 additional searchable fields that you can configure in Index and Search Configuration.

In Setup, find and select Product Discovery Settings.
Make sure Use Indexed Data for Product Listing and Search is enabled.
Turn on Semantic Search and click Create Full Index.
Create dynamic product attributes.
NOTE Semantic search includes product names, descriptions, categories, and up to 12 additional searchable fields that you configure in Index and Search Configuration.
Rebuild your product index.

=== ARTICLE: ind.product_catalog_enable_translated_catalogs_flow_metadata.htm ===
---
article_id: ind.product_catalog_enable_translated_catalogs_flow_metadata.htm
title: Use Flow Metadata to Enable Translated Product Catalogs
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_enable_translated_catalogs_flow_metadata.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_data_translation.htm
fetched_at: 2026-09-04
---

# Use Flow Metadata to Enable Translated Product Catalogs

One method for enabling translated product catalogs is to download an updated version of the Discover Products flow and use its metadata to create a new flow.

REQUIRED EDITIONS
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management where Transaction Management is enabled
USER PERMISSIONS NEEDED
To open, edit, or create a flow in Flow Builder:	Manage Flow
To enable translations:	Manage Product Catalog

To use the metadata from the updated Discover Products flow, you'll create and download a new flow from your org to your local machine. Then you'll replace the contents of the new flow with the contents of the updated Discover Products flow and upload the new flow to your org.

Download Discover_Products_With_Translations.flow.
In Your Salesforce org, select Setup then search for and select Flows.
Open the flow Discover Products.
In Flow Builder, select Save As New Flow and name your new flow Discover Products With Translations.

Make a note of the API name that's generated automatically. For example, Discover_Products_With_Translations.

Open Workbench from https://workbench.developerforce.com and connect it to your org. Salesforce doesn’t maintain Workbench, so we can’t address issues or bugs related to using it. We recommend that you use our alternative and integrated tools. See Replacement Tools for Workbench for more information.
On the Metadata tab, choose the option for Metadata groups
For Input, enter Flow
For Members, enter the API name of the new flow, Discover_Products_With_Translations.
Check Single Package
Select Retrieve.
When the retrieval succeeds, select Fetch then Download.
In the default download location on your local machine, find and extract the file retrieve.zip.
Delete the file Discover_Products_With_Translations.flow that you extracted from the ZIP file. On Windows, it's retrieve\flows\Discover_Products_With_Translations.flow. On MacOS and Linux systems it's retrieve/flows/Discover_Products_With_Translations.flow
Move or copy the version of Discover_Products_With_Translations.flow you downloaded in the first step to the folder retrieve\flows (for Windows) or retrieve/flows (for MacOS and Linux).
Open Discover_Products_With_Translations.flow in a text editor an verify that the flow name defined in the <interviewLabel> and <label> XML tags matches the name of your flow. Also, note of the API version that's defined in the <apiVersion> tag and be sure that Workbench is set to the same version.
Save the file and close the editor.
Create a zip file called package.zipthat includes the flows directory (which in turn contains Discover_Products_With_Translations.flow) and the file package.xml. Be sure to keep the same relative locations of the flow and XML files in the zip file. The flow should be in the flows folder and the XML file should be at the top level of the archive.
To upload the new flow to your org, go back to Workbench and select the Deploy tab.
For File, choose the package.zip file.
Check Single Pagkage.
Select Deploy.
When package.zip finishes uploading, activate the new flow by going to Setup > Flows.
Locate and select the flow Discover Products With Translations.
In the flow, select Activate.

To check your work, go to any quote or order and select Browse Catalogs to see the translated product catalog names.

=== ARTICLE: ind.product_catalog_end_to_end_product_classification_example.htm ===
---
article_id: ind.product_catalog_end_to_end_product_classification_example.htm
title: Explore Product Classification with an Example
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_end_to_end_product_classification_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_classifications.htm
fetched_at: 2026-09-04
---

# Explore Product Classification with an Example

Streamline the creation of a car product template by engineering a product classification hierarchy. Create a parent classification to automatically share attributes with child subclassifications, and curate valid options for specific models to reduce data entry errors.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create a product classification:	Manage Product Catalog

Imagine your company, Autz, sells cars. Start by creating a parent classification for all vehicles. This structured template automatically shares attributes with child subclassifications for specific types, such as Sedans and SUVs

Define the Picklist

Create a picklist to store the available engine sizes.

From the Product Catalog Management app’s home page, click Picklists Classifications.
Click New.
Enter the name Engine Type and data type as Text.
Set the status to Active.
Save your changes.
Click the Related tab.
In the Attribute picklist values section, click New.
Create the first value. Enter the name as 2.5 L, code as 2.5 L, value as 2.5, and set the status to Active.
Save your changes.
Repeat steps 7 through 9 to create values for 3.5 L and 4.0 L.
Repeat the procedure to create a second picklist named Color with values Red, White, Blue, and Black.
Create the Attributes

Now, create the attribute definitions and reference the picklists you built.

From the Product Catalog Management app’s home page, click Attributes .
On the Attribute Definitions list view page, click New.
Enter the label as Engine Type, data type as Picklist.
Select the Engine Type picklist that you created.
Select Active.
Save your changes.
Repeat steps 1 through 6 to create the Color attribute, linking it to the Color picklist.
Define the Car Template

First, create a parent classification for all cars that contains a few common attributes. This classification acts as a reusable template for any vehicle you create.

From the Product Catalog Management app’s home page, click Product Classifications.
On the Product Classifications list view page, click New.
Enter the name Cars and a unique code.
Set the status to Active.
Save your changes.
Map Characteristics to the Template

Assign the attributes created earlier to the template. These attributes will automatically cascade down to any subclassification that you create later.

From the Product Catalog Management app’s home page, click Product Classifications.
Select the Cars classification.
Go to the Attributes tab. In the Attributes section, click Assign.
Select Assign individual attributes.
Find the Engine Type and Color attributes and click Assign.
Save your changes.

The Cars classification is equipped with both attributes, containing all available picklist values.

Derive Specialized Models

Create specific models (subclassifications) based on the template. These models inherit the Engine Type and Color attributes automatically.

From the Product Catalog Management app’s home page, click Product Classifications.
Click the Subclassification tab, and then click New.
In the New Product Classification page, enter the name as Sedan and a unique code.
Set the parent product classification to Cars and the status to Active.
Save your changes.

Repeat this step to create a second subclassification named SUV with the code SUV.

Customize Attributes for Specific Models

Customize the inherited attributes to set specific defaults for each model. For the Sedan, set the standard engine size.

From the Product Classifications list, select the Sedan subclassification.
Go to the Attributes tab.
Next to the inherited Engine Type attribute, click the action menu and select Configure.
In the Default Value field, select 2.5 L.
Save your changes.
Curate Available Options for Each Model

Finally, ensure data accuracy by restricting which options are valid for each model. For example, a Sedan should not be available with a 4.oL engine or in Black color.

Restrict Engine Types for Sedans.
From the Product Classifications list, select the Sedan subclassification.
Go to the Attributes tab.
Select Include or Exclude Picklist Values from the dropdown menu next to Engine Type.
Deselect 4.0 L.
Save your changes.
Restrict colors for sedans.
From the Product Classifications list, select the Sedan subclassification.
Go to the Attributes tab.
Select Include or Exclude Picklist Values from the dropdown menu next to Color.
Deselect Black.
Save your changes.
Configure the SUV model.
Repeat the steps to configure the SUV subclassification to meet its unique requirements.
From the Product Classifications list, select the SUV subclassification.
Exclude 2.5 L and 3.5 L from the Engine Type attribute, leaving only 4.0 L option.
Click the dropdown next to Colors and select Include or Exclude Picklist Values.
Exclude White from the Color attribute.
Save your changes.

You have successfully engineered a product classification hierarchy. Any product record created by using the Sedan classification automatically inherits a restriction to 2.5 L or 3.5 L engines and won’t offer Black as a color option, significantly reducing manual data entry errors. Similarly, any product record created by using the SUV classification automatically inherits a restriction to a 4.0 L engine and won’t offer White as a color option.

=== ARTICLE: ind.product_catalog_enhanced_product_discovery_experience.htm ===
---
article_id: ind.product_catalog_enhanced_product_discovery_experience.htm
title: Product Discovery with Constraint Rules
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_enhanced_product_discovery_experience.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_discovery.htm
fetched_at: 2026-09-04
---

# Product Discovery with Constraint Rules

The Product Discovery with constraint rules experience helps you build accurate transactions as you browse the product catalog. You see real-time transaction details in the transaction preview, along with constraint rule outcomes such as disabled products, product recommendations, and rule messages. When you add or remove a product, Product Discovery automatically saves the change to the transaction, you don't pause your browsing or wait for the save to complete. While the save is in progress, you can continue going to a category, searching for more products, or reviewing recommendations. This non-blocking experience keeps the catalog fully interactive always.

REQUIRED EDITIONS
View supported products and editions.

As you browse the catalog, Product Discovery keeps the Product List page and the transaction preview in sync with your transaction. Each time you add a product, Product Discovery evaluates the updated transaction using configuration rules and updates rule messages, disabled products, recommendations, and the preview.

Key Capabilities

The Product Discovery with constraint rules experience combines several capabilities on the Product List page.

Key Capabilities of Product Discovery with Constraint Rules
CAPABILITY	DESCRIPTION
Visibility rules during product selection.	

You can define constraint rules in a CML constraint model in Product Configurator to disable products, display rule messages, and show product recommendations. As you browse and add products, Product Discovery evaluates these rules and updates the configuration rule outcomes in the Product Discovery experience. You see rule messages at the top of the page, disabled products appear as disabled in the Disqualification filter. This immediate feedback helps you understand constraints as you make selections and avoid issues later in the transaction.

NOTE Product Discovery uses configuration rules, which you define as constraint rules in a constraint model written in CML.
When more than one message rule applies, Product Discovery shows multiple messages in the message bar.
When a product is both recommended and disabled, you can’t add it. Disabled rules take precedence.
When a disabled rule and a disqualification rule apply to the same product, Product Discovery shows messages from both rules, and you can't add the product.

When a disabled rule or a disqualification rule applies, Product Discovery hides the affected products from the product list. Apply the Disqualified filter to view them.


Product recommendations based on transaction.	Product Discovery shows rule-based recommendations defined by configuration rules, based on your current transaction. You can add recommended products directly from the Recommendations list. Product Discovery shows the rule-based recommendations defined by configuration rules, based on your current transaction. You can add recommended products directly from the Recommendations list. Product Discovery honors qualification rules when showing recommended products.
Auto-add and auto-delete during product selection.	Product Discovery evaluates configured rules and automatically adds or removes products from a transaction when the specified conditions are met.
Autosave for committed changes.	When you add a product, Product Discovery saves it directly to the transaction. You don’t need a separate save action, so you can continue adding products while the transaction preview stays in sync.
Transaction preview during browsing.	The transaction preview shows your current transaction in real time and updates automatically as you add or remove products. You can review products, quantities, and pricing while you continue browsing the catalog.
NOTE
In transactions with many line items, adding or removing multiple products at the same time can occasionally lead to unexpected behavior. To ensure consistent results, add or remove products sequentially.
The transaction preview shows committed transaction data only.
Configuration rules are evaluated based on the current transaction and not all catalog results.
If you turn off the feature, users see the older preview experience. The earlier preview doesn’t provide the same real-time updates or configuration rule visibility.
Set Up Enhanced Product Discovery Features
Turn on enhanced Product Discovery features so that Product Discovery can show transaction previews, configuration rule outcomes, and rule-based recommendations, and automatically save product changes while users browse the catalog.
Preview Transactions While Browsing the Catalog
Use the transaction preview to review product selections, quantities, and pricing in real time without leaving Product Discovery. The preview shows up to the 50 most recently added items in the transaction. For bundled products, the preview displays only the main product.
Product Visibility and Recommendations in Real Time
As you browse the catalog, Product Discovery evaluates the current transaction against configuration rules. Based on the rules you configure, Product Discovery shows messages, disables products, and recommended products directly in the browsing experience.

=== ARTICLE: ind.product_catalog_enter_translations_manually.htm ===
---
article_id: ind.product_catalog_enter_translations_manually.htm
title: Enter Translations Manually in the Translations Tab
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_enter_translations_manually.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_data_translation.htm
fetched_at: 2026-09-04
---

# Enter Translations Manually in the Translations Tab

Add translations directly on product, category, or attribute records using the Translations tab. Use this method for quick updates or small sets of localized values. After saving translations, reindex the catalog so users see the localized values in product listings and search results.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To translate product and product category data:	Manage Product Catalog
Open a catalog, category, product, or attribute record.
Go to the Translations tab.
If the tab isn’t visible, see Add the Translations Tab in Lightning Experience. For details about field translations, see Add Translations for Standard and Custom Fields.
Click Add Translation.
Select a language and enter translated values for the supported fields.
Save your changes.
Reindex the catalog.
After importing translations, rebuild the full index to apply them. See Build an Index in Product Catalog Management.
(Optional) Verify translations.

In the UI:

Log in as a user whose org language matches a translation.
Browse catalogs and confirm product and category names are displayed in that language.
Search using translated terms (for example, enter portable in French to return translated laptop products).

=== ARTICLE: ind.product_catalog_example_create_custom_flow_for_browsing_and_adding_products.htm ===
---
article_id: ind.product_catalog_example_create_custom_flow_for_browsing_and_adding_products.htm
title: Override Flow for Product Discovery
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_example_create_custom_flow_for_browsing_and_adding_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_considerations_custom_flow_for_browsing_and_adding_products.htm
fetched_at: 2026-09-04
---

# Override Flow for Product Discovery

Use the Discover Products flow to select a catalog and then add products from the catalog to their associated record pages. The Discover Products flow is readily available with Product Discovery, and you can customize the flow beyond the available capabilities to meet your business needs.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To open, edit, or create a flow in Flow Builder:	Manage Flow
Create an Apex Class That Creates a Context Data Input Record

The flow uses an Apex class that creates a list of ContextDataInput records that contain the object API name and the record ID. The flow then passes the list that contains additional context data to the Product List Page Container component. The component shows products and uses the additional context data, context definition, qualification rule procedure, and qualification rules to determine product eligibility.

IMPORTANT To use the quote and order fields to determine product eligibility, enable Transaction Management in your org, and also update the qualification rule procedure used for Product Discovery. See Edit a Qualification Rule Procedure and Configure Product Discovery Settings.

Create an Apex class that takes an object’s API name and record ID as input and returns a list of ContextDataInput records as the output.

From Setup, in the Quick Find box, enter Apex Classes and select it.
Click New.
In the editor, customize and paste the code that creates additional context data for your records.
public class DiscoverProductFlowAction {
    
    // Define input parameters
    public class FlowInput {
        @InvocableVariable(required=false)
        public String objectApiName;
        
        @InvocableVariable(required=false)
        public String recordId;
    }
    
    // Define output parameters     
    public class FlowOutput {
        @InvocableVariable
        public runtime_industries_cpq.ContextDataInput[] additionalContextData;
    }

    // This method is invoked from a flow
    @InvocableMethod(label='Process Input' description='Creates the Array of ContextDataInput for additional Context Data')
    public static List<FlowOutput> generateAdditionalContextData(List<FlowInput> inputs) {
        String apiName;
        String recId;
        FlowOutput output = new FlowOutput();
        
        // Capture input from the flow
		for(FlowInput input : inputs ){
            apiName = input.objectApiName;
            recId = input.recordId;
        }

        //Populate the ContextDataInput list to store additional context data
      	List<runtime_industries_cpq.ContextDataInput> listContextData = new List<runtime_industries_cpq.ContextDataInput>();
        runtime_industries_cpq.ContextDataInput cd1 = new runtime_industries_cpq.ContextDataInput();
        cd1.nodeName = 'Quote'; //Where Quote is the name of the node in the context definition.
        cd1.nodeData = new Map<String,Object>();
        cd1.nodeData.put('id',recId);       
        listContextData.add(cd1);
        
        // Return the additional Context Data to a flow
        output.additionalContextData = listContextData;
        return new List<FlowOutput>{output};       
    }
}

Save your changes.
Create a Custom Discover Products Flow

The preconfigured Discover Products flow first identifies the number of catalogs available for the user. If a default catalog is selected on the Product Discovery settings page, then the catalog automatically appears when the user initiates the flow. Next, the flow passes the objectApiName and recordId of the record that the flow is invoked from, to the Apex class to generate additional context data. Then, the flow uses the selected catalog and additional context data in the Product List Page Container component, which shows the products that users can add to quotes and orders.

Use the Product List Page component to add product lists to any object, including quotes and orders, or in custom components. The Product List Page component provides you greater flexibility to customize the display and the action label of the product list according to your specific needs.

NOTE

When you add the Product List Page component onto your custom Lightning Web Component, enable communication between them by subscribing the custom component to the productDiscovery_notification message channel of Lightning Message Service. Then, customize the actions for the events sent from the channel based on your business needs. For more information, see Subscribe and Unsubscribe from a Message Channel.

From Setup, in the Quick Find box, enter Flows and select it.
To open the preconfigured flow, click Discover Products.
Click Save as New Flow on the header of the flow page, and enter a flow label and a flow API name.
Save your changes.

You can now customize the flow.

NOTE

Updating or disabling existing parameters inherited from Discover Products flow leads to undesirable behavior or errors. It’s recommend to create new parameters to customize the Flow for specific use cases

After you create the flow, select it on the Product Discovery Settings page to automatically launch the flow when users click the Browse Catalogs button from quote and order pages. Alternatively, map the flow to its associated action button for your record pages.

SEE ALSO
Product Discovery Component Properties
Include Additional Fields in Your Flow

To show additional standard or custom product fields in your overridden flow, create a collection variable that contains these fields and then select the variable on the properties panel on the product list container component.

From Setup, in the Quick Find box, enter Flows and select it.
Open your overridden flow.
Create a flow collection variable.
You can associate the collection variable with product fields in an Assignment element.
From the toolbox manager, click New Resource.
Select Variable as the resource type.
Enter an API name and a description for the variable.
Select Text as the data type.
To convert the variable into a collection variable that can store multiple values, select Allow multiple values (collection).
Save your changes.
To assign values to the collection variable, add an Assignment element before the Product List Page flow screen component.
Enter a name, an API name, and a description for the Assignment element.
In Variable, enter the API name of the flow collection variable.
Select Add as your operator.
Specify the product field API name as a value for the variable.
For example, to add the Specification Type field of the product object as a value for the collection variable, enter Product2.SpecificationType.
You can include up to 3 additional product fields.
Select the collection variable on the Product List Container flow screen component.
Open the flow screen component.
To access the properties panel, click the Product List Container component on the Edit Screen page.
In the Additional Fields property, enter the API name of the collection variable.
Click Done.
Save your flow.
Discover Products Flow Update for Ramped Segments

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
TIP Refer to the Discovery Products flow to ensure your customized flow is in sync with the latest update

=== ARTICLE: ind.product_catalog_example_provide_a_localized_french_buying_experience.htm ===
---
article_id: ind.product_catalog_example_provide_a_localized_french_buying_experience.htm
title: "Example: Provide a Localized French Buying Experience"
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_example_provide_a_localized_french_buying_experience.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_data_translation.htm
fetched_at: 2026-09-04
---

# Example: Provide a Localized French Buying Experience

This example shows how data translation changes the runtime experience for French users. See how translated values appear in catalogs, categories, products, and search results. Deliver localized catalogs without duplicate configurations. Buyers benefit from intuitive search and browsing in their preferred language, reducing confusion and improving adoption.

Export translations

From Setup, export Product2, Product Category, and related PCM entities. The XLIFF file includes base English values, such as:


    <trans-unit id="catalog_hardware">
    <source>Hardware Catalog</source>
    <target></target>
    </trans-unit>
    <trans-unit id="category_laptops">
    <source>Laptops</source>
    <target></target>
    </trans-unit>
    <trans-unit id="product_laptop_pro">
    <source>Laptop Pro</source>
    <target></target>
    </trans-unit>
    <trans-unit id="desc_laptop_pro">
    <source>Powerful laptop for professionals</source>
    <target></target>
    </trans-unit>
    <trans-unit id="attr_color_black">
    <source>Black</source>
    <target></target>
    </trans-unit>
   
Add translations

Edit the XLIFF file and add French values in the <target> fields:


    <trans-unit id="catalog_hardware">
    <source>Hardware Catalog</source>
    <target>Catalogue de matériel</target>
    </trans-unit>
    <trans-unit id="category_laptops">
    <source>Laptops</source>
    <target>Ordinateurs portables</target>
    </trans-unit>
    <trans-unit id="product_laptop_pro">
    <source>Laptop Pro</source>
    <target>Ordinateur portable Pro</target>
    </trans-unit>
    <trans-unit id="desc_laptop_pro">
    <source>Powerful laptop for professionals</source>
    <target>Ordinateur puissant pour les professionnels</target>
    </trans-unit>
    <trans-unit id="attr_color_black">
    <source>Black</source>
    <target>Noir</target>
    </trans-unit>
   

Reimport the file and rebuild the index.

Display the localized catalog

Configure English and French as supported languages, with English as the default language.

If a user’s org is set to a supported language, values display in that language. If a user’s org is set to an unsupported language (for example, German), values display in the default language (English).

OBJECT	FIELD	ENGLISH (DEFAULT)	FRENCH	GERMAN
Catalog	Name	Hardware Catalog	Catalogue de matériel	Hardware Catalog
Category	Name	Laptops	Ordinateurs portables	Laptops
Product2	Name	Laptop Pro	Ordinateur portable Pro	Laptop Pro
Product2	Description	Powerful laptop for professionals	Ordinateur puissant pour les professionnels	Powerful laptop for professionals
Attribute (Picklist)	Color	Black	Noir	Black
NOTE If a user’s org language isn’t one of the configured supported languages, Product Discovery displays values in the default language.
Buyer’s experience in French

When a French user browses the catalog:

The catalog shows Catalogue de matériel.
The category shows Ordinateurs portables.
The product shows Ordinateur portable Pro.
Searching for portable returns the translated product.
Filters show Noir instead of Black.
Business impact

Admins can deliver localized catalogs without duplicate configurations. Buyers benefit from intuitive search and browsing in their preferred language, reducing confusion and improving adoption.

=== ARTICLE: ind.product_catalog_example_use_apex_hooks_in_a_product_discovery_procedure_plan.htm ===
---
article_id: ind.product_catalog_example_use_apex_hooks_in_a_product_discovery_procedure_plan.htm
title: "Example: Use Apex Hooks to Extend Pricing Logic"
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_example_use_apex_hooks_in_a_product_discovery_procedure_plan.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.pricing_customize_pricing_procedures_with_apex_hooks.htm
fetched_at: 2026-09-04
---

# Example: Use Apex Hooks to Extend Pricing Logic

See how Apex hooks interact with Pricing sections when configured as pre- or post-hooks in a Product Discovery procedure plan.

Example Setup

This setup shows how external and internal prices interact. The procedure plan includes:

An Apex section that returns an external price (for example, $1234)
A Pricing section that applies internal pricing logic (for example, PSM = One Time → $199, PSM = Null → $149)

The placement of the Apex section determines whether its price takes effect or is overridden.

Pre-Hook Example: Internal Pricing as the Final Authority

Use this configuration when you want to fetch external prices but still rely on internal pricing as the final authority.

Procedure Plan

Section 1 – Apex (PricingApex)
Section 2 – Pricing (PricingProcedure)

How it works

The Apex hook fetches an external price of $1234 for the null PSM.
The Pricing procedure then calculates $149 and overwrites the null PSM price.

Returned Prices

PSM = One Time → $199
PSM = Null → $149
Post-Hook Example: Override Internal Pricing with External Logic

Use this configuration when you want external prices to override the results of internal pricing logic.

Procedure Plan

Section 1 – Pricing (PricingProcedure)
Section 2 – Apex (PricingApex)

How it works

The Pricing procedure calculates $199 and $149.
The Apex hook then updates the null PSM price to $1234.

Returned Prices

PSM = One Time → $199
PSM = Null → $1234

=== ARTICLE: ind.product_catalog_exclude_bundle_components.htm ===
---
article_id: ind.product_catalog_exclude_bundle_components.htm
title: Exclude Bundle Components From Product Selection at Run Time
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_exclude_bundle_components.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_bundled_products.htm
fetched_at: 2026-09-04
---

# Exclude Bundle Components From Product Selection at Run Time

To make certain products, groups, or classifications unavailable for selection at run time, you can exclude them from the product bundle. This exclusion doesn’t delete the product, it only hides the product from the user at run time. Exclusions are in the context of the root product bundle that you’re in.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To exclude components:	Manage Product Catalog
To use the structure tab:	ARC Access permission set

Excluding products is useful when you need to temporarily restrict a product from being sold, while still keeping it as part of the bundle for use later. Once the restriction period ends, a product manager can restore the product's availability.

For example, a medical device manufacturer sells a patient monitoring system including sensors, a display unit, and connection cables. If there's an unexpected disruption in the supply chain for a specific type of connection cable, the product manager can temporarily exclude that cable component from the bundle configuration. This prevents sales reps from quoting systems that cannot be fully fulfilled due to the supply shortage.

To exclude a bundle component from product selection at run time, follow these instructions:

From the Product Catalog Management app’s home page, click Products.
From the Product list view page, click the bundled product that contains the group or product component that you want to exclude from the product bundle.
Go to the Structure tab.
Click the product tile, product classification tile, or the group tile at the second level in the product hierarchy.
The first product in the bundle hierarchy is the root product. The products and groups at the first level are the immediate child components of the root product. You can exclude products, product classifications, and groups from the second level in the product hierarchy and beyond.
Click .
Excluding a group automatically excludes all the components under that group.
NOTE You can’t edit or override the cardinality of an excluded component.

To include an excluded product or group, click Restore Default Cardinality. You can also click the  to include the product or group.

=== ARTICLE: ind.product_catalog_explore_examples_of_semantic_search.htm ===
---
article_id: ind.product_catalog_explore_examples_of_semantic_search.htm
title: Explore Examples of Semantic Search
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_explore_examples_of_semantic_search.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_semantic_search.htm
fetched_at: 2026-09-04
---

# Explore Examples of Semantic Search

See how Einstein semantic search improves results across different types of queries, including synonyms, abbreviations, misspellings, and product features.

REQUIRED EDITIONS
View supported products and editions.

Einstein semantic search improves the relevance of results across a wide range of queries. Search can recognize synonyms, abbreviations, slang, misspellings, and other natural variations in how users describe products. This table shows examples of how semantic search interprets and expands queries to return the most accurate results possible.

Examples of Semantic Search Queries
QUERY ENTRY	EXAMPLE	SEMANTIC SEARCH RESULT
Synonyms	Couch and sofa	Search results include synonyms of the queried term.
Alternative spellings	Adapter and adaptor	Results include spelling variations such as “adaptor” when a user searches for “adapter.”
Abbreviations	AC and Air Conditioner	Results may include relevant items even if the abbreviation isn’t in the catalog.
Slang	Men’s shades	Results may include relevant products even when slang is used.
Misspellings	Shert and shirt	Results include products with minor spelling errors.
Product themes	Wedding gift	Results include items associated with the concept of “wedding gift.”
Product features	Long USB cable	Results include items with equivalent feature descriptions, such as “10ft cord” or “3m cable.”
Product types	Women’s jackets	Results include exact matches and related items, such as coats and blazers.
Multiple languages	Wireless headphones for running (English) / Auriculares inalámbricos para correr (Spanish)	Results include translations and matches across languages.
Brand names	Adidas shoes, Plorra dress	Results are complete for well-known brands, less so for newer brands.
Ambiguity	Apple charger	Results prioritize the most likely matches.
Related products	20" TV and 21" TV	Results reflect product similarities and differences, ranking closest matches higher.
Exact keywords	iPhone 14 Pro Max	Results return the exact keyword.
Descriptions	Table with blue-greenish color	Results include teal, blue, and green tables as reasonable matches.

=== ARTICLE: ind.product_catalog_extend_productdiscoverycontext_context_definition.htm ===
---
article_id: ind.product_catalog_extend_productdiscoverycontext_context_definition.htm
title: Extend the ProductDiscoveryContext Context Definition
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_extend_productdiscoverycontext_context_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_context_definitions_for_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Extend the ProductDiscoveryContext Context Definition

To add the nodes, attributes, mappings, and tags for your qualification procedure, extend the ProductDiscoveryContext context definition.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To extend context definitions:	Context Service Admin

Product Catalog Management provides a Product Discovery Context Definition template for you. However, you can't edit this out-of-the-box template. Instead you must extend the context definition to make a version that you can customize.

NOTE

Extend context definitions instead of cloning them. When you extend a context definition, you can use the Sync option to easily upgrade the extended definitions to their latest version. Extending a context definition also ensures that all the mandatory mappings are preserved.

Before you extend the built-in context definition, check to see if there's an extended context definition you can use. Some organizations already have a customizable context definition called BrowseProductsCtxDefinition. If so, you can simply customize the existing context definition.

To extend the Product Discovery Context Definition, follow these instructions:

From Setup, in the Quick Find box, enter Context Service, and then select Context Definitions.
On the Standard Definitions tab, click  corresponding to ProductDiscoveryContext, and then select Extend.
See Extend Context Definition.
Enter a name, ensure that ProductDiscoveryContext is selected in the Inherited From field, and click Next.
If you don’t need to map the attributes in the CategoryProduct node to Product object fields, use the default mapping. To map the attributes in the CategoryProduct node to Product object fields, create a custom mapping.
On the Map Data tab, click Add Mapping.
Enter a name and description.
Ensure that the Automatic Salesforce object mapping and the Mark as Default checkboxes are deselected.
On the Mapping Intent Details page, ensure that Association, Hydration, Persistence, and Translation are selected.
Click Map.
Map CategoryProduct attributes to Product fields.
Save the changes.
On the Map Data tab, from the Context Definition dropdown of the new mapping, select Input Mapping.
Click Generate All Mappings.
In the Generate all mappings? window, click Retain and Generate.
Save the changes.
Click  corresponding to ProductDiscoveryMapping, and then click Edit.
Deselect Mark as Default.
Click  corresponding to the new mapping, and then click Edit.
Select Mark as Default.
Add the nodes and attributes that are required for qualification or disqualification of products and categories.
See Create Context Definitions.
IMPORTANT To use object mapping, make sure that the node has an “id” attribute and a corresponding unique tag.
Map the nodes and attributes to the corresponding entities and fields.
See Add Context Mapping.
Activate the context definition.

Update the context definition in:

Product Discovery Pricing Procedures
Qualification Rule Procedure
Product Discovery Settings
SEE ALSO
Trailhead Module: Context Service Basics

=== ARTICLE: ind.product_catalog_faceted_search.htm ===
---
article_id: ind.product_catalog_faceted_search.htm
title: Faceted Search
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_faceted_search.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_index_and_search_of_product_catalog.htm
fetched_at: 2026-09-04
---

# Faceted Search

Faceted search improves the search experience by allowing users to refine search results using multiple criteria, such as price, brand, or color. This feature lets customers quickly narrow down extensive product catalogs to find exactly what they need with fewer clicks. By simplifying the discovery process, faceted search saves users time and effort, ensuring greater search accuracy and efficiency, particularly in large catalogs.

REQUIRED EDITIONS
View supported products and editions.

Standard or custom fields on the Product object can be filterable. Additionally, you can make the fields that are common to the Product Attribute Definition object and Product Classification Attribute objects filterable.

Facets are nothing but filters. Facets that you configure are rendered as filters on product discovery product list page.

NOTE

Only Boolean, pick list, and multipicklist fields are filterable.

Configure Filterable Fields & Attributes
Specify the fields and attributes that your sales reps can use as filters on the product discovery product list page. By configuring filterable fields and attributes, you help sales reps quickly narrow down search results to find the products they need.
Configure the Number of Facets Displayed
You can now define a facet limit to control the number of dynamic facets shown on your Product Discovery list page. In addition, you can also define the number of values shown for each facet. This feature overrides the default display, ensuring only the specified number of facets are visible.
Verify the Facets on the Product Discovery Product List Page
Now that we have set up filterable fields and attributes, let's check the facets on the product discovery product list page. We want to see how the search experience has changed with the facets configured.
Configure Dynamic Product Facets
With Dynamic Product Facets, your users can find products faster on the Product Discovery List page. Dynamic Product Facets automatically selects, orders, and shows the most relevant facets, including the category facet.

=== ARTICLE: ind.product_catalog_group_cardinality.htm ===
---
article_id: ind.product_catalog_group_cardinality.htm
title: Manage Group Cardinality
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_group_cardinality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_local_cardinality_and_group_cardinality.htm
fetched_at: 2026-09-04
---

# Manage Group Cardinality

Bundled products are grouped under product groups. You can control the number of components that can be added to the bundle hierarchy in the runtime through product group cardinality.

REQUIRED EDITIONS
View supported products and editions.

Group cardinality defines the minimum and maximum number of child components that users can add at run time. Add a nested child group, a product classification, or multiple product components to a root group.

With nested groups, the cardinality of the parent group defines the minimum and maximum number of child groups from which users can select products at run time. When the nested group contains a product classification, the nested group cardinality dictates the minimum and maximum number of product classification-based products that your users can add at run time.

IMPORTANT When you use nested groups, the cardinality of groups that contain child groups isn’t enforced at run time. Only the cardinality of the group at the lowest-level is enforced at run time.

When the nested group contains products, the cardinality of the nested group defines the minimum and maximum number of products that users can select at run time.

Here are the available group cardinality options.

FIELD	DESCRIPTION
Max Number of Components	The maximum number of distinct components in the group that users can add to the run-time cart.
Min Number of Components	The minimum number of distinct components in the group that users you can add to the run time cart.
NOTE The maximum number of components must be greater than or equal to the minimum number of components.
Edit Group Cardinality
Edit group cardinality to change the minimum and maximum number of distinct components in the group that users can add to the run-time cart.
Override Group Cardinality
You can override the group cardinality of groups that are at the second level and beyond in the product hierarchy. When you override the group cardinality, you update the group cardinality while maintaining a record of the original group cardinality. You can revert to the original cardinality by restoring the default cardinality.
Nested Group Cardinality and Product Classification Component Cardinality
You can add product classification components only under a product group component. The product group component and the product classification component each have their own cardinalities.
Group Cardinality Examples
To better understand how group cardinality works in Product Catalog Management, refer to these examples.

=== ARTICLE: ind.product_catalog_guided_product_selection.htm ===
---
article_id: ind.product_catalog_guided_product_selection.htm
title: Guided Product Selection
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_guided_product_selection.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_discovery.htm
fetched_at: 2026-09-04
---

# Guided Product Selection

Close deals faster and smarter with Guided Product Selection. By using a series of targeted questions accessed through the Guide Me button on your product lists, you'll instantly uncover exactly what your customers need.

REQUIRED EDITIONS
View supported products and editions.
NOTE Guided Product Selection is available only for Salesforce Lightning Service Console users.

To get started with Guided Product Selection, follow all instructions in each section:

Enable Guided Product Selection
Before you configure Guided Product Selection to help users find the right products, you must enable Product Discovery, Discovery Framework, Omnistudio, and Guided Product Selection. Then, deploy a predefined template to create an Omniscript that’s used to configure questionnaires.
Create and Deploy Requirement Assessment Forms for Guided Product Selection
For each requirement that you want to provide guidance for, create a set of questions, add the questions to a form, add logic to the form, and deploy the form. When your users (such as sales reps and customers) answer these questions, Guided Product Selection uses the answers to show the most suitable products.

=== ARTICLE: ind.product_catalog_include_or_exclude_picklist_values_in_a_product_attribute.htm ===
---
article_id: ind.product_catalog_include_or_exclude_picklist_values_in_a_product_attribute.htm
title: Include or Exclude Picklist Values in a Product Attribute
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_include_or_exclude_picklist_values_in_a_product_attribute.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_products.htm
fetched_at: 2026-09-04
---

# Include or Exclude Picklist Values in a Product Attribute

A product that’s based on a product classification, inherits all the product classification attributes including any included or excluded picklist values. To include or exclude specific picklist values for product attributes of the data type picklist, use Include or Exclude Picklist Values. The included picklist values are available at run time while excluded picklist values are unavailable at run time.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To include or exclude picklist values:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Products.
On the Products list view page, click a product.
Go to the Attributes tab.
In the Overridden Inherited Attributes section, click  next to the attribute, and select Include or Exclude Picklist Values.
This option is available for configured product attributes of only the data type picklist.
In the Include or Exclude Picklist Values window, deselect values that you want to exclude, or select values that you want to include.
All the picklist values are selected (included) by default.

You can include or exclude only active picklist values that aren’t the default values for a product classification attribute or a product attribute.

Save your changes.

=== ARTICLE: ind.product_catalog_include_or_exclude_picklist_values_in_a_product_classification_attribute.htm ===
---
article_id: ind.product_catalog_include_or_exclude_picklist_values_in_a_product_classification_attribute.htm
title: Include or Exclude Picklist Values in a Product Classification Attribute
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_include_or_exclude_picklist_values_in_a_product_classification_attribute.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_classifications.htm
fetched_at: 2026-09-04
---

# Include or Exclude Picklist Values in a Product Classification Attribute

For product classification attributes of the data type picklist, all the picklist values are included by default. To exclude specific picklist values and ensure they’re unavailable to products at run time, use Include or Exclude Picklist Values. Use the same functionality to include picklist values when your requirements change.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To include or exclude picklist values:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Product Classifications.
On the Product Classifications list view page, click a product classification.
Go to the Attributes tab.
To include or exclude picklists from an attribute, click  next to the attribute, and then select Include or Exclude Picklist Values.
This option is available for attributes of only the data type picklist.
In the Include or Exclude Picklist Values window, deselect values that you want to exclude, or select values that you want to include.
All the picklist values are selected (included) by default.

You can include or exclude only active picklist values that aren’t the default values for a product classification attribute or a product attribute.

Save your changes.

=== ARTICLE: ind.product_catalog_include_or_exclude_picklist_values_in_overridden_product_attributes.htm ===
---
article_id: ind.product_catalog_include_or_exclude_picklist_values_in_overridden_product_attributes.htm
title: Include or Exclude Picklist Values in Overridden Product Attributes
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_include_or_exclude_picklist_values_in_overridden_product_attributes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_bundled_products.htm
fetched_at: 2026-09-04
---

# Include or Exclude Picklist Values in Overridden Product Attributes

Override product attributes to create the override in the context of a product bundle. To include or exclude specific picklist values for overridden product attributes of the data type picklist, use Include or Exclude Picklist Values. The included picklist values are available at run time while excluded picklist values are unavailable at run time.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To include or exclude picklist values:	Manage Product Catalog
From the Product Catalog Management app’s home page, click Products.
From the product list view page, click a bundled product.
Go to the Structure tab.
Click the product component tile.
In the right panel, go to the Attributes tab.
Click  next to the overridden product attribute, and select Include or Exclude Picklist Values.
This option is available for overridden product attributes of only the data type picklist.
In the Include or Exclude Picklist Values window, deselect values that you want to exclude, or select values that you want to include.
All the picklist values are selected (included) by default.

You can include or exclude only active picklist values that aren’t the default values for a product classification attribute or a product attribute.

Save your changes.

=== ARTICLE: ind.product_catalog_index_and_search_of_product_catalog.htm ===
---
article_id: ind.product_catalog_index_and_search_of_product_catalog.htm
title: Product Index and Search in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_index_and_search_of_product_catalog.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_search_options_for_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Product Index and Search in Product Catalog Management

Enable sales reps to find products quickly and easily with an index of all the products available across catalogs. Specify searchable fields and attributes that users can use to search the index for products.

REQUIRED EDITIONS
View supported products and editions.

After you define your seachable fields, your sales reps and other users can then search for products more easily. For example, searching for products with a specific SKU, or products of a specific color, display, and size

To get started with product index and search, refer to these instructions:

Manage Your Product Index
To utilize product search and discoverability, you must maintain an accurate index of the product fields and attributes in your product catalog.
Configure Searchable Fields & Attributes
Specify the indexed fields and attributes you want to be searchable by sales reps and customers to find relevant products.
Search Considerations When Using Indexed Data
When users search for a product by using a search term, Product Catalog Management checks for an exact match to the search term. If it can't find an exact match, PCM uses typo correction to help users find the product they're looking for.
Faceted Search
Faceted search improves the search experience by allowing users to refine search results using multiple criteria, such as price, brand, or color. This feature lets customers quickly narrow down extensive product catalogs to find exactly what they need with fewer clicks. By simplifying the discovery process, faceted search saves users time and effort, ensuring greater search accuracy and efficiency, particularly in large catalogs.
Partial Search
Partial search helps you find products by entering an incomplete product code or product SKU. It matches the term that you enter to any part of the product code or product SKU, ignoring special characters such as hyphens, underscores, spaces, periods, and slashes.

=== ARTICLE: ind.product_catalog_index_products.htm ===
---
article_id: ind.product_catalog_index_products.htm
title: Manage Your Product Index
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_index_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_index_and_search_of_product_catalog.htm
fetched_at: 2026-09-04
---

# Manage Your Product Index

To utilize product search and discoverability, you must maintain an accurate index of the product fields and attributes in your product catalog.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To build and rebuild indexes:	

Manage Product Index and Search

AND

View Product Catalog

Rebuild your index whenever you add, change, or remove items. There are two index rebuild options: Full and Partial.

Use the Full Index Rebuild to rebuild the entire search index, including changes to index settings and structural changes. Use the Partial Index Rebuild to update recent changes to products and assignment categories.

To help you decide when to run a Full or Partial index, refer to the scenarios listed in the table.

Changes	Full Index Rebuild	Partial Index Rebuild
Modification of the Manage Fields & Attributes tab in the search configuration.	Applicable	Not Applicable
Modification of the Index Settings tab for localization, such as updating the supported and default languages.	Applicable	Not Applicable
Modification to the Product Specification Type and the Product Specification Record Type.	Applicable	Not Applicable
Modification to the Attribute Picklist value when configured with the Attribute Definition.	Applicable	Not Applicable
Modification of the Data Translation settings.	Applicable	Not Applicable
Attribute values, such as overriding the picklist values, changing the default values, excluding the picklist values, etc.	Applicable	Applicable
Modification of the product field values.	Applicable	Applicable
Modification of the attribute values, such as overriding the picklist values, changing the default values, excluding the picklist values, and etc.	Applicable	Applicable
Modification of the product category assignments.	Applicable	Applicable
Modification of the product data translation values.	Applicable	Applicable

By default, you can fully index up to 1,000,000 products and you can partially index up to 2,000 products.

When you rebuild the search index, consider these factors.

If the indexing excludes some products because the individual product size exceeds the limit, contact Salesforce Customer Support.
You can rebuild the search index up to 60 times per hour. We recommend you to wait at least 5 minutes between full index rebuilds.
After you initiate a rebuild of an index, we recommend that you wait a few minutes before initiating another rebuild. Rebuilding indexes too quickly results in an error.

To get started with your product index, follow these instructions:

Build the Product Index
Rebuild the index every time you add or remove products, change product information, or change search options so that the data accessible to run-time systems is up to date. When the rebuilding is in progress, Product Catalog Management continues to use the existing index. Product Catalog Management uses the updated index only after the index rebuild process is complete.
Product Catalog Index Errors and Troubleshooting
Updating the index can, at times, cause errors in products or even index failures. On the Indexes page of the Index and Search Configuration tile, review the different error scenarios and the corresponding actions you can take when updating the index.
Configure Search Index Localization
Localize your search by configuring the index settings. Choose supported languages and set the default language for your search index.

=== ARTICLE: ind.product_catalog_index_settings.htm ===
---
article_id: ind.product_catalog_index_settings.htm
title: Configure Search Index Localization
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_index_settings.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_index_products.htm
fetched_at: 2026-09-04
---

# Configure Search Index Localization

Localize your search by configuring the index settings. Choose supported languages and set the default language for your search index.

REQUIRED EDITIONS

Enable translations and languages. See Set Up Data Translation

NOTE To add data translations, make sure to enable the Translation Workbench and add active languages.
View supported products and editions.
USER PERMISSIONS
NEEDED
To build and rebuild indexes:	

Manage Product Index and Search

AND

View Product Catalog

From the Product Catalog Management app’s home page, click Index and Search Configuration.
Click Index Settings.
Choose the supported languages, and save your changes.
You can choose up to a maximum of 25 supported languages.
Set the default language, and save your changes.
If the user language isn't part of the supported languages, the default language is used.

After configuring the index settings, a full index rebuild is required to apply the changes effectively.

=== ARTICLE: ind.product_catalog_index_the_product_catalog.htm ===
---
article_id: ind.product_catalog_index_the_product_catalog.htm
title: Build the Product Index
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_index_the_product_catalog.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_index_products.htm
fetched_at: 2026-09-04
---

# Build the Product Index

Rebuild the index every time you add or remove products, change product information, or change search options so that the data accessible to run-time systems is up to date. When the rebuilding is in progress, Product Catalog Management continues to use the existing index. Product Catalog Management uses the updated index only after the index rebuild process is complete.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To build and rebuild indexes:	

Manage Product Index and Search

AND

View Product Catalog

NOTE If the index rebuild fails, Product Catalog Management continues to use the active index.
From the Product Catalog Management app’s home page, click Index and Search Configuration.

To index the product catalog for the first time, click Create Full Index.

To rebuild the index after a change to product data or search configuration, click Rebuild Index.
Select index rebuilding option, and click Rebuild.

Each time you rebuild the full or partial index, a new log entry is added to the Rebuild History section, enabling the user to track the rebuild activity. The Build Status will show In Progress for the duration of the rebuild operation. Once the index operation is successful, click the Refresh icon to view the modifications in the Rebuild History section. You can view the Activation Status in the Index Summary section.

Starting a partial or full index rebuild cancels any rebuilds that are in progress and initiates a new index rebuild.

SEE ALSO
Product Catalog Index Errors and Troubleshooting

=== ARTICLE: ind.product_catalog_index_troubleshooting.htm ===
---
article_id: ind.product_catalog_index_troubleshooting.htm
title: Product Catalog Index Errors and Troubleshooting
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_index_troubleshooting.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_index_products.htm
fetched_at: 2026-09-04
---

# Product Catalog Index Errors and Troubleshooting

Updating the index can, at times, cause errors in products or even index failures. On the Indexes page of the Index and Search Configuration tile, review the different error scenarios and the corresponding actions you can take when updating the index.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management

Check out the different error scenarios and the corresponding actions you can take when updating the search index:

INDEX UPDATE STATUS	SCENARIO	MAPS TO	ACTION
Completed	Index completed without product errors	Completed status in Rebuild History	None
Index completed with product errors	Product error warning	Download the CSV file and resolve the product errors.
Failed	Index failed without product errors	Index failure banner	Use the information in the failure message to resolve the issue.
Index failed with product errors	
Index failure banner
Product error warning
	
Use the information in the failure message to resolve the issue.
To resolve the product errors, download the CSV file in the warning message.
NOTE

The ErrorAttributeDataSizeLimitExceeded code in the CSV file indicates that you have reached the data size limit for all localized and nonlocalized attributes of a product for a single locale. Review your products to see if you can reduce the data indexed for search. For additional help, contact Salesforce Customer Support.

In case of product errors or index failures, Salesforce recommends that you rebuild the index after resolving issues.

=== ARTICLE: ind.product_catalog_introduction.htm ===
---
article_id: ind.product_catalog_introduction.htm
title: Build Your Product Catalog in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_introduction.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
fetched_at: 2026-09-04
---

# Build Your Product Catalog in Revenue Management

Product Catalog Management enables administrators and designers to create robust catalogs for any business. Accelerate your sales with personalized, browsable product offerings. Simplify complex catalog management, and ensure relevant products reach customers across all channels, from brick-and-mortar stores to ecommerce platforms and beyond.

REQUIRED EDITIONS
View supported products and editions.
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.
Learn About Product Catalog Management

Listen to this podcast-style Audio Tour which introduces the key features of Product Catalog Management and how they work together. The audio features an AI-generated conversation between two database administrators.

NOTE After you've had a chance to listen to the Audio Tour, head over to Trailhead and visit the Product Catalog Management: Quick Look.
Product Catalog Management Architecture

For quick reference, here's a diagram showing how the key elements of Product Catalog Management fit together.

Ready to Jump In?

To get started with Product Catalog Management, refer to these resources. In general, we recommend working through these sections in order.

Begin Using Product Catalog Management
Review the supported products, editions, and permission sets for Product Catalog Management (PCM). Tailor the experience of using PCM for all users using permission sets to give them precise access to what they need.
Product Catalog Management Set Up
Product Catalog Management includes different permission sets for users. These users or personas perform various roles in implementing and managing your product portfolio. Configure your users to use Product Catalog Management and assign permission sets so that the users can access catalogs, products, attributes, rules, context definitions, product bundles, and more. To complete the setup of Product Catalog Management, adjust the page layout and field access on the product object.
Plan Your Product Catalog
Learn how to plan your product catalog implementation and explore sample catalog configurations.
Organize Your Products with Catalogs and Categories
A catalog is a collection of the products that you sell, organized into categories for easier browsing. You must create a catalog before you create catalog categories and assign products to the categories.
Manage Dynamic Attributes in Revenue Management
Attributes are the key characteristics or properties of products. Define your attributes, and then assign them to your products using product classifications.
Create Product Templates Using Product Classifications
Product classifications are templates that organize your product catalog and streamline product creation. Define attributes once, and let subclassifications automatically inherit them, while still allowing you to manually override attributes as needed. Product classifications help you maintain data consistency and reduce repetitive manual tasks, allowing you to quickly define and launch products with shared characteristics.
Create Products and Product Bundles in Revenue Management
Products are all the items and services that you sell to customers. There are two types of products: simple products and bundled products. Simple products are single-element products with no dependencies on any other products. Bundled products are a group of products that are sold together as one unit.
Create Product Variants in Revenue Management
Use product variants to group related products that share a common identity but differ by specific characteristics. Instead of creating separate, disconnected entries in your catalog for every minor difference, variants help you organize these options logically under a single umbrella record.
Manage Qualification Rules for Products in Revenue Management
Use qualification rules to define the customer eligibility and availability for products, or product categories. Configure qualification rules using criteria such as location, account attributes, purchase history, and more.
Manage Product Selling Model in Revenue Management
Product selling models define how you sell products. The models can be one time, term-defined, or evergreen.
Product Discovery and Guided Product Selection
Use Product Discovery to provide a simple, structured product browsing experience for sales reps and customers to efficiently identify the most suitable products. Users can see product information such as images, description, pricing, product bundle details, and product attributes in a single comprehensive view.
Product Catalog Management Limits
Before you plan and create products, attributes, and a bundled product hierarchy in Product Catalog Management, make sure that you’re aware of the capabilities and limits.

=== ARTICLE: ind.product_catalog_local_cardinality.htm ===
---
article_id: ind.product_catalog_local_cardinality.htm
title: Manage Local Cardinality
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_local_cardinality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_local_cardinality_and_group_cardinality.htm
fetched_at: 2026-09-04
---

# Manage Local Cardinality

Use local cardinality to define if a product component or products based on a product classification are required, are included in the bundle by default, whether their quantities can be changed, and what the minimum and maximum quantities are.

REQUIRED EDITIONS
View supported products and editions.

Here are the available cardinality fields:

CARDINALITY FIELDS	DESCRIPTION
Require this component	Select if the product component is a required component in the product bundle. Deselect if the product component is an optional component in the product bundle. If Require this component is selected, ensure that you select Include component by default. Ensure that Require this component is deselected for a product classification components.
Include component by default	Select if the product component is included in the product bundle by default. Deselect if the product component isn’t included in the product bundle by default. You must select this field if the product component is a required component. Ensure that Include component by default is deselected for product classification components.
Allow quantity changes	

Select if users can edit the product quantity at run time.

If Allow Quantity Changes is deselected, you can’t enter a minimum quantity and maximum quantity.
If the Price includes component field in the product related component record is selected, then you must deselect Allow quantity changes.
NOTE If the product's Quantity Scaling Method is set to Proportional, selecting this checkbox makes the quantity editable, but only when configuring the product in the configurator. Once added to a quote, the quantity field is locked (read-only) in the sales transaction line editor. This happens because the line editor displays the final multiplied quantity stored on the quote line item, rather than the editable per-parent unit quantity.

Price Includes Component	Select when the price of the product bundle includes the price of the component. You can’t change component quantities when you select Price Includes Component.
Quantity Scaling Method	

Defines how the child product quantity changes as the quantity of the parent product changes in the runtime cart. This field can have these values:

None: To change the quantity values of the child product in the run time irrespective of the quantity of the parent product, select Allow Quantity Changes. Deselect Allow Quantity Changes to restrict changes to the quantity values of the child product in the run time irrespective of the quantity of the parent product.
Constant:
The quantity of the child product in the runtime cart remains constant irrespective of the changes to the parent product quantity when the Quantity Scaling Method is set to Constant. You can’t change the child product quantity in runtime. The child product quantity value remains what was defined in design time in Product Catalog Management.
You must deselect Allow Quantity Changes when the Quantity Scaling Model is set to Constant.
Proportional:
This is the default value for the Quantity Scaling Method when Allow Quantity Changes isn’t selected in the Specify Component Details window. The Quantity Scaling Method is set to None when the Allow Quantity Changes is selected in the Specify Component Details window.
When the Quantity Scaling Method is set to Proportional, the quantity of the child product in the runtime cart changes in proportion to the changes to the parent product quantity. For example, if the parent product quantity is A and the child product quantity is B, then the runtime cart has A number of parent products, but A multiplied by B number of child products.

Min Quantity	The minimum number of product components or products based on a product classification in the bundle.
Max Quantity	The maximum number of product components or products based on a product classification in the bundle.
Quantity	The default number of product components or products based on a product classification in the bundle.
Edit Local Cardinality
To define the default, minimum, and maximum quantity of a product that’s permissible in the product bundle, edit the local cardinality of the product component and the product classification component.
Override Local Cardinality
You can override the cardinality of product components and product classification components that are at the second level and beyond in the product hierarchy. When you override the local cardinality, you update the product component or product classification component cardinality while maintaining a record of the original local cardinality. You can revert to the original cardinality by restoring the default cardinality.

=== ARTICLE: ind.product_catalog_local_cardinality_and_group_cardinality.htm ===
---
article_id: ind.product_catalog_local_cardinality_and_group_cardinality.htm
title: Define Quantity Limits for Bundled Products
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_local_cardinality_and_group_cardinality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_bundled_products.htm
fetched_at: 2026-09-04
---

# Define Quantity Limits for Bundled Products

For bundled products businesses can limit, or require, the quantity of items purchased. For example, an airline that offers up to two companion fares for each frequent flyer customer. In Product Catalog Management, use local and group cardinality to create these quantity limitation rules.

REQUIRED EDITIONS
View supported products and editions.
Local Cardinality

Local cardinality defines if a product component or products based on a product classification component are required, are included in the bundle by default, and whether their quantities can be changed. When the quantity can be changed, use local cardinality to define the default, minimum and maximum quantities of the product that are allowed in the product bundle.

Consider a scenario where you want to allow users to purchase up to two double beds. In this case, define the local cardinality with the minimum quantity as 1, the maximum quantity as 2, and the default quantity as 1. With this cardinality, if users enter quantity 3, they’re notified that they can add only up to two beds.

Group Cardinality

Group cardinality defines the minimum and maximum number of child components that users can add at run time. You can add a nested child group, a product classification, or multiple product components to a root group.

Consider a scenario where you have a group of 4 types of beds and you want to allow users to select a minimum of 1 bed and a maximum of 3 beds. In this case, define the group cardinality with the minimum components as 1 and the maximum components as 3.

Manage Local Cardinality
Use local cardinality to define if a product component or products based on a product classification are required, are included in the bundle by default, whether their quantities can be changed, and what the minimum and maximum quantities are.
Manage Group Cardinality
Bundled products are grouped under product groups. You can control the number of components that can be added to the bundle hierarchy in the runtime through product group cardinality.

=== ARTICLE: ind.product_catalog_manage_and_view_constraints_for_a_product.htm ===
---
article_id: ind.product_catalog_manage_and_view_constraints_for_a_product.htm
title: Manage and View Constraints for a Product
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_manage_and_view_constraints_for_a_product.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_bundled_products.htm
fetched_at: 2026-09-04
---

# Manage and View Constraints for a Product

Maintain a unified user experience for product definitions and constraint rules. Manage, view, and activate all constraints associated with a product from a single location.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To manage and view constraints:	

Manage Product Catalog

Product Configuration Constraints Designer permission set

From the Product Catalog Management app’s home page, click Products.
Select the product for which you want to view the constraints.
Click the Constraints tab.

Here you can view and manage constraint models for the selected product.

Click Add Item and select the products that you want to add to the CML editor.
If product indexing is enabled, products appear in the Add Item drop down after a partial or full indexing process is executed.

=== ARTICLE: ind.product_catalog_manage_qual_rule_components.htm ===
---
article_id: ind.product_catalog_manage_qual_rule_components.htm
title: Manage Qualification Rule Components
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_manage_qual_rule_components.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_qualification_rules.htm
fetched_at: 2026-09-04
---

# Manage Qualification Rule Components

To fine-tune your qualification rules, modify or deactivate its components.

REQUIRED EDITIONS
View supported products and editions.
SEE ALSO
Simulate and Active a Qualification Rule Procedure
Deactivate a Qualification Rule Procedure Version

You can’t edit active rule procedures. To edit a rule procedure, first deactivate the version.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To deactivate a qualification rule procedure:	Manage Product Catalog
To use a decision table:	Rules Engine Runtime
To create a context definition:	Context Service Admin
From the Product Catalog Management app’s home page, click Qualification Rules Procedures.
From the Qualification Procedures list view, click a qualification.
On the Qualification Procedures details page, click the qualification procedure under Qualification Procedure Versions.
On the expression set builder page, click Deactivate.
You can now edit the qualification rule procedure. After you save your changes, activate the rule procedure.
Edit a Qualification Rule Procedure

Edit a qualification rule procedure, or add new fields in the associated decision table and context definition.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To create a qualification rule procedure:	Manage Product Catalog
To use a decision table:	Rules Engine Runtime
To create a context definition:	Context Service Admin
Add Custom Fields to the qualification rule objects as necessary.
Modify or add nodes and attributes in an active context definition.
Deactivate the qualification and pricing procedures that are using the context definition.
Deactivate the context definition.
Edit the nodes and attributes.
Activate the context definition.
To add nodes and attributes to a context definition, edit the context definition.
Deactivate the decision table, update the decision table to use the new fields, and then activate the decision table.
To create a new version of the qualification rule procedure, update the qualification rule procedure and add mappings to the new fields.
Simulate the updated qualification procedure version, and then activate it if it meets your requirements.
Deactivate a Decision Table in Revenue Management

You can’t edit active decision tables. Deactivate a decision table, add new rules or modify existing rules, and then activate the decision table. The changes don't take effect until you deactivate and activate the decision table.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To deactivate the decision table:	

Manage Product Catalog

AND

Rules Engine Designer

AND

Context Service Runtime


To use a decision table:	Rules Engine Runtime
From the Product Catalog Management app’s home page, click Qualification Rules.
From the Qualification Decision Tables list view page, click the decision table that you want to deactivate.
Click Deactivate.
You can now edit the decision table to add new qualification rules, or delete or edit existing qualification rules. After you save your changes, activate the decision table. When you activate the decision table, the changes to the rules are applied to the objects, and the decision table shows the new rules.

=== ARTICLE: ind.product_catalog_management_essentials.htm ===
---
article_id: ind.product_catalog_management_essentials.htm
title: Product Catalog Management Essentials
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_management_essentials.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.revenue_impl_glossary.htm
fetched_at: 2026-09-04
---

# Product Catalog Management Essentials

Browse through this collection of terms, key objects, and key concepts. This collection is designed to give Salesforce admins, sales reps, and developers a clear and consistent understanding of Product Catalog Management (PCM) concepts and helps them navigate the PCM landscape.

Attributes
Attributes are the characteristics or properties that define products and product classifications. They are also referred to as Dynamic Attributes.
Attribute Categories
You can group attributes into logical groups called attribute categories. Attribute categories help users easily find and use the right attributes when they create product classifications. You can assign attributes to product classifications individually or through an attribute category.
Attribute Fields
Attribute Fields are special fields that affect how attributes behave at run time. You can update these field values when you edit product classification attributes or configure product attributes.
Attribute Inheritance
This process helps a product automatically obtains a set of dynamic attributes from its associated Product Classification. These attributes are available to the product even if you haven’t explicitly defined them.
Auto Save
Auto Save ensures that when a product is added from the catalog, it is automatically saved to the transaction line without requiring a manual save action. This ensures the transaction preview stays perfectly in sync and helps sales reps to continue browsing and adding products seamlessly.
Bundled Products
Bundled products are a group of products that are sold together as one unit. You can create static or dynamic bundled products. For static products, you can’t add or remove child products, alter product quantities, or configure product attributes at run time. For configurable products, you can add or remove child products, alter product quantities, and configure product attributes at run time.
Catalog
A catalog is a collection of the products that you sell, organized into categories for easier discoverability. You must create a catalog before you create catalog categories and assign products to the categories.
Category
Organize and group products in your catalog by creating catalog categories and catalog subcategories. Assign products to more than one catalog category and subcategory. The Categories tab shows a hierarchical view of categories that you can expand or collapse to show or hide the catalog subcategories.
Decision Tables
Advanced lookup tables can provide multiple matching outcomes for the same set of inputs. Decision tables can read rules from Salesforce objects and support various operators for each field within the object.
Dynamic Bundle
A bundle with complex hierarchy that's configurable at run time. A Dynamic bundle is a complex product hierarchy that starts with a root product and includes child products, product component groups, or product classes as children. The parent-child relationship can be multilevel.
Faceted Search
Facets offer an effective way to filter your search results, allowing you to quickly find the products you need by narrowing results based on selected criteria. For example, when searching for a phone, you can filter by attributes such as color, screen size, storage capacity, memory. Auto-faceting also displays relevant filters based on the selected category or search keyword.
Global Search
A search that helps users find desired products on the Product List page of Product Discovery.
Group Cardinality
Group cardinality defines the minimum and maximum number of child products that users can add in the run time across the group’s immediate child products.
Guided Product Selection
A feature that uses dynamic questions to identify requirements and show matching products. Users can click the Guide Me button on the Product List page to show personalized list of products. Available only in Salesforce Lightning Service Console.
Local Cardinality and Group Cardinality
A product bundle consists of multiple products sold as a single package. You can define cardinality for each product within the bundle, which ensures that the correct quantities are added to the cart.
Local Cardinality
Use local cardinality to determine whether a product component or products based on a product classification component are required, included in the bundle by default, and whether their quantities can be changed. When quantities can be changed, use local cardinality to set the default, minimum, and maximum quantities allowed in the product bundle. You can adjust quantities only if the price of the bundle doesn’t include the price of the product component or the product classification component.
Nested Bundle
The ability within Product catalog management for users to define a *Bundle* component that contains another existing *Bundle*, enabling modularity and reuse.
Nested Product Component Groups
It's a nesting of groups for better organisation of related products in a bundle.
Picklists
Attributes of the data type picklist can have multiple values. Picklists represent all possible values for such attributes. Users choose one of these values when they purchase a product. You must define picklists before you create attributes for the picklist data type.
Products
Products are all the items and services that you sell to customers. Products can also be nonsellable. There are two types of products: simple products and bundled products. Simple products don’t have an associated product hierarchy, while bundled products generally have one. Bundled products are a group of products that are sold together as one unit.
Product Category Qualification Rules
Product categories are a group of products that are categorized in a certain way for sale. Product category qualification rules evaluate the availability and eligibility of product categories during browsing.
Product Classifications
A product classification is a template that you can use to quickly define and create products. Product classifications hold a collection of dynamic attributes. You can reuse product classifications to create multiple products that are similar yet different. You can also organize your product catalog by building classification hierarchies with up to three levels of subclassification. Each subclassification inherits attributes from its parent, with the flexibility to include additional attributes as needed. This approach helps you create and manage related product classes more efficiently.
Product Component Attributes Override
You can override the attributes of product components in the context of the product bundle. This mechanism is called overriding the bundle component attributes. This mechanism doesn’t change the attributes on the product that’s used as a component. The changes remain localized to the bundle that you’re overriding the attributes in.
Product Cache
Caching solution adds a caching layer to quickly retrieve product details. Product related details uses the Product Catalog Management cache to access the frequently used product details without reloading them from the source every time.
Product Details Page (PDP)
This page shows detailed product information, such as product attributes, bundle hierarchy, and pricing, when a sales rep selects a product.
Product Discovery
Product Discovery offers a simple, structured browsing experience for sales reps and customers to efficiently identify the most suitable products. Product Catalog Management ensures a seamless product discovery experience for sales reps when browsing products on the Product List and Product Details pages.
Product Recommendations
Product recommendations are contextual, rule-based suggestions that surface directly in the user interface based on the current transaction. These recommendations are driven by predefined configuration rules and honor all existing qualification rules. Product recommendations help sales reps to identify and add compatible products directly from a recommendations list.
Product Relationships
A product can be related to another product. The relationship can be parent-child. For example, bundled products consist of components such as groups, products, and product classifications. These components are related to each other through product relationships.
Product Specification
Define product specification types unique to your industry. These types are linked to product specification record types, which are associated with the Product object. The record type determines whether a product is sold commercially.
Product Qualification Rules
Products are the items and services that you sell. Qualification rules evaluate the products’ availability and eligibility when users browse the products. By default, only qualified products are visible to users. You can view disqualified products as well, but you can’t purchase them.
Product Selling Model
Product selling models define how you sell products. The models can be one-time, term-defined, or evergreen. For example, a phone is sold one time or in a term of 12 months. However, the cellular data plan is billed monthly in an evergreen model until the user cancels the plan. Product selling model is an optional feature.
Product Variants
Product variants are a group of related products that share a common core design but differ in specific attributes, such as size or color. This structure simplifies catalog management and streamlines the browsing experience. Instead of scrolling through multiple individual product records, sales reps can view a single parent product and select the required configuration or options the customer needs.
Qualification Procedure Elements
Qualification Procedure Elements are the building blocks of expression sets. Product Catalog Management supports two elements.
EvaluateQualification: Evaluates rules of type qualification by looking up the decision tables based on objects that store qualification rules.
EvaluateDisqualification: Evaluates rules of type disqualification by looking up the decision tables based on objects that store disqualification rules.
Qualification Rules
Use qualification rules to define ‌customer eligibility and availability for products, or product categories. Eligibility and availability criteria include location, account attributes, and other related information.
A product or product category is qualified only if you’ve defined a qualification rule and the product or the product category meets the qualification.
Qualification Rule Object
The source object that contains the rules. The columns of the object act as criteria, and each row in the object represents a rule. You can look up these objects faster by creating a decision table for each object.
Simple Products
Products that don't have any parent-child relationship with other products. Their product type is None.
Static Bundle
A complex product hierarchy that starts with a root product and includes child products. The parent-child relationship can be multilevel. This type of bundle can't be configured at run time.
Transaction Preview
Transaction preview is an embedded panel that displays the current transaction in real time alongside the product catalog. It updates automatically as users add or remove products.
Visibility Rule
A visibility rule determines whether a product is displayed or hidden in the product list during product discovery. When constraint rules or disqualification rules apply to a specific product based on the current transaction, the visibility rule automatically hides the affected product from the default view.

=== ARTICLE: ind.product_catalog_nested_group_cardinality_and_product_classification_component_cardinality.htm ===
---
article_id: ind.product_catalog_nested_group_cardinality_and_product_classification_component_cardinality.htm
title: Nested Group Cardinality and Product Classification Component Cardinality
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_nested_group_cardinality_and_product_classification_component_cardinality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_group_cardinality.htm
fetched_at: 2026-09-04
---

# Nested Group Cardinality and Product Classification Component Cardinality

You can add product classification components only under a product group component. The product group component and the product classification component each have their own cardinalities.

Here's an example that demonstrates how the group, nested group, and product classification cardinality determine how many products you can add in your cart at run time.

In this example, we have a parent group called Wardrobes. Mirrored Wardrobes, Sliding Wardrobes, Open Wardrobe, Fitted Wardrobe, and Corner Wardrobe are child groups of the Wardrobes parent group. Here's the cardinality of the Wardrobes parent group:

Minimum number of components: 1
Maximum number of components: 4

At run time, users can select products from a minimum of 1 child group and select products from a maximum of 4 child groups from the 5 available child groups. Let’s assume that a user selects the Mirrored Wardrobes child group.

Mirrored Wardrobes is a nested child group. This nested group has a product classification called Mirrored Wardrobes. Double-door wardrobe, three-door wardrobe, four-door sliding wardrobe, and four-door swing wardrobe are four products based on the Mirrored Wardrobe product classification.

Here's the cardinality for the Mirrored Wardrobes product classification:

Minimum number of components: 2
Maximum number of components: 4

At run time, users can select a minimum of 2 products based on the product classification and a maximum of 4 products. Let’s assume that a user selects the double-door wardrobe and the four-door swing wardrobe.

Mirrored Wardrobe Classification (Product Classification Component)

Minimum Quantity: 1
Maximum Quantity: 2
Default Quantity: 1

At run time, users can select a minimum of one instance of the product and a maximum of 2 instances of the product. That means that a user can select a minimum of 1 double-door wardrobe and a maximum of 2 double-door wardrobes. Similarly, the user can select a minimum of 1 four-door swing wardrobe and a maximum of 2 four-door swing wardrobes.

=== ARTICLE: ind.product_catalog_override_group_cardinality.htm ===
---
article_id: ind.product_catalog_override_group_cardinality.htm
title: Override Group Cardinality
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_override_group_cardinality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_group_cardinality.htm
fetched_at: 2026-09-04
---

# Override Group Cardinality

You can override the group cardinality of groups that are at the second level and beyond in the product hierarchy. When you override the group cardinality, you update the group cardinality while maintaining a record of the original group cardinality. You can revert to the original cardinality by restoring the default cardinality.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To override group cardinality:	Manage Product Catalog
To use the structure tab:	ARC Access permission set
NOTE Overriding the cardinality overrides the cardinality for the group in the context of the root product bundle. The cardinality of the group remains the same in the context of other product bundles.
WARNING Overriding the group cardinality for a group that’s been added multiple times in a bundle, overrides the group cardinality for every instance of the group throughout the bundle. Groups are added multiple times when the product above the group in the hierarchy is added multiple times.
From the Product Catalog Management app’s home page, click Products.
From the Product list view page click the bundled product that contains the group whose cardinality you want to override.
Navigate to the Structure tab.
Click the group tile for the group at the second level in the product hierarchy.
The first product in the bundle hierarchy is the root product. The products, groups, and product classifications at the first level are the immediate child components of the root product. You can edit the cardinality of products, groups, and product classifications only at the first level. You can override the cardinality of products, groups, and product classifications only at the second level and beyond.
In the right pane, navigate to the Cardinality tab.
Click Override.
Overriding the cardinality overrides the cardinality for the group in the context of the product bundle. The original group cardinality is retained and can be reverted to if necessary.
Override the cardinality as necessary.
This example illustrates the original and updated group cardinality values for the group Wooden Beds at the second level. The original group cardinality was minimum 1 component and maximum 2 components. The updated group cardinality is minimum 0 components and maximum 2 components.
Save your changes
The overridden cardinality appears in the right pane. You can edit the overridden cardinality as necessary.

If you want to revert to the original group cardinality, click Restore Default Cardinality. Restoring the default cardinality deletes the overridden cardinality and restores the original group cardinality.

=== ARTICLE: ind.product_catalog_override_local_cardinality.htm ===
---
article_id: ind.product_catalog_override_local_cardinality.htm
title: Override Local Cardinality
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_override_local_cardinality.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_local_cardinality.htm
fetched_at: 2026-09-04
---

# Override Local Cardinality

You can override the cardinality of product components and product classification components that are at the second level and beyond in the product hierarchy. When you override the local cardinality, you update the product component or product classification component cardinality while maintaining a record of the original local cardinality. You can revert to the original cardinality by restoring the default cardinality.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To override cardinality:	Manage Product Catalog
To use the structure tab:	ARC Access permission set
NOTE Overriding the cardinality overrides the cardinality for the product component or product classification component in the context of the root product bundle. The cardinality of the product component or product classification component remains the same in the context of other product bundles.
WARNING Overriding the local cardinality for a product that’s been added multiple times in a bundle, overrides the local cardinality for every instance of the product throughout the bundle.
From the Product Catalog Management app’s home page, click Products.
From the Product list view page, click the bundled product that contains the product component or product classification component whose cardinality you want to override.
Navigate to the Structure tab.
To override the product cardinality, click the product tile for a product at the second level in the product hierarchy. To override the product classification cardinality, click the product classification tile under a group at the second level in the product hierarchy
The first product in the bundle hierarchy is the root product. The products, groups, and product classifications at the first level are the immediate child components of the root product. You can edit the cardinality of products, groups, and product classifications only at the first level. You can override the cardinality of products, groups, and product classifications only at the second level and beyond.
In the right pane, click  next to More, and click Cardinality.
Click Override.
Overriding the cardinality overrides the cardinality for the product component or product classification component in the context of the product bundle. The original product component or product classification component cardinality is retained and can be reverted to if necessary.
Override the cardinality as necessary.
This example illustrates the local and updated cardinality for the product Teak Wood Beds with Storage at the second level. The local cardinality was minimum quantity 1, maximum quantity 2, and default quantity 1. The updated cardinality is minimum quantity 1, maximum quantity 4, and the default quantity 2.
Save your changes.
The overridden cardinality appears in the right pane. You can edit the overridden cardinality as necessary.

If you want to revert to the original product component or product classification component cardinality, click Restore Default Cardinality. Restoring the default cardinality deletes the overridden cardinality and restores the original product component or product classification component cardinality.

=== ARTICLE: ind.product_catalog_override_product_component_attributes_in_bundles.htm ===
---
article_id: ind.product_catalog_override_product_component_attributes_in_bundles.htm
title: Override Product Component Attributes in Bundles
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_override_product_component_attributes_in_bundles.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_bundled_products.htm
fetched_at: 2026-09-04
---

# Override Product Component Attributes in Bundles

You can override the attributes of product components in the context of the product bundle.

REQUIRED EDITIONS
View supported products and editions.
USER
PERMISSIONS NEEDED
To override component attributes:	Manage Product Catalog
To use the Structure tab:	ARC Access permission set

If products are sold separately, see Configure Product Attributes. Perform these steps if products are sold as part of a bundle.

WARNING When you override product attributes for a product that’s added multiple times in a bundle, you override the product attributes for every instance of the product throughout the bundle.
From the Product Catalog Management app’s home page, click Products.
From the product list view page, click the bundled product.
Navigate to the Structure tab.
Click the product component tile.
In the right panel, navigate to the Attributes tab.
Click the action icon associated with the attribute, and select Create Override.
Edit the attribute as necessary and save your changes.
Save your changes.

You can create, edit, and delete product component attribute overrides.

=== ARTICLE: ind.product_catalog_partial_search.htm ===
---
article_id: ind.product_catalog_partial_search.htm
title: Partial Search
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_partial_search.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_index_and_search_of_product_catalog.htm
fetched_at: 2026-09-04
---

# Partial Search

Partial search helps you find products by entering an incomplete product code or product SKU. It matches the term that you enter to any part of the product code or product SKU, ignoring special characters such as hyphens, underscores, spaces, periods, and slashes.

REQUIRED EDITIONS
View supported products and editions.

Partial search works on Product Code and Product SKU fields, if they're marked as searchable. To make the fields searchable, see Configure Searchable Fields & Attributes.

Searches don't require SKU or sku prefixes to return Product SKU results. For example, searching for "12345" returns "SKU-12345".
Searches don't need special characters such as hyphens, underscores, periods, and slashes. For example, searching for "1234567" returns "SKU-1234567".
Search terms must include at least 3 characters for optimal results.
EXAMPLE

If a product Titanium Pro 2026 has the product SKU LP-X1C-2025 and the product code TPX1C:

SEARCH TERM	MATCHES	DESCRIPTION
X1C	Product SKU	Matches the middle of the SKU
2025	Product SKU	Matches the end of the SKU
LP	Product SKU	Matches the beginning of the SKU
TPX or X1C	Product Code	Matches the product code
Configure Partial Search
Find products more efficiently by searching with partial product codes or product SKUs.

=== ARTICLE: ind.product_catalog_permissions_to_access_product_discovery.htm ===
---
article_id: ind.product_catalog_permissions_to_access_product_discovery.htm
title: Assign Product Discovery Permissions
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_permissions_to_access_product_discovery.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.qocal_product_discovery_setup.htm
fetched_at: 2026-09-04
---

# Assign Product Discovery Permissions

To provide users access to Product Discovery data and components, assign the necessary permissions and data access.

REQUIRED EDITIONS
View supported products and editions.
Permissions for Authenticated Users

Authenticated users means both customers with a portal account, and your internal users who need access to Product Discovery.

For internal Salesforce Lightning Console users, and for customers and partners with Experience Cloud accounts, assign the respective Product Catalog Management permission set. See Product Catalog Management Permission Set Licenses.

To provide access to use Guided Product Selection, assign the OmniStudio User permission set in addition to the Product Catalog Management permission set.

NOTE The permission set is available only after Guided Product Selection is set up. Guided Product Selection is available only to Salesforce Lightning Service Console users.
Permissions for Guest Users

Guest users are customer portal visitors who don't have an active portal account.

To the guest user profile, provide the necessary administrative permissions, general user permissions, object and field-level permissions, and data access.

Assign these administrative permissions.
Salesforce Pricing: Run time user
Context Service Run time user
API Enabled
Assign these general user permissions.
Allow access to Product Discovery
Grant users access to Industries Interaction Calculation features
Run Decision Matrices
Run Expression Sets
View Product Catalog for Customer Community User
View Product Catalog via API for Customer Community User
To use Guided Product Selection, select ‘Enables consumers and partners to execute OmniScripts, DRs, Cards through a Community or off platform’
Assign read access to these standard objects. Then for each of these standard objects, edit field-level security and provide read access to all the fields.
Attribute Categories
Attribute Category Attributes
Attribute Definitions
Attribute Picklists
Attribute Picklist Excluded Values
Attribute Picklist Values
Catalogs
Categories
To use qualification or pricing:
Decision Matrices
Decision Matrix Columns
Decision Matrix Column Ranges
Decision Matrix Rows
Decision Matrix Versions
Expression Sets
Expression Set Versions
To use pricing, Price Books
Products
Product Attribute Definitions
Product Category Disqualifications
Product Category Products
Product Category Qualifications
Product Classifications
Product Classification Attributes
Product Component Groups
Product Component Group Overrides
Product Disqualifications
Product Qualifications
Product Related Component Overrides
Product Relationship Types
Product Selling Models
Product Specification Record Types
Product Specification Type
To use ramp deals, Product Ramp Segment
NOTE The Product Ramp Segment object is available only when you have Revenue Management and Ramp Deals enabled.
To use usage-based pricing, Unit Of Measure
NOTE The Unit of Measure object is available only when you have Revenue Management and Ramp Deals enabled.

=== ARTICLE: ind.product_catalog_picklists.htm ===
---
article_id: ind.product_catalog_picklists.htm
title: Manage Attribute Picklists in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_picklists.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_dynamic_attributes.htm
fetched_at: 2026-09-04
---

# Manage Attribute Picklists in Revenue Management

Picklists allow you to define multiple values for a given attribute. For example, colors for t-shirts or sizes of pants. To use picklists with your attributes, you must define your picklists first before creating the attributes.

REQUIRED EDITIONS
View supported products and editions.

You can reuse picklists by associating them with more than one attribute. For example, you can create a picklist Color with values such as Blue, Red, Silver, and White, and then use that picklists for all attributes that share those colors.

When creating picklists, you can choose one of these data types to define your picklist values:

Boolean
Date
Datetime
Number
Text
Currency
Percent
Create Attribute Picklists
Follow these instructions to create an attribute picklist. You must create your picklists first before you create attributes of type picklist.

=== ARTICLE: ind.product_catalog_plan_catalog.htm ===
---
article_id: ind.product_catalog_plan_catalog.htm
title: Plan Your Product Catalog
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_plan_catalog.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Plan Your Product Catalog

Learn how to plan your product catalog implementation and explore sample catalog configurations.

REQUIRED EDITIONS
View supported products and editions.
NOTE If you're not familiar with Product Catalog Management (PCM) basics, we recommend starting with these Trailhead resources:
Discover PCM
Set Up Your Product Offerings
Core Concepts

Planning your product catalog starts with assessing all your product and service offerings and translating them into the data model that Product Catalog Management uses.

At its core, Product Catalog Management consists of catalogs, categories, dynamic attributes, product, and of course the products themselves.

Catalogs and categories are your high-level organizational tools. Dynamic attributes specify the characteristics of each individual product. You assign attributes to products using product. Additionally, products can be sold individually or bundled and sold together as a package.

Let's unpack these elements a bit more and explore how you can implement your product catalog using this model.

Product Catalog Implementation Workflow
First, define your catalogs. Catalogs are your curated collection of products and the highest-level container in the Product Catalog Management model. You need to create at least one catalog, but some companies have many catalogs. Catalogs can represent types of products, services, or even sales territories or business units. It's all up to you.
Second, define your categories. Categories are hierarchical groupings within a catalog that organize similar products and services. Categories can have subcategories for even more granular organization. For example, within a Software catalog, you might have categories for Collaboration Tools, Security Apps, or Games. Under Security Apps, you could have an Antivirus subcategory.
Next, define the characteristics for each of your products using dynamic attributes. These attributes are assigned through product. Attributes offer product personalization and customization, for example, size, color, storage, resolution, and so forth. A big benefit of attributes is that they reduce the number of individual products you need to build. Imagine a new model of mobile phone. You only need one product with attributes that define the different colors, storage options, and data plans.
Finally, create your products! This is the fun part where it all comes together. Products can be plain simple products like a bottle of shampoo, simple but configurable products like a t-shirt offered in various sizes, or complex groupings of products associated together in a product bundle.

Now, let's explore some examples and see how all the components interact with each other to create the rich detail found in a complete product catalog.

Example 1: Men's Polo Shirt

In this example, we'll explore a simple product with configurable options. One product SKU along with attributes so customers can choose their shirt size and color. Here are the elements required to create this product in PCM:

Catalog: Men's Clothing
Category: Men's Shirts
Attributes
Polo Color: navy, black, gray, striped, yellow, white
Polo Size: small, medium, large, extra large
Product Classification: Polo Attributes
Contains both Polo Color and Polo Size attributes.
Product Name: The Pleasant Polo

Here's an example of The Pleasant Polo as it appers for configuration in a quote:

Going further, imagine a large product catalog where you have dozens or even hundreds of color combinations in your clothing catalog. To help organize and manage large attribute lists, use Attribute Categories. For example, you could create an Attribute Category for Shirt Size and another for Shirt Color, that groups all available colors and sizes into categories. This helps product designers manage large lists of attributes.

Example 2: Laptop Packages

In this example, we need several products bundled together. There's the laptop itself and then its accessories, software, and services like an extended warranty and technical support. Here are the elements required to create a product bundle like this in PCM:

Computer Hardware Catalog
Categories: Laptops, Desktops, Tablets
Attributes: Memory, CPU Speed, Storage, Color
Product Classification: Laptop Attributes
Products: Travel Laptop, Developer Desktop, Handy Tablet
Accessories Catalog
Categories: Keyboards, Pointing Tools, External Monitors, USB Hubs, Webcams
Attributes: Monitor Size, Monitor Resolution, Connection Type (wireless, bluetooth)
Product Classification: Monitor Attributes, Connectivity Attributes
Products: Basic Keyboard, Gaming Keyboard, Basic Mouse, Personal Webcam
Software Catalog
Categories: Collaboration, Security, Productivity, Media
Attributes: License Type (commercial, educational), Operating System (Windows, Linux, MacOS)
Product Classification: Software Attributes
Products: Awesome Anti-Virus, Spreadsheets 3.0, Home Video Editor
Product Support Catalog
Categories: Warranties, Support Plans
Attributes: Warranty Period (2-year, 3-year, 5-year), Support Tiers (basic, standard, enterprise, premium)
Products: Laptop Warranty, Desktop Warranty, Technical Support Add-On

After defining all of these product catalog details, product attributes, and product records, you can assemble the products into bundles. There are many possible combinations we could create. For example, a premium laptop bundle could have this configuration:

Laptop with 1TB storage, 2.33Ghz processor, and 32GB of RAM.
Wireless Keyboard and Mouse
4K resolution external monitor
Antivirus software
5-year extended warranty with premium support plan

Here's an example of the product bundle structure as it appears in the bundle editor:

Going further, some companies create two kinds of complimentary catalogs: commercial, and technical product catalogs.

The distinction between a commercial and a technical catalog is crucial for bridging the gap between sales and fulfillment. The commercial catalog is what your customers see and interact with – it showcases the finished products or services they can browse and purchase. The technical catalog contains the granular, underlying components and services that are necessary to actually provision and deliver what the customer bought from the commercial catalog. It's the detailed blueprint for order fulfillment, and part of order orchestration.

These distinctions in the product catalogs are handled using Product Types and Product Record Types.

What's Next

As part of your catalog planning process, it's a good idea to get some hands-on experience. In a developer edition or sandbox, build out a sample product catalog using your company's actual products or services as examples. Once you've worked through the process a couple of times, you'll have a better understanding of how to scale up and tackle your entire catalog.

There's even more to discover about Product Catalog Management and related Revenue Management features like Salesforce Pricing and Product Discovery. As you're working on your product catalog, explore the rest of Revenue Management to understand how your product catalog fits into the bigger picture of your CRM solution.

SEE ALSO
Sign Up for Revenue Cloud Developer Edition
Organize Your Products with Catalogs and Categories
Manage Dynamic Attributes in Revenue Cloud
Create Product Templates Using Product Classifications
Create Products and Product Bundles in Revenue Cloud

=== ARTICLE: ind.product_catalog_preview_transactions_while_browsing_the_catalog.htm ===
---
article_id: ind.product_catalog_preview_transactions_while_browsing_the_catalog.htm
title: Preview Transactions While Browsing the Catalog
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_preview_transactions_while_browsing_the_catalog.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_enhanced_product_discovery_experience.htm
fetched_at: 2026-09-04
---

# Preview Transactions While Browsing the Catalog

Use the transaction preview to review product selections, quantities, and pricing in real time without leaving Product Discovery. The preview shows up to the 50 most recently added items in the transaction. For bundled products, the preview displays only the main product.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To preview transactions:	Product Catalog Management Designer

When you add or remove a product, Product Discovery shows a processing indicator on the product tile and in the top-right corner of the page while it saves the change and evaluates rules. Once processing completes, the preview updates to reflect the latest saved transaction.

On the Browse Products page, click View Quote Line Items.
In the transaction preview, review transaction line items, quantities, and net pricing.
Add or remove products. The preview updates automatically.

=== ARTICLE: ind.product_catalog_product_catalog_management_limits.htm ===
---
article_id: ind.product_catalog_product_catalog_management_limits.htm
title: Product Catalog Management Limits
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_catalog_management_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Product Catalog Management Limits

Before you plan and create products, attributes, and a bundled product hierarchy in Product Catalog Management, make sure that you’re aware of the capabilities and limits.

REQUIRED EDITIONS
View supported products and editions.
Product Classification Limits
You can create up to 10,000 products by using a single product classification.
A product classification hierarchy can have up to 3 levels of subclassifications. At each level, a parent classification can have up to 5 child subclassifications. For example, a root classification such as Electronics can have up to 5 subclassifications (Audio, Video, Computing, Mobile, Accessories), and each of those can have up to 5 subclassifications of its own.
A simple or bundle product can have up to 200 dynamic attributes. As a best practice, limit the attribute count for better performance.
Product Bundle Limits
A product bundle hierarchy can have up to 3 levels of nesting (root product, child group, and nested child group).
A product bundle can have up to 200 bundle components total across all groups and levels.
A bundle includes up to 200 lines, including the root product. This means a single quote line item or order line item for a bundle supports up to 199 associated child items.
A product bundle hierarchy can have up to 600 attribute overrides in total, including all bundle components.
A product bundle hierarchy can have up to 10 product component overrides.
A product bundle hierarchy can have up to 10 group component overrides.
Category and Catalog Limits
A category hierarchy can have up to 5 levels, excluding the root category.
A category can have up to 100,000 products.
You can search catalogs with up to 20 million products using the product field search option.
You can select a combined total of up to 87 searchable and filterable fields and attributes. There is no specific limit for each type, provided the combined total doesn't exceed 87.
You can index up to 1,000,000 products. To increase this limit, contact Salesforce Customer Support.
You can partially index up to 2,000 products.
API Limits
The Bulk Product Details API can take up to 100 product IDs in the request.
NOTE With Indexed product feature enabled, when defining constraints from product definition, the Add Item lookup displays all products as opposed to displaying the current product. You must search for the product to add to the Constraint Model.
Large Transaction Limits
Apex Pricing isn’t supported when using a procedure plan with product discovery.
Qualification within product details is unavailable if the configurator invokes product discovery to retrieve those details.
Large transactions require the use of Product Catalog Management Cache. Because Product Catalog Management Cache doesn’t support localization, your organization can’t have data translation enabled while using Large transactions.
Due to the mandatory use of Product Catalog Management Cache, Field-Level Security (FLS) and Record-Level Security (RLS) aren’t supported in Large transactions.
Large transactions support Advanced decision tables. Modifying the pricing procedure to use Standard or Custom decision tables is unsupported and will cause the procedure to fail.

=== ARTICLE: ind.product_catalog_product_catalog_management_permission_set_licenses.htm ===
---
article_id: ind.product_catalog_product_catalog_management_permission_set_licenses.htm
title: Product Catalog Management Editions and Permission Sets
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_catalog_management_permission_set_licenses.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_begin_using_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Product Catalog Management Editions and Permission Sets

Give users access to Product Catalog Management features. Review the supported products, editions, and permission sets for Product Catalog Management. Assign the prebuilt permission sets or custom permission set groups.

REQUIRED EDITIONS
View supported products and editions.
User Interface

Product Catalog Management is available in Lightning Experience.

Supported Products and Editions

Here's a list of products that provide access to Product Catalog Management.

PRODUCT	EDITIONS
Automotive Cloud	Enterprise, Unlimited, and Developer
Consumer Goods Cloud	Enterprise and Unlimited
Energy & Utilities Cloud	Enterprise, Performance, and Unlimited
Financial Services Cloud	Professional, Enterprise, and Unlimited
Health Cloud	Enterprise and Unlimited
Life Sciences Cloud	Enterprise and Unlimited
Loyalty Management	Enterprise, Performance, Developer, and Unlimited
Manufacturing Cloud	Enterprise, Unlimited, and Developer
Revenue Management	Enterprise, Unlimited, and Developer
Unified Catalog	Enterprise, Unlimited, and Developer
Product Catalog Management Permission Sets

These permission sets provide the user permissions, permission set license, and access to the objects and fields that are needed to manage and use Product Catalog Management.

PERMISSION SET	AVAILABLE IN THESE PRODUCTS	NOTES
Product Catalog Management Designer	All supported products	Assign it to the users who set up Product Catalog Management and Product Discovery, such as Salesforce admins, catalog admins, and product designers.
Product Catalog Management Viewer	Assign it to the users, such as sales reps, who need access to products, catalogs, and Product Discovery components.
Product Catalog Management Customer Community User	
Automotive Cloud
Health Cloud
Life Sciences Cloud
Manufacturing Cloud
	Assign it to the customers who need access to products, catalogs, and Product Discovery components to purchase products.
Product Catalog Management Partner Community User	Assign it to the partners who need access to products, catalogs, and Product Discovery components to sell products.

See permissions enabled in a permission set and review your cloud’s documentation.

If you don't see your product here, contact your account executive.

Permission Customization

To make sure that users always have the latest default permissions, we recommend the use of permission set groups instead of cloning permission sets. If you customize Product Catalog Management, for example, by adding fields, create a custom permission set. To remove user permissions from the default permission set, create a muting permission set. Then, create and use permission set groups to assign the prebuilt Product Catalog Management permission sets and your custom permission sets.

SEE ALSO
Agentforce Revenue Management License Comparison
Assign Agentforce Revenue Management Permission Sets to Your Users

=== ARTICLE: ind.product_catalog_product_catalog_management_personas.htm ===
---
article_id: ind.product_catalog_product_catalog_management_personas.htm
title: Product Catalog Management Personas for Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_catalog_management_personas.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_begin_using_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Product Catalog Management Personas for Revenue Management

Explore the different types of users who work with Product Catalog Management and the permission sets they need.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
Create Users and Profiles

To begin, create users for Product Catalog Management. Then assign users the appropriate permission sets. To help you plan, refer to the Product Catalog Management personas table.

When you create a user, you must also assign a profile. Profiles define default settings for users. Some organizations create their own profiles, while others choose to use profiles included with Salesforce.

Remember, users can have only one profile, but can have many permission sets assigned to them.

PERSONA	DESCRIPTION	REQUIRED PERMISSION SETS
Salesforce Admin	Administers Product Catalog Management, integrates Product Catalog Management features, and assigns permission set groups to admins who handle specific areas; for example, a catalog admin. Only Salesforce admins can set up Specification Types.	Product Catalog Management Designer
Catalog Admin	Creates and manages attributes, attribute categories, product classifications, product classification attributes, product catalogs, and product categories.	Product Catalog Management Designer
Product Designer	Creates and manages products, product groups, product attributes, product components, product relationships, and Qualification Rules. The Product Designer also assigns products to product categories.	Product Catalog Management Designer
Product Discovery Admin	Manages features and settings. The Product Discovery Admin also customizes product browsing experience in Lightning App Builder and Experience Builder.	Product Catalog Management Designer
Sales Agent	Browses catalogs and products, and can optionally create quotes, and place orders.	Product Catalog Management Viewer
Partner Community User	Sells Product Catalog Management products to their customers via the partner community portal.	Product Catalog Management Partner Community User
Customer Community User	Purchases Product Catalog Management products from the customer community portal.	Product Catalog Management Customer Community User

Assign permission sets to your users based on their persona.

SEE ALSO
Manage Permission Set Assignments
View and Manage Users
Create or Clone Profiles

=== ARTICLE: ind.product_catalog_product_classifications.htm ===
---
article_id: ind.product_catalog_product_classifications.htm
title: Create Product Templates Using Product Classifications
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_classifications.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Create Product Templates Using Product Classifications

Product classifications are templates that organize your product catalog and streamline product creation. Define attributes once, and let subclassifications automatically inherit them, while still allowing you to manually override attributes as needed. Product classifications help you maintain data consistency and reduce repetitive manual tasks, allowing you to quickly define and launch products with shared characteristics.

REQUIRED EDITIONS
View supported products and editions.

Product classifications are attribute templates that you can reuse to quickly define and create products that share similar attributes. These classifications are required to assign attributes to products. Configure and override the inherited attributes for each product if necessary. You can also define and manage attribute properties, such as whether an attribute is required, optional, visible, or hidden.

Product subclassifications helps you organize your product catalog into a hierarchy of up to three levels, where a parent can have up to five child nodes at a given level. Subclassifications automatically inherit all attributes from their parent classification, while still allowing you to manually override attributes as needed. This functionality streamlines the creation and maintenance of related product classes, ensuring data consistency and reducing redundant assignments.

EXAMPLE

Autz, an automobile company that sells cars and uses product classifications to manage its catalog. Instead of creating each car model from scratch, Autz establishes a parent classification called Cars that includes common attributes like Engine and Wheels.

To handle specific vehicle types, Autz then creates subclassifications under the Cars parent, such as Sedan and SUV.

The Sedan subclassification automatically inherits the Engine and Wheels attributes from its parent. Autz can also add a unique attribute like Music System to it. When a new product, like Sedan-X, is associated with this subclassification, it receives all the attributes: Engine, Wheels, and Music System.

Similarly, the SUV subclassification also inherits the Engine and Wheels attributes from the parent. Autz can add a unique attribute like 4 Wheel Drive to it. When a new product, like SUV-Y, is associated with this subclassification, it receives all the attributes: Engine, Wheels, and 4 Wheel Drive.

This tiered system streamlines the product creation process. It ensures that common attributes are automatically applied, saving time and ensuring consistency across all car models.

Create a Product Classification
A product classification is a template that you use to create products with similar characteristics. Product classifications are the primary tool for assigning attributes to products.
Create a Product Subclassification
Create and manage product classification hierarchies up to three levels deep to enhance the product catalog’s structure. Subclassifications automatically inherit attributes from their parent, simplifying attribute management and reducing redundant work.
Assign Attributes to a Product Classification
After you create a Product Classification, assign attributes to it. You can assign individual attributes to a product classification or a collection of attributes through attribute categories.
Include or Exclude Picklist Values in a Product Classification Attribute
For product classification attributes of the data type picklist, all the picklist values are included by default. To exclude specific picklist values and ensure they’re unavailable to products at run time, use Include or Exclude Picklist Values. Use the same functionality to include picklist values when your requirements change.
Explore Product Classification with an Example
Streamline the creation of a car product template by engineering a product classification hierarchy. Create a parent classification to automatically share attributes with child subclassifications, and curate valid options for specific models to reduce data entry errors.

=== ARTICLE: ind.product_catalog_product_description_generation.htm ===
---
article_id: ind.product_catalog_product_description_generation.htm
title: Product Description Generation in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_description_generation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_products.htm
fetched_at: 2026-09-04
---

# Product Description Generation in Product Catalog Management

Use Einstein AI or Agentforce to generate detailed product descriptions that enhance product discoverability and minimize the time and manual effort spent on catalog creation.

Write Product Descriptions with Einstein Generative AI
Einstein generative AI uses your instructions to generate revised product descriptions. Product descriptions support instructions only in English but you can generate descriptions in all supported languages. Any user can generate product descriptions by using Einstein but only the Salesforce admin and Product Catalog Designer can accept or reject the recommendations.

=== ARTICLE: ind.product_catalog_product_discovery.htm ===
---
article_id: ind.product_catalog_product_discovery.htm
title: Product Discovery and Guided Product Selection
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_discovery.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Product Discovery and Guided Product Selection

Use Product Discovery to provide a simple, structured product browsing experience for sales reps and customers to efficiently identify the most suitable products. Users can see product information such as images, description, pricing, product bundle details, and product attributes in a single comprehensive view.

REQUIRED EDITIONS
View supported products and editions.
Customize the Product Browsing Experience
To specify the information and options shown to your users during product discovery, override a preconfigured flow or use the Lightning App Builder to customize the experience.
Guided Product Selection
Close deals faster and smarter with Guided Product Selection. By using a series of targeted questions accessed through the Guide Me button on your product lists, you'll instantly uncover exactly what your customers need.
Search Options in Product Catalog Management
Product Catalog Management gives your sales reps three search options to quickly find the products in a catalog. They can choose the search option based on its search capabilities and the size of the product catalog.
Replace Deprecated Permissions Set for Product Discovery
Product Discovery includes a permission set for admins who set up Product Discovery, and a permission set for users who browse products. In Winter '25, the Product Discovery permission set license and permission sets are deprecated. The permissions required to access Product Discovery are available in Product Catalog Management permission set licenses and permission sets. So assign the Product Catalog Management permission sets, and then unassign the Product Discovery permission sets.
Product Discovery Lightning Components
Product Discovery provides Product List, Product Details, Product Bundle Details, and Product Attribute Details components that you can add to pages on supported Salesforce Lightning Apps and Experience Cloud sites. To provide easy access to these components, some Salesforce Apps also use a tailored version of these components.
Product Discovery with Constraint Rules
The Product Discovery with constraint rules experience helps you build accurate transactions as you browse the product catalog. You see real-time transaction details in the transaction preview, along with constraint rule outcomes such as disabled products, product recommendations, and rule messages. When you add or remove a product, Product Discovery automatically saves the change to the transaction, you don't pause your browsing or wait for the save to complete. While the save is in progress, you can continue going to a category, searching for more products, or reviewing recommendations. This non-blocking experience keeps the catalog fully interactive always.

=== ARTICLE: ind.product_catalog_product_discovery_component_properties.htm ===
---
article_id: ind.product_catalog_product_discovery_component_properties.htm
title: Product Discovery Component Properties
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_discovery_component_properties.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_considerations_custom_flow_for_browsing_and_adding_products.htm
fetched_at: 2026-09-04
---

# Product Discovery Component Properties

Use the Product Discovery component properties to show only the information and options that your users need.

REQUIRED EDITIONS
View supported products and editions.

Here’s a table that lists all the properties and their descriptions. Keep in mind that the available properties vary across components.

PROPERTY NAME	DESCRIPTION	LIGHTNING APP BUILDER	PRODUCT LIST CONTAINER FLOW COMPONENT	PRODUCT LIST PAGE FLOW COMPONENT
Account ID	Enter the ID of the account that you want to show products for.	No	Yes	Yes
Record ID	Enter the ID of the product catalog that you want to list products for.	No	Yes	Yes
Run qualification procedure	Enable the property if you want the qualification procedure selected on the Product Discovery Settings page to run for the component.	Yes	Yes	Yes
Run pricing procedure	

This setting works only when Salesforce Pricing is enabled.

Enable the setting if you want the pricing procedure selected on the Product Discovery Settings page to run for the component.

	Yes	Yes	Yes
Let users configure products	

Enable the property to configure products from the Browse Catalogs quick action from quote and order pages.

	Yes	Yes	Yes
Let users enter the quantity	Enable the property for users to enter a quantity.	Yes	Yes	Yes
Let users select multiple products	Enable the property if you want to allow users to select multiple products.	Yes	Yes	Yes
Page Size	Enter the number of products that the page loads by default. When a user reaches the end of the list, the next set of products are loaded.	Yes	Yes	Yes
Add Products To	

Use this setting only if record types aren’t enabled for the object.

Select the object that a user can add products to. For example, if you select Quote in the Add Products To field, then users see the Add to Quote and Add Selections to Quote buttons.

The list of objects that appear depends on the availability of other products. For example, the Quote and Order options appear in the dropdown list only if Transaction Management is available in your Salesforce org.

	Yes	Yes	Yes
Supported Views	Select how products appear for users. If you select List and Tile views, users can switch between these views.	Yes	Yes	Yes
Default View	

If you select List and Tile Views in Supported Views, specify the default view.

When a user refreshes the page or starts a new session, the view returns to the default view.

	Yes	Yes	Yes
Tile View Type	

If you select tile view, specify the type of tile view.

The basic tile shows only the image, name, and description.

The detailed tile shows the image, name, and description along with other information such as pricing, configuration options, product selling model, and additional fields based on the configured properties.

	Yes	Yes	Yes
Display Fields	Select up to 3 additional standard or custom fields that you want to show.	Yes	Yes	Yes
Custom Action Label	Enter an action label for the product list page to add products to your record page.	Yes	No	Yes
Context Data Input Array	Enter the apex class of the list of records that determine product eligibility and calculate product prices.	No	Yes	Yes
Select catalogs from the product list page	Enable the property so that users can select and move between catalogs.	Yes	Yes	Yes
Show guided product selection	

The functionality provided in this setting is available only if users have enabled Guided Product Selection.

Enable this property to provide users access to Guided Product Selection. Users can answer questions to show specific products according to their requirements.

	Yes	Yes	Yes
Show smart product selection	

The functionality provided in this setting is available only if users have enabled Smart Product Selection.

Enable this property to use AI capabilities to show relevant products to users when they browse product catalogs.

	No	Yes	Yes
View Cart	Enable the property so that users can view the selected products in the cart.	No	Yes	No
Product Catalog Id	Enter the ID of the product catalog that you want to list products for.	Yes	Yes	Yes
Product Catalog Name	Enter the name of the product catalog that you want to list products for.	Yes	Yes	Yes
Object API Name	Enter the API name of the transaction record object, such as Quote or Order.	Yes	Yes	Yes
Group Transaction Id	Enter the ID of the specific group within a transaction (e.g., a Quote Group) to which products should be added.	Yes	Yes	Yes
Group Transaction Name	Enter the name of the transaction group to which products should be added.	Yes	Yes	Yes
Discover Products Context	Enter the Apex class that defines the context for product discovery to tailor the list based on specific business logic.	Yes	Yes	Yes
Transient Line Save Flow	Enable this property if the component is being used within a Transient Line Save flow to manage temporary line item records.	Yes	Yes	Yes
Run Qualification Procedure	Enable the property if you want the qualification procedure selected on the Product Discovery Settings page to run for the component.	Yes	Yes	Yes
Configure Products	Enable the property if you want to allow users to configure products from the Browse Catalogs quick action from quote and order pages.	Yes	Yes	Yes
Configure Quantity	Enable the property if you want to allow users to enter a product quantity.	Yes	Yes	Yes
Select Multiple Products	Enable the property if you want to allow users to select multiple products simultaneously.	Yes	Yes	Yes
View Product Image	Enable this property if you want product images to be visible to users in the list or tile views.	Yes	Yes	Yes
View Product Prices	Enable this property if you want users to see the list price for products in the list.	Yes	Yes	Yes
View Cart	Enable the property so that users can view the selected products in the cart.	Yes	Yes	Yes
Number of Products	Enter the number of products that the page loads by default. The minimum is 12 and the maximum is 100.	Yes	Yes	Yes
Tile View Label	Specifies the tile variant. Supported values are Basic Tile and Detailed Tile.	Yes	Yes	Yes
Additional Fields	Select up to 3 additional standard or custom fields from the Product2 object that you want to show in the list.	Yes	Yes	Yes
Maximum Values per Facet	Enter the maximum number of filter values (facet values) that a user can see within a single filter category.	Yes	Yes	Yes
Maximum number of Facets	Enter the maximum number of filter categories (facets) available to the user for narrowing down products.	Yes	Yes	Yes
Show Message Bar	Enable this property to display a bar at the top of the page showing error, warning, and info messages from configuration rules.	Yes	Yes	Yes
Recommended Products	Enable this property to display a tab for recommended products based on the Configuration Rules on the current transaction.	Yes	Yes	Yes
Configure Action Display Type	Optional. Shows the Configure icon as a button with a label when set to True. Defaults to False.	Yes	Yes	Yes
Configure Label	Specifies the custom text to show on the configure button. Applicable only when Configure Action Display Type is True. Defaults to Configure.	Yes	Yes	Yes
Hide Add for Configurable Products	Hides the Add button for configurable products when set to True. Defaults to False.	Yes	Yes	Yes
Hide Add for Static Products	Hides the Add button for static products when set to True. Defaults to False.	Yes	Yes	Yes
NOTE When you create an apex class to create additional context data for your records, you must configure it in the Context Data Input Array property of your product list component.

=== ARTICLE: ind.product_catalog_product_discovery_personas_and_permission_sets.htm ===
---
article_id: ind.product_catalog_product_discovery_personas_and_permission_sets.htm
title: Replace Deprecated Permissions Set for Product Discovery
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_discovery_personas_and_permission_sets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_discovery.htm
fetched_at: 2026-09-04
---

# Replace Deprecated Permissions Set for Product Discovery

Product Discovery includes a permission set for admins who set up Product Discovery, and a permission set for users who browse products. In Winter '25, the Product Discovery permission set license and permission sets are deprecated. The permissions required to access Product Discovery are available in Product Catalog Management permission set licenses and permission sets. So assign the Product Catalog Management permission sets, and then unassign the Product Discovery permission sets.

REQUIRED EDITIONS
View supported products and editions.

The Product Discovery User permission set has a subset of permissions available in the Product Catalog Management Viewer permission set. And the Product Discovery Admin permission set has a subset of permissions available in the Product Catalog Management Designer permission set.

 If needed, clone and customize the Product Catalog Management Viewer and the Product Catalog Management Designer permission sets.
Assign the Product Catalog Management Viewer and the Product Catalog Management Designer permission sets to users.
Unassign the Product Discovery User and Product Discovery Admin permission sets.
SEE ALSO
Configure Permissions and Access in Permission Sets
Manage Permission Set Assignments

=== ARTICLE: ind.product_catalog_product_field_search_in_product_catalog_management.htm ===
---
article_id: ind.product_catalog_product_field_search_in_product_catalog_management.htm
title: Product Field Search in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_field_search_in_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_search_options_for_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Product Field Search in Product Catalog Management

Sales reps can use the Product field search option to quickly locate specific products within large catalogs (millions of products) by searching text-indexed fields such as Product Name, Description, Product Code, and SKU.

REQUIRED EDITIONS
View supported products and editions.

Product field search doesn’t limit your sales reps to catalogs with over 4 million products. If the product field search capabilities meet their needs, they can use this search option for catalogs that have 1 million to 4 million products as well.

NOTE Product Field Search doesn’t support faceted search, attribute based search, guided product selection, and search by translated product name.
Configure Product Field Search
Give your users the option to quickly search for catalogs having more than 4 million products.

=== ARTICLE: ind.product_catalog_product_ramp_segments.htm ===
---
article_id: ind.product_catalog_product_ramp_segments.htm
title: Create a Product Ramp Segment
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_ramp_segments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.qocal_configure_ramp_segments.htm
fetched_at: 2026-09-04
---

# Create a Product Ramp Segment

A ramp deal is a type of sales agreement where price and volume vary across time periods. A ramp segment is a specific period within a ramp deal during which certain prices and volume are in effect.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) with the Revenue Cloud Growth license, the Revenue Cloud Advanced license, or the Revenue Cloud Billing license.
USER PERMISSIONS NEEDED
To create a ramp segment:	Manage Product Catalog

Considerations for product ramp segments.

You can associate only static simple and configurable simple products with ramp segments.
You must assign a term-defined product selling model to a product and then use the combination of the term-defined product selling model and the product to create a ramp segment.
A product can have only one ramp segment of the same segment type — for example, a product can have only one yearly product ramp segment.
Before you create a product ramp segment, turn on Ramp Deals for Lines in Quotes and Orders.
From Setup, in the Quick Find box, find, and select Revenue Settings.
Turn on Ramp Deals for Lines in Quotes and Orders.
From the App Launcher, find and select Product Catalog Management.
From the product list, click the simple product for which you want to create ramp segments.
Go to the Related tab for the product.
From the Product Ramp Segments related list, click New.
In the New Product Ramp Segment window, specify the following:
Select a term-defined product selling model.
To try the product at no additional cost for a specified duration, under Segment Type select Free Trial, enter a trial duration, and select the duration type. For example, to offer a 1-month trial at no additional cost, enter 1 in the Trial Duration field and select Month under Duration Type. To associate a trial segment at no additional cost with a product, first associate a yearly or custom segment with that product.
To create a segment for a specific number of years, select Yearly under Segment Type. Leave the Trial Duration and Duration Type fields blank.
To create a segment for a custom duration, select Custom under Segment Type. Leave the Trial Duration and Duration Type fields blank.
Save your changes.

=== ARTICLE: ind.product_catalog_product_relationships.htm ===
---
article_id: ind.product_catalog_product_relationships.htm
title: Product Relationship Management in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_relationships.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_creation_of_a_bundled_product_structure.htm
fetched_at: 2026-09-04
---

# Product Relationship Management in Revenue Management

Bundle products consist of components such as groups, products, and product classifications. These components are related to each other through product relationships.

REQUIRED EDITIONS
View supported products and editions.

The first product in a product hierarchy is the root product (1). All components added to the root product are its children (2).

A root product can have multiple root groups or multiple products as its immediate level-one child components. A root group can have either multiple child groups, or multiple products, or a single product classification component as its immediate child component.

You define a Product Relationship Type when you add a product or a product classification component to a bundle.

Specify Component Detail Fields
FIELD	DESCRIPTION
Child Product	The name of the child product that you add to the bundle. This field is empty when you add a product classification to a group.
Child Product Classification	The name of the product classification that you add to a group. This field is empty when you add products to a group.
Sequence	The display order of the product in the run-time cart
Quantity	The default quantity of the product or products based on the product classification in the run-time cart
Product Relationship Type	When you add a product, the product relationship type is Bundle to Bundle Component Relationship. When you add a product classification, the product relationship type is Bundle to Product Classification Component Relationship
Group	The group under which you add the product or product classification
Require this component	To make the product a required component in the bundle, select Require this component. Ensure that Require this component is deselected for product classification components.
Include component by default	To include the product in the bundle by default, select Include component by default. Ensure that Include component by default is deselected for product classification components.
Allow Quantity Changes	To allow users to change product quantities during run time, select Allow quantity changes. If Allow Quantity Changes is deselected, you can’t enter a minimum and maximum quantity
Min Quantity	The minimum number of products that you can select in the bundle at run time
Max Quantity	The maximum number of products that you can select in the bundle at run time
Additional Product-Related Component Fields

To edit the product relationship, click the product tile from the Structure tab and click Edit Relationship under the Relationship tab in the right pane.

FIELD	DESCRIPTION
Component Selling Model	
Don’t select a component selling model for products added under a new static bundle. The parent selling model for these products must be none.
Don’t select a component selling model for configurable bundles.

Quantity Scaling Method	

Defines how the child product quantity changes as the quantity of the parent product changes in the runtime cart. This field can have these values:

None: Select Allow Quantity Changes to change the quantity values of the child product in the run time, irrespective of the quantity of the parent product. Deselect Allow Quantity Changes to restrict changes to the quantity values of the child product in the run time irrespective of the quantity of the parent product.
Constant:
The quantity of the child product in the runtime cart remains constant irrespective of the changes to the parent product quantity when the Quantity Scaling Method is set to Constant. You can’t change the child product quantity in the runtime. The child product quantity value remains what was defined in the design time in Product Catalog Management.
You must deselect Allow Quantity Changes when the Quantity Scaling Model is set to Constant.
Proportional:
This is the default value for the Quantity Scaling Method when you don’t select Allow Quantity Changes in the Specify Component Details window. The Quantity Scaling Method is set to None when you select Allow Quantity Changes in the Specify Component Details window.
When the Quantity Scaling Method is set to Proportional, the quantity of the child product in the runtime cart changes in proportion to the changes to the parent product quantity. For instance, if the parent product quantity is A and the child product quantity is B, then the runtime cart has A number of parent products, but A multiplied by B number of child products.

Quote Visibility	

The value in this field controls whether a child product is shown in Transaction Line Editor, quote documents, both, or neither:

Always: To show the child product in both Transaction Line Editor and quote documents.
Never: To hide the child product in both Transaction Line Editor and quote documents.
Transaction Line Editor Only
Quote Document Only

If you don’t select a value, child products appear in quotes and quote documents.

If you hide a bundled product, its child products are also hidden. If you show a bundled product, its child products are shown based on their individual visibility settings.

WARNING
When the Quantity Scaling Method is Constant or Default, child product quantities are read-only in the runtime cart, even for legacy products where Allow Quantity Changes is selected. To enable edits, change the scaling method to None or Proportional.
When the Quantity Scaling Method is Proportional and Allow Quantity Changes is enabled, child product quantities are editable only in the configurator during new sales. The quantity field is read-only in the sales transaction line editor because it displays the final calculated quantity stored on the quote line item, not the editable per-parent unit quantity.
When the Quantity Scaling Method is Proportional and Allow Quantity Changes is enabled, child product quantities are read-only in the configurator during Amend, Renew, or Cancel transactions. The original parent-to-child ratio remains fixed throughout the asset lifecycle. To adjust the child product quantity, change the parent product's quantity instead. The child quantity updates proportionally.

=== ARTICLE: ind.product_catalog_product_selling_model.htm ===
---
article_id: ind.product_catalog_product_selling_model.htm
title: Manage Product Selling Model in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_selling_model.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Manage Product Selling Model in Revenue Management

Product selling models define how you sell products. The models can be one time, term-defined, or evergreen.

REQUIRED EDITIONS
View supported products and editions.

Product selling models are an optional feature. You don't have to define or assign a selling model to use Product Catalog Management.

Product selling models have these types:

SELLING MODEL TYPE	DESCRIPTION
One Time	Sell a product one time, not as a subscription.
Term-Defined	Sell a product or a product subscription with an end date.
Evergreen	Sell a product or a product subscription that recurs until the user cancels it.

To get started with product selling models, follow these instructions:

Create a Product Selling Model
Create product selling models for your products from the Product Catalog Management home page.
Assign a Product Selling Model to a Product
After you create a product selling model, assign it to your products.

=== ARTICLE: ind.product_catalog_product_specification.htm ===
---
article_id: ind.product_catalog_product_specification.htm
title: Create Product Specifications in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_product_specification.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Create Product Specifications in Revenue Management

With Product Catalog Management, you can define a specification type for the products that are unique to your industry. A product specification type is associated with a product specification record type.

REQUIRED EDITIONS
View supported products and editions.

The product specification record type links the product specification type with Record Types defined on the Product object. The product specification record type also determines if the product specification is sold commercially or not. 

Product specification types and product specification record types are optional configurations. You can create them when you set up Product Catalog Management.

Create Product Specification Type and Product Specification Record Type
Ensure that your products have the terminology that’s unique to your industry. Use Product Catalog Management to define a specification type for the products that are specific to your industry and create corresponding product record types.
SEE ALSO
Create Page Layouts
Create Record Types

=== ARTICLE: ind.product_catalog_productdiscoverycontext_context_definition.htm ===
---
article_id: ind.product_catalog_productdiscoverycontext_context_definition.htm
title: Nodes and Attributes in the ProductDiscoveryContext Context Definition
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_productdiscoverycontext_context_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_context_definitions_for_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Nodes and Attributes in the ProductDiscoveryContext Context Definition

The ProductDiscoveryContext context definition contains nodes and attributes that are used by and populated by Product Discovery, pricing procedure, qualification procedure, and object mapping.

REQUIRED EDITIONS
View supported products and editions.
The ProductDiscoveryContext Context Definition

The ProductDiscoveryContext context definition contains the Catalog, Category, Category Product, Pricing Product, and Account nodes.

IMPORTANT The qualification procedure and pricing procedure for product discovery must use the context definition selected on the Product Discovery Settings page.
Nodes and Attributes
NODE	ATTRIBUTE	TYPE	DESCRIPTION
Catalog (Root node)	CatalogId	Input	The Salesforce ID of the selected catalog.
CurrentDate	Input	The user’s current date and time.
Category (Child node of the Catalog node)	CategoryId	Input	The Salesforce ID of the category selected by the user.
IsCategoryQualified	Output	

The value that specifies whether a category is qualified.

The qualification procedure populates this value.


CategoryDisqualifiedReason	Output	

The reason for category disqualification.

If a category isn’t qualified, the qualification procedure populates this value.


ParentReference	Input	

A reference to the parent node.

This value is auto-populated.


CategoryProduct (Child node of the Category node)	Quantity	Input	The quantity of a specific product selected by a user.
IsQualified	Output	

Specifies whether a product is qualified.

The qualification procedure populates this value.


Reason	Output	

The reason for product disqualification.

If a product isn’t qualified, the qualification procedure populates this value.


AdditionalProductInformation	Input Output	Don’t use this attribute. This attribute is reserved for future use.
ParentReference	Input	

A reference to the parent node.

This value is auto-populated.


Id	Input	The Salesforce ID of the product.
ProductId	Input	The Salesforce ID of the product.
RootProductId	Input	The Salesforce ID of the root product.
ParentProductId	Input	The Salesforce ID of the parent product.
CategoryId	Input	This field isn’t used by default.
CatalogId	Input	This field isn’t used by default.
Name	Input	The name of the product.
Code	Input	The product code.
MaxQuantity	Input	The maximum quantity of the product that can be added.
MinQuantity	Input	The minimum quantity of the product that must be added.
PricingProduct (Child node of the Category node)	PricingId	Input	The Product’s Salesforce ID and the product selling model’s Salesforce ID.
PricingProductId	Input	The Salesforce ID of the product.
ProductSellingModelId	Input	The Salesforce ID of the product selling model.
ProductQuantity	Input	The product quantity selected by a user.
PricebookId	Input	The Salesforce ID of the price book.
PricingCurrencyCode	Input	The currency ISO code of the user’s account or the currency ISO code specified by the user.
UnitPrice	Output	The list price of the product based on the product selling model.
IsDerived	Output	Specifies whether the price of the product is derived from another source, such as a product or an asset.
NetUnitPrice	Output	The unit price of the item after applying discounts and before tax calculation.
SubTotal	Output	The total price of the product calculated by using the quantity, net unit price, and pricing terms.
PriceBookEntryId	Output	

The Salesforce ID of the price book entry.

The pricing procedure populates this value.


PriceWaterFall	Output	

The ID of the price waterfall.

A price waterfall provides insights into every step of the pricing process.


PricingErrorMessage	Output	The message that appears when price calculation errors occur.
AdditionalPricingInformation	Input Output	Don’t use this attribute. This attribute is reserved for future use.
ParentReference	Input	

A reference to the parent node.

This value is auto-populated.


Account (Root node)	id	Input	The Salesforce ID of the account.
AccountId	Input	The Salesforce ID of the account.
ContactId	Input	The Salesforce ID of the contact.
CurrencyIsoCode	Input Output	

The currency ISO code associated with the account.

This value is auto-populated from the account.

=== ARTICLE: ind.product_catalog_products.htm ===
---
article_id: ind.product_catalog_products.htm
title: Create Products and Product Bundles in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_products.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Create Products and Product Bundles in Revenue Management

Products are all the items and services that you sell to customers. There are two types of products: simple products and bundled products. Simple products are single-element products with no dependencies on any other products. Bundled products are a group of products that are sold together as one unit.

REQUIRED EDITIONS
View supported products and editions.

Simple and bundled products are further classified into configurable or static products depending on whether your sales reps need to configure product options during the sales process or not.

Here are a few examples of the various types of products and product bundles:

Static Simple Product:
Generic instant coffee.
A coffee grinder.
Configurable Simple Product:
Coffee where a customer can choose medium roast or dark roast.
T-shirts with small, medium, and large sizes.
Static Bundle:
A travel kit that contains a shampoo, conditioner, body wash, hand lotion, and a toothbrush.
A software support plan that includes 10 hours of technical support and two online training sessions.
Configurable Bundle:
A laptop with mouse, keyboard, and monitor but also with optional extended warranty plan and wireless headphones.
A flatscren TV that come in various sizes, all with standard remote control and sound bar.

Use fields on the product itself to create these various product and bundle types. Refer to this table to understand how the product fields define the product and bundle type.

PRODUCT TYPE	CONFIGURE DURING SALE	PRODUCT	CHILD COMPONENTS
None	Not Allowed or None	Static simple product	None
Allowed	Configurable simple product	None
Bundle	Not Allowed or None	Static product bundle	
Static simple
Static bundle

Allowed	Configurable product bundle	
Static simple
Static bundle
Configurable simple
Configurable bundle
Important Things to Note About Static Product Bundles
You can optionally add Product Group (1) components to the static bundle hierarchy.
If you delete a group, all components under the group, such as products and product classifications, are deleted.
Add only static simple products or static bundled products as child components of static bundled products. You can’t add configurable simple products or configurable bundle products as child components of static bundled products.
When you add child components to a static product bundle, make sure that the field Include component by default is selected on the child components. Also ensure that the field Allow Quantity Changes isn’t selected on the child components.
If your static simple product is based on a product classification, then all attributes for all components in the static bundle must have default values.
When adding a child component with a defined unit of measure to a static product bundle, the Quantity, Min Quantity, and Max Quantity fields automatically inherit the scaling and rounding method of the child component.
Important Things to Note About Configurable Product Bundles
Groups are mandatory components in a configurable product bundle. Child components must be added only under Groups and not directly under the root product.
Product groups are structured hierarchically, where a root group acts as the parent and can contain multiple child groups. While a root group can include multiple child product groups, multiple product components, or a single product classification, this hierarchy is limited to two levels; child groups can’t contain further nested groups, and these elements can’t be mixed at the same level within a child group. For example, a child group can’t contain both product components and a product classification. A product classification can only be added once per group.
When you delete a group, all components under the group, such as products and product classifications, are deleted.
You can add simple and bundled products of type static or configurable as child components of a configurable bundle.
When adding a child component with a defined unit of measure to a configurable product bundle, the Quantity, Min Quantity, and Max Quantity fields automatically inherit the scaling and rounding method of the child component.

To get started creating products and product bundles, refer to these instructions:

Create Simple Products
Learn how to create simple products for your product catalog. Simple products are products that aren't bundled with other products. You can create static or configurable simple products.
Configure Product Attributes in Revenue Management
Products that are based on a product classification inherit all the attributes from the product classification. You can configure the inherited attributes to make them product-specific. You can override the configured and inherited attributes in the context of a product bundle.
Include or Exclude Picklist Values in a Product Attribute
A product that’s based on a product classification, inherits all the product classification attributes including any included or excluded picklist values. To include or exclude specific picklist values for product attributes of the data type picklist, use Include or Exclude Picklist Values. The included picklist values are available at run time while excluded picklist values are unavailable at run time.
Create Bundled Products
Bundled products are a group of products that are sold together as one unit. You can create static or configurable bundled products.
Product Description Generation in Product Catalog Management
Use Einstein AI or Agentforce to generate detailed product descriptions that enhance product discoverability and minimize the time and manual effort spent on catalog creation.
Deep Clone Products in Product Catalog Management
Create products by cloning existing products and their related information such as attributes, child components, and selling models. Use deep cloning to reduce manual effort and quickly create products that are similar to the existing products. Leverage context service capabilities to customize the deep clones of custom objects and fields that are not included in the available default context definition.
Decimal Quantity Support in Product Catalog Management
Define accurate product quantities for products that support decimal values. Based on the product's unit of measure (UOM), define the number of decimal places the product supports, with specific rounding methodologies.
Data Import Through CSV Files in Product Catalog Management
Catalog admins and product designers can create records by importing CSV files into Product Catalog Management.

=== ARTICLE: ind.product_catalog_qual_rules_example.htm ===
---
article_id: ind.product_catalog_qual_rules_example.htm
title: Explore a Qualification Rule Example
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_qual_rules_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_qualification_rules.htm
fetched_at: 2026-09-04
---

# Explore a Qualification Rule Example

Qualification rules can be a complex topic to understand. Let's look at an example to see how the components come together to create a fully functional qualification rule.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create and test all qualification rule components:	

Manage Product Catalog

Context Service Admin

Rules Engine Designer

Rules Engine Runtime

NOTE Your Salesforce org may be customized or configured differently from what is described here. If these instructions become difficult to follow, create a promo developer org to use for this example exercise.
Example Overview

Qualification rules come in two types: qualification and disqualification. In this example, we'll explore a disqualification rule.

Consider a company in the United States that sells landscaping and lawn care materials such as tools, grass seed, mulch, fertilizer, and pesticide. In the agricultural industry, many states regulate the use and sale of certain chemicals. One particular product, a pesticide sold as PEST-1X, is not allowed for sale in California due to local environmental laws.

We'll use the Billing State field as the primary criteria for our qualification rule. If a sales rep creates a quote or order for a customer in California, PEST-1X does not appear as a choice in the Landscaping product catalog.

Let's explore how to build a qualification rule that satisfies these requirements.

Summary of Components

Qualification rules require several technical components. To make keeping track of them easier, refer to this table. Note that the exact component names used here may be different from what's in your org.

COMPONENT NAME	COMPONENT TYPE
PEST-1X	Product
Disqualification Record	Product Disqualification Object
BrowseProductsCtxDefinition	Product Discovery Context Definition
ProductDisqualificationDT	Product Disqualification Decision Table
Product Qualification	Qualification Rule Procedure
Create the PEST-1X Product

Before implementing the qualification rule, let's add a product we can test with the catalog.

Create a Catalog called Landscaping.
Create a Category called Pesticides, and assign it to the Landscaping Catalog.
Create a simple Product called PEST-1X. Make sure to activate it.
Create a One Time Product Selling Model Option for the product.
Create a price book entry for PEST-1X. Choose any price you want.
Select One Time as the Selling Model, then save the price book entry.

You now have a product that is ready to add to quotes and orders.

Add Custom Field to the Product Disqualification Object

To begin building the qualification rule, add a custom field for Billing State to the Product Disqualification object. Fields on this object are used as evaluation criteria by qualification rules.

To create the custom field:

Go to the Object Manager in Setup.
Find the Product Disqualification object.
Create a new text field called BillingState.
Set the field visibility for all profiles and select the page layout to display the field.
Save your work.
Create a Product Disqualification Record

Now that you have the custom Billing State field, create a Product Disqualification record with the criteria for our example scenario.

To create the Product Disqualification record:

Open the App Launcher and find Product Disqualifications.
Click New and enter this field data:
Product: PEST-1X.
Effective From: today's date.
Effective To: a date in the future.
BillingState: CA.
Save the record.
Modify the Product Discovery Context Definition

To add Billing State to the active product discovery context definition, modify the BrowseProductsCtxDefinition context definition.

To modify the BrowseProductsCtxDefinition context definition:

Go to Setup and find Context Definitions using Quick Find.
Click Custom Definitions.
Click BrowseProductsCtxDefinition.
Click Edit.
Click Next.
You don't need to add any nodes, so click Next.
Click Account Inherited, then click Add Attributes and enter these field values:
Name: BillingState.
Type: Input.
Data Type: String.
Click CategoryProduct Inherited. Add another BillingState attribute with the same values as before.
Click Next.
In the Account Node, enter BillingState as the Context Tag for BillingState.
Save your work.
Map Billing State in the Context Definition

To complete the context definition modifications, map Billing State from the context definition input node to the account object node.

Go to Setup and find Context Definitions using Quick Find.
Click Custom Definitions.
Click BrowseProductsCtxDefinition.
Click Map Data.
Open the action menu for the mapping and click Edit.
Click Map.
Map BillingState from the input Account Node to BillingState on the account object node.
Save your work.
Modify the Product Disqualification Decision Table

Modify the disqualification decision table to include the criteria for our example qualification rule. The decision table is used by the Qualification Rule Procedure to evaluate the criteria for both qualification and disqualification.

To add the Billing State criteria to the product disqualification decision table:

Open the App Launcher and select Product Catalog Management. Navigate to the Home tab.
Scroll down the page and click Qualification Rules.
Open the Product Disqualification rule and click Deactivate.
Click Save & Next.
Click Add Condition.
In Source Object Field, enter BillingState__c for the Source.
In Operator, select Equals.
Click Save & Next.
Click Save & Next.
Click Finish.
Click Activate.
Modify the Qualification Rule Procedure

We're almost there! Now that we have configured all the qualification rule components we need, let's bring them all together in the qualification rule procedure.

To modify the qualification rule procedure:

Open the App Launcher and select Product Catalog Management.
On the Home tab, scroll down and click Qualification Rules Procedures.
Select the All Qualification Procedures list view.
Click Product Qualification.
In Qualification Procedure Versions click the most recent, active version.
Deactivate the Rule Procedure.
Open the Evaluate Disqualification component.
Map the Billing State input parameter by selecting BillingState.
Save and Activate the procedure.
Confirm Product Discovery Settings

All the pieces are now in place. As a best practice, let's check the Product Discovery Settings to ensure that we have the correct Context Definition and Qualification Procedure selected there.

In Setup, find Product Discovery Settings using Quick Find.
Confirm that Context Definition is set to BrowseProductsCtxDefinition.
Confirm that Qualification Procedure is set to ProductQualification.
Test the Qualification Rule

Now let's ensure that the qualification rule performs as expected.

Create a quote for an Account where Billing State = CA. Confirm that PEST-1X is not available in the catalog.
Create a quote for an Account where Billing State is not CA. Confirm that PEST-1X is available in the catalog.
NOTE If the qualification rule doesn't appear to be working, Sync Pricing Data and try again.

=== ARTICLE: ind.product_catalog_qualification_rules.htm ===
---
article_id: ind.product_catalog_qualification_rules.htm
title: Manage Qualification Rules for Products in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_qualification_rules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Manage Qualification Rules for Products in Revenue Management

Use qualification rules to define the customer eligibility and availability for products, or product categories. Configure qualification rules using criteria such as location, account attributes, purchase history, and more.

REQUIRED EDITIONS
View supported products and editions.

By default every product or product category is qualified. With qualification rules, you can specify the conditions under which products and categories remain qualified or become disqualified.

Sales reps can select qualified products during the quote and order process through the Browse Catalogs button. Disqualified products don't appear in Browse Catalogs and can't be added to quotes or orders.

Rule Types

In Product Catalog Management, you can define qualification rules in two ways:

Qualification
The product or product category is qualified when the product or product category matches specified qualification criteria. For example, a premium dining table is available to customer accounts with enough rewards points.
Disqualification
The product or product category is disqualified when the product or product category matches specified disqualification criteria. For example, a newly launched product category is available to customer accounts in all states except New York. In this example, it’s easier to control availability with a disqualification rule. The product is disqualified when the customer account's state is New York.
Qualification Rule Components

To use qualification rules, you must define these components:

Objects
Qualification rule criteria are stored in Salesforce objects. You can either build your own custom objects, or choose to extend the out-of-the-box qualification objects that come with Product Catalog Management.
Context Definitions
Use a context definition to pass product or product category data to the qualification procedure. The qualification procedure then evaluates the qualification of products or product categories, and returns the qualification or disqualification results to the context definition.
Decision Tables
Decision tables contain the selected Salesforce object criteria fields through which the rules qualify or disqualify products and product categories. Decision tables facilitate data lookup and criteria matching.
Qualification Rule Procedures
A qualification rule procedure consists of a series of steps connected in a logical flow that evaluate product or product category qualification and disqualification based on criteria defined in the related decision table.
Qualification Rule Considerations
Products and categories that don’t have any qualification or disqualification rules are qualified by default.
Qualification rules take precedence over disqualification rules. For example, when a category is qualified based on a category qualification rule, the category remains qualified even if it’s disqualified based on other rules.
If a product category is qualified based on a qualification criteria, then the user sees all the products within the qualified category, provided the products don’t have specific disqualification rules defined.
Build a Qualification Rule

Qualification rules can be a complex topic to understand. Follow these steps in sequence to build a functional qualification rule.

Create Qualification Rule Criteria
Create criteria using field data on your chosen Salesforce object that you want to use for qualification rules. The object can be one that you create, or one of the included qualification or disqualification objects.
Configure a Context Definition for Qualification Rules
For qualification rules, context definitions pass product or product catagory data to your qualification rule procedures. The qualification procedure then evaluates the qualification of products or product categories and returns the qualification or disqualification results back to the context definition.
Decision Tables for Qualification Rules
A decision table contains the criteria used for qualification and disqualification of products and product categories. Create a decision table for every type of qualification and disqualification that you want to configure.
Create a Qualification Rule Procedure
A qualification rule procedure contains qualification procedure elements that evaluate the rules in a decision table. The procedure accepts a list of categories and products as input and returns the list of products and categories along with their qualification or disqualification information as output.
Simulate and Activate a Qualification Rule Procedure
Before you activate your qualification rule procedure, run simulations to test whether the rules you defined in the decision table are accurate and give you the desired output. If your rule procedure doesn’t work as expected, edit the values and simulate again. When you’re satisfied, activate the rule procedure version.
Manage Qualification Rule Components
To fine-tune your qualification rules, modify or deactivate its components.
Explore a Qualification Rule Example
Qualification rules can be a complex topic to understand. Let's look at an example to see how the components come together to create a fully functional qualification rule.

=== ARTICLE: ind.product_catalog_record_sharing_in_product_catalog_management.htm ===
---
article_id: ind.product_catalog_record_sharing_in_product_catalog_management.htm
title: Record Sharing in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_record_sharing_in_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Record Sharing in Product Catalog Management

Set up record sharing and grant all runtime users of Product Catalog Management read access to all child records and related object records for a given product.

REQUIRED EDITIONS
View supported products and editions.

Give all runtime users read access to these objects:

Attribute Category
Attribute Category Attribute
Attribute Definition
Attribute Picklist
Attribute Picklist Excluded Value
Catalog
Product
Product Attribute Definition
Product Category Disqualification
Product Category Qualification
Product Classification
Product Classification Attribute
Product Component Group
Product Component Group Override
Product Disqualification
Product Qualification
Product Related Component Override
Product Ramp Segment (Available only when you have Revenue Management and Ramp Deals enabled)
UnitOfMeasure (Available only when you have Revenue Management)
NOTE If a bundle product's gear icon appears greyed out in Browse Catalogs, the user may be missing read access to the Product Component Group object. For details, see Bundle Product Not Configurable in Browse Catalogs.
SEE ALSO
Set Up Record Access for Your Users
Create Guest User Sharing Rules

=== ARTICLE: ind.product_catalog_record_sharing_in_product_discovery.htm ===
---
article_id: ind.product_catalog_record_sharing_in_product_discovery.htm
title: Record Sharing in Product Discovery
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_record_sharing_in_product_discovery.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.qocal_product_discovery_setup.htm
fetched_at: 2026-09-04
---

# Record Sharing in Product Discovery

Set up record sharing and grant all runtime users of Product Discovery read access to all child records and related object records for a given product.

REQUIRED EDITIONS
View supported products and editions.

Give all runtime users read access to these objects:

If necessary, Account
Attribute Category
Attribute Category Attribute
Attribute Definition
Attribute Picklist
Attribute Picklist Excluded Value
Catalog
To use qualification or pricing:
Decision Matrix
Expression Set
Product
Product Attribute Definition
Product Classification
Product Classification Attribute
Product Component Group
Product Component Group Override
Product Related Component Override
To use qualification:
Product Disqualification
Product Qualification
Product Category Disqualification
Product Category Qualification
To use ramp deals, Product Ramp Segment
NOTE The Product Ramp Segment object is available only when you have Revenue Management and Ramp Deals enabled.
To use usage-based pricing, Unit Of Measure
NOTE The Unit of Measure object is available only when you have Revenue Management and Ramp Deals enabled.
To use Guided Product Selection:
Assessment
Assessment Question
Assessment Question Response
Omni Process
NOTE Guided Product Selection is available only for Salesforce Lightning Service Console users. These objects are available only when Guided Product Selection is set up.

To proceed with the rest of the Revenue Management setup, see Set Up Revenue Management.

=== ARTICLE: ind.product_catalog_reorder_attribute_categories.htm ===
---
article_id: ind.product_catalog_reorder_attribute_categories.htm
title: Reorder Attribute Categories and Attributes
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_reorder_attribute_categories.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_dynamic_attributes.htm
fetched_at: 2026-09-04
---

# Reorder Attribute Categories and Attributes

Control the order in which attribute categories and attributes appear when reps configure products. Organize attributes into a logical sequence that matches your business process instead of relying on alphabetical order.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To reorder attributes or attribute categories:	Manage Product Catalog

Attribute categories and their attributes appear to reps in the order that you set. Reorder them to match your business process rather than relying on the default alphabetical order.

From the Product Catalog Management app's home page, click Product Classifications or Products.
From the list view, select the product classification or product that you want to reorder attributes for.
Go to the Attributes tab.
Click the Quick Action menu, and then select Reorder Attribute Categories.
In the Reorder Attribute Categories window, drag a row to rearrange attribute categories by using its drag handle. The other categories renumber automatically.

If a product classification or product has only one attribute category, you can't reorder that category.

All attributes within a category must use the same category sequence across every record in the classification hierarchy, and that sequence must match on the associated product record.

Click Next to proceed to attribute-level sequencing.
In the Reorder Attributes window, drag a row to your preferred position by using its drag handle. The other attributes renumber automatically. Expand categories to manage attributes independently and reorder uncategorized attributes the same way.
NOTE If a category has only one attribute, you can't rearrange it independently. Reordering an inherited attribute turns it into an override attribute. If you later delete that override attribute, make sure that its original inherited sequence doesn't conflict with the display order of any other attribute. Uncategorized attributes appear in the Uncategorized section. Because they lack a category sequence, reorder them individually.
Save your changes. If you assign a new attribute to a product classification, refresh your browser before you reorder attributes again.

=== ARTICLE: ind.product_catalog_sample_apex_class_for_product_discovery_external_pricing.htm ===
---
article_id: ind.product_catalog_sample_apex_class_for_product_discovery_external_pricing.htm
title: "Sample: Apex Class for Product Discovery External Pricing"
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_sample_apex_class_for_product_discovery_external_pricing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.pricing_customize_pricing_procedures_with_apex_hooks.htm
fetched_at: 2026-09-04
---

# Sample: Apex Class for Product Discovery External Pricing

Use this sample Apex implementation to update product prices in a Product Discovery procedure plan. The class demonstrates how to query pricing data, fetch external values, and update the transaction response when using Apex hooks.

This example shows how to implement a custom Apex hook that interacts with external pricing logic. Use it as a starting point for building your own external pricing integrations.

SAMPLE APEX HOOK IMPLEMENTATION

    global class ApexUpdateExternalPricePostHook implements RevSignaling.SignalingApexProcessor {
    
    public virtual class BaseException extends Exception {}
    public class OtherException extends BaseException {}
    
    // Static flag to prevent recursive execution
    private static Boolean isUpdating = false;
    
    public RevSignaling.TransactionResponse execute(RevSignaling.TransactionRequest request) {
        System.debug('=== START OF EXECUTION ===');
        String contextId = request.ctxInstanceId;
        System.debug('Context ID: ' + contextId);
        
        // Check for recursive execution
        if (isUpdating) {
            System.debug('Preventing recursive execution for context: ' + contextId);
            RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
            response.status = RevSignaling.TransactionStatus.SUCCESS;
            response.message = 'Skipping recursive execution';
            return response;
        }
        
        try {
            isUpdating = true;
            System.debug('Executing External Pricing Post Hook');
            Context.IndustriesContext industriesContext = new Context.IndustriesContext();
            
            // STEP 1 - Query PricingProduct and extract ProductId values
            Map<String, Object> inputProdQueryItem = new Map<String, Object>{
                'contextId' => contextId,
                'tags' => new List<String>{ 'PricingProduct' }
            };
                
            Map<String, Object> itemProdQueryOutput = industriesContext.queryTags(inputProdQueryItem);
            Map<String, Object> itemProdQueryResult = (Map<String, Object>) itemProdQueryOutput.get('queryResult');
            List<Object> itemProdData = (List<Object>) itemProdQueryResult.get('PricingProduct');
            System.debug('itemProdDataCount: ' + itemProdData.Size());
            System.debug('itemProdData: ' + itemProdData);
            
            Map<String, Decimal> productPricingMap = new Map<String, Decimal>();
            List<String> pricingProductList = new List<String>();
            for (Object itemObj : itemProdData) {
                Map<String, Object> itemNode = (Map<String, Object>) itemObj;
                Map<String, Object> tagMap = (Map<String, Object>) itemNode.get('tagValue');
                String pricingId = null;
                Decimal pricingProductOrigPrice = null;
                if (tagMap.containsKey('PricingId')) {
                    pricingId = (String)((Map<String, Object>) tagMap.get('PricingId')).get('tagValue');
                }
                if (tagMap.containsKey('UnitPrice')) {
                    pricingProductOrigPrice = (Decimal)((Map<String, Object>) tagMap.get('UnitPrice')).get('tagValue');
                }
                pricingProductList.add(pricingId);
                productPricingMap.put(pricingId, pricingProductOrigPrice);
            }
            
            //Step 2 - Get External Prices
            System.debug('pricingProductList: ' + pricingProductList);
            System.debug('preApexproductPricingMap: ' + productPricingMap);
            Map<String, Decimal> outputProductPricingMap = ProductPriceCalculator.calculateProductPrices(pricingProductList);
            System.debug('outputProductPricingMap: ' + outputProductPricingMap);
            
            // STEP 3 - Build update list
            List<Map<String, Object>> itemNodeUpdates = new List<Map<String, Object>>();
            
            for (Object itemObj : itemProdData) {
                Map<String, Object> itemNode1 = (Map<String, Object>) itemObj;
                List<Object> dataPath = (List<Object>) itemNode1.get('dataPath');
                System.debug('Full item dataPath: ' + JSON.serialize(dataPath));
                dataPath.remove(0);
                
                Boolean matched = false;
                String pricingId = null;
                Map<String, Object> itemNode = (Map<String, Object>) itemObj;
                Map<String, Object> tagMap = (Map<String, Object>) itemNode.get('tagValue');
                if (tagMap.containsKey('PricingId')) {
                    pricingId = (String)((Map<String, Object>) tagMap.get('PricingId')).get('tagValue');
                }
                
                Decimal newPrice = outputProductPricingMap.get(pricingId);
                System.debug('Pricing Product Id: ' + pricingId);
                System.debug('Pricing Product Price: ' + newPrice);
                
                if(newPrice == null) {
                    System.debug('No price found for product: ' + pricingId);
                    continue;
                }
                
                // Check if the price actually needs to be updated
                Decimal currentPrice = null;
                if (tagMap.containsKey('UnitPrice')) {
                    currentPrice = (Decimal)((Map<String, Object>) tagMap.get('UnitPrice')).get('tagValue');
                }
                
                if (currentPrice != newPrice) {
                    itemNodeUpdates.add(new Map<String, Object>{
                        'nodePath' => new Map<String, Object>{ 'dataPath' => dataPath },
                        'attributes' => new List<Object>{
                            new Map<String, Object>{
                                'attributeName' => 'UnitPrice',
                                'attributeValue' => newPrice
                            },
                            new Map<String, Object>{
                                'attributeName' => 'NetUnitPrice',
                                'attributeValue' => newPrice
                            },
                            new Map<String, Object>{
                                'attributeName' => 'SubTotal',
                                'attributeValue' => newPrice
                            }
                        }
                    });
                    matched = true;
                    System.debug('Added update for product: ' + pricingId + ' with new price: ' + newPrice);
                } else {
                    System.debug('No price update needed for product: ' + pricingId);
                }
                
                if (!matched) {
                    String itemCtxId = dataPath.size() > 1 ? String.valueOf(dataPath[1]) : 'UNKNOWN';
                    System.debug('No Price match found for item ' + itemCtxId);
                }
            }
            
            // STEP 4 - Submit context update only if there are changes
            if (!itemNodeUpdates.isEmpty()) {
                System.debug('Submitting ' + itemNodeUpdates.size() + ' updates to context');
                Map<String, Object> updateInput = new Map<String, Object>{
                    'contextId' => contextId,
                    'nodePathAndAttributes' => itemNodeUpdates
                };
                System.debug('Update input: ' + JSON.serializePretty(updateInput));
                Map<String, Object> result = industriesContext.updateContextAttributes(updateInput);
                System.debug('Update result: ' + JSON.serializePretty(result));
            } else {
                System.debug('No updates needed for context: ' + contextId);
            }
            
            RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
            response.status = RevSignaling.TransactionStatus.SUCCESS;
            response.message = 'External Pricing Successful';
            return response;
            
        } catch (Exception e) {
            System.debug('Error processing context ' + contextId + ': ' + e.getMessage());
            System.debug('Stack trace: ' + e.getStackTraceString());
            RevSignaling.TransactionResponse response = new RevSignaling.TransactionResponse();
            response.status = RevSignaling.TransactionStatus.FAILED;
            response.message = 'Error: ' + e.getMessage();
            return response;
        } finally {
            isUpdating = false;
            System.debug('=== END OF EXECUTION ===');
        }
    }
}

public class ProductPriceCalculator {
    
    public static Map<String, Decimal> calculateProductPrices(List<String> pricingIds) {
        // Fetch the product names and external IDs using the product IDs
        //List<Product2> products = [SELECT Id, Name, ExternalId FROM Product2 WHERE Id IN :productIds];
        
        //if (products.isEmpty()) {
        //    throw new IllegalArgumentException('No products found with the given IDs');
        //}

        // Initialize the map to store the product prices
        Map<String, Decimal> productPrices = new Map<String, Decimal>();

        // Calculate the price for each product
        for (String pricingId : pricingIds) {
            String productName = pricingId;
            Integer asciiSum = 0;
            for (Integer i = 0; i < productName.length(); i++) {
                asciiSum += (Integer) productName.charAt(i);
            }

            Decimal priceInGivenCurrency = asciiSum;

            // Add the product ID and price to the map
            productPrices.put(pricingId, priceInGivenCurrency);
        }

        return productPrices;
    }
}

=== ARTICLE: ind.product_catalog_search_considerations.htm ===
---
article_id: ind.product_catalog_search_considerations.htm
title: Search Considerations When Using Indexed Data
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_search_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_index_and_search_of_product_catalog.htm
fetched_at: 2026-09-04
---

# Search Considerations When Using Indexed Data

When users search for a product by using a search term, Product Catalog Management checks for an exact match to the search term. If it can't find an exact match, PCM uses typo correction to help users find the product they're looking for.

REQUIRED EDITIONS
View supported products and editions.

Here are some search considerations to keep in mind.

Search terms support prefix matching, which is enabled by default and works alongside partial search. It helps locate products when your search term matches the beginning of a product name, product code, or product SKU. For example, typing “Think” finds “ThinkPro X1 Carbon” and typing “LP-X1” finds SKU “LP-X1C-2025”.

Prefix matching applies to search terms with at least 3 characters. It works on the Product Name, Product SKU, and Product Code fields, if they're marked as searchable. To make the fields searchable, see Configure Searchable Fields & Attributes.

Typo tolerance in search terms is supported, provided the search terms have three or more characters. Typo tolerance handles user input errors, such as misspellings and typographical errors, and it provides relevant search results. Typo tolerance can autocorrect a search term when the closest match is within 2 character corrections. For example, the search term “Coff” is autocorrected to “Coffee”. However, the search term “Cof” can't be autocorrected to Coffee because it takes more than 2 character corrections to reach Coffee.
You can enter a maximum of 1024 characters or 32 words in the search field as a search term per search.
EXAMPLE Acme sells a wide range of computers. Here are the different products they offer and their attributes. Only some of its fields and attributes are marked as searchable and indexed.
PRODUCT NAME (INDEXED FIELD)	STORAGE	RAM (INDEXED ATTRIBUTE)	DISPLAY SIZE (INDEXED ATTRIBUTE)	COLOR (INDEXED ATTRIBUTE)	GRAPHICS CARD
Laptop 1	256GB	16GB	15Inch	Red	16GB
Laptop 2	256GB	32GB	21Inch	Blue	16GB
Laptop 3	512GB	64GB	15Inch	Black	32GB
Laptop 4	512GB	64GB	21Inch	Silver	32GB
Desktop 1	256GB	16GB	15Inch	Red	16GB
Desktop 2	256GB	32GB	21Inch	Blue	16GB
Desktop 3	512GB	64GB	15Inch	Black	32GB
Desktop 4	512GB	64GB	21Inch	Silver	32GB
Supercomputer	1TB	256GB	24Inch	Gray	128GB

Here are some sample search terms and responses based on the indexed data.

SEARCH TERMS	RESPONSES	REASON
15Inch Laptop	
Laptop 1
Laptop 3
Desktop 1
Desktop 3
	The size field is indexed and all these products have at least 1 matching term (15Inch).
Desktop	
Desktop 1
Desktop 2
Desktop 3
Desktop 4
	The product name is indexed.
Gray Supercomputer	Supercomputer	Only one product matches the search terms.
Supercomptute	Supercomputer	The search term has more than 3 characters and there's a typo with less than 2 incorrect characters.
16GB	
Laptop 1
Desktop 1
	

The RAM attribute is indexed and these two products have a matching value.

Although 16GB also matches the graphics card for Laptop 2 and Desktop 2, they're not returned in the search because the Graphics Card attribute isn't indexed.


Lap	
Laptop 1
Laptop 2
Laptop 3
Laptop 4
	Prefix matching is enabled by default and matches the beginning of the product name, so this three-character term returns all products whose name starts with "Lap".
512GB	No results	The storage field isn't marked as searchable and isn't indexed.

=== ARTICLE: ind.product_catalog_search_options_for_product_catalog_management.htm ===
---
article_id: ind.product_catalog_search_options_for_product_catalog_management.htm
title: Search Options in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_search_options_for_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_product_discovery.htm
fetched_at: 2026-09-04
---

# Search Options in Product Catalog Management

Product Catalog Management gives your sales reps three search options to quickly find the products in a catalog. They can choose the search option based on its search capabilities and the size of the product catalog.

REQUIRED EDITIONS
View supported products and editions.

The search options are Salesforce Object Query Language (SOQL) search, Indexed search, and Product field search (SOSL based).

SOQL based search: This option is suitable for simple product searches. It can search for products by term, and it has a quick find feature within the transaction line table (such as a specific UI element). The search API supports filtering by ‌standard and custom Product2 fields.

Indexed search: This option provides comprehensive search capabilities, including configurable term-based search across various product fields, product attributes, faceted search, guided product selection (question-based), and quick find.

Product field search (SOSL): This option is suitable for large product catalogs (over 4 million products),This option searches across text-indexed fields of the product object, including key fields such as product name, description, product code, and SKU

CAPABILITY	SOQL BASED SEARCH	INDEXED SEARCH	PRODUCT FIELD SEARCH
Catalog size	Less than or equal to 250,000 products.	Less than or equal to 4 million products.	More than 4 million products and up to 20 million products. 
Setup	Not Required	Required	Required
Supported capabilities	Term-based search by product name	
Faceted search
Full and partial indexing
Search index configuration
Term-based search for product fields or attributes
Guided product selection
	Term-based search by product fields such as name, description, product code, and SKU.
Unsupported Capabilities	
Faceted search
Attribute- based search
Guided product selection
Search by translated product name
	Search by translated, searchable, and filterable field or attribute values.	
Faceted search
Attribute -based search
Guided product selection
Search by translated product name and description
Product Field Search in Product Catalog Management
Sales reps can use the Product field search option to quickly locate specific products within large catalogs (millions of products) by searching text-indexed fields such as Product Name, Description, Product Code, and SKU.
Product Index and Search in Product Catalog Management
Enable sales reps to find products quickly and easily with an index of all the products available across catalogs. Specify searchable fields and attributes that users can use to search the index for products.
Semantic Search
Semantic search reduces “no results found” pages, lowers bounce rates, and improves conversions by interpreting search intent. It matches product names, descriptions, categories, and dynamic attributes based on the words that buyers enter in the search bar.

=== ARTICLE: ind.product_catalog_semantic_search.htm ===
---
article_id: ind.product_catalog_semantic_search.htm
title: Semantic Search
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_semantic_search.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_search_options_for_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Semantic Search

Semantic search reduces “no results found” pages, lowers bounce rates, and improves conversions by interpreting search intent. It matches product names, descriptions, categories, and dynamic attributes based on the words that buyers enter in the search bar.

REQUIRED EDITIONS
View supported products and editions.

By default, Product Discovery uses keyword-based search, which only matches exact terms. If users don’t know the exact product name or type it differently, they can miss relevant results.

Semantic search improves product discovery by:

Interpreting synonyms (for example, “power” also finds products described with “energy”).
Handling variations and typos (for example, “wotches” matches “watches”).
Searching across product names, descriptions, and attributes.
Reducing “no results found” pages and increasing relevant results.

Semantic search supports up to 15 searchable fields. Three fields are fixed — product name, product description, and category name. The remaining 12 can be configured from the searchable fields in Index and Search Configuration, including dynamic attributes.

Semantic search helps users find what they’re looking for even when they don’t know the exact product name or spelling. This reduces abandoned searches, surfaces relevant alternatives, and makes the shopping experience more intuitive.

Enable Semantic Search for Product Discovery
Enable Einstein semantic search in Product Discovery to interpret search intent and surface relevant results based on synonyms, variations, and attributes.
Explore Examples of Semantic Search
See how Einstein semantic search improves results across different types of queries, including synonyms, abbreviations, misspellings, and product features.

=== ARTICLE: ind.product_catalog_set_default_catalog.htm ===
---
article_id: ind.product_catalog_set_default_catalog.htm
title: Set a Default Product Catalog
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_set_default_catalog.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_catalogs.htm
fetched_at: 2026-09-04
---

# Set a Default Product Catalog

Set a default catalog for your product list page to show the most relevant products for your users. For complex orders, configure your product list page in Lightning App Builder or flows to help users to easily switch catalogs.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To set a default catalog:	Manage Product Catalog
In Setup, find and select Product Discovery Settings.
Select a default catalog.

=== ARTICLE: ind.product_catalog_set_the_display_order_of_catalog_categories.htm ===
---
article_id: ind.product_catalog_set_the_display_order_of_catalog_categories.htm
title: Set the Display Order of Catalog Categories
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_set_the_display_order_of_catalog_categories.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_sort_categories_in_a_catalog.htm
fetched_at: 2026-09-04
---

# Set the Display Order of Catalog Categories

Define the display order of catalog categories by assigning numeric sort order values. Use null, negative, zero, or positive numbers to control which categories appear first, in the middle, or last.

REQUIRED EDITIONS
View supported products and editions.
Open a catalog and click Categories.
Click Edit.
To determine the sort order of the category, in the Sort Order field, enter a numeric value.
Leave the field blank (null) to display the category before all defined values.
Enter a negative number to display the category after null values but before zero and positive values.
Enter 0 to display the category after null and negative values but before positive values.
Enter a positive number to display the category last in the sequence.
Save your changes.

=== ARTICLE: ind.product_catalog_set_up_data_translation_in_product_catalog_management.htm ===
---
article_id: ind.product_catalog_set_up_data_translation_in_product_catalog_management.htm
title: Set Up Data Translation in Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_set_up_data_translation_in_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_data_translation.htm
fetched_at: 2026-09-04
---

# Set Up Data Translation in Product Catalog Management

Enable data translation and add supported languages so you can translate PCM entities into multiple languages. After you enable data translation, you can configure which languages to support and make them available in Product Catalog Management (PCM). Translations appear at runtime only after you configure Index Settings and run a full reindex.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To enable translation:	Manage Product Catalog
To enable workbench:	Manage Product Catalog
Enable data translation for your org. See Enable Data Translation.
Enable Translation Workbench in your org. See Enable or Disable Translation Workbench.
Add one or more translation languages in the translation language settings for your user account. See Add Translated Languages and Translators.
Configure default and supported languages. See Configure Search Index Localization.
Rebuild index. See Build the Product Index.

=== ARTICLE: ind.product_catalog_set_up_enhanced_product_discovery_features.htm ===
---
article_id: ind.product_catalog_set_up_enhanced_product_discovery_features.htm
title: Set Up Enhanced Product Discovery Features
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_set_up_enhanced_product_discovery_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_enhanced_product_discovery_experience.htm
fetched_at: 2026-09-04
---

# Set Up Enhanced Product Discovery Features

Turn on enhanced Product Discovery features so that Product Discovery can show transaction previews, configuration rule outcomes, and rule-based recommendations, and automatically save product changes while users browse the catalog.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To manage enhanced product discovery:	Product Catalog Management Designer

Before you begin:

Product Discovery is enabled in your org.
Product Catalog Management is configured for the catalog you use for quoting.
Turn On Enhanced Product Discovery Features
From Setup, in the Quick Find box, enter Product Discovery, and then select Product Discovery Settings.
Turn on Transaction Preview, Configuration Rules, Product Recommendations, and Auto Save.
Configure Constraint Rules for Product Discovery

In Product Configurator, you can define rules in a constraint model to control how products behave during Product Discovery, including which products are disabled, which products are recommended, and which messages users see. After you activate the model, Product Discovery evaluates these rules in real time as users add products to the transaction.

NOTE

Set the virtual type annotation to true for the transaction type so Product Discovery can evaluate rules against the transaction header, such as a Quote or Order, during catalog browsing.

Set up Constraint Rules Engine for Product Configurator. See Set Up Constraint Rules Engine for Product Configurator
Create a Constraint Model
In the constraint model, add or update rules that evaluate transaction line items.

Use disable rules to make products unavailable when the current transaction meets specific conditions. Use message rules to show info, warning, or error messages when the current transaction meets specific conditions. Use recommendation rules to show related or add-on products based on the current transaction, without blocking selection.

Save your changes to the constraint model.
Activate the updated model so Product Discovery evaluates the rules at run time.

For detailed rule authoring, see the Constraint Modeling Language

=== ARTICLE: ind.product_catalog_set_up_objects_for_pcm.htm ===
---
article_id: ind.product_catalog_set_up_objects_for_pcm.htm
title: Set Up Objects for Product Catalog Management
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_set_up_objects_for_pcm.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Set Up Objects for Product Catalog Management

To complete the setup of Product Catalog Management, adjust the page layout and field access on the product catalog objects.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management
Update the Attribute Definition Page Layout.
From the Object Manager for Attribute Definition, go to Page Layouts.
Click on Attribute Definition Layout.
Drag and drop the related lists to your Attribute Definition page layout.
Related Product Attribute Definitions
Related Product Classifications
Update the Category Page Layout.
From the Object Manager for Category, go to Page Layouts.
Click New button and create a page layout.
Click the name of the new category page layout you created. Add these related lists:
Product Category Qualifications
Product Category Disqualifications
Products
Click Page Layout Assignment button and assign the new layout to System Admin and Standard User.
Save your changes.
Update the Product Page Layout.
From the Object Manager for Product, go to Page Layouts.
Click on Product Layout.
Drag and drop these fields to your product page layout.
Configure During Sale
Based On
Availability Date
Discontinued Date
End Of Life Date
Product SKU
Display URL
Sell Only With Other Products
Is Assetizable
Product Type
Specification Type
Add these related lists to your product page layout.
Categories
Product Selling Model Option
Inherited Attributes
Overridden Inherited Attributes
Product Qualifications
Product Disqualifications
Child Components
Overridden Bundle Components
Overridden Product Component Attributes
Product Component Group
Overridden Product Component Groups
Click on Record Types.
Create these Record Types: Commercial and Technical.
Make them available for all profiles.
Set Commercial as the default record type.
When creating a record type, use the same product layout for all record types.
Update the Product Classification Page Layout.
From the Object Manager for Product Classification , go to Page Layouts.
Click on Product Classification Layout.
Drag and drop the Parent Product Classifiaction field.
Add theses related lists to your product classification page layout
Inherited Attributes
Overridden Inherited Attributes

=== ARTICLE: ind.product_catalog_set_up_product_catalog_management.htm ===
---
article_id: ind.product_catalog_set_up_product_catalog_management.htm
title: Product Catalog Management Set Up
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_set_up_product_catalog_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_introduction.htm
fetched_at: 2026-09-04
---

# Product Catalog Management Set Up

Product Catalog Management includes different permission sets for users. These users or personas perform various roles in implementing and managing your product portfolio. Configure your users to use Product Catalog Management and assign permission sets so that the users can access catalogs, products, attributes, rules, context definitions, product bundles, and more. To complete the setup of Product Catalog Management, adjust the page layout and field access on the product object.

REQUIRED EDITIONS
View supported products and editions.
Set Up Objects for Product Catalog Management
To complete the setup of Product Catalog Management, adjust the page layout and field access on the product catalog objects.
Record Sharing in Product Catalog Management
Set up record sharing and grant all runtime users of Product Catalog Management read access to all child records and related object records for a given product.
Create Product Specifications in Revenue Management
With Product Catalog Management, you can define a specification type for the products that are unique to your industry. A product specification type is associated with a product specification record type.
Customize and Extend the Product Catalog Management Home Page
Manage attributes, products, catalogs, and rules on the Product Catalog Management app’s home page. Your admin can use the Lightning App Builder to customize and extend the home page for your users.
Translate Product Catalog Data
Display product catalog data in the user’s configured language with data translation. Localize key Product Catalog Management (PCM) objects so buyers and sales teams can search, filter, and browse in their preferred language, improving accuracy and adoption.
Configure the Product Catalog Management Cache
Store frequently requested product details in a dedicated cache for faster retrieval. You can then access product details without reloading them from the source every time. When product details change, the system detects the updates and regenerates the cache. If a user requests information for a product that isn’t in the cache, the system fetches the information from the database and saves it to the cache for future requests.
Configure Decimal Support for Unit-Level Prices
Improve pricing accuracy by configuring up to six decimal places for unit-level rate and currency fields. Show precise values for unit prices, list prices, and discounts across product discovery, quote, and order pages. Standard summary and total fields retain their default decimal settings.
Turn On List Price from Cache
To retrieve product details faster, cache list prices from price book entries with the product details.
Turn On Price Book Filtering
Price book filtering addresses incomplete product results in large catalogs when the price book and catalog overlap are minimal. Price book filtering retrieves only the products that are associated with the selected price book, so you see relevant results without going through the entire catalog.
Product Discovery Setup
To populate the information that users see when they use Product Discovery, select a context definition, and if necessary, select a qualification procedure and a pricing procedure.

=== ARTICLE: ind.product_catalog_set_up_product_deep_clone.htm ===
---
article_id: ind.product_catalog_set_up_product_deep_clone.htm
title: Set Up Product Deep Cloning
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_set_up_product_deep_clone.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_deep_clone_in_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Set Up Product Deep Cloning

Customize the product deep clone settings to add the appropriate context definition and expression set.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To set up a product deep clone:	Product Designer
From Setup, in the Quick Find Box, enter Deep Clone Product Settings, and select it.
Select the required context definition and expression set.

You can choose only the ProductDeepCloneContext context definition or a context definition extended from ProductDeepCloneContext.

ProductDeepCloneContext is available as the default context definition. You can extend the ProductDeepCloneContextcontext definition to add standard or custom fields and objects.

Always define context tags on relationship nodes, not on canonical nodes. When performing ExpressionSet calculations, reference context tags from these relationship nodes.

EXAMPLE

Scenario 1: Include a custom field.

You have a custom field on a Product X and want it included in the deep-cloned product, you need to include this custom field in the product X deep clone definition. Extend the product X deep clone definition to include the custom field. Make sure to map this field to the corresponding SObject field in the context mapping.

Scenario 2: Include an extended object.

You have an extended object related to Product X and want to include it in the deep cloned product, extend the product X deep clone definition to include the extended object. Define the appropriate relationship mapping between the two objects within the context definition. Include the fields of the extended object that you want to deep clone.

Scenario 3: Modify field values.

If the current product has a date field set to "TODAY," and you want the cloned product to have a date field set to "TODAY + 10 days," you can define a rule within the expression set to achieve this. Further, the date field must be present in the context definition and must have a context tag defined.

=== ARTICLE: ind.product_catalog_simulate_and_activate_a_qualification_rule_procedure.htm ===
---
article_id: ind.product_catalog_simulate_and_activate_a_qualification_rule_procedure.htm
title: Simulate and Activate a Qualification Rule Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_simulate_and_activate_a_qualification_rule_procedure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_qualification_rules.htm
fetched_at: 2026-09-04
---

# Simulate and Activate a Qualification Rule Procedure

Before you activate your qualification rule procedure, run simulations to test whether the rules you defined in the decision table are accurate and give you the desired output. If your rule procedure doesn’t work as expected, edit the values and simulate again. When you’re satisfied, activate the rule procedure version.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To create a qualification rule procedure:	Manage Product Catalog
To use a decision table:	Rules Engine Runtime
To create a context definition:	Context Service Admin
From the Product Catalog Management app’s home page, click Qualification Rules Procedures.
From the Qualification Procedures list view page, open the qualification rule procedure version in the Expression Set Builder.
Click Simulate.
To pass sample data to the expression set for simulation, select an input mode from the input tab.
Simplified	Enter sample values for the variables defined in the qualification rule procedure in the form. To export the sample data as JSON input, click Export JSON Input (1).
Advanced	Enter sample values for the variables defined in the qualification rule procedure in the JSON Input text box. Alternatively, download the sample JSON Input file (2), modify the file with your input values, and paste the updated JSON in the text box.
 
Add the product ids or product category IDs for the products for which you want to run the simulation. Leave the Is Qualified field blank.
Click Simulate.
The simulation results are visible in a tabular format under the Output tab. To view additional details, click View Details. The simulation results give you the reason for a product or product category disqualification. The qualified column indicates the product or product category qualification status.
If you're happy with the simulation result, you’re ready to activate the qualification rule procedure. Perform these steps before activating your procedure:
In the left pane, click Expression Set Properties , and enter a rank under Advanced Details. The rank can be any positive number.
In the left pane, click Element Details
and select Include in Output.
Save the qualification rule procedure.
Click Activate.

All the pieces are now in place for your qualification rule. As a best practice, check the Product Discovery Settings to ensure that you have the correct Context Definition and Qualification Procedure selected there.

To check these settings, go to Setup | Product Discovery | Product Discovery Settings.

=== ARTICLE: ind.product_catalog_sort_categories_in_a_catalog.htm ===
---
article_id: ind.product_catalog_sort_categories_in_a_catalog.htm
title: Sort Categories in a Catalog
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_sort_categories_in_a_catalog.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_catalogs.htm
fetched_at: 2026-09-04
---

# Sort Categories in a Catalog

Make the browsing experience consistent and predictable for your buyers by defining category display order in Product Catalog Management (PCM) at design time. The same order appears in Product Discovery (PD) at runtime.

REQUIRED EDITIONS
View supported products and editions.

Unsorted categories can confuse users and slow product discovery. Adding sort order values ensures a consistent browsing experience and lets catalog admins prioritize categories without custom workarounds.

Categories sort in the sequence: null → negative → zero → positive.
If all categories have a null sort order, they’re listed by creation time in descending order (newest first).
If two or more categories share the same sort order value, they’re listed by creation timestamp in descending order (newest first).
Editing a category doesn’t change its position unless you change its sort order.

Suppose your hardware catalog contains these categories:

Desktop (Sort Order = null, created on Jan 1)
Tablet (Sort Order = –1, created on Feb 1)
Laptop (Sort Order = 0, created on Mar 1)
Monitor (Sort Order = 1, created on Apr 1)
Printer (Sort Order = null, created on May 1)

When users browse the catalog, the categories appear in this order:

Printer (null, newest created among nulls)
Desktop (null, older null)
Tablet (–1, negative)
Laptop (0)
Monitor (1, positive)
Set the Display Order of Catalog Categories
Define the display order of catalog categories by assigning numeric sort order values. Use null, negative, zero, or positive numbers to control which categories appear first, in the middle, or last.

=== ARTICLE: ind.product_catalog_translate_product2_and_productcategory_data.htm ===
---
article_id: ind.product_catalog_translate_product2_and_productcategory_data.htm
title: Bulk Export and Import Translation Files
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_translate_product2_and_productcategory_data.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_data_translation.htm
fetched_at: 2026-09-04
---

# Bulk Export and Import Translation Files

Export Product Catalog Management (PCM) translation data into STF or XLIFF files, add your localized values, and import the files back into Salesforce. Use this method to update large volumes of product, category, and attribute translations at once. After import, reindex the catalog so users see the localized values in product listings and search results.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To translate product and product category data:	Manage Product Catalog
Bulk export translation files.
From Setup, find and select Export.
Set Translation Type to Data.
In Available Objects, select the PCM entities to translate (for example, Product2, Product Category, Product Classification Attribute, Attribute Picklist Value) and move them to Selected Objects.
Set Export Type to Source.
Set Format to STF or XLIFF.
Click Export.
Salesforce emails a ZIP file with the translation files. Each file contains translation elements for the selected PCM objects.
Edit and import translation files.
If you export in XLIFF (.xlf):
Open the file in a text editor.
For each <trans-unit>, keep <source> unchanged and add your translation in <target>.
Make sure the target-language attribute matches your language (for example, fr).
Save the file.
If you export in STF:
Open the file in a text editor.
Add the language code under Translation type: Data.
For Product2, translate names, descriptions, help text, and enum (picklist) values.
For Product Category, translate names and descriptions.
For Product Classification Attributes and Dynamic Picklists, update the relevant values.
Save the file.
From Setup, find and select Import.
Upload the translated file and click Import. See Import Translated Files.
Reindex the catalog.
After importing translations, rebuild the full index to apply them. See Build an Index in Product Catalog Management.
(Optional) Verify translations.

In the UI:

Log in as a user whose org language matches a translation.
Browse catalogs and confirm product and category names are displayed in that language.
Search using translated terms (for example, enter portable in French to return translated laptop products).

With SOQL:

Use an approved open-source tool to query Salesforce objects.
Run SOQL queries for the translation objects to confirm values.
Product2DataTranslation: Query Name, Description, HelpText, and picklist/enum fields.
ProductCategoryDataTranslation: Query Name and Description.
Use the corresponding translation objects for Product Classification Attributes and Dynamic Attributes.

=== ARTICLE: ind.product_catalog_turn_on_list_price_from_cache.htm ===
---
article_id: ind.product_catalog_turn_on_list_price_from_cache.htm
title: Turn On List Price from Cache
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_turn_on_list_price_from_cache.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Turn On List Price from Cache

To retrieve product details faster, cache list prices from price book entries with the product details.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To turn on List Price from Cache:	Product Catalog Management Designer

Before you begin:

Turn on the Product Catalog Management Cache and refresh the cache. See Configure the Product Catalog Management Cache.

From Setup, in the Quick Find box, enter Product Discovery, and then select Product Discovery Settings.
Turn on List Price from Cache.
NOTE

If you turn on Multi-Currency with List Price from Cache setting turned on, then refresh the cache after enabling Multi-Currency.

=== ARTICLE: ind.product_catalog_turn_on_price_book_filtering.htm ===
---
article_id: ind.product_catalog_turn_on_price_book_filtering.htm
title: Turn On Price Book Filtering
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_turn_on_price_book_filtering.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_set_up_product_catalog_management.htm
fetched_at: 2026-09-04
---

# Turn On Price Book Filtering

Price book filtering addresses incomplete product results in large catalogs when the price book and catalog overlap are minimal. Price book filtering retrieves only the products that are associated with the selected price book, so you see relevant results without going through the entire catalog.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS
NEEDED
To turn on price book filtering:	Product Catalog Management Designer

Before you begin:

If you're using indexed data, rebuild the index before turning on Price Book Filtering. Index is required only the first time, subsequent updates don't need a full rebuild. See Build the Product Index.

From Setup, in the Quick Find box, enter Product Discovery, and then select Product Discovery Settings.
Turn on Price Book Filtering.

=== ARTICLE: ind.product_catalog_turn_on_product_variants.htm ===
---
article_id: ind.product_catalog_turn_on_product_variants.htm
title: Turn On Product Variants
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_turn_on_product_variants.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_create_product_variants_in_revenue_cloud.htm
fetched_at: 2026-09-04
---

# Turn On Product Variants

Enable product variation to create and manage variant products in Product Catalog Management and make them available for product discovery.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To enable product variants:	Manage Product Catalog
In Setup, find and select Product Discovery Settings.
Turn on Product Variants.

If Use Indexed Data for Product Listing and Search is enabled, toggling this setting requires reindexing of products.

NOTE After enabling Product Variants and creating variation products, do not disable this feature. Disabling it can cause errors and data inconsistencies.

=== ARTICLE: ind.product_catalog_validate_product_definition.htm ===
---
article_id: ind.product_catalog_validate_product_definition.htm
title: Validate the Product Definition
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_validate_product_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_bundled_product_validations.htm
fetched_at: 2026-09-04
---

# Validate the Product Definition

Use Validate Product Definition to check the integrity of your product bundles.

REQUIRED EDITIONS
USER PERMISSIONS NEEDED
To validate the product definition:	

Manage Product Catalog

Product Catalog Management Designer Permission Set

From the Product Catalog Management app’s home page, click Products.
From the product list view, click the simple product or static bundle product that you want to validate the product definition for.
Click  next to the product, and click Validate Product Definition.
The validation results notify you of any checks that have failed and guide you on how to take corrective action.

Take corrective action as suggested and validate the product definition again.

=== ARTICLE: ind.product_catalog_verify_the_facets_on_the_product_discovery_product_list_page.htm ===
---
article_id: ind.product_catalog_verify_the_facets_on_the_product_discovery_product_list_page.htm
title: Verify the Facets on the Product Discovery Product List Page
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_verify_the_facets_on_the_product_discovery_product_list_page.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_faceted_search.htm
fetched_at: 2026-09-04
---

# Verify the Facets on the Product Discovery Product List Page

Now that we have set up filterable fields and attributes, let's check the facets on the product discovery product list page. We want to see how the search experience has changed with the facets configured.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To build and rebuild indexes:	

Manage Product Index and Search

AND

View Product Catalog

Create a new quote or open an existing quote. For this example, let us open an existing quote.
Click on Browse Catalog.
On the Product Discovery List page, search for a Compound in the global search bar.
The search results show all three products with the term compound in the product name.
Select the filter Gel Quantity.
Only products matching Gel Quantity are shown.

=== ARTICLE: ind.product_catalog_view_visibility_rule_outcomes_during_product_discovery.htm ===
---
article_id: ind.product_catalog_view_visibility_rule_outcomes_during_product_discovery.htm
title: Product Visibility and Recommendations in Real Time
source_url: https://help.salesforce.com/s/articleView?id=ind.product_catalog_view_visibility_rule_outcomes_during_product_discovery.htm&type=5&release=264
release: 264
release_name: Winter '27
area: pcm
parent_article: ind.product_catalog_enhanced_product_discovery_experience.htm
fetched_at: 2026-09-04
---

# Product Visibility and Recommendations in Real Time

As you browse the catalog, Product Discovery evaluates the current transaction against configuration rules. Based on the rules you configure, Product Discovery shows messages, disables products, and recommended products directly in the browsing experience.

REQUIRED EDITIONS
View supported products and editions.
USER PERMISSIONS NEEDED
To view visibility rules:	Product Catalog Management Designer
Visibility Rules

Visibility rules control how products appear in the catalog based on your current transaction. When configured rules evaluate the transaction, products that don't meet the conditions are restricted or hidden from selection. This makes sure that sales reps see only the products that are valid for the current context, reducing errors and improving accuracy during the quoting process.

On the Browse Products page, browse or search for products.
To find products disabled by rules, apply the Disqualified filter.
Review the message to understand why a product is disabled.
EXAMPLE Example: Disable products based on the transaction.

Use a disable rule to make certain products disabled in Product Discovery when the transaction meets specific conditions. In this example, when the transaction includes a Desktop Computer, Product Discovery disables a set of related products while users browse the catalog.

@(virtual = "true")
type Transaction {
  @(sourceContextNode = "SalesTransaction.SalesTransactionItem")
  relation lineitems : LineItem;
  rule(
    lineitems[DesktopComputer],
    "disable",
    "relation", "LineItem",
    "type", "DisabledProducts",
    "message", "These products are unavailable based on the current transaction."
  );
}
type LineItem;
type DesktopComputer : LineItem;
type DisabledProducts;
type Monitor  : DisabledProducts;
type Keyboard : DisabledProducts;
type Mouse    : DisabledProducts;

Product Recommendations

Recommendation rules show suggested products based on your current transaction. You can review these suggestions, understand why they’re recommended, and easily add them to your quote.

On the Browse Products page, click Recommendations in the left panel.
Review the suggested products and the messages explaining why they’re recommended.
Add recommended products directly from the list to the transaction, or continue browsing.

To view products that are disabled but also recommended, use the Disqualified filter.

EXAMPLE Example: Recommend products based on the transaction.

Recommendation rules show relevant products based on the current transaction. Recommended products appear in the Recommendations panel and can be added to the transaction, but the rules don't restrict or prevent product selection.

In this example, when the transaction includes a Primary Product, Product Discovery recommends a group of products while users browse the catalog.

@(virtual = "true")
type Transaction {
  @(sourceContextNode = "SalesTransaction.SalesTransactionItem")
  relation lineitems : LineItem;
  rule(
    lineitems[Laptop],
    "recommend",
    "type", "RecommendedProducts",
    "message", "Consider these add-ons for the selected laptop."
  );
}
type LineItem;
type Laptop : LineItem;

type RecommendedProducts;
type Headset      : RecommendedProducts;
type Mouse     : RecommendedProducts;
type ExtendedWarranty : RecommendedProducts;

Auto-Add and Auto-Delete

Product Discovery evaluates configured rules and automatically adds or removes products from a transaction when the specified conditions are met.

On the Browse Products page, add a product that triggers a rule to add products.
Click Preview to view the transaction.
Review the products that were automatically added to the transaction.
EXAMPLE Example: Automatically add products based on the transaction.
@(virtual = "true")
type Transaction {
  @(sourceContextNode = "SalesTransaction.SalesTransactionItem")
  relation lineitems : LineItem;
  rule(
  require(lineitems[APIAccessRequests], lineitems[QuantumBitDatabase], "Unable to add Quantum Bit Database");
}

type LineItem;
type APIAccessRequests : LineItem;

type QuantumBitDatabase : RequiredProducts;

Messages

Messages display error, warning, or informational alerts based on the current transaction. They appear at the top of the Browse Products page when a message rule applies, providing guidance without interrupting browsing.

On the Browse Products page, select or add a product.
If an alert appears at the top of the page, click Errors, Warnings, or Info to view the messages.
EXAMPLE Example: Display messages based on the current transaction

Use a message rule to show info, warning, or error messages in Product Discovery when the transaction meets specific conditions. Message rules guide users by explaining important conditions or considerations as they browse the catalog.

In this example, when the transaction includes a Primary Product, Product Discovery shows a message to inform the user.

@(virtual = "true")
type Transaction {
  @(sourceContextNode = "SalesTransaction.SalesTransactionItem")
  relation lineitems : LineItem;

  rule(
    lineitems[PrimaryProduct],
    "message",
    "info",
    "message", "Info: Review available options before continuing."
  );

  rule(
    lineitems[PrimaryProduct],
    "message",
    "warning",
    "message", "Warning: This selection may require additional review."
  );

  rule(
    lineitems[PrimaryProduct],
    "message",
    "error",
    "message", "Error: This selection requires a correction before you proceed."
  );
}

