# Salesforce Help 264 — área: agents (17 artículos)

=== ARTICLE: ind.rev_agent_approval_agent.htm ===
---
article_id: ind.rev_agent_approval_agent.htm
title: Agentforce for Advanced Approval
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_approval_agent.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-07
---

# Agentforce for Advanced Approval

The Approval Agent brings the full approval lifecycle into the conversation. Sales reps and reviewers can submit records, track pending work, generate summaries and comments, and take action on approvals, all from Salesforce or Slack. When a decision is made, the agent syncs the outcome to the underlying approval record and confirms the action in the conversation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
NOTE Before you begin, set up Agentforce for Revenue Management and connect the agent to slack.

When sales reps, reviewers, and approval admins need to submit, review, or manage approval requests, Approval Agent gives them a conversational way to complete approval tasks without navigating multiple records or systems. Users can build custom topics to submit records for approval, track pending submissions, retrieve approval work items, generate AI-powered summaries and comments, and take action on decisions directly from Salesforce or Slack.

Approval Agent follows the approval workflows, routing rules, and approvers configured by your Salesforce admin. When a reviewer makes a decision, the agent syncs the outcome to the underlying approval record and confirms the action in the conversation.

Approval Agent is designed for users who participate in the approval lifecycle, such as:

Sales reps who submit quotes and other records for approval and need to track or resubmit requests.

Reviewers who need to retrieve approval work items, understand requests, and make approval decisions.

Use Approval Agent to:

Give sales reps instant visibility across entities like Quotes, Cases, and other objects to quickly identify pending reviews and pinpoint exactly where each approval stands.

Reduce context switching by letting users track, review, and manage approvals in the same conversation.

Accelerate review cycles with AI-generated summaries and suggested approval comments.

Keep approvals aligned with changing information by recalling and updating.

Approval Agent runs within your Salesforce org and uses your existing approval workflows, approvers, and routing rules. Reviewers can retrieve and review multiple work items and get AI-generated summaries with key record details and context. For quote approvals, they can also review quote line items before making a decision. The agent provides approve or reject actions and can suggest comments that reviewers can accept, edit, or replace. Decisions are synced to the underlying approval record and confirmed in the conversation.

Subagent: Approval Management
Manage approval work items and submissions by summarizing, approving, rejecting, or recalling requests, with optional comments.
Subagent: Search Approval Record
Filter and list approval work item or approval submission records based on related record type, date ranges, status, and assignee context.
Subagent: Summarize Multiple Approval Work Items
Filter approval work item records and summarize them in aggregate, providing per-record details so reviewers can quickly understand the context of each approval.

=== ARTICLE: ind.rev_agent_billing_topic_invoice_line_explanation.htm ===
---
article_id: ind.rev_agent_billing_topic_invoice_line_explanation.htm
title: "Subagent: Invoice Line Explanation"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_billing_topic_invoice_line_explanation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.billing_agentforce_billing_agent.htm
fetched_at: 2026-09-07
---

# Subagent: Invoice Line Explanation

Help users understand their invoice lines by providing detailed explanations of each charge, including the reasons and calculation methods.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license and the Revenue Cloud Billing license with the Agentforce Employee Agent add-on.
Topic Details
API Name	InvoiceLineExplanation
Included Agent Actions	

Get Invoice Line Records

Explain Invoice Line


Required Setup	Set Up Agentforce for Revenue Management
Considerations
The agent is available to authenticated users in Lightning Experience. Customers and partners who use Experience Cloud don’t yet have access to external digital agents.
If multiple invoice line records are found, the agent presents them as a selectable list for users to choose from.
Examples of Utterances Classified to This Topic
Explain the Slack line for the invoice DOC-00089.
Explain the charges for invoice line Professional Services in invoice DOC-00089.
I'm seeing a 'Slack' charge line for three units here, but the original order was placed for one unit. Can you explain?
Can you also explain the "Usage for SMS" charge? I thought that was included in my AT&T mobile plan.
Why is there an overage charged in the invoice DOC-0075?
Hi, I see charges for Professional Services on this invoice, but the service wasn't fully delivered. Can you explain the charge breakdown?
Why am I charged for 10 monitors when I only ordered 6?
Billing Employee Assistance Use Case
At Acme, the billing team spent hours digging through orders, amendments, and cancellations whenever a customer questioned an invoice. Each case meant switching between systems, piecing together the story of a charge, and explaining it to the customer. This process often delayed resolutions and sometimes left customers frustrated.

=== ARTICLE: ind.rev_agent_overview.htm ===
---
article_id: ind.rev_agent_overview.htm
title: Agentforce for Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_overview.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
fetched_at: 2026-09-07
---

# Agentforce for Revenue Management

Agentforce for Revenue Management is a suite of AI-powered agents designed to streamline product-to-cash operations. These agents help users manage every step of the revenue lifecycle, from quote creation and management to deriving overage consumption and handling billing inquiries with clear invoice line breakdowns. By using generative AI for both reasoning and orchestration, the agents cut down on manual work so that users drive more revenue with greater speed and accuracy.

Agent Templates in Revenue Management
Quickly deploy AI-powered agents for your product-to-cash operations using Revenue Management agent templates. All Agentforce templates and topics within Revenue Management are Agentforce Employee Agent (AEA) templates. You must have access to the Revenue solutions to use them.
Set Up Agentforce for Revenue Management
To use the Revenue agent templates, configure the required Revenue and manage agent features and assign permissions.
Set Up Community and Partner Access for Agentforce in Revenue Management
Make an Agentforce for Revenue agent available to customers or partners by configuring community or partner sites and enabling Embedded Messaging. You can create a community site for the Billing Service Assistance agent and a partner site for the Revenue Quote Management agent.
Considerations for Agentforce in Revenue Management
To use Agentforce for Revenue, consider supported functionality, usage, limitations and allowances, limits, and other issues.
Agentforce for Revenue Quote Management
With the new Revenue Quote Management template, your sales reps can streamline quoting workflows and accelerate the sales cycle. This template comes with a suite of advanced Agentforce actions that automate routine tasks like product selection, quote creation, and management, helping sales reps create and update quotes and line items within minutes. By leveraging simple prompts, sales reps can easily create initial, renewal, and amendment quotes. This allows them to respond to customer needs more quickly and accurately, ultimately improving productivity and driving more meaningful customer interactions.
Agentforce for Billing Employee Assistance
When internal finance or billing teams need clarity on billing data for customer accounts, Billing Employee Assistance gives them a conversational way to understand charges and retrieve billing information. Employees can ask questions about invoice charge explanations, payment plans, outstanding account balances, or upcoming payment due dates. They get clear explanations powered by generative AI, without navigating multiple billing records or systems.
Agentforce for Billing Service Assistance Agent
Use Billing Service Assistance Agent to give customers fast, conversational explanations for invoice charges directly in your Experience Cloud billing portal.
Agentforce for Advanced Approval
The Approval Agent brings the full approval lifecycle into the conversation. Sales reps and reviewers can submit records, track pending work, generate summaries and comments, and take action on approvals, all from Salesforce or Slack. When a decision is made, the agent syncs the outcome to the underlying approval record and confirms the action in the conversation.
Revenue Subagent Reference
To optimize common revenue use cases, explore the standard agent topics available in Revenue Management. While these agent topics aren't included with a Revenue agent template, you can add them to any Agentforce Employee Agent template.

=== ARTICLE: ind.rev_agent_pcm_topic_product_description_generation.htm ===
---
article_id: ind.rev_agent_pcm_topic_product_description_generation.htm
title: "Subagent: Product Description Generation"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_pcm_topic_product_description_generation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_topic_reference.htm
fetched_at: 2026-09-07
---

# Subagent: Product Description Generation

Generate and refine product descriptions and update records with new product descriptions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license with the Agentforce Employee Agent add-on.
Topic Details
API Name	ProductDescriptionGeneration
Included Product Description Generation Actions	

Generate Product Description


Included Standard Actions	

Query Records

Update Record


Required Setup	Set Up Agentforce for Revenue
Considerations
The agent is available to authenticated users in Lightning Experience. Customers and partners who use Experience Cloud don’t yet have access to external digital agents.
Examples of Utterances That Trigger This Topic
"Generate a description for QuantumBit Gold Platform."
"Generate a description for this product."

=== ARTICLE: ind.rev_agent_pcm_topic_product_selection.htm ===
---
article_id: ind.rev_agent_pcm_topic_product_selection.htm
title: "Subagent: Product Selection"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_pcm_topic_product_selection.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.qocal_agentforce_quote_mgmt.htm
fetched_at: 2026-09-07
---

# Subagent: Product Selection

Use Agentforce to power product discovery and filtering with AI-driven assistance. Sales users can use the Product Selection topic to search the product catalog, ask clarifying questions, and refine results based on customer criteria. The topic helps users explore available products, review key details, and receive recommendations that support accurate and complete quote building. You can customize the Product Selection topic to match your catalog, sales workflows, and conversational experience.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license with the Agentforce Employee Agent add-on.
Topic Details
API Name	ProductSelection
Included actions	

Find Products

Get Product Details

Get Rule-Based Product Recommendations (Beta)


Required Setup	Set Up Agentforce for Revenue Management
Examples of Utterances Classified to This Topic
USER SAMPLE INPUT	ACTIONS ENGAGED	AGENT RESPONSE
“Find running shoes.”	FindProducts	The agent lists available running shoes from the catalog.
“Do you have wireless headphones?”	FindProducts	The agent returns wireless headphones that match the query.
“Give me details for Galaxy S24.”	GetProductDetails	The agent shows product details for Galaxy S24, such as description and attributes.
“What are the specs for Laptop Pro?”	GetProductDetails	The agent shows detailed information for Laptop Pro.
“What else should I add to this quote?”	GetRuleBasedProductRecommendations	The agent returns products that are recommended by configuration rules for the quote.
“Are there any recommended add-ons?”	GetRuleBasedProductRecommendations	The agent lists recommended products based on configuration rules.
Use Case: Search and Filter Products with Agentforce
Use AI-powered Product Selection in the Revenue Quote Management agent to search your catalog with natural language, filter results by customer criteria, ask clarifying questions about product attributes, and generate a shortlist of products to add to a quote.

=== ARTICLE: ind.rev_agent_pcm_use_case_search_and_filter_products_with_ai_in_the_quoting_agent.htm ===
---
article_id: ind.rev_agent_pcm_use_case_search_and_filter_products_with_ai_in_the_quoting_agent.htm
title: "Use Case: Search and Filter Products with Agentforce"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_pcm_use_case_search_and_filter_products_with_ai_in_the_quoting_agent.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_pcm_topic_product_selection.htm
fetched_at: 2026-09-07
---

# Use Case: Search and Filter Products with Agentforce

Use AI-powered Product Selection in the Revenue Quote Management agent to search your catalog with natural language, filter results by customer criteria, ask clarifying questions about product attributes, and generate a shortlist of products to add to a quote.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license with the Agentforce Employee Agent add-on.

As a sales representative preparing a quote for Cloud Kicks, use AI-powered Product Selection inside the Revenue Quote Management agent to search and filter products, validate details, and create a focused shortlist for quoting.

Before You Begin
Make sure the Revenue Quote Management agent template is available in your org.
Confirm that you have Product Catalog Management Designer permission and agentforce permissions. See Manage Employee Agent Access and Product Catalog Management Designer permissions.
Ensure that product data exists in the catalog.
For best results, enable indexing and semantic search.
Goals
Quickly find relevant products using natural language search.
Filter products by customer-specific criteria.
Ask clarifying questions to validate details.
Create a concise shortlist for quoting.
Search Products

In the Revenue Quote Management agent panel, enter a natural language query such as:

“Find laptops with 16 GB RAM.”
“Show me waterproof running shoes.”

Review the returned product names and descriptions, then select the most relevant matches to continue.

Get Product Details

Narrow results with follow-up queries, such as:

“Only show waterproof models.”
“Exclude red color options.”

Review refined attributes such as memory size, price, color, and warranty.

Ask Follow-Up Questions

Use natural language to validate product specifics before quoting:

“What warranty is included with this laptop?”
“Do these shoes come in size 10?”
IMPORTANT AI answers are based on product catalog data. They don’t provide legal, commercial, or policy advice.
Share the Shortlist

Summarize the top product candidates for quoting and use them to build a new quote or update an existing one.

=== ARTICLE: ind.rev_agent_qocal_topic_quote_management.htm ===
---
article_id: ind.rev_agent_qocal_topic_quote_management.htm
title: "Subagent: Quote Management"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_qocal_topic_quote_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.qocal_agentforce_quote_mgmt.htm
fetched_at: 2026-09-07
---

# Subagent: Quote Management

Create and modify quotes and their quote line items in Revenue Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license with the Agentforce Employee Agent add-on.
Topic Details
API Name	quoteManagement
Included Revenue Actions	

Add Quote Line Item to Quote

Apply Discount To Quote Line Item

Create Amendment Quote

Create Initial Quote

Create Renewal Quote

Get Account Assets

Get Product Selling Model for Products

Query Quote Line Items (Beta)

Update Quote Details

Update Quote Line Item Details


Included Platform Actions	

Get Record Details

Identify Object by Name

Identify Record by Name

Query Records

Summarize Record

Update Record


Required Setup	Set Up Agentforce for Revenue Management
Considerations
The agent is available to authenticated users in Lightning Experience. Customers and partners who use Experience Cloud don’t yet have access to external digital agents.
The agent supports only one currency in quotes. To provide support for multiple currencies, modify the Add QuoteLineItem to Quote flow to check if the Currency ISO Code field is available on the product record. See Set Up Agentforce for Revenue Management.
You can modify up to 10 quote line items at a time in an agent request. For example, you can create a quote with 10 quote line items, add 10 quote line items to an existing quote, or apply a discount on 10 quote line items in a single request.
Examples of Utterances Classified to This Topic
USER SAMPLE INPUT	ACTIONS ENGAGED	AGENT RESPONSE
“Add three units of QuantumBit Gold Platform to the Cloud Kicks Technology quote.”	
Identify Record By Name
Get Product Selling Model for Products
Add Quote Line Item to Quote
	The agent retrieves the default product selling model for QuantumBit Gold Platform and then confirms with the user if it can add the product to the Cloud Kicks Technology quote. After adding the product, the agent shares the link to the updated quote for the user to view or modify manually.
“Apply a discount to API Access so it’s sold at 60% of list price.”	
Identify Record By Name
Query Quote Line Items (Beta)
Apply Discount to Quote Line Item
	The agent calculates the discount percentage or amount for the product to be sold at 60% of list price and then updates the price fields.
“Create an amendment quote for Acme for both Laptop Bag and Mouse starting on 5/12 for -1 unit?”	
Identify Record By Name
Create Amendment Quote
	The agent creates an amendment quote for Acme with the updated product details, reducing their quantity by one and modifying their start date to 5/12.
“Update the quote status under Acme to Accepted.”	
Identify Record By Name
Update Quote Details
	The agent updates the status of the quote associated with Acme to Accepted.
“Sync Acme quote to its opportunity.”	
Get Record Details
Update Record Fields
	The agent syncs the Acme quote to its related opportunity.
“Unsync Acme quote to its opportunity.”	
Get Record Details
Update Record Fields
	The agent stops syncing the Acme quote to its related opportunity.

=== ARTICLE: ind.rev_agent_set_up_community_and_partner_access_for_agentforce_in_revenue_cloud.htm ===
---
article_id: ind.rev_agent_set_up_community_and_partner_access_for_agentforce_in_revenue_cloud.htm
title: Set Up Community and Partner Access for Agentforce in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_set_up_community_and_partner_access_for_agentforce_in_revenue_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-07
---

# Set Up Community and Partner Access for Agentforce in Revenue Management

Make an Agentforce for Revenue agent available to customers or partners by configuring community or partner sites and enabling Embedded Messaging. You can create a community site for the Billing Service Assistance agent and a partner site for the Revenue Quote Management agent.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license with the Agentforce Employee Agent add-on.
USER PERMISSIONS NEEDED
To create Customer and Partner Community users and profiles:	

Manage External Users

Manage Profiles and Permission Sets

Edit on Accounts


To use the Revenue Quote Management agent in the partner site:	

CalculatePrices API

CalculateTaxes API

InitiateAmendment API

InitiateRenewal API

Price and Tax Calculations on Quotes for Partner Community License

ProductAndPriceConfiguration API


To create and customize an Experience Cloud site by using the Self-Service Billing Portal template:	

Billing Admin permission set


To access Experience Cloud site created by using the Self-Service Billing Portal template:	

Billing Experience Cloud User permission set

Before you begin, Set Up Agentforce for Revenue Management.

Prepare Community and Partner Users

Create and configure users who can access the agent in a community or partner site.

Verify that these standard profiles exist:
Customer Community User
Customer Community Plus User
Partner Community User
Clone the required profile to create a custom community or partner profile.
From the App Launcher, open Accounts.
Create a new account or open an existing account.
From the account menu:
OPTION	VALUE
For community users	Enable Customer User
For partner users	Enable As Partner
Open the account’s Contacts related list.
From a contact record:
OPTION	VALUE
For community users	Enable Customer User
For partner users	Enable Partner User
Edit the user record and assign the Customer Community or the Partner Community license.
Select the custom profile and role for the user.
Save your changes.
Grant Community or Partner Users Access to the Site and Agent

Grant site and agent access so community or partner users can interact with the agent from the Experience Cloud site.

In Setup, find and select All Sites.
Open your site workspace.
Click Administration, and then select Members.
Add the custom community or partner profiles.
Save your changes.
Assign the custom Agentforce permission set to your community or partner users.
Configure Embedded Messaging for the Site

With embedded messaging customers and partners can chat with the agent from your Experience Cloud site.

Turn on Messaging.
Set Up Omni Channel
From Setup, find and select Omni-Channel Settings.
Turn on Enable Omni-Channel and then select Enable Skills-Based and Direct-to-Agent Routing.
Configure Routing and Queues

Create a fallback queue so conversations can route to service reps when the agent can’t resolve a request.

Create routing configurations for your queues.
Create your queues.
NOTE This queue acts as a fallback. If the Omni-Channel flow can’t route a conversation to the agent, the conversation is sent to this queue and assigned to a service rep.
In the Routing Configuration field, select the routing configuration you created.
Under Supported Objects, add Messaging Session.
Add supported objects based on the user type:
OPTION	VALUE
For community users:	
Billing Account
Billing Milestone Plan
Billing Schedule Group
Invoice
Messaging User
Messaging Session

For partner users:	
Messaging Session
In the Queue Members section, add your service reps to Selected Users.
Save your changes.
Create an Omni-Channel Flow

Use an Omni-Channel flow to route messages to the agent and send unresolved requests to a fallback queue.

Create an Omni-Channel flow with a Route Work element.
Specify these details:
OPTION	VALUE
Record ID	The recordId variable that you created.
Service Channel	Messaging
Route To	Agentforce <Employee/Service> Agent
Agentforce <employee/service> Agent	<your agent name>
Fallback Queue	The messaging queue that you previously created.
Create and Add an Enhanced Chat Channel

Create an Enhanced Chat channel to connect your Experience Cloud site to Omni-Channel routing and the agent experience.

Create an Enhanced Chat messaging channel.
Add these to your messaging channel:
Your Experience Cloud site domain
The Omni-Channel flow
The messaging queue
Activate the channel.
Add Embedded Messaging to the Site

Enable messaging on your Experience Cloud site so customers or partners can chat with the agent in context.

From Setup, find Digital Experiences, and then select All Sites.
Open your site in Builder.
Drag the Embedded Messaging component to the canvas.
Configure the component and select credential-based user verification.
Publish the site.
After publishing, users can open the chat window and interact with the agent from the site.

If you’re setting up the Billing Service Assistance agent for community users, complete Set Up the Billing Service Assistance Agent for Experience Cloud.

=== ARTICLE: ind.rev_agent_setup.htm ===
---
article_id: ind.rev_agent_setup.htm
title: Set Up Agentforce for Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-07
---

# Set Up Agentforce for Revenue Management

To use the Revenue agent templates, configure the required Revenue and manage agent features and assign permissions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license with the Agentforce Employee Agent add-on.
USER PERMISSIONS NEEDED
To create an agent:	

Manage AI Agents

OR

Customize Application

Before you begin, set up Einstein Generative AI, turn on Agentforce, and set up any required solutions in Revenue Management.

Keep these recommendations in mind while setting up your agent.

To ensure consistency and a better user experience, use the available templates in Revenue Management. Alternatively, you can use the Agentforce Employee Agent template.
To prevent performance issues, avoid including topics belonging to a template into another template.
Create an agent from the available templates.
Revenue Quote Management
Billing Employee Assistance
Billing Service Assistance
Approval Agent
All Agentforce templates available for Revenue are Agentforce Employee Agent templates.
TIP To ensure agents access to external links, you must manually add it to your trusted URLs. Enable messaging to create channels for customer communication.
Review the topics and actions available with your agent template.
If needed, manage other topics and actions for your agent.
If you’re customizing the topics or actions within a template, test your agent.
To grant users access to your agent, create a custom permission set.
If you're tracking the usage of Agentforce actions, turn on audit trails.
Activate your agent.

=== ARTICLE: ind.rev_agent_templates.htm ===
---
article_id: ind.rev_agent_templates.htm
title: Agent Templates in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_templates.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-07
---

# Agent Templates in Revenue Management

Quickly deploy AI-powered agents for your product-to-cash operations using Revenue Management agent templates. All Agentforce templates and topics within Revenue Management are Agentforce Employee Agent (AEA) templates. You must have access to the Revenue solutions to use them.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license with the Agentforce Employee Agent add-on.
AGENT TEMPLATE	TOPICS	ADDITIONAL PERMISSION SETS
Revenue Quote Management	Product Selection	Product Catalog Management Designer
Quote Management	
CalculatePrices API
CalculateTaxes API
InitiateAmendment API
InitiateCancellation API
InitiateRenewal API
Price and Tax Calculation for Quoting (Not for Experience Cloud users)
ProductAndPriceConfiguration API

Consumption Management	
Usage Management Design
Usage Management Runtime
Usage: Design User

Billing Employee Assistance	Invoice Line Breakdown	
Billing Admin

OR

Billing Operations User

AND

Prompt Template User

AND

A permission set with these App Permissions:

Manage Flows
Run Flows
View Flows

Any AEA Template	Product Description Generation	Product Catalog Management Designer
SEE ALSO
Set Up Agentforce for Revenue
Agent Types and Considerations

=== ARTICLE: ind.rev_agent_topic_approval_management.htm ===
---
article_id: ind.rev_agent_topic_approval_management.htm
title: "Subagent: Approval Management"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_topic_approval_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_approval_agent.htm
fetched_at: 2026-09-07
---

# Subagent: Approval Management

Manage approval work items and submissions by summarizing, approving, rejecting, or recalling requests, with optional comments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Subagent Details
API Name	ApprovalManagement
Included actions	

Identify Record by Name

Get Record Details

Review Approval Work Item

Recall Approval Submission

Examples of Utterances Classified to This Topic
USER SAMPLE INPUT	ACTION ENGAGED	AGENT RESPONSE
"Find the approval work item named AWI-000000001."	Identify Record by Name	The agent looks up the approval work item by the provided name and returns the matching record.
"Do we have an approval submission called AS-000000006?"	Identify Record by Name	The agent checks whether an approval submission with that name exists and returns the matching record reference.
"Summarize this approval request."	Get Record Details	The agent resolves the approval work item from the current page context and returns a concise summary of its key fields.
"What's the reviewer and status on AWI-000000008?"	Get Record Details	The agent retrieves the approval work item's details and reports the assigned reviewer and current status.
"Go ahead and approve AWI-000000008."	Review Approval Work Item	The agent confirms the approval decision, asks whether the user wants to add a comment, and submits the approval.
“Reject this work item with the comment 'budget exceeded.'"	Review Approval Work Item	The agent confirms the rejected decision and exact comment text, then submits the rejection.
"I need to withdraw the approval I submitted for this quote."	Recall Approval Submission	The agent finds the approval submission related to the current quote, confirms the recall, asks for an optional comment, and recalls the submission.
"Recall the approval submission for this lead."	Recall Approval Submission	The agent finds the approval submission related to the current lead, confirms the recall, asks for an optional comment, and recalls the submission.

=== ARTICLE: ind.rev_agent_topic_billing_collections_management.htm ===
---
article_id: ind.rev_agent_topic_billing_collections_management.htm
title: "Subagent: Billing Collections Management"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_topic_billing_collections_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.billing_agentforce_billing_agent.htm
fetched_at: 2026-09-07
---

# Subagent: Billing Collections Management

Use Agentforce to help teams quickly assess and act on customer account health. The Billing Collections Management subagent provides an at-a-glance view of financial standing, highlighting high-risk invoices based on payment history, disputes, and outstanding balances, along with recommended next actions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license and the Revenue Cloud Billing license with the Agentforce Employee Agent add-on.
Subagent Details
API Name	BillingCollections
Included actions	

Get Account Billing Summary

Get Dunning Strategy


Required Setup	

Billing Collections

AND

Recovery Specialist

Examples of Utterances Classified to This Topic
USER SAMPLE INPUT	ACTION ENGAGED	AGENT RESPONSE
"What is the billing health summary for the Acme account?"	Get Account Billing Summary	The agent summarizes the outstanding balances, high-risk invoice counts, and historical payment trends.
"Give me a summary for high-risk invoices, late payment history, and open disputes for Acme account"	Get Account Billing Summary	The agent summarizes the account’s high-risk invoice counts, open disputes, and historical payment trends.
"What dunning strategy should I use for collection plan #CP-101?"	Get Dunning Strategy	The agent analyzes the collection plan along with prior customer communications, payment history, and open disputes to recommend the most effective dunning strategy to expedite payment recovery.
"Based on the high-risk score for this account, what is the recommended engagement strategy?"	Get Dunning Strategy	The agent evaluates the risk profile and suggests the most effective dunning orchestration to expedite payment recovery.
SEE ALSO
Manage Collections for Accounts in Billing

=== ARTICLE: ind.rev_agent_topic_billing_inquiries.htm ===
---
article_id: ind.rev_agent_topic_billing_inquiries.htm
title: "Subagent: Billing Inquiries"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_topic_billing_inquiries.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.billing_agentforce_billing_agent.htm
fetched_at: 2026-09-07
---

# Subagent: Billing Inquiries

Use Agentforce to help internal teams quickly access and understand key billing information. The Billing Inquiries subagent answers questions about account balances, payment plans, upcoming payment dates, invoice details, and downloadable invoice documents. Users can ask about an account or a specific invoice, and the agent automatically identifies the right billing flow to run. The subagent consolidates information from Revenue Management Billing so teams can resolve billing questions efficiently and confidently.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license and the Revenue Cloud Billing license with the Agentforce Employee Agent add-on.
Topic Details
API Name	BillingInquiries
Included actions	

Get Account Balance

Retrieve Next Due Payment

Generate Payment Plan Details

Get Invoice Document PDF


Required Setup	Set Up Agentforce for Revenue Management
Examples of Utterances Classified to This Topic
USER SAMPLE INPUT	ACTIONS ENGAGED	AGENT RESPONSE
“How much do I currently owe?”	Get Account Balance	The agent summarizes the net amount due across outstanding invoices, including debit memos, credit memos, payments, and refunds.
“Can you tell me the current account balance for my account?”	Get Account Balance	The agent retrieves posted invoices, credits, debits, payments, and refunds to summarize the outstanding balance for the requested account.
“When is my next payment due?”	Retrieve Next Due Payment	The agent identifies the earliest upcoming due date and the due amount for one or more invoices.
“What is the next payment for account ABC Corp?”	Retrieve Next Due Payment	The agent returns the next due amount and date for that account.
“Can you get me the payment plan for my invoice?”	Generate Payment Plan Details	The agent returns payment installment amounts, dates, and statuses for the specified invoice.
“Get the payment plan for invoice DOC-12345.”	Generate Payment Plan Details	The agent reads the invoice details and returns the full payment schedule.
“Can you show me my latest bill?”	Get Invoice Document PDF	The agent retrieves the most recent posted invoice and provides a downloadable PDF link.
“Download the latest invoice for this account.”	Get Invoice Document PDF	The agent fetches the latest invoice and provides the file link in Markdown format.

=== ARTICLE: ind.rev_agent_topic_reference.htm ===
---
article_id: ind.rev_agent_topic_reference.htm
title: Revenue Subagent Reference
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_topic_reference.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-07
---

# Revenue Subagent Reference

To optimize common revenue use cases, explore the standard agent topics available in Revenue Management. While these agent topics aren't included with a Revenue agent template, you can add them to any Agentforce Employee Agent template.

Subagent: Product Description Generation
Generate and refine product descriptions and update records with new product descriptions.

=== ARTICLE: ind.rev_agent_topic_search_approval_records.htm ===
---
article_id: ind.rev_agent_topic_search_approval_records.htm
title: "Subagent: Search Approval Record"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_topic_search_approval_records.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_approval_agent.htm
fetched_at: 2026-09-07
---

# Subagent: Search Approval Record

Filter and list approval work item or approval submission records based on related record type, date ranges, status, and assignee context.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Subagent Details
API Name	SearchApprovalRecords
Included actions	

Query Records

Examples of Utterances Classified to This Topic
What approval work items are pending my review?
Show me all approval records for this record.
List approval submissions related to this opportunity.
Show approved approval submissions from the last 30 days.

=== ARTICLE: ind.rev_agent_topic_summarize_multiple_approval_work_items.htm ===
---
article_id: ind.rev_agent_topic_summarize_multiple_approval_work_items.htm
title: "Subagent: Summarize Multiple Approval Work Items"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_topic_summarize_multiple_approval_work_items.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.rev_agent_approval_agent.htm
fetched_at: 2026-09-07
---

# Subagent: Summarize Multiple Approval Work Items

Filter approval work item records and summarize them in aggregate, providing per-record details so reviewers can quickly understand the context of each approval.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Subagent Details
API Name	SummarizeMultipleApprovalWorkItems
Included actions	

Query Records

Get Record Details

Examples of Utterances Classified to This Topic
USER SAMPLE INPUT	ACTION ENGAGED	AGENT RESPONSE
"Summarize my most recent Approval Work Item and tell me what I need to look at."	Query Records	The agent searches for the latest approval work item assigned to the user, fetches its record details, and generates a summary highlighting key fields and items requiring attention.
"Summarize the 10 most recent approval work items of the contracts."	Query Records	The agent searches for the 10 most recent approval work items linked to the records and provides a summarized breakdown of their statuses and key details.
"Summarize the most recent 10 approval work items on this record."	Get Record Details	The agent searches for approval work items associated with the record, retrieves the 10 latest entries, and presents a summarized list of their current progress.
"Summarize the 10 most recent approval work items assigned to me."	Get Record Details	The agent queries approval work items filtered by the current user's ID as the assignee, orders them by date, and generates a summary of the 10 most recent items.

=== ARTICLE: ind.rev_agent_usage_topic_consumption_management.htm ===
---
article_id: ind.rev_agent_usage_topic_consumption_management.htm
title: "Subagent: Consumption Management"
source_url: https://help.salesforce.com/s/articleView?id=ind.rev_agent_usage_topic_consumption_management.htm&type=5&release=264
release: 264
release_name: Winter '27
area: agents
parent_article: ind.qocal_agentforce_quote_mgmt.htm
fetched_at: 2026-09-07
---

# Subagent: Consumption Management

Get consumption details of accounts with resource overages and generate quotes for the resources with overages.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license and the Revenue Cloud Billing license with the Agentforce Employee Agent add-on.
Topic Details
API Name	ConsumptionManagement
Included Consumption Management Action	

Get Usage Details


Required Setup	Set Up Agentforce for Revenue
Considerations for Consumption Management
To access the Consumption Management topic within the Revenue Quote Management template, turn on Rate Management and Usage Management.
Make sure that the Wallet Management User and Usage Runtime user personas have the same object permissions as Traceability.
The agent is available to authenticated users in Lightning Experience. Customers and partners who use Experience Cloud don’t yet have access to external digital agents.
Examples of Utterances That Trigger This Topic
"I would like to get account usage details for Acme and Cloud Kicks."
"What is the current consumption on my account?"
“How many assets from Acme are with overages?”

