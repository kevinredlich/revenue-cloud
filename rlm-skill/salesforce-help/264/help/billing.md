# Salesforce Help 264 — área: billing (265 artículos)

=== ARTICLE: ind.billing.htm ===
---
article_id: ind.billing.htm
title: Manage Billing in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
fetched_at: 2026-09-04
---

# Manage Billing in Revenue Management

Monetize all the sales models of your business with Billing. Generate invoices for diverse scenarios, such as customer milestones, product usage, amendments, cancellations, or early renewal of evergreen subscriptions. Bill in advance or in arrears, or bill for external transactions. Consolidate invoices with custom grouping, automate and scale invoice generation, and suspend or resume billing for specific accounts or billing schedule groups as needed.

Process payments for invoices, issue refunds, and track payments for unpaid invoices. Collect payment promises from customers and write off unpaid or partially paid invoices if the balance is deemed uncollectible. Automate the conversion of negative invoice lines to credit memos and the application of credits to invoices. Preview upcoming invoices and create PDFs for previews and actual invoices by using customized templates.

Configure multiple legal entities, tax engines, and billing profiles to support your business operations and customer requirements. Keep business records accurate and improve financial reporting by using accounting periods and a chart of accounts for legal entities, automating journal entries, and managing multi-currency transactions. Get real-time visibility into invoices, credit memos, and billing schedules.

Set Up Billing
Enable Billing, assign the required permission sets, and set up features.
Set Up Additional Billing Features
Beyond the core functionality, you can set up and configure various additional Billing features to extend its capabilities. This allows you to tailor Billing to your specific business requirements.
Considerations When Setting Up and Using Billing
Before you set up and use Billing, keep these considerations in mind.
Define Billing Policies and Billability Rules
Define billing policies, treatments, and treatment items to generate invoices that suit your sales models. Specify product billability rule criteria to define whether you want to bill your products in advance or in arrears, whether specific products are billed, and other conditions.
Create Payment Terms
Negotiate and define payment terms to set a due date for payments and collect payments in a timely manner. You can anticipate or enforce the date by when payments for outstanding invoices must be paid.
Manage Billing Arrangements
Billing arrangements facilitate precise invoicing for business scenarios such as parent account billed for subsidiary accounts, cross-departmental charge allocations, or services or assets shared among multiple parties. Use billing arrangements to configure the allocation of billing amounts to a specific billing account or distribute costs among several billing accounts based on fixed percentages.
Configure Milestone Billing
Bill projects in installments based on milestone achievements or predefined dates. Align payments with project progress and enhance customer satisfaction through timely invoicing.
Tax Calculation for Invoices
Configure how taxes are calculated on the billing amounts of your taxable products or services, or import tax amounts calculated by an external system.
Create Billing Profiles
Cater to your customers' billing preferences and business needs by creating billing profiles for their accounts. Define multiple billing profiles for an account to manage diverse billing needs, each with its own billing details, payment terms, and contacts. Set a default billing profile for accounts to easily access your customers' preferred billing day of the month, billing address, billing contact, and other details. With billing profiles, sales representatives no longer need to enter this information for each transaction, saving time and effort.
Manage Financial Accounting in Revenue Management
Streamline the financial accounting process for your organization with accounting periods for legal entities, chart of accounts, journal entries for your billing transactions, and by capturing transaction amounts in corporate currency.
Preview Invoices
Preview invoices for the next two billing periods of orders, quotes, accounts, or billing schedule groups to verify order products, discounts, amendments, cancellations, and tax calculations.
Manage Billing Schedules and Billing Schedule Groups
Billing schedules define when and how an order product is invoiced. Billing schedule groups contain one or more billing schedules. Both of these are created and updated as a result of creating, amending, and canceling orders. You can generate billing schedules directly from transactions in external systems, or from any Salesforce object by using Create Standalone Billing Schedules API. To generate billing schedules from orders, use the Order to Billing Schedule flow, Create Billing Schedules for Orders API, or Create Standalone Billing Schedules API.
Suspend and Resume Billing
Pause invoicing temporarily for an account or billing schedule group without canceling its billing schedules. Suspensions defer charges, they don’t waive them.
Billing Forecast
Billing Forecast estimates upcoming invoice charges before invoices are created. Review projected charges to understand expected billing and discuss estimates with customers.
Generate Invoices in Revenue Management
Schedule invoice runs to generate invoices from billing schedules or generate invoices directly from accounts or orders. Create standalone invoices or import invoices from an external system.
Invoice Risk Score (Pilot)
Invoice Risk Scoring uses invoice data and predictive AI to estimate the likelihood that payment for an open invoice will be delayed beyond its due date. Learn how risk scores and risk levels are displayed on invoice records to help identify potential payment risks.
Generate Invoice PDF Documents
After invoices are generated, generate PDF documents for a batch of invoices or a single invoice.
Send Invoices Through Email
Ensure regional compliance by sending invoices through emails to your customers after the invoices are posted and before the payment due date. Customize your preferences at various levels in your Salesforce org to choose the way emails are delivered to your customers.
Manage Credit Memos in Revenue Management
Create and apply credit memos to decrease the balance of invoices when the quantity or price of orders are amended.
Configure Sequential Numbering for Invoices and Credit Memos
Use a sequence policy to configure automated sequential numbering for your invoices and credit memos. Generate unique, gapless numbers to create fully traceable records for financial audits.
Manage Debit Memos in Revenue Management
Create debit memos when you undercharge your customer or want to add additional charges. When debit memo lines are converted to invoice lines, the balance of the related invoices increases.
Process Payments and Issue Refunds in Revenue Management
Complete your cash journey by making payments for posted invoices and issuing refunds when needed. Settle open invoice balances in a timely manner and accurately report cash flow by collecting and applying payments. Refund your customers if they change or cancel products or services that they paid for.
Manage Collections for Accounts in Billing
To recover overdue invoices, your collections reps use Collections workflow to track payments, record customer payment promises, and send personalized, automated dunning emails to minimize bad debt and maintain healthy cash flow.
Write Off Invoices
Write off unpaid or partially paid invoices when the balance on the invoice is deemed uncollectible. To maintain accurate accounting, the system automatically creates and applies credit memos to write off the uncollectible balance on the invoice.
Manage Billing Disputes
Fragmented billing dispute processes often lead to payment delays and poor customer experience. By using the dispute management feature, you can streamline the intake and resolution process for common billing requests and disputes. Install pre-built service process templates by using Unified Catalog. Your billing specialists and customer service representatives can initiate cases directly from the Account record page, and quickly capture, validate, and resolve common inquiries, all from a single catalog. Billing portal users can raise service requests through the self-service Billing portal.
Billing Account Overview
View and manage customer billing information from a single page. Track billing transactions, generate and preview invoices, suspend and resume billing, create credit memos, and resolve billing inquiries. Get a complete view of the customer's billing status by accessing key billing actions, account details, and related account records.
Statement of Account
Account statements consolidate billing activity for accounts over a time period so customers see transactions and outstanding balances in one statement.
Billing Settlements Central
Access invoices, payments, credit memos, and debit memos with ease from a single console. Perform settlements and adjustments, track balances, and act from a single console. Reduce navigation, gain visibility into outstanding balances, and support efficient billing through in-context actions and customizable views.
Billing Operations Console
Monitor invoices, credit memos, and invoice schedules with ease. Manage billing transactions effectively with timely insights into revenue transaction log errors and failed invoices.
Limits in Billing
Review the default limits for Billing features.

=== ARTICLE: ind.billing_account_document_template.htm ===
---
article_id: ind.billing_account_document_template.htm
title: Assign an Invoice Document Template to a Billing Profile
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_account_document_template.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_document_generation_batch_and_single.htm
fetched_at: 2026-09-04
---

# Assign an Invoice Document Template to a Billing Profile

Configure a custom invoice document template to use for account-specific invoice document generation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create and assign an invoice document template:	

Billing Admin permission set OR Billing Operations User permission set

AND

DocGen User permission set

AND

DocGen Designer permission set

To assign account-specific templates for invoice PDF documents, make sure your Billing admin turns on Document Generation for Billing.

From the App Launcher, find and select Billing Accounts.
Open the billing account.
Select the invoice template to use for the account.
Save your changes.

=== ARTICLE: ind.billing_account_overview.htm ===
---
article_id: ind.billing_account_overview.htm
title: Billing Account Overview
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_account_overview.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Billing Account Overview

View and manage customer billing information from a single page. Track billing transactions, generate and preview invoices, suspend and resume billing, create credit memos, and resolve billing inquiries. Get a complete view of the customer's billing status by accessing key billing actions, account details, and related account records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
NOTE

You can view the Account Summary and Unpaid Bills section by installing Billing Analytics and Timeline.

If you've started using Billing from Summer ’25 or a later release, turn on Timeline and then turn on Billing.
If you were already using Billing before Summer ’25, turn off Billing, turn on Timeline, and then turn on Billing again.

From the App Launcher, find and select Billing. From the navigation bar, click Account. Open any Account record to view all the required details.

Account Details and Summary

Gain valuable insights about a customer account from these sections.

Customer Details: View and edit customer information such as account name, account owner, and billing address.
Unpaid Bills: View the account’s invoice status and prioritize collections by using aging analytics information.
Account Summary: View the account's net pending balance with totals for invoices, overdue amounts, and overall balance.
Account Billing History and Overview

Manage billing account interactions and account's related records with these details.

Timeline: Shows a sequential view of billing transactions and engagement activities related to the account. Filter the timeline to view account activity based on date range and event type.
Tabs: The various tabs show the account's billing details and related records. Access billing profiles, invoices, payments, credit memos, and all records associated with the customer's account in just a few clicks.
Quick Actions

Generate invoices, suspend and resume billing, create credit memos, and preview invoices from the account’s customer details section. From the billing profile section, create billing profiles.

You can view and create tasks, emails, and events, and log a call. Filter activities by date range, sort them by newest or oldest, and choose to show all activities or only the billing-related ones.

NOTE To perform the quick actions, you must have certain permission sets.
SEE ALSO
Create and Apply Credit Memos to Invoice Lines

=== ARTICLE: ind.billing_account_specific_invoice_template_configure.htm ===
---
article_id: ind.billing_account_specific_invoice_template_configure.htm
title: Generate Invoice PDF Documents Specific to Billing Profiles
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_account_specific_invoice_template_configure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_document_generation_batch_and_single.htm
fetched_at: 2026-09-04
---

# Generate Invoice PDF Documents Specific to Billing Profiles

Generate a PDF document for an invoice directly from the invoice record. Provide billing profile specific individual invoice documents without waiting for invoice batch runs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create and generate invoice PDF documents:	

Billing Admin permission set OR Billing Operations User permission set

AND

DocGen User permission set

AND

DocGen Designer permission set

AND

DocGen Runtime Community User

NOTE

Before generating invoice PDF documents, review the default limits for document generation requests and the process for increasing the maximum number of content versions that are published per day.

NOTE If you can’t access DocGen records, add yourself to the DocGen Document Template Library and make sure you have one of the required permissions.
From the App Launcher, find and select Invoices.
Open a draft or posted invoice for which you want to generate a document.
Click Generate Invoice Document.
You can preview the invoice document in the Generate Invoice Document window. If necessary, download a local copy of the invoice document. You can also regenerate the invoice document as needed.

Billing selects the appropriate invoice template based on these resolution order:

If the invoice has a billing profile with an invoice document template, Billing uses that template.
If the invoice’s billing profile has no invoice document template, Billing uses the default template from the billing account’s billing profile.
If neither is available, Billing uses the default invoice document template defined for the Salesforce org.

=== ARTICLE: ind.billing_account_statement.htm ===
---
article_id: ind.billing_account_statement.htm
title: Statement of Account
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_account_statement.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Statement of Account

Account statements consolidate billing activity for accounts over a time period so customers see transactions and outstanding balances in one statement.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

Use account statements to give customers a complete overview of their transactions and what they owe. You can generate a statement from an account record, review how amounts appear on the PDF, or integrate generation by using APIs and flows.

Generate an Account Statement
Use the Generate Account Statement quick action on an account to produce a PDF statement without leaving the page.
Generate Account Statements by Using APIs
Use the Generate Account Statement REST API to integrate Statement of Account PDF generation with external systems, custom apps, and automated jobs.
Generated Statement Details
The generated account statement PDF groups billing data into an account summary, transaction history, and balance due. The statement period filters transaction history, while summary and balance due reflect balances as of generation time.

=== ARTICLE: ind.billing_account_statement_api.htm ===
---
article_id: ind.billing_account_statement_api.htm
title: Generate Account Statements by Using APIs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_account_statement_api.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_account_statement.htm
fetched_at: 2026-09-04
---

# Generate Account Statements by Using APIs

Use the Generate Account Statement REST API to integrate Statement of Account PDF generation with external systems, custom apps, and automated jobs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

Each request generates a Statement of Account PDF for a primary account and any related accounts included. The statement consolidates billing activity and reflects the current outstanding balance, with amounts converted to the primary account’s currency when multiple currencies are involved. For resource paths, request fields, response handling, and asynchronous processing details, see Generate Account Statement API.

SEE ALSO
Account Statements
Generate an Account Statement
Generated Statement Details

=== ARTICLE: ind.billing_account_statement_generate.htm ===
---
article_id: ind.billing_account_statement_generate.htm
title: Generate an Account Statement
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_account_statement_generate.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_account_statement.htm
fetched_at: 2026-09-04
---

# Generate an Account Statement

Use the Generate Account Statement quick action on an account to produce a PDF statement without leaving the page.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To generate statement of account:	

Billing Admin permission set

Or

Billing Operations User permission set

NOTE Before you generate account statements, turn on Document Generation from Billing Settings.

Account statements use a document template to define the layout of the generated PDF. You can select a custom template created by using Document Generation. If you don’t select a template, the system uses the template defined on the billing profile or the org default template.

From the App Launcher, find and select Accounts.
Open the account record that you want to generate the statement for.
Click Generate Account Statement.
Verify the primary account that you’re generating the statement for.
Select the related accounts to include in the statement.
Select the billing transactions to include by transaction type.
By default, all invoices, credit memos, debit memos, payments, and refunds are selected.
Select a document template.
Select the start date.
The statement reflects the current outstanding balance and can’t calculate the balance for a past end date. Therefore, the end date defaults to today and can’t be changed.
Select how to sort the transactions, and select the sorting order.
Generate the statement.

The system generates the statement asynchronously. When processing completes, the PDF is saved in the Files related list on the account.

=== ARTICLE: ind.billing_account_statement_pdf_details.htm ===
---
article_id: ind.billing_account_statement_pdf_details.htm
title: Generated Statement Details
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_account_statement_pdf_details.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_account_statement.htm
fetched_at: 2026-09-04
---

# Generated Statement Details

The generated account statement PDF groups billing data into an account summary, transaction history, and balance due. The statement period filters transaction history, while summary and balance due reflect balances as of generation time.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Account Summary

The account summary shows the primary account’s current financial position, calculated as of the statement generation date. It includes all transactions regardless of the selected statement period, and amounts appear in the primary account currency.

Transaction History

The transaction history lists billing transactions for the selected accounts within the statement period. It includes only posted transactions with transaction dates that fall within the defined date range. Transactions must belong to the selected accounts and match the selected transaction types. The section includes invoices, credit memos, debit memos, payments, and refunds, grouped by account. Amounts are in their original currency.

Balance Due

The balance due section shows the total outstanding balance for the primary account as of the statement generation date.

Key Behaviors and Considerations

The statement period determines which transactions appear in transaction history. The account summary and balance due reflect the current balance as of the statement generation date, not a historical balance as of the statement end date. The system includes only posted transactions.

=== ARTICLE: ind.billing_accounting_periods.htm ===
---
article_id: ind.billing_accounting_periods.htm
title: Manage Accounting Periods in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_accounting_periods.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_financial_accounting.htm
fetched_at: 2026-09-04
---

# Manage Accounting Periods in Revenue Management

Accounting periods help your company organize and monitor financial performance by defining specific time frames for business reports. Ensure accurate financial reporting and streamlined record-keeping by associating billing transactions to legal entity accounting periods.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
What are Accounting Periods?
An accounting period is a specific time frame for which a company prepares its financial statements. For example, a month, quarter, or an year. It's a fundamental concept in accounting, as it dictates how and when revenue and expenses are recognized. Define start and end dates on the accounting periods to prevent overlaps or gaps and maintain a clean financial record for auditing purposes.
Create Accounting Periods
Create accounting periods to organize and store financial information for specific time frames. For example, if your company tracks performance quarterly, define quarterly accounting periods.
Assign Legal Entities to Accounting Periods
Assign legal entities to accounting periods, and associate each billing transaction to a specific accounting period of a legal entity.

=== ARTICLE: ind.billing_accounting_periods_close.htm ===
---
article_id: ind.billing_accounting_periods_close.htm
title: Close an Accounting Period
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_accounting_periods_close.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entity_accounting_periods_close_and_reopen.htm
fetched_at: 2026-09-04
---

# Close an Accounting Period

Close an accounting period after its duration ends and after all journal entries are validated for financial reporting of that period.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To close accounting periods:	Accounts Receivables Admin permission set

Before closing an accounting period, ensure there are no related open legal entity accounting periods. If there are related legal entity accounting periods that are open, an error message appears and the accounting period remains open.

Open the record of the accounting period that you want to close.
Click Close Accounting Period and confirm that you want to close it.

When there aren't any related open legal entity accounting periods, the accounting period's status is set to Closed.

When you close an accounting period, several key metrics are updated. The Total Asset Amount, Total Liabilities Amount, Total Equities Amount, Total Revenue Amount, and Total Expenses Amount fields are recalculated. These amounts are calculated by aggregating the corresponding field values from all associated legal entity accounting periods and are shown in corporate currency configured for your Salesforce org.

=== ARTICLE: ind.billing_accounting_periods_create.htm ===
---
article_id: ind.billing_accounting_periods_create.htm
title: Create Accounting Periods
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_accounting_periods_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_accounting_periods.htm
fetched_at: 2026-09-04
---

# Create Accounting Periods

Create accounting periods to organize and store financial information for specific time frames. For example, if your company tracks performance quarterly, define quarterly accounting periods.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create accounting periods:	Accounts Receivables Admin permission set

Accounting periods can be created for a month for internal reporting, and consolidated for a quarter, a half-year, or a year for external reporting.

From the App Launcher, find and select Accounting Periods.
Click New.
Specify a start date and an end date for the accounting period.
You can't create accounting periods that are longer than a year, or with start and end dates of an existing accounting period.
Specify the financial period in which the accounting period falls.
For example, if the accounting period is for the fiscal year of 2027, enter FY 2027.
Select Open as the Status.
When you create accounting periods, the status can only be set to Open.
Save your work.

The name of the accounting period is automatically generated, combining the specified financial year, start date, and end date.

NOTE You can't edit or delete accounting periods that have related legal entity accounting periods.

=== ARTICLE: ind.billing_accounting_periods_explain.htm ===
---
article_id: ind.billing_accounting_periods_explain.htm
title: What are Accounting Periods?
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_accounting_periods_explain.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_accounting_periods.htm
fetched_at: 2026-09-04
---

# What are Accounting Periods?

An accounting period is a specific time frame for which a company prepares its financial statements. For example, a month, quarter, or an year. It's a fundamental concept in accounting, as it dictates how and when revenue and expenses are recognized. Define start and end dates on the accounting periods to prevent overlaps or gaps and maintain a clean financial record for auditing purposes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
What are Legal Entity Accounting Periods?

While accounting periods define the overall timeframes, legal entity accounting periods represent the accounting period a legal entity uses for accounting.

Granular Reporting: Enables precise financial reporting tailored to the unique operational and legal requirements of each individual legal entity within your organization.
Transaction Assignment: Ensures that every billing transaction is directly tied to a specific legal entity and its corresponding legal entity accounting period. This ensures that a transaction initiated by a legal entity is recorded against that specific entity's books for a specific period.
Example: Streamlining Financial Closes for a Global Company

Imagine Innovate Solutions Corp., a global SaaS company with US, EU, and APAC legal entities, which struggled with manual financial closes, processing thousands of monthly billing transactions like invoices and payments. This led to extended monthly closes and audit challenges.

By using Revenue Management's accounting period features, Innovate Solutions creates required records to automate their process:

Creating Accounting Periods: Innovate Solutions defines monthly, quarterly, and annual accounting periods to align with internal and external reporting cycles. For example, they create an Accounting Period for Q1 2027 with the start date as January 1, 2027, the end date as March 31, 2027, and the financial period as FY 2027.
Assigning Legal Entities to Accounting Periods: They assign specific legal entity to an accounting period for each subsidiary. For example, a Legal Entity Accounting Period record is created for Innovate Solutions EU - Jan 2027 linking to the Innovate Solutions EU legal entity and the Jan 2027 accounting period.
Automated Transaction Association: As new invoices, credit memos, and payments are processed, the system automatically assigned them to the correct legal entity accounting period based on the transaction's legal entity and effective date.

At the end of each month, Innovate Solutions Corp finalize and close their accounting records. See Example: Streamlining Accounting Period Closure.

SEE ALSO
Legal Entity Accounting Periods Closure and Reopening

=== ARTICLE: ind.billing_agentforce_billing_agent.htm ===
---
article_id: ind.billing_agentforce_billing_agent.htm
title: Agentforce for Billing Employee Assistance
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_agentforce_billing_agent.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-04
---

# Agentforce for Billing Employee Assistance

When internal finance or billing teams need clarity on billing data for customer accounts, Billing Employee Assistance gives them a conversational way to understand charges and retrieve billing information. Employees can ask questions about invoice charge explanations, payment plans, outstanding account balances, or upcoming payment due dates. They get clear explanations powered by generative AI, without navigating multiple billing records or systems.

REQUIRED EDITIONS

Billing Employee Assistance is designed for internal users, such as:

Finance or Billing operations teams who frequently track payments and monitor outstanding invoices for customer accounts.
Customer service teams who handle inquiries that require fast and accurate billing information.
Collections specialists who need immediate insight into outstanding invoices or upcoming payments.

Use Billing Employee Assistance to:

Accelerate internal inquiry handling by giving teams direct conversational access to billing data.
Reduce context switching by viewing invoices, payments, and balances in one place.
Improve billing clarity and transparency through consistent explanations of line items and charges.
Enhance operational efficiency by eliminating manual record navigation and repetitive lookup steps.

Billing Employee Assistance runs inside your Salesforce org and uses your existing Agentforce Revenue Management Billing data to answer billing questions. When an internal user needs information, such as an explanation for a specific invoice line, the customer’s outstanding balance, or the next payment due, they can open Agentforce and ask a question in natural language.

The agent uses generative AI with real-time billing data retrieved through supported flows to return concise, plain language explanations. It can summarize invoice charges, list payment plan details, generate or retrieve invoice documents, and surface key account information to help employees resolve questions quickly and accurately.

Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Billing license with the Agentforce Employee Agent add-on.

To review the billing considerations for Billing Employee Assistance, see Considerations for Agentforce in Revenue Management.

Set Up Billing Employee Assistance
To use additional Billing features, turn on the required features and assign permissions.
Subagent: Invoice Line Explanation
Help users understand their invoice lines by providing detailed explanations of each charge, including the reasons and calculation methods.
Subagent: Billing Collections Management
Use Agentforce to help teams quickly assess and act on customer account health. The Billing Collections Management subagent provides an at-a-glance view of financial standing, highlighting high-risk invoices based on payment history, disputes, and outstanding balances, along with recommended next actions.
Subagent: Billing Inquiries
Use Agentforce to help internal teams quickly access and understand key billing information. The Billing Inquiries subagent answers questions about account balances, payment plans, upcoming payment dates, invoice details, and downloadable invoice documents. Users can ask about an account or a specific invoice, and the agent automatically identifies the right billing flow to run. The subagent consolidates information from Revenue Management Billing so teams can resolve billing questions efficiently and confidently.

=== ARTICLE: ind.billing_agentforce_billing_agent_setup.htm ===
---
article_id: ind.billing_agentforce_billing_agent_setup.htm
title: Set Up Billing Employee Assistance
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_agentforce_billing_agent_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_agentforce_billing_agent.htm
fetched_at: 2026-09-04
---

# Set Up Billing Employee Assistance

To use additional Billing features, turn on the required features and assign permissions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license and the Revenue Cloud Billing license with the Agentforce Employee Agent add-on.
USER PERMISSIONS NEEDED
To create an agent:	

Manage AI Agents

OR

Customize Application

Set Up Agentforce for Revenue Management.
Verify that Usage Management is turned on in the org before you use Billing Employee Assistance.
Create a permission set that includes the Prompt Template User permission and these app permissions for flow and flow orchestration: Manage Flow, Run Flows, and View Flows.
Assign this permission set to the appropriate standard user with a Billing Admin or Billing Operations User permission.

=== ARTICLE: ind.billing_agentforce_billingagent_usecase.htm ===
---
article_id: ind.billing_agentforce_billingagent_usecase.htm
title: Billing Employee Assistance Use Case
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_agentforce_billingagent_usecase.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.rev_agent_billing_topic_invoice_line_explanation.htm
fetched_at: 2026-09-04
---

# Billing Employee Assistance Use Case

At Acme, the billing team spent hours digging through orders, amendments, and cancellations whenever a customer questioned an invoice. Each case meant switching between systems, piecing together the story of a charge, and explaining it to the customer. This process often delayed resolutions and sometimes left customers frustrated.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license and the Revenue Cloud Billing license with the Agentforce Employee Agent add-on.

Things changed when Acme introduced Billing Employee Assistance. Suddenly, the admin no longer had to chase data across records. The agent became the single place to ask questions and uncover the reasoning behind any charge.

When a customer received an invoice for 10 monitors instead of 6, the admin simply asked Billing Employee Assistance to explain the one-time charge. Within moments, the agent showed that the original order was for 6 units, an amendment had added 4 more, and taxes had been applied. Instead of a back-and-forth investigation, the admin had a clear explanation ready to share.

In another case, a subscription customer was unsure about a Slack charge. The agent retraced the full sequence. It even highlighted how proration and adjustments were calculated. What might have taken hours of manual review was now presented as a straightforward story the customer could understand.

Milestone-based work has created its own challenges. When a customer questioned why professional services were invoiced even though the project wasn’t complete, Billing Employee Assistance revealed which milestones had already been billed, the corresponding amounts, and the milestones remaining.

Even usage-based billing, often the trickiest to explain, became easier. A customer once disputed an API overage charge of $5,370. With a single query, the agent displayed the granted quantities, actual consumption, and how tiered rates applied.

For Acme, the shift was clear. What used to be hours of detective work turned into confident, timely explanations. Customers received quick, transparent answers, disputes dropped, and trust grew stronger. Billing Employee Assistance didn’t just save time, it gave both admins and customers clarity they could rely on.

=== ARTICLE: ind.billing_agentforce_for_billing_service_assistance_agent.htm ===
---
article_id: ind.billing_agentforce_for_billing_service_assistance_agent.htm
title: Agentforce for Billing Service Assistance Agent
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_agentforce_for_billing_service_assistance_agent.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.rev_agent_overview.htm
fetched_at: 2026-09-04
---

# Agentforce for Billing Service Assistance Agent

Use Billing Service Assistance Agent to give customers fast, conversational explanations for invoice charges directly in your Experience Cloud billing portal.

If customers are confused by charges on their invoices, Billing Service Assistance Agent helps them get clear explanations without opening a support case. Customers stay on the invoice page, ask questions about specific invoice lines, and receive generative AI–powered explanations in real time.

Billing Service Assistance Agent is for external community users who use your billing portal to review and manage their own invoices. These users include:

Individual customers who sign in to view, download, or pay invoices.
Business or partner contacts who access billing information for their account through the portal.

Use Billing Service Assistance Agent to:

Deflect billing-related support cases by resolving common charge explanation questions directly from the self-service portal.
Improve customer clarity by providing plain-language explanations for technical or confusing invoice charges.
Offer a consistent self-service experience where customers get help without leaving the invoice page.

Billing Service Assistance Agent runs in your Experience Cloud billing portal and uses existing billing data to explain invoice charges. When a signed-in customer views an invoice, they open Embedded Messaging and ask a question such as “Explain this Slack subscription fee.” The agent uses generative AI with Revenue Management Billing data to return a short, plain-language explanation in the chat window.

Set Up Billing Service Assistance Agent for Experience Cloud
Configure service access, security, and data sharing so that external users can securely interact with Billing Service Assistance Agent through Embedded Messaging in an Experience Cloud site.

=== ARTICLE: ind.billing_automate_invoice_generation.htm ===
---
article_id: ind.billing_automate_invoice_generation.htm
title: Automated Invoice Generation with Invoice Batch Runs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_automate_invoice_generation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Automated Invoice Generation with Invoice Batch Runs

Schedule invoice batch runs to automate invoice generation. These runs use Data Processing Engine to generate invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Understand Invoice Date, Target Date, and Billing Period Count
Before you schedule invoice batch runs, learn how invoice dates are determined, how billing schedules are selected, and how many billing periods are processed for each schedule. You can also process a specific number of billing periods without relying on a target date.
Catch-Up Bill Runs
Use a catch-up bill run to advance the next billing date, billed amount, and pending amount on billing schedules for transactions that a legacy system fully or partially billed. Catch-up doesn’t create invoices for those periods.
Generate Invoices Automatically Based on Billing Schedules
Set up invoice schedulers to generate invoices on a schedule or on demand. Select billing schedules by target date, billing period count, or both. Generate invoice documents during the run, or use a catch-up bill run to advance migrated schedules without creating invoices.
Convert Automations to Asynchronous for Invoice Batch Runs
Identify active flows and Apex triggers on Billing objects and convert them to asynchronous processes before you schedule an invoice batch run. Synchronous automations can stop a run or leave invoices in Draft In Progress, Posting In Progress, or Error.
Examples: Invoice Batch Run Frequencies
Explore examples to understand how to schedule invoice batch runs based on your requirements.
Invoice Batch Run Process
Invoice batch runs stream invoices by processing billing schedules in parallel. Track each stage of the invoice batch run to monitor progress and status.

=== ARTICLE: ind.billing_automate_invoice_run_schedules.htm ===
---
article_id: ind.billing_automate_invoice_run_schedules.htm
title: Generate Invoices Automatically Based on Billing Schedules
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_automate_invoice_run_schedules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_automate_invoice_generation.htm
fetched_at: 2026-09-04
---

# Generate Invoices Automatically Based on Billing Schedules

Set up invoice schedulers to generate invoices on a schedule or on demand. Select billing schedules by target date, billing period count, or both. Generate invoice documents during the run, or use a catch-up bill run to advance migrated schedules without creating invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


This feature is available with the Revenue Management Advanced license or the Revenue Management Billing license.

The Milestone Billing and Usage-Based Invoicing features are available only with the Revenue Management Billing license. Contact your Salesforce account executive for more information.

USER PERMISSIONS
NEEDED
To create invoice schedulers:	

Billing Admin permission set

OR

Billing Operations User permission set


To generate invoice documents during a batch run:	

Billing Admin permission set OR Billing Operations User permission set

AND

DocGen User permission set

From the App Launcher, find and select Billing Batch Schedulers.
Click New Invoice Scheduler.
Enter a scheduler name.
To advance migrated billing schedules without generating invoices, select Catch-Up Bill Run.
Catch-up bill runs use the Once frequency and require a target date. Because catch-up doesn't generate invoices, the scheduler disables the invoice generation options, such as post invoices, create invoice documents, invoice date, and recurrence. For when to use a catch-up bill run, see Catch-Up Bill Runs.
To initiate a one-time invoice run, select Start run now.
All other scheduling options for the invoice run are hidden when you immediately start the invoice run.
To activate the invoice scheduler, select Active.
Invoices are generated only when the scheduler is active. You can also create invoice schedulers in a draft state and activate them when needed.
Select a start date, start time, and the time zone for the scheduler.
To generate invoices in a posted status, select Post invoices.
If you deselect Post invoices, invoices are created in draft status.
To create invoice PDF documents automatically as invoices are streamed during the batch run, select Generate Invoice Documents.
Select a frequency, then specify the date and period fields that appear.
For when to use each option, see Understand Invoice Date, Target Date, and Billing Period Count.
Once	Enter the target date and invoice date as calendar dates. If Catch-Up Bill Run is selected, frequency is Once and Invoice Date is disabled.
Daily, weekly, or monthly	Billing calculates the target date and invoice date for each invoice batch run. Base Target Date On, Base Invoice Date On, and Invoice Date Offset control those calculated dates. You can also select Exclude holidays and weekends. Holidays are configured in the UTC time zone, and the scheduler must match the time zone. A weekly run also shows the day of the week.
For every frequency, Select billing schedules based on determines whether Billing uses a target date, a billing period count, or a billing period count with an optional target date filter.
Target Date	For a once run, enter Target Date. For a daily, weekly, or monthly run, specify Base Target Date On. Billing selects schedules whose next billing date is on or before the target date.
Billing Period Count	Billing Period Count appears. Each selected schedule is invoiced for that number of periods. Target date fields remain available to filter which schedules are selected for invoicing. For a once run, Target Date is optional. For a daily, weekly, or monthly run, Base Target Date On remains available; those target date fields are optional.
For a daily, weekly, or monthly run, Base Target Date On controls how Billing calculates the target date.
Offset from Run Date	Billing adds Target Date Offset to the date the invoice batch run runs.
Day Of Month	Billing uses Target Day Of Month in the month of the invoice batch run, shifted by Target Month Offset. Target day of month can be 1 through 28, or last, second-to-last, or third-to-last.
For a daily, weekly, or monthly run, Base Invoice Date On controls how Billing calculates the invoice date. Invoice Date Offset appears with either option.
Offset from Target Date	Billing adds Invoice Date Offset to the target date.
Offset from Run Date	Billing adds Invoice Date Offset to the date the invoice batch run runs.
For a monthly run, On controls whether the run uses a weekday cadence or a calendar date.
Every	Cadence (First, Second, Third, Fourth, or Last) and Day (Sunday through Saturday).
Specific Date	Date (1 through 28, or last, second-to-last, or third-to-last).
If needed, for recurring invoice runs, stop the schedule recurrence after a date by selecting the end date.
Click Next.
Select the billing batch to generate invoices for, or filter billing schedules based on your criteria.
The invoice run selects billing batches from the billing schedules based on the invoice run matching criteria. A billing batch includes several invoices that are processed simultaneously during an invoice run.
Select the billing charge type for the invoice.
You can select one or a combination of the charge types. By default, all charge types are selected.
If needed, you can also filter the invoice based on legal entity and customer account.
Select the currency for the invoices. You can select multiple currencies to manage invoicing across different regions and locations.
The billing schedules are filtered based on the selected currency.
Click Schedule.
You can modify the scheduled invoice runs later, provided that the runs are in a draft or inactive state.
IMPORTANT When generating invoices by using the Invoice Creation API or invoice batch runs, implement custom automation on generated invoices as asynchronous processes, such as asynchronous flow paths or asynchronous Apex triggers. Synchronous automation in this context can cause performance issues, timeouts, or failures.

To explore examples to understand how to schedule invoice batch runs based on your requirements, see Examples: Invoice Batch Run Frequencies.

To understand the invoice generation process, see Invoice Batch Run Process.

SEE ALSO
Knowledge Article: Invoice Batch Run Fails When Billing Permission Sets Are Assigned via Permission Set Group

=== ARTICLE: ind.billing_billing_arrangement_create.htm ===
---
article_id: ind.billing_billing_arrangement_create.htm
title: Create Billing Arrangements and Billing Arrangement Lines
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_billing_arrangement_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_billing_arrangements.htm
fetched_at: 2026-09-04
---

# Create Billing Arrangements and Billing Arrangement Lines

Billing arrangements define how a transaction’s billable amount is invoiced to the relevant billing accounts.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To create billing arrangements:	

Billing Admin permission set

OR

Billing Operations User permission set

NOTE

Starting Spring ’26, the Billing Arrangement Lines related list is enabled by default. For the Salesforce orgs created in or upgraded to Spring ’26, your Billing admin must perform a one-time task of adding the Billing Arrangement Lines related list to the Billing Arrangement page layout.

From the App Launcher, find and select Billing Arrangements.
Create a billing arrangement.
Click New.
Enter a name for the billing arrangement.
Select Draft as the status.
Save your changes.
Create billing arrangement lines for the billing arrangement.
In the Related tab of the billing arrangement, click New.
Select an account or create one.
Select a billing account or create one.
Enter a percentage of the billing amount to assign to the billing account.
If required, select Remainder to indicate whether to bill the remainder percentage to the billing account.
Save your changes.
You can set the billing arrangement as Active.

Alternatively, you can configure billing arrangements on the billing schedule groups by using the Billing Arrangements tab.

=== ARTICLE: ind.billing_billing_arrangements.htm ===
---
article_id: ind.billing_billing_arrangements.htm
title: Manage Billing Arrangements
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_billing_arrangements.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Manage Billing Arrangements

Billing arrangements facilitate precise invoicing for business scenarios such as parent account billed for subsidiary accounts, cross-departmental charge allocations, or services or assets shared among multiple parties. Use billing arrangements to configure the allocation of billing amounts to a specific billing account or distribute costs among several billing accounts based on fixed percentages.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Key Terms

Here are a few key terms used when configuring billing arrangements.

Owning Account
The account that uses or owns the service or asset
Billing Account
The account that receives the bill
Billing Arrangement
The configuration for invoicing a transaction’s billing amount to one or more accounts. The billing arrangement specifies whether the total amount is invoiced to the owning account or a different billing account, or whether the invoice is split among multiple billing accounts. For each assigned account, users can select a corresponding billing profile to fetch its billing preferences.
Billing Arrangement Line
The billing account, billing profile, and the percentage of the billing amount to be invoiced. Each billing arrangement line results in a separate invoice addressed to the selected billing account.
Split Billing
The process of splitting the bills for services or assets to generate multiple invoices addressed to different billing accounts. The split billing amounts in each invoice are calculated based on predefined percentages in the billing arrangement that’s associated with the billing schedule group.
How Billing Arrangements Work

You can create billing arrangements and apply them to billing schedule groups. When the invoice batch run processes billing schedule groups with related billing arrangements, Billing generates invoices simultaneously for each of the billing accounts that are part of the billing arrangement on the next billing date of the billing schedule group. Based on the configuration specified in the billing arrangement, Billing generates one or more invoices for the total bill amount. If the billing arrangement indicates a 100% allocation to an account, then Billing generates one invoice for the corresponding billing account. If the billing arrangement has multiple billing arrangement lines with various specified percentages, then Billing splits the total amount into multiple split invoices, and generates invoices for each billing account accordingly.

The billing profile selected for a billing account in the billing arrangement line indicates the preferred payment terms, bill-to contact, billing address, and invoice template for that account. These preferences take precedence over the default values provided on the billing schedule group. Billing preferences such as suspension dates, and document and email delivery settings, are based on the default billing profiles of the corresponding billing accounts. All other billing details such as the billing day of month, next billing date, ship-to address, ship-from address, and saved payment method are based on the billing schedule group and apply to the split invoices as well.

The invoices can be viewed on the Invoices related list of the corresponding billing accounts. The invoices are also available in the All Invoices related list of the corresponding Order records.

How Account-Level Invoicing Works with Billing Arrangements

When you generate, preview, or schedule invoices for a specific account, Billing selects billing schedule groups from two sources by default:

Billing schedule groups that the account owns directly
Billing schedule groups that the account is responsible for as a billing account on an active billing arrangement, even if another account owns those groups

Each time you generate, preview, or schedule invoices, Billing always includes both owned and billed charges together in the same run.

NOTE

To invoice only the billing schedule groups that an account owns, or only the groups that it's billed for through an arrangement, use the Invoice Creation API. Specify the billingScheduleIds parameter to generate invoices from the billing schedules in those billing schedule groups, instead of generating invoices for the account.

When a billing arrangement splits a group's cost across multiple billing accounts, invoicing any one of those accounts generates a separate invoice for each account, based on its share of the total.

How Billing Operations Impact Billing Arrangements

Let’s understand the impact of billing operations on billing arrangements.

BILLING OPERATION	IMPACT ON THE BILLING ARRANGEMENT
Post, void, or delete invoices	

If any invoice generated from a billing schedule group with a related billing arrangement is voided, deleted, or posted, then the same action applies to all the split invoices generated from that billing schedule group. This is because the invoice lines originate from the same billing schedule group and billing arrangement. For instance, if you post one invoice, then all the other split invoices are also posted.


Amend, renew, cancel transactions	Billing preserves the billing arrangement configuration when a billing schedule group with associated billing arrangements undergoes amend, renew, or cancel transactions. The actions create new amend, renew, or cancellation billing schedules in the same billing schedule group. The percentage allocations and billing account assignments remain intact across the transaction lifecycle.
Write-off invoices	If any of the split invoices created from the same set of billing schedule group and billing arrangement is written off,then the other split invoices can’t be voided.
Suspend billing	If the billing schedule group or any of the billing accounts in its associated billing arrangement are suspended for billing, then none of the billing accounts are invoiced during the suspension period.
Billing Arrangements on Orders and Other External Transactions

To view an order or account’s related billing arrangement as a field on the Order or Account record, add the Billing Arrangement field as a custom field of type Lookup Relationship to the Order or Account object.

To view the Billing Arrangements as a separate tab on the Order or Account record, edit the page layout of the Order or Account object and add a new tab for the Billing Arrangements component.

To configure billing arrangements for an order or any other external transaction, extend the out-of-the-box BillingContext or StandaloneBillingContext context definitions and map the billing arrangement to its billing schedule groups. Make sure to add the Billing Arrangement field on the Order object, and then view all related billing arrangements for the order on the Billing Arrangement tab of the Order record.

Track Billing Arrangement Relationships on Account and Invoice Records

Use the related lists on Account and Invoice records to track billing arrangement activity.

On the Account record, two related lists give you visibility into billing schedule groups. The Billing Schedule Groups Owned related list shows all billing schedule groups owned by the account, The Billing Schedule Groups with Billing Arrangement related list shows the groups tagged with an active billing arrangement where the account is a billing account. A billing schedule group appears in this list for all billing accounts in the billing arrangement, regardless of which account owns the billing schedule group.

On the Invoice record, the Related Invoices with Same Billing Arrangement related list shows all other invoices generated from the same billing arrangement version as the current invoice.

Create Billing Arrangements and Billing Arrangement Lines
Billing arrangements define how a transaction’s billable amount is invoiced to the relevant billing accounts.
Configure Billing Arrangements for Billing Schedule Groups
Route invoices with the appropriate allocated charges to the correct billing accounts by configuring billing arrangements on billing schedule groups.
Examples: Flexible Invoicing for Complex Business Models
Billing arrangements can help you manage complex financial relationships by automating the allocation of invoice charges across billing accounts. You can configure billing arrangements for invoicing a billing account that’s different from a service or owning account. You can also split bills for products or services shared by multiple accounts to streamline invoicing with prorated charge allocation. Here are several business scenarios where billing arrangements help businesses by invoicing and billing the right parties.

=== ARTICLE: ind.billing_billing_arrangements_examples.htm ===
---
article_id: ind.billing_billing_arrangements_examples.htm
title: "Examples: Flexible Invoicing for Complex Business Models"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_billing_arrangements_examples.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_billing_arrangements.htm
fetched_at: 2026-09-04
---

# Examples: Flexible Invoicing for Complex Business Models

Billing arrangements can help you manage complex financial relationships by automating the allocation of invoice charges across billing accounts. You can configure billing arrangements for invoicing a billing account that’s different from a service or owning account. You can also split bills for products or services shared by multiple accounts to streamline invoicing with prorated charge allocation. Here are several business scenarios where billing arrangements help businesses by invoicing and billing the right parties.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Different Owning and Billing Accounts

Consider a parent-subsidiary business model where the subsidiary company, say Acme Manufacturing, uses a Cloud Storage subscription licensed by the parent company, Acme Corp. Though Acme Manufacturing uses the subscription service, Acme Corp manages the licensing, so all bills go to the corporate headquarters, say Acme Corp, for centralized payment processing.

For this business scenario, let’s use a billing arrangement to clearly demarcate the owning and billing accounts. Create a new billing arrangement to specify the owning and billing accounts, and allocate 100% of invoice charges to the billing account.

Owning Account: Acme Manufacturing that uses the service, and performs any amendments, renewals, and cancellations.
Billing Account: Acme Corp that receives the invoices and handles payments.
Billing Profile: Acme Corp’s billing profile to indicate the billing preferences such as billing contact, billing address, payment terms, and payment method.
Billing Percentage: 100%

The billing schedule group shows the new billing arrangement with details about the owning and billing account, the assigned billing percentage, together with the billing preferences.

In the upcoming billing cycle, the invoice is generated based on the billing arrangement details. The generated invoice shows Acme Corp as the billing account (1) with the associated billing arrangement (2) and billing profile (3) stamped on it.

Shared or Split Billing Across Accounts

Consider a shared service model where multiple organizations share infrastructure, software, or services with proportional cost allocation. Three companies—SmartBytes, AT&T, Acme Corp—share a few services that are owned by SmartBytes. SmartBytes, AT&T, and Acme Corp share costs for the shared services based on this split configuration.

SmartBytes: 40%
AT&T: 30%
Acme Corp: 30%

For this business scenario, let’s create a split billing arrangement where the entire service or order is owned by one account, SmartBytes, but billed to all the three organizations, SmartBytes, AT&T, and Acme Corp.

Owning Account:SmartBytes that owns the shared infrastructure
Billing Accounts: SmartBytes, AT&T, Acme Corp
Billing Arrangement Lines: SmartBytes, AT&T, Acme Corp
SmartBytes: 40%, including any remainders
AT&T: 30%
Acme Corp: 30%

The billing arrangement “SmartBytes” Split (1) is created for the order (7) that’s owned by SmartBytes. The billing arrangement has three billing arrangement lines (2). Each billing arrangement line (3) includes the billing account (4), it’s corresponding billing profile (5), and the allocated billing percentage (6).

Here’s a view of the billing arrangements for each account as seen on the Billing Arrangements tab. The SmartBytes owning account is allocated zero billing percentage but the SmartBytes billing account pays 40%, AT&T billing account pays 30%, and Acme Corp pays 30% of the total order amount.

When the order is activated, the same billing arrangement is applied and stamped on the billing schedule groups. When the invoice is then generated, three separate invoice documents are produced, one for each account. You can view the invoices in the All Invoices tab of the order. The invoice amounts are based on the percentages defined in the billing arrangement.

=== ARTICLE: ind.billing_billing_profiles_create.htm ===
---
article_id: ind.billing_billing_profiles_create.htm
title: Create Billing Profiles
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_billing_profiles_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Create Billing Profiles

Cater to your customers' billing preferences and business needs by creating billing profiles for their accounts. Define multiple billing profiles for an account to manage diverse billing needs, each with its own billing details, payment terms, and contacts. Set a default billing profile for accounts to easily access your customers' preferred billing day of the month, billing address, billing contact, and other details. With billing profiles, sales representatives no longer need to enter this information for each transaction, saving time and effort.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create billing profiles:	

You must have ONE of these permission sets:

Billing Admin
Billing Operations User
Payment Admin
Payment Operations User
Credit Memo Operations User
NOTE

On Account record pages in the Billing app, the Billing Profile related list on the Billing Profile tab has been updated in Winter ’26. It now displays Billing Accounts records, replacing the Account Billing Accounts records shown in Summer ’25. If you have customized the Account record pages, this change is not automatically applied during the upgrade. You will consequently encounter an error and the related list will be missing. To fix this issue, edit the customized Account record page to remove the old Account Billing Accounts related list and add the new Billing Accounts related list instead.

Each billing profile corresponds to a billing account record.

From the App Launcher, find and select Billing.
From the navigation bar, click Accounts and open the account for which you want to create a billing profile.
In the Billing Profile section, click New.
In the Information section, enter these details.
Enter a name for the billing account.
The account is autopopulated. You can select a different account for the billing account.
To set the billing account as the default billing profile for the account, select Default Billing Profile.
You can set only one default billing profile for an account.
In the Address section, enter the primary billing address and shipping address.
In the Billing Information section, enter these details.
Enter a bill day of the month and select a contact for billing.
When a billing schedule is generated from any transaction, the bill day of month comes from the billing profile. When a billing schedule is generated from an order, the bill day of month is determined by the period boundary set on the order item.
Select the payment terms.
Select Skip Automatic Payment to disable the automatic processing of payments.
You can also view the saved payment methods associated with the selected account.
In the Email Information section, enter these details.
Select an email template.
Use Default Invoice Email Template or clone and customize the email template based on your business needs.
To send an invoice PDF document with the email, select Attach Invoice Document to Email.
Save your changes.

When processing a transaction, Billing follows the behavior mentioned in this table to determine which values to use.

SCENARIO	BEHAVIOR
Transaction record has the required values.	The values of the transaction are used.
Transaction record doesn't have the required values but is associated with a billing profile.	The values of the associated billing account are used.
Transaction record doesn't have the required values and isn't associated with a billing profile.	The values of the account's default billing profile are used.
Transaction record doesn't have the required values, isn't associated with a billing profile, and the account doesn't have a default billing profile.	The org default values are used.
NOTE Updating an account’s billing profile doesn’t affect the existing billing schedules.

Optionally, to pass the billing profile field to a transaction, complete these steps.

Create a custom lookup relationship field on the order object, and associate it to the billing account object.
In the extended BillingContext context definition, map the out-of-the-box billing profile context tag to this custom lookup field.

=== ARTICLE: ind.billing_catch_up_bill_runs.htm ===
---
article_id: ind.billing_catch_up_bill_runs.htm
title: Catch-Up Bill Runs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_catch_up_bill_runs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_automate_invoice_generation.htm
fetched_at: 2026-09-04
---

# Catch-Up Bill Runs

Use a catch-up bill run to advance the next billing date, billed amount, and pending amount on billing schedules for transactions that a legacy system fully or partially billed. Catch-up doesn’t create invoices for those periods.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


This feature is available with the Revenue Management Advanced license or the Revenue Management Billing license.

The Milestone Billing feature is available only with the Revenue Management Billing license. Contact your Salesforce account executive for more information.

After you import accounts, orders, billing schedules, billing schedule groups, and billing milestone plans, complete catch-up before generating invoices for those schedules. You can run catch-up more than once for the same schedules until a draft or posted invoice exists. Schedules that already have a draft or posted invoice aren’t included.

Set the target date to the last date billed in the legacy system so the next invoice batch run in Billing starts with the next unbilled period. Catch-up doesn’t create tax, credit or debit memos, payments, or invoice documents for those periods.

NOTE Don’t start an invoice batch run while a catch-up bill run is in progress. Parallel invoicing can leave billing schedules and invoices inconsistent.

For milestone billing, accomplished milestones with an accomplishment date on or before the target date are treated as invoiced. Later milestones remain available for the next invoice run.

To schedule a catch-up bill run, select Catch-Up Bill Run when you create an invoice scheduler. Catch-up bill runs use the Once frequency and require a target date. See Generate Invoices Automatically Based on Billing Schedules.

CATCH-UP AFTER A LEGACY MIGRATION

Infiwave migrates monthly billing schedules from a legacy system that billed those schedules through May 1, 2026. The company wants the first invoice in Billing to cover June 2026. The company configures a catch-up bill run by using these values.

Catch-Up Bill Run: Selected
Frequency: Once
Target Date: May 1, 2026

Catch-up advances the next billing date, billed amount, and pending amount through May 1. It doesn’t create invoices. Billing updates the next billing date to June 1, 2026. The company then configures an invoice batch run by using these values.

Frequency: Once
Select billing schedules based on: Target Date
Target Date: June 1, 2026

Billing generates invoices for the June 2026 billing period. A later target date, such as July 1, 2026, can include more than one billing period. To invoice only the next unbilled period, match the target date to that period or set billing period count.

=== ARTICLE: ind.billing_change_billing_frequency_examples.htm ===
---
article_id: ind.billing_change_billing_frequency_examples.htm
title: "Examples: Impact of Billing Frequency Change"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_change_billing_frequency_examples.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_change_billing_pricing_frequencies.htm
fetched_at: 2026-09-04
---

# Examples: Impact of Billing Frequency Change

When you change billing frequency on a transaction as different from the pricing frequency, Billing prorates the total amount from the transaction over whole and partial billing periods. For any partial periods, Billing prorates the amount based on the billing frequency. Let’s understand the calculation process with a few examples.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Mid-Year Subscription Start with Annual Billing Preference

Many enterprise customers prefer annual billing cycles for better cash flow management and reduced administrative overhead, even when product or service subscriptions start mid-month. This scenario is particularly common in businesses where the commencement of a product or service doesn’t align with calendar months, the finance teams prefer consolidated annual invoices, or when customers want predictable annual costs.

Product Configuration

Product: Analytics Platform Subscription
Unit Price: $100.00 (monthly pricing)
Quantity: 2
Pricing Term: Monthly
Billing Frequency: Annual (changed from Monthly)
Subscription Period: March 15, 2025 - March 14, 2026

Calculation Process

Step 1: Billing Period Breakdown

Monthly unit price: $100.00 (Quantity: 2 = $200.00/month)
Subscription covers: Total of 12 months

Step 2: Calculation for the first partial month in March 2025

March 15-31, 2025: 17 days out of 31 days in March
Proration multiplier: 17/31 = 0.5484
Prorated amount: $200.00 × 0.5484 = $109.68

Step 3: Calculation for Full Months

April 2025 - February 2026: 11 full months
Full month amount: $200.00 × 11 = $2,200.00

Step 4: Calculation for the last partial month in March 2026

March 1-14, 2026: 14 days out of 31 days in March
Proration multiplier: 14/31 = 0.4516
Prorated amount: $200.00 × 0.4516 = $90.32

Step 5: Generated Billing Schedule

Start Date: March 15, 2025
End Date: March 14, 2026
Billing Amount: $2,400.00 ($109.68 + $2,200.00 + $90.32)
Billing Frequency: Annual
Proration Multiplier: 1.00
Calculated Quantity: 1.00
Quarter-End Subscription with Fiscal Year Alignment

Many enterprises align their software subscriptions with fiscal quarters to streamline budget planning and financial reporting. This scenario is particularly relevant for companies with seasonal business cycles, or when finance teams manage quarterly budgets, or for other audit and compliance requirements.

In this example, a customer starts their subscription at the end of Q1 (March 25th) but wants annual billing to consolidate their software expenses into a single yearly transaction. Billing must accurately generate billing schedules for a subscription starting March 25th with only 7 days left in the quarter, spanning into the next fiscal year, while maintaining annual billing frequency with exact calendar day precision.

Product Configuration

Product: Enterprise CRM Platform
Unit Price: $180.00 (monthly pricing)
Quantity: 1
Pricing Term: Monthly
Billing Frequency: Annual (changed from Monthly)
Subscription Period: March 25, 2025 - March 24, 2026

Calculation Process

Step 1: Billing Period Breakdown

Monthly unit price: $180.00
Subscription covers: Total of 12 months

Step 2: Calculation for the first partial month in March 2025

March 25-31, 2025: 7 days out of 31 days in March
Proration multiplier: 7/31 = 0.2258
Prorated amount: $180.00 × 0.2258 = $40.64

Step 3: Calculation for Full Months

April 2025 - February 2026: 11 full months
Full month amount: $180.00 × 11 = $1,980.00

Step 4: Calculation for the last partial month in March 2026

March 1-24, 2026: 24 days out of 31 days in March
Proration multiplier: 24/31 = 0.7742
Prorated amount: $180.00 × 0.7742 = $139.36

Step 5: Generated Billing Schedule

Start Date: March 25, 2025
End Date: March 24, 2026
Billing Amount: $2,160.00 ($40.64 + $1,980.00 + $139.36)
Billing Frequency: Annual
Proration Multiplier: 1.00
Calculated Quantity: 1.00

=== ARTICLE: ind.billing_change_billing_pricing_frequencies.htm ===
---
article_id: ind.billing_change_billing_pricing_frequencies.htm
title: Change Billing Frequency on New and Existing Subscriptions
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_change_billing_pricing_frequencies.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_frequency_change_flow_impact.htm
fetched_at: 2026-09-04
---

# Change Billing Frequency on New and Existing Subscriptions

You can update the billing frequency of a subscription at any time, such as by switching from monthly to annual or from annual to monthly. On active subscriptions, you can update the billing frequency from any cadence to any other, such as monthly to annual billing or vice versa, without canceling or recreating the subscription. To achieve this, sales reps make a zero-quantity, field amendment for the asset, to update the billing frequency, Billing automatically prorates the charges and applies the new billing cadence from the effective date.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To change billing frequency on new and existing subscriptions:	

Billing Admin permission set

OR

Billing Operations User permission set

NOTE For orgs created in or upgraded to Spring ’26, perform a one-time task of adding the Change Billing Frequency checkbox to the Billing Treatment page layout.
Examples: Impact of Billing Frequency Change
When you change billing frequency on a transaction as different from the pricing frequency, Billing prorates the total amount from the transaction over whole and partial billing periods. For any partial periods, Billing prorates the amount based on the billing frequency. Let’s understand the calculation process with a few examples.
Change the Billing Frequency

Make sure that the product has a valid, active billing treatment, and the Change Billing Frequency checkbox is selected on that billing treatment.

Open the quote line record or open the Billing Information section of the order product.
For new sale orders, select the billing frequency or cadence, such as Weekly, Monthly, Quarterly, Semi-Annual, or Annual. For existing orders, initiate the billing frequency change as a zero-quantity, field amend action.
Save your changes, and then activate the order.

On existing orders, Billing automatically prorates the charges and applies the new billing frequency from the effective date. Billing cancels existing billing schedules and generates updated billing schedules for the new billing frequency, which are picked up during invoice generation.

Change the Billing Frequency by Using Create Standalone Billing Schedules API

Starting Summer ’26, you can use the Create Standalone Billing Schedules API to change billing frequencies of order products during a subscription period. Use the API to update multiple billing schedules from lower pricing frequency to higher billing frequencies and vice versa, directly from the Billing Schedule Group record.

In the request body of the API, specify these values in the transactionDetails property value of the amended transaction.
Specify the billing schedule group ID for which you want to update the billing frequency in BillingScheduleGroupId__std.
Specify the billing frequency for the specific billing schedule group ID in BillingTermUnit__std.
Specify the date from when the update to the billing frequency is applicable in StartDate__std.
If the billing term unit is quarterly, semi-annual, or annual, then specify the month from when the billing frequency change is applicable in BillingStartMonth__std.
Specify Amend as the action type in BillingActionType__std.
Specify BillingFrequencyChange as the action subtype in BillingSubActionType.

Billing automatically handles complex proration and calculates the correct billing period amounts for the varied pricing and billing frequencies.

IMPORTANT When a billing schedule group is linked to an asset, initiate any new sale, amend, renew, or cancel actions directly from the order or asset. In such cases, use the Order to Billing Schedule flow or Create Billing Schedules for Orders API, and not the Create Standalone Billing Schedules API.

=== ARTICLE: ind.billing_collection_plan_payment_promise_collect.htm ===
---
article_id: ind.billing_collection_plan_payment_promise_collect.htm
title: Collect Payment Promises for a Collection Plan Item
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_collection_plan_payment_promise_collect.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_collections.htm
fetched_at: 2026-09-04
---

# Collect Payment Promises for a Collection Plan Item

Record your customer's payment promises, and create payment schedules and payment schedule items for collection plan items. Collections reps can secure payments for the outstanding balance of the invoice related to the collection plan item.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To collect payment promises:	Billing Collections and Recovery Specialist permission set
To use dataraptors, integration procedures, and flexcards:	Omnistudio User permission set
To create and view payment schedules and payment schedule items:	

Payment Operations permission set

OR

Payment Admin permission set

When you click New Payment Promise on the Collect Payment Promises tab of a Collection Plan record, the Create Billing Promise to Pay flow is run. To use a customized version of this flow, save it as a new flow, make your changes, and then save and activate it.

Open the Collection Plan record that's related to the collection plan item for the invoice that you want to collect payment promises for.
From the Collect Payment Promises tab, click New Payment Promise.
The Create Billing Promise to Pay flow is run to display collection plan items that are related to the collection plan. The invoice balance value of the collection plan items is the same as the actual invoice balance value, but the currency is shown in the user's currency. To avoid confusion, change the user currency in your Salesforce org.
Select a collection plan item for which you want to create a payment schedule and payment schedule items.
Click Next.
A list of existing payment schedules that are related to the invoice of the selected collection plan item appear.
Enter the payment promise details.
Select the number of partial payments in which the customer wants to repay the overdue amount.
You can select up to three partial payments.
If the customer wants to make a single payment, in the First Part Payment Amount field, enter the total payment amount, and select a payment date.
If the customer wants to make multiple partial payments, enter the part payment amounts and select the corresponding payment date for each partial payment.
The sum of all the partial payments can be equal to or less than the invoice balance.
Select a saved payment method, click Next, and then click Finish.

The payment schedule and payment schedule items that are created for the selected collection plan item appear in the Collect Payment Promises tab. A payment batch run processes payment schedule items and applies the corresponding payments to invoices. See Payment Batch Run Overview

Instead of automatically creating payment schedules and payment schedule items for collection plan items, you can create them manually. When you manually create them, the currency ISO code of the collection plan item is used as the payment schedule's currency ISO code regardless of the currency ISO code that you choose on the New Payment Schedule page.

=== ARTICLE: ind.billing_collection_plans_and_plan_items_create.htm ===
---
article_id: ind.billing_collection_plans_and_plan_items_create.htm
title: Create Collection Plans and Collection Plan Items
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_collection_plans_and_plan_items_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_collections.htm
fetched_at: 2026-09-04
---

# Create Collection Plans and Collection Plan Items

Create collection plans for accounts to help your collections reps track and resolve unpaid invoices. Create collection plan items for unpaid invoices that are related to the collection plan's account, enabling your collections rep to focus on the payment collection for individual invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create collection plans and collection plan items:	Billing Collections and Recovery Specialist permission set
Create Collection Plans

A collection plan stores information about the related account, the related collection plan items, the total invoice balance, and the collection timeline. It also includes the payment promises obtained by the collections reps.

You can create Collection Plan records either from the Collections app or directly from the Collection Plans page.

From the App Launcher, find and select Collection Plans.
Click New.
Select the account for which you creating the collection plan.
Select a contact of the account for which you creating the collection plan.
Select a collection plan reason.
Select the usage type as Billing.
If required, specify the due date, closed date, total tax amount, and days past due.
The days past due value isn’t calculated automatically because a collection plan can include one or more invoices with different invoice due dates. We recommend that you provide a value based on your business requirements.
The payment batch run requests payments based on the target payment processing date on the payment schedule item. So, the due date or days past due values specified in the collection plan aren't considered during the collections or payment batch run process.
Save your work.
Create Collection Plan Items

Each collection plan item stores information about the related invoice and its outstanding balance.

You can create Collection Plan Item records either from the Collection Plan Items page or from the Collection Plan records. When you create Collection Plan Item records from a Collection Plan record page, the Create Collection Plan Items For Invoices flow is run. To use a customized version of this flow, save it as a new flow, make your changes, and then save and activate it.

From the App launcher, find and select Collection Plans.
Open the Collection Plan record that you want to generate the collection plan items for.
From the Invoices tab, select the invoices that you want to create collection plan items for. You can select up to 10 invoices.

When you go to Invoices tab, the Create Collection Plan Items For Invoices flow is run to display invoices. These invoices are related to the collection plan's account, aren't fully settled, and aren't related to the existing collection plan items.

Click Create.

The collection plan items that you create appear in Collection Plan Items related list.

When you select multiple invoices, if collection plan items aren't created for a few invoices, check the Revenue Transaction Error Logs related list on those Invoice records. The Error Message field of the logs show the reason for the failure.

NOTE

On the Invoices tab, the Balance value is the same as the invoice balance, but it appears in your personal currency. For example, if the balance of an invoice is 100 Canadian dollars, it appears as US$100 if your personal currency is U.S. Dollars. To avoid this confusion, change your personal currency to the transactional currency of the invoices.

=== ARTICLE: ind.billing_collections.htm ===
---
article_id: ind.billing_collections.htm
title: Manage Collections for Accounts in Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_collections.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Manage Collections for Accounts in Billing

To recover overdue invoices, your collections reps use Collections workflow to track payments, record customer payment promises, and send personalized, automated dunning emails to minimize bad debt and maintain healthy cash flow.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Key Terms

Collection Plan: A record that a collections rep uses to manage an account’s overdue invoices. It shows the account’s total invoice balance, due date, contact details, usage type, collection plan segment, timeline, collection plan items, and payment promises.

Collection Plan Item: An individual invoice on a collection plan. A collection plan can include multiple collection plan items, each corresponding to a different invoice for the same account.

Process Workflow

The Collections feature provides collections reps a structured process for recovering invoice balances.

A collections rep creates a collection plan to track and resolve an account's unpaid or partially paid invoices, then adds each invoice as a collection plan item.

A collections rep initiates dunning orchestration for a collection plan. Billing uses predefined Dynamic Revenue Orchestrator templates to send a milestone-driven sequence of reminders and escalations based on the collection plan’s due date and collection plan segment. Low- and medium-risk accounts receive an early reminder, a due notice, and a suspension notice before the process escalates to manual recovery. The dunning process starts earlier and escalates faster for high-risk accounts. Billing triggers each email or task on the specified date or after the specified day offset, so the dunning process continues until it reaches a manual action, such as a recovery call.

The collections rep then makes recovery calls to customers and records their payment commitments as payment promises. The collections rep generates a payment schedule and payment schedule items with one payment or up to 3 partial payments, each with a due date and amount. A payment batch run then processes these payment schedule items and applies the successful payments to the invoice.

The collections rep can track all recovery activity for an account from the collection plan and its collection plan items. If an invoice is deemed uncollectible, a collections rep can write it off.

Business Use Case: Managing Collections for an Overdue Invoice

Acme Software Innovations provides a cloud-based analytics platform to its customer, Growth Digital Marketing Pro, through a monthly subscription. Growth Digital Marketing Pro owes Acme Software Innovations US$60,600 for an invoice due on March 31, 2025.

Acme Software Innovations’ collections rep reviews the invoice and finds that Billing classified it as high risk and initiated the orchestrated dunning process. Growth Digital Marketing Pro hasn’t paid the invoice or responded to the email reminders.

The collections rep contacts Growth Digital Marketing Pro to negotiate repayment. Growth Digital Marketing Pro agrees to pay in two equal installments. The collections rep creates these payment promises for the collection plan and uses Growth Digital Marketing Pro’s preferred saved payment method.

Payment Schedule: PS0000006

Payment Schedule Item 1: PSI0000001, $30,300 due on May 31, 2025
Payment Schedule Item 2: PSI0000002, $30,300 due on June 30, 2025

The collections rep then schedules a few follow-up reminders based on the new payment schedule due date.

Key Features
Collections App: Create, view, and monitor collection plans and collection plan items for accounts with overdue invoices to manage the invoice recovery process.
Dunning Emails: Leverage out-of-the-box email capabilities of Salesforce to set up and send personalized email reminders to notify customers about overdue invoice balance or upcoming payments. Use Dynamic Revenue Orchestrator templates to orchestrate your dunning strategy for collections. You can use the email templates that are available as part of the dunning orchestration solution to send automated email reminders for your collection plans. However, if you have Marketing Cloud, you can also design dunning campaigns and tailor your email communication for specific customer segments.
Timeline: Track the timeline of unpaid invoices from collections initiation and email communications to scheduled calls. You can also view upcoming tasks such as calling the customer or sending a second email reminder by using the New Task  icon on the activity panel in your collections timeline. See Enable Timeline for Collections and Set Up a Timeline in Salesforce.
Payment Promises: Communicate with the customers, receive payment commitments, and set up payment schedules to streamline the payment process.
Create Collection Plans and Collection Plan Items
Create collection plans for accounts to help your collections reps track and resolve unpaid invoices. Create collection plan items for unpaid invoices that are related to the collection plan's account, enabling your collections rep to focus on the payment collection for individual invoices.
Orchestrate Your Dunning Strategy for Collections
Automate the entire dunning journey—from sending email reminders to manual recovery on payment collections—by using the out-of-the-box Dynamic Revenue Orchestrator (DRO) templates.
Collect Payment Promises for a Collection Plan Item
Record your customer's payment promises, and create payment schedules and payment schedule items for collection plan items. Collections reps can secure payments for the outstanding balance of the invoice related to the collection plan item.
Set Up and Send Dunning Emails
Configure automated dunning campaign emails to improve overdue invoice collections. Your collections reps can schedule timely overdue payment email reminders on a recurring basis, helping improve payment recovery rate and reduce collections efforts.
Collections Specialist Console
Use the Collections Specialist Console to manage your day to day collections from a single screen. Track receivables, invoice aging, and payment promises, and take necessary action directly from the console.

=== ARTICLE: ind.billing_collections_dunning_process_setup.htm ===
---
article_id: ind.billing_collections_dunning_process_setup.htm
title: Set Up and Send Dunning Emails
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_collections_dunning_process_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_collections.htm
fetched_at: 2026-09-04
---

# Set Up and Send Dunning Emails

Configure automated dunning campaign emails to improve overdue invoice collections. Your collections reps can schedule timely overdue payment email reminders on a recurring basis, helping improve payment recovery rate and reduce collections efforts.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Collections feature is available with the Revenue Management Billing license and the Marketing Cloud Growth edition. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To enable Data 360:	Data Cloud Admin permission set
To enable Marketing Cloud:	Marketing Cloud Admin permission set
To create and send dunning emails:	Billing Collections and Recovery Specialist permission set

To segment customer accounts and send personalized communication, complete the prerequisites, integrate your data into Data 360, and then create and send dunning emails.

Complete the Prerequisites

Before you configure the dunning process, complete these prerequisites.

Enter your company's address details in the Company Information page.
Verify if Data 360 is enabled in your Salesforce org. See Build your Data 360 Connection.
Make sure that your Salesforce org is connected to the Data 360 org.
Enable Marketing Cloud Next and install the marketing data kit.
If the Sales data kit isn't available in the list of install the marketing data kits, install and deploy it manually.
Import customer consent to receive dunning emails in a CSV file and upload the CSV file to the Marketing Cloud. See Import Consent Data to Marketing Cloud Next.
Integrate Your Data Into Data 360

To create dunning emails, integrate and manage your data in Data 360 by using data streams, mapping fields, employing identity resolution, segmenting data, and creating data graphs.

Ingest the data of accounts, contacts, invoices, collection plans, or collection plan items into the Data 360 by creating a data stream using Salesforce CRM Starter Bundle.
Data ingested by all data streams is written to data lake objects.
Map the data of the Data Lake Object fields to the Data Model Object fields.
If a standard data model object meets your business needs, view and edit the data model object.
If a standard data model object doesn't meet your business needs, create a custom data model object.
To maintain the relationships between data model objects, map the data of one data model object to another data model object.
This step is required to create data graphs later.
Consolidate data from various sources to integrate information about individuals and accounts into a unified profile by using identity resolution.
See Create identity resolution rulesets and define the identity resolution rulesets to consolidate multiple sources of data into a unified profile.
Create and publish standard, custom, or waterfall segments based on your business needs.
Create and manage data graphs in your Salesforce org.
To use the fields of the datagraph as a placeholder or merge fields when you create a customized email, setup a default data graph in your Salesforce org. See Configure a Data Graph.
Create and Send Dunning Emails

Create campaigns with predefined flows to send dunning emails to the targeted segments. Customize and publish email templates based on your business requirement. Schedule your dunning emails or send them immediately. Track, report, and manage campaigns with the Marketing Calendar to streamline the email communication process.

Create an email campaign and send the dunning emails.
Create and manage SMS messages in Marketing Cloud.
NOTE Instead of segmenting customer accounts and sending dunning emails using the Data 360 and Marketing Cloud, you can alternatively send emails directly from the Collection Plan record page, See Send Email from a Record in Lightning Experience.

=== ARTICLE: ind.billing_collections_specialist_console.htm ===
---
article_id: ind.billing_collections_specialist_console.htm
title: Collections Specialist Console
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_collections_specialist_console.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_collections.htm
fetched_at: 2026-09-04
---

# Collections Specialist Console

Use the Collections Specialist Console to manage your day to day collections from a single screen. Track receivables, invoice aging, and payment promises, and take necessary action directly from the console.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

From the App Launcher, find and select Collections. From the navigation bar, click Collections Specialist Console.

If you don't see the console, ask your Salesforce admin to complete the setup first. See Set Up the Collections Specialist Console.

Filters

Use the Account and Currency filters to keep your whole team working from the same prioritized view, whether you're focused on one account or comparing several. To remove a filter, select All Accounts or All Currencies. If your Salesforce org has multiple currencies enabled, select a specific currency to see totals in the cards and charts.

Summary

Four cards show your overall receivables position at a glance.

Outstanding Receivables: Total unpaid, posted invoice balance, with the invoice count.
Current Due: Unpaid invoices due today or in the future.
Overdue: Unpaid invoices that are past due.
Unapplied Payments: Payments with available balance.

Outstanding Balance totals unpaid invoices and debit memos for the selected account, minus unapplied credits and unapplied payments.

Collection Progress

Use the donut chart to compare your Recovered balance against your Outstanding balance for the selected account and currency. The chart shows the total amount you still need to recover, compared with how much you've already recovered. The chart records the total invoice balance from the collection plan item at the time of creation. View each balance's amount in the legend below the chart.

My Tasks

Review your open tasks linked to a collection plan. The console sorts these by due date to show what's due next.

My Collection Plans

Track your collection plans within the console. Use the sidebar card to see Open and Closed plan counts and access their details. The table below the tabs lists each plan's ID, due date, and account. Use the Create Collection Plan button to start a plan that isn't tied to a specific invoice selection.

Invoice Aging and Payment Promises Charts

Switch between two charts to identify outstanding balance concentrations and expected payments.

View your unpaid invoice total across five overdue-day buckets (Current Due, 30 Days Overdue, 31 to 60 Days Overdue, 61 to 90 Days Overdue, and More Than 90 Days Overdue) in the Invoice Aging bar. Click a bucket to open a filtered list view of the underlying invoices.

Group payment schedule items by status (Ready for Processing, Draft, Failed, and Processing) in the Payment Promises chart. Click a status to open a filtered list view.

Invoice and Dispute Tabs

Act on invoices and disputes using the three tabs. Each tab provides a list-view picker, a table of records, and an Open List View link. Scroll to load more rows automatically.

TAB	SHOWS	AVAILABLE ACTIONS
Critical Follow-Ups	Posted invoices with a balance greater than 0, more than 30 days overdue	Create Collection Plan, Write Off Invoice, Create Task
High-Value Overdue Invoices	Posted invoices with a balance greater than $2,000	Send Reminder, Create Task, Create Collection Plan
Invoice Disputes	Open disputes on invoices, shown as dispute records rather than invoice records	Send Reminder, Resolve Case, Create Task

Switch among prebuilt and custom views using each tab's list-view picker. Use the Open List View option to create a new view, edit an existing view's filters, or rename a view. It opens the list view page for that tab's records with your current view applied, so you can create, edit, and rename list views there. A renamed view keeps its new name on the console.

To act on a row, select one or more records in a tab, and then click an action button.

ACTION	DESCRIPTION
Create Collection Plan	Select one or more invoices, then click Create Collection Plan to create a plan covering them. The button is unavailable if a selected invoice already has a linked collection plan. To create a plan without selecting invoices, use Create Collection Plan in My Collection Plans instead, or see Create Collection Plans and Collection Plan Items to build one field at a time.
Write Off Invoice	Select a single invoice, then click Write Off Invoice to open the dialog. Select a value from the Reason Code picklist and, optionally, enter a Description, then save your changes. Refresh the page after some time to see the invoice removed from the tab and the balance updated. Behind the scenes, the system creates and applies a credit memo for the amount you're writing off. To understand how write-offs and credit memos work, see Write Off Invoices.
Send Reminder	Select an invoice, then click Send Reminder to send a payment reminder to the invoice's billing contact through Salesforce's standard Send Email action.
Resolve Case	Select a single dispute, then click Resolve Case to open the case record linked to it. From there, click the case's own Resolve Case action, select the resolution type that matches the request, and finish. Billing completes the resolution and closes the case. For the full workflow by request type, see Resolve Billing Service Requests.
Create Task	Select a single invoice or dispute, then click Create Task to open the task composer and log a follow-up task.
Set Up the Collections Specialist Console
Grant your collections team access to the Collections Specialist Console: turn on the tab and add the console to the Collections app.

=== ARTICLE: ind.billing_collections_specialist_console_setup.htm ===
---
article_id: ind.billing_collections_specialist_console_setup.htm
title: Set Up the Collections Specialist Console
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_collections_specialist_console_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_collections_specialist_console.htm
fetched_at: 2026-09-04
---

# Set Up the Collections Specialist Console

Grant your collections team access to the Collections Specialist Console: turn on the tab and add the console to the Collections app.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To set up the Collections Specialist Console:	

System Administrator

AND

Billing Collections and Recovery Specialist permission set

From Setup, in the Quick Find box, enter Profiles, and then select Profiles.
Select the profile assigned to your collections team.
Under Tab Settings, make sure the Collections Specialist Console tab's visibility is set to Default On.
From Setup, in the Quick Find box, enter App Manager, and then select App Manager.
Find the Collections app and click Edit.
In App Options or Navigation Items, add the Collections Specialist Console page, and then save your changes.
Grant field-level security access to the Initial Due Amount field on the Collection Plan Item object for the profile or permission set your collections team uses. Without this access, the Collection Progress chart in the console appears empty for those users.

After setup, assign the Billing Collections and Recovery Specialist permission set to each user who opens the console.

=== ARTICLE: ind.billing_configure_context_definitions.htm ===
---
article_id: ind.billing_configure_context_definitions.htm
title: Configure Context Definitions for Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_configure_context_definitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup.htm
fetched_at: 2026-09-04
---

# Configure Context Definitions for Billing

Context definitions in Billing act as a central data-mapping layer that helps information flow seamlessly from orders or external transactions into billing schedules. They transform data from Salesforce objects into a standardized format that enable the Billing APIs to read the details required to create accurate billing records. By configuring these context definitions, businesses can automate the transfer of custom field data.

Standard Context Definitions for Billing
After you turn on Context Service, you can access the standard context definitions that are available with Billing.
Select Context Definition and Mapping for Create Billing Schedules for Orders API
The Create Billing Schedules for Orders API uses Context Service to hydrate the data of orders to create billing schedules. Before using this API, select a context definition and its mapping that you want the API to use.
Capture Preferred Transaction Details by Using Custom Fields
To meet specific business requirements, populate custom field data from orders or external transactions to corresponding billing schedule, billing schedule group, and billing schedule group relationship records. Use Context Service to define how data must be transferred by configuring a custom intracontext mapping. Then, use the Create Billing Schedules for Orders API or the Create Standalone Billing Schedules API to generate billing schedules and billing schedule groups. You can also use custom fields to override the standard fields in billing nodes by using the custom intracontext mapping.

=== ARTICLE: ind.billing_configure_dunning_orchestration.htm ===
---
article_id: ind.billing_configure_dunning_orchestration.htm
title: Orchestrate Your Dunning Strategy for Collections
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_configure_dunning_orchestration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_collections.htm
fetched_at: 2026-09-04
---

# Orchestrate Your Dunning Strategy for Collections

Automate the entire dunning journey—from sending email reminders to manual recovery on payment collections—by using the out-of-the-box Dynamic Revenue Orchestrator (DRO) templates.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To initiate dunning orchestration:	

Billing Operations User permission set

OR

Billing Collections and Recovery Specialist permission set

How Dunning Orchestration Works

The dunning orchestration feature in Billing uses the Dynamic Revenue Orchestrator framework to manage and automate the dunning lifecycle. The orchestration plan that’s shipped out of the box, drives a structured sequence of reminders and escalations based on collection plan’s due dates and customer risk profiles.

When you set up dunning orchestration solution and turn on Automate Dunning Orchestration on the Billing Settings page, these components are installed in your Salesforce org.

Collections Dunning Orchestration Workspace: A DRO fulfillment workspace that contains the step definitions and step definition groups that define the dunning sequence. The fulfillment workspace includes two fulfillment scenarios that categorize accounts based on the risk score of the collection plan. The Fulfillment Workspace object includes these objects:Fulfillment Workspace Item, Fulfillment Scenario, Fulfillment Step Definition Group, Fulfillment Step Definition, and Fulfillment Step Dependency Definition.
BillingOrchPlanCtxMapping context mapping: The orchestration plan context mapping that maps the DRO engine to the BillingCollectionPlanContext standard context definition. It also enables the orchestration framework to access collection plan data and trigger automated workflows.
Email Templates: Early Reminder, Invoice Due Notice, and Suspension Notice. The dunning workflow uses these three email formats to send email reminders and notices to customers.

Your Salesforce org also includes an out-of-the-box screen flow named Orchestrate Dunning Reminders. The screen flow includes the Send Dunning Email invocable action that, when invoked, sends reminder and notice emails for upcoming and overdue invoices.

Billing Dunning Orchestration Workflow

The dunning orchestration follows a milestone-driven sequence where each fulfillment scenario contains milestones and automated tasks with step dependencies that control the timing and sequencing of actions. Before triggering the next action, each step waits for a specific date or day count, depending on the collection plan’s due date. The fulfillment scenarios are based on the collection plan’s risk score—Low, Medium, or High—populated in the Overdue Risk Indicator field of the Collection Plan record.

Low and Medium Risk Accounts: This orchestration sequence applies to collection plans with a Low or Medium risk score. The orchestration follows a gradual escalation path.
High Risk Accounts: This orchestration sequence applies to collection plans with a High risk score. The orchestration starts earlier and escalates faster.

For low and medium risk accounts, here’s the dunning orchestration sequence.

STEP	TIMING	ACTION
1	5 days before the collection plan due date	Early Reminder email: a friendly email to the customer with a list of all invoices, balances, and due dates
2	On the collection plan due date	Invoice Due Notice email: an email notice to the customer with a list of all unsettled or partially settled invoices, and total balance
3	7 days after the collection plan due date	Suspension Notice email: a suspension notice to the customer with details of all unsettled invoices and total balance
4	10 days after the collection plan due date	Call the customer and initiate manual recovery of payments.

For high risk accounts, here’s the dunning orchestration sequence.

STEP	TIMING	ACTION
1	10 days before the collection plan due date	Early Reminder email: a friendly email to the customer with a list of all invoices, balances, and due dates
2	5 days before the collection plan due date	Early Reminder email: a friendly email again to the customer with a list of all invoices, balances, and due dates
3	On the collection plan due date	Invoice Due Notice email: an email notice to the customer with a list of all unsettled or partially settled invoices, and total balance
4	3 days after the collection plan due date	Suspension Notice email: a suspension notice to the customer with details of all unsettled invoices and total balance
5	4 days after the collection plan due date	Call the customer and initiate manual recovery of payments.

The dunning orchestration is based on the collection plan’s due date, not individual invoice due dates. This means that your collections team can send a single, coordinated set of reminders per collection plan, including all associated invoices in each email. Also, all email reminders are sent at the collection plan level. If a collection plan has multiple invoices, each reminder email includes the invoice details, balance, and due date for all associated invoices.

Collection Plan Context Definition and Context Mapping

The BillingCollectionPlanContext is a standard Billing context definition that includes fields from the CollectionPlan object and its related CollectionPlanItem and Invoice objects. The dunning orchestration workflow uses the context definition to retrieve and process collection plan information. You can extend the context definition to add custom fields and attributes based on your business requirements.

Customize the Dunning Orchestration Workflow

You can customize the dunning orchestration workflow to suit your business needs and match your customer segments, to build a more effective dunning strategy.

Timing of the automated steps: Initiate tasks and reminders on specific days before or after the collection plan’s due date. The out-of-the-box workflow sends the email reminder 5 days before the due date, but you can adjust the timelines to suit your needs.
Email templates: Modify the email templates to match your messaging and branding needs.
Step definitions and sequences: Modify the step definitions, such as changing the actions or adding new steps to suit your dunning strategy.
Orchestration paths: Customize the timing and actions within each orchestration path to reflect your own escalation threshold and manual recovery process.
Execution profiles: Configure the execution rules in the fulfillment scenario to create new rules or update the existing rules and conditions with custom rules and logic. See Configure a Fulfillment Scenario, Define Conditions for a Fulfillment Step to Run, and Understand Execution Conditions for Order Fulfillment for more information.
Set Up Orchestrated Dunning for Collections
Configure and integrate out-of-the-box Dynamic Revenue Orchestrator templates into Billing to automate the entire dunning lifecycle.
Initiate and Monitor Dunning Orchestration
With the dunning orchestration solution set up and enabled on the Billing Settings page, you can initiate automated dunning on your collection plans.

=== ARTICLE: ind.billing_configure_salesforce_payments.htm ===
---
article_id: ind.billing_configure_salesforce_payments.htm
title: Configure Salesforce Payments
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_configure_salesforce_payments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_salesforce_payments_features.htm
fetched_at: 2026-09-04
---

# Configure Salesforce Payments

To use Salesforce Payments for financial transactions, set up an Experience Cloud site and enable Payments for your org. Then, use a guided setup to create a merchant account and payment methods.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To enable and configure Payments features:	Payment Admin permission set
Turn On Salesforce Payments

Set up an Experience Cloud site that's used as a data channel between the payment provider and the Salesforce Payments feature.

After you set up an Experience Cloud site, make sure that Salesforce Payments is enabled.

NOTE

You can automate the process of setting up an Experience Cloud site and enabling Salesforce Payments by using the Commerce Setup Assistant.

Configure Account-Based Sharing for Payments and Refunds Objects

To make sure that only users working with a specific account have access to its payments and refunds details, turn on Share Payment Accounts on the Billing Settings page. This feature grants users access to payment and refund details related to the corresponding Account record. For example, if a user has Read access to the Account record object, they also get Read access to the related Payments and Refunds records.

See PaymentsSharingSettings Metadata API.

SEE ALSO
Trailhead: Set Up Salesforce Payments
Assign Permissions to Access Billing Features
Set Up Merchant Accounts
Automatic Creation of Payment Schedules and Payment Schedule Items
Payment Batch Run Overview

=== ARTICLE: ind.billing_considerations.htm ===
---
article_id: ind.billing_considerations.htm
title: Considerations When Setting Up and Using Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Considerations When Setting Up and Using Billing

Before you set up and use Billing, keep these considerations in mind.

Coexistence with Subscription Management

You can’t turn on Billing when Subscription Management is enabled in your Salesforce org.

Impact of Turning Off Billing

If you set up Billing, and then turn it off:

You can't access any Billing features, including APIs and objects.
When you activate orders, billing schedules aren't created for order products.
Asynchronous API requests that are waiting to be dequeued and invoice runs that are queued before turning off Billing fail because the related Billing objects aren't accessible. In this scenario, Revenue Transaction Error Log records aren't created because the Billing objects they’re created for are no longer accessible.
If you turn off Billing before order activation and the initial orders don't have a billing treatment and a tax treatment, orders are activated without a billing treatment and a tax treatment. Else, they’re activated with the initial order's billing treatment and tax treatment.
If you turn off Billing after order activation and those orders don't have a related billing policy, Billing uses the default billing and tax treatments of your Salesforce org for those orders.
If you turn off Billing after order activation, billing schedules aren't created for any billing transactions.
Required Billing Permission Sets

To avoid facing access issues after turning on Billing and before setting up Billing features, assign the Billing Admin and Billing Operations User permission sets to users with the System Administrator profile.

See Assign Permissions to Access Billing Features.

Unsupported Orders

Billing also doesn't support Subscription Management orders.

Required Values for Order Activation

After turning on Billing, order activation succeeds only if the Order records have values for the Bill to Contact, Billing Address, and Shipping Address fields. Order activation fails if any of these values are missing.

Order Bill To Contact Field-Level Security

On enabling Billing, the field-level security for the Bill To Contact field of the Order object isn’t enabled automatically. You must manually set the field-level security before cloning the Billing context definition.

Designing Billing Policies

You must create and activate billing policies and their related records in this exact sequence because they’re inter-dependent:

Create draft billing policies.
Create the related billing treatments.
Create the related billing treatment items.
Activate the billing treatment items.
Activate the related billing treatments.
Activate the related billing policies.

See Define Billing Policies and Billability Rules.

Designing Tax Policies

You must create and activate tax policies and their related records in this exact sequence because they’re inter-dependent:

Create draft tax policies.
Create the related tax treatments.
Activate the tax treatments.
Activate the related tax policies.

See Tax Calculation for Invoices.

Default Values

The default billing treatment, tax treatment, and legal entity selected on the Billing Settings page are applicable only to Billing.

See Select Default Billing Treatment, Tax Treatment, and Legal Entity.

Supported Languages

The Billing user interface is available in English and all the fully supported languages.

=== ARTICLE: ind.billing_create_and_apply_credit_memos.htm ===
---
article_id: ind.billing_create_and_apply_credit_memos.htm
title: Create and Apply Credit Memos to Invoice Lines
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_create_and_apply_credit_memos.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# Create and Apply Credit Memos to Invoice Lines

Generate credit memos for an account and apply them to invoice and invoice lines that belong to the same account.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create credit memos:	

Billing Admin permission set

OR

Credit Memo Operations User permission set

From the App Launcher, find and select Invoices.
Open a posted invoice that includes the invoice lines.
Go to the Invoice Lines tab and select one or more invoice lines to which you want to apply the credit memo
Click Create and Apply Credit Memo.
For each invoice line, enter the credit amount value greater than or equal to zero, and less than or equal to the invoice line balance.
Define the tax calculation strategy.
To calculate taxes automatically based on the credit amount, select Enable tax calculation.
To use the amount in the Credit Tax Amount field instead of automatic tax line calculation, deselect Enable tax calculation and enter a credit tax amount.
To ignore the tax lines, deselect Enable tax calculation and leave the Credit Tax Amount field blank.
Click Create and Apply.
SEE ALSO
Billing Account Overview

=== ARTICLE: ind.billing_create_legal_entities.htm ===
---
article_id: ind.billing_create_legal_entities.htm
title: Create Legal Entities in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_create_legal_entities.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entities_manage.htm
fetched_at: 2026-09-04
---

# Create Legal Entities in Revenue Management

Create legal entities to manage the billing and tax information for order products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create legal entities:	Billing Admin permission set

Before you create a legal entity record, make sure that the Status field is visible on the Legal Entities page layout. If it isn't, add the field to the page layout.

From the App Launcher, find and select Legal Entities.
Click New.
Enter a name for the new legal entity.
Select Active as the status.
Enter the details as needed.
If multiple currencies are enabled in your Salesforce org, select a currency ISO code.
If you don't select a currency ISO code, your personal currency is considered as the currency ISO code of the record. You can't edit the currency ISO code after a Legal Entity record is created.
Select an email template.
Use Default Invoice Email Template or clone and customize the email template based on your business needs.
To send an invoice PDF document with the email, select Attach Invoice Document to Email.
Save your changes.
To save the new legal entity, the status must be either Active or Inactive.

=== ARTICLE: ind.billing_credit_application_results.htm ===
---
article_id: ind.billing_credit_application_results.htm
title: Results of Credit Memo Application
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_credit_application_results.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# Results of Credit Memo Application

After posted invoices are generated, credits are applied based on the credit application level.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

Applying a credit memo or credit memo line reduces the balance of an invoice or an invoice line. For example, applying a $100 credit memo line to a $500 invoice line reduces the invoice line’s balance to $400.

After the credits are applied, the balance amounts and applied credit amounts are automatically updated as shown in this table.

CREDIT APPLICATION LEVEL	UPDATED CREDIT FIELDS	UPDATED INVOICE FIELDS	NEW RECORD
Invoice	

Credit Memo fields:

Net Credits Applied
Settlement Level is Top Level
	

Invoice fields:

Balance
Net Credits Applied
Settlement Level is Invoice
	Credit Memo Invoice Application record
Invoice Line	

Credit Memo Line fields:

Line Amount
Net Credits Applied

Credit Memo fields:

Net Credits Applied
Settlement Level is Line Level
	

Invoice Line fields:

Line Amount
Net Credits Applied

Invoice fields:

Balance
Net Credits Applied
Settlement Level is Invoice Line
	Credit Memo Line Invoice Line record
SEE ALSO
Credit Application Level

=== ARTICLE: ind.billing_credit_memos.htm ===
---
article_id: ind.billing_credit_memos.htm
title: Manage Credit Memos in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_credit_memos.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Manage Credit Memos in Revenue Management

Create and apply credit memos to decrease the balance of invoices when the quantity or price of orders are amended.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

This flowchart shows how a user with the Credit Memo Operations User permission set can use credit memos in Revenue Management.

About Credit Memos
A credit memo is a document issued by a seller to a buyer to acknowledge a reduction in the amount owed by the customer.
Credit Memo Data Model in Revenue Management
The Credit Memo data model depicts the objects and their relationships to adjust invoices through credit amounts for returns, overcharges, or other billing discrepancies.
Create and Apply Standalone Credit Memos
Create individual credit memos to efficiently provide credits to your customers. Apply these credits to the relevant customer invoice.
Create and Apply Credit Memos to Invoice Lines
Generate credit memos for an account and apply them to invoice and invoice lines that belong to the same account.
Void or Recover Credit Memos
Fix credit memos that are Pending or Error status by recovering them. You can also void an unapplied posted credit memo and reverse the credit by creating a corresponding debit memo.
Automatic Conversion of Negative Invoice Lines into Credit Memo Lines
In certain billing scenarios, an invoice line can be generated with a negative charge amount. This typically occurs when you amend an order to decrease the quantity of a product and generate an invoice for the amended product, or generate an invoice for an order product that has a negative price. Automate conversion of large volumes of such negative invoice lines to credit memo lines, and the application of these credit memo lines to invoices.
Automatic Application of Credits to Settle Invoice Balances
Eliminate the need to manually apply credit memos by automatically applying available credit memo balances to settle the balances of posted invoices.
Manage Credit Memos by Using APIs or Flow Actions
Use APIs or Flow actions to create credit memos, apply credit memos to invoices, unapply already applied credits from invoices, and convert negative invoice lines into posted credit memos.
Results of Credit Memo Application
After posted invoices are generated, credits are applied based on the credit application level.

=== ARTICLE: ind.billing_credit_memos_apis_and_actions.htm ===
---
article_id: ind.billing_credit_memos_apis_and_actions.htm
title: Manage Credit Memos by Using APIs or Flow Actions
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_credit_memos_apis_and_actions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# Manage Credit Memos by Using APIs or Flow Actions

Use APIs or Flow actions to create credit memos, apply credit memos to invoices, unapply already applied credits from invoices, and convert negative invoice lines into posted credit memos.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
GOAL	API
Create a standalone credit memo without applying it to an invoice	

Create a Standalone Credit Memo


Create a credit memo and apply it to an invoice	Create and Apply Credit Memo API
Apply a credit memo to an invoice	

Apply Credit Memo API

To automate the process of applying credits, build a custom flow and use the Apply Credit action. When the credit application level is Invoice, this action applies the balances of credit memos to settle the balances of posted invoices.


Apply a credit memo line to an invoice line	

Apply Credit Memo Line API

To automate the process of applying credits, build a custom flow and use the Apply Credit action. When the credit application level is Invoice Line, this action applies the balances of credit memo lines to settle the balances of posted invoice lines.


Unapply an applied credit memo from an invoice	

Unapply Credit Memo API

To automate the process of unapplying credits, build a custom flow and use the Unapply Credit action. When the credit application level is Invoice, this action unapplies credit memos from invoices and creates a related Credit Memo Invoice Application record of type Unapplied for the existing Credit Memo Invoice Application record of type Applied.


Unapply an applied credit memo line from an invoice line	

Unapply Credit Memo Line API

To automate the process of unapplying credits, build a custom flow and use the Unapply Credit action. When the credit application level is Invoice Line, this action unapplies credit memos lines from invoice lines and creates a related Credit Memo Line Invoice Line record of type Unapplied for the existing Credit Memo Line Invoice Line record of type Applied.


Convert a list of invoice lines with a negative amount into a posted credit memo	Convert Negative Invoice Lines into Credit Memos API

=== ARTICLE: ind.billing_credit_memos_explain.htm ===
---
article_id: ind.billing_credit_memos_explain.htm
title: About Credit Memos
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_credit_memos_explain.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# About Credit Memos

A credit memo is a document issued by a seller to a buyer to acknowledge a reduction in the amount owed by the customer.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
When are Credit Memos Issued?

Credit memos are issued in various scenarios where a seller needs to reduce the amount a buyer owes. These situations often arise due to:

Billing Errors
If a seller mistakenly overcharged a customer or billed them inaccurately, a credit memo is used to adjust the charges and correct the error promptly.
Product Returns and Allowances
When customers return items due to defects, damages, or dissatisfaction, or because they don’t meet specifications, credit memos are issued to either refund the purchase amount or provide store credit.
Pricing Discrepancies and Discounts
Credit memos address situations where incorrect prices were charged or when a discount was not properly applied to an invoice. They can also be used for volume discounts or promotional rebates agreed upon after the initial sale.
Cancellation of Services or Orders
If services are canceled or not fully delivered, or an order is canceled before it's delivered, a credit memo adjusts the amount owed or refunds the customer.
Overpayment
In cases where a buyer overpays an invoice, the seller can issue a credit memo for the excess amount.
Business Use Case: Issuing a Credit Memo for Damaged Goods

Imagine a customer, TechSolutions Inc., purchased 10 units of a specific server model from Global Electronics Ltd. for a total of $10,000. Upon delivery, TechSolutions Inc. discovered that 2 of the 10 servers were damaged during transit.

In this scenario, Global Electronics Ltd. would issue a credit memo to TechSolutions Inc. to account for the damaged goods. The credit memo would contain the total credit amount for these items (2 units x $1,000/unit = $2,000) and have two credit memo lines for the two damaged servers.

Here's the accounting impact:

For Global Electronics Ltd. (Seller): Their accounts receivable would decrease by $2,000, as they no longer expect to receive payment for the damaged servers. Their revenue would also decrease by $2,000, reflecting the reversal of previously recognized revenue. Additionally, their inventory records would be adjusted to account for the damaged goods.
For TechSolutions Inc. (Buyer): Their accounts payable would decrease by $2,000, as they now owe $2,000 less to Global Electronics Ltd. This positively impacts their cash flow by reducing their outstanding payables.

This credit memo ensures that both Global Electronics Ltd. and TechSolutions Inc. have accurate financial records reflecting the adjusted transaction, maintaining transparency and a good business relationship.

=== ARTICLE: ind.billing_credit_memos_standalone_user_interface_create.htm ===
---
article_id: ind.billing_credit_memos_standalone_user_interface_create.htm
title: Create and Apply Standalone Credit Memos
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_credit_memos_standalone_user_interface_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# Create and Apply Standalone Credit Memos

Create individual credit memos to efficiently provide credits to your customers. Apply these credits to the relevant customer invoice.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create and apply credit memos:	

Billing Admin permission set

OR

Credit Memo Operations User permission set

Create Standalone Credit Memos
From the App Launcher, find and select Credit Memos.
Click Create Credit Memo.
Enter an account name.
Select Draft as the status.
You can create a credit memo in both draft and posted status.
Select the credit memo effective date.
Choose a tax strategy to define your tax calculation approach.
To skip the creation of tax lines, select Ignore.
To manually specify a tax amount, select Manual Override.
To compute tax lines by using a tax treatment, select Calculate.
If your tax strategy is Calculate, select a tax treatment.
If needed, provide a description for the credit memo.
Select the ID of the product that are creating the credit memo for. If the product isn't in your Salesforce org, enter the product name.
Either a product ID or product name is required to create a credit memo.
Enter the credit amount.
If your tax strategy is Manual Override, enter a manual override tax amount.
Select the currency of your credit amount.
If needed, enter the billing and shipping address.
Click Create.

The credit memo generation is initiated, and you'll receive a notification after the credit memo is generated.

If you create the credit memo in ‌draft status, obtain the necessary approvals and click Post Credit Memo. After the credit memo is posted, apply it to the required invoice.

Apply Standalone Credit Memos to Invoice or Invoice Lines
From a posted credit memo, click Apply Credit Memo.
The system uses the default credit memo flow to retrieve invoices associated with the same billing account as the credit memo.
Enter the credit amount you want to apply from the available credit memo balance, and select the required invoice.
Click Apply.

The system automatically applies the credit to the invoice or invoice line based on the credit application level. If the total amount of the invoice lines exceeds the credit memo amount to be applied, the system applies the credit to matching invoice lines in descending order. If the invoice line amount is higher than the remaining credit, a partial credit amount is applied to the invoice line. You can view the remaining credit balance from the Balance field on the Credit Memo record. The Balance field isn’t available by default and you can add it from Page Layouts.

Alternatively, you can apply credit memos by using Apply Credit Memo API or Apply Credit Memo Line API.

=== ARTICLE: ind.billing_credit_memos_void_recover.htm ===
---
article_id: ind.billing_credit_memos_void_recover.htm
title: Void or Recover Credit Memos
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_credit_memos_void_recover.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# Void or Recover Credit Memos

Fix credit memos that are Pending or Error status by recovering them. You can also void an unapplied posted credit memo and reverse the credit by creating a corresponding debit memo.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create credit memos:	

Billing Admin permission set

OR

Billing Operations User permission set

OR

Credit Memo Operations User permission set

Void Credit Memos
From the App Launcher, find and select Credit Memos.
Open the posted credit memo that you want to void.
Click Void Credit Memo.

You can void only an unapplied posted credit memo. After the credit memo is voided, the status of the credit memo changes from Posted to Voided. Billing creates a corresponding debit memo in Posted status to offset the credit amount for the ledger. If original credit memo includes a tax calculation, the debit memo includes the applicable tax details.

Recover Credit Memos
From the App Launcher, find and select Credit Memos.
Open the credit memo that’s in pending or error status.
Click Recover Credit Memo.

After you recover a credit memo, its status changes to Canceled.

If the original credit memo included tax, the credit memo moves to the Voided status. Billing automatically creates a corresponding debit memo in the Posted state to reverse the credit in the ledger. The debit memo includes all the original tax details and tax treatments. Billing reverses the tax interaction in the tax engine. Billing sets the debit memo’s invoice generation status to Not Applicable, so it isn’t invoiced.

NOTE To track the status of the void and recover actions, open the Related tab and review the Async Operation Tracker section.

=== ARTICLE: ind.billing_custom_field_support.htm ===
---
article_id: ind.billing_custom_field_support.htm
title: Capture Preferred Transaction Details by Using Custom Fields
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_custom_field_support.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_configure_context_definitions.htm
fetched_at: 2026-09-04
---

# Capture Preferred Transaction Details by Using Custom Fields

To meet specific business requirements, populate custom field data from orders or external transactions to corresponding billing schedule, billing schedule group, and billing schedule group relationship records. Use Context Service to define how data must be transferred by configuring a custom intracontext mapping. Then, use the Create Billing Schedules for Orders API or the Create Standalone Billing Schedules API to generate billing schedules and billing schedule groups. You can also use custom fields to override the standard fields in billing nodes by using the custom intracontext mapping.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To select default records:	Billing Admin permission set

For example, you can create and map a custom field Purchase Order Number on an order object to a field named Purchase Order Number on the corresponding billing schedule object. Similarly, you can define and map a custom field Purchase Order Date on an order item to a Purchase Order Date field on the corresponding billing schedule group object.

Create the required custom fields on the billing schedule, billing schedule group, and billing schedule group relationship objects.
In Context Service, add the corresponding attributes and tag names to the extended context definitions.
Pass any preferred transaction data from orders to billing schedules by using the extended BillingContext context definition.
Pass transaction data from external transactions to billing schedules by using the StandaloneBillingContext context definition.
Map the corresponding attributes to the custom fields on the billing transaction nodes.
To capture preferred details from orders, edit the OrderEntities context mapping to map custom fields from the billing transaction context node attributes to the order fields.
To capture preferred details from any external transactions, edit the TransactionMapping context mapping to map the Transaction node attributes with external transaction fields.
Edit the BSGEntities context mapping to map the billing schedule context nodes to the fields of the billing schedule, billing schedule group, and billing schedule group relationship objects.
Add a custom intracontext mapping with the mapping intent set to Association. Add mappings from the billing schedule group, billing schedule, and billing schedule group relationship nodes to the corresponding billing transaction nodes.
BillingScheduleGroup node to the BillingTransaction node
BillingSchedule node to the BillingTransactionItem node
BillingScheduleGroupRelationship node to the BillingTransactionItemRelationship node
Activate the extended context definition.
Specify the custom intracontext mapping.
Before generate billing schedules from orders, select the custom intracontext mapping on the Billing Settings page in Setup.
Before you generate billing schedules from other internal or external transactions, specify the custom intracontext mapping name as the intraContext​CustomMapping​Name property value in the request body of the Create Standalone Billing Schedules API.
Generate billing schedules.
Use the Create Billing Schedules for Orders API for generating billing schedules from orders.
Use the Create Standalone Billing Schedules API for generating billing schedules from internal or external transactions, or CSV files.
The values in the custom fields are populated automatically.
SEE ALSO
Turn On Context Service
Select Context Definition and Mapping for Create Billing Schedules for Orders API
Revenue Cloud Developer Guide: Create Billing Schedules for Orders API
Revenue Cloud Developer Guide: Create Standalone Billing Schedules API

=== ARTICLE: ind.billing_data_model_credit_memo.htm ===
---
article_id: ind.billing_data_model_credit_memo.htm
title: Credit Memo Data Model in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_data_model_credit_memo.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# Credit Memo Data Model in Revenue Management

The Credit Memo data model depicts the objects and their relationships to adjust invoices through credit amounts for returns, overcharges, or other billing discrepancies.

=== ARTICLE: ind.billing_data_model_debit_memo.htm ===
---
article_id: ind.billing_data_model_debit_memo.htm
title: Debit Memo Data Model in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_data_model_debit_memo.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_debit_memo.htm
fetched_at: 2026-09-04
---

# Debit Memo Data Model in Revenue Management

The Debit Memo data model depicts the objects and their relationships to process debit memos when you undercharge your customer or want to add additional charges.

=== ARTICLE: ind.billing_data_model_financial_accounting.htm ===
---
article_id: ind.billing_data_model_financial_accounting.htm
title: Financial Accounting Data Model in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_data_model_financial_accounting.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_financial_accounting.htm
fetched_at: 2026-09-04
---

# Financial Accounting Data Model in Revenue Management

The Financial Accounting data model depicts the objects and their relationships to record and manage the financial accounting process for Invoice, Credit Memo, Payment, and Refund records. This process includes defining accounting periods, setting up a chart of accounts, and creating dual journal entries for your legal entities.

=== ARTICLE: ind.billing_data_model_invoice.htm ===
---
article_id: ind.billing_data_model_invoice.htm
title: Invoice Data Model in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_data_model_invoice.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Invoice Data Model in Revenue Management

The Invoice data model depicts the objects and their relationships to configure billing criteria, billing periods, and payment due dates for generating billing schedules and invoices aligned with your sales models. This data model also depicts integrating with saved payment methods to store customer payment methods, sequence policies to configure automated sequential numbering for your invoices, and email templates to send emails for invoices.

=== ARTICLE: ind.billing_data_model_payments.htm ===
---
article_id: ind.billing_data_model_payments.htm
title: Payments Data Model in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_data_model_payments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Payments Data Model in Revenue Management

The Payments data model depicts the objects and their relationships to manage the processing of customer payments including a timely collection of these payments and their application to appropriate invoices, and issuing refunds when needed.

=== ARTICLE: ind.billing_debit_memo.htm ===
---
article_id: ind.billing_debit_memo.htm
title: Manage Debit Memos in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_debit_memo.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Manage Debit Memos in Revenue Management

Create debit memos when you undercharge your customer or want to add additional charges. When debit memo lines are converted to invoice lines, the balance of the related invoices increases.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
About Debit Memos
A debit memo is issued by a seller to a buyer when the seller wants to levy additional charges to what was already billed or charged. For example, late payment fees, cancellation fees, and so on.
Debit Memo Data Model in Revenue Management
The Debit Memo data model depicts the objects and their relationships to process debit memos when you undercharge your customer or want to add additional charges.
Create Debit Memos and Related Records
After you identify the additional charges to be paid by your buyer, create debit memos and their related records to make the required adjustments.
Considerations and Results
Learn what happens when debit memo or debit memo lines get converted to invoice and invoice lines.

=== ARTICLE: ind.billing_debit_memo_create.htm ===
---
article_id: ind.billing_debit_memo_create.htm
title: Create Debit Memos and Related Records
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_debit_memo_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_debit_memo.htm
fetched_at: 2026-09-04
---

# Create Debit Memos and Related Records

After you identify the additional charges to be paid by your buyer, create debit memos and their related records to make the required adjustments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create debit memos:	

You must have one of these permission sets:

Billing Admin permission set
Billing Operations User permission set
Payment Admin permission set
Payment Operations User permission set
Credit Memo Operations User permission set
NOTE

For Salesforce orgs that are created in Winter ’26, the Debit Memos and Debit Memo Lines tabs are available by default. For Salesforce orgs that are created before Winter ’26, change the tab settings for these objects to Default On.

Create Debit Memos

Create a Debit Memo record for an account that's undercharged.

Before you create debit memos, go to the Object Manager and add all the required values to the Reason Code picklist field on the Debit Memo object. Add values such as LP for late payment charges.

From the App Launcher, find and select Debit Memo.
Click New.
Select the account that you are creating the debit memo for.
Select Draft as the status.
A Debit Memo record can be created only in the Draft status.
Select the reason code for the debit memo.
If necessary, enter a description.
Select the legal entity.
Select the next billing date.
On the target date of the invoice batch run, the invoice batch run picks up all the debit memos that have the next billing date on or before the target date.
Enter an invoice matching reference key or invoice matching reference name.
The specified value along with the default matching group of the debit memo is used to identify an invoice with the same details. The default matching group includes the account, currency, and legal entity of the debit memo.
	
Matching invoice reference key is specified	The specified matching invoice reference key is considered along with the default matching group.
Matching invoice reference name is specified	The specified matching invoice reference name is considered along with the default matching group.
Both fields are specified	The specified matching invoice reference key is considered along with the default matching group.
Neither of the fields is specified	The default matching group is considered.
Save your work.

Create the required debit memo lines for the debit memo.

Create Debit Memo Addresses

Create a debit memo address to specify the billing address and shipping address for the debit memo lines.

Open the debit memo that you want to create the debit memo address for.
Go to the debit memo address related list, and click New.
Enter the address.
Save your work.
Create Debit Memo Lines

Create Debit Memo Line records for an asset, contract, invoice line, or refund. Create the debit memo line from the related list of the Debit Memo record or from the Debit Memo tab.

Open the debit memo.
Go to the debit memo lines related list, and click New.
Enter a name.
Enter the product that you're creating the debit memo line for.
If necessary, enter a description.
Select the start date and end date.
When you don't select a date in these fields, the date when the record is created is used as the default date for the fields.
Enter the charge amount.
This amount appears as the charge amount of the invoice lines, when the debit memo line gets converted into an invoice line.
Select a tax treatment.
If no tax treatment is selected, then the tax treatment of the related product is considered. If the tax treatment isn't found on the product, then the default tax treatment of your Salesforce org is used.
Select the legal entity.
If you don't select a legal entity, then the legal entity of the related debit memo or the default legal entity of your Salesforce org is used.
Select the legal entity accounting period.
Select the reference record.
You can manually enter the ID of an asset, contract, invoice line, or refund that the debit memo line is created for.
Select the debit memo address as the shipping address and billing address.
Save your work.

Go back to the parent debit memo and change the status to Posted. The invoice generation status then automatically changes to Ready for Invoice Generation.

If you manually convert debit memo lines to invoice lines, then post the related invoice and select the Manually Processed check box on the related Debit Memo record. You can also use Invoice Ingestion API to convert them manually.

When you click the Generate Invoices button or schedule an invoice batch run, after all valid billing schedule groups are converted to invoice lines, all valid debit memo lines are converted to invoice lines.

=== ARTICLE: ind.billing_debit_memo_explain.htm ===
---
article_id: ind.billing_debit_memo_explain.htm
title: About Debit Memos
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_debit_memo_explain.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_debit_memo.htm
fetched_at: 2026-09-04
---

# About Debit Memos

A debit memo is issued by a seller to a buyer when the seller wants to levy additional charges to what was already billed or charged. For example, late payment fees, cancellation fees, and so on.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Debit Memo Scenarios

Debit memos are issued in scenarios where a seller must charge an additional amount that a buyer owes. These situations often arise because of:

Billing Errors: If a seller undercharges a customer, then a debit memo is issued to adjust the charge and collect the payment.
Cancellation or Suspension of Services: If services are canceled before they're completely delivered or a recurring subscription is suspended, then a debit memo is issued to bill the cancellation charges or suspension fee.
Late Payment Charges: If a customer misses to pay the outstanding invoice amounts, then a debit memo is issued to charge a late payment fee.
Business Use Case: Issuing a Debit Memo for an Undercharged Invoice

A service provider, Acme Software Innovations Inc., provides a monthly subscription of their analytics platform to their customer, Growth Digital Marketing Pro, for a standard fee of US$500. Because of a data entry error, the invoice for the current month was accidentally generated for only $400, resulting in an undercharge of $100.

In this scenario, Acme Software Innovations Inc. would issue a debit memo to Growth Digital Marketing Pro to correct the undercharge. The debit memo would be for the missing $100, with a single debit memo line for Analytics Platform License adjustment.

For Acme Software Innovations Inc. (Seller), the accounting impact of this transaction is twofold.

Their accounts receivable increases by $100, as they now expect to collect the additional amount.
Their revenue also increases by $100, correcting the previously under recognized revenue for the service provided.

This debit memo makes sure that Acme Software Innovations Inc. have accurate financial records reflecting the true value of the transaction, which maintains transparency and proper financial reconciliation.

=== ARTICLE: ind.billing_dispute_management_assisted_case_creation.htm ===
---
article_id: ind.billing_dispute_management_assisted_case_creation.htm
title: Raise Service Requests on Behalf of the Customer
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_dispute_management_assisted_case_creation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_manage_disputes.htm
fetched_at: 2026-09-04
---

# Raise Service Requests on Behalf of the Customer

Initiate billing disputes or inquiries on behalf of your customer directly from the Billing app.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To raise service requests on behalf of the customer:	
UnifiedCatalogAgentPsl permission set group
UnifiedCatalogAgent permission set
Omnistudio User permission set
Industry Service Excellence permission set
Billing Operations User permission set
Billing Customer Service User permission set

As a one-time setup task, configure the Action Launcher component to add the Billing service catalog.

In the Billing app, navigate to the customer’s account.
Click New Case on the Account record.
Select the appropriate service process template.
Complete the required fields and any supporting documents or linked invoices.
Submit the case.
A new billing case is created and associated with the customer’s account. Billing also records the intake method as Internal.

When you submit the case, your customer gets an email notification and can view the case details and status on the Cases tab of the self-service Billing portal. You can also route cases to specific service reps by setting up case assignment rules.

You can now proceed to resolve the case using the case resolution workflow.

=== ARTICLE: ind.billing_dispute_management_enable.htm ===
---
article_id: ind.billing_dispute_management_enable.htm
title: Set Up Billing Dispute Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_dispute_management_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_manage_disputes.htm
fetched_at: 2026-09-04
---

# Set Up Billing Dispute Management

Track and resolve billing inquiries, service requests, and invoice-related disputes by using Billing Dispute Management.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To install and deploy service process templates:	
UnifiedCatalogAdminPsl permission set group
Unified Catalog Admin permission set
Omnistudio Admin permission set
Billing Admin permission set

To create and customize an Experience Cloud site by using the self-service Billing Portal template:	Billing Admin permission set
From Setup, in the Quick Find box, navigate to these settings and enable access.
In Billing Settings, turn on Manage Billing Disputes and Service Requests.
In Omnistudio Settings, turn on Omnistudio Metadata.
In Context Service Settings, turn on Context Definitions.
In Sharing Settings, specify the level of access to these objects.
OBJECT	DEFAULT INTERNAL ACCESS	DEFAULT EXTERNAL ACCESS
Catalog	Public Read/Write	Public Read Only
Dispute	Public Read/Write	Private
Omni Data Transformation	Public Read/Write	Public Read Only
Omni Process	Public Read/Write	Public Read Only
Product2	Public Read/Write	Public Read Only
Product Component Group	Public Read/Write	Public Read Only
Product Component Group Override	Public Read/Write	Public Read Only
Product Configuration Flow	Public Read/Write	Public Read Only
Product Related Component Override	Public Read/Write	Public Read Only
Service Catalog Request	Public Read/Write	Private
Configure Digital Experiences settings.
From Setup, in the Quick Find box, enter Digital Experiences, and then select Digital Experiences.
Click Settings, and in the Role and User Settings section, enable Allow using standard external profiles for self-registration, user creation, and login.
Create Customer Community users, enable the customer users from contacts, and add permissions.
Create Customer Community Plus users for your Experience Cloud site.
On the account’s contact related list, view or add the contact record for the user that you want to add to a site. When you create a customer user, Salesforce creates a user record in your org with some details pre-populated from the contact record.
On the contact detail page, click the actions dropdown, and then select Enable Customer User.
Add these permissions to the community user.
UnifiedCatalogCommunityUserPsl permission set group
Unified Catalog Community User permission set
Omnistudio User permission set
Billing Experience Cloud User permission set
Repeat the above steps to add multiple users and then refresh the page.
Set up your Self-Service Billing Portal.
Create and publish an Experience Cloud site by using the Self-Service Billing Portal template.
Starting Spring ’26, the new Billing self-service portal tabs are available by default only for newly created portals. If your Salesforce org was created before or upgraded to Spring ‘26, manually add the new Cases and Help Center tabs to the existing self-service billing portal configuration.
Add the Customer Community Plus user to your Experience Cloud site.
In Digital Experiences Settings, navigate to the Sharing Sets section, and create a new sharing set. Add the Customer Community Plus user profile and the Invoice object.
Configure access for the Invoice object.
Refresh the page.
Add dynamic picklist values in the Dispute Type and Dispute Subtype fields of the Dispute object.
In Object Manager, navigate to the Fields & Relationships section of the Dispute object.
Edit these fields to add the dynamic picklist values.
Add Billing Dispute as the picklist value in the Dispute Type field.
Add Incorrect Invoice Charge as the picklist value in the Dispute Subtype field.
Clone the out-of-the-box Billing service process Omniscripts.
From the App Launcher, find and select Omniscripts.
Create a new version of these Omniscripts.
BillingSvcProcessSuspendBilling
BillingSvcProcessUpdateBillToContact
BillingSvcProcessExtendDueDate
BillingSvcProcessInvoiceChargeCorrection
BillingSvcProcessOtherBillingRequests
Install the service process templates by using Unified Catalog.
From the App Launcher, find and select Unified Catalog.
In Templates, select the service process template that you want to install and click Install.
Review the data model and attributes of the installed template.
Continue to click Next until you view the intake form.
Click Open Editor to view the intake form in Omniscript Designer.
Activate the Omniscript.
Save and activate the template.
Repeat the above steps to install each service process template.
After installation, the service process templates are saved as service processes in Unified Catalog.
Organize your service processes in Unified Catalog.
Create a catalog and select Service Process as the catalog type.
Create a catalog category for your catalog.
Add the service processes to the catalog and save your changes. Note the catalog ID as you need it to configure the Help Center page in Experience Builder.
Edit the Help Center page and Unified Catalog component in Experience Builder.
Open the Help Center page and select the Unified Catalog component.
Enter the catalog ID in the RecordId field of the Unified Catalog component.
Preview and publish your site.
Set object permissions for the Customer Community Plus User profile.
In Setup, navigate to the Customer Community Plus User profile.
In the Standard Object Permissions section, enable the View All Fields access for the Omni Data Transformations and Omni Data Transformation Items objects.
Configure the Action Launcher component to add your service catalog.
Edit the Account Record page in the Billing app.
Select Unified Catalog in Action Launcher Configuration.
Search and select your service catalog.
Enter the name of your service catalog Service Catalog or any other appropriate name as the action launcher title.
Save and activate the Action Launcher component.

We recommend that you clone the out-of-the-box Resolve Service Request screen flow. In the cloned screen flow, you can modify the invoice charge correction resolution screen to make the Approved Amount column editable. This configuration helps your customer service reps directly update approved amounts on disputed invoice lines when they resolve invoice charge disputes.

Your dispute management setup is complete. Your billing portal or community user can now raise billing inquiries and disputes that can be resolved by your customer service representatives.

NOTE To resolve any Omniscripts component issues in the Help Center, we recommend that you set the field-level security for Content and Sequence fields of the Omni Process Compilation object.
SEE ALSO
Create an Experience Cloud Site
Create a Sharing Set for Experience Cloud Site Users
Install a service process template
Create a Catalog
Edit Pages and Components in Experience Builder
Enable field-level security
Manage Billing Disputes

=== ARTICLE: ind.billing_dispute_management_resolve_service_requests.htm ===
---
article_id: ind.billing_dispute_management_resolve_service_requests.htm
title: Resolve Billing Service Requests
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_dispute_management_resolve_service_requests.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_manage_disputes.htm
fetched_at: 2026-09-04
---

# Resolve Billing Service Requests

When customers or service reps raise billing service requests or inquiries , Billing creates corresponding cases that are resolved by using the automated resolution actions. For specific service requests such as suspending billing, extending invoice due date, updating billing contact details, or correcting invoice charges, Billing automatically initiates the appropriate resolution associated with the service request. However, for any other billing inquiries that don’t have automated resolution, resolve the cases manually based on the business need and requirements.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To resolve service requests:	
Billing Customer Service User permission set
Unified Catalog Admin permission set
To resolve a case, open the case record on the Cases page.
If you have the case number, you can search the list of open cases for the specific case record. You can also view recent cases for the account on the Recent Billing Cases section to check whether similar cases were raised in the past and gather any historical information.
On the Billing Request tab, review the case details and any supporting documents or linked invoices.
Click Resolve Case, and then select the appropriate action based on the type of your request.
CASE REQUEST TYPE	RESOLUTION ACTION
Request to suspend billing	
Review the suspension and resumption dates, and revise as required, based on your company policies, if any.
Click Suspend Billing and then Finish.

Billing updates the invoice with the revised suspension and resumption dates, and the case is closed.


Request to update bill-to contact	
Review the revised bill-to contact and set it as default, if necessary.
Click Update Bill-to Contact and then Finish.

Billing updates the billing contact details and the case is closed.


Request to extend the invoice due date	
Review the current due date and set a revised due date based on your company policies, if any.
Click Extend Due Date, and then Finish.

Billing updates the invoice with the new due date and the case is closed.


Request to correct invoice charge dispute	
Review the disputed invoice lines in the invoice.
Edit the approved amounts for one or more invoice lines by updating the dispute record, and save your changes.
Select one or more dispute lines that you want to approve to issue a credit memo.
Click Next to submit the approved invoice lines for credit memo application, and then click Finish.

Billing generates a credit memo in Posted status and the case is closed.

Your customer can also view the updated case status on the Cases tab of the self-service Billing portal.

If necessary, you can change the status or priority of the case in the Additional Information section.

You can also use Billing Employee Assistance Agent to understand invoice charges and retrieve billing information.

=== ARTICLE: ind.billing_document_generation_default_invoice_template.htm ===
---
article_id: ind.billing_document_generation_default_invoice_template.htm
title: Default Document Template to Generate Invoice PDF Documents
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_document_generation_default_invoice_template.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_document_generation_batch_and_single.htm
fetched_at: 2026-09-04
---

# Default Document Template to Generate Invoice PDF Documents

After your Billing admin turns on Document Generation for Billing, immediately generate bulk PDF documents for invoices by using the default document template that's preselected.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
NOTE For on-demand, account–specific invoice documents, see Assign an Invoice Document Template to a Billing Profile and Generate a Single Invoice PDF Document.

The field values of the Default Invoice Template document template are derived from:

The Invoice Date, Invoice Number, Due Date, Description, Total Amount, Total Tax, Balance, and Net Credits Applied fields of the Invoice record.
The Billing Address and Shipping Address fields of the Account record.
The Product, Quantity, Unit Price, Tax Amount, and Line Amount fields of the Invoice Line record.
The start and end dates of the invoice line, which determine the billing period.
SEE ALSO
Turn On Invoice PDF Document Generation and Account Statement

=== ARTICLE: ind.billing_document_generation_logo.htm ===
---
article_id: ind.billing_document_generation_logo.htm
title: Generate Invoice PDFs with Your Company Logo
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_document_generation_logo.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_document_generation_batch_and_single.htm
fetched_at: 2026-09-04
---

# Generate Invoice PDFs with Your Company Logo

Automatically add your company logo to the invoice PDF documents by installing Omnistudio packages and uploading the logo to your Salesforce org.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

Document Generation 2.0 supports dynamic image tags, which are used to add the company logo on PDF documents. If you haven't installed Document Generation 2.0 in your Salesforce org, install Omnistudio to use the logo capabilities and upload your company's logo to your Salesforce org.

From the App launcher, find and select Files.
Upload the logo.

Make sure your logo file is in PNG format and follows this file naming convention: Company_Logo.

NOTE Only one logo can be uploaded as a File records. To change the logo, delete the existing logo and add a new logo.

When you generate invoice PDF documents, you see the logo at the top of the PDF document.

SEE ALSO
Dynamic Images in Server-Side Document Generation 2.0

=== ARTICLE: ind.billing_dunning_orchestration_enable.htm ===
---
article_id: ind.billing_dunning_orchestration_enable.htm
title: Set Up Orchestrated Dunning for Collections
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_dunning_orchestration_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_configure_dunning_orchestration.htm
fetched_at: 2026-09-04
---

# Set Up Orchestrated Dunning for Collections

Configure and integrate out-of-the-box Dynamic Revenue Orchestrator templates into Billing to automate the entire dunning lifecycle.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To install and configure the Dynamic Revenue Orchestrator feature and the Dunning Orchestration solution by using Salesforce Go:	Billing Admin permission set
Configure the Dynamic Revenue Orchestrator feature in Salesforce Go. Skip this step if it’s already configured.
From Setup, in the Quick Find box, enter Salesforce Go, and then select Salesforce Go.
Go to the Features tab and filter by Revenue Cloud to view and set up Dynamic Revenue Orchestrator.
Turn on Dynamic Revenue Orchestrator, and then in the Unlock Advanced Functionality section, turn on Future-Dated Steps to configure steps to execute at a future date and time.
To monitor the installation status, in Setup, find and select Jobs, and then click Bulk Data Load Jobs.
The setup can take a few minutes. We recommend that you wait until the configuration is complete before you proceed further.
In Setup, find and select Billing Settings, and then turn on Automate Dunning Orchestration.
This action creates the BillingOrchPlanCtxMapping orchestration plan context mapping record with orchestration type as Billing. The context mapping corresponds to the BillingCollectionPlanContext context definition and maps to the CollectionPlan object.
Install the Dunning Orchestration solution in Salesforce Go.
From Setup, in the Quick Find box, enter Salesforce Go, and then select Salesforce Go.
Go to the Initial Setup tab and filter by Revenue Cloud and Data Pack category.
View and install Dunning Orchestration Solution.
This step can take a few minutes.
The solution installs a dunning orchestration fulfillment workspace and three email templates.

Your Billing Operations User or Collections and Recovery Specialist is now ready to initiate dunning orchestration on your collection plans.

NOTE After it’s installed, you can’t uninstall the Salesforce Go solutions.
SEE ALSO
Turn on Future-Dated Steps

=== ARTICLE: ind.billing_extend_revenue_standard_tax_engine.htm ===
---
article_id: ind.billing_extend_revenue_standard_tax_engine.htm
title: Extend Your Revenue Standard Tax Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_extend_revenue_standard_tax_engine.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_standard_tax_rate.htm
fetched_at: 2026-09-04
---

# Extend Your Revenue Standard Tax Engine

Apply tax rates based on custom attributes, such as product category, customer attributes, or exemption criteria, without writing Apex code. Use a custom metadata type to map billing transaction fields to a cloned Revenue Standard Tax Entries decision table, and persist matched values on invoice and credit memo tax lines.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Configure Custom Metadata Types
Create a custom metadata type that maps billing transaction fields to decision table columns for the Revenue Standard Tax Engine.
Clone the Decision Table
Clone the Revenue Standard Tax Entries decision table and add the custom columns that you use to match tax rates.

=== ARTICLE: ind.billing_extend_tax_interface.htm ===
---
article_id: ind.billing_extend_tax_interface.htm
title: Extend the Revenue Cloud Tax Extension Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_extend_tax_interface.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_partner_or_custom_tax_engine.htm
fetched_at: 2026-09-04
---

# Extend the Revenue Cloud Tax Extension Engine

Enhance the existing tax interface by mapping additional fields for tax callouts. Use custom metadata types to send additional data in tax requests and persist more detailed information from tax responses.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Tax Interface Extension
Handle tax calculation needs that go beyond standard integrations, capture the right data for audits, and adapt to new requirements through configuration instead of custom code.
Configure Your Custom Metadata Types
Create a custom metadata type to house your field mappings. These field mappings are required for all the additional fields you want to include in your tax callouts. Associate your custom metadata type with your tax engine provider so it's aware of the fields used in the request and response.

=== ARTICLE: ind.billing_fgn_exch_realized_gains_losses_use_case.htm ===
---
article_id: ind.billing_fgn_exch_realized_gains_losses_use_case.htm
title: "Example: Automatically Capture Foreign Exchange Realized Gains or Losses"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_fgn_exch_realized_gains_losses_use_case.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_foreign_exchange_realized_gains_and_losses.htm
fetched_at: 2026-09-04
---

# Example: Automatically Capture Foreign Exchange Realized Gains or Losses

Explore an example to understand how general ledger accounts are set up and how dual transaction journals are created when Payments or Credit Memo records are created and applied to the invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Smartbytes Scenario: Initial Setup and Configuration

Smartbytes is a US-based large enterprise company with multiple legal entities. Their Billing admin enables advanced currency management, edits dated conversion rates, turns on the Create Transaction Journals for Transactions, and Create Transaction Journals for Foreign Exchange Gains or Losses features in their Salesforce org. Then, their Accounting admin creates the general ledger accounts for realized gains, realized losses, and account receivables, and sets them as their Salesforce’s org defaults.

Realized Gain General Ledger Account: 01-900-9000 Realized Gain
Realized Losses General Ledger Account: 01-901-9000 Realized Loss
Account Receivable General Ledger Account: 01-100-1001 Accounts Receivable
Foreign Exchange Realized Gain or Loss Calculation

Let's look at a specific transaction to see how foreign exchange realized gains or losses are calculated.

Invoice creation: On invoice date August 27, 2025, Smartbytes creates an invoice for their Indian customer with an invoice's balance of 10,000 INR.

The system automatically converts the balance to the corporate currency (USD) using the conversion rate on the invoice date.

Dated conversion rate on the invoice date: 1 USD = 87.66 INR
Corporate currency equivalent of the balance amount on August 27, 2025: 10,000/97.66 = 114.07 USD

Payment and settlement: On September 3, 2025, a full payment is made for 10,000 INR. When the payment is applied to an invoice, a Payment Line Invoice record is created and the invoice is settled.

Dated conversion rate on the payment's effective date: 1 USD = 88.07 INR
Corporate Currency equivalent of the paid amount on the payment's effective date = 113.54 USD

Foreign exvhange realized gain or loss calculation: The foreign exchange realized gains or losses are calculated by taking the payment's corporate currency value and subtracting the invoice's corporate currency value. The loss recorded for this transaction is 0.53 USD.

Automatic Transaction Journal Creation

As soon as the payment is processed, the corresponding invoice settlement status is updated to Settled. Dual transaction journals are automatically created to record the foreign exchange realized loss of 0.53 USD.

A transaction journal is created for the 01-100-1001 Accounts Receivable account with the realized loss amount as the credit amount.
A transaction journal is created for the 01-901-9000 Realized Loss account with the realized loss amount as the debit amount.

If the calculations result in foreign exchange realized gain, then these two transaction journals are created.

A transaction journal is created for the 01-100-1001 Accounts Receivable account with the realized gain amount as the debit amount.
A transaction journal is created for the 01-900-9000 Realized Gain account with the realized gain amount as the credit amount.

=== ARTICLE: ind.billing_fgn_exch_unrealized_gains_losses_use_case.htm ===
---
article_id: ind.billing_fgn_exch_unrealized_gains_losses_use_case.htm
title: "Example: Automatically Capture Unrealized Foreign Exchange Unrealized Gains or Losses"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_fgn_exch_unrealized_gains_losses_use_case.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entity_accounting_periods_close.htm
fetched_at: 2026-09-04
---

# Example: Automatically Capture Unrealized Foreign Exchange Unrealized Gains or Losses

Explore an example to understand how to a set up general ledger accounts on the Salesforce org's default general ledger accounts and create dual transaction journals and reversal transaction journals to capture unrealized gains or losses amount of the invoices during legal entity accounting period closure.

Smartbytes Scenario: Initial Setup and Configuration

Smartbytes is a US based large enterprise company with multiple legal entities. Their Billing Admin turns on Create Transaction Journals for Transactions, Create Transaction Journals for Foreign Exchange Gains or Losses, enables advanced currency management, and edits dated conversion rates in their Salesforce org. Then, their Accounting Admin creates the general ledger accounts with type as Others for unrealized gains, unrealized losses, and account receivables, and sets the accounts as their Salesforce org's defaults.

Unrealized Gain General Ledger Account: 01-800-8000 Unrealized Gain
Unrealized Losses General Ledger Account: 01-800-8001 Unrealized Loss
Account Receivable General Ledger Account: 01-100-1001 Accounts Receivable
Foreign Exchange Unrealized Gain or Loss Calculation

Let's look at a specific transaction to see how foreign exchange unrealized gains or losses are calculated.

Invoice creation: On invoice date August 27, 2025, Smartbytes creates an invoice for their Indian customer with an invoice's balance of 10,000 INR.

The system automatically converts the balance to the corporate currency (USD) using the conversion rate on the invoice date.

Dated conversion rate on the invoice date: 1 USD = 87.66 INR
Corporate currency equivalent of the balance amount on August 27, 2025 = 114.07 USD

Legal entity accounting period closure: The INR-2025-2026-August1-August31 legal entity accounting period is closed on August 31, 2025.

Dated conversion rate on the end date of the legal entity accounting period: 1 USD = 88.17 INR
Corporate currency equivalent of the balance amount on August 31, 2025 = 113.417 USD

Foreign exchange unrealized gain or loss calculation: The foreign exchange unrealized gains or losses are calculated as the difference between the corporate currency equivalent of the balance amount on August 31, 2025, and the corporate currency equivalent of the balance amount on August 27, 2025. The loss recorded for this transaction is 0.66 USD.

Automatic Transaction Journal Creation

When the legal entity accounting period is closed, dual transaction journals are automatically created to record the foreign exchange unrealized loss of 0.66 USD and dual reversal transaction journals are also created to record the same for the start date of next legal entity accounting period.

A transaction journal is created for the 01-800-8001 Unrealized Loss account with the unrealized loss amount as the debit amount for INR-2025-2026-August1-August31 legal entity accounting period..
A transaction journal is created for the 01-100-1001 Accounts Receivable account with the unrealized loss amount as the credit amount for INR-2025-2026-August1-August31 legal entity accounting period.
A reversal transaction journal is created for the 01-800-8001 Unrealized Loss account with the unrealized loss amount as the credit amount for INR-2025-2026-September1-September30 legal entity accounting period.
A reversal transaction journal is created for the 01-100-1001 Accounts Receivable account with the unrealized loss amount as the debit amount for INR-2025-2026-September1-September30 legal entity accounting period.

=== ARTICLE: ind.billing_field_combination_requirements.htm ===
---
article_id: ind.billing_field_combination_requirements.htm
title: Field Combination Requirements
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_field_combination_requirements.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_frequency_change_flow_impact.htm
fetched_at: 2026-09-04
---

# Field Combination Requirements

The combination of billing frequency, period boundary, period boundary day, and period boundary start month determines billing behavior.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

Identify which period boundary values are supported for each billing frequency.

BILLING FREQUENCY	SUPPORTED PERIOD BOUNDARY	SUPPORTED PERIOD BOUNDARY DAY AND PERIOD BOUNDARY START MONTH
Weekly	Align to Calendar, Anniversary, Day of Period, Last Day of Period	You can set the period boundary day to a number from 1 (Monday) through 7 (Sunday) to choose the day of the week that each billing period starts. You can’t specify the period boundary start month as it doesn’t apply to weekly billing.
Monthly, Annual	Align to Calendar, Anniversary, Day of Period, Last Day of Period	You can only specify period boundary start month when period boundary is day of period. You can’t specify period boundary start month for monthly billing frequency.
Quarterly, Semi-Annual	Anniversary, Day of Period	You can only specify period boundary day and period boundary start month for day of period.

Here are some examples that illustrate how different configurations of billing frequency and period boundaries work.

WEEKLY BILLING ALIGNED TO A SPECIFIC DAY OF THE WEEK

Some businesses bill on a weekly cadence and want each billing period to start on a specific day of the week. Consider an order product with the following configuration.

Billing frequency: Weekly
Period boundary: Day of Period
Period boundary day: 1 (Monday)
Order start date: June 2, 2025 (Monday)

When invoicing runs on June 2, billing generates a weekly invoice for the period from June 2 to June 8. Subsequent invoices cover June 9 to June 15, June 16 to June 22, and so on, with each billing period starting on a Monday. This configuration bills the customer every week, with each period anchored to the same day of the week.

If you set the period boundary as Last Day of Period, then the period boundary day is 7 (Sunday). So, when the invoicing runs on June 2, Billing generates a prorated weekly invoice from June 2 to June 7, and then full period invoices from June 8 to June 14, and so on.

If you set the period boundary as Align to Calendar, the period boundary is set to 1 (Monday), by default. So, Billing generates weekly invoices from Monday, June 2 for the period June 2 to June 8, June 9 to June 15, and so on.

When the period boundary is set to Anniversary, the period boundary day is derived from the start date. If the order start date is June 2, 2025, and is a Monday, then the period boundary day is set to 1 (Monday). Billing then generates weekly invoices every Monday.

QUARTERLY BILLING WITH A TRANSITION MONTH BEFORE THE CYCLE BEGINS

Businesses often need flexibility when a customer’s order begins before the regular billing cycle is scheduled to start. In such cases, you can configure billing to handle a short initial billing period that covers the gap between the order start date and the beginning of the defined cycle. Let’s say an order product has the following configuration.

Billing frequency: Quarterly
Period boundary: Day of period
Period boundary day: 1
Period boundary start month: July
Order start date: June 1, 2025

When invoicing runs with a target date of June 1, 2025, billing generates a monthly invoice for the period from June 1 to June 30, covering the period before the quarterly cycle begins.

When invoicing runs again after July 1, billing generates the first full quarterly invoice for the period from July 1 to September 30.

This configuration supports an initial one-month billing period before transitioning to a recurring quarterly schedule.

ALIGN ANNUAL BILLING TO A CUSTOM START MONTH

Some businesses align annual billing to a fixed month, such as the start of a fiscal year, regardless of when a customer places an order. This setup ensures coverage from the order date while anchoring all future invoices to the chosen billing cycle start. For example, an order is placed on August 1, 2025 and has the following configuration.

Billing frequency: Annual
Period boundary: Day of period
Period boundary day: 1
Period boundary start month: April

When invoicing runs on August 1, billing generates an invoice for the period from August 1, 2025 to March 31, 2026.

When invoicing runs again on April 1, 2026, billing generates the next annual invoice covering the period from April 1, 2026 to March 31, 2027.

This configuration aligns all future billing to start on April 1, even though the order was placed in August.

TERM-BASED PRODUCT WITH SEMIANNUAL BILLING

Some subscriptions follow the customer’s start date instead of aligning to a fixed calendar boundary. With an anniversary-based setup, each billing period is calculated from the original subscription start, creating consistent intervals, such as semiannual or annual. This ensures the customer is always billed for a full term tied to when their service began. A term-based subscription begins on January 15, 2025. The configuration includes:

Billing frequency: Semiannual
Period boundary: Anniversary

When invoicing runs on January 15, an invoice is generated for the period from January 15 to July 14.

Subsequent invoices are generated every 6 months, starting July 15, January 15 (next year), and so on.

This setup ties each billing period directly to the original subscription start date, maintaining consistent semiannual billing.

TERM-DEFINED PRODUCT WITH QUARTERLY BILLING AND A MIDTERM AMENDMENT

In some cases, a subscription may need to handle changes within an active billing term, such as an update to quantity or product configuration. With quarterly billing tied to a fixed day, the system generates standard invoices while also applying prorated adjustments for midterm amendments, maintaining accurate charges within the affected billing period. For example, a term product starts on January 15, 2025 with the following configuration:

Billing frequency: Quarterly
Period boundary: Day of period
Period boundary start month: January
Period boundary start date: 15

The billing frequency is quarterly, and the period boundary is set to day of period with a start date of January 15. Each billing period starts from the 15th of one month to the 14th of the month 3 months later. The first invoice, generated in advance on January 15, covers the period from January 15 to April 14. On February 15, a midterm amendment, such as a quantity change, occurs. At the next invoicing run, Billing calculates a prorated charge for the updated quantity, effective from February 15 to April 14. On April 15, Billing generates the next quarterly invoice, covering the period from April 15 to July 14 and reflecting the amended configuration.

=== ARTICLE: ind.billing_financial_accounting.htm ===
---
article_id: ind.billing_financial_accounting.htm
title: Manage Financial Accounting in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_financial_accounting.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Manage Financial Accounting in Revenue Management

Streamline the financial accounting process for your organization with accounting periods for legal entities, chart of accounts, journal entries for your billing transactions, and by capturing transaction amounts in corporate currency.

Financial Accounting Data Model in Revenue Management
The Financial Accounting data model depicts the objects and their relationships to record and manage the financial accounting process for Invoice, Credit Memo, Payment, and Refund records. This process includes defining accounting periods, setting up a chart of accounts, and creating dual journal entries for your legal entities.
Legal Entities
A legal entity defines how your organization is structured. In Revenue Management, you can create multiple legal entities, which define the billing and tax information for an order product. If you have customers and business segments in different tax locations, use multiple legal entities to govern the use of tax treatments, billing treatments, finance periods, and finance books.
Manage Accounting Periods in Revenue Management
Accounting periods help your company organize and monitor financial performance by defining specific time frames for business reports. Ensure accurate financial reporting and streamlined record-keeping by associating billing transactions to legal entity accounting periods.
Manage Chart of Accounts and Transaction Journals in Revenue Management
Set up a chart of accounts for your legal entities by creating general ledger accounts. Assign appropriate general ledger accounts to transaction journals by setting up general ledger account assignment rules. Automatically generate dual transaction journals based on the configuration for the billing transaction type and criteria in the general ledger account assignment rule.
Foreign Exchange Realized Gains and Losses
Automatically create dual transaction journals for foreign exchange gains or losses when payments and credit memos are created and applied to invoices. The invoices can be fully or partially settled. Foreign exchange gains and losses transaction journals help with income statements during corporate accounting, which ensures accurate measurement of financial performance.
Legal Entity Accounting Periods Closure and Reopening
Close legal entity accounting periods and accounting periods after their duration ends to maintain data integrity. Reopen legal entity accounting periods to reconcile receivable transactions.
Capture Transaction Amounts in Multiple Currencies
Manage multi-currency billing transactions by viewing amounts in transactional currency, functional currency, and corporate currency.

=== ARTICLE: ind.billing_forecast.htm ===
---
article_id: ind.billing_forecast.htm
title: Billing Forecast
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_forecast.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Billing Forecast

Billing Forecast estimates upcoming invoice charges before invoices are created. Review projected charges to understand expected billing and discuss estimates with customers.

REQUIRED EDITIONS

Billing Forecast estimates upcoming invoice charges before invoices are created. Finance and sales teams can review projected charges, including new sales, amendments, renewals, and cancellations, to plan expected billing and discuss estimates with customers.

Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

Billing Forecast doesn’t apply to milestone charges or usage charges.

Turn On Billing Forecast
Turn on Billing Forecast in Billing Settings so your org can generate forecast runs.
Add the Billing Forecast to Data 360
Complete this setup if you want to review forecast data in the Billing Forecast Console, which uses Tableau Next.
Schedule Billing Forecast Runs
Create a billing forecast scheduler to run forecasts once or on a recurring schedule, then filter the billing schedules to include, similar to the invoice scheduler.
Use the Billing Forecast Console
Review projected charges across accounts, charge types, and billing periods, and see how cancellations change upcoming amounts.
Example: Preview Projected Billing Charges
Explore an example that shows how a billing team reviews subscription charges after an amendment and a cancellation.
Recover Billing Schedules
Update Forecast Status from Processing to Pending Forecast or Forecasted so stuck billing schedules can be included in the next forecast run.
Generated Forecast Details
Each Billing Forecast record shows a projected charge from a forecast run, including the related Forecast Batch Run and Forecast Status.

=== ARTICLE: ind.billing_forecast_console.htm ===
---
article_id: ind.billing_forecast_console.htm
title: Use the Billing Forecast Console
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_forecast_console.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_forecast.htm
fetched_at: 2026-09-04
---

# Use the Billing Forecast Console

Review projected charges across accounts, charge types, and billing periods, and see how cancellations change upcoming amounts.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

To view the Billing Forecast Console, you need the Tableau Next Consumer license. Users who create or edit dashboards and semantic models need the Tableau Next Creator license. See Tableau Next Permission Sets and Licenses.

Turn on Billing Forecast and run the forecast scheduler at least once so that forecast data is available. Your org must have Data 360 enabled and connected. See Build your Data Cloud Connection.

After you enable Billing Forecast, deploy the Billing Forecast Console. See Add the Billing Forecast to Data 360.

The console gets Billing Forecast data from Data 360. After a forecast run writes records in your Salesforce org, there can be a delay before those records appear in the dashboard.

From the App Launcher or the Billing app navigation bar, find and select Billing Forecast Console.

Amounts in the dashboard are shown in the Salesforce org default currency. To create a scheduler from the console, click New Billing Forecast Scheduler.

Filters

Use the filters at the top of the dashboard to focus on a specific data.

Date Range: Limit the dashboard to a selected period of projected billing. The default is Next 90 Days.
Legal Entity: Show forecast data for one or more legal entities.
Account: Show forecast data for one or more accounts.
Charge Type: Show forecast data for one or more charge types, such as Recurring or One-Time.
Billing Frequency: Show forecast data for one or more billing frequencies, such as monthly or yearly.
Category: Show forecast data for one or more line categories, such as Original, Amendment, Renewal, or Cancellation.
Summary Cards

The console shows three summary cards.

Total Forecasted Billings: The net projected amount and the number of forecast lines.
Recurring Billing Contribution: The projected amount from termed and evergreen subscriptions, and how many of the total lines are recurring.
Cancellation Impact: The reduction in projected billings from cancellations, and the number of cancelled lines.

The chart shows projected amounts by billing period. Group the amounts by Charge Type, Legal Entity, Currency, or Category. Charge Type is selected by default.

Billing Forecast Details

The details table lists the projected charge lines that make up the dashboard totals for the filters you applied. The heading shows that line count. For each line, you can review billing period, charge type, billing frequency, account, legal entity, quantity, unit price, charge amount, currency, and category.

=== ARTICLE: ind.billing_forecast_data_360.htm ===
---
article_id: ind.billing_forecast_data_360.htm
title: Add the Billing Forecast to Data 360
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_forecast_data_360.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_forecast.htm
fetched_at: 2026-09-04
---

# Add the Billing Forecast to Data 360

Complete this setup if you want to review forecast data in the Billing Forecast Console, which uses Tableau Next.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To update a Data 360 data bundle:	Data Cloud Architect permission set

Before you start, turn on Billing Forecast. Data 360 must be enabled and connected. See Build your Data Cloud Connection.

If you already use Billing Analytics, add the Billing Forecast object to the Advanced Billing Bundle in Data 360, then update the bundle and redeploy Billing Analytics.

If you haven’t installed Billing Analytics yet, deploy the Common Billing Bundle and the Advanced Billing Bundle, then install Billing Analytics. See Deploy the Revenue Management Intelligence Data Kit and Install Revenue Management Intelligence Apps.

From the App Launcher, find and select Data 360.
Click the Data Streams tab.
Open the Salesforce CRM data stream for the Advanced Billing Bundle.
On the objects page, select Billing Forecast.
Click Update.

After the update completes, from the App Launcher or the Billing app navigation bar, find and select Billing Forecast Console.

=== ARTICLE: ind.billing_forecast_details.htm ===
---
article_id: ind.billing_forecast_details.htm
title: Generated Forecast Details
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_forecast_details.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_forecast.htm
fetched_at: 2026-09-04
---

# Generated Forecast Details

Each Billing Forecast record shows a projected charge from a forecast run, including the related Forecast Batch Run and Forecast Status.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

From the App Launcher, find and select Billing Forecast. You can also review related Billing Forecast records from the Billing Schedule, Billing Schedule Group, Invoice Batch Run, Order, Quote, and Account record pages.

Each Billing Forecast record is associated with a Forecast Batch Run, the run that created the record. Open that run from the Billing Forecast record, from the scheduler in Billing Batch Schedulers, or from Invoice Batch Runs.

Forecast Status on the billing schedule shows where the schedule is in the forecast process.

Pending Forecast: The schedule is queued for a forecast run.
Processing: A forecast run is in progress for the schedule.
Forecasted: The schedule reflects current forecast data.
Error: The forecast run failed for the schedule.

Use last forecast run target date on the billing schedule to see the target date from the most recent forecast run that processed the schedule. The next forecast run also includes billing schedules in error, and schedules whose last forecast run target date is earlier than this run’s target date.

If Forecast Status remains Processing after a run fails, see Recover Billing Schedules.

NOTE The Legal Entity Accounting Period field on Billing Forecast isn’t populated automatically. Set the value on the Billing Forecast record, or use your own automation to populate it.

When a forecast run processes a billing schedule, it replaces that schedule’s Billing Forecast records starting with the earliest billing period the run generates. Forecast lines for earlier billed periods stay. Billing schedules that aren’t included in the run, or that have Forecast Status set to Error, keep their existing Billing Forecast records. Running the same forecast twice doesn’t create duplicate records.

If you generate a draft invoice for a charge that’s already in Billing Forecast, Forecast Status doesn’t change, and the existing forecast line stays. That line remains until you post the invoice and a later forecast run processes the billing schedule.

When you post an invoice or change the billing schedule, billing schedule group, billing arrangement, billing profile, or account, the system sets Forecast Status to Pending Forecast. Posted invoices show amounts already billed, and Billing Forecast shows projected amounts. After you post an invoice, the related forecast line can still appear until the next forecast run processes that billing schedule.

=== ARTICLE: ind.billing_forecast_enable.htm ===
---
article_id: ind.billing_forecast_enable.htm
title: Turn On Billing Forecast
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_forecast_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_forecast.htm
fetched_at: 2026-09-04
---

# Turn On Billing Forecast

Turn on Billing Forecast in Billing Settings so your org can generate forecast runs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To turn on Billing Forecast:	Billing Admin permission set
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
Turn on Billing Forecast.

After you turn on Billing Forecast, you can schedule billing forecast runs. To use the Billing Forecast Console, add Billing Forecast to Data 360. See Schedule Billing Forecast Runs and Add the Billing Forecast to Data 360.

=== ARTICLE: ind.billing_forecast_example.htm ===
---
article_id: ind.billing_forecast_example.htm
title: "Example: Preview Projected Billing Charges"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_forecast_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_forecast.htm
fetched_at: 2026-09-04
---

# Example: Preview Projected Billing Charges

Explore an example that shows how a billing team reviews subscription charges after an amendment and a cancellation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

Acme Software Innovations provides these products to Growth Digital Marketing Pro.

Analytics Platform, annual subscription, billed yearly at $12,000
User Licenses, monthly subscription, billed monthly at $200
Support Package, monthly subscription, billed monthly at $50

On April 1, 2026, Growth Digital Marketing Pro amends the order to add licenses, which increases the monthly user licenses charge from $200 to $300. On May 1, 2026, they cancel the support package.

The Acme billing team wants to review projected charges through September 1, 2026, and share the upcoming amounts with the account team before invoices are created. They create a billing forecast scheduler, set the target date to September 1, 2026, and run the forecast.

After the Forecast Batch Run completes, they open the Billing Forecast Console.

Total forecasted billings shows the net projected amount for supported one-time and subscription charges through the target date.
Recurring billing contribution shows the subscription amounts from Analytics Platform and User Licenses.
Cancellation impact shows the reduction from the canceled Support Package.

The billing team uses the Billing Forecast Details section to review the forecasted invoice lines by billing period, charge type, and category. Amendment lines show the April license increase, and cancellation lines show the canceled Support Package. They share the projected charges with the account team so the customer knows what to expect.

=== ARTICLE: ind.billing_forecast_recover.htm ===
---
article_id: ind.billing_forecast_recover.htm
title: Recover Billing Schedules
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_forecast_recover.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_forecast.htm
fetched_at: 2026-09-04
---

# Recover Billing Schedules

Update Forecast Status from Processing to Pending Forecast or Forecasted so stuck billing schedules can be included in the next forecast run.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To recover billing schedules from a failed forecast run:	Recover Forecast Billing Schedules user permission
NOTE Assign the Recover Forecast Billing Schedules user permission in a permission set. It isn’t included in the Billing Admin permission set. See Manage Permission Set Assignments.

When a billing forecast run fails partway through, some billing schedules can remain with Forecast Status set to Processing. A user with the Recover Forecast Billing Schedules user permission can update Forecast Status from Processing to either:

Pending Forecast: The schedule is queued for the next forecast run.
Forecasted: The schedule is marked as already reflecting current forecast data, without running a forecast on it again.

Performing this action changes the forecast status only. It doesn’t change the billing schedule Status used for invoicing.

To recover billing schedules:

Open the billing schedule that has Forecast Status set to Processing.
Change Forecast Status to Pending Forecast or Forecasted.
IMPORTANT Use this recovery step only for billing schedules that remain in progress after a failed or interrupted forecast run. Recover these schedules before starting a new forecast run. Running both at the same time can result in conflicting forecast statuses.

After you recover the schedules, run forecast again if you need updated Billing Forecast records. For a Once run that refreshes matching schedules, select Recalculate All Forecast Lines. See Schedule Billing Forecast Runs.

=== ARTICLE: ind.billing_forecast_schedule.htm ===
---
article_id: ind.billing_forecast_schedule.htm
title: Schedule Billing Forecast Runs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_forecast_schedule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_forecast.htm
fetched_at: 2026-09-04
---

# Schedule Billing Forecast Runs

Create a billing forecast scheduler to run forecasts once or on a recurring schedule, then filter the billing schedules to include, similar to the invoice scheduler.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create and manage forecast schedules:	

Billing Operations User permission set

OR

Billing Admin permission set

Before you start, turn on Billing Forecast. Billing schedules and billing schedule groups must exist for the charges you want to forecast. Add Billing Forecast to Data 360 to view the Billing Forecast Console. See Turn On Billing Forecast and Add the Billing Forecast to Data 360.

From the App Launcher, find and select Billing Batch Schedulers.
Click New Billing Forecast Scheduler.
Enter a scheduler name.
To start a one-time forecast run immediately, select Start run now. Otherwise, configure the start date, start time, time zone, and frequency.
To activate the scheduler, select Active.
Configure the target date, and any other schedule parameters that apply to your run.
For Billing Forecast, you can set a target date up to 5 years. Target date is required for every forecast schedule. Invoice date and date offsets aren’t used for Billing Forecast. These options otherwise work similarly to invoice schedulers. See Understand Invoice Date, Target Date, and Billing Period Count.
Optionally, select Recalculate All Forecast Lines.
This option that’s supported for Once frequency includes filtered billing schedules regardless of forecast status, and recalculates and overwrites existing forecast data. Use it when you need a complete refresh of forecasted data. This option isn’t selected by default, allowing for a faster incremental calculation for billing schedules where Forecast Status is Pending Forecast.
Click Next.
Filter billing schedules by criteria such as billing batch, charge type, legal entity, billing profile, or currency.
NOTE Billing Forecast doesn’t apply to milestone charges or usage charges. Those schedules are excluded even when Recalculate All Forecast Lines is selected.
Click Schedule.

When the forecast run completes, Billing Forecast records are available to review. From the App Launcher, find and select Billing Forecasts, and open a record. Open the related run from the scheduler in Billing Batch Schedulers. Billing Forecast runs also appear in Invoice Batch Runs with Job Type as Forecast. You can also review results in the Billing Forecast Console.

Forecasts cover projected charges for supported one-time and subscription billing schedules. Forecast amounts are calculated before tax and before credit memos or debit memos.

IMPORTANT Don’t run an invoice batch run, a forecast run, or a catch-up bill run while another of these runs is in progress. Overlapping runs can produce inaccurate forecast data. You can still generate invoices while a forecast run is in progress.
NOTE

To check the progress of a forecast run, open the Forecast Batch Run, then click a job ID in the Batch Management Job field. To view all Batch Management jobs, from Setup, find and select Monitor Workflow Services.

=== ARTICLE: ind.billing_foreign_exchange_realized_gains_and_losses.htm ===
---
article_id: ind.billing_foreign_exchange_realized_gains_and_losses.htm
title: Foreign Exchange Realized Gains and Losses
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_foreign_exchange_realized_gains_and_losses.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_financial_accounting.htm
fetched_at: 2026-09-04
---

# Foreign Exchange Realized Gains and Losses

Automatically create dual transaction journals for foreign exchange gains or losses when payments and credit memos are created and applied to invoices. The invoices can be fully or partially settled. Foreign exchange gains and losses transaction journals help with income statements during corporate accounting, which ensures accurate measurement of financial performance.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

To enable Foreign Exchange Gain or Loss calculations, your Billing admin must turn on the Create Transaction Journals for Transactions and Create Transaction Journals for Foreign Exchange Gains or Losses features, and select the realized gain, realized loss, and account receivable general ledger accounts. See Set Up Financial Accounting Features.

WARNING If you've already created transaction journals that record realized foreign exchange gains or losses, don't modify the corporate currency or the dated conversion rates. Changing these impacts the accuracy of existing transaction journals.

The foreign exchange realized gains and losses are calculated based on the difference between the corporate currency conversion rates on the invoice date and the payment's effective date. This difference amount is populated as the debit or credit amounts of the transaction journals. All the amount values for the foreign exchange realized gains and losses transaction journals are in corporate currency.

In case of partial invoice settlement, unrealized gain and loss calculations are calculated during the legal entity accounting period closure. Unrealized and reversal transaction journals are created for the remaining invoice balance. See Legal Entity Accounting Period Closure Procedure

Example: Automatically Capture Foreign Exchange Realized Gains or Losses
Explore an example to understand how general ledger accounts are set up and how dual transaction journals are created when Payments or Credit Memo records are created and applied to the invoices.

=== ARTICLE: ind.billing_frequency_change_flow_impact.htm ===
---
article_id: ind.billing_frequency_change_flow_impact.htm
title: Manage Billing Frequencies
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_frequency_change_flow_impact.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_and_schedule_groups.htm
fetched_at: 2026-09-04
---

# Manage Billing Frequencies

You can set a product’s billing frequency to be different from its pricing frequency. For example, you can bill a customer on an annual basis even if the order or subscription is priced monthly.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Key Terms

Review these terms that define how often a customer is billed and how the billing periods are calculated.

Billing Frequency
The time period that indicates how often an order product is billed. The billing frequency indicates the cadence, such as Weekly, Monthly, Quarterly, Semi-Annual, Annual, or Milestone Plan, that determines how often a billing period item is generated.
Billing Period

The duration or span of time over which an order product is billed.

Billing Period Item
The specific billing information for a billing period. The billing period item record contains billing information, such as the amount, billing period start date, and billing period end date, that’s passed to an invoice line during the invoice batch run.
Billing Term Unit

The unit of time, such as Week, Month, Quarter, Semiannual, or Year, that’s used to measure the billing term. The billing term unit indicates the billing frequency such as Weekly, Monthly, Quarterly, and so on.

Billing Term

The number of billing term units to combine into a single billing period item. The default value is 1 and the maximum value is 1,200.

How Billing Frequency is Carried Into Billing Schedules

When you set the billing frequency on an order product, or change it from the frequency inherited from the product’s pricing, and then activate the order, Billing automatically generates updated billing schedules for the selected billing frequency. These billing schedules are picked up by the invoice batch run to generate invoices.

Considerations

Here are a few things to keep in mind when you change the billing frequency on orders and subscriptions.

On existing orders or active subscriptions, you can change the billing frequency only through a zero-quantity, amend transaction that uses the field amendment subtype, and not during a renew or cancel transaction.
You can’t change the billing frequency from weekly to any other frequency and vice versa.
You can’t change the billing term on the quote line item or order products during amendments, renewals, or cancellations, or when you use Create Standalone Billing Schedules API.
You can’t change the billing term on existing billing schedules.
For an evergreen subscription, consider the following behavior before changing the billing frequency. For example, a product priced at $100 per year when billed monthly prorates to $8.3333 per month, which Billing bills as $8.33. Over 12 months, the total billed amount adds up to $99.96, which is $0.04 less than the $100 original annual price.
About Period Boundaries and Billing Day of Month
You can adjust when billing periods start and how charges are calculated by using flexible date settings that align with your business model and customer preferences. You can use the Period Boundary, Period Boundary Day, and Period Boundary Start Month fields on the order product, to define when billing begins, how billing periods are segmented, and how proration is applied. The period boundary on the order product ‌defines how the billing period is calculated. The Billing Day of the Month field on the Billing Schedule record specifies the day you expect to bill the customer. Together, these fields define how billing periods align with the transaction timeline and how Billing in Revenue Management calculates and groups charges on invoice lines.
Change Billing Frequency on New and Existing Subscriptions
You can update the billing frequency of a subscription at any time, such as by switching from monthly to annual or from annual to monthly. On active subscriptions, you can update the billing frequency from any cadence to any other, such as monthly to annual billing or vice versa, without canceling or recreating the subscription. To achieve this, sales reps make a zero-quantity, field amendment for the asset, to update the billing frequency, Billing automatically prorates the charges and applies the new billing cadence from the effective date.
Field Combination Requirements
The combination of billing frequency, period boundary, period boundary day, and period boundary start month determines billing behavior.

=== ARTICLE: ind.billing_gapless_sequential_numbering.htm ===
---
article_id: ind.billing_gapless_sequential_numbering.htm
title: Gapless Sequential Numbering
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_gapless_sequential_numbering.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_sequential_numbering_for_invoices_configure.htm
fetched_at: 2026-09-04
---

# Gapless Sequential Numbering

For businesses that handle large volumes of transactions, assigning unique, gapless sequential numbers to invoice and credit memo records is essential for legal compliance, auditing, and reconciliation. Manual numbering introduces operational complexity and increases the risk of errors or fraudulent activity. Billing addresses this challenge by automating the assignment of unique identifiers according to the defined sequence policies.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Key Terms

Before you define your sequence policies, review these concepts.

Sequential Numbering
This feature automatically generates unique, formatted, and sequential identifiers for posted invoice and credit memo records.
Sequence Policy
This configuration record is where you define specific rules for how a sequential number is generated and assigned to invoice and credit memo records.
Sequence Pattern
The structure of an invoice or a credit memo number that determines how it appears and includes components such as static text and dynamic placeholders. {SequenceValue} is a mandatory component for the sequence pattern.
Sequence Value
The unique, incrementing value that forms the core of the invoice or credit memo number. The system automatically updates this dynamic placeholder {SequenceValue} in the sequence pattern based on the sequence properties. For example, in the invoice number INV-2025-1001, the sequence value is 1001.
Sequence Pattern Value
This is the final, complete identifier that's generated and assigned to a record after all placeholders in the sequence pattern are resolved. For example, if the sequence pattern is US-{YYYY}-{SequenceValue}, the resolved value is US-2025–1001. The generated sequential pattern value is stamped to an invoice or a credit memo record and stored as the invoice or credit memo number.
Business Use Case: Create Unique Sequential Invoice Numbers

Global Electronics, a company that operates in different countries through multiple legal entities, faced a significant issue with its generic invoice numbers. The finance team couldn’t identify the legal entity responsible for a sale without manually checking customer accounts. This process was slow, prone to errors, and complicated their ability to analyze sales revenue. Additionally, their invoice numbers had unexplained gaps that resulted in traceability issues during auditing.

To eliminate this inefficiency, the company used sequence policies to automatically assign a unique, gapless invoice number based on the legal entity from which the products were sold. For example, an invoice for products sold from the U.S. office now carries a number like USA-2025-1001, indicating the country, year, and sequence value. An invoice for sales from Germany shows a number such as DE-12-2025-2001, indicating the country, month, year, and sequence value. An invoice for sales from India uses a number such as IN/12-02-2025/00123, indicating the country, date, month, year, and sequence value. Each invoice number is tailored to reflect the legal entity code and the specific numbering rules legally mandated for that region.

This automation transformed their financial tracking by eliminating manual data entry and reducing errors. Now, both the finance and sales teams have instant clarity, as the invoice number itself reflects the legal entity responsible for the sale and adheres to the regional legal regulations for invoice bookkeeping and auditing purposes.

=== ARTICLE: ind.billing_general_ledger.htm ===
---
article_id: ind.billing_general_ledger.htm
title: Manage Chart of Accounts and Transaction Journals in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_financial_accounting.htm
fetched_at: 2026-09-04
---

# Manage Chart of Accounts and Transaction Journals in Revenue Management

Set up a chart of accounts for your legal entities by creating general ledger accounts. Assign appropriate general ledger accounts to transaction journals by setting up general ledger account assignment rules. Automatically generate dual transaction journals based on the configuration for the billing transaction type and criteria in the general ledger account assignment rule.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
What are Chart of Accounts and Dual Journal Entries?
Financial accounting provides a structured framework for recording, summarizing, and reporting an organization's financial transactions. The chart of accounts and the principle of dual journal entries are two fundamental concepts of this framework.
Create General Ledger Accounts
Set up a chart of accounts for your organization's legal entities by creating general ledger accounts. Use these accounts to categorize your billing transactions by accounting type and report them in your company’s financial statements.
General Ledger Account Assignment Rules and Related Records
Define rules to assign accurate general ledger accounts to transaction journals and establish criteria for which these rules must apply to. Define multiple journal entry rules for a billing transaction with a specified criteria from a single user interface.
Automatic Creation of Dual Transaction Journals
Automatically generate dual transaction journals, that represent a credit entry and a debit entry, based on the configuration for the transaction type in the General Ledger Account Assignment Rule record. Integrate these transaction journals with any accounting system of your choice to prepare your financial statements such as balance sheets, and profit and loss statements.
Example: Chart of Accounts and Dual Journal Entries
Explore an example to understand how chart of accounts are set up and how dual transaction journals are created based on the configured general ledger accounts and account assignment rules.
Create General Ledger Accounting Period Summary Manually
General Ledger Accounting Period Summary records are automatically created when the Create General Ledger Accounting Period Summary Records for Multiple Currencies or the Create General Ledger Accounting Period Summary Records data processing engine runs during legal entity accounting period closure. You can create them manually as well. General ledger accounting period summaries are created to capture the opening balance and closing balance for general ledger accounts of a legal entity accounting period.

=== ARTICLE: ind.billing_general_ledger_account_assignment_rules_and_criteria.htm ===
---
article_id: ind.billing_general_ledger_account_assignment_rules_and_criteria.htm
title: General Ledger Account Assignment Rules and Related Records
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_account_assignment_rules_and_criteria.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger.htm
fetched_at: 2026-09-04
---

# General Ledger Account Assignment Rules and Related Records

Define rules to assign accurate general ledger accounts to transaction journals and establish criteria for which these rules must apply to. Define multiple journal entry rules for a billing transaction with a specified criteria from a single user interface.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
List of Billing Transactions or Transaction Types

You can create general ledger account assignment rules or general ledger journal entry rules for these objects.

Invoice
Invoice Line
Invoice Line Tax
Credit Memo
Credit Memo Line
Credit Memo Line Tax
Credit Memo Invoice Application
Credit Memo Line Invoice Line
Payment
Payment Line Invoice
Payment Line Invoice Line
Refund records
Refund Line Payment
Debit Memo Line
Create General Ledger Account Assignment Rules
Define general ledger account assignment rules that assign the correct general ledger accounts to credit and debit transaction journal entries.
Define Criteria for Transaction Types
Edit, delete, or define the filter criteria for the transaction type on the general ledger account assignment rule you created.

=== ARTICLE: ind.billing_general_ledger_account_assignment_rules_create.htm ===
---
article_id: ind.billing_general_ledger_account_assignment_rules_create.htm
title: Create General Ledger Account Assignment Rules
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_account_assignment_rules_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger_account_assignment_rules_and_criteria.htm
fetched_at: 2026-09-04
---

# Create General Ledger Account Assignment Rules

Define general ledger account assignment rules that assign the correct general ledger accounts to credit and debit transaction journal entries.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To create general ledger account assignment rules and related records:	Accounts Receivables Admin permission set

Create a general ledger account assignment rule for every combination of legal entity and transaction type.

From the App Launcher, find and select General Ledger Account Assignment Rules.
Click New.
In the Details section (1), enter these details.
Enter a name.
Select the billing transaction that you’re defining the rule for as the transaction type.
Select a legal entity.
If you define multiple general ledger account assignment rules for the same combination of legal entity and transaction type, enter the priority of the rule.
For example, if you have two rules for the same legal entity and Invoice records, enter 1 as the priority for the rule that must be considered first, and 2 as the priority for the rule that must be considered later.

If multiple general ledger account assignment rules have the same priority, all of them are considered to create transaction journals.

Select the status.
Only active general ledger account assignment rules are considered when transaction journals are generated.
Select a transaction amount field, a debit general ledger account, and a credit general ledger account.
If you specify these field values here, you can't define them in the General Ledger Journal Entry Rule section.
NOTE

For General Ledger Account Assignment Rule records created before Summer ’25, the Transaction Amount Field was automatically assigned. From Summer ’25, you can select a Transaction Amount Field value for the existing General Ledger Account Assignment Rule records.

If you edit General Ledger Account Assignment Rule records created before Winter ’26, the Details section shows the specified details.

In the Filter Condition section (2), enter these details.
Select the filter criteria.
To filter the records that meet all the filter conditions, select All (AND).
To filter the records that meet any of the filter conditions, select Any (OR).
To define custom filter criteria, select Custom and enter your custom filter logic. For example, enter (1 AND 2) OR 3).
Define the filter conditions based on the fields from the transaction type of the general ledger account assignment rule.
You can define up to 10 conditions and select both custom and standard fields of the data types: currency, date, percent, picklist, number, lookup, and text.
In the General Ledger Journal Entry Rules section (3), enter these details.
Select a debit general ledger account and a credit general ledger account that have the same legal entity as the General Ledger Account Assignment Rule record.
Select a transaction amount field.
You can create multiple rules for the same transaction amount field, by applying the transaction amount field to different debit and credit general ledger accounts.
Enter a percentage.
When you create multiple rules for the same transaction amount field, the sum of all the percentages must be less than or equal to 100%. The percentage value can have up to five decimals.
Save your work.
Default Transaction Amount Fields
If you don't select a transaction amount field when defining the criteria, the default transaction amount field is populated as the credit or debit amount in transaction journals.
Record Creation for the General Ledger Account Assignment Rule
When billing transactions are Posted, Canceled, Voided, or Processed and they match the defined filter criteria and journal entry rules, then dual transaction journals are created for the defined general ledger accounts for each general ledger journal entry rule.

=== ARTICLE: ind.billing_general_ledger_account_assignment_rules_criteria.htm ===
---
article_id: ind.billing_general_ledger_account_assignment_rules_criteria.htm
title: Define Criteria for Transaction Types
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_account_assignment_rules_criteria.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger_account_assignment_rules_and_criteria.htm
fetched_at: 2026-09-04
---

# Define Criteria for Transaction Types

Edit, delete, or define the filter criteria for the transaction type on the general ledger account assignment rule you created.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To create general ledger account assignment rules and related records:	Accounts Receivables Admin permission set
NOTE Use the Edit button or the Define Criteria button on the General Ledger Account Assignment Rule record to add, edit, or delete filter criteria. When you use the Define Criteria button, you must deactivate the related general ledger account assignment rule to save your changes.
From the App Launcher, find and select General Ledger Account Assignment Rules.
Open the General Ledger Account Assignment Rule record that you want to define the criteria for.
Click Define Criteria.
Select a transaction amount field.

The Transaction Amount Field shows the standard and custom currency fields of the transaction type of the general ledger account assignment rule. The value of the selected currency field is used for the credit or debit amounts when the transaction journals are generated.

For General Ledger Account Assignment Rule records created before Summer ’25, the Transaction Amount Field value wasn't preselected. From Summer ’25, you can select a Transaction Amount Field value for the existing General Ledger Account Assignment Rule records.

Specify the filter criteria.
To filter records that meet all the filter conditions, select All (AND).
To filter records that meet any of the filter conditions, select Any (OR).
To define custom filter criteria, select Custom and enter your custom filter logic. For example, enter (1 AND 2) OR 3).
Define the filter conditions based on the fields from the transaction type of the general ledger account assignment rule.
You can define up to 10 conditions and select both custom and standard fields of the data types: currency, date, percent, picklist, number, lookup, and text.
Save your work.

For each filter criteria, a billing batch filter criteria record is created. When billing transactions that meet the general ledger account assignment rule and filter criteria are created, then dual transaction journals are created.

=== ARTICLE: ind.billing_general_ledger_account_assignment_rules_default_transaction_amount_fields.htm ===
---
article_id: ind.billing_general_ledger_account_assignment_rules_default_transaction_amount_fields.htm
title: Default Transaction Amount Fields
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_account_assignment_rules_default_transaction_amount_fields.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger_account_assignment_rules_create.htm
fetched_at: 2026-09-04
---

# Default Transaction Amount Fields

If you don't select a transaction amount field when defining the criteria, the default transaction amount field is populated as the credit or debit amount in transaction journals.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

These fields are considered as the default transaction amount fields:

TRANSACTION TYPE	TRANSACTION AMOUNT FIELD LABEL
Invoice	Total with Tax
Invoice Line	Charge Amount
Invoice Line Tax	Tax Amount
Credit Memo	Total with Tax
Credit Memo Line	Charge Amount
Credit Memo Line Tax	Tax Amount
Credit Memo Line Invoice Line	Amount
Credit Memo Invoice Application	Amount
Payment	Amount
Payment Line Invoice	Amount
Payment Line Invoice Line	Amount
Refund	Amount
Refund Line Payment	Amount
Debit Memo Line	Charge Amount

=== ARTICLE: ind.billing_general_ledger_accounting_period_summary_create.htm ===
---
article_id: ind.billing_general_ledger_accounting_period_summary_create.htm
title: Create General Ledger Accounting Period Summary Manually
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_accounting_period_summary_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger.htm
fetched_at: 2026-09-04
---

# Create General Ledger Accounting Period Summary Manually

General Ledger Accounting Period Summary records are automatically created when the Create General Ledger Accounting Period Summary Records for Multiple Currencies or the Create General Ledger Accounting Period Summary Records data processing engine runs during legal entity accounting period closure. You can create them manually as well. General ledger accounting period summaries are created to capture the opening balance and closing balance for general ledger accounts of a legal entity accounting period.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create general ledger accounting period summary:	Accounts Receivables Admin permission set

You can manually create a General Ledger Accounting Period Summary records only when the status of the legal entity accounting period is Open. You can create a general ledger accounting period summary for every combination of general ledger account and legal entity accounting period.

IMPORTANT

For Salesforce orgs that are created in Winter ’26, the General Ledger Accounting Period Summaries tab is available by default. For Salesforce orgs that are created before Winter ’26, change the tab settings for this object to Default On.

From the App Launcher, find and select General Ledger Accounting Period Summaries.
Click New.
Select a legal entity accounting period.
Select the general ledger account that you want to calculate the balances for.
Enter the total debit amount.
Enter the total credit amount.
Enter the opening balance amount.
Save your work.

The closing balance amount for the general ledger accounting period summary is automatically derived based on the type of the general ledger account. You can edit the general ledger accounting period summary when the status of the related legal entity accounting period is Pending Closure, Opened, or Reopened.

NOTE The Total Debit Amount, Total Credit Amount, Opening Balance Amount, and Closing Balance Amount fields of manually created General Ledger Accounting Period records are updated automatically when their related legal entity accounting period is closed.
SEE ALSO
DPE: Create General Ledger Accounting Period Summary Records for Multiple Currencies

=== ARTICLE: ind.billing_general_ledger_accounts_create.htm ===
---
article_id: ind.billing_general_ledger_accounts_create.htm
title: Create General Ledger Accounts
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_accounts_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger.htm
fetched_at: 2026-09-04
---

# Create General Ledger Accounts

Set up a chart of accounts for your organization's legal entities by creating general ledger accounts. Use these accounts to categorize your billing transactions by accounting type and report them in your company’s financial statements.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create general ledger accounts:	Accounts Receivables Admin permission set
IMPORTANT

Starting Winter ’26, the General Ledger Account object has a new Type field. For General Ledger Account records created before Winter ’26, there's no Type value. To calculate opening and closing balances for general ledger accounts during the closure of legal entity accounting periods, manually select the Type value for existing records.

From the App Launcher, find and select General Ledger Accounts.
Click New.
Enter an accounting name.
Enter a unique accounting code.
Enter the name of the financial statement that this general ledger account contributes to. For example, you can enter Income Statement or Balance Sheet.
If necessary, enter a description.
Select a legal entity.
Select the type for the accounting code that you entered.
From Winter ’26, use the Type field instead of Accounting Type field. The opening and closing balance amounts are calculated for the general ledger accounts based on the Type value when the legal entity accounting period is closed.
Save your work.

The autogenerated name of the general ledger account is a combination of the specified accounting code and name.

After you create general ledger accounts, create general ledger account assignment rules to assign the correct general ledger accounts to transaction journals.

=== ARTICLE: ind.billing_general_ledger_accounts_explain.htm ===
---
article_id: ind.billing_general_ledger_accounts_explain.htm
title: What are Chart of Accounts and Dual Journal Entries?
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_accounts_explain.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger.htm
fetched_at: 2026-09-04
---

# What are Chart of Accounts and Dual Journal Entries?

Financial accounting provides a structured framework for recording, summarizing, and reporting an organization's financial transactions. The chart of accounts and the principle of dual journal entries are two fundamental concepts of this framework.

What are the Chart of Accounts (COA)?

The Chart of Accounts (COA) is a classified and organized list of all financial accounts an organization uses, acting as a comprehensive directory for tracking every financial item. Each account receives a unique number and name, enabling systematic data categorization and retrieval. Typically, the COA is structured around the five core financial statement account types: Assets, Liabilities, Equity, Revenues, and Expenses. This foundational structure is crucial for providing a consistent way to categorize transactions, ensure accurate financial reporting and analysis, support budgeting and compliance, and enable the automation of accounting processes.

What are Dual Journal Entries (Double-Entry System)?

The dual journal entry system is the foundational principle for recording financial transactions, ensuring every event impacts at least two accounts with equal debits and credits. Debits always appear on the left side of a T-account, while credits are on the right. An account's balance dictates how debits or credits affect it. For instance, assets and expenses increase with debits, whereas liabilities, equity, and revenues increase with credits. All these movements are initially documented in a journal entry.

Dual journal entries are vital for several reasons, starting with maintaining the accounting equation's balance. This system provides a critical self-checking mechanism, instantly highlighting errors if total debits and credits don't match. It also offers a comprehensive view of a transaction's financial impact, detailing both the source and destination of value. Furthermore, these entries directly feed into the general ledger and financial statements, ensuring reporting accuracy. Ultimately, the dual journal entry system creates an indispensable audit trail for internal control, external audits, and regulatory compliance.

=== ARTICLE: ind.billing_general_ledger_results.htm ===
---
article_id: ind.billing_general_ledger_results.htm
title: Automatic Creation of Dual Transaction Journals
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_results.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger.htm
fetched_at: 2026-09-04
---

# Automatic Creation of Dual Transaction Journals

Automatically generate dual transaction journals, that represent a credit entry and a debit entry, based on the configuration for the transaction type in the General Ledger Account Assignment Rule record. Integrate these transaction journals with any accounting system of your choice to prepare your financial statements such as balance sheets, and profit and loss statements.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

After your Accounts Receivables admin creates general ledger accounts and assignment rules, and your Billing admin enables the Create Transaction Journals for Transactions feature, the system automatically creates transaction journals in these scenarios:

BILLING TRANSACTION	TRANSACTION JOURNALS CREATED WHEN
Invoice, Invoice Line, and Invoice Line Tax	A Invoice record's status changes to Posted, Voided, or Canceled
Credit Memo, Credit Memo Line, and Credit Memo Line Tax	A Credit Memo record's status changes to Posted, Voided, or Canceled
Credit Memo Invoice Application and Credit Memo Line Invoice Line	After these records are created
Payment	A Payment record's status changes to Processed
Payment Line Invoice and Payment Line Invoice Line	After these records are created
Refund	A Refund record's status changes to Processed
Refund Line Payment	After these records are created
Debit Memo Line	After these records are created
NOTE Your Accounts Receivable Admin can create General Ledger Account and General Ledger Account Assignment Rule records even when the Create Transaction Journals for Transactions toggle is disabled.

=== ARTICLE: ind.billing_general_ledger_usecase.htm ===
---
article_id: ind.billing_general_ledger_usecase.htm
title: "Example: Chart of Accounts and Dual Journal Entries"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_general_ledger_usecase.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger.htm
fetched_at: 2026-09-04
---

# Example: Chart of Accounts and Dual Journal Entries

Explore an example to understand how chart of accounts are set up and how dual transaction journals are created based on the configured general ledger accounts and account assignment rules.

Chart of Accounts

SmartBytes is a large enterprise company with multiple legal entities. Their Accounting admin creates general ledger accounts for all legal entities, and then creates a list view similar to a chart of accounts for each legal entity.

Notice that the admin defines the accounting codes clearly to easily differentiate the general ledger accounts.

Dual Transaction Journals

SmartBytes provides high-tech services to their customers in Europe. Their accounting team wants to create transaction journals automatically as soon as each ‌invoice line is posted, for these rules:

Recognize 80% of the charge amount towards accounts receivable, and the remaining 20% towards commissions.
Recognize 100% of tax amount towards sales tax liabilities.

To achieve this, the Billing admin enables the Create Transaction Journals for Transactions feature and the Accounts Receivables admin configures a general ledger account assignment rule with filter criteria and general ledger journal entry rules.

The Accounts Receivables admin configures the rule with these details.

Transaction Type: Invoice Line
Legal Entity: Europe
Priority: 1

To apply this rule, the admin defines these filter criteria.

Product: Software
Invoice Status: Posted

To use the charge amount for transaction journals, the admin defines these general ledger journal entry rules with a percentage split of 80 and 20.

General Ledger Journal Entry Rule 1:
Debit General Ledger Account: 01-100-1002 Accounts Receivable
Credit General Ledger Account: 01-200-2001 Deferred Revenue
Transaction Amount Field: Charge Amount
Percentage: 80
General Ledger Journal Entry Rule 2:
Debit General Ledger Account: 01-100-1012 Commissions
Credit General Ledger Account: 01-200-2001 Deferred Revenue
Transaction Amount Field: Charge Amount
Percentage: 20

To use the tax amount for transaction journals, the admin defines another general ledger journal entry rule.

General Ledger Journal Entry Rule 3:

Debit General Ledger Account: 01-100-1002 Accounts Receivable
Credit General Ledger Account: 01-200-2010 Sales Tax Liabilities
Transaction Amount Field: Tax Amount
Percentage: 100

When the general ledger account assignment rule is activated, one General Ledger Account Assignment Rule record, two Billing Batch Filter Criteria records, and three General Ledger Journal Entry Rule records are created immediately.

As soon as invoice lines are posted, four transaction journals are created based on the charge amount and two transaction journals are created based on the tax amount for each invoice line.

A transaction journal is created for the 01-100-1002 Accounts Receivable account with 80% of invoice’s charge amount as the debit amount.
A transaction journal is created for the 01-200-2001 Deferred Revenue account with 80% of invoice’s charge amount as the credit amount.
A transaction journal is created for the 01-100-1012 Commissions account with 20% of invoice’s charge amount as the debit amount.
A transaction journal is created for the 01-200-2001 Deferred Revenue account with 20% of invoice’s charge amount as the credit amount.
A transaction journal is created for the 01-100-1002 Accounts Receivable account with 100% of invoice’s tax amount as the debit amount.
A transaction journal is created for the 01-200-2010 Sales Tax Liabilities account with 100% of invoice’s total tax amount as the credit amount.
SEE ALSO
Create General Ledger Account Assignment Rules
Set Up Financial Accounting Features

=== ARTICLE: ind.billing_generate_pay_now_payment_links_for_business_accounts.htm ===
---
article_id: ind.billing_generate_pay_now_payment_links_for_business_accounts.htm
title: Generate Pay Now Links for Business Accounts
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_generate_pay_now_payment_links_for_business_accounts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_salesforce_payments_features.htm
fetched_at: 2026-09-04
---

# Generate Pay Now Links for Business Accounts

Collect invoice payments against the correct business account by generating Pay Now links. Your customers pay as a guest with their preferred payment method and can save it for future use.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To generate Pay Now payments links and associate payments with business accounts:	Payment Admin permission set
From the App Launcher, find and select Stores.
Set up a new Pay Now store or select an existing one.
Click Settings, and select Store.
Click Buyer Access..
Turn off Self-Registration.
From Setup, in the Quick Find box, enter Flows, and then select Flows.
Click Generate Payment Link.
Click Save As New Flow and name the flow Generate Payment Link V2.
In the With Products or Predefined Amount Link Type? Decision element, , delete the With Products outcome and all its elements one by one. To select and delete multiple elements at after, switch to Free-Form layout, click Drag to select, select the elements, and press Delete. Delete the With Products outcome only if your org does not have a Salesforce Commerce license.

Delete the With Products outcome only if your org doesn’t have a Salesforce Commerce license.

In the Predefined Amount branch, click the Predefined Amount Payment Link Create Records element.
In the Set Field Values for the Payment Link panel, click Add Field and add these fields.
FIELD	VALUE
Account ID	The business account ID from your data source
Is Business Account Payment	True
NOTE To set the Account ID value dynamically, use a Get Records element in the flow to get the business account ID from your data source. For example, if you’re running this flow from an invoice record page, get the account ID from the invoice record and pass it to this field.
In the Toolbox, expand the Formulas section and delete the Single_Use_Or_Multi_Use formula to avoid an activation error.
Save and activate the flow.

When your customer completes the payment, they can select Save this payment method for future use to save the payment method to the business account.

NOTE To run the flow and generate a payment link, see Generate a Pay Now Payment Link. To add the Generate Payment Link V2 flow as an action button on a record page so that you can generate payment links directly from any record, see Add a Payment Link to a Salesforce Record.

=== ARTICLE: ind.billing_generate_single_payment_schedule.htm ===
---
article_id: ind.billing_generate_single_payment_schedule.htm
title: Generate a Single Payment Schedule for Multiple Invoices of an Account
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_generate_single_payment_schedule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments_consolidate_invoices.htm
fetched_at: 2026-09-04
---

# Generate a Single Payment Schedule for Multiple Invoices of an Account

To consolidate payment schedules for an account’s invoices, configure the payment schedule treatment, set the grouping source as Account, and add a due date window.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Salesforce Payments feature is available with the Revenue Management Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Management Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.

Confirm that payment schedule treatments are configured in your Salesforce org. Verify that the invoices you want to consolidate use the same currency and saved payment method.

From the App Launcher, find and select Payment Schedule Treatment.
Select Account as the grouping source to group the invoices by account.
The default value is Invoice, which creates one payment schedule and payment schedule item per invoice.
Enter the number of days to use as the due date window.
Billing calculates each invoice’s due date as the invoice date plus the payment term period. Invoices whose due dates fall within this range are grouped together.
Save your changes.

When you post invoices for the account, Billing automatically evaluates them against the consolidation criteria and creates a consolidated payment schedule for the invoices that qualify the grouping criteria. The total amount on the payment schedule is the sum of all invoice amounts in the grouped invoices. The target payment processing date is the earliest due date among all invoices in the group.

=== ARTICLE: ind.billing_gl_account_assignment_rules_create_result.htm ===
---
article_id: ind.billing_gl_account_assignment_rules_create_result.htm
title: Record Creation for the General Ledger Account Assignment Rule
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_gl_account_assignment_rules_create_result.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_general_ledger_account_assignment_rules_create.htm
fetched_at: 2026-09-04
---

# Record Creation for the General Ledger Account Assignment Rule

When billing transactions are Posted, Canceled, Voided, or Processed and they match the defined filter criteria and journal entry rules, then dual transaction journals are created for the defined general ledger accounts for each general ledger journal entry rule.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

The debit general ledger account is populated for the debit transaction journal entry, and the credit general ledger account is populated for the credit transaction journal entry. See Automatic Creation of Dual Transaction Journals.

If multiple general ledger journal entry rules apply to the same transaction type, a corresponding number of transaction journals are generated. For example, if two general ledger journal entry rules are defined for a single transaction type, four transaction journals are created.

The table specifies the records that are created based on the sections filled.

SECTIONS	RESULT
Details section	
One General Ledger Account Assignment Rule record is created immediately.
Dual transaction journals are created when billing transactions that meet the rule are created for an active general ledger account assignment rule.

Details and Filter Criteria sections	
One General Ledger Account Assignment Rule record is created.
One Billing Batch Filter Criteria record for each filter criterion is created.
Dual transaction journals are created when billing transactions that meet the rule are created for an active general ledger account assignment rule.

Details and General Ledger Journal Entry Rules sections	
One General Ledger Account Assignment Rule record is created immediately.
One General Ledger Journal Entry Rule record is created for each row.
Dual transaction journals are created when billing transactions that meet the rule are created for an active general ledger account assignment rule.

Details, Filter Criteria, and General Ledger Journal Entry Rules sections	
One General Ledger Account Assignment Rule record is created immediately.
One Billing Batch Filter Criteria record is created for each filter criterion.
One General Ledger Journal Entry Rule record is created for each row.
Dual transaction journals are created when billing transactions that meet the rule are created for an active general ledger account assignment rule.
NOTE If you clone a general ledger account assignment rule, the filter criteria and general ledger journal entry rule sections aren't cloned.

=== ARTICLE: ind.billing_guided_setup.htm ===
---
article_id: ind.billing_guided_setup.htm
title: Guided Setup for Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_guided_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup.htm
fetched_at: 2026-09-04
---

# Guided Setup for Billing

Admins can use the Billing Guided Setup for a ‌step-by-step guidance to complete key tasks that are required to set up Billing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


The Billing Advanced Features setup assistant and the Payment Configurations setup assistant are available only with the the Revenue Management Billing license. Contact your Salesforce account executive for more information.

All the other setup assistants are available with the Revenue Management Advanced license or the Revenue Management Billing license.

How It Works

The guided experience is structured to help Billing admins complete each step sequentially, ensuring that the Billing setup is accurate and fully operational. The guided setup includes these setup assistants:

Billing Prerequisites—Set up billing users, assign relevant permission sets, and define billing rules for your products. This step makes sure that authorized personnel manage the billing operations according to clearly defined rules, which boosts both security and accuracy.
Tax Configurations—Set up the tax engine and configure tax policies to ensure accurate tax calculations and compliance with regional regulations.
Invoice Configurations—Schedule and manage invoice runs to streamline the invoicing process.
Accounting Configurations—Streamline the accounting process for your billing transactions by creating accounting periods and legal entity accounting periods.
Currency Conversion Configurations—View transaction amounts not only in the transactional currency but also in your corporate currency. Enable multiple currencies and Advanced Currency Management. Then, turn on the Billing feature to convert and store transaction amounts in your corporate currency.
Billing Advanced Features—Turn on the generation and email delivery of invoice documents. Manage the document template and email template that are used to generate and email invoice documents. You can also set up a chart of accounts for your legal entities, assign appropriate general ledger accounts to transaction journals, and automatically create dual transaction journals for your billing transactions.
Payment Configurations—Set up payment processing for your billing transactions. Configure native payment gateways, payment schedule policies, payment schedules, and related payment records. Then, schedule payment batch runs to process payments and apply them to invoices or invoice lines.
NOTE

For Salesforce orgs that are created in Winter ’26, the Configure Payment Gateways button in Step 7: Payment Configurations of the Billing Guided Setup, which redirects users to the Payment Gateway Configuration tab, is available by default. For Salesforce orgs that are created before Winter ’26, the Payment Gateway Configuration tab isn’t available by default. To fix this issue, change the settings of the Payment Gateway Configuration tab to Default On.

How to Do This

From Setup, enter Billing Guided Setup in the Quick Find box, and then select the required setup assistant.

SEE ALSO
Assign Permissions to Access Billing Features
Define Billing Policies and Billability Rules
Tax Calculation for Invoices
Automated Invoice Generation with Invoice Batch Runs
Manage Accounting Periods in Revenue Management
Capture Transaction Amounts in Multiple Currencies
Turn On Invoice PDF Document Generation and Account Statement
Turn On Email Delivery of Invoices
Manage Chart of Accounts and Transaction Journals in Revenue Management
Process Payments and Issue Refunds in Revenue Management

=== ARTICLE: ind.billing_initiate_dunning_orchestration.htm ===
---
article_id: ind.billing_initiate_dunning_orchestration.htm
title: Initiate and Monitor Dunning Orchestration
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_initiate_dunning_orchestration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_configure_dunning_orchestration.htm
fetched_at: 2026-09-04
---

# Initiate and Monitor Dunning Orchestration

With the dunning orchestration solution set up and enabled on the Billing Settings page, you can initiate automated dunning on your collection plans.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Create a collection plan and add the required collection plan items.
Make sure that the collection plan has the due date, risk profile, accurate contact information, and includes at least one fulfillment workspace with usage type as Billing.
On the collection plan record, click Initiate Dunning Orchestration.

This action creates an orchestration plan with an In Progress status and triggers an automated task. The customer receives an email notification detailing their upcoming invoices.

When you initiate dunning orchestration, the orchestration plan shows the status of each step based on the collection plan’s milestones. You can check which steps are in waiting status before the due date or when the next milestone is reached. You can also check whether reminder emails have been sent to the customers, and if any manual escalation task has been assigned.

NOTE If the Initiate Dunning Orchestration quick action button isn’t available, add it by editing the Collection Plan object’s page layout.

=== ARTICLE: ind.billing_invc_document_delivery_for_invc_btch_runs.htm ===
---
article_id: ind.billing_invc_document_delivery_for_invc_btch_runs.htm
title: Send Invoice Emails in Bulk from Invoice Batch Runs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invc_document_delivery_for_invc_btch_runs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_pdf_document_delivery_through_email.htm
fetched_at: 2026-09-04
---

# Send Invoice Emails in Bulk from Invoice Batch Runs

After an invoice batch run completes and the invoice PDF documents are generated for the posted invoices of the invoice batch run, send invoice emails in bulk to your customers who opted for invoice delivery through email. Attach invoice PDF documents to the emails based on the selected preferences.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To send invoice emails from an Invoice Batch Runs record:	

Billing Admin permission set

OR

Billing Operations User permission set

Before you send invoice emails from Invoice Batch Run records, you and your Billing Admin must define the invoice email delivery configuration and preferences.

Open the completed invoice batch run that you want to send emails for.
Click Email Invoices.

When you click Email Invoices, the system first looks for email preferences in this sequence.

To track the status of the invoice email delivery, view the Last Email Dispatch Status field on the Invoice record. You can also track the emails in the activity timeline on the Invoice record's Details page.

When an email delivery fails because of these reasons, a Revenue Transaction Error Log record is created.

Exceeded the daily email limit.
Missing email address on the invoice's Bill to Contact record.
Presence of merge fields other than the invoice merge fields on the customized email template.

=== ARTICLE: ind.billing_invoice_aging.htm ===
---
article_id: ind.billing_invoice_aging.htm
title: Invoice Aging Summaries on Accounts and Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_aging.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Invoice Aging Summaries on Accounts and Orders

See an aging summary of account invoices so that sales reps and accounts receivable teams can prioritize collections without opening each invoice. The Invoice Aging for Account component shows invoice counts, overdue invoices, aging buckets, and average and maximum invoice age on Account and Order pages.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

The Invoice Aging for Account component shows an aging summary of account invoices so that sales reps and accounts receivable teams can identify overdue invoices without reviewing individual records. To view the summary, you need the Billing Admin or Billing Operations User permission set. Your Salesforce admin adds the component in Lightning App Builder. See Add Invoice Aging for Account to an Account or Order Page.

The component is available on Account and Order record pages. On an Order page, it shows aging data for the associated account. The component includes:

Total Invoices: Total count of invoices.
Open Invoices: Count of unsettled invoices.
Overdue Invoices: Count of past-due invoices.
Aging Breakdown: A bar chart that groups open invoices into four aging buckets based on invoice date.
Average Invoice Age and Maximum Invoice Age: Measured in days.
Aging Buckets

By default, aging buckets use 30-day increments: less than 30 days, 30 to 60 days, 60 to 90 days, and more than 90 days. Your Salesforce admin can change the bucket duration to match your business requirements.

=== ARTICLE: ind.billing_invoice_aging_component.htm ===
---
article_id: ind.billing_invoice_aging_component.htm
title: Add Invoice Aging for Account to an Account or Order Page
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_aging_component.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Add Invoice Aging for Account to an Account or Order Page

Add the Invoice Aging for Account component to an Account or Order page in Lightning App Builder. Sales reps and accounts receivable teams then see overdue invoices, aging buckets, and average invoice age without opening individual invoice records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To add the Invoice Aging for Account component:	Customize Application
To view invoice aging summaries:	

Billing Admin permission set

OR

Billing Operations User permission set

The Invoice Aging for Account component shows an aging summary of account invoices so that sales reps and accounts receivable teams can prioritize collections. On an Order page, the component shows aging data for the associated account. See Invoice Aging Summaries on Accounts and Orders.

Open an Account or Order record.
From Setup, select Edit Page.
From the Lightning App Builder components palette, drag Invoice Aging for Account onto the page canvas.
Save your changes, then activate the page.
To change the bucket duration, select Customize Bucket Size from the actions menu on the Invoice Aging for Account component, enter a value in the Days per Bucket field, and then save your changes.

=== ARTICLE: ind.billing_invoice_batch_run.htm ===
---
article_id: ind.billing_invoice_batch_run.htm
title: Invoice Batch Run Process
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_batch_run.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_automate_invoice_generation.htm
fetched_at: 2026-09-04
---

# Invoice Batch Run Process

Invoice batch runs stream invoices by processing billing schedules in parallel. Track each stage of the invoice batch run to monitor progress and status.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Job Types

Billing Batch Schedulers support Invoice, Catch-Up Bill Run, and Forecast job types. The job type determines whether the run generates invoices, advances billing schedules without invoicing, or creates forecast data.

Invoice—Generates invoices for selected billing schedules. The run is an invoice batch run. See Generate Invoices Automatically Based on Billing Schedules.
Catch-Up Bill Run—Advances billing schedules without generating invoices. See Catch-Up Bill Runs.
Forecast—Creates projected billing forecast data. The run is labeled Forecast Batch Run. See Billing Forecast.

For target date, billing period count, and day-of-month options used when selecting schedules, see Understand Invoice Date, Target Date, and Billing Period Count.

How Invoice Batch Runs Generate Invoices

Invoice batch runs use the Batch Management Service to process billing schedules and generate invoices in parallel. You can start reviewing, sending, and collecting payments on invoices as they’re generated, without waiting for the entire batch to complete.

From the App Launcher, find and select Invoice Batch Runs, and then open the relevant record. To view the related Invoice Batch Draft to Posted Run or Invoice Batch Run Recovery records, go to the Related tab.

To check the overall status and stage of an invoice batch run, check the status subtype on the Invoice Batch Run record. See Status Subtype of Invoice Batch Runs.

To monitor granular progress, select the job ID in the Batch Management Job field to open the corresponding Batch Management Job record. You can view real-time progress, processing status, and any errors. To view the status of all Batch Management jobs, from Setup, find and select Monitor Workflow Services.

The batch management service processes invoice batch runs in these stages.

Identifies billing schedules that meet the criteria defined in the invoice batch run scheduler, such as the next billing date and billing frequency. Each eligible billing schedule is assigned a grouping key
Processes billing schedules simultaneously across multiple threads. Each grouping key is processed independently, so completed invoices are available for review as soon as they're generated
Calculates estimated taxes for draft invoices and actual taxes for posted invoices using the configured tax engine
Updates the amounts and billing dates on associated billing schedules and billing schedule groups in alignment with the generated invoices, to prepare the data for the next billing cycle
Updates the invoice batch run record with a summary of the completed run, including the total number of invoices generated, any failures, and the overall status
Status of Invoice Batch Runs

If an invoice batch run completes successfully, its status changes to Completed. If any errors occur during processing, its status changes to Failed.

Status Subtype of Invoice Batch Runs

To monitor and troubleshoot an invoice batch run, the Billing Operations user can check its status subtype. The status subtype provides visibility into each stage of the invoice batch run. This field isn’t available by default and can be added from the Invoice Batch run object’s page layout settings.

Billing Schedules Filtering Started—The invoice run is preparing to identify the billing schedules to include for invoice generation.
Billing Schedules Filtering In Progress—The invoice run is identifying the billing schedules to include for invoice generation.
Billing Schedules Filtering Completed—The invoice run has identified the billing schedules to include for invoice generation.
Invoice Generation Started—The process of generating invoices has started.
Invoice Generation In Progress—The invoice run is generating invoices for the identified billing schedules.
Invoice Generation Completed—The invoice run has finished generating invoices for the identified billing schedules.
Invoice Generation Summarization In Progress—The summarization of the generated invoices is in progress.
Completed—The invoice batch run has completed successfully. This corresponds to the Completed status of the invoice batch run.
Failed—The invoice batch run has failed.
NOTE Canceling in-flight batch management jobs isn't supported and results in inaccurate data summarization on the Invoice Batch Run record.

In the Invoice Batch Run records, the billing schedule summary is available on the Details tab. If the invoice batch run processes multiple currencies or a currency different from your Salesforce org’s default currency, the total invoiced amount and total draft invoice amount can’t be summarized.

Target Date Offset Limit

By default, the maximum target date for an invoice batch run is 12 months from the current date. If you schedule a batch run with a target date offset greater than 12 months, you receive an error. This limit is an org-level configuration.

Failed Invoice Batch Runs

Review the generated invoices in the Invoices related list. If the invoice generation fails, check the Revenue Transaction Error Logs related list on the Invoice Batch Run records. The log’s Error Message field shows the reason for the failure.

SEE ALSO
Data Processing Engine
Revenue Cloud Developer Guide: InvoiceBatchRun
Monitor Your Batch Jobs

=== ARTICLE: ind.billing_invoice_batch_run_example.htm ===
---
article_id: ind.billing_invoice_batch_run_example.htm
title: "Examples: Invoice Batch Run Frequencies"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_batch_run_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_automate_invoice_generation.htm
fetched_at: 2026-09-04
---

# Examples: Invoice Batch Run Frequencies

Explore examples to understand how to schedule invoice batch runs based on your requirements.

Weekly Invoice Schedule

Cumulus Cloud Corporation operates in an industry that requires frequent billing cycles to maintain cash flow and minimize outstanding payments. Weekly invoicing ensures timely processing, reduces the risk of delays, and enhances financial tracking. Invoices are initially set to draft status for internal review before finalization, ensuring accuracy. The company generates invoices every Monday to cover the previous week's charges. The company configures invoice runs by using these values.

Invoice Status: Draft (for internal review to ensure accuracy)
Frequency: Weekly every Monday
End Date: Dec 31, 2025
Target Date Offset: —7 (to include the previous week's invoices)
Monthly Invoice Schedule

Ursa Major Solar, a renewable energy company, follows a subscription-based model, billing customers for recurring and usage-based charges. A monthly invoicing cycle aligns with standard subscription practices, making invoice management easier for customers. The company generates invoices on the 1st of each month for applicable charges. If this date falls on a public holiday, invoicing is postponed to the next business day. Automatically posting invoices streamlines billing, reduces manual effort, and improves revenue recognition. The company configures invoice runs by using these values.

Invoice Status: Post invoices (to generate invoice documents)
Frequency: 1st day of every month
Special Requirement: If the 1st day of the month is a public holiday, shift to the next business day and generate invoices only for recurring and usage-based charges.
On-Demand Invoice Schedule

Northern Trail Outfitters needs on-demand invoicing to handle urgent client requests and one-time services across various regions. The run now option allows invoices to be created immediately, instead of waiting for a set schedule. This improves cash flow, reduces delays in billing, and makes it easier to manage invoices. The company configures invoice runs by using these values.

Invoice Status: Post invoices (to generate invoice documents)
Frequency: Generate invoices on-demand
Special Requirement: Include the billing schedules for all currencies.
Invoice Schedule with Billing Period Count

Cloud Kicks sells memberships billed monthly and quarterly. Those billing schedules don’t share the same next billing date. A later target date that includes all of them invoices extra periods on the monthly memberships. To invoice one period for each selected schedule, the company configures invoice runs by using these values.

Invoice Status: Post invoices
Frequency: Monthly
Select billing schedules based on: Billing Period Count
Billing Period Count: 1
Monthly Invoice Schedule Using Day of Month

Edge Communications invoices customers through the last day of the previous month. The invoice batch run runs on the 5th of each month. Billing calculates the target date as the last day of the previous month and stamps that date on each invoice for tax. The company configures invoice runs by using these values.

Invoice Status: Post invoices
Frequency: Monthly
On: Specific Date
Date: 5
Select billing schedules based on: Target Date
Base Target Date On: Day Of Month
Target Day Of Month: last
Target Month Offset: −1
Base Invoice Date On: Offset from Target Date
Invoice Date Offset: 0

Each company's invoicing schedule is strategically designed to align with its business model, optimize cash flow, and enhance customer experience.

=== ARTICLE: ind.billing_invoice_creation.htm ===
---
article_id: ind.billing_invoice_creation.htm
title: Create Standalone Invoices or Import External Invoices
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_creation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Create Standalone Invoices or Import External Invoices

Use the Invoice Ingestion API to create standalone invoices by providing the required details to import invoices from an external system. You can also use the API to generate invoices from debit memos.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

To create or import invoices by using the Invoice Ingestion API, provide invoice details from any standard or custom Salesforce object record, or an external system. If the ingested invoice lines have the Tax Processing Status value as either Pending or Estimated, the Invoice Estimated Tax Calculation API is used to calculate estimated taxes for these invoice lines.

The API creates Invoice, Invoice Line, Invoice Line Tax, and Invoice Address Group records based on the specified details.

If you specify an order ID as the referenceEntityId property value in the Invoice Ingestion API, the generated invoices appear on the All Invoices related list of the Order record.

To generate invoices from debit memos, specify the debit memo ID as the referenceEntityId property value in the request body of this API. Make sure that the debit memo is in Posted status and is ready for invoice generation. The invoice is generated in Draft status.

=== ARTICLE: ind.billing_invoice_delete.htm ===
---
article_id: ind.billing_invoice_delete.htm
title: Delete Invoices
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_delete.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Delete Invoices

Delete invoices in Agentforce Revenue Management to correct billing errors, remove duplicate invoices, or clean up invoice drafts.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To delete invoices:	

Billing Admin permission set

OR

If you have only the Billing Operations User permission set, you can delete invoices with a status of Draft or Canceled

Before you delete an invoice with a status other than Draft or Canceled, clone the Billing Admin permission set and enable the Delete Invoice and Invoice Lines user permission.

WARNING Invoice deletion can cause data integrity issues.
From the App Launcher, find and select Invoices.
Open the Invoice record that you want to delete.
From the quick actions menu, click Delete.
Confirm the deletion.

After you delete an invoice, you can’t recover it. The invoice deletion also removes the related invoice lines and billing period items. If Billing can’t delete the invoice, an error message appears on the Invoice record.

=== ARTICLE: ind.billing_invoice_document_email.htm ===
---
article_id: ind.billing_invoice_document_email.htm
title: Send Invoice Emails from Invoice Records
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_document_email.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_pdf_document_delivery_through_email.htm
fetched_at: 2026-09-04
---

# Send Invoice Emails from Invoice Records

After invoice PDF documents are generated, send them to your customers through an email.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To send invoice email from an Invoice record:	

Billing Admin permission set

OR

Billing Operations User permission set

Before you send invoice PDF documents from Invoice records, you and your Billing Admin must define the invoice email delivery configuration and preferences.

From the App Launcher, find and select Invoices.
Open the Invoice record that you want to send an email for.
Go to the Invoice Documents related list.
From the quick actions menu on the Invoice Document row that you want to send an email for, click Email Invoice.
When you click Email Invoice, the system doesn't consider email opt-out preference selected on the related Bill to Contact record.

When you click Email Invoice, the system first looks for email preferences in this sequence. An email, with the invoice PDF document attached, is then sent to the email address of the bill to contact of the invoice. The email body has the invoice ID, the balance amount, and the invoice due date.

If the invoice email is delivered, then a success message appears immediately on the record. If the invoice email delivery fails due to these reasons, an error message appears on the Invoice record.

Exceeded the daily email limit.
Missing email address on the invoice's Bill to Contact record.
Presence of merge fields other than the invoice merge fields on the customized email template.

You can also track the emails in the activity timeline on the Invoice record's Details page.

=== ARTICLE: ind.billing_invoice_document_generation_batch.htm ===
---
article_id: ind.billing_invoice_document_generation_batch.htm
title: Generate a Batch of Invoice PDF Documents
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_document_generation_batch.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_document_generation_batch_and_single.htm
fetched_at: 2026-09-04
---

# Generate a Batch of Invoice PDF Documents

After a batch of draft or posted invoices are generated by an invoice batch run, generate PDF documents for those invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To generate invoice PDF documents:	

Billing Admin permission set OR Billing Operations User permission set

AND

DocGen User permission set

To generate invoice PDF documents from an invoice batch run, see Turn On Invoice PDF Document Generation and Account Statement.

NOTE

Before generating invoice PDF documents, review the default limits for document generation requests and the process for increasing the maximum number of content versions that are published per day.

If you selected Generate Invoice Documents on the invoice scheduler, PDF documents are created automatically as invoices are streamed during the invoice batch run. See Generate Invoices Automatically Based on Billing Schedules.

For posted invoices, Billing also delivers those documents by email during the invoice batch run when invoice email delivery is configured. See Send Invoices Through Email.

To generate PDF documents that weren’t created during the invoice batch run, or to generate them again, use the Batch Document Generation API or generate them from the Invoice Batch Run record.

From the App Launcher, find and select Invoice Batch Runs.
Open the Invoice Batch Run record that you want to generate invoice PDF documents for.
Click Generate Invoice Documents.

On clicking Generate Invoice Documents, a Batch Document Generation API request is processed to generate invoice PDF documents. See Generated Invoice PDF Document Details.

You can generate multiple invoice PDF documents for the same invoice. For example, you can generate a PDF document for a draft invoice and one more after the invoice is posted.

To send invoice emails in bulk after the documents are generated, see Send Invoice Emails in Bulk from Invoice Batch Runs.

SEE ALSO
Generate Invoices Automatically Based on Billing Schedules
Send Invoices Through Email
Send Invoice Emails in Bulk from Invoice Batch Runs
Turn On Invoice PDF Document Generation and Account Statement

=== ARTICLE: ind.billing_invoice_document_generation_batch_and_single.htm ===
---
article_id: ind.billing_invoice_document_generation_batch_and_single.htm
title: Generate Invoice PDF Documents
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_document_generation_batch_and_single.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Generate Invoice PDF Documents

After invoices are generated, generate PDF documents for a batch of invoices or a single invoice.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Default Document Template to Generate Invoice PDF Documents
After your Billing admin turns on Document Generation for Billing, immediately generate bulk PDF documents for invoices by using the default document template that's preselected.
Generate a Batch of Invoice PDF Documents
After a batch of draft or posted invoices are generated by an invoice batch run, generate PDF documents for those invoices.
Assign an Invoice Document Template to a Billing Profile
Configure a custom invoice document template to use for account-specific invoice document generation.
Generate Invoice PDF Documents Specific to Billing Profiles
Generate a PDF document for an invoice directly from the invoice record. Provide billing profile specific individual invoice documents without waiting for invoice batch runs.
Generate a Single Invoice PDF Document by Using Flow, Apex, and Omniscript
Generate a PDF document for an invoice that's generated from an Account or Order record page, or that's generated by using the Invoice Creation API.
Generate Invoice PDFs with Your Company Logo
Automatically add your company logo to the invoice PDF documents by installing Omnistudio packages and uploading the logo to your Salesforce org.
Generated Invoice PDF Document Details
When you click Generate Invoice Documents or Generate Invoice Document, the action is triggered to create a Document Generation Batch Process or Document Generation Process record with a status of In Progress. Once the status changes to Success, it means the invoice PDF document has been generated.

=== ARTICLE: ind.billing_invoice_document_generation_generated_document.htm ===
---
article_id: ind.billing_invoice_document_generation_generated_document.htm
title: Generated Invoice PDF Document Details
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_document_generation_generated_document.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_document_generation_batch_and_single.htm
fetched_at: 2026-09-04
---

# Generated Invoice PDF Document Details

When you click Generate Invoice Documents or Generate Invoice Document, the action is triggered to create a Document Generation Batch Process or Document Generation Process record with a status of In Progress. Once the status changes to Success, it means the invoice PDF document has been generated.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

The description of the Document Generation Batch Process record contains the ID of the Invoice Batch Run record for which it's created. You can see the Document Generation Process record for each invoice PDF document that's generated in the Document Generation Process related list of the Document Generation Batch Process record.

If the document generation fails, you can try again by using Retry Batch Document Generation API.

View Generated Invoice PDF Documents

Invoice PDFs are generated based on the document resolution logic for on-demand invoices and the default invoice document template that's selected on the Billing Settings page for invoice batch runs. You can see the invoice PDF documents in two locations:

From the App Launcher, find and select Files.
Open the Invoice record for which the PDF is generated, and go to the Invoice Documents related list.

When you regenerate a single invoice document, it replaces the previous version.

If you’re generating invoices in bulk, each invoice version has a separate Invoice Document record.

To download the PDF, open the PDF and click Download.

Information in the Invoice PDF Documents

The Description column of the invoice PDF document provides context-specific information of the invoice line based on the product type. For usage-based products, the Description column shows the Unit of Measure, Quantity, and Usage Overage Quantity fields of the usage-based Invoice Line record. For milestone-based products, it shows the Percentage or Flat Amount field, and the Milestone Accomplishment Date field of the Billing Milestone Plan Item record.

The invoice PDF document generated by using the default template shows bundled invoice lines in a hierarchy up to three levels, highlighting the difference between bundled and independent invoice lines. If your use case includes more than three levels of bundled invoice lines, use a customized document template to view all the invoice lines.

SEE ALSO
Manage a Document Generation Batch Process
View Document Generation Batch Process Status

=== ARTICLE: ind.billing_invoice_document_generation_single.htm ===
---
article_id: ind.billing_invoice_document_generation_single.htm
title: Generate a Single Invoice PDF Document by Using Flow, Apex, and Omniscript
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_document_generation_single.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_document_generation_batch_and_single.htm
fetched_at: 2026-09-04
---

# Generate a Single Invoice PDF Document by Using Flow, Apex, and Omniscript

Generate a PDF document for an invoice that's generated from an Account or Order record page, or that's generated by using the Invoice Creation API.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To create and generate invoice PDF documents:	

Billing Admin permission set OR Billing Operations User permission set

AND

DocGen User permission set

To generate a PDF document for an invoice, create a Document Generation Process record by configuring an Apex class, by creating a flow with the Create Records element, or by using the default Omniscript available on that Invoice record page.

Create a Document Generation Process Record Using Flow or Apex
Create a Document Generation Process record by creating a Flow with a Create Records element or by configuring an Apex class.
Generate a Single Invoice PDF Document with Omniscript
Generate a PDF document for an invoice by using Omniscript.

=== ARTICLE: ind.billing_invoice_generation.htm ===
---
article_id: ind.billing_invoice_generation.htm
title: Generate Invoices in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_generation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Generate Invoices in Revenue Management

Schedule invoice runs to generate invoices from billing schedules or generate invoices directly from accounts or orders. Create standalone invoices or import invoices from an external system.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Invoice Data Model in Revenue Management
The Invoice data model depicts the objects and their relationships to configure billing criteria, billing periods, and payment due dates for generating billing schedules and invoices aligned with your sales models. This data model also depicts integrating with saved payment methods to store customer payment methods, sequence policies to configure automated sequential numbering for your invoices, and email templates to send emails for invoices.
Automated Invoice Generation with Invoice Batch Runs
Schedule invoice batch runs to automate invoice generation. These runs use Data Processing Engine to generate invoices.
Generate Invoices for Accounts or Orders
Generate all the pending invoices of your customers in one go and on-demand. You can also generate consolidated invoices on-demand based on the invoice group type of the related billing schedules.
Create Standalone Invoices or Import External Invoices
Use the Invoice Ingestion API to create standalone invoices by providing the required details to import invoices from an external system. You can also use the API to generate invoices from debit memos.
Manage Invoices by Using APIs or Flow Actions
Use APIs or Flow actions to generate and update invoices, recover the latest generated invoices for billing schedules, void posted invoices, and send emails with posted invoices.
Void Invoices
Simplify invoice corrections by voiding posted invoices directly from the Invoice record.
Generated Invoice Details
View the relationship between invoice lines in invoice line bundles generated for billing schedule group bundles. For amended billing schedules, eliminate manual calculations by automatically generating consolidated invoices. The amounts on invoice lines that are generated for amended, canceled, and renewed assets are matched to the corresponding billing schedule amounts, ensuring accuracy. The invoice lines generated for usage resources contain the consumed quantity and the applied overage charges. The invoice lines generated for orders with quantities in decimals inherit the same quantity and unit of measure.
Invoice Aging Summaries on Accounts and Orders
See an aging summary of account invoices so that sales reps and accounts receivable teams can prioritize collections without opening each invoice. The Invoice Aging for Account component shows invoice counts, overdue invoices, aging buckets, and average and maximum invoice age on Account and Order pages.
Add Invoice Aging for Account to an Account or Order Page
Add the Invoice Aging for Account component to an Account or Order page in Lightning App Builder. Sales reps and accounts receivable teams then see overdue invoices, aging buckets, and average invoice age without opening individual invoice records.
Delete Invoices
Delete invoices in Agentforce Revenue Management to correct billing errors, remove duplicate invoices, or clean up invoice drafts.
Review Split Invoices Before Posting, Voiding, or Deleting
Before you post, void, or delete an invoice from a billing arrangement, review the related split invoices on the Split Invoices tab. Each card shows status, account, total with tax, settlement status, bill-to contact, billing profile, and invoice date.

=== ARTICLE: ind.billing_invoice_generation_for_accounts_orders.htm ===
---
article_id: ind.billing_invoice_generation_for_accounts_orders.htm
title: Generate Invoices for Accounts or Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_generation_for_accounts_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Generate Invoices for Accounts or Orders

Generate all the pending invoices of your customers in one go and on-demand. You can also generate consolidated invoices on-demand based on the invoice group type of the related billing schedules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To generate invoices for accounts or orders:	

Billing Operations User permission set

OR

Billing Customer Service User permission set

The Generate Invoices quick action is available by default on the Account object's page layout. To generate invoices for orders, add the quick action to the Order object's page layout.

From the App Launcher, find and select Accounts or Orders.
Open the Account or Order record that you want to generate an invoice for.
From the quick actions menu, click Generate Invoices.
Select a target date.
Invoices are generated for all the related billing schedules that have the next billing date before the target date, and also have the status as Ready for Invoicing.
Select the date that you want to show on the invoice.
Select whether you want to generate draft invoices or posted invoices.
Click Generate.

A Create Invoices By Using Billing Schedules API request is created. After the request is processed, users are notified of the response.

Invoices generated for accounts appear in the Invoices related list of the Account records. Invoices generated for orders appear in the All Invoices related list of the Order records.

The All Invoices related list on the Order record page is available from Spring ’26. For the Salesforce orgs created in or upgraded to Spring ’26, perform a one-time task of adding the All Invoices related list on the Order page layout.

Invoices aren’t generated for any related billing schedules that are suspended for billing. If multiple billing schedules are processed at a time for generating invoices and any of them are suspended for billing, invoices aren’t generated for any of those billing schedules. When invoices aren't generated for billing schedules because they’re invalid or suspended for billing, Revenue Transaction Error Log records are created. These records appear in the Revenue Transaction Error Logs related list of the Account or Order record.

SEE ALSO
Define Invoice Grouping on a Billing Schedule
Suspend and Resume Billing
Manage Suspend and Resume Billing
Understand Billing Suspensions and Target Date

=== ARTICLE: ind.billing_invoice_pdf_document_delivery_through_email.htm ===
---
article_id: ind.billing_invoice_pdf_document_delivery_through_email.htm
title: Send Invoices Through Email
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_pdf_document_delivery_through_email.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Send Invoices Through Email

Ensure regional compliance by sending invoices through emails to your customers after the invoices are posted and before the payment due date. Customize your preferences at various levels in your Salesforce org to choose the way emails are delivered to your customers.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Management Billing license. Contact your Salesforce account executive for more information.
Sequence of Invoice Email Preferences

When you send invoice emails, the system looks for email preferences in this sequence:

Billing Account record
Legal Entity record
Billing Settings page

If emails are sent based on the preferences on the Billing Settings page and the invoice PDF documents are already generated, the PDF documents are attached to the emails by default.

Define Invoice Email Delivery Configuration and Preferences
Before you send invoices to your customers through email, your Billing admin and Billing Operations user must complete certain tasks.
Send Invoice Emails from Invoice Records
After invoice PDF documents are generated, send them to your customers through an email.
Send Invoice Emails in Bulk from Invoice Batch Runs
After an invoice batch run completes and the invoice PDF documents are generated for the posted invoices of the invoice batch run, send invoice emails in bulk to your customers who opted for invoice delivery through email. Attach invoice PDF documents to the emails based on the selected preferences.

=== ARTICLE: ind.billing_invoice_preview_billing_schedule_groups.htm ===
---
article_id: ind.billing_invoice_preview_billing_schedule_groups.htm
title: Generate Invoice Previews for Billing Schedule Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_preview_billing_schedule_groups.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_preview_invoice.htm
fetched_at: 2026-09-04
---

# Generate Invoice Previews for Billing Schedule Groups

Preview invoices for the next two billing periods of billing schedule groups.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER
PERMISSIONS NEEDED
To generate invoice previews:	

You must have one of these permission sets:

Billing Admin
Billing Operations User
Billing Customer Service
Open the Billing Schedule Group record that you want to generate an invoice preview for.
Go to Preview Invoices tab, select a preview date and the number of billing periods.
The default preview date is the effective next billing date of the billing schedule group and the default number of billing periods is 1.
Click Preview.
NOTE You can't generate PDF documents for the invoice previews of billing schedule groups.

In the generated invoice previews, bundled products are shown in a hierarchy for up to five levels. This helps you distinguish bundled and independent products.

=== ARTICLE: ind.billing_invoice_preview_create.htm ===
---
article_id: ind.billing_invoice_preview_create.htm
title: Generate Invoice Previews for Orders and Accounts
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_preview_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_preview_invoice.htm
fetched_at: 2026-09-04
---

# Generate Invoice Previews for Orders and Accounts

Preview invoices for the next two billing periods of orders and accounts. Generate and download PDF documents of the invoice previews.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER
PERMISSIONS NEEDED
To generate invoice previews:	

You must have one of these permission sets:

Billing Admin
Billing Operations User
Billing Customer Service

To generate invoice preview PDF documents:	DocGen User permission set

The Preview Invoices quick action is available by default on both the Order page layout and the Account page layout.

Open the Account or Order record that you want to generate an invoice preview for.
From the quick actions menu, click Preview Invoices.
Select a preview date.

The default preview date is the current date and the default number of billing periods is 2. The preview date is the target date for generating an invoice preview for the first billing period. If you select 2 as the number of billing periods, the target date for generating an invoice preview for the second billing period is calculated by adding the transaction's shortest billing frequency to the previous invoice preview's target date.

For example, if you select March 3, 2025 as the preview date and the number of billing periods as 2, and the shortest billing frequency is monthly, invoice previews are generated for March 3, 2025 and April 3, 2025.
Select up to two as the number of billing periods.
Click Preview.
To generate a PDF for the invoice preview, click Generate PDF.
The generated PDF appears in the Notes & Attachments related list.
Open the PDF that you want to download and click Download.
NOTE Preview Invoices quick action is available out-of-the-box for draft and activate orders, accounts, and billing schedule groups. To preview invoices for quotes, see Generate Invoice Previews with the Invoice Preview API.

=== ARTICLE: ind.billing_invoice_preview_default_template.htm ===
---
article_id: ind.billing_invoice_preview_default_template.htm
title: Default Document Template to Generate Invoice Preview PDF Documents
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_preview_default_template.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_previews.htm
fetched_at: 2026-09-04
---

# Default Document Template to Generate Invoice Preview PDF Documents

After your Billing admin turns on Document Generation for Billing, immediately generate PDF documents for invoice previews by using the default document template that's preselected.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
NOTE When creating a custom document template, use only the data tokens from the default invoice preview template to prevent missing data.

The field values of the Default Invoice Preview Template document template are derived from:

The Invoice Date, Bill To Contact, Due Date, Total Amount, Total Tax, and Total with Tax fields of the Invoice object.
The Billing Address and Shipping Address fields of the Account object.
The Product, Quantity field, Unit Price, Tax Amount, and Line Amount fields of the Invoice Line object.
The start and end dates of the invoice line, which determine the billing period.
SEE ALSO
Turn On Invoice PDF Document Generation and Account Statement

=== ARTICLE: ind.billing_invoice_preview_example.htm ===
---
article_id: ind.billing_invoice_preview_example.htm
title: "Example: Preview Invoices for an Order"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_preview_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_previews.htm
fetched_at: 2026-09-04
---

# Example: Preview Invoices for an Order

This example shows how Billing generates preview invoices when an order includes products with different billing frequencies.

Acme Software Innovations places an order with these products for its customer, Growth Digital Marketing Pro.

Cloud Storage Pro, annual subscription, billed yearly at $1,200
Support Package, annual subscription, billed yearly at $600
User Licenses, monthly subscription, billed monthly at $150
API Access, monthly subscription, billed monthly at $50

The Acme Software Innovations Billing team wants to preview billing charges and share a proforma invoice before generating the actual invoices. The Billing team opens the order record for Growth Digital Marketing Pro and clicks Preview Invoices. They select March 1, 2025 as the preview date and 2 as the number of billing periods.

Billing generates two invoice previews.

The first invoice preview includes these products due for billing on March 1, 2025.

Cloud Storage Pro billed at $1,200
Support Package billed at $600
User Licenses billed at $150
API Access billed at $50

Billing calculates the second preview date by adding the shortest billing frequency, which is 1 month to the first preview date. The second invoice preview includes these monthly products due for billing on April 1, 2025.

User Licenses billed at $150
API Access billed at $50
NOTE The annual products were billed in the first invoice preview and their next billing is on March 1, 2026. Therefore, the second invoice preview has only monthly subscription products.

The Acme Software Innovations Billing team generates a PDF for each invoice preview, downloads them, and emails them to Growth Digital Marketing Pro for reconfirmation.

=== ARTICLE: ind.billing_invoice_preview_procedure_plan_create.htm ===
---
article_id: ind.billing_invoice_preview_procedure_plan_create.htm
title: Generate Invoice Previews with the Invoice Preview API
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_preview_procedure_plan_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_previews.htm
fetched_at: 2026-09-04
---

# Generate Invoice Previews with the Invoice Preview API

To generate preview invoices by using the Invoice Preview API, create and activate a custom procedure plan definition for the object that you want to preview invoices for. The Invoice Preview API uses the procedure plan to generate invoice previews. A custom procedure plan creation isn't required to use the Invoice Preview API for orders, accounts, and billing schedule groups.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create and update custom procedure plan definitions:	Context Service Admin permission set
To generate invoice previews by using the API:	

You must have one of these permission sets:

Billing Admin
Billing Operations User
Billing Customer Service
IMPORTANT

From Summer ’25 and onwards, you will not be able to sync existing context definitions that were either cloned or extended from the standard BillingContext context definition. To fix this issue, use the Context Attribute Mapping API to delete duplicate BSGEntitiesMapping attribute mappings.

BillingTransactionSource attribute of the BillingSchedule node to Reference attribute of the BillingSchedule object.
BillingTransactionItemSource attribute of the BillingSchedule node to the ReferenceItem attribute of the BillingSchedule object.
SEE ALSO
Create a Custom Procedure Plan Definition
Create a Custom Procedure Plan

Create a custom procedure plan when you want to preview invoices using the Invoice Preview API for quotes or other billing transactions.

Create a custom procedure plan definition.
Select Billing as the process type.
Select the object that you want to preview invoices for as the primary object.
Select the extended BillingContext context definition as the context definition.
Update and activate the procedure plan definition.
Open the procedure plan definition and select a read context mapping for the primary object.
Activate the procedure plan definition.
To generate invoice previews for any billing transaction, use the Invoice Preview API.
Preview Invoices for Quotes

To use the standalone Billing Schedules API and Invoice API for quotes, create context definition, a context mapping and a procedure plan.

Extend the BillingContext Context Definition.
Map the Billing Transaction, Billing Transaction Item, Billing Transaction Item Detail, and Billing Transaction Item Relationship nodes and fields to Quote, Quote Line, Quote Line Detail, and Quote Line Relationship objects and fields.
See Add Context Mapping.
Activate the context definition.
Create a custom procedure plan.
To generate invoice previews for quotes, use the Invoice Preview API.

=== ARTICLE: ind.billing_invoice_previews.htm ===
---
article_id: ind.billing_invoice_previews.htm
title: Preview Invoices
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_previews.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Preview Invoices

Preview invoices for the next two billing periods of orders, quotes, accounts, or billing schedule groups to verify order products, discounts, amendments, cancellations, and tax calculations.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Default Document Template to Generate Invoice Preview PDF Documents
After your Billing admin turns on Document Generation for Billing, immediately generate PDF documents for invoice previews by using the default document template that's preselected.
Generate Invoice Previews and Preview PDF Documents
Generate invoice previews without generating an actual invoice and then generate PDF documents for the invoice previews. Share the PDF documents with your customers to reduce billing disputes.
Generate Invoice Previews with the Invoice Preview API
To generate preview invoices by using the Invoice Preview API, create and activate a custom procedure plan definition for the object that you want to preview invoices for. The Invoice Preview API uses the procedure plan to generate invoice previews. A custom procedure plan creation isn't required to use the Invoice Preview API for orders, accounts, and billing schedule groups.
Example: Preview Invoices for an Order
This example shows how Billing generates preview invoices when an order includes products with different billing frequencies.

=== ARTICLE: ind.billing_invoice_risk_score.htm ===
---
article_id: ind.billing_invoice_risk_score.htm
title: Invoice Risk Score (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_score.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Invoice Risk Score (Pilot)

Invoice Risk Scoring uses invoice data and predictive AI to estimate the likelihood that payment for an open invoice will be delayed beyond its due date. Learn how risk scores and risk levels are displayed on invoice records to help identify potential payment risks.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
Overview of Features and Assets of Invoice Risk Scoring (Pilot)
Review key input features and assets involved in the installation and configuration of Invoice Risk Scoring via the Scoring Framework configuration template type.
View Invoice Risk Scores (Pilot)
After configuring Invoice Risk Scoring, you can view the predicted risk scores and risk levels on invoice records.

=== ARTICLE: ind.billing_invoice_risk_score_template_configure.htm ===
---
article_id: ind.billing_invoice_risk_score_template_configure.htm
title: Configure the Scoring Framework Template (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_score_template_configure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Configure the Scoring Framework Template (Pilot)

After you configure the scoring framework template, set up the predictive AI model by defining the data space, training data, risk score thresholds, and input features.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create and configure Invoice Risk Scoring:	AI Accelerator User AND Scoring Framework Admin
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
From Setup, in the Quick Find box, find and select Scoring Framework.
Open the Invoice Risk Scoring template.
Select the data space where you want to create the data stream for invoice risk scoring. Select default if you don't have any custom data space.
Select Invoice (STANDARD) as the Data Model Object.

This determines which invoice data the model uses for training and scoring.

Configure Risk Score Thresholds.

The thresholds determine how risk scores are categorized into Low, Medium, and High risk levels.

Set up the medium threshold value. The default value is 0.3.
NOTE Invoices with risk scores less than or equal to this value are classified as low risk. Invoices with risk scores greater than this value are classified as medium or high risk.
Set up the high threshold value. The default value is 0.7.
NOTE Invoices with risk scores greater than this value are classified as high risk. Invoices with risk scores between the medium and high thresholds are classified as medium risk.

For example, with the default thresholds set to Medium: 0.2 and High: 0.8, a risk score of 0.15 is classified as low risk. A risk score of 0.5 is classified as medium risk, while a risk score of 0.85 is classified as high risk.

If needed, configure the filter training and scoring data.
Select at least two fields from predefined fields or invoice custom fields that act as input for your scoring model.

Predefined fields are standard invoice fields optimized for risk prediction. Invoice custom fields are business-specific fields used for risk assessment.

NOTE Input features are invoice attributes used by the AI model to predict payment risk. Select features from predefined and custom fields that are strong indicators of payment behavior in your business, as more relevant features improve prediction accuracy.
If needed, use debug configuration settings to troubleshoot installation issues.

Enable Save Assets to keep successfully installed components if the installation fails. By default, all changes are rolled back if the installation fails.

Review and activate the framework.

The system starts creating the Invoice Risk Scoring app, which includes generating data transforms for training and scoring, training the AI model on historical invoice data, and deploying the model for scoring, with an expected duration of 15–20 minutes. During this process, it automatically runs model training, creates data transforms, and deploys the AI model for scoring readiness.

Verify Installation
From Setup, in the Quick Find box, find and select App Hub.
Check the installation status of your Invoice Risk Scoring app.
View the AI Model
From the Data 360 App Launcher, search for and select AI Models.
Locate and open your Invoice Risk Score model.
Review the model details: training status, model accuracy metrics, input features used, and last training date.
Troubleshooting
From Setup, in the Quick Find box, find and select App Install History.
Locate your Invoice Risk Scoring app installation attempt.
Review the failure details and error messages.

=== ARTICLE: ind.billing_invoice_risk_scoring.htm ===
---
article_id: ind.billing_invoice_risk_scoring.htm
title: Set Up Invoice Risk Scoring to Predict Risk Scores for Invoices (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Set Up Invoice Risk Scoring to Predict Risk Scores for Invoices (Pilot)

A risk score for an invoice predicts the likelihood that payment for an open invoice is delayed beyond its due date. The score estimates the probability of late payment based on patterns and signals such as historical payment behavior, invoice aging, outstanding balances, customer payment trends, dispute history, and other relevant account characteristics.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.

The risk score helps billing and finance teams identify invoices potentially requiring closer monitoring, and it helps them prioritize collection efforts. A higher risk score indicates a greater likelihood of overdue payments, while a lower score suggests payment is more likely on or before the due date.

By incorporating risk scores into collections workflows, organizations can improve collection efficiency, reduce overdue receivables, and better manage cash flow. For example, organizations can route invoices with higher risk scores to specialized collection plans, assign invoices to collection reps for proactive outreach, or include them in targeted reminder campaigns before the due date. Lower-risk invoices can follow standard collection processes so teams focus their efforts on accounts that require immediate attention.

Get Started with Data 360 for Invoice Risk Score Predictions (Pilot)
Before you install and configure Invoice Risk Scoring, complete the prerequisites.
Add Data Cloud Salesforce Connector Permissions for Invoice Risk Scoring (Pilot)
To ingest invoice objects and fields into Data 360, add the View All Records and Read permissions to the Data Cloud Salesforce Connector permission set in your Salesforce org.
Turn On Legacy AI Model Creation (Pilot)
Legacy AI Model Creation allows the system to create predictive AI models with the appropriate runtime configuration required for invoice risk scoring.
Turn On Predictive Risk Scoring for Invoices (Pilot)
To view the invoice risk scores and levels, turn on predictive risk score for invoices.
Configure Scoring Framework (Pilot)
Use the prebuilt Scoring Framework configuration template type to install and configure the scoring app. This app creates and trains the Predictive AI model to project invoice risk levels.
Configure the Scoring Framework Template (Pilot)
After you configure the scoring framework template, set up the predictive AI model by defining the data space, training data, risk score thresholds, and input features.
Schedule Data Transform for Scoring (Pilot)
After successfully installing the Invoice Risk Scoring app, schedule the data transform to compute risk scores on your latest open invoices.
Create a Copy Field Enrichment to Copy Risk Score from Data Model Object (Pilot)
The Invoice Risk Scoring app computes risk scores in Data 360.
Create Use Case for AI Accelerator (Pilot)
After configuring the Scoring Framework and creating the Copy Field Enrichment, create and configure a machine learning use case in AI Accelerator. The AI Accelerator use case connects the trained Invoice Risk Score model to your Salesforce org so that risk predictions are accessible on invoice records.

=== ARTICLE: ind.billing_invoice_risk_scoring_ai_accelerator_use_case.htm ===
---
article_id: ind.billing_invoice_risk_scoring_ai_accelerator_use_case.htm
title: Create Use Case for AI Accelerator (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_ai_accelerator_use_case.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Create Use Case for AI Accelerator (Pilot)

After configuring the Scoring Framework and creating the Copy Field Enrichment, create and configure a machine learning use case in AI Accelerator. The AI Accelerator use case connects the trained Invoice Risk Score model to your Salesforce org so that risk predictions are accessible on invoice records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To view enrichments in Setup:	View Setup
To create or update enrichments:	Customize Application AND Data Cloud User AND Write Access to Data Action AND Write Access to Data Space Definition
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
From Setup, in the Quick Find box, find and select AI Accelerator.
Click New to create a use case.
Use the more option to edit the use case to configure it.
Select Einstein on Data Cloud as the Prediction Platform.
The Invoice Risk Score model is built and trained in Data 360, so AI Accelerator looks for predictions there.
For Prediction, select Already Generated.
In the Scoring Field section, configure these fields.
	
Predicted Overdue	Predicted Date Invoice Overdue
Risk Level	Invoice Risk Score
These fields are the model outputs that surface on the Invoice record—the predicted overdue date and the High, Medium, or Low risk classification.
For Reference Record Field, select the InvoiceRiskScoringObject and set the field to Invoice ID.
This action links each Data 360 prediction row to the correct Invoice record.
Enter a Prediction Label Template.
A prediction label template is a display string that tells AI Accelerator how to present the prediction result to users on the Invoice record. It typically combines static text with dynamic field values.
In the Use Case Model section, select the Invoice Risk Score model created during Scoring Framework setup.
Save the changes.

=== ARTICLE: ind.billing_invoice_risk_scoring_configure_framework.htm ===
---
article_id: ind.billing_invoice_risk_scoring_configure_framework.htm
title: Configure Scoring Framework (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_configure_framework.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Configure Scoring Framework (Pilot)

Use the prebuilt Scoring Framework configuration template type to install and configure the scoring app. This app creates and trains the Predictive AI model to project invoice risk levels.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create and configure Invoice Risk Scoring:	AI Accelerator User AND Scoring Framework Admin
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
From Setup, use the Quick Find box to find and select Scoring Framework.
Click New Template Configuration.
Select Invoice Risk Scoring as the template configuration type.
Enter a label for the template configuration.
Select Train and Deploy model mode to start scoring open invoices immediately.
Save the changes.

=== ARTICLE: ind.billing_invoice_risk_scoring_connector_permissions.htm ===
---
article_id: ind.billing_invoice_risk_scoring_connector_permissions.htm
title: Add Data Cloud Salesforce Connector Permissions for Invoice Risk Scoring (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_connector_permissions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Add Data Cloud Salesforce Connector Permissions for Invoice Risk Scoring (Pilot)

To ingest invoice objects and fields into Data 360, add the View All Records and Read permissions to the Data Cloud Salesforce Connector permission set in your Salesforce org.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To configure Data Cloud Salesforce Connector permissions:	Data Cloud Admin permission set
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
From Setup, use the Quick Find box to find and select Permission Sets.
Click the required permission set to edit it, then open System Permissions under the App section.
Add the Manage Billing, Manage Billing Access, View All Data, and View All Fields (Global) system permissions for the Data Cloud Salesforce Connector permission set.
NOTE The Data Cloud Salesforce Connector permission set is available only after you connect your Salesforce org to Data Cloud. For deployed orgs that haven't been updated recently, the permission set is listed as Salesforce CDP Salesforce Connector Integration, Customer Data Platform Salesforce Connector Integration, or Customer 360 Audiences Salesforce Connector Integration.
Add the Manage Billing Access system permission to the Customer 360 Data Platform Integration permission set.
Edit the Data Cloud Data Space Management app permission for the Data Cloud Architect permission set to include the required data space.

=== ARTICLE: ind.billing_invoice_risk_scoring_copy_field_enrichment.htm ===
---
article_id: ind.billing_invoice_risk_scoring_copy_field_enrichment.htm
title: Create a Copy Field Enrichment to Copy Risk Score from Data Model Object (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_copy_field_enrichment.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Create a Copy Field Enrichment to Copy Risk Score from Data Model Object (Pilot)

The Invoice Risk Scoring app computes risk scores in Data 360.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To view enrichments in Setup:	View Setup
To create or update enrichments:	Customize Application AND Data Cloud User AND Write Access to Data Action AND Write Access to Data Space Definition
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
NOTE If you enabled enhanced security data spaces, you also need the Customize Data Actions on the Dataspace Scope permission.

Create a Data 360 Copy Field Enrichment to copy the risk score from the Invoice Risk Scoring Data Model Object to the risk score field of the Invoice object in your Salesforce org.

From Setup, in the Quick Find box, find and select Copy Field.
On the Data 360 Copy Field Enrichments page, click New.
Configure the copy fields.
Data Space: The data space that you selected during Scoring Framework setup
Data 360 Object: Specify the name created during Invoice Risk Scoring installation. The object follows the naming pattern <AppName> InvoiceRiskScoringObject. For example, if you named the app IRS, the Data Model Object name is IRS InvoiceRiskScoringObject.
Target Object: Invoice
Data 360 Copy Fields: Invoice Risk Level
Map the invoice risk level to the invoice overdue risk indicator field.
Save the changes and start the sync.

After creating the enrichment, start the sync operation to begin copying risk score data from Data 360 to Salesforce Invoice records. The initial sync can take a few minutes depending on the number of invoices. Then, open an invoice record in posted status with a non-zero balance and verify that the risk score and risk level fields are populated.

The copy field enrichment runs on a schedule that aligns with your scoring data transform schedule. If you score invoices daily, schedule the enrichment to run shortly after the scoring completes.

=== ARTICLE: ind.billing_invoice_risk_scoring_enable.htm ===
---
article_id: ind.billing_invoice_risk_scoring_enable.htm
title: Turn On Predictive Risk Scoring for Invoices (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Turn On Predictive Risk Scoring for Invoices (Pilot)

To view the invoice risk scores and levels, turn on predictive risk score for invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To turn on predictive risk scoring for invoices:	Billing Admin permission set
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
From Setup, use the Quick Find box to find and select Billing Settings.
Turn on Predictive Risk Scoring for Invoices.

After you turn on this setting, you can configure the scoring framework to calculate the predictive risk levels for invoices.

=== ARTICLE: ind.billing_invoice_risk_scoring_enable_legacy_ai.htm ===
---
article_id: ind.billing_invoice_risk_scoring_enable_legacy_ai.htm
title: Turn On Legacy AI Model Creation (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_enable_legacy_ai.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Turn On Legacy AI Model Creation (Pilot)

Legacy AI Model Creation allows the system to create predictive AI models with the appropriate runtime configuration required for invoice risk scoring.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To turn on Legacy AI Model Creation:	Data Cloud Admin permission set
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
From Setup, use the Quick Find box to find and select Feature Manager.
Under the Data Cloud section, find the Legacy AI Model Creation feature.
Turn on Legacy AI Model Creation.

=== ARTICLE: ind.billing_invoice_risk_scoring_features_overview.htm ===
---
article_id: ind.billing_invoice_risk_scoring_features_overview.htm
title: Overview of Features and Assets of Invoice Risk Scoring (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_features_overview.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_score.htm
fetched_at: 2026-09-04
---

# Overview of Features and Assets of Invoice Risk Scoring (Pilot)

Review key input features and assets involved in the installation and configuration of Invoice Risk Scoring via the Scoring Framework configuration template type.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
Standard Invoice Fields

The Invoice Risk Scoring template includes predefined invoice fields that are used to train and score the predictive AI model.

FIELD	DESCRIPTION
Billing Account	Account associated with the invoice
Total Amount	Total invoice amount
Payment Term Item Period	Payment term duration (for example, Net 30 = 30 days)
Net Credit Memo Applied Amount	Net credit memo amount applied to the invoice
Net Credit Applied Amount	Net credits applied to the invoice
Settlement Date	Actual or expected settlement date
Posted Date	Invoice posted date
Due Date	Invoice due date
Derived Days Invoice Overdue	Calculated overdue days based on settlement status
NOTE The model uses only invoice header-level fields. Invoice line-level fields aren't included in scoring.
Predefined Fields

Created specifically for this model, these fields are useful for score predictions.

FIELD	DESCRIPTION
Account Annual Revenue	Annual revenue of the billing account
Account Primary Industry	Industry classification of the account
Net Credits to Invoice Amount Ratio	Ratio of credits applied to invoice amount
Net Payments to Invoice Amount Ratio	Ratio of payments applied to invoice amount
Invoice Amount to Account Revenue Ratio	Ratio of invoice amount to annual revenue
Account Average Days Overdue	Historical average overdue days for the account
Invoice Overdue	Indicates whether the invoice is overdue
NOTE Dynamic fields such as Days Invoice Overdue and Days Invoice Open aren't used directly because they change daily for open invoices. Instead, the model uses Derived Days Invoice Overdue for consistent scoring.
Risk Score Calculation

The risk score is calculated by using invoice due dates, posted dates, and AI predicted days overdue of the invoice values.

Invoices already overdue or with invalid date ranges receive a fixed score of 0.99.
Predicted late payments can produce scores greater than 1.0, which are treated as high risk.
Default Risk Level Thresholds
RISK LEVEL	THRESHOLD
Low	≤ 0.3
Medium	> 0.3 and ≤ 0.7
High	> 0.7 or ≥ 0.99
AI Explainability

Each score includes explainability details showing:

The top 3 factors influencing the score
Impact value of each factor

=== ARTICLE: ind.billing_invoice_risk_scoring_get_started.htm ===
---
article_id: ind.billing_invoice_risk_scoring_get_started.htm
title: Get Started with Data 360 for Invoice Risk Score Predictions (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_get_started.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Get Started with Data 360 for Invoice Risk Score Predictions (Pilot)

Before you install and configure Invoice Risk Scoring, complete the prerequisites.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To access Data 360 setup:	Data Cloud Architect permission set
To create a custom data space:	Data Cloud Admin permission set
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
Turn on Data 360.

Data 360 is automatically provisioned when a Data 360 license is added to your Salesforce org. However, if auto provisioning isn't available or if you're working in a Developer Edition or sandbox org, you manually enable it. Data 360 can be enabled on a new or an existing Salesforce org.

Create a custom data space so that all the relevant Data 360 objects related to risk score data can be mapped to it.
Creating a custom data space is optional. To segregate your brand, region, or department data and services, create a custom data space. If you don't create a custom data space, all Data 360 objects are mapped to the default data space.
Deploy the Advanced Billing Bundle Data Kit and Common Billing Bundle Data Kit to Data 360 before configuring Invoice Risk Scoring.
From the App Launcher, find and select Data 360.
On the Data Streams tab, click New.
Select Salesforce CRM as the connected source, and then click Next.
In the Standard Data Bundles section, select Advanced Billing Bundle Data Kit and deploy it. Then select and deploy Common Billing Bundle Data Kit
Review the data fields and click Next.
Click Deploy.
If you have data in Data 360 in other orgs, you can import that data by setting up a CRM Salesforce Org connection.

=== ARTICLE: ind.billing_invoice_risk_scoring_schedule_data_transform.htm ===
---
article_id: ind.billing_invoice_risk_scoring_schedule_data_transform.htm
title: Schedule Data Transform for Scoring (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_schedule_data_transform.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_scoring.htm
fetched_at: 2026-09-04
---

# Schedule Data Transform for Scoring (Pilot)

After successfully installing the Invoice Risk Scoring app, schedule the data transform to compute risk scores on your latest open invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create and configure Invoice Risk Scoring:	AI Accelerator User AND Scoring Framework Admin
NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.
From the Data 360 App Launcher, search for and select AI Models.
Locate and open your Invoice Risk Score model.
From More options, click Data Transforms.

The Invoice Risk Scoring app creates two data transforms.

Training Data Transform (InvoiceRiskTrainingBDT): Trains the AI model on historical settled invoices
Scoring Data Transform (InvoiceRiskScoringBDT): Scores open invoices with non-zero balance
Click Schedule to configure the schedule.
Save the changes.

=== ARTICLE: ind.billing_invoice_risk_scoring_view_scores.htm ===
---
article_id: ind.billing_invoice_risk_scoring_view_scores.htm
title: View Invoice Risk Scores (Pilot)
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_risk_scoring_view_scores.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_risk_score.htm
fetched_at: 2026-09-04
---

# View Invoice Risk Scores (Pilot)

After configuring Invoice Risk Scoring, you can view the predicted risk scores and risk levels on invoice records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To view invoice risk scores:	

Billing Admin permission set

AND

Billing Operations User permission set

NOTE Invoice Risk Scoring is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.

Use the AI Accelerator Card component to view risk scores on invoice records. After your Billing Admin adds the component to the Invoice record page in the Lightning App Builder, select the use case definition and model name, and then set the threshold score to 0.

Invoice includes two fields for displaying risk score predictions.

Risk Score: A numeric value representing the likelihood of delayed or non-payment. Higher scores indicate greater risk.
Risk Level: A text value that categorizes the risk as Low, Medium, or High. The thresholds that you configured during setup determine the risk level.
From the App Launcher, find and select Invoices.
Open the invoice record that you want to review.
Review the risk score information displayed for the invoice record.

=== ARTICLE: ind.billing_invoice_run_sync_process.htm ===
---
article_id: ind.billing_invoice_run_sync_process.htm
title: Convert Automations to Asynchronous for Invoice Batch Runs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_run_sync_process.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_automate_invoice_generation.htm
fetched_at: 2026-09-04
---

# Convert Automations to Asynchronous for Invoice Batch Runs

Identify active flows and Apex triggers on Billing objects and convert them to asynchronous processes before you schedule an invoice batch run. Synchronous automations can stop a run or leave invoices in Draft In Progress, Posting In Progress, or Error.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To review and convert record-triggered flows:	Manage Flow
To view Apex triggers:	View Setup and Configuration
To convert Apex triggers:	Author Apex
To recover stuck invoices:	

Billing Admin permission set

OR

Billing Operations User permission set

A record-triggered flow or Apex trigger is tied to an object, such as Invoice or Invoice Line. You define and activate the flow on that object in Flow Builder. A person who has the Author Apex permission defines the Apex trigger on that object and sets it to active. These automations are custom. Billing doesn't create them. See Activate or Deactivate a Flow and Define Apex Triggers.

When an invoice batch run generates invoices, the run creates or updates records on Billing objects. Those objects include invoices, invoice lines, tax lines, debit and credit memos, billing schedules, and billing period items. Any active flow or trigger on a Billing object then runs for every record the invoice batch run saves.

A synchronous automation runs as part of saving the record. The invoice batch run doesn't finish saving the invoice until that flow or trigger is done. If the automation queries related records for every invoice, the run can hit processing limits or time out. Invoices can remain in Draft In Progress, Posting In Progress, or Error.

An asynchronous automation waits until the invoice records are saved, then runs. The batch run can finish generating invoices. The flow or trigger still runs, just not while the invoice is being saved.

From Setup, in the Quick Find box, enter Flows, and then select Flows.
Review active record-triggered flows on these Billing objects.
Invoice
Invoice Line
Invoice Line Tax
Debit Memo
Debit Memo Line
Debit Memo Line Tax
Credit Memo
Credit Memo Line
Credit Memo Line Tax
Billing Schedule
Billing Period Item
From Setup, in the Quick Find box, enter Apex Triggers, and then select Apex Triggers.
Review active triggers on the same objects.
To list the automations with SOQL, open the Developer Console Query Editor.

Sample scripts:

For the flow query, select Use Tooling API. For the Apex trigger query, leave Use Tooling API cleared.

Flows:

SELECT Id, IsActive, Label, ProcessType, ManageableState, TriggerObjectOrEventId, TriggerObjectOrEventLabel, TriggerType FROM FlowDefinitionView WHERE TriggerObjectOrEventId IN ('Invoice','InvoiceLine','DebitMemo','DebitMemoLine','CreditMemo','CreditMemoLine','InvoiceLineTax','DebitMemoLineTax','CreditMemoLineTax','BillingSchedule','BillingPeriodItem') AND IsActive = TRUE

Apex triggers:

SELECT Id, TableEnumOrId, Name, Status FROM ApexTrigger WHERE TableEnumOrId IN ('Invoice','InvoiceLine','DebitMemo','DebitMemoLine','CreditMemo','CreditMemoLine','InvoiceLineTax','DebitMemoLineTax','CreditMemoLineTax','BillingSchedule','BillingPeriodItem') AND Status = 'Active'
For each after-save record-triggered flow, move the logic to a Run Asynchronously path so it runs after the invoice save commits. See Triggered Flows.
For each Apex trigger, work with a person who has the Author Apex permission to move the logic out of the record save. Use queueable Apex or an Apex trigger on a change event, which runs after the save is complete. See Queueable Apex and Subscribe with Apex Triggers.

After you convert the automations, schedule the next invoice batch run. See Generate Invoices Automatically Based on Billing Schedules.

If invoices from an earlier run are stuck in Draft In Progress, Posting In Progress, or Error, click Recover on the invoice batch run. Then generate invoices again.

=== ARTICLE: ind.billing_invoice_scheduler_amended_bundle_schedule_groups.htm ===
---
article_id: ind.billing_invoice_scheduler_amended_bundle_schedule_groups.htm
title: Generated Invoice Details
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoice_scheduler_amended_bundle_schedule_groups.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Generated Invoice Details

View the relationship between invoice lines in invoice line bundles generated for billing schedule group bundles. For amended billing schedules, eliminate manual calculations by automatically generating consolidated invoices. The amounts on invoice lines that are generated for amended, canceled, and renewed assets are matched to the corresponding billing schedule amounts, ensuring accuracy. The invoice lines generated for usage resources contain the consumed quantity and the applied overage charges. The invoice lines generated for orders with quantities in decimals inherit the same quantity and unit of measure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


This feature is available with the Revenue Management Advanced license or the Revenue Management Billing license.

The Usage Management feature is available only with the the Revenue Management Billing license. Contact your Salesforce account executive for more information.

Invoices for Amended, Renewed, or Canceled Assets

If there are billing schedules for amended, renewed, canceled assets, invoice lines are created for the same positive or negative amounts as those of the billing schedules.

Single Invoice Line for Amended Billing Schedules

When an asset is amended and the related amendment order is activated, amended billing schedule groups are generated. When you generate an invoice for an amended billing schedule, the details of the original and the amended order product are automatically consolidated into a single invoice line. The criteria to generate a consolidated invoice line is that the original and amended order product must have the same Billing Period Start Date and Billing Period End Date. The Has Multiple Items field of the amended Invoice Line record indicates if there are multiple billing period items for the invoice. If there are multiple billing period items, they appear on the Billing Period Items related list.

EXAMPLE If an asset priced at $5 per unit is amended by adding five units to an existing ten units, then the consolidated invoice line reflects a total of 15 units at a Charge Amount of $75.
Invoices for Usage-Based Products

For usage-based charge types, invoice lines for usage resources include details about the total consumed quantity, any overage quantity, and applicable overage charges. Usage-based products are invoiced when the liable summary, usage entitlement bucket, and usage entitlement account share the same grant binding target.

See Track Product Usage and Consumption in Revenue Cloud.

Quantity and Unit of Measure for Invoice Lines

Invoice lines inherit their quantity and unit of measure from the related billing schedules’ quantity and unit of measure. An invoice line’s quantity is rounded off based on the scale and rounding method of the quantity’s unit of measure.

See Generated Billing Schedule Details.

Invoice Line Bundles for Billing Schedule Group Bundles

When an invoice run processes a billing schedule group bundle, the corresponding invoice line bundles are generated. These invoice line bundles are displayed hierarchically in the Invoice Lines related lists of the Invoice record, distinguishing related and independent products.

All the invoice lines related to an invoice line bundle appear in the Associated Invoice Lines (1) related list of the Invoice Line Bundle record.
The invoice line bundle related to an invoice line appears in the Main Invoice Lines (2) related list of the Invoice Line record.

If the line amount of invoice lines in a bundle is zero, the parent invoice line shows the total line amount for the entire bundle.

Invoice Line Bundles with Different Billing Frequencies

When a child product in a bundle has a different billing frequency than the parent product, the invoice reflects each billing period separately. This means a single child invoice line can span multiple parent invoice lines — one for each billing period within the child's billing term.

To consistently identify the parent, the child invoice line is associated with the parent invoice line from the earliest billing period in its span.

EXAMPLE

Consider a bundle where the parent product is billed monthly and the child product is billed quarterly:

Quantum Bit Subscription Pro — $120/month (parent)
Data Storage — $50/quarter (child)

When an invoice is generated for Q4 2026, the following invoice lines are created:

Invoice lines generated for Q4 2026
PRODUCT	BILLING PERIOD	QUANTITY	AMOUNT
Quantum Bit Subscription Pro	Oct 1, 2026 – Oct 31, 2026	1	$120
Data Storage	Oct 1, 2026 – Dec 31, 2026	1	$50
Quantum Bit Subscription Pro	Nov 1, 2026 – Nov 30, 2026	1	$120
Quantum Bit Subscription Pro	Dec 1, 2026 – Dec 31, 2026	1	$120

Since the parent product is billed monthly, it generates three separate invoice lines: one each for October, November, and December. The child product, billed quarterly, generates a single invoice line covering the entire quarter, October through December.

Because the Data Storage invoice line spans all three months, it overlaps with all three parent invoice lines. In this case, the October invoice line, the earliest billing period, is displayed as the associated parent invoice line.

=== ARTICLE: ind.billing_invoices_apis_and_actions.htm ===
---
article_id: ind.billing_invoices_apis_and_actions.htm
title: Manage Invoices by Using APIs or Flow Actions
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoices_apis_and_actions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Manage Invoices by Using APIs or Flow Actions

Use APIs or Flow actions to generate and update invoices, recover the latest generated invoices for billing schedules, void posted invoices, and send emails with posted invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
GOAL	API
Create or update an invoice scheduler to automatically generate invoices.	Batch Invoice Scheduler API
Generate an invoice for an account, order, or a list of billing schedules.	Invoice Creation API
Ingest or generate an invoice from an internal or external billing transaction data.	Invoice Ingestion API
Update the status of an invoice from Draft to Posted.	

Invoice Draft to Posted Status API

To automate the process of updating the status of an invoice from Draft to Posted, build a custom flow and use the Post Draft Invoice action.


Update a batch of invoices from Draft to Posted status for a credit memo application.	

Batch Invoices Draft to Posted Status API

To automate the process of updating the status of a batch of invoices from Draft to Posted for a credit memo application, build a custom flow and use the Post Draft Invoice Batch Run action.


Recover the latest generated invoice associated with the billing schedules in the Error or Processing status.	

Billing Schedule Recovery List API

To automate the process of recovering one or more billing schedules in the Error or Processing status, build a custom flow and use the Recover Billing Schedules action.


Recover records associated with a failed invoice run. Recovery is required only when billing schedules remain in the Processing, Void In Progress, or Error status.	Invoice Run Recovery API
Void a posted invoice to rebill the customer.	Void a Posted Invoice API
Send emails for the posted invoices of a specified invoice batch run ID.	Send Emails for Posted Invoices API
IMPORTANT When generating invoices by using the Invoice Creation API or invoice batch runs, implement custom automation on generated invoices as asynchronous processes, such as asynchronous flow paths or asynchronous Apex triggers. Synchronous automation in this context can cause performance issues, timeouts, or failures.

=== ARTICLE: ind.billing_invoices_email_prerequisites.htm ===
---
article_id: ind.billing_invoices_email_prerequisites.htm
title: Define Invoice Email Delivery Configuration and Preferences
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoices_email_prerequisites.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_pdf_document_delivery_through_email.htm
fetched_at: 2026-09-04
---

# Define Invoice Email Delivery Configuration and Preferences

Before you send invoices to your customers through email, your Billing admin and Billing Operations user must complete certain tasks.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Configure Email Delivery of Invoices

Before you send invoice emails, your Billing Admin must configure these settings in your Salesforce org.

If you want to send invoice emails from Invoice records, turn on Document Generation for Billing.

See Turn On Invoice PDF Document Generation and Account Statement.

If you want to send invoice emails from Invoice Batch Run records, turning on Document Generation for Billing is optional.

Turn on Configure Email Delivery Settings and select a default email template. Optionally, create custom email templates and select one as the default template instead.
See Turn On Email Delivery of Invoices, Invoice Email Prerequisites, and Create Email Templates.
Define the email preferences on Legal Entity records.
See Create Legal Entities in Revenue Management.
Enable Customer User for a Bill to Contact record to provide access to Experience Cloud sites.

See Create Experience Cloud Site Users.

A maximum of 5000 emails can be sent to the email address on Bill to Contact records daily. To send emails beyond the daily limit, enable customer user for the Bill to Contact record. Emails sent to customer community users are not counted against the 5000 daily email limit. The system first checks for a customer community user before considering the email address on the Bill to Contact record.

Enable Email Tracking to track emails in activity timeline.
See Enable Email Tracking for All Customers Opening Email from Your Company.
Define Invoice Email Delivery Preferences

Before you send invoice emails, your Billing Operations user must define these values.

Define the email preferences on Billing Account records.
See Create Billing Profiles.
Specify the email address on Bill To Contact records of invoices.
See Contact Fields.
If yours customers choose to not receive emails, edit the Contact record to opt out of receiving emails.

See Opting Out of Email.

Only the contacts that have self-service access to the Experience Cloud site can opt themselves out of receiving emails.

After you define these values, send invoice emails from Invoice records or Invoice Batch Run records.

=== ARTICLE: ind.billing_invoices_void.htm ===
---
article_id: ind.billing_invoices_void.htm
title: Void Invoices
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_invoices_void.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Void Invoices

Simplify invoice corrections by voiding posted invoices directly from the Invoice record.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create credit memos:	

Billing Admin permission set

OR

Billing Operations User permission set

From the App Launcher, find and select Invoices.
Open the posted invoice that you want to void.
Click Void Invoice.

Billing creates a credit memo that mirrors the original invoice. The invoice status changes to Void in Progress while the process completes. The related billing schedules are updated automatically to reflect the voided invoice. The related taxes are voided automatically, and the credit memo status updates based on the tax engine's response.

If an invoice remains in Void in Progress status for a long time, you can recover it by using the Billing Schedule Recovery API. Recovery restores the invoice to the Posted status, allowing you to take corrective action.

NOTE You can void invoices in reverse chronological order, starting with the most recent invoice. You can't void invoices that credit memos, payments, or write-offs have partially or fully settled.
Tax Implications of Invoice Voids
Learn how voiding an invoice cancels its associated taxes and affects the status of related credit memos.

=== ARTICLE: ind.billing_issue_unreferenced_refund.htm ===
---
article_id: ind.billing_issue_unreferenced_refund.htm
title: Issue Refund Against a Credit Memo
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_issue_unreferenced_refund.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_unreferenced_refunds.htm
fetched_at: 2026-09-04
---

# Issue Refund Against a Credit Memo

Return an available credit balance to a customer by issuing a refund against a credit memo, paid to a saved payment method on a third-party gateway.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To issue an unreferenced refund:	

Payment Admin permission set

OR

Payment Operations User permission set

Before you issue an unreferenced refund, confirm that the customer has an available credit balance on the credit memo, that the account uses a supported third-party payment gateway, and the payment gateway supports processing of unreferenced refunds. Also, make sure that a saved card payment method is available on the credit memo or billing account.

Open the credit memo that has the available credit balance you want to refund.
Confirm the available credit balance and the saved payment method on the credit memo.
If no saved payment method is stamped on the credit memo, Billing resolves one from the billing account. To refund to a specific card, select the saved payment method on the credit memo.
Issue the refund against the credit memo or a credit memo line, and enter the refund amount.
With header-level application, the refund applies to the credit memo as a whole. With line-level application, Billing distributes the refund amount across the credit memo charge lines that have an open balance, starting with the line that has the largest open balance.
Submit the refund.
Billing sends the refund to the saved payment method through the third-party payment gateway and reduces the outstanding credit balance. On a synchronous gateway, the refund status changes to Processed. On an asynchronous gateway, the status stays Pending until the gateway confirms the refund, and then changes to Processed.
EXAMPLE

A customer has an available credit balance of $200 on a credit memo set for header-level application. You issue an unreferenced refund of $200 against the credit memo, paid to the customer's saved card. Billing reduces the credit memo's pending balance by $200 and sets the refund balance to zero.

To confirm the refund reached the customer, check the refund status. If the status stays Pending on an asynchronous gateway, wait for the gateway to confirm the refund before you take further action.

=== ARTICLE: ind.billing_legal_entities_manage.htm ===
---
article_id: ind.billing_legal_entities_manage.htm
title: Legal Entities
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entities_manage.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_financial_accounting.htm
fetched_at: 2026-09-04
---

# Legal Entities

A legal entity defines how your organization is structured. In Revenue Management, you can create multiple legal entities, which define the billing and tax information for an order product. If you have customers and business segments in different tax locations, use multiple legal entities to govern the use of tax treatments, billing treatments, finance periods, and finance books.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Create Legal Entities in Revenue Management
Create legal entities to manage the billing and tax information for order products.
Legal Entity Automatic Population, Usage, and Considerations
Legal entity is a required value for financial accounting. It's either specified or automatically populated when billing transaction records are created. Explore the usage of legal entity and considerations of editing legal entity on the billing transactions.

=== ARTICLE: ind.billing_legal_entity_accounting_period_closure_importance.htm ===
---
article_id: ind.billing_legal_entity_accounting_period_closure_importance.htm
title: Importance of Legal Entity Accounting Period Closure
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entity_accounting_period_closure_importance.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entity_accounting_periods_close_and_reopen.htm
fetched_at: 2026-09-04
---

# Importance of Legal Entity Accounting Period Closure

Closing an accounting period, both at the legal entity level and the enterprise accounting period level, is a formal act that signifies all transactions within that period are posted from sub-ledger to your enterprise general ledger.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management (formerly Revenue Cloud)


The feature is available for the Invoice and Credit memo records, and their related records with the Revenue Cloud Advanced license or the Revenue Cloud Billing license.

This feature is available for the Payment, Refund, and Debit Memo records, and their related records with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

Closing an accounting period is a critical step in the accounting cycle that ensures accuracy and finality of financial statements.

Accurate transaction details: When accounting periods are closed, transaction records are updated to have the latest closing balances. These closing balances are copied as the opening balances for the next period.
Prerequisite to close legal entity accounting period: Closing the previous period and creating next period is often a prerequisite for fully recognizing transactions in the current period.
Prerequisite to close next period: Closing the current period is often a prerequisite for fully recognizing transactions in the subsequent period, maintaining a clean progression of financial cycles.
Example: Streamlining Accounting Period Closure

Continuing with Innovate Solutions Corp.'s journey, after successfully assigning legal entities to accounting periods and the system associating the billing transactions with their accounting periods, they further streamline their accounting period closures.

Streamlined Legal Entity Accounting Period Closure: At the end of the month, accounting teams close the legal entity accounting periods. A maximum of 3 Data Processing Engine (DPEs) definitions are run automatically based on the licenses your Salesforce org has, to close the legal entity accounting period.
Accounting Period Closure: After all legal entity accounting periods for a period were closed across all legal entities, the accounting period itself is closed, indicating the accounting period is closed as well in there enterprise general ledger.

This comprehensive process significantly reduces time to reconcile and improves audit readiness for Innovate Solutions Corp.

=== ARTICLE: ind.billing_legal_entity_accounting_period_reopen.htm ===
---
article_id: ind.billing_legal_entity_accounting_period_reopen.htm
title: Reopen a Legal Entity Accounting Period
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entity_accounting_period_reopen.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entity_accounting_periods_close_and_reopen.htm
fetched_at: 2026-09-04
---

# Reopen a Legal Entity Accounting Period

Reopen legal entity accounting periods to reconcile any previous journal entries. This exercise helps maintain accurate and compliant financial records during accounting period closure.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


This feature is available for the Invoice and Credit Memo records, and their related records with the Revenue Management Advanced license or the Revenue Management Billing license.

This feature is available for the Payment, Refund, and Debit Memo records, and their related records with the Revenue Management Billing license. Contact your Salesforce account executive for more information.

The Delete Transaction Journals with Unrealized Foreign Exchange Gains or Losses data processing engines is available only with the Revenue Management Billing license.

USER PERMISSIONS NEEDED
To reopen legal entity accounting periods:	

Accounts Receivables Admin permission set

AND

Data Pipelines Base User permission set

Before reopening a legal entity accounting period, make sure the status of the related Accounting Period record is Open.

NOTE Make sure that data pipelines is enabled. See Enable Data Piepelines.
Open the legal entity accounting period that you want to reopen.
Click Reopen Legal Entity Accounting Period and confirm that you want to reopen it.

When you click Reopen Legal Entity Accounting Period, the Delete Transaction Journals with Unrealized Foreign Exchange Gains or Losses data processing engine deletes all unrealized foreign exchange gain and loss transaction journals that were created during the legal entity accounting period closure. The Legal Entity Accounting Period record opens immediately and its status changes to Reopened.

SEE ALSO
Close Legal Entity Accounting Periods

=== ARTICLE: ind.billing_legal_entity_accounting_periods_close.htm ===
---
article_id: ind.billing_legal_entity_accounting_periods_close.htm
title: Close Legal Entity Accounting Periods
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entity_accounting_periods_close.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entity_accounting_periods_close_and_reopen.htm
fetched_at: 2026-09-04
---

# Close Legal Entity Accounting Periods

Maintain financial data integrity and accurate reporting by finalizing all transactions and closing the legal entity accounting periods at the end of their related accounting periods.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management (formerly Revenue Cloud)


The feature is available for the Invoice and Credit memo records, and their related records with the Revenue Cloud Advanced license or the Revenue Cloud Billing license.

This feature is available for the Payment, Refund, and Debit Memo records, and their related records with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

USER PERMISSIONS
NEEDED
To close legal entity accounting periods:	

Accounts Receivables Admin permission set

AND

Data Pipelines Base User permission set

Before closing the legal entity accounting period, make sure these settings are configured in your Salesforce org.

Enable Data Pipelines
Turn on Create Transaction Journals for Transactions feature
Turn on Create Transaction Journals for Foreign Exchange Gains or Losses feature, and select the required general ledger accounts
Select a default DPE definition to close legal entity accounting period
If required, enable Multiple currencies and set the dated exchange rates
NOTE If your Billing Admin deletes a dated exchange rate entry, Salesforce recommends running data sync manually before closing the legal entity accounting period.

See Set Up Financial Accounting Features.

Open the record of the legal entity accounting period that you want to close.
Click Close Legal Entity Accounting Period and confirm that you want to close it.

After clicking Close Legal Entity Accounting Period, three data processing engine jobs run in a sequence. See Understand the Legal Entity Accounting period Closure Procedure.

Legal Entity Accounting Period Closure Procedure
When you close legal entity accounting period, the system runs three Data Processing Engine (DPE) definitions in a sequence.
Example: Automatically Capture Unrealized Foreign Exchange Unrealized Gains or Losses
Explore an example to understand how to a set up general ledger accounts on the Salesforce org's default general ledger accounts and create dual transaction journals and reversal transaction journals to capture unrealized gains or losses amount of the invoices during legal entity accounting period closure.

=== ARTICLE: ind.billing_legal_entity_accounting_periods_close_and_reopen.htm ===
---
article_id: ind.billing_legal_entity_accounting_periods_close_and_reopen.htm
title: Legal Entity Accounting Periods Closure and Reopening
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entity_accounting_periods_close_and_reopen.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_financial_accounting.htm
fetched_at: 2026-09-04
---

# Legal Entity Accounting Periods Closure and Reopening

Close legal entity accounting periods and accounting periods after their duration ends to maintain data integrity. Reopen legal entity accounting periods to reconcile receivable transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management (formerly Revenue Cloud)


The feature is available for the Invoice and Credit memo records, and their related records with the Revenue Cloud Advanced license or the Revenue Cloud Billing license.

This feature is available for the Payment, Refund, and Debit Memo records, and their related records with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

Importance of Legal Entity Accounting Period Closure
Closing an accounting period, both at the legal entity level and the enterprise accounting period level, is a formal act that signifies all transactions within that period are posted from sub-ledger to your enterprise general ledger.
Close Legal Entity Accounting Periods
Maintain financial data integrity and accurate reporting by finalizing all transactions and closing the legal entity accounting periods at the end of their related accounting periods.
Reopen a Legal Entity Accounting Period
Reopen legal entity accounting periods to reconcile any previous journal entries. This exercise helps maintain accurate and compliant financial records during accounting period closure.
Close an Accounting Period
Close an accounting period after its duration ends and after all journal entries are validated for financial reporting of that period.

=== ARTICLE: ind.billing_legal_entity_accounting_periods_close_result.htm ===
---
article_id: ind.billing_legal_entity_accounting_periods_close_result.htm
title: Legal Entity Accounting Period Closure Procedure
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entity_accounting_periods_close_result.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entity_accounting_periods_close.htm
fetched_at: 2026-09-04
---

# Legal Entity Accounting Period Closure Procedure

When you close legal entity accounting period, the system runs three Data Processing Engine (DPE) definitions in a sequence.

This feature is available for the Invoice and Credit Memo records, and their related records with the Revenue Management Advanced license or the Revenue Management Billing license.

This feature is available for the Payment, Refund, and Debit Memo records, and their related records with the Revenue Management Billing license. Contact your Salesforce account executive for more information.

The Create Transaction Journals for Unrealized Foreign Exchange Gains or Losses and Create General Ledger Accounting Period Summary Records for Multiple Currencies data processing engines are available only with the Revenue Management Billing license.

DPE Execution Sequence

These Data Processing Engine definitions are executed in this sequence based on the licenses and currency settings in your Salesforce org.

DATA PROCESSING ENGINE	REVENUE MANAGEMENT ADVANCED LICENSE	REVENUE MANAGEMENT BILLING LICENSE WITH SINGLE CURRENCY	REVENUE MANAGEMENT BILLING LICENSE WITH MULTIPLE CURRENCIES	REVENUE MANAGEMENT BILLING LICENSE WITH ADVANCED CURRENCY MANAGEMENT


Close Legal Entity Accounting Period (Basic)

Or

Close Legal Entity Accounting Period (Advanced)

	Close Legal Entity Accounting Period (Basic) DPE runs and closes the legal entity accounting period.	Close Legal Entity Accounting Period (Advanced) DPE runs and closes the legal entity accounting period.	Close Legal Entity Accounting Period (Advanced) DPE runs and closes the legal entity accounting period.	Close Legal Entity Accounting Period (Advanced) DPE runs and closes the legal entity accounting period.
Create Transaction Journals for Unrealized Foreign Exchange Gains or Losses	Not Available	Not Available	Create Transaction Journals for Unrealized Foreign Exchange Gains or Losses DPE runs and creates transaction journals.	

Create Transaction Journals for Unrealized Foreign Exchange Gains or Losses DPE runs and creates transaction journals.




Create General Ledger Accounting Period Summary Records for Multiple Currencies

Or

Create General Ledger Accounting Period Summary Records

	Not Available	Create General Ledger Accounting Period Summary Records DPE runs and creates summary records.	Create General Ledger Accounting Period Summary Records for Multiple Currencies DPE runs and creates summary records.	

Create General Ledger Accounting Period Summaries Using Dated Conversion Rates DPE runs and creates summary records.

DPE: Close Legal Entity Accounting Period

The Close Legal Entity Accounting Period DPE starts a batch calculation job that sets the legal entity accounting period's status to Pending Closure and closure stage to Closing Legal Entity Accounting Period. It then evaluates all the billing transactions related to the legal entity accounting period with these field values.

BILLING TRANSACTION RECORD	FIELD VALUE
Invoice	The status is Posted.
Invoice Line	The status of the parent invoice is Posted.
Invoice Line Tax	The tax processing status is Posted.
Credit Memo	The status is Posted.
Credit Memo Line	The status is Posted.
Credit Memo Line Tax	The calculation status is Complete.
Credit Memo Line Invoice Line	All the records related to the legal entity accounting period are evaluated.
Payment	The status is Processed.
Payment Line Invoice	All the records related to the legal entity accounting period are evaluated.
Payment Line Invoice Line	All the records related to the legal entity accounting period are evaluated.
Refund	The status is Processed.
Refund Line Payment	All the records related to the legal entity accounting period are evaluated.
Debit Memo Line	The status of the related debit memo is Posted.

The DPE definition evaluates the related billing transactions with these statuses. If any of the billing transactions don't have a legal entity accounting period, the batch calculation job assigns a legal entity accounting period to those transactions.

DPE: Create Transaction Journals for Unrealized Foreign Exchange Gains or Losses

The Create Transaction Journals for Unrealized Foreign Exchange Gains or Losses data processing engine starts a batch calculation job to calculate unrealized foreign exchange gains and losses and create dual transaction journals and dual reversal transaction journals.

Field update: The DPE batch calculation job sets the Closure Stage field of the legal entity accounting period to Creating Unrealized Gain or Loss Transaction Journals.
Records considered: All the unsettled and partially settled posted invoices that aren't in corporate currency related to the legal entity accounting period are considered.
Unrealized foreign exchange gains and losses calculation: The difference between the dated conversion rate value on the invoice date and on the end date of the accounting period of the legal entity is calculated.
Transaction journals:
The calculated unrealized gain or loss amount is captured as debit and credit entry of transaction journals for the unrealized gains, unrealized loss, and account receivable general ledger accounts selected on the Billing Settings page.
Two reversal transaction journals are also created on the start date of the next legal entity accounting period. Reversal transaction journals record the same debit and credit amounts as the unrealized transaction journals, but for the opposite general ledger accounts.

See Use Case: Automatically Capture Unrealized Foreign Exchange Unrealized Gains or Losses.

NOTE If multiple currencies aren't enabled in your Salesforce org, then the Create Transaction Journals for Unrealized Foreign Exchange Gains or Losses DPE definition isn't executed.
DPE: Create General Ledger Accounting Period Summary Records for Multiple Currencies

The Create General Ledger Accounting Period Summary for Multiple Currencies DPE definition starts a batch calculation job to calculate the total credit amount, total debit amount, opening balance amount, and closing balance amount for a general ledger account that has transaction journals related to the legal entity accounting period.

Field update: The DPE batch calculation job sets the Closure Stage field of the legal entity accounting period to Creating General Ledger Accounting Period Summaries.
DPE calculation: The DPE definition calculates the amount fields based on the dated conversion rate on the end date of the accounting period related to the legal entity accounting period.
DPE execution logic: There are three DPE definitions. The currency settings configured in your Salesforce org determine which DPE definition runs.
ORG CURRENCY SETTINGS	EXECUTED DPE	FILTERED RECORDS


Both multiple currency and Advanced currency management are disabled

	

Create General Ledger Accounting Period Summary Records DPE runs.

	

The transaction journals are filtered for the legal entity accounting period and opening balance and closing balance are calculated.


Multiple currency is enabled	Create General Ledger Accounting Period Summary Records for Multiple Currencies DPE definition runs.	

All transaction journals for the legal entity accounting period are filtered. The debit and credit amounts of transaction journals that are in a currency other than the legal entity currency are converted into the currency of the legal entity using conversion rates, and then the opening and closing balances are calculated.


Advanced currency management is enabled	

Create General Ledger Accounting Period Summaries Using Dated Conversion Rates DPE runs.

	

All transaction journals for the legal entity accounting period are filtered. The debit and credit amounts of transaction journals that are in a currency other than the legal entity currency are converted into the currency of the legal entity using dated conversion rates, and then the opening and closing balances are calculated.

Result: After the successful execution of the DPE definition, two General Ledger Accounting Period Summary records are created for each general ledger account.
A summary record is created for the legal entity accounting period that's being closed.
A summary record is created for the next legal entity accounting period where the closing balance amount from the current period's record becomes the opening balance for the next period's record.
Go to the related list of the legal entity accounting period to view all the related general ledger accounting period summaries.
Considerations and Limitations
You can manually create a General Ledger Accounting Period Summary record only when the legal entity accounting period status is Open.
Only one General Ledger Accounting Period Summary record can exist for a unique combination of a general ledger account and a legal entity accounting period.
The DPE definition updates any existing General Ledger Accounting Period Summary record with the calculations.
You can manually update the general ledger accounting period summaries only when the status of the related legal entity accounting period is set to Open, Pending Closure, or Reopened.
If the Type field isn't selected on the general ledger accounts, the data processing engine fails and a revenue transaction error log is created.
Result and Error Logs

The fields on the Legal Entity Accounting Period record are updated based on the execution of the DPE definitions.

DPE OUTCOME	RECORD STATUS	RECORD UPDATES	NOTES
Success	The Closure Stage field is set to Completed and Status field is set to Closed.	

The Total Assets Amounts, Total Liabilities Amounts, Total Equities Amount, Total Revenue Amounts, and Total Expenses Amount fields on the legal entity accounting period are automatically updated.

In a Salesforce org with multiple currencies enabled, these fields show values in the legal entity accounting period's currency.

	The calculation of total assets, liabilities, equity, revenue, and expenses for a legal entity accounting period doesn't consider the general ledger accounting period summaries created for the foreign exchange realized and unrealized gain and loss general ledger accounts that are selected on the Billing Settings page.
Error	The Closure Stage field shows the specific DPE definition that encountered the error, and Status is set to Error.	A revenue transaction error log is created.	The revenue transaction error log is found on the related list of the legal entity accounting period.
Monitor Batch Calculation Job

Go to Monitor Workflow Services in Setup to check the status of the batch calculation job.

SEE ALSO
Set Up Financial Accounting Features
Example: Automatically Capture Unrealized Foreign Exchange Unrealized Gains or Losses

=== ARTICLE: ind.billing_legal_entity_accounting_periods_create.htm ===
---
article_id: ind.billing_legal_entity_accounting_periods_create.htm
title: Assign Legal Entities to Accounting Periods
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entity_accounting_periods_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_accounting_periods.htm
fetched_at: 2026-09-04
---

# Assign Legal Entities to Accounting Periods

Assign legal entities to accounting periods, and associate each billing transaction to a specific accounting period of a legal entity.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create legal entity accounting periods:	Accounts Receivables Admin permission set

Before you assign a legal entity to an accounting period, make sure that you create legal entities and accounting periods.

From the App Launcher, find and select Legal Entity Accounting Periods.
Click New.
Select the legal entity that you want to assign to an accounting period.
Select Open as the status.
When you create legal entity accounting periods, the status can only be set to Open.
Select an accounting period for the legal entity.
See Considerations for Selecting Accounting Period.
Save your work.

The name of the Legal Entity Accounting Period record is automatically generated by combining the names of the legal entity and the accounting period. Legal Entity Accounting Period records appear in the Legal Entity Accounting Periods related list of the specified Accounting Period record.

To view the related billing transactions on Legal Entity Accounting Period records, add the billing transaction related lists to the Legal Entity Accounting Period page layout. For example, add the Invoices related list.

NOTE You can't delete Legal Entity Accounting Period records.
Considerations and Result
Review the considerations for selecting a valid accounting period. Learn how legal entities assigned to accounting periods are automatically populated on the billing transactions.

=== ARTICLE: ind.billing_legal_entity_accounting_periods_create_result.htm ===
---
article_id: ind.billing_legal_entity_accounting_periods_create_result.htm
title: Considerations and Result
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entity_accounting_periods_create_result.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entity_accounting_periods_create.htm
fetched_at: 2026-09-04
---

# Considerations and Result

Review the considerations for selecting a valid accounting period. Learn how legal entities assigned to accounting periods are automatically populated on the billing transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Considerations for Selecting Accounting Period

When you select an accounting period while assigning legal entities to accounting periods, keep these considerations in mind:

The accounting period can't overlap with any existing accounting period for the same legal entity.
There can't be any gaps between the selected period, and the previous or next accounting periods for the same legal entity.
The total duration between the earliest and latest accounting period for a single legal entity can't be longer than 10 years.
How Are Legal Entity Accounting Periods Auto-Populated?

After legal entity accounting periods are created, they are auto-populated on billing transactions as mentioned in this table:

SCENARIO	BEHAVIOR
No legal entity is selected for the billing transaction.	The system uses the legal entity accounting period that's related to the default legal entity of your Salesforce org.
No open legal entity accounting period is available for the legal entity and date of the billing transaction.	The billing transaction record is created without any legal entity accounting period.

For transaction journal records created for the general ledger account assignment rules, the legal entity accounting period is derived from the transaction type record.

All the related billing transactions appear on the related list of the Legal Entity Accounting Period record.

Usage of Legal Entity Accounting Period

During the legal entity accounting period closure, the system validates the billing transaction record's legal entity and transaction date with the legal entity accounting period. See Legal Entity Accounting Period Closure Procedure.

Considerations for Editing Legal Entity Accounting Period

Review these considerations before editing the Legal Entity Accounting Period field on billing transactions.

The legal entity accounting period field can't be edited if the specified legal entity accounting period is closed.
The legal entity of the new legal entity accounting period must be same as the legal entity of the billing transaction.
When a legal entity accounting period is missing on the billing transaction, specify a legal entity accounting period that's in Open or Reopen status where the date of the billing transaction is within the accounting period's start and end dates. If that legal entity accounting period is closed, specify the next open legal entity accounting period.
When legal entity is edited on a billing transaction, update the billing transaction's Legal Entity Accounting Period field manually.
If the Legal Entity Accounting Period field is automatically updated when you edit the legal entity of a billing transaction, or if you edit the Legal Entity Accounting Period field on a billing transaction record for which transaction journals and general ledger accounting period summaries have been created, then:
Manually update the Legal Entity Accounting Period field on the transaction journals created for the general ledger accounting assignment rule.
Reopen and close Legal Entity Accounting Period record to update the foreign exchange unrealized gain and loss transaction journals and the general ledger accounting period summaries.
Manually update the existing foreign exchange realized gain and loss transaction journals that are created for the Payment Line Invoice, Payment Line Invoice Line, and Credit Memo Line Invoice Line records.

=== ARTICLE: ind.billing_legal_entity_default.htm ===
---
article_id: ind.billing_legal_entity_default.htm
title: Legal Entity Automatic Population, Usage, and Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_legal_entity_default.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_legal_entities_manage.htm
fetched_at: 2026-09-04
---

# Legal Entity Automatic Population, Usage, and Considerations

Legal entity is a required value for financial accounting. It's either specified or automatically populated when billing transaction records are created. Explore the usage of legal entity and considerations of editing legal entity on the billing transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Legal Entity Autopopulated for Billing Schedule Groups

The legal entity is automatically populated on billing schedule groups in this sequential order.

SCENARIO	LEGAL ENTITY USED
Legal entity is selected for the related order item.	Legal entity of the related order item
Legal entity is selected for the related order.	Legal entity of the related order
Legal entity isn't selected for the related order or order item.	Default legal entity of your Salesforce org
Legal Entity Autopopulated for Billing Transactions

The legal entity is populated automatically on billing transaction records in this sequential order.

SCENARIO	LEGAL ENTITY USED
Legal entity is selected for the billing transaction.	The selected legal entity
Legal entity isn't selected for the billing transaction.	Legal entity from the parent or the related record of the billing transaction
Legal entity isn't selected for the billing transaction record, its parent record, or its related record.	Default legal entity of your Salesforce org
Derivation of Legal Entities from Parent or Related Records

This table specifies the parent or the related record that the billing transaction derives its legal entity from.

BILLING TRANSACTION	LEGAL ENTITY DERIVED FROM
Invoice	The related Billing Schedule Group record
Invoice Line	The parent Invoice record
Invoice Line Tax	The parent Invoice Line record
Credit Memo	The Invoice record that's specified in the Reference Entity field
Credit Memo Line	The parent Credit Memo record
Credit Memo Line Tax	The parent Credit Memo Line record
Credit Memo Line Invoice Line	The related Invoice Line record
Payment	Default legal entity of your Salesforce org
Payment Line Invoice	The related Invoice record
Payment Line Invoice Line	The related Invoice Line record
Refund	Default legal entity of your Salesforce org
Refund Line Payment	The related Payment record
Debit Memo	Default legal entity of your Salesforce org
Debit Memo Line	The parent Debit Memo record
Usage of Legal Entities

After automatic population of legal entity on billing transactions, the legal entity is used in these scenarios.

Legal Entity Based Tax Treatment: When you choose legal entity as the treatment selection during tax policy creation, the system selects the tax treatment based on the legal entity and populates it on the order product or quote line item. This tax treatment is then used for the tax calculation. See Create Tax Policies and Treatments.
Invoice Grouping: When the invoice grouping type on the billing schedule is set to default or custom, the system uses the billing schedule group's legal entity along with other fields that make a default group to consolidate invoice records. See Define Invoice Grouping on a Billing Schedule.
Settle invoice lines based on legal entity: During the credit application process, the system validates the invoice line and credit memo line for a matching legal entity. The system applies the credit memo line to an invoice line only if it finds a matching legal entity on the invoice line. See Create and Apply Credit Memos to Invoice Lines.
Financial Accounting Usage:
Automatic Population of Legal Entity Accounting Period: When legal entity of a billing transaction is autopopulated, its legal entity accounting period is also automatically populated. See Assign Legal Entities to Accounting Periods
Transaction Journal creation: During transaction journal creation for the general ledger account assignment rule, the system validates if the transaction type's legal entity matches the general ledger account assignment rule's legal entity. See General Ledger Account Assignment Rules and Related Records.
Legal Entity Accounting Period (LEAP) Closure: During legal entity accounting period closure, the system validates billing transaction records that match the legal entity accounting period's legal entity and are within the start and end dates of its accounting period. See Close Legal Entity Accounting Periods.
Considerations for Editing Legal Entity on Billing Transactions

Review these considerations before you edit the Legal Entity field on billing transactions.

The Legal Entity field on billing transactions is editable regardless of the billing transaction's status.
When you edit the legal entity of a billing transaction, update the legal entity accounting period of the billing transaction manually. See Assign Legal Entities to Accounting Periods.
The legal entity is automatically populated only when a Billing Transaction record is created. When the Legal Entity field is updated on a billing transaction, the Legal Entity field on its related records must be manually updated.
If you edit the Legal Entity field on billing transaction records for which transaction journals are created, then:
Manually update the Legal Entity field on the transaction journals created for the general ledger accounting assignment rule.
Manually update the existing foreign exchange realized gain and loss transaction journals that are created for the Payment Line Invoice, Payment Line Invoice Line, and Credit Memo Line Invoice Line records.
Reopen and close Legal Entity Accounting Period record to update the legal entity field for the foreign exchange unrealized gain and loss transaction journals.

=== ARTICLE: ind.billing_limits.htm ===
---
article_id: ind.billing_limits.htm
title: Limits in Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_limits.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Limits in Billing

Review the default limits for Billing features.

Billing Business API Limits

See Billing Business API Limits to learn about the default limits on the usage of the Billing business APIs.

Total Heap Size Limit for Custom Tax Engine Apex Adapter

From Summer ’25, Billing supports up to 2000 invoice lines for a single invoice. To avoid limit-related issues, test your TaxEngineAdapter Apex interface’s implementation to make sure that it adheres to the Apex limit for total heap size.

See Prerequisites for a Partner or Custom Tax Engine.

Invoice Lines Limit for Invoice Batch Runs

Invoice batch runs can generate a maximum of 2000 invoice lines for an invoice. Since invoice runs use Data Processing Engine, it is crucial to also understand the default limits for Data Processing Engine and Data Pipelines. These underlying limits can impact the overall invoice generation by batch runs.

You can have a maximum of 30 active billing batch schedulers.

See Automated Invoice Generation with Invoice Batch Runs.

Document Generation Request Limits

Before generating invoice PDF documents, review the default limits for document generation requests and the process for increasing the maximum number of content versions that are published per day.

See Generate a Batch of Invoice PDF Documents.

Email Limits

A maximum of 5000 emails can be sent to the email address on Bill to Contact records daily. To send emails beyond the daily limit, enable customer user for the Bill to Contact record. Emails sent to customer community users are not counted against the 5000 daily email limit. The system first checks for a customer community user before considering the email address on the Bill to Contact record.

See Send Invoices Through Email.

=== ARTICLE: ind.billing_manage_disputes.htm ===
---
article_id: ind.billing_manage_disputes.htm
title: Manage Billing Disputes
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_manage_disputes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Manage Billing Disputes

Fragmented billing dispute processes often lead to payment delays and poor customer experience. By using the dispute management feature, you can streamline the intake and resolution process for common billing requests and disputes. Install pre-built service process templates by using Unified Catalog. Your billing specialists and customer service representatives can initiate cases directly from the Account record page, and quickly capture, validate, and resolve common inquiries, all from a single catalog. Billing portal users can raise service requests through the self-service Billing portal.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Key Features

Billing Dispute Management centralizes billing inquiries into one automated system and reduces the time to resolve common billing inquiries and disputes.

Unified dispute management platform: Centralize all billing inquiries, service requests, and disputes in a single system and get real-time visibility and tracking for both customers and internal teams.
Automated resolution capabilities: Use out-of-the-box service process templates in Unified Catalog. Enable automated resolution actions for issuing credit memos, suspending billing, extending due date, and updating contact details.
Self-Service customer experience: Enable your customers to use the Billing service catalog to raise billing requests or dispute invoice charges. Help customers track the progress of their inquiries or disputes, and receive automated status updates via email.
Integrated case management: Enable your billing specialists and customer service reps to verify, edit, and resolve billing case details by using the Resolve Case quick action that triggers automated workflows.
Assisted Case Creation: Streamline the end-to-end workflow for dispute management for internal users such as billing specialists and customer service representatives in your Salesforce org. Enable your service reps to initiate and complete service requests directly on behalf of your customers. They can use the same service process templates available to community users on the Self-Service Billing portal.
Case Notifications: Get notification alerts when a new billing case is created for any service process request, so your service reps are notified immediately of any new billing inquiries or disputes.
Recent Billing Cases and Case Metrics: Review the recent list of billing cases for the account. Your service reps can use this history of cases for the account to identify patterns and make informed decisions. They can also view metrics for open billing cases and disputes on the Billing Operations Console homepage.
Billing Dispute Management Workflow

The dispute management feature provides an end-to-end process for handling billing inquiries and disputes through three interconnected workflows. From initial setup to final resolution, these workflows help you streamline dispute handling, reduce manual intervention, and provide transparent self-service capabilities for your customers. The dispute management lifecycle consists of three phases.

Initial Setup: Set up dispute management feature to assign permissions, object and field accesses, add community users, configure the self-service Billing portal, and install the service process templates. This one-time setup establishes the foundation for automated capture and processing of service requests raised by your community users.
Service Request Submission: The billing portal or community users initiate billing inquiries or raise invoice-related disputes by using the self-service portal. For every service request that’s submitted, billing automatically creates a case or dispute record that your billing specialist or customer service representative can review and resolve. Starting Summer ‘26, your service reps can also submit service requests and raise cases on behalf of the customer, directly using the Billing app. Depending on
Service Request Resolution: Your customer service representatives and billing specialists resolve the service requests directly from the case records. Depending on the type of service process request, Billing automatically runs the appropriate billing resolution whether it’s extending the invoice due date, updating the billing contact, suspending billing, or issuing credit memos.
Service Process Templates

The dispute management setup installs Unified Catalog templates for common billing inquiry and dispute scenarios. Each template corresponds to a type of service process request. The template includes an Omniscripts intake form, an email template to notify the customer upon successful case submission, and a predefined Resolve Case action on the case record. For example, when you install the Suspend Billing template, a service process with the same name is created, that you can then add to a catalog in Unified Catalog.

Suspend Billing: Temporarily pause or resume billing for services or subscriptions.
Update Bill To Contact on Invoice: Change billing contact for specific invoices with an optional default setting.
Extend Invoice Due Date: Extend the due date on a selected invoice.
Incorrect Invoice Charge: Report and correct incorrect charges on invoice or invoice lines.
Other Billing Inquiries: Raise any general billing inquiries or disputes that don’t have predefined service process templates.
Help Center and Cases Tabs on the Self-Service Billing Portal

The self-service billing portal is a dedicated portal that helps your customers log billing inquiries and disputes. They can use the Help Center and Cases tabs to raise case requests and track case status.

Help Center tab: This tab shows the billing service catalog with available service processes to raise requests. Your community users can navigate this tab to identify and run the service processes they need. The tab shows available service requests for suspending billing, updating bill-to contact, extending invoice due date, raising invoice charge disputes, and other billing inquiries.
Cases tab: Helps your community users monitor their case details, updates, and resolution information. Your customers can also track all active and historical billing inquiries.
Set Up Billing Dispute Management
Track and resolve billing inquiries, service requests, and invoice-related disputes by using Billing Dispute Management.
Raise Service Requests on Behalf of the Customer
Initiate billing disputes or inquiries on behalf of your customer directly from the Billing app.
Resolve Billing Service Requests
When customers or service reps raise billing service requests or inquiries , Billing creates corresponding cases that are resolved by using the automated resolution actions. For specific service requests such as suspending billing, extending invoice due date, updating billing contact details, or correcting invoice charges, Billing automatically initiates the appropriate resolution associated with the service request. However, for any other billing inquiries that don’t have automated resolution, resolve the cases manually based on the business need and requirements.
SEE ALSO
Set Up Billing Dispute Management
Self-Service Billing Portal
Raise Billing Inquiries and Invoice-Related Disputes

=== ARTICLE: ind.billing_migrate_saved_payment_methods.htm ===
---
article_id: ind.billing_migrate_saved_payment_methods.htm
title: Migrate Tokenized Saved Payment Methods
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_migrate_saved_payment_methods.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Migrate Tokenized Saved Payment Methods

Expand your payment ecosystem by bringing in externally tokenized payment methods into your Salesforce org. Bring in external payment method tokens generated by using buyer-facing portals or the Self-Service Billing portal, and save them as payment methods in your Salesforce org. These externally saved payment methods are immediately available for use in payments batch processing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To import payment method tokens:	

Payment Admin

OR

Payment Operations User

permission set


To embed third-party UI components on the self-service Billing portal:	Billing Portal User permission set
Import Existing Tokenized Payment Methods

Migrate your customers’ existing payment data into your org as saved payment method records. Import payment method tokens from native or third-party payment gateways, either individually or in bulk.

To import an existing payment method token, include the existing payment token and related tokenized details in your SavedPaymentMethod sObject API request.
For API details and examples, see Create a Saved Payment Method Using the sObject API.
To import multiple payment method tokens at once by using CSV files, use the Bulk API.

After importing the payment method tokens into your org, use the saved payment methods, without any further configuration, for both batch payment processing and in the Sale, Authorize, and Capture APIs.

Create Saved Payment Methods from Buyer-Facing Client-Side Components

Bring in saved payment methods into your Salesforce org by tokenizing your customers’ payment details using buyer-facing client-side components. You can use this method to bring in tokens for payment method categories such as alternative payment methods, digital wallets, and credit cards.

Get your customers to save their payment details on your storefront or client-side component. The client-side component tokenizes the payment information by using a third-party payment gateway. The payment gateway then returns a payment method token and related payment metadata. Using the tokenized payment details, create a saved payment method synchronously or asynchronously.
You can also bring in saved payment methods by customizing the Self-Service Billing portal to add third-party UI components.

After creating saved payment methods from buyer-facing portal or the Self-Service Billing portal, you can use the newly added saved payment methods for payments processing.

SEE ALSO
Object Reference: SavedPaymentMethod
Bulk API 2.0 and Bulk API Developer Guide: Walkthrough for Bulk Insert
Self-Service Billing Portal

=== ARTICLE: ind.billing_milestone_amended_renewed_canceled_assets.htm ===
---
article_id: ind.billing_milestone_amended_renewed_canceled_assets.htm
title: Milestone Billing for Amended, Renewed, and Canceled Assets
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_milestone_amended_renewed_canceled_assets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_milestone_plans.htm
fetched_at: 2026-09-04
---

# Milestone Billing for Amended, Renewed, and Canceled Assets

Handle milestone plans during amendments, renewals, and cancellations to ensure accurate billing. By default, milestone-based billing doesn’t create new milestone plans or plan items for amend or renew orders. When the Support Milestone Plans for Amended Billing Schedules setting is enabled, Billing creates or links a milestone plan to the amendment schedule and recalculates milestone dates and amounts from the amendment start date.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Amendment Scenarios

When you amend an asset with a milestone billing plan:

Amendments with a milestone-enabled billing treatment create a new billing milestone plan based on the amendment and link it to the amendment billing schedule. Milestone dates and amounts are recalculated from the amendment start date.
Amendments with a non-milestone billing treatment are processed as one-time billing schedules, and no billing milestone plan is created.
Amendments that include a preconfigured or negotiated billing milestone plan link the provided milestone plan directly to the amendment billing schedule.
Amendments without a billing treatment use the billing treatment from the original billing schedule group to create a new billing milestone plan based on the amendment details. They don’t reuse the original milestone plan.
Cancellation Behavior

When you cancel an asset with a milestone billing plan:

A cancellation billing schedule is created within the same billing schedule group, reflecting a negative amount equal to the cancellation order.
Invoiced milestones from the original billing milestone plan remain unchanged.
Date-based billing milestone plan items with milestone accomplishment dates on or after the cancellation date move to Canceled status.
Date-based billing milestone plan items with milestone accomplishment dates before the cancellation date remain active and are invoiced after the completion.
All uninvoiced event-based billing milestone plan items are marked as Canceled after the event-based milestone plan item on the original order is invoiced and posted. Until then, event-based milestone plan items can still be marked as Accomplished, but they remain uninvoiced.

Billing issues a credit memo for the difference between the original sale amount and the total invoiced billing milestone plan items, providing a partial credit for incomplete milestones.

The generated invoice lines reflect the net amount of the original sale and the canceled amount, similar to standard one-time or subscription cancellations.

=== ARTICLE: ind.billing_milestone_create.htm ===
---
article_id: ind.billing_milestone_create.htm
title: "Method 2: Create Billing Milestone Plans and Plan Items"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_milestone_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_milestone_methods.htm
fetched_at: 2026-09-04
---

# Method 2: Create Billing Milestone Plans and Plan Items

Create billing milestone plans, and then create billing milestone plan items to specify how billings are scheduled based on the completion of specific project milestones throughout the lifecycle of the order product.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To create billing milestone plans and plan items:	

Billing Admin permission set

OR

Billing Operations User permission set

Create Billing Milestone Plans
From the App Launcher, find and select Billing Milestone Plans.
Click New.
Enter a name for the billing milestone plan.
Select a billing treatment for the billing milestone plan.
Select Draft as the status.
If necessary, enter a description.
Select a reference item for which you want to create a billing milestone plan.
You can select a billing schedule, order product, quote line item, or an external reference item.
Save your changes.
Create Billing Milestone Plan Items
Open the billing milestone plan that you want to create the plan item for.
Click Configure Milestones.
You can create up to 20 milestones at once.
Select Billing Schedule Start Date as the milestone commencement trigger.
Enter a name for the billing milestone plan item.
Specify whether to set date-based or event-based milestones.
For the billing checkpoint to occur when you manually activate the milestone trigger by selecting Milestone accomplished, select Event. For example, you can invoice a client after completing a project phase, delivering a key output, or reaching a specific goal. This type of milestone makes sure that billing is directly linked to project progress and measurable achievements.
For the billing checkpoint to occur on a predefined date, which is calculated from the activation date of an order product, select Date. For example, you can configure a billing milestone plan item such that an invoice for the billing milestone plan item is generated one month after an order product is activated. By specifying the milestone commencement offset and milestone commencement unit, you can define the exact duration after which the date-based billing milestone becomes ready for invoicing. This method provides a predictable billing timeline, supporting efficient cash flow management and financial planning.
Select Draft as the status.
If necessary, enter a description.
For a date-based milestone, enter these values.
For the offset, specify the wait time from the commencement trigger to determine the milestone's accomplishment date.
For the offset unit, specify the time unit for the milestone commencement offset, such as days, months, or years. For example, if you activate a product on January 1 and set a 30-day milestone commencement offset, the milestone completes on January 31.
Specify the distribution method for the milestone amount.
Enter the percentage of the total billable amount for the reference item to be invoiced for this milestone.
Enter a flat amount to be invoiced for this milestone.
You can combine both the distribution methods within a single milestone billing plan.
Click Add Item to add the required milestone items and enter the necessary values.
Save the changes.
Update the status of the billing milestone plan to Active, and save the changes.
If needed, modify the uninvoiced billing milestone plan items.

Alternatively, on the Related tab, in the Billing Milestone Plan Items section, click New and follow the same configuration steps. After activating the billing treatment, you can view the milestones and update only the Milestone accomplished field for event-based milestones.

=== ARTICLE: ind.billing_milestone_methods.htm ===
---
article_id: ind.billing_milestone_methods.htm
title: Define Billing Milestones
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_milestone_methods.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_milestone_plans.htm
fetched_at: 2026-09-04
---

# Define Billing Milestones

Milestone billing is a flexible billing method where customers are billed at specific project checkpoints.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Methods to Create Billing Milestone Plans

Create billing milestone plans and milestone plan items from billing treatments and apply them to one or more products.

You can also create a billing milestone plan directly for an order product when the milestone requirement is specific to that product.

Method 1: Configure Billing Milestones Using Billing Treatments
Create billing milestone plans and billing milestone plan items from billing treatment and billing treatment items and apply them to one or more products. This method is ideal when multiple products follow the same milestone billing pattern. You can edit the billing milestone plans for individual order products without affecting the billing treatment.
Method 2: Create Billing Milestone Plans and Plan Items
Create billing milestone plans, and then create billing milestone plan items to specify how billings are scheduled based on the completion of specific project milestones throughout the lifecycle of the order product.

=== ARTICLE: ind.billing_milestone_plans.htm ===
---
article_id: ind.billing_milestone_plans.htm
title: Configure Milestone Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_milestone_plans.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Configure Milestone Billing

Bill projects in installments based on milestone achievements or predefined dates. Align payments with project progress and enhance customer satisfaction through timely invoicing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Define Billing Milestones
Milestone billing is a flexible billing method where customers are billed at specific project checkpoints.
Milestone Billing for Amended, Renewed, and Canceled Assets
Handle milestone plans during amendments, renewals, and cancellations to ensure accurate billing. By default, milestone-based billing doesn’t create new milestone plans or plan items for amend or renew orders. When the Support Milestone Plans for Amended Billing Schedules setting is enabled, Billing creates or links a milestone plan to the amendment schedule and recalculates milestone dates and amounts from the amendment start date.
Milestone Billing Example
Explore an example that shows how milestone billing ties invoices to project progress. Structured invoicing at key delivery points improves revenue accuracy, builds customer trust, and supports financial planning.

=== ARTICLE: ind.billing_milestone_treatment_and_item_create.htm ===
---
article_id: ind.billing_milestone_treatment_and_item_create.htm
title: "Method 1: Configure Billing Milestones Using Billing Treatments"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_milestone_treatment_and_item_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_milestone_methods.htm
fetched_at: 2026-09-04
---

# Method 1: Configure Billing Milestones Using Billing Treatments

Create billing milestone plans and billing milestone plan items from billing treatment and billing treatment items and apply them to one or more products. This method is ideal when multiple products follow the same milestone billing pattern. You can edit the billing milestone plans for individual order products without affecting the billing treatment.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create billing treatments and billing treatment items:	Billing Admin permission set
Configure Billing Treatments for Milestone Plan Items
Create a billing policy.
Create a billing treatment with Enable milestone billing selected.
Click Configure Milestones to create up to 20 milestones at once. For configuration steps, see Create Billing Milestone Plan Items.
Activate the Billing Treatment.

Alternatively, on the Related tab, in the Billing Treatment Items section, click New, and follow the configuration steps.

Configure Billing Treatment Items Template for Milestone Plan Items
Create a billing treatment item.
After you define the billing treatment item fields, enter these values in the billing milestone plan-specific fields before you save the changes.
OPTION	SELECTION
Zero Amount Behavior	None
Type	Percentage
Billing Type	None
Sequencing	None
Controller	None
Milestone Type	Specify whether the milestone is based on an event or a specific date. An event-based milestone is triggered when a specific event or task within a project is completed. Select the Milestone accomplished checkbox to manually trigger this checkpoint. A date-based milestone is scheduled on a specific date and is calculated from the activation date of an order product.
Milestone Commencement Trigger	For date-based milestones, specify that the milestone commencement aligns with the billing schedule start date.
Milestone Commencement Offset	For date-based milestones, specify the wait time from the commencement trigger to determine the milestone's accomplishment date.
Milestone Commencement Offset Unit	For date-based milestones, specify the time unit for the milestone commencement offset, such as days, months, or years. For example, if you activate a product on January 1 and set a 30-day milestone commencement offset, the milestone completes on January 31.

After you create an active billing treatment item, update the status of the related billing treatment to Active, and then update the status of the related billing policy to Active.

For milestone billing, activate the related order to automatically generate billing schedules, and create billing milestone plan and billing milestone plan items based on the specified billing treatment and billing treatment items inputs. The validation on the fields is run, and calculated fields are updated only when the order is activated.

=== ARTICLE: ind.billing_milestone_usecase.htm ===
---
article_id: ind.billing_milestone_usecase.htm
title: Milestone Billing Example
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_milestone_usecase.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_milestone_plans.htm
fetched_at: 2026-09-04
---

# Milestone Billing Example

Explore an example that shows how milestone billing ties invoices to project progress. Structured invoicing at key delivery points improves revenue accuracy, builds customer trust, and supports financial planning.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

ABC Corp has engaged TechBuild Solutions to design a customized software platform within 6 months. The project consists of four phases, each with clear deliverables and timelines. ABC Corp started billing for the order on January 1, 2025. To meet the billing requirements, TechBuild has adopted milestone-based billing, invoicing ABC Corp only after completing each milestone.

Milestone 1 - Requirement Gathering and Planning: 25% of total project fee, invoiced after planning is completed. The date of this milestone completion isn’t known in advance.
Milestone 2 - Design and Prototype: 20% of total project fee, invoiced after client approval of design. The date of this milestone completion isn’t known in advance.
Milestone 3 - Development: 30% of total project fee, invoiced after delivery of the functional prototype. The date of this delivery is scheduled as 4 months after the billing schedule start date.
Milestone 4 - Testing and Deployment: 20% of total project fee, invoiced after successful deployment and sign-off. The date of this milestone completion is 6 months after the billing schedule start date.
The remaining 5% is billed when all the milestones are invoiced.
Method 1: Create a Billing Treatment and Specify Billing Treatment Items for Each Milestone

You can edit the billing milestone plans for individual order products without impacting the billing treatment.

Billing Treatment: Default Milestone Treatment
Status: Draft
Enable milestone billing: Selected

Then, create the billing treatment items for the billing treatment.

After you activate the associated order, a billing milestone plan is automatically created and linked to the order product's billing schedule. To modify the created milestone plan, change its status from active to draft. You can then modify the Milestone Type, Milestone Commencement Trigger, Milestone Commencement Offset, Milestone Commencement Offset Unit, Percentage, Flat Amount, and Milestone accomplished fields on the milestone plan items. When the milestone plan is active, you can only update the Milestone accomplished field to mark the successful completion of an event.

Method 2: Create a Billing Milestone Plan and Define Milestone Plan Items for the Order Product

The total price of the order product is US$10000, with each milestone amount calculated based on its percentage value. Using the same attributes that you used in method 1 to create billing treatment items, create the billing milestone plan items. After you create them, set the status of the billing milestone plan items to draft and save them. The milestone amount is automatically distributed based on the distribution method value.

Requirement Gathering and Planning milestone amount: $2500
Design and Prototype milestone amount: $2000
Development milestone amount: $3000
Testing and Deployment milestone amount: $2000

A fifth billing milestone plan item with the remainder of the 5% with milestone amount of $500 is automatically generated after you activate the associated billing milestone plan. The status of the billing milestone plan items is automatically changed to the Waiting for Milestone Accomplishment status.

For example, the requirement gathering and planning milestone is finalized 2 months after the billing schedule start date. At this stage, the billing admin can manually mark the milestone as completed. When you save the milestone plan item, its status changes from Waiting for Milestone Accomplishment to Ready for Invoicing, and the milestone completion date is recorded. When the billing schedule is processed for invoicing, an invoice line is generated for the first milestone plan item, charging 25% of the total billable amount. At this point, the status of the milestone changes to Invoiced.

The remainder billing milestone plan item is always invoiced with the final milestone. If the final milestone is an event billing milestone plan item, the milestone type for the remainder line is updated to event.

=== ARTICLE: ind.billing_multiple_term_billing.htm ===
---
article_id: ind.billing_multiple_term_billing.htm
title: Bill for Multiple Terms in a Billing Period
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_multiple_term_billing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_and_schedule_groups.htm
fetched_at: 2026-09-04
---

# Bill for Multiple Terms in a Billing Period

Your sales reps can now set up flexible terms for billing subscriptions whether it’s every three weeks, every five months, or every two years. For example, to bill a subscription every three months, your sales reps can set the billing frequency to monthly and billing term to 3 on the order product. Billing automatically calculates the correct amount for the combined period and sets the next billing date accordingly.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
NOTE For orgs created in or upgraded to Winter ’27, perform a one-time task of adding the Billing Term Unit field on the Asset Action Source, Order Product, and Quote Line Item page layouts.

Sometimes a customer prefers to be billed for several periods at once, or you want to reduce the number of invoices that you generate. You can set how many billing term units to combine into a single billing period. When you combine multiple terms, Billing generates one billing period item for the combined period and adds one invoice line to the invoice, instead of a separate billing period item and invoice line for each period.

For example, for a monthly billing term unit and a billing term of 3, Billing combines 3 months into one billing period, generates one billing period item that covers all 3 months, and adds a single line to the invoice for that period. The billing period amount equals the unit price multiplied by the quantity and by the number of combined periods.

You can set the billing term on the order product or quote line item. Its default value is 1, which bills each period separately. However, to bill for multiple terms, you can enter a higher value up to 1,200, to combine that number of billing term units into one billing period. For both termed and evergreen products, you can combine multiple terms with weekly, monthly, quarterly, semiannual, and annual billing frequencies. For products that use the one-time selling model, leave the billing term blank or set it to 1.

=== ARTICLE: ind.billing_operations_console.htm ===
---
article_id: ind.billing_operations_console.htm
title: Billing Operations Console
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_operations_console.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Billing Operations Console

Monitor invoices, credit memos, and invoice schedules with ease. Manage billing transactions effectively with timely insights into revenue transaction log errors and failed invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

From the App Launcher, find and select Billing. From the navigation bar, click Home.

Key Metrics

View key financial data in summary cards to quickly assess billing activities.

Invoices: Track billing transactions with the total count and amount of invoices.
Draft Invoices: Review the total count and amount of draft invoices before finalizing the invoices.
Invoice Batch Runs: Monitor processing volume with the total number of completed batch runs.
Credit Memos: Track issued credits with the total count and amount of credit memos.
Invoice Management

Manage invoice schedules and batch runs within the console.

Next Invoice Run: View the upcoming invoice runs. Schedule new invoices or deactivate invoices in this section.
Invoice Batch Run Details: Review invoice batch run details for past runs. Retry document generation or recover failed batches from this section.
Issue Resolution

Resolve invoice issues efficiently.

Failed Invoices: Review invoices with processing errors, their status, account, and due date. Identify the issues and resolve them.
Billing Revenue Transaction Error Logs: Review revenue transaction error logs related to billing transactions with details such as the error message, creation date, and related records. Analyze the information to troubleshoot and fix billing errors.
Billing Metrics

View a summary of open billing activities.

Number of Open Billing Cases: The total count of active billing-related cases.
Open Disputes: The number of currently active disputes.
Disputed Invoices: A count of the distinct invoices that have been disputed.
Total Disputed Amount: The cumulative amount that’s currently in dispute.
Navigation Link: A configurable link that directs users to a case landing page or a specific report.
Filters

Use filters to customize the data shown on the dashboard.

Date range: View data from the last 7, 14, or 30 days.
Currency: View invoices, credit memos, and draft invoices in a specific currency.

=== ARTICLE: ind.billing_page_layout.htm ===
---
article_id: ind.billing_page_layout.htm
title: Add New Billing Fields to Page Layouts
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_page_layout.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup.htm
fetched_at: 2026-09-04
---

# Add New Billing Fields to Page Layouts

Provide users more context by adding new fields to the default page layouts each release.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

For Salesforce orgs provisioned in a particular release, the default page layouts include the new fields that were introduced in that release. If you're already using Billing before that release, add the new fields from the page layout settings of objects.

To identify the fields that were introduced in particular release, see the object documentation for the corresponding API version.

This completes the basic setup for Billing. To enable additional features, see Set Up Additional Billing Features. To proceed with the rest of the Revenue Management setup, see Set Up Revenue Cloud.

SEE ALSO
Knowledge Article: Find Salesforce Edition and API version
Page Layouts

=== ARTICLE: ind.billing_partner_or_custom_tax_engine.htm ===
---
article_id: ind.billing_partner_or_custom_tax_engine.htm
title: Partner or Custom Tax Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_partner_or_custom_tax_engine.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_configuration.htm
fetched_at: 2026-09-04
---

# Partner or Custom Tax Engine

When you need complex tax jurisdictions or already use a tax vendor, you connect a partner tax app or your own tax engine. The TaxEngineAdapter Apex interface retrieves information from the tax engine and evaluates the information to define tax details.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Prerequisites for a Partner or Custom Tax Engine
If you want to calculate taxes by using your own tax engine or by integrating the Billing TaxEngineAdapter Apex interface with a partner app, complete these prerequisites.
Configure Additional Tax Identification Details
Send additional tax identification details to your external tax engine. Meet regional tax compliance requirements by storing tax identification and exemption information on the Billing Account and passing it to the tax engine.
Extend the Revenue Cloud Tax Extension Engine
Enhance the existing tax interface by mapping additional fields for tax callouts. Use custom metadata types to send additional data in tax requests and persist more detailed information from tax responses.
Create a Tax Engine Provider and Tax Engine
If you use a partner app or your own engine, create a tax engine provider and a tax engine.

=== ARTICLE: ind.billing_payment_batch_run_overview.htm ===
---
article_id: ind.billing_payment_batch_run_overview.htm
title: Payment Batch Run Overview
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_batch_run_overview.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Payment Batch Run Overview

At the start time of the payment scheduler, payment batch runs start processing payment schedule items based on the defined criteria.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
Process Overview

Understand the steps involved in processing payment schedule items and applying the corresponding payments.

Payment batch runs process Payment Schedule Item records that are in the Ready for Processing status and are related to Payment Schedule records that are in the Open status.
A Payment record is created for each payment schedule item that’s successfully processed.
The payment batch run then applies the Payment record to the corresponding Invoice or Invoice Line record based on the payment application level.

Billing applies payments based on the descending order of invoice line balances, that is, a payment is first applied to an invoice line with the highest balance.

NOTE Payments can only be applied to invoices of the same currency.
Payment Methods

For automatically created payment schedules and payment schedule items, the payment gateway collects payments by using the default saved payment method.

For manually created payment schedules and payment schedule items, the payment gateway collects payments by using the most recently created saved payment method for the account that’s related to the invoice.

Statuses of Payment Schedules and Payment Schedule Items

The status of the payment schedule item is updated at various stages of the payment batch run.

PAYMENT BATCH RUN STAGE	PAYMENT SCHEDULE ITEM STATUS
A payment batch run picks up the payment schedule item for processing.	Processing
A payment batch run completes collecting the amount of the payment schedule by using the merchant account.	Processed
A payment batch run applies the payment schedule item to an invoice or invoice line.	Applied
A payment batch run fails to process the payment schedule.	Failed
A payment batch run fails to apply the payment schedule item to an invoice or invoice line.	Apply Failed
A payment batch run successfully processes a payment schedule.	Completed
The balance of the corresponding invoice is less than that of the payment schedule line.	Canceled
Results of Payment Application

After payments are collected and applied, Billing automatically creates and updates these fields and records.

PAYMENT APPLICATION LEVEL	UPDATED PAYMENT SCHEDULE AND PAYMENT SCHEDULE ITEM FIELDS	UPDATED INVOICE FIELDS	NEW RECORDS
Invoice	

Payment Schedule fields:

Status changes to Completed
Total Processed Amount
Remaining Amount To Be Processed
Total Applied Amount

Payment Schedule Item fields:

Status changes to Applied
Processed Amount
Payment Source
Last Payment Gateway Log
Payment Gateway Log Number
	
Balance
Net Payments Applied if the Settlement Status is Settled
Settlement Status changes to Partially Settled or Settled based on the applied payment amount
Full Settlement Date if the Settlement Status is Settled
Settlement Level changes to Invoice
Saved Payment Method
	
A Payment record is created after payment is collected using the merchant account.
A Payment Line Invoice record is created after the payment is applied to an invoice.

Invoice Line	

Payment Schedule fields:

Status changes to Completed
Total Processed Amount
Remaining Amount To Be Processed
Total Applied Amount

Payment Schedule Item fields:

Status changes to Applied
Processed Amount
Payment Source
Last Payment Gateway Log
Payment Gateway Log Number
	
Balance
Net Payments Applied if the Settlement Status is Settled
Settlement Status changes to Partially Settled or Settled based on the applied payment amount
Full Settlement Date if the Settlement Status is Settled
Settlement Level changes to Invoice Line
Saved Payment Method
	
A Payment record is created after payment is collected using the merchant account.
A Payment Line Invoice Line record is created after the payment is applied to an invoice line.
Payment Batch Run Failures

To troubleshoot failed payment schedule items, check the Revenue Transaction Error Logs related list on the Payment Batch Run and Payment Schedule records.

To automatically retry failed payments, set up payment retry rules, define a default payment retry rule set, and then enable the retry failed payments feature on the Billing Settings page.

To manually retry processing of failed payments, change the status of the failed payment schedule items to Canceled. Then, create new payment schedule items with the same details and schedule a payment batch run.

=== ARTICLE: ind.billing_payment_reconciliation.htm ===
---
article_id: ind.billing_payment_reconciliation.htm
title: Automate Payment Reconciliation
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Automate Payment Reconciliation

Accelerate cash collection by automating payment reconciliation between the payment advice records your customers send and the payment proofs your bank confirms. Billing uses Document AI to extract payment data from payment advice documents, lockbox files, or emails, and automatically matches the payment data against payment proofs such as bank statements. Your accounts receivable team can then review all matched and unmatched transactions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Payment Reconciliation Workflow

When a customer pays, you often receive two kinds of documents–a payment advice and a payment proof. A payment advice such as a remittance advice lists what the customer claims to pay. A payment proof, such as a bank statement, confirms what the bank received. Payment reconciliation ingests both document types, extracts the data, and compares it with your invoices. It then matches a customer’s payment advice with the bank’s payment proof and with open invoices, so that each payment can be applied to the correct account and invoice amount.

The end-to-end process involves these stages.

Set up a Salesforce CRM connection in a Data 360 org.
Ingest payment advice and payment proof documents from an external source, such as Google Drive, into Data 360.
Use Document AI in Data 360 to extract structured data from the unstructured documents.
Create a custom batch data transform to transform the text and numeric data parsed by Document AI into valid data types required for payment reconciliation in Billing.
Map the output of the custom batch data transform to the out-of-the-box data model objects (DMO).
Create a vector search index to enhance searchability of the data.
Deploy the payment reconciliation data kit.
Run the batch data transforms.
Review the matched and unmatched results.
Understand How Payment Reconciliation Evaluates a Match
Payment reconciliation first checks whether the currency ISO code matches between the payment advice and payment proof documents. If yes, then it compares each payment against three criteria and records how closely the values align, so your accounts receivable team can review the results.
Understand Why Document AI Extracts a Payment Advice Into Two Tables
When Document AI processes a payment advice, it writes the data into two related tables, but it writes a payment proof into one. Understand why before you configure the output data lake objects (DLOs).
Understand How Document AI Maps the Payment Advice Into Tables and Columns
Consider the sample payment advice (such as a remittance advice) and the sample payment proof (such as a bank statement) for a single $10,000 ACH payment from Acme Corp against two invoices. Document AI reads each document and writes the values into the corresponding columns.
Set Up Payment Reconciliation
Set up payment reconciliation by preparing your payment data in Data 360 and deploying the payment reconciliation data kit that Billing uses to match payments against your invoices.
Reconcile Payment Advice and Payment Proof with Bank Data
Payment reconciliation connects the data you prepared in Data 360 with your billing records. After you share your payment advice and payment proof documents through the connector of your choice, Data 360 ingests them, Document AI extracts the data, and your batch data transforms convert it into the fields that Billing needs. When you run the reconciliation transforms, Billing pulls in this data, matches each payment advice against the bank’s payment proof and your open invoices, and creates reconciliation records. Your accounts receivable team then reviews the matched and unmatched records.

=== ARTICLE: ind.billing_payment_reconciliation_document_ai_tables_columns.htm ===
---
article_id: ind.billing_payment_reconciliation_document_ai_tables_columns.htm
title: Understand How Document AI Maps the Payment Advice Into Tables and Columns
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_document_ai_tables_columns.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation.htm
fetched_at: 2026-09-04
---

# Understand How Document AI Maps the Payment Advice Into Tables and Columns

Consider the sample payment advice (such as a remittance advice) and the sample payment proof (such as a bank statement) for a single $10,000 ACH payment from Acme Corp against two invoices. Document AI reads each document and writes the values into the corresponding columns.

Here’s the remittance advice document for Acme Corp.

ELEMENT IN THE SAMPLE PAYMENT ADVICE	EXTRACTS TO	TABLE
Payer “Acme Corp”	Payer Name	Header
Total payment amount $10,000	Payment Amount	Header
Payment date March 15, 2026	Payment Date	Header
Remittance reference ACME-RA-20260315	Reference Number	Header
Payment method ACH	Payment Method	Header
INV-1001—$6,000 invoice, $6,000 applied, no deduction	Invoice Number, Gross Amount, Applied Amount	Invoice-level (record 1)
INV-1002—$4,200 invoice, $4,000 applied, $200 EARLYPAY	Adds Deduction Amount and Deduction Code	Invoice-level (record 2)

In INV-1001, the Gross Amount is the invoice’s stated amount, Applied Amount is what the payment actually remits or pays against that invoice, and the difference between them is captured in INV-1002 as Deduction Amount and Deduction Code. So, INV-1001 is a complete match and INV-1002 is a short payment with a deduction.

Here’s the account statement (payment proof) document for Acme Corp.

ELEMENT IN THE SAMPLE PAYMENT PROOF	EXTRACTS TO
Incoming credit from Acme Corp for $10,000	Payer Name, Payment Amount, Credit Debit Indicator (CRDT)
Transaction reference TXN-88231, “ACH CREDIT ACME CORP”	Transaction Reference Number, Payment Description
Booking and value date March 18, 2026; statement dated March 31, 2026	Booking Date, Value Date, Statement Date
Source file AcmeBank_Statement_Mar2026.pdf	Source Document Name, Source Document URL

The payment proof table captures how the bank categorizes the payment, which is what reconciliation matches the payment advice against. For example, Credit Debit Indicator records the direction of funds: CRDT (credit) means money came in, which is what you expect for a customer payment. Payer Name and Payment Amount are the values that reconciliation compares against the payment advice to confirm that the same party paid the same amount. The three dates serve different purposes: Booking Date is when the bank posted the entry, Value Date is when the funds became available, and Statement Date is when the statement was issued. Payment reconciliation compares the payment date on the advice with the date the bank confirmed the payment to calculate the date variance. The date variance, in this case, indicates the normal settlement time gap between when a customer intends to pay and when the funds are actually settled.

=== ARTICLE: ind.billing_payment_reconciliation_document_ai_two_tables.htm ===
---
article_id: ind.billing_payment_reconciliation_document_ai_two_tables.htm
title: Understand Why Document AI Extracts a Payment Advice Into Two Tables
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_document_ai_two_tables.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation.htm
fetched_at: 2026-09-04
---

# Understand Why Document AI Extracts a Payment Advice Into Two Tables

When Document AI processes a payment advice, it writes the data into two related tables, but it writes a payment proof into one. Understand why before you configure the output data lake objects (DLOs).

A single payment advice can claim to pay one or more invoices with one payment. For example, a customer sends one $10,000 payment that settles several open invoices. To represent that relationship, the payment advice output DLO uses two tables in a one-to-many relationship.

A header table holds the payment-level details that apply to the whole payment: who paid, how much, when, and by what payment method.
An invoice-level table holds one record per invoice that the payment covers, with the amount applied to each invoice and any deduction applied.

This two-table extraction layer mirrors the reconciliation layer that consumes it. The extraction objects PaymentAdvice (payment header) and PaymentAdviceLineInvoice (invoices) populate the reconciliation objects PaymentAdviceReconciliation (payment header) and PaymentAdviceInvoiceRecile (invoices). Both layers use the same payment and invoice relationship, with a one-to-many structure that runs from the payment extraction process through to the payment reconciliation process.

Here are the columns that you need to add when you configure the output DLOs for payment advice. They map to the PaymentAdvice and PaymentAdviceLineInvoice data model objects.

Add these columns to the payment advice header table.

Payment Advice Id
Payer Name
Payment Amount
Payment Date
Reference Number
Source Document
Transaction Description
Payment Method
Processing Status
Account

Add these columns to the payment advice invoice-level table.

Payment Advice Line Invoice Id
Payment Advice
Invoice Number
Applied Amount
Gross Amount
Deduction Amount
Deduction Code
Created Date Time
Last Modified Date Time
Invoice

However, in case of the payment proof, the output DLO is a single table. A bank statement confirms one transaction that the bank received, which results in one record per confirmed payment. Here are the columns you need to add when you configure the output DLO for payment proof.

Add these columns to the payment proof table.

Payment Proof Id
Transaction Reference Number
Payer Name
Payment Amount
Booking Date
Value Date
Statement Date
Source Document Name
Source Document URL
Credit Debit Indicator
Payment Description
Processing Status
Created Date Time
Last Modified Date Time
Proof Type
Account

=== ARTICLE: ind.billing_payment_reconciliation_match_evaluation.htm ===
---
article_id: ind.billing_payment_reconciliation_match_evaluation.htm
title: Understand How Payment Reconciliation Evaluates a Match
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_match_evaluation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation.htm
fetched_at: 2026-09-04
---

# Understand How Payment Reconciliation Evaluates a Match

Payment reconciliation first checks whether the currency ISO code matches between the payment advice and payment proof documents. If yes, then it compares each payment against three criteria and records how closely the values align, so your accounts receivable team can review the results.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

When the payment advice and payment proof use the same currency ISO code, then payment reconciliation evaluates these criteria.

Account—Reconciliation resolves the payer named on the payment advice and payment proof to an account and records a match score. A high-confidence score resolves the account automatically.
Amount—Reconciliation compares the amount on the payment advice with the amount confirmed on the payment proof, and each applied amount with its open invoice. It records the difference as an amount variance percentage. Payment reconciliation treats an amount variance within 2% as a match.
Date—Reconciliation compares the payment date on the advice with the date the bank confirmed the payment, and records the difference as a date variance in days. Payment reconciliation treats a date variance within 5 days as a match.

The matching is performed by using two data transforms:

PaymentAdviceInvoiceReconciliation—An advice-to-invoice data transform that matches a payment advice to your open invoices with balance greater than 0, confirming what the payment pays for, including any deductions.
PaymentAdvicePaymentProofReconciliation—An advice-to-proof data transform that matches a payment advice to the bank’s payment proof, confirming that the funds are settled.

Every reconciliation record is created with a Pending status that can then be reviewed by your accounts receivable team.

NOTE You can implement custom logic to create and apply payments after the match is confirmed.
Example 1: Payment Reconciliation with a 3-day Variance in Date

Acme Corp sends a payment advice for a $10,000 ACH payment dated March 15, 2026, that pays two invoices. Acme’s payment settles into your bank account, and your bank statement books the deposit on March 18, 2026, three days later. Payment reconciliation checks the currency ISO code in the payment advice and payment proof documents, and if there’s a match, it compares the two documents and your open invoices, and records the results.

PARAMETER	PAYMENT ADVICE	PAYMENT PROOF	RESULT
Account	Payer “Acme Corp”	Resolves to the Acme Corp account	High-confidence account match
Amount	$10,000	$10,000 confirmed	0% amount variance
Date	March 15, 2026	Booked March 18, 2026	3-day date variance
Invoice INV-1001	$6,000 applied	$6,000 invoice	Complete match, no deduction
Invoice INV-1002	$4,000 applied	$4,200 invoice	$200 short payment, deduction code EARLYPAY

Payment reconciliation writes these results to two kinds of records–Payment Advice Reconciliation and Payment Advice Invoice Reconciliation–that your accounts receivable team reviews.

The Payment Advice Reconciliation record is the header record for the advice-to-proof match.

FIELD	VALUE
Payer Name	Acme Corp
Account	Acme Corp (resolved)
Payment Advice Account Score	1, high confidence
Amount Variance %	0%
Date Variance (Days)	3
Review Status	Pending

A Payment Advice Invoice Reconciliation record is created for each invoice, for the advice-to-invoice match.

INVOICE	APPLIED AMOUNT	INVOICE AMOUNT	DEDUCTION AMOUNT	REVIEW STATUS
INV-1001	$6,000	$6,000	None	Pending
INV-1002	$4,000	$4,200	$200, EARLYPAY	Pending

The account and amount align, and the Payment Advice Reconciliation record shows a 3-day date variance between when Acme intended to pay and when the bank confirmed the deposit. Considering this as a normal settlement gap, your reviewer accepts the advice-to-proof match. On the Payment Advice Invoice Reconciliation records, INV-1001 is a complete match. INV-1002 is a $200 short payment against a $4,200 invoice, so the reviewer confirms the early-payment discount.

Example 2: Payment Reconciliation with a 2% Variance in Amount

Globex Corp sends a payment advice for a $10,000 wire payment dated April 6, 2026, that pays two invoices. The wire settles into your bank account the same day, but your bank statement confirms a deposit of $9,820, that’s $180 less, because an intermediary bank deducted a wire fee. Payment reconciliation checks the currency ISO code in the payment advice and payment proof documents, and if there’s a match, it compares the two documents and your open invoices, and records the results.

PARAMETER	PAYMENT ADVICE	PAYMENT PROOF	RESULT
Account	Payer “Globex Corp”	Resolves to the Globex Corp account	High-confidence account match
Amount	$10,000	$9,820 confirmed	1.8% amount variance (within 2%)
Date	April 6,2026	Booked April 6, 2026	0-day date variance
Invoice INV-2001	$6,000 applied	$6,000 invoice	Complete match
Invoice INV-2002	$4,000 applied	$4000 invoice	Complete match

Payment reconciliation writes these results to two kinds of records–Payment Advice Reconciliation and Payment Advice Invoice Reconciliation–that your accounts receivable team reviews.

The Payment Advice Reconciliation record is the header record for the advice-to-proof match.

FIELD	VALUE
Payer Name	Globex Corp
Account	Globex Corp (resolved)
Payment Advice Account Score	1, high confidence
Amount Variance %	1.8%
Date Variance (Days)	0
Review Status	Pending

A Payment Advice Invoice Reconciliation record is created for each invoice, for the advice-to-invoice match.

INVOICE	APPLIED AMOUNT	INVOICE AMOUNT	DEDUCTION AMOUNT	REVIEW STATUS
INV-2001	$6,000	$6,000	0	Pending
INV-2002	$4,000	$4,000	0	Pending

The account, currency ISO code, and dates all align. The advice-to-proof amount varies by 1.8%, within the 2% threshold, because the bank deducted a wire fee before the funds landed, so reconciliation treats it as a match and your reviewer accepts the advice-to-proof match. On the Payment Advice Invoice Reconciliation records, both INV-2001 and INV-2002 are considered as complete matches, because Globex applied the full invoice amounts even though the bank’s net deposit was lower.

=== ARTICLE: ind.billing_payment_reconciliation_run.htm ===
---
article_id: ind.billing_payment_reconciliation_run.htm
title: Reconcile Payment Advice and Payment Proof with Bank Data
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_run.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation.htm
fetched_at: 2026-09-04
---

# Reconcile Payment Advice and Payment Proof with Bank Data

Payment reconciliation connects the data you prepared in Data 360 with your billing records. After you share your payment advice and payment proof documents through the connector of your choice, Data 360 ingests them, Document AI extracts the data, and your batch data transforms convert it into the fields that Billing needs. When you run the reconciliation transforms, Billing pulls in this data, matches each payment advice against the bank’s payment proof and your open invoices, and creates reconciliation records. Your accounts receivable team then reviews the matched and unmatched records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To reconcile payment advice and payment proof with bank data by using batch data transforms:	

Billing Admin permission set

AND

Data Cloud Architect permission set

Complete the setup steps for payment reconciliation, including deploying the payment reconciliation data kit.

Confirm that your latest payment advice and payment proof documents are ingested and processed into the PaymentAdvice, PaymentAdviceLineInvoice, and PaymentProof data model objects. To verify, view these data model objects in the Query Editor in Data 360.
In the Data Transforms tab in Data 360, run these payment reconciliation batch data transforms.
PaymentAdvicePaymentProofReconciliation
PaymentAdviceInvoiceReconciliation

You can also run them by using REST API.

POST /services/data/v68.0/ssot/data-transforms/PaymentAdvicePaymentProofReconciliation/actions/run
POST /services/data/v68.0/ssot/data-transforms/PaymentAdviceInvoiceReconciliation/actions/run
Billing matches the payment with payment proofs and invoices, and creates payment advice reconciliation records for you to review.
Open the payment advice reconciliation and payment advice invoice reconciliation records to review the matched and unmatched results.
Each record shows how closely the payment advice, payment proof, and invoice match, including the difference in amount and in payment date.
NOTE You can define and implement custom logic to accept, reject, and resolve the matched records, and then apply the payment to the appropriate invoice.

=== ARTICLE: ind.billing_payment_reconciliation_setup.htm ===
---
article_id: ind.billing_payment_reconciliation_setup.htm
title: Set Up Payment Reconciliation
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation.htm
fetched_at: 2026-09-04
---

# Set Up Payment Reconciliation

Set up payment reconciliation by preparing your payment data in Data 360 and deploying the payment reconciliation data kit that Billing uses to match payments against your invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To set up payment reconciliation and deploy data kits:	

Billing Admin permission set

AND

Data Cloud Architect permission set

Establish Data Connection with Data 360
Billing uses unstructured Data 360 connectors to ingest unstructured data in payment documents such as payment advice documents and payment proof documents.
Process Data by Using Document AI
Use Document AI to extract structured data from the ingested payment advice and payment proof documents. Document AI reads each document and writes the extracted values into an output data lake object (DLO), a structured table whose columns represent the fields that you want to capture. You define one output DLO for payment advice and one for payment proof, and Document AI populates them as it processes your documents. Edit or delete any fields or tables in a DLO as needed.
Create a Custom Batch Data Transform
After Document AI parses your payment advice and payment proof files, convert the numeric and text fields that represent currency and date values into the currency and date data types that payment reconciliation requires.
Create a Vector Search Index
Enhance the searchability of your data by creating a vector search index on the Account object.
Set Up the Ingestion API Schema
Upload and save a JSON-formatted schema to create the output data lake objects (DLOs) for payment reconciliation.
Deploy the Payment Reconciliation Data Kit
The Payment Reconciliation data kit bundles the data model objects, batch data transforms, data actions, and a data action target that reconcile your payments.

=== ARTICLE: ind.billing_payment_reconciliation_setup_batch_transform.htm ===
---
article_id: ind.billing_payment_reconciliation_setup_batch_transform.htm
title: Create a Custom Batch Data Transform
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_setup_batch_transform.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation_setup.htm
fetched_at: 2026-09-04
---

# Create a Custom Batch Data Transform

After Document AI parses your payment advice and payment proof files, convert the numeric and text fields that represent currency and date values into the currency and date data types that payment reconciliation requires.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create a custom batch data transform:	

Data Cloud Architect permission set

Create a custom batch data transform to convert the text and number fields parsed by Document AI into date and currency fields. Make sure that your data transform is able to resolve the currency ISO code from the payment details.
For each output DLO, complete these steps.
Add a transform node to convert all the fields in the DLO to the required data type. Optionally, add custom transformation logic or formula nodes.
Select the three DLOs and add them to the default data space. Select the Add without filters checkbox.
Map the output DLOs to the PaymentAdvice_std__dlm, PaymentAdviceLineInvoice_std__dlm, and PaymentProof_std__dlm data model objects.
Save, build, and run the batch data transform. You can run the data transform manually or schedule it.

=== ARTICLE: ind.billing_payment_reconciliation_setup_data_connection.htm ===
---
article_id: ind.billing_payment_reconciliation_setup_data_connection.htm
title: Establish Data Connection with Data 360
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_setup_data_connection.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation_setup.htm
fetched_at: 2026-09-04
---

# Establish Data Connection with Data 360

Billing uses unstructured Data 360 connectors to ingest unstructured data in payment documents such as payment advice documents and payment proof documents.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To set up payment reconciliation and deploy data kits:	

Billing Admin permission set

AND

Data Cloud Architect permission set

Turn on Data 360.
Set up a Salesforce CRM connection.
Connect to a Salesforce org by setting up a CRM Salesforce org connection.
Create and deploy data streams for the Account and Invoice objects. On the Invoice object, select all fields except the Corporate Currency Converted Total Amount With Tax and Functional Currency Converted Total Amount With Tax standard fields.
Set up a data connection with Data 360.
In Data Cloud Setup, go to Feature Manager and enable Connectors. For a list of supported connectors, see Unstructured Data Connectors.
Integrate your preferred data connector to enable the flow of unstructured data in Data 360.

For example, to ingest unstructured data in payment advice and payment proofs, you can use unstructured data connectors such as Confluence, GitHub, or Google Drive. Follow the connector-specific instructions in the Data 360 Connectors and Integrations section of Data 360 Integration Guide.

Enable access to the folder, drive, or repository that contains your payment advice and payment proof documents. We recommend that you store or access the payment advice and proof documents from separate locations.
For example, if you’ve set up the unstructured Google connector, access the payment advice and payment proof docs from separate folders on Google Drive.
To ingest data from the source into Data 360, create two unstructured data lake objects (UDLO), and map the payment advice and payment proof UDLOs to corresponding payment advice and payment proof unstructured data model objects (UDMO).
The connector begins to ingest the unstructured data from the payment advice and payment proof documents into Data 360. The data ingestion process can take several minutes depending on the size and nature of your data. You can monitor the ingestion status by using the Data Streams tab or Query Editor in Data 360.

=== ARTICLE: ind.billing_payment_reconciliation_setup_deploy_data_kit.htm ===
---
article_id: ind.billing_payment_reconciliation_setup_deploy_data_kit.htm
title: Deploy the Payment Reconciliation Data Kit
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_setup_deploy_data_kit.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation_setup.htm
fetched_at: 2026-09-04
---

# Deploy the Payment Reconciliation Data Kit

The Payment Reconciliation data kit bundles the data model objects, batch data transforms, data actions, and a data action target that reconcile your payments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To set up payment reconciliation and deploy data kits:	

Billing Admin permission set

AND

Data Cloud Architect permission set

In Data Cloud Setup, click Data Kits, and select Payment Reconciliation.
Deploy the Payment Advice Account Reconciliation and Payment Proof Account Reconciliation bundles.
On the Deploy page, under Connector name, select Payment Reconciliation Ingestion API.
Select the connector twice—once for the Payment Advice Account Reconciliation bundle and once for the Payment Proof Account Reconciliation bundle.
Check the deployment status in the Deployment History tab.
The deployment can take a few minutes. Confirm that the deployment is completed successfully before you run any payment reconciliation.

After the data kit is deployed, you’re ready to run payment reconciliation and review the results.

=== ARTICLE: ind.billing_payment_reconciliation_setup_document_ai.htm ===
---
article_id: ind.billing_payment_reconciliation_setup_document_ai.htm
title: Process Data by Using Document AI
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_setup_document_ai.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation_setup.htm
fetched_at: 2026-09-04
---

# Process Data by Using Document AI

Use Document AI to extract structured data from the ingested payment advice and payment proof documents. Document AI reads each document and writes the extracted values into an output data lake object (DLO), a structured table whose columns represent the fields that you want to capture. You define one output DLO for payment advice and one for payment proof, and Document AI populates them as it processes your documents. Edit or delete any fields or tables in a DLO as needed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To process data by using Document AI:	

Data Cloud Architect permission set

To configure these output DLOs, complete both procedures, first for payment advice, then for payment proof. For more information, see Document AI and Create a Document Schema Configuration Manually.

Configure Output DLOs for Payment Advice
In the Data 360 app, click Process Content | Document AI | New.
Select the payment advice UDMO as the source object.
Select PDF and Image as the file types available for configuring the document schema.
In DLO configuration, create two tables with columns that represent the payment-level and invoice-level details from the payment advice document.
Payment Advice Output DLO Columns
PAYMENT-LEVEL DETAILS ON PAYMENT ADVICE	INVOICE-LEVEL DETAILS ON PAYMENT ADVICE
Payment Advice Id	Payment Advice Line Invoice Id
Payer Name	Payment Advice
Payment Amount	Invoice Number
Payment Date	Applied Amount
Reference Number	Gross Amount
Source Document	Deduction Amount
Transaction Description	Deduction Code
Payment Method	Created Date Time
Processing Status	Last Modified Date Time
Account	Invoice
View and publish your document schema.
Open the output DLOs to check the field-level mappings, and rebuild the schema if required.
Use the Query Editor to view the records.
Configure Output DLO for Payment Proof
In the Data 360 app, click Process Content | Document AI | New.
Select the payment proof UDMO as the source object.
Select PDF and Image as the file types available for configuring the document schema.
In DLO configuration, create a table with columns that represent the payment proof details from the payment proof document.
Payment Proof Output DLO Columns
DETAILS ON PAYMENT PROOF
Payment Proof Id
Transaction Reference Number
Payer Name
Payment Amount
Booking Date
Value Date
Statement Date
Source Document Name
Source Document URL
Credit Debit Indicator
Payment Description
Processing Status
Created Date Time
Last Modified Date Time
Proof Type
Account
View and publish your document schema.
Open the output DLO to check the field-level mappings, and rebuild the schema if required.
Use the Query Editor to view the records.
HOW DOCUMENT AI STRUCTURES A PAYMENT

Consider a single payment from Acme Corp. Acme sends a remittance advice (a type of payment advice) to pay two open invoices with one $10,000 ACH payment, and Acme’s bank issues a statement that confirms the deposit. Document AI extracts data from both documents into their output DLOs. Because the two documents describe the payment differently, their schemas differ too.

Because one payment advice can pay several invoices, the payment advice output DLO uses two related tables: one for the payment-level details and one for the invoice-level records.

Sample payment advice

Payment Advice Extraction
PAYMENT ADVICE DETAILS	CONFIGURATION OF THE OUTPUT DLO
Payer Acme Corp, a $10,000 ACH payment dated March 15, 2026, with reference number ACME-RA-20260315.	One record in the payment-level table: Payer Name, Payment Amount, Payment Date, Reference Number, and Payment Method.
Invoice INV-1001, with $6,000 applied and no deduction.	One record in the invoice-level table: Payment Advice Invoice Number, Applied Amount, and Gross Amount.
Invoice INV-1002, with $4,000 applied against a $4,200 gross amount and a $200 early-payment deduction (code EARLYPAY).	A second record in the invoice-level table, including Deduction Amount and Deduction Code.

A payment proof confirms a single payment that the bank received, so its output DLO uses one table, with one record per confirmed transaction.

Sample payment proof

Payment Proof Extraction
PAYMENT PROOF DETAILS	CONFIGURATION OF THE OUTPUT DLO
An incoming credit from Acme Corp for $10,000.	Payer Name, Payment Amount, and Credit Debit Indicator.
Transaction reference TXN-88231, described as ACH CREDIT ACME CORP.	Transaction Reference Number and Payment Description.
A booking date and value date of March 18, 2026, on a statement dated March 31, 2026.	Booking Date, Value Date, and Statement Date.
The source file AcmeBank_Statement_Mar2026.pdf.	Source Document Name and Source Document URL.

Together, these two output DLOs give payment reconciliation the structured data that it needs to later match Acme’s payment advice against the bank’s payment proof and the open invoices.

=== ARTICLE: ind.billing_payment_reconciliation_setup_ingestion_api.htm ===
---
article_id: ind.billing_payment_reconciliation_setup_ingestion_api.htm
title: Set Up the Ingestion API Schema
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_setup_ingestion_api.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation_setup.htm
fetched_at: 2026-09-04
---

# Set Up the Ingestion API Schema

Upload and save a JSON-formatted schema to create the output data lake objects (DLOs) for payment reconciliation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To set up Ingestion API connector:	

Billing Admin permission set

AND

Data Cloud Architect permission set

Upload and save this schema. For more information, see Set up Ingestion API connector.
openapi: 3.0.3
info:
  title: Ingestion API Schema
  description: Ingestion API schema for payment reconciliation.
  version: "1.0.0"
paths: {}
components:
  schemas:
    PaymentAdviceAccountRecile:
      type: object
      properties:
        Id:
          type: string
        PaymentAdviceId:
          type: string
        AccountId:
          type: string
        AccountName:
          type: string
        MatchScoreNumber:
          type: number
        PayerName:
          type: string
        AccountReviewStatus:
          type: string
        ReviewedById:
          type: string
        ReviewedDateTime:
          type: string
          format: date-time
        RejectionReasonText:
          type: string
    PaymentProofAccountRecile:
      type: object
      properties:
        Id:
          type: string
        PaymentProofId:
          type: string
        AccountId:
          type: string
        AccountName:
          type: string
        MatchScoreNumber:
          type: number
        PayerName:
          type: string
        AccountReviewStatus:
          type: string
        ReviewedById:
          type: string
        ReviewedDateTime:
          type: string
          format: date-time
        RejectionReasonText:
          type: string

=== ARTICLE: ind.billing_payment_reconciliation_setup_vector_search.htm ===
---
article_id: ind.billing_payment_reconciliation_setup_vector_search.htm
title: Create a Vector Search Index
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_reconciliation_setup_vector_search.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_reconciliation_setup.htm
fetched_at: 2026-09-04
---

# Create a Vector Search Index

Enhance the searchability of your data by creating a vector search index on the Account object.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create a vector search index:	

Data Cloud Architect permission set

For any data and query requirements, create a vector search index to enhance the searchability of your data.

Select Account as the source object.
On the chunking page, click Manage Fields and add Account Name.
The chunking strategy is autopopulated as Passage Extraction.
Click Next twice.
Review the configuration and target data model objects, and then save the search index.
Track the status of the search index and make sure it’s in Ready state.
NOTE Though the creation of a vector search index is a one-time task, make sure that you rebuild the vector search index when new accounts are added to the data streams.

=== ARTICLE: ind.billing_payment_runs_schedule.htm ===
---
article_id: ind.billing_payment_runs_schedule.htm
title: Schedule Payment Batch Runs to Process Payments
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_runs_schedule.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Schedule Payment Batch Runs to Process Payments

Set up a payment scheduler with specific filters to automatically process payments for your transactions. Payment batch runs process existing payment schedules and payment schedule items to collect the corresponding payments, and then apply them to invoices based on the payment application level.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To schedule payment batch runs:	Payment Operations User permission set
From the App Launcher, find and select Billing Batch Schedulers.
Click New Payment Scheduler.
Enter a name for the payment scheduler.
To activate the payment scheduler, select Active.
Payments are collected and applied only when the scheduler is active. You can create payment schedulers in inactive state, and modify and activate them later.
Select the frequency at which you want the payment batch runs to process payments.
If you select Once, select a start date and a start time for the scheduler.
If you select Daily, select a start date and a start time, and an end date for the scheduler.
If you select Monthly, select a start date and a start time, and an end date for the scheduler. Additionally, select the number of days after which you want the monthly payment batch run to recur.
Click Next.
To configure matching criteria for the payment scheduler, select Match Any, select Payment Schedule Item as the Type, Payment Run Matching Value as the Column, and select the payment run matching value that you want to filter payment schedule items by.
By default, no matching criteria is selected. If you don't specify a matching criteria, the default matching criteria is used to determine the payment schedule items that the payment batch run must process. With the default matching criteria, all the payment schedule items with a target payment date that's less than or equal to the job run date are processed by the payment batch runs.
Click Create.

A Billing Batch Scheduler record with Payment as the Job Type is created. At the start time of the scheduler, a Payment Batch Run record is created.

To understand how payment batch runs process payment schedules and payment schedule items, see Payment Batch Run Overview.

SEE ALSO
Revenue Cloud Developer Guide: PaymentLineInvoiceLine
Revenue Cloud Developer Guide: Billing Fields on PaymentLineInvoice

=== ARTICLE: ind.billing_payment_schedules_and_payment_schedule_items.htm ===
---
article_id: ind.billing_payment_schedules_and_payment_schedule_items.htm
title: Manually Create Payment Schedules and Payment Schedule Items
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_schedules_and_payment_schedule_items.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_schedules_and_payment_schedule_items_auto_manual.htm
fetched_at: 2026-09-04
---

# Manually Create Payment Schedules and Payment Schedule Items

Instead of automatically creating payment schedules and payment schedule items, you can create them manually.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Salesforce Payments feature is available with the Revenue Management Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Management Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To create payment schedules and payment schedule items:	Payment Admin permission set
Manually Create Payment Schedules

Instead of automatically creating payment schedules, you can create them manually to store the details that are used to process payments for a particular record.

From the App Launcher, find and select Payment Schedules.
Click New.
Select the reference entity and reference record that you want to process payments for.
Select a status for the payment schedule.
If you want to configure the payment schedule further, select Draft.
If the payment schedule is ready to be processed by a payment batch run, select Open.
If a payment batch run successfully processes the payment schedule, the status changes to Completed. If a payment batch run fails to process the payment schedule, the status changes to Canceled.
Select a saved payment method as the default payment method for the payment schedule.
The saved payment method is used to collect payments for all the payment schedule items that are related to the payment schedule.
You can’t specify a card payment method as the default payment method in Salesforce orgs with the Revenue Management Billing license.
Enter any additional details about the payment schedule as comments.
Enter the total amount that you want the payment schedule to process as a payment for the reference record.
Save your work.

The Payment Schedule record that’s created has the account that’s related to the reference record as the payment account.

After you create a Payment Schedule record, create payment schedule items for that record.

Manually Create Payment Schedule Items

Instead of automatically creating payment schedule items, you can create them manually. A payment schedule item represents information about a single payment to be processed for a record and can have different payment configuration values, such as payment methods, payment dates, and payment amounts.

Create one or more payment schedule items for a payment schedule based on whether you want to process payments for a record in a single or multiple installments.

From the App Launcher, find and select Payment Schedules.
Open the Payment Schedule record that you want to create payment schedule items for, and go to the Related tab.
On the Payment Schedule Items related list, click New.
Select a status for the payment schedule item.
If you want to configure the payment schedule item further, select Draft.
If the payment schedule item is ready to be processed by a payment batch run, select Ready for Processing.
When a payment batch run picks up the payment schedule item for processing, the status changes to Processing.
When a payment batch run completes collecting the amount of the payment schedule by using the merchant account, the status changes to Processed.
When a payment batch run applies the payment schedule item to an invoice or invoice line, the status changes to Applied.
When a payment batch run fails to process the payment schedule, the status changes to Failed.
When a payment batch run fails to apply the payment schedule item to an invoice or invoice line, the status changes to Apply Failed.
When the balance of the corresponding invoice is less than that of the payment schedule line, the processing of the payment schedule line fails and the status changes to Canceled.
If you haven’t selected a default payment method for the payment schedule, select a saved payment method as the default payment method.

If you’ve specified a saved payment method for the Payment Schedule record, the Payment Schedule Item record has the same value.

You can’t specify a card payment method as the default payment method in Salesforce orgs with the Revenue Management Billing license.

To group all the payment schedule items that you want to process together, select a payment run matching value.
When you schedule payment batch runs, you can select a payment run matching value to process all the payment schedule items with the same value.
Select the date on which you want the payment batch run to process the payment schedule item.
Enter the amount that must be paid for the reference record by processing the payment schedule item.
Save your work.

=== ARTICLE: ind.billing_payment_schedules_and_payment_schedule_items_auto_manual.htm ===
---
article_id: ind.billing_payment_schedules_and_payment_schedule_items_auto_manual.htm
title: Payment Schedules and Payment Schedule Items
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_schedules_and_payment_schedule_items_auto_manual.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Payment Schedules and Payment Schedule Items

Payment schedules contain information about a set of payments that a customer wants to pay at different times for a certain record. A payment schedule contains one or more payment schedule items, where each item represents one payment to be processed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
Automatic Creation of Payment Schedules and Payment Schedule Items
Automate the creation of payment schedules and payment schedule items so that they are ready to be processed.
Manually Create Payment Schedules and Payment Schedule Items
Instead of automatically creating payment schedules and payment schedule items, you can create them manually.
Group Multiple Invoices into a Single Payment Request
Reduce payment gateway calls and gateway transaction fees by combining multiple invoices of an account into a single payment request. When you post invoices for an account, Billing automatically consolidates qualifying invoices into one payment schedule and one payment schedule item.

=== ARTICLE: ind.billing_payment_terms.htm ===
---
article_id: ind.billing_payment_terms.htm
title: Create Payment Terms
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_terms.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Create Payment Terms

Negotiate and define payment terms to set a due date for payments and collect payments in a timely manner. You can anticipate or enforce the date by when payments for outstanding invoices must be paid.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create payment terms and payment term items:	Billing Admin permission set
Examples: Payment Terms
Explore two examples that demonstrate how payment terms determine the payment due dates for invoices.
Create Payment Terms

A payment term is a formal agreement that defines the date by which an invoice must be paid.

From the App Launcher, find and select Payment Terms.
Click New.
Enter a name for the payment term.
Select a status.

When you create payment terms, you can select the status as either Draft or Inactive. If you select the status as Inactive, you can't change it to Draft.

You can't select the status as Active without creating a related payment term item.

To make this the default payment term for your Salesforce org, select Default.
If necessary, enter a description.
Save your changes.

After you create a payment term, create a corresponding payment term item.

Create Payment Term Items

Payment term items define the specific configuration for payment terms.

From the App Launcher, find and select Payment Terms.
Open the Payment Term record for which you want to create an item.
On the Payment Term Items related list, click New.
Select a type for the payment term item.
To calculate the invoice due date by adding the period to the invoice date, select Period-Based.
To calculate the invoice due date by adding the period to the last day of the month in which the invoice date falls, select Derive End of Month and Add Period.
Enter the period.
When the type of the payment term item is Derive End of Month and Add Period, to set the due date as the last day of the month in which the invoice is posted, enter 0 as the period.
To indicate that the payment term is for a standard payment, select Standard as the payment timeframe.
Each payment term can have only one payment term item with a Standard payment timeframe.
If you have entered a period, select the unit of measurement for the period.
If necessary, enter a description.
Save your changes.

After you create the payment term item, complete these steps:

Change the status of the payment term to Active. Only active payment terms can be used to determine the due dates of invoices.
Go to the Order records and specify the relevant payment term.
NOTE If you don't specify payment terms for orders, the default payment term for your Salesforce org is used.

The same payment terms are autopopulated for the billing schedules that are generated for these orders, and eventually used to determine the due dates of the invoices.

=== ARTICLE: ind.billing_payment_terms_usecase.htm ===
---
article_id: ind.billing_payment_terms_usecase.htm
title: "Examples: Payment Terms"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payment_terms_usecase.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_terms.htm
fetched_at: 2026-09-04
---

# Examples: Payment Terms

Explore two examples that demonstrate how payment terms determine the payment due dates for invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Net 30 Payment Term

A software company provides a subscription service and wants to use the Net 30 payment term for its subscription service. The company's Salesforce admin creates a draft payment term and a related payment term item with these values:

Type: Period-Based
Period: 30
Payment Timeframe: Standard
Period Unit: Days

The admin then activates the payment term and assigns it to the relevant order. When invoices are posted for that order, the due date is calculated by adding 30 days to the invoice date. For example, if an invoice is posted on July 1, the due date is calculated by adding 30 days, making the payment due by July 31.

Net 45 EOM Payment Term

A construction company completes a phase of a project and wants to use the Net 45 EOM payment term for the project. The company's Salesforce admin creates a draft payment term and a related payment term item with these values:

Type: Derive End of Month and Add Period
Period: 45
Payment Timeframe: Standard
Period Unit: Days

The admin then activates the payment term and assigns it to the relevant order. When invoices are posted for that order, the due date is calculated by adding 45 to the last day of the month in which the invoice is posted. For example, if an invoice is posted on April 15, the system first finds the last day of the month (April 30) and then adds 45 days. This makes the payment due by June 14.

=== ARTICLE: ind.billing_payments.htm ===
---
article_id: ind.billing_payments.htm
title: Process Payments and Issue Refunds in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Process Payments and Issue Refunds in Revenue Management

Complete your cash journey by making payments for posted invoices and issuing refunds when needed. Settle open invoice balances in a timely manner and accurately report cash flow by collecting and applying payments. Refund your customers if they change or cancel products or services that they paid for.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.

This flowchart shows how a user with the Payment Operations User permission set can use Payments in Revenue Management.

Payments Data Model in Revenue Management
The Payments data model depicts the objects and their relationships to manage the processing of customer payments including a timely collection of these payments and their application to appropriate invoices, and issuing refunds when needed.
Configure Saved Payment Methods for Revenue Management
Collect one-time or scheduled recurring payments by securely saving the payment methods of your customers, rather than manually entering payment method details each time a payment is processed. Save various payment methods from native or third-party payment gateways, and set a default saved payment method for each account.
Migrate Tokenized Saved Payment Methods
Expand your payment ecosystem by bringing in externally tokenized payment methods into your Salesforce org. Bring in external payment method tokens generated by using buyer-facing portals or the Self-Service Billing portal, and save them as payment methods in your Salesforce org. These externally saved payment methods are immediately available for use in payments batch processing.
Payment Schedules and Payment Schedule Items
Payment schedules contain information about a set of payments that a customer wants to pay at different times for a certain record. A payment schedule contains one or more payment schedule items, where each item represents one payment to be processed.
Schedule Payment Batch Runs to Process Payments
Set up a payment scheduler with specific filters to automatically process payments for your transactions. Payment batch runs process existing payment schedules and payment schedule items to collect the corresponding payments, and then apply them to invoices based on the payment application level.
Payment Batch Run Overview
At the start time of the payment scheduler, payment batch runs start processing payment schedule items based on the defined criteria.
Retry Failed Payments
Failed payments slow down cash flow and can lead to lost customers. When you enable automatic payment retries, Billing handles payment failures seamlessly and reprocesses each failed payment without manual intervention. You define a payment retry strategy that applies to all failed payments, with retry rules based on error categories such as insufficient funds or payment processing issues. For greater control and flexibility, you can define retry rules based on specific payment gateways and gateway-specific error codes. For each rule, you can configure the retry intervals that determine how often Billing can attempt to reprocess the failed payment. Additionally, you can set the maximum number of retry attempts, after which Billing either tries an alternate payment method or marks the payment request as failed.
Issue Refunds and Settle Balances
A refund returns an amount that a customer no longer owes, such as an overpayment or an available credit balance. Billing issues a refund either automatically, after you cancel or reduce a subscription, or on demand, when you want to settle a customer’s available credit balance by using a credit memo.
Automate Payment Reconciliation
Accelerate cash collection by automating payment reconciliation between the payment advice records your customers send and the payment proofs your bank confirms. Billing uses Document AI to extract payment data from payment advice documents, lockbox files, or emails, and automatically matches the payment data against payment proofs such as bank statements. Your accounts receivable team can then review all matched and unmatched transactions.
Send Level 2 and Level 3 Payment Data Through Your Payment Gateways
Level 2 and Level 3 processing data are the additional line-item and transaction-level details passed during credit card authorization. Use Level 2 and Level 3 data mainly for business-to-business and business-to-government corporate card transactions to lower fraud risk and get richer reporting. When Level 2 and Level 3 data support is enabled, Billing automatically includes additional transaction data in payment requests that you send through native and third-party payment gateways.
Process Payments and Issue Refunds by Using APIs
Use a suite of APIs to process payments and issue refunds. Authorize and capture payments by using native payment gateways, reverse payment authorizations, tokenize payment methods, and save card details for processing recurring payments. Create and update payment schedulers, and allocate or unallocate payments. You can process ad hoc payments, and refund your customers if they change or cancel products or services that they paid for.

=== ARTICLE: ind.billing_payments_apis.htm ===
---
article_id: ind.billing_payments_apis.htm
title: Process Payments and Issue Refunds by Using APIs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payments_apis.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Process Payments and Issue Refunds by Using APIs

Use a suite of APIs to process payments and issue refunds. Authorize and capture payments by using native payment gateways, reverse payment authorizations, tokenize payment methods, and save card details for processing recurring payments. Create and update payment schedulers, and allocate or unallocate payments. You can process ad hoc payments, and refund your customers if they change or cancel products or services that they paid for.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To process payments and issue refunds by using APIs:	Payment Operations User permission set
GOAL	API
Process ad hoc payments	

Payment Sale API

To automate the processing of ad hoc payments, build a custom flow and use the Payment Sale action.


Authorize payments	Payment Authorization API
Reverse the authorization of payments	Authorization Reversal API
Capture authorized payments	Payment Capture API
Tokenize payment methods	Tokenize Payment Method API
Create payment schedulers	Create Payment Scheduler API
Activate or deactivate payment schedulers	Update Payment Scheduler API
Apply a payment to an invoice or invoice line	

Payment Line Apply API

To automate this step, build a custom flow and use the Apply Payment action.


Unapply a payment from an invoice or invoice line	

Payment Line Unapply API

To automate this step, build a custom flow and use the Unapply Payment action.


Create refunds for processed payments	Create a Payment Refund API
Issue refunds against original payments	

Refund Line Apply API

To automate this step, build a custom flow and use the Automate Refund action.

=== ARTICLE: ind.billing_payments_consolidate_invoices.htm ===
---
article_id: ind.billing_payments_consolidate_invoices.htm
title: Group Multiple Invoices into a Single Payment Request
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_payments_consolidate_invoices.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_schedules_and_payment_schedule_items_auto_manual.htm
fetched_at: 2026-09-04
---

# Group Multiple Invoices into a Single Payment Request

Reduce payment gateway calls and gateway transaction fees by combining multiple invoices of an account into a single payment request. When you post invoices for an account, Billing automatically consolidates qualifying invoices into one payment schedule and one payment schedule item.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Salesforce Payments feature is available with the Revenue Management Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Management Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To generate a consolidated payment schedule and payment schedule item for multiple invoices on an account:	

Payment Admin permission set

OR

Payment Operations User permission set

How Invoice Grouping Works

When you turn on Create Payment Schedules and Payment Schedule Items on the Billing Settings page, Billing automatically creates a single payment schedule and payment schedule item for each posted invoice associated with an account. You can also generate a consolidated payment schedule and payment schedule item for invoices that match the grouping criteria.

Invoices with the same currency and payment method
Invoices with payment due dates that fall within the predefined due date window

Before you generate a consolidated payment schedule and payment schedule item for a set of invoices for an account, update the default payment schedule treatment for these values.

Grouping Source: Indicates whether to generate payment schedules and payment schedule items per invoice or per account. To group invoices by account, set the grouping source as Account. The default grouping source is Invoice, which creates one payment schedule and payment schedule item per posted invoice.

When you set the grouping source to Account, Billing records the payment schedule in the Payment Schedule field on the invoice, even when payment of only one invoice is processed for a payment schedule item.

Due Date Window: Specifies the time frame in days based on which the account’s invoices are grouped. All invoices with payment due dates that fall within the due date window are considered for grouping. The payment due date is calculated by adding the period on the payment term item of the associated billing schedule group to the date when the invoice is posted. For example, if an invoice is posted on March 5 and the period is 20, then the payment due date is March 25. For more information, see Create Payment Terms.

Now, when you generate invoices for the account by using the payment batch run, Billing creates a single, consolidated payment schedule and payment schedule item for all of the account’s invoices whose payment due dates fall within the due date window. Billing also populates these fields for the grouped invoices.

The total amount in the Payment Schedule record is the sum of all invoices in the group.
The target payment processing date in the Payment Schedule Item record is the earliest due date among the grouped invoices.

For any invoices whose payment due dates don’t fall within the due date window, Billing generates separate payment schedule and payment schedule items.

Example: Generate Single Payment Schedule and Payment Schedule Item for Multiple Invoices

Let’s consider an example of the Acme account with an associated billing schedule group and payment term. The billing schedules use a common currency and payment method, with payment term periods outlined in the table.

BILLING SCHEDULE	BILLED AMOUNT	PAYMENT TERM PERIOD (IN DAYS)	INVOICE	INVOICE AMOUNT	PAYMENT DUE DATE ON INVOICE	INCLUDED IN CONSOLIDATED PAYMENT REQUEST
A	$500	5	Invoice A	$500	April 6	Yes
B	$100	20	Invoice B	$100	April 21	Yes
C	$400	40	Invoice C	$400	May 10	No

Before you generate invoices for the account:

Make sure to turn on Create Payment Schedules and Payment Schedule Items on the Billing Settings page.
Update the default payment schedule treatment to set the grouping source as Account and due date window to 30.

Now, when you generate invoices for the account on April 1 in Posted status:

Billing generates three invoices: Invoice A, Invoice B, and Invoice C.
Billing sorts the invoices in an ascending order. Starting with the invoice having the earliest due date, Billing groups all invoices within the defined due date window. In the example, Invoice A and Invoice B are grouped together.
Billing creates a single Payment Schedule and Payment Schedule Item record for both Invoice A and Invoice B because they meet the grouping criteria for matching account, payment method, and currency, and they have payment due dates that fall within the due date window of 30 days.
The total requested amount on the Payment Schedule record is $600, which is equal to the sum of Invoice A ($500) and Invoice B ($100).
The target payment processing date on the Payment Schedule Item record is April 6, which is the earlier date among Invoice A and Invoice B.
Billing also generates a separate payment schedule and payment schedule item for Invoice C with a total requested amount of $400 and a target payment processing date of May 10.
Generate a Single Payment Schedule for Multiple Invoices of an Account
To consolidate payment schedules for an account’s invoices, configure the payment schedule treatment, set the grouping source as Account, and add a due date window.

=== ARTICLE: ind.billing_permission_sets.htm ===
---
article_id: ind.billing_permission_sets.htm
title: Assign Permissions to Access Billing Features
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_permission_sets.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup.htm
fetched_at: 2026-09-04
---

# Assign Permissions to Access Billing Features

Assign your users the required permission sets based on their persona, and for the APIs for which they need access.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


The Billing Collections and Recovery Specialist permission set, the Payment Admin permission set, and the Payment Operations User permission set are available only with the the Revenue Management Billing license. Contact your Salesforce account executive for more information.

All the other permission sets are available with the Revenue Management Advanced license or the Revenue Management Billing license.

Create Users and Profiles

To begin, create users for Billing in Revenue Management. Then assign users the appropriate permission sets. To help you plan, use the permission set table for Billing. When you create a user, you must also assign a profile to define the default settings for users. Some organizations create their own profiles, while others choose to use profiles included with Salesforce.

Remember, users can have only one profile, but can have many permission sets assigned to them.

Billing Permission Sets by Persona

Billing is managed by users who have different roles and expertise. The permission sets based on personas combine specific permissions that outline each user's responsibilities. All these permission sets are part of the Billing User permission set license. The Billing Customer Service User permission set is included in both Billing and Billing Advanced permission set licenses.

PERSONA	PERMISSION SET	PERMISSIONS
Billing Admin	Billing Admin	Assign permissions, configure billing policies, billing treatments, billing arrangements, legal entities, sequential numbering, generate account statements, and manage default records. Install and deploy service process templates for Billing dispute management. Install and configure the Dynamic Revenue Orchestrator feature and the Dunning Orchestration solution by using Salesforce Go.
Billing Operations User	Billing Operations User	Schedule invoice runs, generate account statements, manage invoice-related operations, and initiate dunning orchestration.
Billing Customer Service User	Billing Customer Service User	Generate invoices on demand for accounts and transactions, suspend and resume billing, resolve service requests for billing suspension, invoice due date extension, updating bill-to contact, and invoice charge correction.
Credit Memo Operations User	Credit Memo Operations User	Create, edit, and monitor credit memos.
Tax Admin	Tax Admin	Configure the tax engine, establish tax policies, and define tax treatment for billing.
Accounts Receivables Admin	Accounts Receivables Admin	Set up accounting periods and legal entities accounting periods, close legal entities accounting periods and accounting periods, and manage general ledger accounts and general ledger account assignment rules. Review and approve reconciled payment records.
Billing Collections and Recovery Specialist	Billing Collections and Recovery Specialist	Create collection plans and collection plan items for unpaid or partially paid invoices. Collect payment promises for the collection plan items, initiate dunning orchestration, and create payment schedule and payment schedule items.
Payment Admin	Payment Admin	Set up payment merchant accounts through supported native and third-party payment gateways and create saved payment methods. Automatically create payment schedules and payment schedule items based on default payment schedule policy, payment schedule treatment, payment schedule treatment detail, and payment schedule distribution method. Retry failed payments, issue refunds, and apply credits and payments to settle the balances of invoices or invoice lines. Turn on Level 2 and Level 3 data support. Generate Pay Now payment links to associate payments with business accounts.
Payment Operations User	Payment Operations User	Manually create and manage payment schedules and payment schedule items. Schedule payment batch runs to process payment schedule items for collecting and applying payments to invoices. Issue refunds, and apply credits and payments to settle the balances of invoices or invoice lines.
Billing Experience Cloud User	Billing Experience Cloud User	View and download invoices, and select a payment method or add a saved payment method for making payments on outstanding invoice balances. Raise service requests related to billing inquiries or invoice-related disputes.
Billing Permission Sets by API

Assign the API permission sets individually to users based on their role. You can also combine them with persona-based permission sets by creating permission set groups.

API NAME	PERMISSION SET	PERMISSIONS
Create Billing Schedules for Orders API	Create Billing Schedules From Billing Transactions API and Context Service Runtime	Create billing schedules by passing a list of order IDs.
Generate Invoices From Billing Schedule API	Generate Invoices From Billing Schedule API	Generate invoices on demand by using the billing schedules.
Tax Calculation API	CalculateTaxes API	Calculate the tax for a transaction.
Invoice Run Recovery API	Manage Errors Using Invoice Error Recovery API	Detect and correct invoicing errors, automate error resolution, and provide tools for manual overrides and detailed diagnostics.
Void a Posted Invoice API	Void a Posted Invoice API	Void posted invoices if there are errors.
SEE ALSO
View and Manage Users
Create or Clone Profiles
Manage Permission Set Assignments

=== ARTICLE: ind.billing_policies_and_treatments.htm ===
---
article_id: ind.billing_policies_and_treatments.htm
title: Define Billing Policies and Billability Rules
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_policies_and_treatments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Define Billing Policies and Billability Rules

Define billing policies, treatments, and treatment items to generate invoices that suit your sales models. Specify product billability rule criteria to define whether you want to bill your products in advance or in arrears, whether specific products are billed, and other conditions.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Create Billing Policies, Treatments, and Treatment Items
Define billing policies, treatments, and treatment items to generate invoices that suit your sales models.
Understand Exclude From Billing
When you set Exclude From Billing on a billing treatment value to Yes, the system skips creating billing schedules, billing schedule groups, and invoices for order items that aren’t ready for billing. Instead of delaying the entire order, you can exclude specific order items and continue processing the rest. When the excluded order items are ready, set Exclude From Billing to No, or assign a billable treatment to the order item, and then reprocess the order so the system reevaluates the items.
Understand Billing Treatment Resolution
The billing treatment field of an order product determines how it is billed. If the billing treatment is missing on the order product, an attempt is made to resolve the issue and assign an active billing treatment during the resolution.

=== ARTICLE: ind.billing_policies_and_treatments_create.htm ===
---
article_id: ind.billing_policies_and_treatments_create.htm
title: Create Billing Policies, Treatments, and Treatment Items
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_policies_and_treatments_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_policies_and_treatments.htm
fetched_at: 2026-09-04
---

# Create Billing Policies, Treatments, and Treatment Items

Define billing policies, treatments, and treatment items to generate invoices that suit your sales models.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create billing policies, treatments, and treatment items:	

Billing Admin permission set

OR

Billing Operations User permission set

Create Billing Policies

A billing policy is a group of billing treatments that consist of the rules to establish billing schedules for generating invoices. The billing policies are linked to products and applied to the resulting order product items.

From the App Launcher, find and select Billing Policies.
Click New.
Enter a name for the billing policy.
Select Draft as the status.
You can create billing policies only in the Draft status when there are no related active billing treatments.
Select how you want to assign billing treatments to the order items associated with the billing policy.
To use the billing treatment mentioned in the Default Billing Treatment field, select Default.
To use the billing treatment of the related order product, select Manual.
To use the billing treatment of the legal entity, select Legal Entity.
Select a default billing treatment.
To activate the billing policy, you must define a default billing treatment.
If necessary, enter a description.
Save your changes.

After you create a billing policy, create the related billing treatment.

Create Billing Treatments

Billing treatments are the set of rules that determine how an order item is billed.

From the App Launcher, find and select Billing Treatments.
Click New.
Enter a name for the billing treatment.
Select the billing policy for the billing treatment.
Multiple billing treatments are grouped to create a billing policy.
Select the legal entity.
Select Draft as the Status.
You can create billing treatments only in the Draft status when there are no related active billing treatment items.
If necessary, enter a description.
If you don't want to create billing schedules for the order items related to the billing treatment, select Yes as the Exclude From Billing value.
Save your changes.

After you create a billing treatment, create and activate a related billing treatment item.

Create Billing Treatment Items

Billing treatment items define how the order item’s total amount is distributed into billing schedules across the lifecycle of the order item.

You can create only one billing treatment item for each billing treatment.

From the App Launcher, find and select Billing Treatment Items.
Click New.
Enter a name for the billing treatment item.
Select a billing treatment for the billing treatment item.
Select Active as the status.
You can create billing treatment items in the Draft state also.
Enter the processing order in which you want to create billing schedules for the treatment item.
If necessary, enter a description.
Select how you want to bill the customers.
To bill the order product in advance, select Advance. The product is billed on the date that falls on or before the start date of the order product. For example, if a monthly order starts on January 1 and the billing date is the 15th, the first billing date is December 15.
To bill the order product after its start date, select Arrears. The item is billed on the date that falls after the start date of the order product. For example, if a monthly order starts on January 1 and the billing date is the 15th, the first billing date is January 15.
If your billing is based on milestones, select None to align charges with milestones.
When billing schedule group and billing schedule have a shared field with different values, select Billing Schedule Group as the controller to use the group's value.
Save your changes.

The Zero Amount Behavior, Type, Percentage, Flat Amount, and Sequencing values aren't considered when generating invoices. However, you must specify these values because they’re required to create a billing treatment item.

After you create an active billing treatment item, update the status of the related billing treatment to Active, and then update the status of the related billing policy to Active.

NOTE You can’t deactivate a billing treatment that is set as the default on an active billing policy.

=== ARTICLE: ind.billing_preview_invoice.htm ===
---
article_id: ind.billing_preview_invoice.htm
title: Generate Invoice Previews and Preview PDF Documents
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_preview_invoice.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_previews.htm
fetched_at: 2026-09-04
---

# Generate Invoice Previews and Preview PDF Documents

Generate invoice previews without generating an actual invoice and then generate PDF documents for the invoice previews. Share the PDF documents with your customers to reduce billing disputes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Prerequisites

Before you generate invoice previews, make sure that your Billing admin completes the prerequisite steps.

Set up document generation for Billing.
To generate invoice previews for Quote records, create a procedure plan, and then use either the Preview Invoices button or the Invoice Preview API.
Limits

Before you generate invoice previews, consider these limits.

You can generate invoice previews for a maximum of 200 billing schedules of accounts, orders, or billing schedule groups.
Before generating PDF documents for invoice previews, review the default limits for document generation requests and the process for increasing the maximum number of content versions that are published per day.
Generate Invoice Previews for Orders and Accounts
Preview invoices for the next two billing periods of orders and accounts. Generate and download PDF documents of the invoice previews.
Generate Invoice Previews for Billing Schedule Groups
Preview invoices for the next two billing periods of billing schedule groups.

=== ARTICLE: ind.billing_refund_orchestration.htm ===
---
article_id: ind.billing_refund_orchestration.htm
title: Initiate Automated Refunds on Negative and Canceled Invoices
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_refund_orchestration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_refunds_overview.htm
fetched_at: 2026-09-04
---

# Initiate Automated Refunds on Negative and Canceled Invoices

During subscription changes such as a quantity reduction or cancellation, Billing generates a negative invoice which then gets converted to a credit memo. This action triggers the automated refund process, where Billing automatically initiates the refund to the original payment method.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To initiate automated refunds on negative and canceled invoices:	

Billing Admin permission set

OR

Credit Memo Operations User permission set

How Automated Refund Process Works

When an amendment or cancellation is applied to a subscription associated with a fully settled invoice, Billing follows this sequence.

Calculate the refund amount based on the original invoice and the amendment or cancellation invoice.
Generate a credit memo to settle the original invoice.
Initiate refund orchestration process to issue the refund to the original payment method.
NOTE Refunds are initiated only when the payments are associated with a payment gateway.

To initiate funds, in Setup, find and select Billing Settings, and then turn on these features.

Issue Refunds and Settle Balances
Apply Credits to Posted Invoices

Billing automatically applies the balances of credit memo to settle the balances of posted invoices based on the credit application level.

To trace the refund back to its original transaction, follow these steps.

Open the credit memo generated by the amendment or cancellation.
Review the Payment and Invoice Applications section to view the original invoice balance, the unapplied amount, and the refund application details.
Confirm the refund amount and the payment method used for processing the refund.
EXAMPLE

A customer account has a one-year subscription starting in March 2026, totaling $3,000. The original invoice is generated, activated, and fully settled via a payment method linked to a payment gateway.

However, when an amendment reduces the subscription quantity by five, Billing generates amendment billing schedules, and applies a credit of $825 to the posted invoices. Billing automatically triggers the automated refund process, and the $825 refund amount is settled against the same payment method used in the initial transaction.

=== ARTICLE: ind.billing_refunds_overview.htm ===
---
article_id: ind.billing_refunds_overview.htm
title: Issue Refunds and Settle Balances
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_refunds_overview.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Issue Refunds and Settle Balances

A refund returns an amount that a customer no longer owes, such as an overpayment or an available credit balance. Billing issues a refund either automatically, after you cancel or reduce a subscription, or on demand, when you want to settle a customer’s available credit balance by using a credit memo.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Types of Refunds

Billing supports two types of refunds—referenced refunds and unreferenced (or non-referenced) refunds. They differ by whether the refund references an original payment, how and when the refund is issued, and which payment method receives the funds.

 	REFERENCED REFUND	UNREFERENCED REFUND
How the refund is issued	Automatically	Manually
When the refund is issued	When you cancel or reduce a subscription	When you settle an available credit balance back to the customer’s account.
Refund issued via	The original payment method used on the settled invoice.	A saved payment method resolved from the API request, the credit memo, or the billing account.
Applied to	The credit memo that the subscription change creates.	A credit memo or a credit memo line.
Requirements	The original payment is associated with a payment gateway.	The account has an available credit balance and uses a supported third-party payment gateway.
How Billing Processes Referenced Refunds

When you cancel or reduce a subscription, Billing calculates the refund amount and generates a credit memo to settle the resulting negative invoice. Billing then automatically issues the refund against the original payment method. Billing can initiate a referenced refund only when the original payment is associated with a payment gateway.

To issue referenced refunds, turn on Issue Refunds and Settle Balances on the Billing Settings page. For more information, see Initiate Automated Refunds on Negative and Canceled Invoices.

How Billing Processes Unreferenced Refunds

Customers build up credit balances from overpayments, adjustments, or canceled orders that have no payment to reference. An unreferenced refund returns an available credit balance against a credit memo instead of refunding back against the original payment. Accounts receivable and collections teams can issue an unreferenced refund against a credit memo or a credit memo line, and Billing automatically reduces the outstanding credit balance.

Billing pays the refund to a saved payment method through a supported third-party gateway. Teams also use unreferenced refunds to resolve billing disputes and overpayment claims by converting credit memo balances into refunds.

To learn how Billing applies and pays unreferenced refunds, see Refund Available Credit Balances to Customer Accounts. To issue an unreferenced refund, see Issue an Unreferenced Refund Against a Credit Memo.

Initiate Automated Refunds on Negative and Canceled Invoices
During subscription changes such as a quantity reduction or cancellation, Billing generates a negative invoice which then gets converted to a credit memo. This action triggers the automated refund process, where Billing automatically initiates the refund to the original payment method.
Refund Available Credit Balances to Customer Accounts
Refund a customer’s available credit balance against a credit memo or credit memo line without referencing an original payment.

=== ARTICLE: ind.billing_retry_failed_payments.htm ===
---
article_id: ind.billing_retry_failed_payments.htm
title: Retry Failed Payments
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_retry_failed_payments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Retry Failed Payments

Failed payments slow down cash flow and can lead to lost customers. When you enable automatic payment retries, Billing handles payment failures seamlessly and reprocesses each failed payment without manual intervention. You define a payment retry strategy that applies to all failed payments, with retry rules based on error categories such as insufficient funds or payment processing issues. For greater control and flexibility, you can define retry rules based on specific payment gateways and gateway-specific error codes. For each rule, you can configure the retry intervals that determine how often Billing can attempt to reprocess the failed payment. Additionally, you can set the maximum number of retry attempts, after which Billing either tries an alternate payment method or marks the payment request as failed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Key Terms

Here are a few key terms used when configuring payment retry rules and rule sets for failed payments.

Payment Retry Rule Set
The retry rule set that contains the default retry settings to be applied when no specific rule matches. It also contains default org preferences for retry behavior.
Payment Retry Rule
One or more rules that define specific retry behavior for various failure scenarios. The payment retry rule defines the retry category, the payment gateway, and the payment gateway raw error code. It also includes information on specific retry intervals and maximum attempts on failed payment records.
Retry Interval Type
The regular or varied intervals of time when the payment batch run retries the failed payment records.
Fixed: Sets a consistent time period between retry attempts. To retry at regular intervals of a few hours, minutes, or days, set the retry interval type as Fixed. For example, to retry every five days, set the retry interval type to Fixed and retry interval to 5.
Staggered: Sets different intervals for each retry attempt. To retry at varied intervals of time, set the retry interval type as Staggered. For example, to retry every second, fourth, and sixth hour, set the retry interval type to Staggered and retry interval to 2,4,6.
Maximum Retry Count
The maximum number of retries attempted by the payment batch run on failed payment records
Interval Unit
The unit of time such as hours, days, or minutes based on which a payment batch run tries again the failed payment records
Interval Value
The single or comma-separated values that determine the fixed or staggered intervals at which the payment batch run tries failed payment records again
Initial Setup
Define the Retry Rule Set: Create a payment retry rule set that defines your organization’s overall retry strategy. Define the rule set with relevant details such as the maximum retry count, interval value, interval unit, and a retry mode such as fixed or staggered. You can opt to use an alternate payment method in the last payment attempt when all previous attempts fail. A payment retry rule set acts as a parent record for a set of payment retry rules.
Define Retry Rules: Define one or more payment retry rules in the payment retry rule set. Create specific payment retry rules based on:
Payment gateway
Payment gateway error category
Payment gateway error code

The settings such as maximum retry count, retry interval type, interval value, and interval unit that are defined in the payment retry rule set are automatically inherited by all payment retry rules in the rule set. But, you can override these values in the payment retry rules that are part of the rule set.

Set a default payment retry rule set: Mark at least one rule set as active, and set it as the org default.
Turn On Retry Failed Payments setting: Enable the Retry Failed Payments feature for your org on the Billing Settings page.
Failed Payments Retry Process

When a payment fails, Billing retries the failed payment based on the retry behavior defined in the payment retry rule set and rules. Based on the next scheduled retry attempt defined in the retry rules, Billing continues to pick up failed payment schedule items until the retry attempts are exhausted or the payment succeeds, whichever is earlier.

If you opted to use an alternate payment method in the payment retry rule set, Billing uses the alternate payment method in the last attempt. For example, if the maximum retry count is 5, then the alternate payment method is used on the fifth retry.

For each payment schedule item, you can view the maximum retry count, payment retry value, and the next payment retry time in the payment schedule item record.

Payment Retry Rule Resolution at Run Time

When a payment for a payment schedule item fails, Billing searches for a payment retry rule that matches the payment gateway error. If Billing doesn’t find a match, it gradually broadens the search.

Billing looks for payment retry rules that match all three criteria–retry category, payment gateway, and raw error code.
If no match is found, Billing searches for payment retry rules matching the retry category with the payment gateway, and then the retry category with raw error code.
If no match is found, Billing searches for payment retry rules based only on the retry category.

If none of these searches find a match, Billing applies the default values from the payment retry rule set.

Payment Method Application

Based on the maximum retry count, Billing automatically retries failed payments by using the payment method specified on the payment schedule item. However, if you opted to use an alternate payment method in the payment retry rule set, then Billing attempts the last retry by using the alternate payment method. Billing automatically selects the appropriate payment method based on recency and availability.

If the failed payment method isn’t the account’s default payment method, then Billing uses the account default payment method.
If the failed payment method is already the account’s default payment method, then Billing uses the most recently created payment method that’s different from the existing one.
Payment Gateway Error Categories

A payment transaction sent across a payment gateway can fail due to multiple reasons such as insufficient funds, incorrect card information, or a connectivity issue. When you set up Billing for retrying failed payments, you can define payment retry rules for specific types of errors based on the failure reasons. For each payment retry rule, you can select from these predefined error categories.

ERROR CATEGORY	DESCRIPTION
Card Limit Decline	Insufficient funds, exceeded spending limits, or other restrictions on the card.
Payment Processing Error	Payment account is invalid, closed, restricted, or the transaction was declined for reasons other than insufficient funds.
Invalid Payment Details	Missing or incorrect data such as incorrect card numbers, addresses, or currencies.
Security Failure	Security violations or issues such as fraud, risk, authentication, verification, and authorization.
Gateway Connection Error	Connectivity or communication errors between systems, including upstream gateway errors.
Internal Validation Error	An internal error occurred due to a validation failure even before the request was sent to the gateway.
Unknown Error	Payment gateway error code isn't recognized or isn't mapped to a specific category.
Set Up Payment Retry Rules
Define payment retry rule sets and payment retry rules and configure Billing to automatically retry failed payments for specific error categories at various time intervals.
Examples: Configure Payment Retry Rule Sets and Retry Rules
Let’s explore a few examples for creating and configuring payment retry rule sets and rules.

=== ARTICLE: ind.billing_review_split_invoices.htm ===
---
article_id: ind.billing_review_split_invoices.htm
title: Review Split Invoices Before Posting, Voiding, or Deleting
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_review_split_invoices.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoice_generation.htm
fetched_at: 2026-09-04
---

# Review Split Invoices Before Posting, Voiding, or Deleting

Before you post, void, or delete an invoice from a billing arrangement, review the related split invoices on the Split Invoices tab. Each card shows status, account, total with tax, settlement status, bill-to contact, billing profile, and invoice date.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To view all related split invoices:	

Billing Admin permission set

OR

Billing Operations User permission set

When a billing arrangement splits a charge across accounts, Billing generates related split invoices. Review those invoices together before you post, void, or delete any one of them.

NOTE

An action that you take on one split invoice, such as posting, voiding, or deleting, also applies to the related split invoices.

Open the invoice record that was generated from a billing arrangement.
Select the Split Invoices tab.

Each split invoice card shows status, account, total amount with tax, settlement status, bill-to contact, billing profile, and invoice date.

Click an invoice number to open that record.

After you review the related split invoices, post, void, or delete the invoice.

=== ARTICLE: ind.billing_rules_based_credits_payments_application.htm ===
---
article_id: ind.billing_rules_based_credits_payments_application.htm
title: Invalid Match ID During Payment Application
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_rules_based_credits_payments_application.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_credit_memos_payments_application_rules.htm
fetched_at: 2026-09-04
---

# Invalid Match ID During Payment Application

When a payment is applied using the Match ID rule, the invoice ID specified on the payment record is validated. If the referenced invoice is deemed invalid, the payment is applied to the next available invoice based on the subsequent rule in the sequence.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

An invoice is considered invalid for the Match ID rule in these scenarios.

The Invoice ID specified on the Payment record is in Draft status.
The referenced invoice is posted but has a zero balance.
The legal entity of the referenced invoice and the payment are different.
The related account of the referenced invoice and the payment are different.
The currency ISO code of the referenced invoice and the payment are different.

=== ARTICLE: ind.billing_rules_based_credits_payments_example.htm ===
---
article_id: ind.billing_rules_based_credits_payments_example.htm
title: "Example: Apply Rule-Based Credits and Payments"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_rules_based_credits_payments_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_credit_memos_payments_application_rules.htm
fetched_at: 2026-09-04
---

# Example: Apply Rule-Based Credits and Payments

Explore an example to understand the setup of rule-based credits and payments in your Salesforce org, and how credit memos and payments are applied to posted invoices of the same account.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Initial Setup

On the Billing Settings page, the Billing Admin makes these selections.

Application Order: Credits First
Allocation Rules and Sequence: Match Balance, Prioritize Highest Balance Invoices, and Prioritize Oldest Invoices
Credit and Payment Application Level: Invoice Line

Then, the Billing Admin enables Rule-Based Credit and Payment Application.

Record Details

The Billing Operations user creates these records for their customer, Acme Corp.

Credit Memo 1 with a balance amount of 100 USD.
Credit Memo 2 with a balance amount of 75 USD.
Payment 1 with a balance amount of 80 USD.
Invoice Generation

The Billing Operations user then schedules an invoice batch run to generate these invoices and invoice lines for Acme Corp.

INVOICE	INVOICE LINE	BALANCE AMOUNT
Invoice 1	Invoice Line 1	50 USD
 	Invoice Line 2	50 USD
Invoice 2	Invoice Line 1	150 USD
 	Invoice Line 2	50 USD
Allocation of Rules and Sequence

When the invoices are posted, the selected rules are applied sequentially to reduce the outstanding balances on the invoices.

Allocation Rule: Match Balance
Credit Memo 1: Invoice 1 is found with a matching balance of 100 USD. Credit Memo 1 is applied to Invoice Line 1 and Invoice Line 2 of Invoice 1, settling the invoice.
Credit Memo 2: No matching balance invoice is found for applying credits.
Payment 1: No matching balance invoice is found for applying payments.
Allocation Rule: Prioritize Highest Balance Invoices
Credit Memo 2: Invoice 2 with a highest balance of 200 USD is found. Credit Memo 2 is applied to Invoice Line 1 of Invoice 2, that had a balance amount of 150 USD. After applying the credit memo, the remaining balance on Invoice Line 1 is 75 USD.

Invoice 2 has a remaining balance of 125 USD.

Payment 1:
NOTE When the invoice with the highest balance is found, credit memos and payments are applied to it to settle the invoice or invoice line. After an invoice is settled, the invoice with the next highest balance is retrieved, and credit memo and payments are applied accordingly.
Payment 1 is applied to Invoice Line 1 of Invoice 2 that has a balance amount of 75 USD. Invoice Line 1 is settled and Payment 1 shows a balance of 5 USD.
The remaining payment balance of 5 USD is applied to the next highest balance line, that’s Invoice Line 2 of Invoice 2, with a balance amount of 50 USD. After applying the payment, Invoice Line 2 shows a balance amount of 45 USD.
Invoice Status

Here's the status of the invoice records after applying credits and payments.

The credit and payment amounts on Credit Memo 1, Credit Memo 2, and Payment 1 are applied to Invoice 1 and Invoice 2.
Invoice 1 is settled.
Invoice 2 is partially settled with a remaining balance of 45 USD.

=== ARTICLE: ind.billing_saved_payment_methods.htm ===
---
article_id: ind.billing_saved_payment_methods.htm
title: Configure Saved Payment Methods for Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_saved_payment_methods.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Configure Saved Payment Methods for Revenue Management

Collect one-time or scheduled recurring payments by securely saving the payment methods of your customers, rather than manually entering payment method details each time a payment is processed. Save various payment methods from native or third-party payment gateways, and set a default saved payment method for each account.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To create saved payment methods:	Payment Operations User permission set
Prerequisites

Before saving payment methods for accounts, complete these steps.

Complete the setup steps.
To enable standard users to create saved payment methods by using the Merchant Account records created by your Payment admins, select the default internal access of the Merchant Account object to Public Read Only.
Add the Dynamic Related List–Single component to the Saved Payment Method tab of Account records, and select Saved Payment Methods as the related list.
Create Saved Payment Methods

You can save multiple payment methods for a single account or save the same payment method for different customer accounts. You can also choose to set a default payment method for an account.

From the App Launcher, find and select Billing, and then click Accounts.
Open the Account record for which you want to create a saved payment method.
On the Saved Payment Methods tab, select the merchant account that you want to use for receiving payments from the account.
You can save payment methods for different customer accounts with the same merchant account.
Select the payment method that you want to add such as a credit card, bank account, or any other third-party payment method, and then enter the required details.
The combination of merchant account and payment method for an account must be unique.
Optionally, set a payment method on your native payment gateway as the default payment method for the account.
Save your work.

The saved payment method appears in the Saved Payment Methods related list of the Saved Payment Methods tab.

If the saved payment method you’re creating has the same merchant account and payment method details as an existing record, but contains changes to other details, such as the name on the card, the details of the existing Saved Payment Method record is updated.

NOTE You can create saved payment methods for MOTO payments in native payment gateways only.

=== ARTICLE: ind.billing_schedule_details_component.htm ===
---
article_id: ind.billing_schedule_details_component.htm
title: Add the Billing Schedule Details Component to a Group Page
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedule_details_component.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_and_schedule_groups.htm
fetched_at: 2026-09-04
---

# Add the Billing Schedule Details Component to a Group Page

Give billing operations and sales teams a timeline and summary metrics on the Billing Schedule Group page. In Lightning App Builder, drag Billing Schedule Details onto the page, then save and activate the page.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To add the Billing Schedule Details component:	Customize Application
To view billing schedule timelines:	

Billing Admin permission set

OR

Billing Operations User permission set

The Billing Schedule Details component shows summary metrics and a visual timeline of billing schedules in a billing schedule group. After you add the component, teams can evaluate billing outcomes and demonstrate complex billing from the Billing Schedule Group record. See Generated Billing Schedule Details.

Open a Billing Schedule Group record.
From Setup, select Edit Page.
From the Lightning App Builder components palette, drag Billing Schedule Details onto the page canvas.
Save your changes, then activate the page.

=== ARTICLE: ind.billing_schedule_group_update.htm ===
---
article_id: ind.billing_schedule_group_update.htm
title: Update Billing Schedule Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedule_group_update.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_and_schedule_groups.htm
fetched_at: 2026-09-04
---

# Update Billing Schedule Groups

Update billing schedule group fields at any time. You can update the billing day of month, next billing date override, billing and shipping addresses, tax treatment, and the payment term of a billing schedule group.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To update billing schedule groups:	

Billing Admin permission set

OR

Billing Operations User permission set

From the App Launcher, find and select Billing Schedule Groups.
Open the Billing Schedule Group record that you want to update.
Update the necessary fields.
Save your work.
Bill Day of Month
Bill day of the month is the day of the month on which a recurring billing process is scheduled to occur to generate invoices from billing schedules.
Next Billing Date Override
The next billing date override overrides the next billing dates of all the billing schedules.
Billing Start Month
The billing start month indicates the month when billing begins for an annual subscription. For example, if billing starts in January, the value is 1; if billing starts in June, the value is 6.

=== ARTICLE: ind.billing_schedule_group_update_billing_day_of_month.htm ===
---
article_id: ind.billing_schedule_group_update_billing_day_of_month.htm
title: Bill Day of Month
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedule_group_update_billing_day_of_month.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedule_group_update.htm
fetched_at: 2026-09-04
---

# Bill Day of Month

Bill day of the month is the day of the month on which a recurring billing process is scheduled to occur to generate invoices from billing schedules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Eligibility Conditions for Updating Bill Day of Month

The bill day of month can be updated only if these conditions are met:

The billing term unit of the billing schedule group can't be Milestone Plan.
The billing method of the billing schedule group can't be Usage.
The status of any of the billing schedules related to the billing schedule group can't be Processing or Error.
Updating Bill Day of Month when Billing Type is Advance

If the bill day of month is updated when the billing type is Advance, the next billing date and the next charge date of the related billing schedules remain the same until invoices are generated for the first time. Updating the bill day of month results in these changes:

RESULT	EXAMPLE


When the target date is on the original next billing date:

When an invoice is generated for the first time, it's generated for a partial period. The start date of the partial billing period is the original next charge date and the end date is based on the updated bill day of month.
After invoices are generated for the first time, the next billing date and the next charge date are updated based on the updated bill day of month.
The subsequent invoice is generated for a complete period. The start date of the complete billing period is based on the updated bill day of month and the end date is one day before the next billing date.
	

The current month is January, the bill day of month is 17, and the billing frequency is monthly. So, the billing schedules have these values:

Next Billing Date: 01/17/2025
Next Charge Date: 01/17/2025

The billing operations user has updated the bill day of month to 25.

The target date for generating invoices is 01/17/2025. So, when an invoice is generated on 01/17/2025, it's generated for the partial period of 01/17/2025 to 01/24/2025.

The next billing date is then updated to 01/25/2025 and the next charge date is updated to 02/25/2025.

The subsequent invoice is generated for the period of 01/25/2025 to 02/24/2025.




When the target date is on the updated next billing date:

A partial invoice and a complete invoice are generated after the bill day of month is updated.
The start date of the partial billing period is the original next charge date and the end date is based on the updated bill day of month.
The start date of the complete billing period is based on the updated bill day of month and the end date is one day before the next billing date.
	

The current month is January, the bill day of month is 17, and the billing frequency is monthly. So, the billing schedules have these values:

Next Billing Date: 01/17/2025
Next Charge Date: 01/17/2025

The billing operations user has updated the bill day of month to 25.

The target date for generating invoices is 01/25/2024. So, when invoices are generated on 01/25/2025:

An invoice is generated for the partial period of 01/17/2025 to 01/24/2025.
An invoice is generated for the complete period of 01/25/2025 to 02/24/2025.

The next billing date is then updated to 02/25/2025 and the next charge date is updated to 02/25/2025.

Updating Bill Day of Month when Billing Type is Arrears

If the bill day of month is updated when the billing type is Arrears, it results in these changes:

The next billing date of the related billing schedules is updated immediately.
When invoices and billing period items are generated for the first time after the bill day of month is updated, they’re generated for a partial period.
Subsequent invoices and billing period items are generated for complete periods.

For example, let's assume that the current month is January, the bill day of month is 17, and the billing frequency is monthly. So, the billing schedules have these values:

Next Billing Date: 02/17/2025
Next Charge Date: 01/17/2025

The billing operations user has updated the bill day of month to 25.

The target date for generating invoices is 02/25/2025. So, when an invoices are generated on 02/25/2025: it's generated for the partial period of 01/17/2025 to 01/24/2025.

An invoice is generated for the partial period of 01/17/2025 to 01/24/2025.
An invoice is generated for the complete period of 01/25/2025 to 02/24/2025.

The next billing date is updated to 03/25/2025 and the next charge date is updated to 02/25/2025.

The subsequent invoice is generated for the period of 02/25/2025 to 03/24/2025.

=== ARTICLE: ind.billing_schedule_group_update_billing_start_month.htm ===
---
article_id: ind.billing_schedule_group_update_billing_start_month.htm
title: Billing Start Month
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedule_group_update_billing_start_month.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedule_group_update.htm
fetched_at: 2026-09-04
---

# Billing Start Month

The billing start month indicates the month when billing begins for an annual subscription. For example, if billing starts in January, the value is 1; if billing starts in June, the value is 6.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Eligibility Conditions for Updating Billing Start Month

The billing day of month can be updated only if these conditions are met:

The billing term unit of the billing schedule group must be Semi-Annual or Quarter.
The billing method of the billing schedule group can't be Usage.

=== ARTICLE: ind.billing_schedule_group_update_next_billing_date_override.htm ===
---
article_id: ind.billing_schedule_group_update_next_billing_date_override.htm
title: Next Billing Date Override
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedule_group_update_next_billing_date_override.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedule_group_update.htm
fetched_at: 2026-09-04
---

# Next Billing Date Override

The next billing date override overrides the next billing dates of all the billing schedules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Eligibility Conditions for Updating Next Billing Date Override

The next billing date override can be updated only if these conditions are met:

The billing term unit of the billing schedule can't be Milestone Plan.
The status of the related billing schedules must be Ready for Invoicing.
The status of all the billing schedules related to the billing schedule group can't be Completely Billed.
The next billing date override must be greater than the current date, and between the effective next billing date and end date of the billing schedule group.
Updating Next Billing Date Override

When the next billing date override is updated, it results in these changes:

To generate invoices for the related billing schedules, billing schedule groups that have the next billing date override before the target date are considered.
Invoices are generated on the next billing date override instead of the next billing date of the related billing schedules. The invoice is generated for the charge period between the original next charge date and the next billing date override.
The next billing date override is used only once for generating invoices. It’s removed after the invoices are generated.

For example, the current month is April and a billing schedule group has these values:

Billing Type: Advance
Bill Day of Month: 15
Next Billing Date Override: 04/20/2025

The related billing schedules have these values:

Next Billing Date: 04/15/2025
Next Charge Date: 04/15/2025

When a target date that's on or after 04/20/2025 is specified for generating invoices, invoices are generated for these billing schedules. After the invoices are generated, the Next Billing Date Override value is removed.

=== ARTICLE: ind.billing_schedule_invoice_grouping.htm ===
---
article_id: ind.billing_schedule_invoice_grouping.htm
title: Define Invoice Grouping on a Billing Schedule
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedule_invoice_grouping.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_and_schedule_groups.htm
fetched_at: 2026-09-04
---

# Define Invoice Grouping on a Billing Schedule

Generate grouped or split invoices by configuring default, custom, or billing schedule group types on billing schedules.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To edit billing schedules:	

Billing Admin permission set

OR

Billing Operations User permission set

On the billing schedule, define the invoice grouping type. Consolidated or individual invoice records are created based on the invoice grouping type.

From the App Launcher, find and select Billing Schedule Groups.
Open the billing schedule group that your billing schedule belongs to.
Go to the Billing Schedules related list and open the billing schedule.
On the Detail tab of the Billing Schedule record, go to the Invoice Group Information section and select an invoice group type:
To generate a consolidated invoice based on the default group, select Default. The billing account, bill-to-contact, currency ISO code, payment term, tax engine, legal entity, and saved payment method of the billing schedule group make up the default group.
To generate a separate invoice for the billing schedule, select Billing Schedule.
To generate a consolidated invoice based on your own grouping criteria, select Custom.
If you select Custom as the invoice group type, enter a custom invoice group key.
The custom invoice group key isn't case-sensitive. The key can be contract number, purchase order number, account, legal entity, or your own value. Consolidated invoices are generated when the billing schedules have the same default group and custom invoice group key. While grouping invoices during invoice generation process, the default group is considered first, followed by the custom invoice group key.
EXAMPLE A billing operations user selects specific invoice group types for five billing schedules of an order.
BILLING SCHEDULES	INVOICE GROUP TYPE	CUSTOM INVOICE GROUP KEY
Billing Schedule 1	Default	

—


Billing Schedule 2	Billing Schedule	

—


Billing Schedule 3	Custom	00000101 [Contract Number]
Billing Schedule 4	Default	

—


Billing Schedule 5	Custom	00000101 [Contract Number]

Three separate invoices are generated based on the Invoice Group Type field, and the Custom Invoice Group Key field:

A consolidated invoice is generated for Billing Schedule 1 and Billing Schedule 4 because both of them have the same default invoice group.
A separate invoice is generated for Billing Schedule 2 because its invoice group type is Billing Schedule, which results in generating an individual invoice.
A consolidated invoice is generated for Billing Schedule 3 and Billing Schedule 5 because both of them have the same default invoice group and custom invoice group key.

=== ARTICLE: ind.billing_schedules_and_schedule_groups.htm ===
---
article_id: ind.billing_schedules_and_schedule_groups.htm
title: Manage Billing Schedules and Billing Schedule Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedules_and_schedule_groups.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Manage Billing Schedules and Billing Schedule Groups

Billing schedules define when and how an order product is invoiced. Billing schedule groups contain one or more billing schedules. Both of these are created and updated as a result of creating, amending, and canceling orders. You can generate billing schedules directly from transactions in external systems, or from any Salesforce object by using Create Standalone Billing Schedules API. To generate billing schedules from orders, use the Order to Billing Schedule flow, Create Billing Schedules for Orders API, or Create Standalone Billing Schedules API.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
NOTE For details about how billing schedules are triggered and how invoices are grouped, see Understanding Billing Schedule Creation and Invoice Generation.
Generate Billing Schedules from External Transactions or Salesforce Objects
Use the Create Standalone Billing Schedules API to generate billing schedules directly from transactions in external systems, or from any Salesforce object.
Generate Billing Schedules from Orders
Generate billing schedules from orders by using a flow or an API.
Generated Billing Schedule Details
View all the key billing schedule and invoice details in the Billing Schedule Group records.
Add the Billing Schedule Details Component to a Group Page
Give billing operations and sales teams a timeline and summary metrics on the Billing Schedule Group page. In Lightning App Builder, drag Billing Schedule Details onto the page, then save and activate the page.
Manage Billing Frequencies
You can set a product’s billing frequency to be different from its pricing frequency. For example, you can bill a customer on an annual basis even if the order or subscription is priced monthly.
Bill for Multiple Terms in a Billing Period
Your sales reps can now set up flexible terms for billing subscriptions whether it’s every three weeks, every five months, or every two years. For example, to bill a subscription every three months, your sales reps can set the billing frequency to monthly and billing term to 3 on the order product. Billing automatically calculates the correct amount for the combined period and sets the next billing date accordingly.
Update Billing Schedule Groups
Update billing schedule group fields at any time. You can update the billing day of month, next billing date override, billing and shipping addresses, tax treatment, and the payment term of a billing schedule group.
Define Invoice Grouping on a Billing Schedule
Generate grouped or split invoices by configuring default, custom, or billing schedule group types on billing schedules.

=== ARTICLE: ind.billing_schedules_from_order_items.htm ===
---
article_id: ind.billing_schedules_from_order_items.htm
title: Use Create Standalone Billing Schedules API
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedules_from_order_items.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_from_orders.htm
fetched_at: 2026-09-04
---

# Use Create Standalone Billing Schedules API

For one-time, termed, and evergreen products, use Create Standalone Billing Schedules API to generate billing schedules from orders and order items.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Order To Billing Schedule flow template and Create Billing Schedules for Orders API are available with the Revenue Management Advanced license or the Agentforce Revenue Management Billing license.

In the request body of Create Standalone Billing Schedules API, specify the BillingContext standard context definition as the contextDefinitionName property value.

=== ARTICLE: ind.billing_schedules_from_orders.htm ===
---
article_id: ind.billing_schedules_from_orders.htm
title: Generate Billing Schedules from Orders
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedules_from_orders.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_and_schedule_groups.htm
fetched_at: 2026-09-04
---

# Generate Billing Schedules from Orders

Generate billing schedules from orders by using a flow or an API.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Order To Billing Schedule flow template and Create Billing Schedules for Orders API are available with the Revenue Management Advanced license or the Revenue Management Billing license.
USER PERMISSIONS
NEEDED
To use Create Billing Schedules for Orders API:	

Create Billing Schedules From Billing Transactions API permission

AND

Context Service Runtime permission set


To use Order To Billing Schedule flow template:	

Billing Admin permission set

AND

Billing Operations User permission set


To generate billing schedules for usage-based charge types:	

Product Catalog Management Viewer permission set

OR

Usage Management Runtime permission set

To automatically trigger the generation of billing schedules when the order is activated, use the Order to Billing Schedule flow. To generate billing schedules for orders by using API, use Create Billing Schedules for Orders API or Create Standalone Billing Schedules API.

IMPORTANT

Use the Order to Billing Schedules API and Order to Billing Schedules flow for any new sale, amendments, renewals, or cancellations that originate from Revenue Management orders and assets.

Use Order to Billing Schedule Flow
Use the Order to Billing Schedule flow to automatically generate billing schedules and billing schedule groups from order items as soon as orders are activated.
Use Create Billing Schedules for Orders API
Use Create Billing Schedules for Orders API to generate billing schedules from orders.
Use Create Standalone Billing Schedules API
For one-time, termed, and evergreen products, use Create Standalone Billing Schedules API to generate billing schedules from orders and order items.

=== ARTICLE: ind.billing_schedules_from_transactions_create.htm ===
---
article_id: ind.billing_schedules_from_transactions_create.htm
title: Use Create Billing Schedules for Orders API
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedules_from_transactions_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_from_orders.htm
fetched_at: 2026-09-04
---

# Use Create Billing Schedules for Orders API

Use Create Billing Schedules for Orders API to generate billing schedules from orders.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Order To Billing Schedule flow template and Create Billing Schedules for Orders API are available with the Revenue Management Advanced license or the Agentforce Revenue Management Billing license.

Before using Create Billing Schedules for Orders API, select the context definition and the context mapping from the Billing settings page or create a custom procedure plan definition.

Create a custom procedure plan definition with these values.
Select Billing as the process type.
Select the object that you want to generate billing schedules for as the primary object.
Select the context definition extended from BillingContext as the context definition.
Update and activate the procedure plan definition.
Open the procedure plan definition and select a read context mapping for the primary object.
Activate the procedure plan definition.
To create billing schedules from orders, use Create Billing Schedules for Orders API.

To automate this process for external transactions or Salesforce objects, design a custom flow and add the Create Billing Schedules From Billing Transaction action.

Generate invoices from these billing schedules by scheduling invoice runs, from the Order record pages, or by using an API.

=== ARTICLE: ind.billing_schedules_standalone_api.htm ===
---
article_id: ind.billing_schedules_standalone_api.htm
title: Generate Billing Schedules from External Transactions or Salesforce Objects
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_schedules_standalone_api.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_and_schedule_groups.htm
fetched_at: 2026-09-04
---

# Generate Billing Schedules from External Transactions or Salesforce Objects

Use the Create Standalone Billing Schedules API to generate billing schedules directly from transactions in external systems, or from any Salesforce object.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Create Standalone Billing Schedules API is available with the Revenue Management Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To generate billing schedules for usage-based charge types:	

Product Catalog Management Viewer permission set

OR

Usage Management Runtime permission set

Generate billing schedules on-demand and eliminate the need for importing or replicating complex data by using the Create Standalone Billing Schedules API. The API supports various transaction types, including original, amended, canceled, renewed, ramped, bundled, or usage-based transactions.

To automate this process for external transactions or Salesforce objects, design a custom flow and add the Create Standalone Billing Schedules action.

Starting Summer ‘26, you can use the enhanced Create Standalone Billing Schedules API to pass minimal, intent-based requests for amendments, renewals, cancellations, and any changes to price, quantity, or end dates. Billing automatically computes the required fields such as unit price and total price by using historical transaction context or Billing Schedule Group IDs.

IMPORTANT When a billing schedule group is linked to an asset, initiate any new sale, amend, renew, or cancel actions directly from the order or asset. In such cases, use the Order to Billing Schedule flow or Create Billing Schedules for Orders API, and not the Create Standalone Billing Schedules API.

=== ARTICLE: ind.billing_self_service_lwr_components.htm ===
---
article_id: ind.billing_self_service_lwr_components.htm
title: Add Billing Components to LWR Experience Cloud Sites
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_self_service_lwr_components.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_self_service_portal.htm
fetched_at: 2026-09-04
---

# Add Billing Components to LWR Experience Cloud Sites

Add billing self-service capabilities to any Experience Cloud site that uses Lightning Web Runtime (LWR) templates, including a site that you build yourself. Drag the Posted Invoices, Invoice Line Viewer, Self-Service Payment Sheet, Self-Service Payment Confirmation, and Manage Saved Payment Methods components onto your pages so that customers can view invoices, pay outstanding balances, and manage their saved payment methods from your own branded site.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To use the Billing self-service components in an Experience Cloud site:	Billing Experience Cloud User permission set

The Self-Service Billing Portal template gives you a ready-to-use site. These components add the same billing capabilities to any LWR site, including the Build Your Own (LWR) template.

These components are available in the components palette, under the Layout section, in Experience Builder.

Posted Invoices: shows a list of posted invoices for the current user's account.
Invoice Line Viewer: shows the line items of an invoice.
Self-Service Payment Sheet: shows the payment methods available for an invoice, including saved payment methods. Customers can also add a new payment method, save it for future use, and then submit a payment.
Self-Service Payment Confirmation: shows whether a payment that a customer submitted from the Self-Service Payment Sheet succeeded.
Manage Saved Payment Methods: shows customers their saved payment methods so that they can add or delete a saved payment method and set a default.
Add a Billing Component to Your Page
In Experience Builder, open the page where you want to add the component.
In the components palette, under Layout, find the component that you want to add.
Drag the component onto your page.
Configure the component's properties.

Required fields vary by component.

NOTE

Some components need redirect links to other components. For example, Self-Service Payment Sheet redirects to the site page for payment confirmation.

Publish your site for the changes to take effect.

=== ARTICLE: ind.billing_self_service_portal.htm ===
---
article_id: ind.billing_self_service_portal.htm
title: Self-Service Billing Portal
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_self_service_portal.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Self-Service Billing Portal

The self-service billing portal is a customer-facing Experience Cloud site that enables end users and community users to raise and track their billing inquiries and disputes. Your customers can view and download invoice PDF documents and quickly pay the outstanding balances of invoices by using supported payment methods. The self-service portal minimizes manual intervention and improves cash flow and customer satisfaction.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Raise Billing Inquiries and Invoice-Related Disputes
The self-service Billing portal serves as the customer-facing gateway that transforms manual, phone-based dispute processes into a streamlined, transparent self-service experience. The Help Center tab provides a catalog of available billing service processes. The Cases tab shows all cases and their statuses for the customer account.
Pay Invoices with the Self-Service Billing Portal
When your customers log in to the self-service billing portal, they can view invoices, download invoice PDF documents, and pay outstanding balances for the invoices. The Home tab shows the list of invoices that aren't settled, partially settled, and settled.
Supported Payment Methods for the Self-Service Billing Portal
Give your customers more flexibility to pay invoices by configuring additional payment methods, including digital wallets, bank debit methods, and buy now, pay later options, in the Self-Service Billing Portal.
Add Billing Components to LWR Experience Cloud Sites
Add billing self-service capabilities to any Experience Cloud site that uses Lightning Web Runtime (LWR) templates, including a site that you build yourself. Drag the Posted Invoices, Invoice Line Viewer, Self-Service Payment Sheet, Self-Service Payment Confirmation, and Manage Saved Payment Methods components onto your pages so that customers can view invoices, pay outstanding balances, and manage their saved payment methods from your own branded site.

=== ARTICLE: ind.billing_self_service_portal_pay_invoices.htm ===
---
article_id: ind.billing_self_service_portal_pay_invoices.htm
title: Pay Invoices with the Self-Service Billing Portal
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_self_service_portal_pay_invoices.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_self_service_portal.htm
fetched_at: 2026-09-04
---

# Pay Invoices with the Self-Service Billing Portal

When your customers log in to the self-service billing portal, they can view invoices, download invoice PDF documents, and pay outstanding balances for the invoices. The Home tab shows the list of invoices that aren't settled, partially settled, and settled.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To create and customize an Experience Cloud site by using the Self-Service Billing Portal template:	Billing Admin permission set
To access the Experience Cloud site created by using the Self-Service Billing Portal template:	Billing Experience Cloud User permission set

Before you begin, configure your Experience Cloud site users and provide them access to view invoices.

Create Customer Community Plus users or Partner Community users for your Experience Cloud site. See Experience Cloud Sites and Users in Your Salesforce Org.
Create a Sharing Set for Experience Cloud Site Users. to provide your Customer Community Plus users or Partner Community users with access to view the invoice records.
Create an Experience Cloud site by using the Self-Service Billing Portal template. To meet your company's requirements and branding, customize the site with the Experience Cloud builder.

To process payments in an Experience Cloud site, specify a merchant account ID. Before you specify a merchant account ID, set up a payment merchant account.

Set Up the Self-Service Billing Portal for Payments

Configure your Experience Cloud site to accept payments by specifying merchant account details and payment method options.

On the template's home page, from the Experiences menu, select Invoice and Payment Details.
Click the Invoice Payment Options component.
Enter a merchant account ID.
Optionally, to enable additional payment methods such as digital wallets and buy now or pay later options, enter the Payment Method Set ID. To retrieve the Payment Method Set ID, run this query in the Developer Console: SELECT Id, DeveloperName, MerchantAccountId FROM MerchAccPaymentMethodSet
Note: If you don't add a Payment Method Set ID, the portal shows only credit card, ACH, and saved payment methods.
Optionally, to support express payment methods such as Apple Pay, Amazon Pay, and Google Pay, add the Express Payments component to the Invoice and Payment Details page.
In the component properties, set Account ID to {!CurrentUser.effectiveAccountId}, Merchant Account to your merchant account ID, and Payment Method Set ID to your payment method set ID.
On the Invoice Payment Status page, set the Payment Method field to {!paymentMethod}.
Publish the site for the changes to take effect.

After you set up your Experience Cloud site, configure the email that you want to send to your customers. When an invoice is generated, the customer receives an email with a link to the Experience Cloud site and the details of the invoice. See Send Invoices Through Email.

Pay Invoices in the Self-Service Billing Portal

Customers can review invoice details, download invoice documents, and submit payments through the portal.

On the Home tab, click the invoice number to view the invoice details.
Review the invoice lines.
To download the invoice PDF document, click Download.
Click Pay.
Verify the billing information and invoice summary.
Select the payment method, and click Pay Now.
If your customers add a payment method, they can save it for future use and set it as their default.

When the payment is processed, a notification appears with the payment status. If the payment is successful, the invoice is marked as settled. If any invoice is locked, your customers can contact your admin for help.

=== ARTICLE: ind.billing_self_service_portal_raise_service_requests.htm ===
---
article_id: ind.billing_self_service_portal_raise_service_requests.htm
title: Raise Billing Inquiries and Invoice-Related Disputes
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_self_service_portal_raise_service_requests.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_self_service_portal.htm
fetched_at: 2026-09-04
---

# Raise Billing Inquiries and Invoice-Related Disputes

The self-service Billing portal serves as the customer-facing gateway that transforms manual, phone-based dispute processes into a streamlined, transparent self-service experience. The Help Center tab provides a catalog of available billing service processes. The Cases tab shows all cases and their statuses for the customer account.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To access the Experience Cloud site created by using the Self-Service Billing Portal template:	
Billing Experience Cloud User permission set
UnifiedCatalogCommunityUserPsl permission set group
Unified Catalog Community User permission set
Omnistudio User permission set
On the Help Center tab, select a service process such as Extend Invoice Due Date or Suspend Billing, and then click Request.
For any general billing inquiries or disputes that don’t have predefined service process templates, use the Other Billing Inquiries/Disputes service process.
Fill in the required billing inquiry or dispute details, and submit the request.

A case is created for the request, a tracking number is assigned, and an automated email is sent to the customer’s email address. If the request pertains to an invoice charge correction, a corresponding dispute record is also created.

On the Cases tab, your customer can view and track the case and its status.

A case is created for the service process request, a tracking number is assigned, and an automated email is sent to the customer’s email address. If the request pertains to an invoice charge correction, a corresponding dispute record is also created.

Your billing specialist or customer service representative can then view, investigate, and resolve the submitted case.

You can also use Billing Service Assistance Agent on the self-service billing portal to get quick answers for your billing inquiries.

=== ARTICLE: ind.billing_send_l2_l3_data.htm ===
---
article_id: ind.billing_send_l2_l3_data.htm
title: Send Level 2 and Level 3 Payment Data Through Your Payment Gateways
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_send_l2_l3_data.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payments.htm
fetched_at: 2026-09-04
---

# Send Level 2 and Level 3 Payment Data Through Your Payment Gateways

Level 2 and Level 3 processing data are the additional line-item and transaction-level details passed during credit card authorization. Use Level 2 and Level 3 data mainly for business-to-business and business-to-government corporate card transactions to lower fraud risk and get richer reporting. When Level 2 and Level 3 data support is enabled, Billing automatically includes additional transaction data in payment requests that you send through native and third-party payment gateways.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To send Level 2 and Level 3 data:	

Payment Admin permission set

OR

Payment Operations User permission set

Billing sends Level 2 and Level 3 data automatically to native payment gateways, such as Stripe and Adyen. Billing populates the Level 2 and Level 3 fields from the invoice and invoice lines with a fixed mapping.

Quantity, unit price, and line amount are derived from the invoice line.
Ship-from postal code, that’s part of Level 2 data, is derived from the postal code of the invoice’s legal entity.

For third-party payment gateways, Billing sends Level 2 and Level 3 data through Apex adapter classes. You can customize the adapter classes to map additional fields to send data beyond the standard set. For more information, see the Apex Reference Guide.

Supported Level 2 and Level 3 Fields

In payment transactions, Level 1 data includes basic information such as transaction amount, currency ISO code, and merchant account name.

Level 2 data includes Level 1 data and this information.

LEVEL 2 FIELDS	DEFAULT VALUE
DiscountAmount	0
DutyAmount	0
ReferenceId	 
SalesTaxAmount	 
ShipFromZip	 
ShippingAmount	 
ShipToCountry	 
ShipToZip	 
TotalTaxAmount	0

Level 3 data includes Level 2 data and these detailed line items.

LEVEL 3 FIELDS	DEFAULT VALUE
CommodityCode	 
Description	 
Discount	0
DiscountIndicator	false
GrossNetIndicator	"N"
LineItemTotal	 
Quantity	 
Sku	 
TaxAmount	 
TaxRate	 
Uom (unit of measure)	 
UnitPrice	 
NOTE For Stripe, Billing includes Level 3 line data for invoices with up to 200 lines. For an invoice with more than 200 lines, the payment still processes, but Billing sends only Level 2 data and omits the Level 3 line data. Adyen has no such line limit.
Process a Payment That Includes Level 2 and Level 3 Data
Send a payment through a native or third-party payment gateways with enhanced data attached, and verify the Level 2 and Level 3 fields in the payment gateway logs.

=== ARTICLE: ind.billing_send_l2_l3_data_process.htm ===
---
article_id: ind.billing_send_l2_l3_data_process.htm
title: Process a Payment That Includes Level 2 and Level 3 Data
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_send_l2_l3_data_process.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_send_l2_l3_data.htm
fetched_at: 2026-09-04
---

# Process a Payment That Includes Level 2 and Level 3 Data

Send a payment through a native or third-party payment gateways with enhanced data attached, and verify the Level 2 and Level 3 fields in the payment gateway logs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To process payments and review payment gateway logs:	

Payment Admin permission set

OR

Payment Operations User permission set

Turn on Level 2 and Level 3 data support on the Billing Settings page, and confirm that you have a posted invoice with line-level detail. Each invoice line needs a product description, unit price, quantity, and line amount, because these fields form the Level 3 data that Billing sends to the gateway.

When you process a payment on a native gateway, Billing attaches Level 2 and Level 3 data automatically from the invoice and invoice lines.

Create a payment schedule for the invoice.
Create a payment schedule item, and link it to the saved payment method of your third-party or native payment gateway, such as Stripe or Adyen.
Set the payment schedule item status to Ready for Processing.
Run a payment batch run.
After the payment batch run completes, open the payment gateway logs and confirm that the payment transaction has succeeded.
The gateway log shows that Level 2 and Level 3 fields, such as quantity, unit price, and tax amount, have been passed to the payment gateway during the payment transaction.

=== ARTICLE: ind.billing_sequence_policies_manage.htm ===
---
article_id: ind.billing_sequence_policies_manage.htm
title: Configure Sequence Policies
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_sequence_policies_manage.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_sequential_numbering_for_invoices_configure.htm
fetched_at: 2026-09-04
---

# Configure Sequence Policies

Define the sequential number structure and the filters for choosing which invoice or credit memo records to number.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To configure sequence policies:	

Billing Admin permission set

OR

Billing Operations User permission set

To configure sequence policies, your Billing Admin must turn On Sequential Numbering.

From the App Launcher, find and select Sequence Policies.
Click New.
Enter a sequence policy name.
If necessary, enter a description.
Select the target object for which you’re creating the sequence policy.
Specify the sequence policy's effective date and time range.
To activate the sequence policy, select Active.

You can also create draft sequence policies and activate them later.

To generate and assign continuous sequential numbering to the target object records, select Enforce gapless sequence.
NOTE Select this option to ensure sequential numbers are gapless. Any skipped or unassigned numbers are stored in the Sequence Gap Reconciliations records and reassigned to - to the target object records to maintain continuity.
Set selection conditions to determine which sequence policy is applied to a target object record.
If you don't specify any selection conditions, all eligible posted - target object records are automatically assigned a number.
Enter the sequence start number from which the sequential numbering begins.
To determine the value by which the sequential number increases, specify an increment value.
To indicate the last sequence value in the series, enter a maximum sequence number.
If you need the date, month, year, or fiscal year information to be included in the invoice and the credit memo number, select the date stamp format.
To indicate the minimum desired number of digits for the sequence number, add a minimum sequence number width.
If the generated sequence number is shorter than this width, it’s prepended with zeros. For example, if the width is 5 and the generated sequence number is 123, the sequence value becomes 00123.
Construct your sequence pattern with static text, placeholders, and fields from the target object.

The sequence pattern combines static text, such as prefixes or separators, with dynamic values. {SequenceValue} is required. You can also include {Date} and fields from the selected target object, such as invoice or credit memo.

After you select a target object, use Insert Field to add standard, custom, or formula fields. Supported field types are text, number, date, and text area. Combine multiple fields with static text in one pattern. The complete pattern can be up to 255 characters.

The {Date} placeholder is replaced with a date in the date stamp format defined in the sequence policy. Supported formats are MM-DD-YYYY, MM-YYYY, YYYY-YY (Fiscal Year), and YYYY.

Save the changes.

Sequential numbering is applied to invoice or credit memo records when they are posted. When you set up sequence policies, make sure to define a unique policy that resolves for invoice or credit memo records that meet a specific set of conditions.

You can edit a sequence policy only when it’s in draft status. After activation, you can't edit the Increment Number, Sequence Pattern, and Target Object fields. You can also delete a deactivated sequence policy if it isn’t associated with any invoice and credit memo record.

=== ARTICLE: ind.billing_sequential_number_assignment_and_sequence_gap_reconciliation.htm ===
---
article_id: ind.billing_sequential_number_assignment_and_sequence_gap_reconciliation.htm
title: Sequential Invoice and Credit Memo Number Assignment
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_sequential_number_assignment_and_sequence_gap_reconciliation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_sequential_numbering_for_invoices_configure.htm
fetched_at: 2026-09-04
---

# Sequential Invoice and Credit Memo Number Assignment

When you post an invoice or a credit memo record, the system evaluates all active sequence policies. If the target object matches the selection conditions of a unique sequence policy, the system assigns the next available sequential number based on that sequence policy to the target object record.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Invoice and Credit Memo Number Assignment

Invoice and credit memo numbers are assigned based on how you create or post invoices and credit memos, or ingest invoices. These scenarios show when and how the invoice and credit memo numbers are applied.

Setup: If you turn on Mandate Sequence Policy for Posted Invoices, every invoice record must have an invoice number before you post. If an invoice number isn't assigned, the invoice moves to Error or Posting In Progress status. A Revenue Transaction Error Logs (RTEL) is logged for the Invoice record with the sequencing error details.
Setup: If you turn on Mandate Sequence Policy for Posted Credit Memos, every credit memo record must have a credit memo number before you post. If a credit memo number isn't assigned, the credit memo moves to Error status. A Revenue Transaction Error Logs (RTEL) is logged for the Credit Memo record with the sequencing error details.
Generate Invoices: When you generate posted invoices by using the Generate Invoices option on Account or Order record, or via the Invoice generation API invoice numbers are automatically assigned to the posted invoices.
Generate Credit Memo: When you generate a credit memo by using the Standalone Credit Memo API, the Void Credit Memo API, the Post a Draft Memo API, the Create and Apply Credit Memo API, or the Negative Invoice Lines to Credit Conversion API, a credit memo number is automatically assigned if the credit memo is posted and matches a unique active sequence policy.
Invoice Run: When you schedule an invoice run by using the Billing Batch Scheduler, invoice numbers are automatically assigned to all posted invoices.
Draft to Posted: When you post an invoice or a credit memo, an invoice or credit memo number is automatically assigned to it.
Preview Invoices: Invoice previews don't create actual Invoice records, so no invoice number is assigned to them.
Void a Posted Invoice: If you void a posted invoice with an invoice number, the number remains assigned to the voided invoice and can’t be reassigned to another invoice. The credit memo created to void the invoice isn't automatically assigned a credit memo number. This is because the credit memo transitions from a pending status to a voided status without ever being posted. To assign a sequential number to this credit memo, use the Sequence Assignment API.
Void a Posted Credit Memo: If you void a posted credit memo with a credit memo number, the number remains assigned to the voided credit memo and can't be reassigned to another credit memo. The credit memo generated as a result of the void operation isn't assigned a credit memo number, because it isn't posted through the standard posting flow.
Invoice Ingestion: For an ingested draft invoice, an invoice number is assigned during the posting process, provided the invoice aligns with a unique active sequence policy. When an already posted invoice is ingested, the Mandate Sequence Policy for Posted Invoices setting determines whether the invoice is accepted. If you enable this setting, a preexisting invoice number must be supplied in the Invoice Ingestion API payload, as the system won't generate one. If you disable this setting, even an ingested posted invoice without an invoice number is accepted.
NOTE An invoice number isn't assigned if:
Multiple active sequence policies match the same invoice record.
No active sequence policies match the invoice.
Sequence Gap Reconciliation

When you enforce gapless sequence in the sequence policy, the system creates a Sequence Gap Reconciliation record if any gaps are introduced in the sequence. Sequence gap reconciliation applies only to gapless sequences, where unassigned gaps in the sequence are reassigned to matching target object records so the sequence remains continuous.

Every 24 hours, a gap reconciliation scheduled job looks for any gaps in the active gapless sequence policies and stores any missing sequence values in the Sequence Gap Reconciliation record. If required, you can also trigger the Assign Sequences API manually to run the sequence gap reconciliation function.

Here are a few scenarios which could result in gaps:

Any error occurs during sequential number assignment.
An invoice with an invoice number associated with a sequence policy is deleted. Similarly, a credit memo with a credit memo number associated with a sequence policy is deleted.
NOTE If the invoice or the credit memo with the invoice or credit memo number is deleted, the corresponding record is in Blocked status, so that it isn't reassigned. The record is in Unassigned status if sequence number assignment fails for an invoice or a credit memo.

To see the details about these gaps, from the App Launcher, find and select Sequence Gap Reconciliation.

=== ARTICLE: ind.billing_sequential_numbering_apis.htm ===
---
article_id: ind.billing_sequential_numbering_apis.htm
title: Manage Sequential Numbering by Using APIs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_sequential_numbering_apis.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_sequential_numbering_for_invoices_configure.htm
fetched_at: 2026-09-04
---

# Manage Sequential Numbering by Using APIs

Use APIs to create and update sequence policies, assign sequence pattern values to records, and restore missing sequence values.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
GOAL	API
Create a sequence policy to configure a unique, sequential number for all posted invoices and credit memos.	Create a Sequence Policy API
Update the settings of a sequence policy that defines how unique, sequential numbers are generated by using specific patterns, values, and filters.	Update Sequence Policy API
Assign sequence pattern values to objects based on the configured sequence policy.	Sequence Assignment API
Restore a missing sequence value identified by using this API in gapless-enabled sequences. This sequence value can be used later in the subsequent sequence policy numbering, ensuring there are no gaps.	Sequence Gap Reconciliation API

=== ARTICLE: ind.billing_sequential_numbering_for_invoices_configure.htm ===
---
article_id: ind.billing_sequential_numbering_for_invoices_configure.htm
title: Configure Sequential Numbering for Invoices and Credit Memos
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_sequential_numbering_for_invoices_configure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Configure Sequential Numbering for Invoices and Credit Memos

Use a sequence policy to configure automated sequential numbering for your invoices and credit memos. Generate unique, gapless numbers to create fully traceable records for financial audits.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Gapless Sequential Numbering
For businesses that handle large volumes of transactions, assigning unique, gapless sequential numbers to invoice and credit memo records is essential for legal compliance, auditing, and reconciliation. Manual numbering introduces operational complexity and increases the risk of errors or fraudulent activity. Billing addresses this challenge by automating the assignment of unique identifiers according to the defined sequence policies.
Configure Sequence Policies
Define the sequential number structure and the filters for choosing which invoice or credit memo records to number.
Manage Sequential Numbering by Using APIs
Use APIs to create and update sequence policies, assign sequence pattern values to records, and restore missing sequence values.
Sequential Invoice and Credit Memo Number Assignment
When you post an invoice or a credit memo record, the system evaluates all active sequence policies. If the target object matches the selection conditions of a unique sequence policy, the system assigns the next available sequential number based on that sequence policy to the target object record.

=== ARTICLE: ind.billing_set_up_billing_service_assistance_agent_for_experience_cloud.htm ===
---
article_id: ind.billing_set_up_billing_service_assistance_agent_for_experience_cloud.htm
title: Set Up Billing Service Assistance Agent for Experience Cloud
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_set_up_billing_service_assistance_agent_for_experience_cloud.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_agentforce_for_billing_service_assistance_agent.htm
fetched_at: 2026-09-04
---

# Set Up Billing Service Assistance Agent for Experience Cloud

Configure service access, security, and data sharing so that external users can securely interact with Billing Service Assistance Agent through Embedded Messaging in an Experience Cloud site.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management with the Revenue Cloud Advanced license and the Revenue Cloud Billing license with the Agentforce Employee Agent add-on.
USER PERMISSIONS NEEDED
To create an agent:	

Manage AI Agents

OR

Customize Application

Before you begin, make sure you've completed these tasks.

Create an Experience Cloud site by using the Self-Service Billing Portal template
Set Up Community and Partner Access for Agentforce in Revenue Management

These settings establish the trust boundaries that securely loads messages, scripts, and billing data while maintaining controlled access for community users.

After you complete this setup, customers can view billing information and engage with agents in a single Experience Cloud site, reducing support handoffs and administrative overhead.

Enable Service Cloud Admin User Access
In Setup, find and select Users.
Open the admin user record.
Click Edit.
Select Service Cloud User.
Click Save.
If the Service Cloud User option isn’t available:
Update the user’s licenses to include Service Cloud access.
Save your changes.
Reopen the user record and select Service Cloud User.
Update the Embedded Messaging Deployment
Set business hours in enhanced chat to default.
Click Install Code Snippet.
From the Chat Code Snippet, copy the scrt2URL.
Add the SCRT URL as a CSP Trusted Site
In Setup, find and select Trusted URLs.
Click New Trusted URL.
Complete these fields:
OPTION	VALUE
API Name	Embedded_Messaging_SCRT
Trusted Site URL	Paste the SCRT URL you copied earlier
Active	Select
CSP Context	All
Under CSP Directives, select:
connect-src (scripts)
frame-src (iframe content)
Save your changes.
Configure Security and Trusted URLs for the Site
Open your Experience Cloud site in Experience Builder.
Click Settings, and then select Security & Privacy.
Under Trusted Sites for Scripts, click Add Trusted Site.
Add the SCRT script entry:
OPTION	VALUE
Name	SCRT
URL	SCRT URL from the Embedded Messaging JavaScript snippet
Click Add Site.
Click Add Trusted Site again and add the Bootstrap script entry:
OPTION	VALUE
Name	Bootstrap
URL	<site-domain>/assets/js/bootstrap.min.js
Click Add Site.
Configure CORS and Trusted URLs
Configure Salesforce CORS Allowlist.
Add the same domains listed in the CORS configuration to trusted URLs.
Grant Community Users Access to Billing Data
Create a sharing set with read-only access for these objects.
Invoice
Billing Schedule Group
Billing Milestone Plan
Liable Summary
In Setup, find and select Sharing Settings.
Click Edit.
Locate Unit of Measure.
Set the default external acess to Public Read Only.
Save your changes.

=== ARTICLE: ind.billing_set_up_context_definition.htm ===
---
article_id: ind.billing_set_up_context_definition.htm
title: Select Context Definition and Mapping for Create Billing Schedules for Orders API
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_set_up_context_definition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_configure_context_definitions.htm
fetched_at: 2026-09-04
---

# Select Context Definition and Mapping for Create Billing Schedules for Orders API

The Create Billing Schedules for Orders API uses Context Service to hydrate the data of orders to create billing schedules. Before using this API, select a context definition and its mapping that you want the API to use.

REQUIRED EDITIONS
USER PERMISSIONS
NEEDED
To select a context definition and its mappings:	Billing Admin permission set
In Setup, find and select Billing Settings.
In the Context Service Mapping section, select the extended BillingContext context definition as the context definition.
Select OrderEntitiesMapping or a similar source mapping context map that you have added.
Make sure to select only a source context mapping that maps orders to billing transaction context nodes.
Optionally, add a custom intracontext mapping and select the mapping to map custom Order fields to the billing transaction nodes, or to override the existing mapping of standard fields.
You can pass preferred order details to billing schedules by configuring the custom mapping by using Context Service.
SEE ALSO
Turn On Context Service
Revenue Cloud Developer Guide: Create Billing Schedules for Orders API
Revenue Cloud Developer Guide: Create Standalone Billing Schedules API

=== ARTICLE: ind.billing_settlements_central.htm ===
---
article_id: ind.billing_settlements_central.htm
title: Billing Settlements Central
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_settlements_central.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Billing Settlements Central

Access invoices, payments, credit memos, and debit memos with ease from a single console. Perform settlements and adjustments, track balances, and act from a single console. Reduce navigation, gain visibility into outstanding balances, and support efficient billing through in-context actions and customizable views.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
NOTE Starting Summer ’26, the Billing Settlements Central dashboard is included by default. For Salesforce orgs created in or upgraded to Summer ’26, your Billing admin must add the dashboard to the Billing app through the App Manager in Setup. Then, refresh the session by logging out and logging back in to the Salesforce org.

From the App Launcher, find and select Billing. From the navigation bar, click Home.

Billing Transaction Details and Summary

Access real‑time summaries of open invoices, credit memos, debit memos, and payments with high‑level visibility into outstanding balances.

Refine and personalize how the dashboard shows data by using these options.

Currency filter: In multi-currency orgs, apply a currency ISO code to focus on transactions in a specific currency.
Account filter: Filter at the account level to narrow down data across all dashboard components.
Settlements and Adjustments

Get summary and detailed insights into your billing transactions. The Settlements and Adjustments section shows transactions by using the list views that you’ve created. The dashboard automatically reflects any new list view that you create for a record. You can review and act on individual records from the list. Use this section to:

Review detailed lists of billing transactions.
Apply filters to refine your data view.
See an overview of all billing transaction details and act accordingly.
Manage billing settlements and related adjustments efficiently.
Navigate across invoices, payments, credit memos, and debit memos on a single page.
Quick Actions

Perform billing tasks with visibility into all billing transactions, and save time by reducing visits to individual record pages. You can settle invoices and apply payments, create credit memos, or create debit memos all from Billing Settlements Central.

NOTE To perform the quick actions, you need certain permission sets.

To customize the Billing Settlements Central page layout, contact your Billing Admin. The admin can add, remove, or rearrange components to fit your team’s workflow. After making changes, log out and log back in to refresh your session and apply the updates.

=== ARTICLE: ind.billing_setup.htm ===
---
article_id: ind.billing_setup.htm
title: Set Up Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Set Up Billing

Enable Billing, assign the required permission sets, and set up features.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Turn On Billing in Revenue Management
Enable Billing to start using Billing features.
Guided Setup for Billing
Admins can use the Billing Guided Setup for a ‌step-by-step guidance to complete key tasks that are required to set up Billing.
Assign Permissions to Access Billing Features
Assign your users the required permission sets based on their persona, and for the APIs for which they need access.
Select Default Billing Treatment, Tax Treatment, and Legal Entity
If there's no billing policy specified for order products, the default billing treatment defines how those order products are billed. The default tax treatment is used with all order products unless overriden on specific order products or tax policies. The default legal entity is used with quotes and orders to calculate taxes unless overriden for specific quotes and orders.
Configure Context Definitions for Billing
Context definitions in Billing act as a central data-mapping layer that helps information flow seamlessly from orders or external transactions into billing schedules. They transform data from Salesforce objects into a standardized format that enable the Billing APIs to read the details required to create accurate billing records. By configuring these context definitions, businesses can automate the transfer of custom field data.
Add New Billing Fields to Page Layouts
Provide users more context by adding new fields to the default page layouts each release.

=== ARTICLE: ind.billing_setup_additional_features.htm ===
---
article_id: ind.billing_setup_additional_features.htm
title: Set Up Additional Billing Features
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_additional_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Set Up Additional Billing Features

Beyond the core functionality, you can set up and configure various additional Billing features to extend its capabilities. This allows you to tailor Billing to your specific business requirements.

Set Up Milestone Plans for Amendments
Create or link billing milestone plans to amendment billing schedules and recalculate milestone dates and amounts from the amendment start date.
Set Up Financial Accounting Features
Make sure that every billing transaction is compliant with double-entry accounting principles by automatically generating dual transaction journals, each containing both a credit and a debit entry to maintain balanced records. Select a default Data Processing Engine definition that's run to close legal entity accounting periods when your Billing operations user initiates their closure. Set up Billing to show transaction amounts in both the transactional currency and your corporate currency.
Turn On Invoice PDF Document Generation and Account Statement
Before Billing can create PDF documents for invoices, invoice previews, and account statements, enable server-side and batch document generation, then turn on Document Generation in Billing Settings. Batch document generation is required to generate invoice PDF documents from an invoice batch run.
Turn On Email Delivery of Invoices
Send emails with invoice information along with invoice PDF documents to your customers.
Turn On Sequential Numbering Features
Apply unique, gapless sequence numbers to transaction records to ensure financial compliance and a clear audit trail. You can also mandate assigning an invoice number to every posted invoice.
Set Up Credit Memo Features
Set up Billing to automatically create credit memos from negative invoice lines and apply them to settle outstanding invoice balances, and to configure whether credits apply to invoices or invoice lines.
Set Up Invoice Risk Scoring to Predict Risk Scores for Invoices (Pilot)
A risk score for an invoice predicts the likelihood that payment for an open invoice is delayed beyond its due date. The score estimates the probability of late payment based on patterns and signals such as historical payment behavior, invoice aging, outstanding balances, customer payment trends, dispute history, and other relevant account characteristics.
Set Up Payment Features for Revenue Management
Set up Payments to streamline the management of the entire payment lifecycle. By establishing a secure connection with native and third-party payment providers, you can directly process payments for customer transactions within your Salesforce environment.
Define Rules and Order to Apply Credit Memo and Payments
Define the rules and the order in which credit memos and payments are applied to settle the balances of posted invoices or invoice lines within the same account.
Self-Service Billing Portal
The self-service billing portal is a customer-facing Experience Cloud site that enables end users and community users to raise and track their billing inquiries and disputes. Your customers can view and download invoice PDF documents and quickly pay the outstanding balances of invoices by using supported payment methods. The self-service portal minimizes manual intervention and improves cash flow and customer satisfaction.

=== ARTICLE: ind.billing_setup_apply_credits_to_posted_invoices.htm ===
---
article_id: ind.billing_setup_apply_credits_to_posted_invoices.htm
title: Automatic Application of Credits to Settle Invoice Balances
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_apply_credits_to_posted_invoices.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# Automatic Application of Credits to Settle Invoice Balances

Eliminate the need to manually apply credit memos by automatically applying available credit memo balances to settle the balances of posted invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Process Overview

When your Billing admin enables the Apply Credits to Posted Invoices feature, the system automatically applies the balances of credit memo to settle the balances of posted invoices based on the credit application level.

The automatic credit application process runs immediately after invoices are posted by using one of these methods:

After a scheduled invoice run completes.
Using Post Draft Invoices in Batch API.
After running the Post Draft Invoice Batch Run action.
Visualizing the Process

This flowchart shows the step where credit application happens in the business process flow.

=== ARTICLE: ind.billing_setup_billing_arrangements.htm ===
---
article_id: ind.billing_setup_billing_arrangements.htm
title: Configure Billing Arrangements for Billing Schedule Groups
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_billing_arrangements.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_billing_arrangements.htm
fetched_at: 2026-09-04
---

# Configure Billing Arrangements for Billing Schedule Groups

Route invoices with the appropriate allocated charges to the correct billing accounts by configuring billing arrangements on billing schedule groups.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To configure billing arrangements:	

Billing Admin permission set

OR

Billing Operations User permission set

Enable field-level security on the PaymentTerm and BillToContact fields of the Billing Account object.

Go to the Billing Schedule Group record.
In the Billing Arrangements tab, click Manage Billing Arrangements.
Enter a name for the billing arrangement.
Click Add Account to add a new billing arrangement line.
Select a billing account.
Optionally, select Remainder to indicate whether to bill the remainder percentage to the billing account.
Repeat steps 4 and 5 to add up to five billing arrangement lines.
Optionally, select Bill Remainder to Owning Account to allocate any remainder percentage to the owning account.
Any percentage of the billing amount that isn’t assigned to any of the billing accounts is displayed as remainder billing percentage.
Save your changes.
NOTE If the remainder percentage isn’t allocated to the owning account or any of the billing accounts, then the same is automatically allocated to the first billing account in the billing arrangement.

=== ARTICLE: ind.billing_setup_clone_order_to_schedule_flow.htm ===
---
article_id: ind.billing_setup_clone_order_to_schedule_flow.htm
title: Use Order to Billing Schedule Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_clone_order_to_schedule_flow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_from_orders.htm
fetched_at: 2026-09-04
---

# Use Order to Billing Schedule Flow

Use the Order to Billing Schedule flow to automatically generate billing schedules and billing schedule groups from order items as soon as orders are activated.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management
The Order To Billing Schedule flow template and Create Billing Schedules for Orders API are available with the Revenue Management Advanced license or the Agentforce Revenue Management Billing license.

Save a version of the out-of-the-box Order to Billing Schedule flow and activate it. When you clone the flow, we recommend that you include Custom in the name to distinguish it from out-of-the-box flows.

When an order is activated, two flows—Order to Asset and Order to Billing Schedule—are triggered. The Order to Billing Schedule flow then generates a billing schedule group and a billing schedule for the order.

NOTE As a best practice, we recommend that you use only one active flow to generate billing schedules. If there are multiple active flows, duplicate billing schedules get generated for the same order.

=== ARTICLE: ind.billing_setup_credit_memo_features_enable.htm ===
---
article_id: ind.billing_setup_credit_memo_features_enable.htm
title: Set Up Credit Memo Features
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_credit_memo_features_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Set Up Credit Memo Features

Set up Billing to automatically create credit memos from negative invoice lines and apply them to settle outstanding invoice balances, and to configure whether credits apply to invoices or invoice lines.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To enable Billing features:	Billing Admin permission set
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
To automatically convert all negative invoice lines to credit memo and credit memo lines after the related invoices are posted, turn on Conversion of Negative Invoice Lines to Credit Memo and Credit Memo Lines.
To automatically apply all converted credit memo and credit memo lines to the related invoice and invoice lines, turn on Application of Converted Credit Memo and Credit Memo Lines to Header Level and Line Level.
Select the credit application level. If your Salesforce org has the Revenue Management Billing license, the label of this setting is Credit, Refunds and Payment Application Level.
To apply credits to a specific line on invoices, select Line Level.

To apply credits to the total rolled-up balance of invoices, select Header Level.

To automatically apply available credit memo balances to posted invoices, turn on Apply Credits to Posted Invoices.
Select the default flow used to apply the credit memo to invoices.
Select the credit memo and payment application rules.
See Define Rules and Order to Apply Credit Memo and Payments.

After you set up credit memo features, your Credit Memo Operations users can manage credit memos.

SEE ALSO
Automatic Conversion of Negative Invoice Lines into Credit Memo Lines
Automatic Application of Credits to Settle Invoice Balances
Results of Credit Memo Application

=== ARTICLE: ind.billing_setup_credit_memos_payments_application_rules.htm ===
---
article_id: ind.billing_setup_credit_memos_payments_application_rules.htm
title: Define Rules and Order to Apply Credit Memo and Payments
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_credit_memos_payments_application_rules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Define Rules and Order to Apply Credit Memo and Payments

Define the rules and the order in which credit memos and payments are applied to settle the balances of posted invoices or invoice lines within the same account.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To enable Billing features:	Billing Admin permission set
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
Select the order in which credit memos and payments are applied.
The default selection is Payments First, which applies payments to the posted invoices before credits.
Select these predefined rules in the sequence in which you want to run them.
To apply credit memos or payments only if an invoice is specified on the Reference Entity field of the Credit Memo record or on the Invoice field within the Payment record's payment initiation source, select Match ID. Select this rule only if the invoice is referenced on the Credit Memo or Payment records.
To apply credit memos and payments to invoices that have the same balance, select Match Balance.
To apply credit memos or payments to the invoice with the oldest posted date, select Prioritize Oldest Invoices.
To apply credit memos or payments to the invoice with the highest current outstanding balance, select Prioritize Highest Balance Invoices. When the credit and payment application level is Invoice Line, Billing uses the selected rules to match the invoice. It then applies the credit memo line or payment with highest balance to the invoice line with highest balance on that invoice.
NOTE When there are more than 2000 invoices to be processed, Billing applies only the first rule selected for credit and payment application.
Turn on Rule-Based Credit and Payment Application.
You can enable this feature only if you select the application order and rules.
NOTE When both Rule-Based Credit and Payment Application and Apply Credits to Posted Invoices features are turned on, Rule-Based Credit and Payment Application takes precedence.

The balance of credit memos and payments are applied to settle the balances of posted invoices based on these rules and the credit, refunds, and payment application level when your users perform one of these tasks.

Schedule an invoice batch run
Generate invoices for accounts or orders
Use Post Draft Invoices in Batch API
Run the Post Draft Invoice Batch Run action

To apply rule-based credit and payment application on existing invoices of an account, use Rules Application API.

Invalid Match ID During Payment Application
When a payment is applied using the Match ID rule, the invoice ID specified on the payment record is validated. If the referenced invoice is deemed invalid, the payment is applied to the next available invoice based on the subsequent rule in the sequence.
Example: Apply Rule-Based Credits and Payments
Explore an example to understand the setup of rule-based credits and payments in your Salesforce org, and how credit memos and payments are applied to posted invoices of the same account.

=== ARTICLE: ind.billing_setup_default_records.htm ===
---
article_id: ind.billing_setup_default_records.htm
title: Select Default Billing Treatment, Tax Treatment, and Legal Entity
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_default_records.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup.htm
fetched_at: 2026-09-04
---

# Select Default Billing Treatment, Tax Treatment, and Legal Entity

If there's no billing policy specified for order products, the default billing treatment defines how those order products are billed. The default tax treatment is used with all order products unless overriden on specific order products or tax policies. The default legal entity is used with quotes and orders to calculate taxes unless overriden for specific quotes and orders.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To select default records:	Billing Admin permission set

Before you select the default records that'll be used for your Salesforce org, make sure that you complete these prerequisite steps:

Before you select a default billing treatment and a default legal entity, your billing operations user must create the required billing records and the required Legal Entity records.
Before you select a default tax treatment, your tax admin must create the required tax records.
From Setup, find and select Billing Settings.
Go to the Billing Defaults section, and select the default billing treatment, tax treatment, and legal entity.

Your changes are saved as soon as you select the default records.

=== ARTICLE: ind.billing_setup_document_generation.htm ===
---
article_id: ind.billing_setup_document_generation.htm
title: Turn On Invoice PDF Document Generation and Account Statement
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_document_generation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Turn On Invoice PDF Document Generation and Account Statement

Before Billing can create PDF documents for invoices, invoice previews, and account statements, enable server-side and batch document generation, then turn on Document Generation in Billing Settings. Batch document generation is required to generate invoice PDF documents from an invoice batch run.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS
NEEDED
To enable Billing features:	Billing Admin permission set
To enable Document Generation Settings and to create, view, or edit document templates:	DocGen Designer permission set

Before turning on Document Generation for Billing, turn on Design Document Templates.

Document Generation creates PDF documents for invoices, invoice previews, and account statements. Complete this task in Document Generation Settings and then in Billing Settings.

From Setup, in the Quick Find box, enter document generation, and then select Document Generation Settings.
Click the arrow corresponding to the document generation setting, and then select Edit.
If your org doesn’t have a Document Generation Setting record, create one. See Enable Server-Side Document Generation Setting for the Omnistudio Package. Then edit the record and continue with these steps to turn on Enable Batch Document Generation.
Turn on Enable Server-Side Document Generation and Enable Batch Document Generation.
Enable Batch Document Generation is required to generate invoice PDF documents from an invoice batch run.
Click Continue.
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
Turn on Document Generation.

The Default Invoice Template and Default Invoice Preview Template document templates are preselected as the default templates for generating invoice PDF documents and invoice preview PDF documents.

After you turn on document generation, you or your Billing Operations users can generate invoice PDF documents and account statements.

You can clone and customize the Default Invoice Template, Default Invoice Preview Template, or Sample Invoice Template document templates, or create your own document templates, and then select the custom document templates as the default ones.

IMPORTANT

When your Salesforce org upgrades to Summer ’25 or a later release, to view the preselected Default Invoice Preview Template document template, your Billing admin must complete the one-time task of turning off Document Generation for Billing and turning it on again.

SEE ALSO
Enable Design Document Templates in Salesforce Setting
Enable Server-Side Document Generation Setting for the Omnistudio Package
Enable Document Generation Batch Process
Generate a Batch of Invoice PDF Documents
Default Document Template to Generate Invoice PDF Documents
Default Document Template to Generate Invoice Preview PDF Documents
Clone a Document Template
Create a Microsoft Word or Microsoft PowerPoint Template for Omnistudio Document Generation

=== ARTICLE: ind.billing_setup_email_delivery.htm ===
---
article_id: ind.billing_setup_email_delivery.htm
title: Turn On Email Delivery of Invoices
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_email_delivery.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Turn On Email Delivery of Invoices

Send emails with invoice information along with invoice PDF documents to your customers.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To enable Billing features:	Billing Admin permission set
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
Turn on Configure Email Delivery Settings.

The Default Invoice Email Template email template is preselected as the default template for generating the email body.

IMPORTANT

For Salesforce orgs that are created in Winter ’26, after your Billing Admin enables Configure Email Delivery Settings, Default Invoice Email Template is preselected as the default email template.

For Salesforce orgs that are created before Winter ’26 and have Configure Email Delivery Settings already enabled, to view the preselected Default Invoice Email Template email template, your Billing admin must complete the one-time task of turning off Configure Email Delivery Settings and turning it on again.

After your billing admin turns on the configure email delivery settings feature, your billing admin or billing operations users can define invoice email delivery configuration and preferences and email invoice information along with invoice PDF documents to your customers.

SEE ALSO
Send Invoices Through Email

=== ARTICLE: ind.billing_setup_enable.htm ===
---
article_id: ind.billing_setup_enable.htm
title: Turn On Billing in Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup.htm
fetched_at: 2026-09-04
---

# Turn On Billing in Revenue Management

Enable Billing to start using Billing features.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To turn on Billing:	System Administrator profile with the Customize Application user permission
IMPORTANT You can’t turn on Billing when Subscription Management is enabled in your org.
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
Turn on Billing.

To avoid facing access issues after turning on Billing and before setting up Billing features, assign the Billing Admin and Billing Operations User permission sets to users with the System Administrator profile.

NOTE

After turning on Billing, order activation succeeds only if the Order records have values for the Bill to Contact, Billing Address, and Shipping Address fields. Order activation fails if any of these values are missing.

SEE ALSO
Knowledge Article: Disable Subscription Management to use Billing in Revenue Cloud
Select Context Definition and Mapping for Create Billing Schedules for Orders API
Select Default Billing Treatment, Tax Treatment, and Legal Entity
Set Up Financial Accounting Features

=== ARTICLE: ind.billing_setup_financial_accounting_features.htm ===
---
article_id: ind.billing_setup_financial_accounting_features.htm
title: Set Up Financial Accounting Features
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_financial_accounting_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Set Up Financial Accounting Features

Make sure that every billing transaction is compliant with double-entry accounting principles by automatically generating dual transaction journals, each containing both a credit and a debit entry to maintain balanced records. Select a default Data Processing Engine definition that's run to close legal entity accounting periods when your Billing operations user initiates their closure. Set up Billing to show transaction amounts in both the transactional currency and your corporate currency.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


The Store Transaction Amounts in Corporate Currency and Legal Entity Accounting Periods features are available:

For the Invoice and Credit Memo records, and their related records with the Revenue Management Advanced license or the Revenue Management Billing license.
For the Payment, Refund, and Debit Memos records, and their related records only with the Revenue Management Billing license. Contact your Salesforce account executive for more information.

The Create Transaction Journals for Transactions feature and Create Transaction Journals for Foreign Exchange Gains or Losses feature are available with the Revenue Management Billing license. Contact your Salesforce account executive for more information.

USER PERMISSIONS
NEEDED
To enable and configure financial accounting features:	Billing Admin permission set

From Setup, in the Quick Find box, enter Billing, and then select Billing Settings. Follow these steps to configure the required financial accounting features based on your business needs.

Create Transaction Journals

To automatically create Transaction Journal records for your transactions, turn on Create Transaction Journals for Transactions.

After turning on Create Transaction Journals for Transactions, make sure that your Accounts Receivables admin creates general ledger accounts and general ledger account assignment rules, and defines the criteria for billing transactions.

Create Foreign Exchange Gain and Loss Transaction Journals

To automatically create foreign exchange gain and loss transaction journals for your billing transactions, turn on Create Transaction Journals for Foreign Exchange Gains or Losses.

To use this feature, consider these key requirements.

The Create Transaction Journals for Foreign Exchange Gains or Losses toggle appears only when Create Transaction Journals for Transactions is turned on.
This feature is applicable only when advanced currency management is enabled and dated conversion rates are set in your Salesforce org.
Use only these general ledger accounts to create realized and unrealized gains and losses transaction journals. Don't set up general ledger account assignment rules for these accounts:
Select the unrealized gain and unrealized loss general ledger accounts.
Select the realized gain and realized loss general ledger accounts.
Select the account receivable general ledger account.

See Foreign Exchange Realized Gains and Losses.

Select Default Data Processing Engine Definition to Close Legal Entity Accounting Periods

In the Billing Defaults section, select a default Data Processing Engine (DPE) definition to close legal entity accounting periods.

Use the Close Legal Entity Accounting Period Data Processing Engine definition, or clone and customize it to suit your requirements.

If you don't select a default DPE definition, the system automatically selects either the Close Legal Entity Accounting Period DPE definition or the Close Legal Entity Accounting Period (Advanced) DPE definition based on your license.

See Close Legal Entity Accounting Periods and Data Processing Engine.

View Transaction Amounts in Corporate and Functional Currencies

To view transaction amounts in corporate and functional currency, turn on Store Transaction Amounts in Corporate and Functional Currencies.

This feature is applicable only when multiple currencies is enabled for your Salesforce organization.

See Close Legal Entity Accounting Periods.

After you set up financial accounting features, your Accounts Receivables admins can manage financial accounting.

=== ARTICLE: ind.billing_setup_header_tax_enable.htm ===
---
article_id: ind.billing_setup_header_tax_enable.htm
title: Capture Taxes at Header Level
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_header_tax_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_additional_configuration.htm
fetched_at: 2026-09-04
---

# Capture Taxes at Header Level

Use a single consolidated tax amount at the invoice header level for invoices and credit memos.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To enable capture taxes at header:	Billing Admin permission set
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
To capture taxes at the header level of the invoices, select Header Level as the Credit, Payment, and Refund Application Level.

The Capture Taxes At Header checkbox appears on a tax engine only when this setting is Header Level. Tax admins can select that option when they configure the tax engines. See Create a Tax Engine, Create a Tax Engine Provider and Tax Engine, and Tax Totals at the Line and Header Levels.

=== ARTICLE: ind.billing_setup_milestone_plans_amendments.htm ===
---
article_id: ind.billing_setup_milestone_plans_amendments.htm
title: Set Up Milestone Plans for Amendments
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_milestone_plans_amendments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Set Up Milestone Plans for Amendments

Create or link billing milestone plans to amendment billing schedules and recalculate milestone dates and amounts from the amendment start date.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To enable milestone plans for amendments:	Billing Admin permission set
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
Turn on Support Milestone Plans for Amended Billing Schedules.

After you enable this setting, Billing creates or links a billing milestone plan to the amendment billing schedule and recalculates milestone dates and amounts from the amendment start date. For more information about how milestone plans behave during amendments, renewals, and cancellations, see Milestone Billing for Amended, Renewed, and Canceled Assets.

=== ARTICLE: ind.billing_setup_negative_invoice_lines_conversion_to_credit_memo_lines.htm ===
---
article_id: ind.billing_setup_negative_invoice_lines_conversion_to_credit_memo_lines.htm
title: Automatic Conversion of Negative Invoice Lines into Credit Memo Lines
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_negative_invoice_lines_conversion_to_credit_memo_lines.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_credit_memos.htm
fetched_at: 2026-09-04
---

# Automatic Conversion of Negative Invoice Lines into Credit Memo Lines

In certain billing scenarios, an invoice line can be generated with a negative charge amount. This typically occurs when you amend an order to decrease the quantity of a product and generate an invoice for the amended product, or generate an invoice for an order product that has a negative price. Automate conversion of large volumes of such negative invoice lines to credit memo lines, and the application of these credit memo lines to invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Process Overview

When your Billing admin enables the Convert Negative Invoice Lines to Credit Memo Lines feature, the system automatically converts negative invoice lines into credit memo lines. The converted credit memos are then applied to the posted invoice which had the negative lines.

Conditions for Conversion

Negative invoice lines are automatically converted to credit memo lines when these conditions are met:

The negative invoice lines are for posted invoices.
The negative invoice lines haven't been previously converted to credit memos.
Converted Amount Details

The converted amount for each invoice line is stored in its Converted Negative Amount field, and the total converted amount for the invoice is stored in its Total Converted Negative Amount field.

Application of Converted Credit Memos to Invoices

After negative lines of an invoice are converted, if a balance remains on that invoice, the converted credit memos are applied to it. The credit amount applied will be the smaller of the invoice's balance or the credit memo's balance.

If the credit memo's balance is larger than the invoice's balance, the credit memo will fully settle the invoice. Any remaining balance on the credit memo must then be manually applied to other invoices.

Business Use Case: Converting Negative Invoice Lines when a Product's Quantity is Reduced

You amend a customer's order to reduce the quantity of their SaaS subscriptions from 4 to 3. This reduction creates an amended order product with a price of -$100.

The next time you generate an invoice for this order, an invoice line is created with an amount of -$100.
If Convert Negative Invoice Lines to Credit Memo Lines is turned on, this negative invoice line is automatically converted into a credit memo line within a new, posted credit memo.
The new credit memo line has a line amount of $100.
This credit memo's balance of $100 is applied to the original invoice, reducing its balance from $400 to $300.

=== ARTICLE: ind.billing_setup_payment_retry_rules.htm ===
---
article_id: ind.billing_setup_payment_retry_rules.htm
title: Set Up Payment Retry Rules
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_payment_retry_rules.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_retry_failed_payments.htm
fetched_at: 2026-09-04
---

# Set Up Payment Retry Rules

Define payment retry rule sets and payment retry rules and configure Billing to automatically retry failed payments for specific error categories at various time intervals.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To retry failed payments:	Billing Admin permission set
Create Payment Retry Rule Sets

Payment retry rule sets specify how the failed payments must be retried based on the error codes across various retry categories. A payment retry rule set contains one or more payment retry rules. All payment rules in a payment retry rule set inherit the values of retry interval type, interval unit, and interval values, by default. You can, however, override the default values by specifying the same in the payment retry rule.

Make sure to add the Default Rule Set and Use Alternate Payment Method checkbox fields to the Payment Retry Rule Set page layout.

From the App Launcher, find and select Payment Retry Rule Sets.
Click New.
Enter a name for the payment retry rule set.
Select a retry interval type—Fixed or Staggered.
Select an interval unit—Hours, Minutes, or Days.
If you selected the fixed interval type, enter a positive number less than or equal to 10 for the maximum number of retry attempts.
Enter one or more positive numbers for the interval value to indicate the time intervals after which the payment batch run must retry the failed payments.
If you selected the fixed interval type, enter a positive number less than or equal to 60. If you selected a staggered retry interval type, enter one or more positive numbers less than or equal to 60, separated by commas. Make sure that there are no whitespaces before or after the comma.
Select Draft or Active as the status.
If necessary, enter a description.
To set the payment retry rule set as default for your Salesforce org, select Default Rule Set.
You can add only one active default payment retry rule set at a time. If you set any other payment retry rule set as default, the earlier one is automatically removed as the default rule set.
To use an alternate payment method on the last retry of the failed payment, select Use Alternate Payment Method.
Save your changes.
EXAMPLE

To retry failed payments three times every six hours, select the interval type as Fixed and the interval unit as Hours. Then, enter the interval value as 6 and the retry count as 3.

To retry failed payments four times, every first, fifth, tenth, and fifteenth day, select the interval type as Staggered and the interval unit as Days. Then, enter the interval values as 1,5,10,15.

After you create a payment retry rule set, create one or more payment retry rules.

IMPORTANT To automatically retry failed payments, add at least one default payment retry rule set and then turn on Retry Failed Payments on the Billing Settings page.
Create Payment Retry Rules

Payment retry rules define actionable parameters such as the maximum number of retries for the failed records and time intervals between subsequent retry attempts. Create payment retry rules specific to payment gateways and payment gateway error categories. All payment retry rules in a payment retry rule set inherit the default values for interval type, interval time, interval unit, and maximum retry count provided in the rule set. You can, however, override the default values of the payment retry rule set by specifying the values in the payment retry rule.

From the App Launcher, find and select Payment Retry Rules.
Click New.
Enter a name for the payment retry rule set.
Select a payment retry rule set.
Optionally, select a payment gateway.
Select a payment gateway error category.
For information about available error categories, see Payment Gateway Error Categories.
Optionally, enter a payment gateway error code.
Select a retry interval type.
Select an interval unit—Hours, Minutes, or Days.
If you selected the fixed interval type, enter a positive number less than or equal to 10 for the maximum number of retry attempts.
Enter one or more positive numbers for the interval value to indicate the time intervals after which the payment batch run must retry the failed payments.
If you selected the fixed interval type, enter a positive number less than or equal to 60. If you selected a staggered retry interval type, enter one or more positive numbers less than or equal to 60, separated by commas. Make sure that there are no whitespaces before or after the comma.
Save your changes.

Alternatively, if you already have an existing payment retry rule set, create a new payment retry rule by clicking New on the Related tab of the payment retry rule set. The configuration steps are the same.

=== ARTICLE: ind.billing_setup_payment_retry_rules_examples.htm ===
---
article_id: ind.billing_setup_payment_retry_rules_examples.htm
title: "Examples: Configure Payment Retry Rule Sets and Retry Rules"
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_payment_retry_rules_examples.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_retry_failed_payments.htm
fetched_at: 2026-09-04
---

# Examples: Configure Payment Retry Rule Sets and Retry Rules

Let’s explore a few examples for creating and configuring payment retry rule sets and rules.

Create Org Default Payment Retry Rule Sets

Let’s say the Payments Admin at Acme Corp wants to create an org wide payment retry rule that retries all failed payments at regular intervals of six hours for a maximum of three attempts. To do this, the admin creates a new payment retry rule set with these details.

Name: Acme_Payment_Retry_Ruleset_Default
Description: Acme’s Org Default Retry Rule Set
Status: Active
Default Rule Set: Yes
Default Retry Interval Type: Fixed
Default Maximum Retry Count: 3
Default Interval Unit: Hours
Default Interval Value: 6
Create Payment Retry Rules that Inherit Default Values of the Payment Retry Rule Set

Let’s say the Payment admin at SmartBytes wants to create a payment retry rule set with two payment retry rules for two different gateway error categories for the Stripe payment gateway. The payment retry rules inherit the same interval unit, type, and value as the payment retry rule set.

Let’s first create a payment retry rule set with these details and include the default values for retry interval type, interval unit, and interval value.

Name: SmartBytes_Payment_Retry_Ruleset
Description: SmartBytes’ payment retry rule set that retries failed payments after the first, third, and fifth days.
Status: Active
Default Retry Interval Type: Staggered
Default Interval Unit: Days
Default Interval Value: 1,3,5

Let’s now create the first payment retry rule for the Stripe payment gateway for an error category such as “Card Limit Decline”. To do this, click New on the Related tab of “SmartBytes_Payment_Retry_Ruleset” rule set. Enter these details for the payment gateway, error category, and error code, and save your changes.

Payment Gateway: Stripe3P
Payment Gateway Error Category: Card Limit Decline
Payment Gateway Error Code: expired_card

When saved, the new payment retry rule (“PRR-000001002”) automatically inherits the retry interval type (“Staggered”), the interval unit (“Days”), and interval value (“1,3,5”) from the payment retry rule set.

Let’s now create the second payment retry rule for the Stripe payment gateway for an error category such as “Payment Processing Error”. To do this, click New again on the Related tab of “SmartBytes_Payment_Retry_Ruleset” rule set. Enter these details for the payment gateway, error category, and error code, and save your changes.

Payment Gateway: Stripe3P
Payment Gateway Error Category: Payment Processing Error
Payment Gateway Error Code: insufficient_funds

When saved, the new payment retry rule (“PRR-000001003”) automatically inherits the retry interval type (“Staggered”), the interval unit (“Days”), and interval value (“1,3,5”) from the payment retry rule set.

Create a Payment Retry Rule Set with Multiple Payment Retry Rules

Let’s say the Payment admin at SmartBytes wants to create a payment retry rule set with multiple payment retry rules for each payment gateway error category. The payment retry rule set is configured to retry failed payments at fixed intervals, but the payment retry rules are configured to retry failed payments at staggered intervals.

The admin creates a payment retry rule set with these details.

Name: PRRS_Fixed_PRR_Staggered_S3P
Description: SmartBytes’ payment retry rule set of fixed default interval type with multiple retry rules of staggered interval type
Use Alternate Payment Method: Yes
Status: Active
Default Retry Interval Type: Fixed
Default Maximum Retry Count: 5
Default Interval Unit: Minutes
Default Interval Value: 3

When saved, the payment retry rule set is configured with these details.

Let’s now create a payment retry rule for the Stripe payment gateway for an error category “Invalid Payment Details”. To do this, click New on the Related tab of “PRRS_Fixed_PRR_Staggered_S3P” rule set. Enter these details for the payment retry rule, and then save your changes.

Retry Interval Type: Staggered
Interval Unit: Minutes
Interval Value: 1,2,3,4
Payment Gateway: Stripe3P
Payment Gateway Error Category: Invalid Payment Details
Payment Gateway Error Code: payment_method_invalid_parameter

When saved, the new payment retry rule (“PRR-000000722”) is created with the retry interval type (“Staggered”), the interval unit (“Minutes”), and interval value (“1,2,3,4”), overriding the default values of the payment retry rule set.

Similarly, you can create more payment retry rules for other payment gateway error categories of the Stripe3P payment gateway. The Related tab of the payment retry rule set displays the list of all payment retry rules created as part of the rule set.

=== ARTICLE: ind.billing_setup_payment_schedules_and_payment_schedule_items_enable.htm ===
---
article_id: ind.billing_setup_payment_schedules_and_payment_schedule_items_enable.htm
title: Automatic Creation of Payment Schedules and Payment Schedule Items
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_payment_schedules_and_payment_schedule_items_enable.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_payment_schedules_and_payment_schedule_items_auto_manual.htm
fetched_at: 2026-09-04
---

# Automatic Creation of Payment Schedules and Payment Schedule Items

Automate the creation of payment schedules and payment schedule items so that they are ready to be processed.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
Process Overview

When your Payments admin enables the Create Payment Schedules and Payment Schedule Items feature for the first time, these default records are created for your Salesforce org:

DEFAULT RECORD FOR	RECORD NAME	KEY FIELD VALUES
Payment Schedule Policy	Default Payment Schedule Policy	
Payment Schedule Policy Status value: Active
Payment Schedule Treatment Selection value: Default

Payment Schedule Treatment	Default Payment Schedule Treatment	
Payment Schedule Treatment Status value: Active
Automation Trigger Source value: Invoice Posted

Payment Schedule Treatment Detail	Default Payment Schedule Treatment Detail	
Installment Payment Type value: Percentage
Percentage value: 100
Processing Date Reference value: Invoice Due Date
Payment Method Selection Type value: Most Recent Autopay

Payment Schedule Distribution Method	Default Payment Schedule Distribution Method	
Distribution Method Type value: Full Distribution
Distribution Count value: 1
Payment Schedules and Payment Schedule Items

A Payment Schedule record and a Payment Schedule Item record are created based on the configuration of these default records. So, each time an Invoice record is posted, a single Payment Schedule record is created with the entire invoice balance amount as the total requested amount. A single Payment Schedule Item record is created for each Payment Schedule record. You can also group multiple invoices of an account to generate a consolidated Payment Schedule and Payment Schedule Item record.

Access to Edit Payment Schedules and Payment Schedule Items

The user that turns on Create Payment Schedules and Payment Schedule Items is the owner of the default Payment Schedule Treatment record, and the Payment Schedule and Payment Schedule Item records that are automatically created. To enable other users to edit Payment Schedule records and Payment Schedule Item records, set the default internal access of the Payment Schedule object and Payment Schedule Item object to Public Read/Write.

SEE ALSO
Revenue Cloud Developer Guide: PaymentSchedule
Revenue Cloud Developer Guide: PaymentScheduleItem
Revenue Cloud Developer Guide: PaymentSchedulePolicy
Revenue Cloud Developer Guide: PaymentScheduleTreatment
Revenue Cloud Developer Guide: PaymentScheduleTreatmentDtl
Revenue Cloud Developer Guide: PymtSchdDistributionMethod

=== ARTICLE: ind.billing_setup_payments_configure.htm ===
---
article_id: ind.billing_setup_payments_configure.htm
title: Set Up Payment Features in Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_payments_configure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_salesforce_payments_features.htm
fetched_at: 2026-09-04
---

# Set Up Payment Features in Billing

Set up Billing to automatically create payment schedules and payment schedule items for posted invoices, share payment accounts, retry failed payments, pass payment metadata via payment gateways, issue refunds, apply credits and payments to settle the balances of invoices or invoice lines, and automate dunning orchestration.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To enable and configure Payments features:	Payment Admin permission set
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
To automatically create payment schedules and payment schedule items for posted invoices, turn on Create Payment Schedules and Payment Schedule Items.
To view billing details related to payments, payment authorizations, refunds, and saved payment methods, turn on Share Payment Accounts.
To automatically retry failed payments for specific error categories at various time intervals, add at least one default payment retry rule, and then turn on Retry Failed Payments.
To automatically send Level 2 and Level 3 payment details, turn on Level 2 and Level 3 Data Support.
To automatically apply standalone processed payments to posted invoices during invoice run, turn on Application of Payments to Posted Invoices.
To automate the issue of refunds when a fully settled invoice is amended or canceled, turn on Issue Refunds and Settle Balances.
Select the payment application level. The label of this setting is Credit, Refunds, and Payment Application Level.
To apply payments to settle the balances of invoice lines of posted invoices, select Line Level.
To apply payments to settle the balances of posted invoices that have invoice line amounts rolled-up, select Header Level.

The default payment application level is Line Level.

Select the credit memo and payment application rules.
See Define Rules and Order to Apply Credit Memo and Payments.

After you configure Salesforce Payments and turn on the Payment features of Billing, your Payment Operations users can process payments and issue refunds.

=== ARTICLE: ind.billing_setup_payments_merchant_accounts.htm ===
---
article_id: ind.billing_setup_payments_merchant_accounts.htm
title: Set Up Native Payment Gateways by Using Salesforce Payments
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_payments_merchant_accounts.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_salesforce_payments_features.htm
fetched_at: 2026-09-04
---

# Set Up Native Payment Gateways by Using Salesforce Payments

Accept electronic payments from your customers on Stripe and Adyen payment gateways by using the Salesforce Payments native payment service. Create new Stripe merchant accounts or connect your existing Adyen merchant accounts by using Salesforce Payments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To enable and configure Payments features:	Payment Admin permission set

To connect to existing merchant accounts with Adyen, contact your Salesforce account executive for provisioning details.

From Setup, in the Quick Find box, enter Billing, and then select Step 7: Payment Configurations in the Guided Setup.
Expand the Configure Native Payment Gateways step, and click Configure Merchant Payment Accounts.
Click Add Account and follow the guided setup to create a new merchant account for Stripe or connect to an existing merchant account with Adyen.
SEE ALSO
Salesforce Payments

=== ARTICLE: ind.billing_setup_salesforce_payments_features.htm ===
---
article_id: ind.billing_setup_salesforce_payments_features.htm
title: Set Up Payment Features for Revenue Management
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_salesforce_payments_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Set Up Payment Features for Revenue Management

Set up Payments to streamline the management of the entire payment lifecycle. By establishing a secure connection with native and third-party payment providers, you can directly process payments for customer transactions within your Salesforce environment.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.

This flowchart shows how a user with the Payment Admin permission set can set up Payments in Revenue Management.

Configure Salesforce Payments
To use Salesforce Payments for financial transactions, set up an Experience Cloud site and enable Payments for your org. Then, use a guided setup to create a merchant account and payment methods.
Set Up Native Payment Gateways by Using Salesforce Payments
Accept electronic payments from your customers on Stripe and Adyen payment gateways by using the Salesforce Payments native payment service. Create new Stripe merchant accounts or connect your existing Adyen merchant accounts by using Salesforce Payments.
Set Up Third-Party Payment Gateways
Bring your own third-party payment gateways to process payments and issue refunds. Set up and add external payment gateways, and then connect them to Billing.
Set Up Payment Features in Billing
Set up Billing to automatically create payment schedules and payment schedule items for posted invoices, share payment accounts, retry failed payments, pass payment metadata via payment gateways, issue refunds, apply credits and payments to settle the balances of invoices or invoice lines, and automate dunning orchestration.
Generate Pay Now Links for Business Accounts
Collect invoice payments against the correct business account by generating Pay Now links. Your customers pay as a guest with their preferred payment method and can save it for future use.

=== ARTICLE: ind.billing_setup_sequential_numbering_features.htm ===
---
article_id: ind.billing_setup_sequential_numbering_features.htm
title: Turn On Sequential Numbering Features
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_sequential_numbering_features.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_additional_features.htm
fetched_at: 2026-09-04
---

# Turn On Sequential Numbering Features

Apply unique, gapless sequence numbers to transaction records to ensure financial compliance and a clear audit trail. You can also mandate assigning an invoice number to every posted invoice.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To enable Billing features:	Billing Admin permission set
From Setup, in the Quick Find box, enter Billing, and then select Billing Settings.
In the Configure Gapless Sequential Numbering for Billing section, click Sequential Numbering Settings.
Turn on Sequential Numbering.
Return to the Billing Settings page.
To make sure that every posted invoice is assigned an invoice number, turn on Mandate Sequence Policy for Posted Invoices.
To make sure that every posted credit memo is assigned a credit memo number, turn on Mandate Sequence Policy for Posted Credit Memos.

After you turn on sequential numbering features, you or your Billing Operations Users can configure sequential numbering for invoices.

=== ARTICLE: ind.billing_setup_third_party_payments.htm ===
---
article_id: ind.billing_setup_third_party_payments.htm
title: Set Up Third-Party Payment Gateways
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_setup_third_party_payments.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_setup_salesforce_payments_features.htm
fetched_at: 2026-09-04
---

# Set Up Third-Party Payment Gateways

Bring your own third-party payment gateways to process payments and issue refunds. Set up and add external payment gateways, and then connect them to Billing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Cloud
The Salesforce Payments feature is available with the Revenue Cloud Billing license, with a cost per transaction model for both native and Bring Your Own payment gateways. Contact your Salesforce account executive for more information.
If you purchased the Revenue Cloud Billing license on or before July 2025, contact your Salesforce account executive to add the Salesforce Payments feature to your existing license.
USER PERMISSIONS NEEDED
To configure third-party payment features:	Payment Admin permission set
Initial Setup for Configuring Third-Party Payment Gateway

Before you configure third-party payment gateways, complete the preparatory tasks to establish a connection between your Salesforce org and your preferred third-party payment gateway. You need these details to get started.

An e-commerce merchant account and an API key
Apex classes adapters and the adapter name
Named credentials to authenticate your third-party payment gateway
A third-party payment gateway site that's registered in your Salesforce org
A Salesforce site that has access to the third-party payment gateway
Create an e-commerce merchant account in the third-party payment gateway that you want to implement.
Log in to your third-party payment gateway provider and add an e-commerce merchant account.
Navigate to the key management, developer, or advanced settings section of your chosen payment gateway platform, and generate an API key or secret key.

Your API key would look like: AQEvhmfxJ43HaxxHw0m/n3Q5qf3Ve4pBCIBMV3dVwyD4zesmTx/rk8/RZRz2w0bDdqMQwV1bDb7kfNy1WIxIIkxgBw==-C5bPe6tPCqOM35AEGroDa54J1Bl9AnsQKrDsDofVlrk=-i1ibf$Hu2v>8jR:Y9nU.

Note the merchant account user name and API key. You need them to create the named credentials.
Create your payment gateway Apex classes in your Salesforce org.
Obtain the adapter class details from your payment gateway provider or AppExchange.
To build and set up payment gateway adapters, see Payment Gateway Adapters. To define your Apex classes, see Commerce Payments namespace.
Save your Apex classes. Note the adapter name as you need it to create your payment gateway provider.
Create a legacy named credential in your Salesforce org to specify authentication parameters and the URL of your Apex callout endpoint.
Specify a user-friendly name for the label and a unique identifier for the name.
Enter the URL of your third-party payment gateway.
Select Named Principal as the identity type and Password Authentication as the authentication protocol.
Use your merchant account user name as the username. Use the API key as password as required by your payment gateway provider.
Save the named credentials as you need them to create your payment gateway.
Register your third-party payment gateway site in your Salesforce org to make sure that Apex callouts from the org to the payment gateway site are successful.
Enter a name and URL of your third-party payment gateway.
Mark the site as active and save your changes.
Add your third-party payment gateway URL as a trusted URL in your Salesforce org.
Enter an API name.
Enter the URL of your third-party payment gateway.
Mark the URL as active and save your changes.
Enable and set up your Salesforce site, so you can send and receive payments notifications from your third-party gateway.
Enter a label, name, and home page for your site.
Set the site’s public access settings to Guest Access to the Payments API.
Save your site details.
Configure Notification Settings on Your Third-Party Payment Gateway

The payment gateway uses a webhook to send notifications to your payment gateway adapter. A webhook is a combination of your site endpoint and the ID of the payment gateway provider. Create a webhook by providing a URL in the standard notification transport settings of your third-party payment gateway.

Use this URL for your site’s endpoint, replacing MyDomainName with your site's domain and URL. For example:
https://MyDomainName.my.salesforce-sites.com/solutions/services/data/v65.0/commerce/payments/notify
Find the ID of your payment gateway provider, and append the ?provider=ID query parameter to the endpoint. For example, https://MyDomainName.my.salesforce-sites.com/solutions/services/data/v65.0/commerce/payments/notify?provider=0cJR00000004CEhMAM
Enter the webhook in your third-party payment gateway’s standard notification settings.
Configure Payment Gateway Provider and Payment Gateway

Add a payment gateway provider after you set up your merchant account, your adapter classes, and your Salesforce site. Then, add a payment gateway on the payment gateway provider.

From Setup, in the Quick Find box, enter Billing, and then select Step 7: Payment Configurations in the Guided Setup.
Expand the Configure Third-Party Payment Gateways step, click Configure Payment Gateways, and then click Configure.
NOTE

For Salesforce orgs that are created in Winter ’26, the Configure Payment Gateways button in Step 7: Payment Configurations of the Billing Guided Setup, which redirects users to the Payment Gateway Configuration tab, is available by default. For Salesforce orgs that are created before Winter ’26, the Payment Gateway Configuration tab isn’t available by default. To fix this issue, change the settings of the Payment Gateway Configuration tab to Default On.

Complete these fields to create a payment gateway provider.
Enter a unique name and label for your payment gateway provider.
Select the Apex adapter class from the dropdown list.
Specify your required support for idempotency. For more details, see Idempotency Guidelines.
Save the payment gateway provider details.
Complete these fields to add a payment gateway.
Enter a unique name for your payment gateway.
Select a payment gateway provider from the dropdown list.
Select a named credential from the dropdown list.
Mark the status of your payment gateway as Active.
Save the payment gateway details.

If you already have an existing payment gateway provider, select Step 7: Payment Configurations in the Guided Setup, expand the Configure Third-Party Payment Gateways step, and click Configure Payment Gateways. On the Payment Gateway Configuration page, click Payment Gateways, and then click New. The configuration steps are the same.

Add Multiple Payment Methods

Configure support for payment methods such as Automated Clearing House (ACH), Single Euro Payments Area (SEPA), Bankers’ Automated Clearing Services (BACS), and Bulk Electronic Clearing System (BECS) on your third-party payment gateway. You can process payments, issue refunds, and view these saved payment methods in the Saved Payment Methods tab of your billing profile.

To add bank payment methods such as ACH, SEPA, BACS, and BECS, use the tokenizePaymentMethod API and set the bankType property in the bankPaymentMethod object to your chosen bank payment method.
To add card payment methods such as credit card or debit card, use the tokenizePaymentMethod API and set the cardCategory property in the cardPaymentMethod object.
SEE ALSO
Process Payments and Issue Refunds in Revenue Management

=== ARTICLE: ind.billing_standard_context_definitions.htm ===
---
article_id: ind.billing_standard_context_definitions.htm
title: Standard Context Definitions for Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_standard_context_definitions.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_configure_context_definitions.htm
fetched_at: 2026-09-04
---

# Standard Context Definitions for Billing

After you turn on Context Service, you can access the standard context definitions that are available with Billing.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


The BillingContext context definition is available with the Revenue Management Advanced license or the Revenue Management Billing license.

The StandaloneBillingContext context definition is available only with the the Revenue Management Billing license. Contact your Salesforce account executive for more information.

Billing provides two standard context definitions. For optimal integration and a simplified setup, we recommend that you extend the standard context definitions and then use the extended context definitions.

BillingContext Context Definition

The Create Billing Schedules for Orders API uses the BillingContext context definition to hydrate the data of orders to create billing schedules. This context definition maps order data to structured billing configurations and has these mappings:

The OrderEntitiesMapping is the source mapping that maps Order fields to the billing transaction context nodes. The billing transaction nodes outline the structure, interpretation, and processing of billing-related data.
The BSGEntitiesMapping is the target mapping that maps the billing schedule context nodes to the fields of the Billing Schedule, Billing Schedule Group, and Billing Schedule Group Relationship objects. This mapping ensures that Order data is properly transferred to the appropriate Billing Schedule, Billing Schedule Group, and Billing Schedule Group Relationship fields.

On the Billing Settings page, select the extended context definition and context mapping that you want the Create Billing Schedules for Orders API to use.

IMPORTANT

From Summer ’25 and onwards, you will not be able to sync existing context definitions that were either cloned or extended from the standard BillingContext context definition. To fix this issue, use the Context Attribute Mapping API to delete duplicate BSGEntitiesMapping attribute mappings.

BillingTransactionSource attribute of the BillingSchedule node to Reference attribute of the BillingSchedule object.
BillingTransactionItemSource attribute of the BillingSchedule node to the ReferenceItem attribute of the BillingSchedule object.
StandaloneBillingContext Context Definition

The Create Standalone Billing Schedules API uses the StandaloneBillingContext context definition to hydrate the data of transactions to create billing schedules. This context definition has these mappings:

The TransactionMapping maps the fields of the transaction to the attributes of the Transaction node.
The BSGEntitiesMapping maps the attributes of the Billing Schedule, Billing Schedule Group, and Billing Schedule Group Relationship context nodes to the fields of the corresponding Salesforce objects.

=== ARTICLE: ind.billing_standard_tax_custom_metadata_types_configure.htm ===
---
article_id: ind.billing_standard_tax_custom_metadata_types_configure.htm
title: Configure Custom Metadata Types
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_standard_tax_custom_metadata_types_configure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_extend_revenue_standard_tax_engine.htm
fetched_at: 2026-09-04
---

# Configure Custom Metadata Types

Create a custom metadata type that maps billing transaction fields to decision table columns for the Revenue Standard Tax Engine.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create a custom metadata type and custom fields:	Tax Admin permission set

Before you begin, create the custom fields on the Tax Rate object that you want to use as matching criteria or as outputs on tax lines. Also create any custom fields you need on invoice line tax and credit memo line tax. See Create a Custom Field.

Create a custom metadata type.
Click New in the Custom Fields section of the created custom metadata and create these fields exactly as shown here.
FIELD LABEL	API NAME	FIELD TYPE	DESCRIPTION
Entity Field Name	Entity_Field_Name__c	Metadata Relationship (Field Definition)	The field on that object whose value is used when calculating tax.
Entity Name	Entity_Name__c	Metadata Relationship (Entity Definition)	The billing object that this mapping applies to. This field controls Entity Field Name.
Request/Response	Request_Response__c	Picklist. Add these values: Request, Response.	The Request value used as a decision table input. The Response value used to store the matched value on the tax line.
Tax Field Name	Tax_Field_Name__c	Text	The name that links the billing field to the decision table column.
Tax Rate Entity Name	Tax_Rate_Entity_Name__c	Metadata Relationship (Entity Definition)	The Tax Rate entity used in the mapping. This field controls Tax Rate Input Field Name and Tax Rate Output Field Name.
Tax Rate Input Field Name	Tax_Rate_Input_Field_Name__c	Metadata Relationship (Field Definition)	The Tax Rate field used as a decision table input when matching a tax rate.
Tax Rate Output Field Name	Tax_Rate_Output_Field_Name__c	Metadata Relationship (Field Definition)	The Tax Rate field used as a decision table output. Fill this field when Request/Response is Response.
Save the changes. Here’s how a configured custom metadata type appears.
To define records, click Manage [Your Custom Metadata Type Label].
To add your custom field mappings, click New.
For each field mapping, provide the entity name, entity field name, tax field name, request/response, tax rate entity name, and tax rate input or output field values.
Save the changes. Here’s how a configured tax mapping appears.

=== ARTICLE: ind.billing_standard_tax_decision_table_clone.htm ===
---
article_id: ind.billing_standard_tax_decision_table_clone.htm
title: Clone the Decision Table
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_standard_tax_decision_table_clone.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_extend_revenue_standard_tax_engine.htm
fetched_at: 2026-09-04
---

# Clone the Decision Table

Clone the Revenue Standard Tax Entries decision table and add the custom columns that you use to match tax rates.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To change the decision table:	Rule Engine Designer permission set
From the App Launcher, find and select Lookup Tables.
Open Revenue Standard Tax Entries.
From the Show menu, click Clone, enter a name and API name, and save.
Add custom input or output columns from the Tax Rate object to the cloned decision table.
Configure the required setting and operator for each custom input column. See Create a Decision Table and How Null Values Work in Decision Tables.
Activate and refresh the cloned decision table. See Activate a Decision Table and Refresh a Decision Table.

After you configure the custom metadata type and activate the cloned decision table, associate both with a tax engine. Set Type to Revenue Standard Tax Engine, enter the Custom Metadata Type API Name, and select the Decision Table. See Create a Tax Engine.

NOTE After you add or change a tax rate, refresh the cloned decision table so Billing uses the latest rates. See Refresh a Decision Table.

=== ARTICLE: ind.billing_standard_tax_rate.htm ===
---
article_id: ind.billing_standard_tax_rate.htm
title: Revenue Standard Tax Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_standard_tax_rate.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_configuration.htm
fetched_at: 2026-09-04
---

# Revenue Standard Tax Engine

Organizations often face challenges when managing taxes. Common issues include dependency on external tax vendors for simple scenarios, extra licensing and per-transaction costs, performance overhead from external API calls, and regulatory or data residency constraints. These challenges make tax management more complex and costly than necessary. The revenue standard tax engine addresses these issues by enabling internal tax calculation and storage for predictable tax structures. By handling simple tax scenarios internally, organizations can streamline their Revenue Management processes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

You can use multiple tax engines at the same time. Configure some legal entities to use the revenue standard tax engine for simple tax rates, while others use external tax providers for complex jurisdictions.

NOTE Revenue standard tax engine is designed for simple calculations and may not be suitable for tax compliance needs. It calculates taxes at a line level and might include rounding at line level.
Configure Tax Rates
Use the Revenue Standard Tax Engine to calculate taxes natively in Revenue Management. Define tax rates and use the built-in decision table to determine applicable taxes for products.
Understand How Revenue Management Determines and Applies Tax Rates
When you use the Revenue Standard Tax Engine, Revenue Management calculates taxes for transactions by matching the transaction record field values to the configured tax rates. These values include the shipping address, product code, legal entity, and currency ISO code. You can also match custom tax rate fields. Revenue Management uses the Revenue Standard Tax Entries decision table, or a cloned decision table that you associate with the tax engine, to perform this matching.
Revenue Standard Tax Engine Example
Explore an example that shows how the Standard Tax Engine applies multiple tax rates to an invoice based on location, currency, and product criteria.
Extend Your Revenue Standard Tax Engine
Apply tax rates based on custom attributes, such as product category, customer attributes, or exemption criteria, without writing Apex code. Use a custom metadata type to map billing transaction fields to a cloned Revenue Standard Tax Entries decision table, and persist matched values on invoice and credit memo tax lines.
Create a Tax Engine
Create a tax engine record that Billing uses to calculate tax. Set the type to Revenue Standard Tax Engine. When you extend the Revenue Standard Tax Engine, associate a custom metadata type and a decision table.

=== ARTICLE: ind.billing_standard_tax_rate_application.htm ===
---
article_id: ind.billing_standard_tax_rate_application.htm
title: Understand How Revenue Management Determines and Applies Tax Rates
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_standard_tax_rate_application.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_standard_tax_rate.htm
fetched_at: 2026-09-04
---

# Understand How Revenue Management Determines and Applies Tax Rates

When you use the Revenue Standard Tax Engine, Revenue Management calculates taxes for transactions by matching the transaction record field values to the configured tax rates. These values include the shipping address, product code, legal entity, and currency ISO code. You can also match custom tax rate fields. Revenue Management uses the Revenue Standard Tax Entries decision table, or a cloned decision table that you associate with the tax engine, to perform this matching.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

To match custom tax rate fields, see Extend Your Revenue Standard Tax Engine.

How Matching, Priority, and Application Basis Work
NOTE

Revenue Management matches tax rates to transactions by using the Geo Country and Geo State records and their currency ISO codes. If your Salesforce org has State and Country/Territory picklists enabled, Revenue Management can immediately evaluate addresses on transactions against tax rate criteria.

If Geo Country and Geo State records aren’t available or are incomplete, enabling state and country/territory picklists and creating Geo Country and Geo State records can help ensure consistent ISO code usage. This improves address matching accuracy when Revenue Cloud determines applicable tax rates, especially in scenarios where tax rules depend on country or state-level location data. See Enable State and Country/Territory Picklists, Create Geo Countries for the Manual Salesforce Tax Solution, and Create Geo States for the Manual Salesforce Tax Solution.

Revenue Management processes all matching tax rates in the priority order defined on the tax rate record and creates individual tax lines for each applicable tax rate. The priority number determines the order in which tax rates are applied, with lower numbers indicating a higher priority. When both country and state tax rates apply, the priority controls which rate is calculated first. If multiple tax rates share the same priority, the tax rate record created first takes precedence. If no priority is specified, the tax rate is applied last. Similarly, if multiple tax rates have no priority specified, Revenue Management uses them in chronological order, with the tax rate created first taking precedence.

Revenue Management generates tax lines based on the defined tax rates. The tax can be a percentage of the charge amount for gross calculation, a percentage of the charge amount plus previously calculated taxes for net calculation, or a flat tax amount as defined in your tax rate.

Multi-Currency and Single-Currency Considerations

Revenue Management handles tax calculation differently for single and multi-currency orgs.

Single-Currency Org: In a single-currency org, the Revenue Standard Tax Entries decision table is created without the Currency ISO Code field. Tax rate matching considers only the tax code, legal entity, country ISO code, state ISO code, and product code.
Multi-Currency Org: In a multi-currency org, the Revenue Standard Tax Entries decision table automatically includes the Currency ISO Code field. Tax rate matching considers tax code, legal entity, country ISO code, state ISO code, product code, and currency ISO code, ensuring accurate tax application for transactions created with different currencies.
NOTE If you can’t view the Currency ISO Code field for a multi-currency org, manually add this field from the tax rate page layout.
NOTE If your Salesforce org changes currency configuration after initially setting up the standard tax, you must refresh the Revenue Standard Tax Entries decision table to ensure correct tax matching. Revenue Management updates the decision table structure based on your Salesforce org configuration after every refresh. When switching to multi-currency, the Currency ISO Code field is added. When switching to single-currency, the Currency ISO Code field is removed.

=== ARTICLE: ind.billing_standard_tax_rate_example.htm ===
---
article_id: ind.billing_standard_tax_rate_example.htm
title: Revenue Standard Tax Engine Example
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_standard_tax_rate_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_standard_tax_rate.htm
fetched_at: 2026-09-04
---

# Revenue Standard Tax Engine Example

Explore an example that shows how the Standard Tax Engine applies multiple tax rates to an invoice based on location, currency, and product criteria.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

Cloud Kicks sells products across the United States and operates using USD as its currency. The company has configured these tax rates in Standard Tax for the Acme_US legal entity.

Consider an invoice generated on 11/25/2025, with a single invoice line having a Professional Services product for a customer based out of San Francisco, California.

When Acme Corp invoices a customer in San Francisco, California, using the Standard Tax Engine, Revenue Management matches the invoice line to the applicable tax rates by using the in-built decision table.

The matching logic considers the invoice line’s Legal Entity, Country ISO code, and State ISO code, Currency ISO Code, Product Code to filter the tax rate records which are applicable.

In our example the first four rows match and the resulting invoice line taxes generated.

=== ARTICLE: ind.billing_supported_payment_methods_for_the_self_service_billing_portal.htm ===
---
article_id: ind.billing_supported_payment_methods_for_the_self_service_billing_portal.htm
title: Supported Payment Methods for the Self-Service Billing Portal
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_supported_payment_methods_for_the_self_service_billing_portal.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_self_service_portal.htm
fetched_at: 2026-09-04
---

# Supported Payment Methods for the Self-Service Billing Portal

Give your customers more flexibility to pay invoices by configuring additional payment methods, including digital wallets, bank debit methods, and buy now, pay later options, in the Self-Service Billing Portal.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

The payment methods available to your customers depend on the payment gateway that you configure. To configure payment methods, see Set Up Native Payment Gateways by Using Salesforce Payments and Pay Invoices with the Self-Service Billing Portal.

Stripe

If you configure Stripe as your payment gateway, your customers can pay by using these payment methods.

ACH Debit
Affirm
Afterpay/Clearpay
Amazon Pay
Apple Pay
BACS Debit
BECS Debit
Bancontact
Canadian PAD
Credit Cards
EPS
Google Pay
iDEAL
Klarna
Link By Stripe
New Zealand BECS Debit
SEPA Debit
Adyen

If you configure Adyen as your payment gateway, your customers can pay by using these payment methods.

ACH Debit
Afterpay/Clearpay
Affirm
Apple Pay
Bancontact
Canadian PAD
Credit Cards
EPS
Google Pay
iDEAL
Klarna
SEPA Debit
NOTE Payment method availability depends on your invoice currency and merchant account region. For a complete list of supported payment methods and constraints, see the Stripe Payment Methods documentation and Adyen Payment Methods documentation.

=== ARTICLE: ind.billing_suspend_and_resume.htm ===
---
article_id: ind.billing_suspend_and_resume.htm
title: Manage Suspend and Resume Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_suspend_and_resume.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_suspend_and_resume_overview.htm
fetched_at: 2026-09-04
---

# Manage Suspend and Resume Billing

Suspend billing from an account or billing schedule group, then update the resumption date or cancel the suspension.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To suspend and resume billing:	

You must have one of these permission sets:

Billing Admin permission set
Billing Operations User permission set
Billing Customer Service User permission set
Suspend Billing

You can suspend billing directly from an Account record or a Billing Schedule Group record.

From the App Launcher, find and select Accounts or Billing Schedule Groups.
Open the Account record or Billing Schedule Group record that you want to suspend billing for.
From the quick actions menu, click Suspend Billing.
Specify the suspension date.
The suspension date can be the current date or a future date.
Specify the resumption date.
The resumption date can be any date after the suspension date. If you don’t know when billing should resume, specify your best estimate. You can update the resumption date later from Resume Billing.
Click Suspend.

After you suspend billing, no invoices are generated for the account or billing schedule group between the suspension date and the day before the resumption date.

Suspending billing defers charges for that period—it doesn’t waive them. For how Billing evaluates suspensions with a target date, billing period count, and multiple suspensions, see Understand Billing Suspensions and Target Date.

NOTE Starting Winter ’27, Billing evaluates billing suspensions as of the target date, not the run date of the invoice batch run. If you already have suspension periods, invoice runs that use a target date can generate different invoices than before.
EXAMPLE A customer’s payment method fails on April 10 and is expected to recover in 10 days. Specify the suspension date as April 10 and the resumption date as April 20 for that customer’s account. As a result, invoices aren’t generated from April 10 to April 19, and billing resumes from April 20.
Resume Billing or Cancel Suspension

When an account or a billing schedule group is currently suspended for billing or is scheduled to be suspended for billing in the future, the Resume Billing button appears on the Account record or the Billing Schedule Group record.

To update the resumption date of billing during this period, click Resume Billing, update the resumption date, and click Resume.
To cancel the suspension, click Resume Billing, select Cancel suspension, and click Resume.

After billing resumes, charges from the suspension period are also billed. Those deferred charges can also be included when an invoice run uses a target date on or after the resumption date. If you don’t want to include these charges, issue a credit memo. See Understand Billing Suspensions and Target Date.

You can also suspend and resume billing by using the Suspend Billing API and the Resume Billing API.

=== ARTICLE: ind.billing_suspend_and_resume_overview.htm ===
---
article_id: ind.billing_suspend_and_resume_overview.htm
title: Suspend and Resume Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_suspend_and_resume_overview.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Suspend and Resume Billing

Pause invoicing temporarily for an account or billing schedule group without canceling its billing schedules. Suspensions defer charges, they don’t waive them.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

Use Suspend and Resume Billing when invoicing should stop for a while, but the customer’s account and billing schedules stay in place. Common reasons include:

Payment method failures or other payment disruptions
Billing errors that need time to correct
Customer disputes to resolve before the next invoice
Temporary gaps when the customer doesn’t need to be billed
Manage Suspend and Resume Billing
Suspend billing from an account or billing schedule group, then update the resumption date or cancel the suspension.
Understand Billing Suspensions and Target Date
Learn how Billing evaluates suspensions when invoice runs and the Invoice Creation API use a target date or billing period count.

=== ARTICLE: ind.billing_tax_additional_configuration.htm ===
---
article_id: ind.billing_tax_additional_configuration.htm
title: Additional Tax Information
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_additional_configuration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_configuration.htm
fetched_at: 2026-09-04
---

# Additional Tax Information

After you choose a tax engine, Billing uses tax policies and treatments to decide how invoices are taxed. You can also capture a consolidated tax amount at the invoice header. Billing then calculates tax and stores tax totals on the invoice.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Capture Taxes at Header Level
Use a single consolidated tax amount at the invoice header level for invoices and credit memos.
Create Tax Policies and Treatments
Create tax policies and their treatments to define the tax calculation for your invoices.
Override Addresses on Invoice Lines
When you separately bill certain order products of an account, you can specify different tax addresses on the invoices of those order products. This flexibility ensures accurate tax calculations and compliance with regional tax regulations because the tax address is important for calculating tax. Also, your customers benefit from the enhanced accuracy in their financial documentation.
Tax Totals at the Line and Header Levels
Understand how Billing applies line-level and header-level tax amounts during balance calculation.
Tax Calculation Process
Understand the tax calculation process for invoices.

=== ARTICLE: ind.billing_tax_address_invoice_line_override.htm ===
---
article_id: ind.billing_tax_address_invoice_line_override.htm
title: Override Addresses on Invoice Lines
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_address_invoice_line_override.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_additional_configuration.htm
fetched_at: 2026-09-04
---

# Override Addresses on Invoice Lines

When you separately bill certain order products of an account, you can specify different tax addresses on the invoices of those order products. This flexibility ensures accurate tax calculations and compliance with regional tax regulations because the tax address is important for calculating tax. Also, your customers benefit from the enhanced accuracy in their financial documentation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To modify billing schedule groups and set history tracking:	Billing Admin permission set
Change Addresses of Billing Schedule Groups

The addresses of your accounts appear as addresses on the related billing schedule groups. The addresses of your billing schedule groups appear as addresses on the related invoice tax lines. So, to specify different tax addresses on the invoices of order products that you’re billing, change the shipping and billing addresses of the billing schedule groups that are related to the order products.

From the App Launcher, find and select Billing Schedule Groups.
Open the Billing Schedule Group record that you want to modify.
Change the shipping address and billing address.
Save your changes.

When invoice runs process the billing schedule groups, the invoice runs generate invoices with invoice line taxes that show the changed addresses of the billing schedule groups.

Track Changes to Billing Schedule Group Addresses

Your Billing admin can enhance the accountability of your billing processes by enabling field history tracking for the Billing Schedule Group object’s address fields. Billing specialists can then monitor and audit any modifications made to these fields.

From the object management settings for billing schedule groups, go to Fields & Relationships.
Click Set History Tracking.
Select Billing Address and Shipping Address from the list of fields.
Save your changes.

Customize the Billing Schedule Group’s page layout to include the History related list. All the changes that you make to the Billing Schedule Group address fields are added to the History related list on the Billing Schedule Group records.

=== ARTICLE: ind.billing_tax_calculation_results.htm ===
---
article_id: ind.billing_tax_calculation_results.htm
title: Tax Calculation Process
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_calculation_results.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_additional_configuration.htm
fetched_at: 2026-09-04
---

# Tax Calculation Process

Understand the tax calculation process for invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

Billing schedules generated for order products inherit tax treatment from the order products. When invoices are generated from billing schedules, the Calculate Tax API is triggered. This API then uses the tax engine specified for the billing schedules' tax treatment to calculate the applicable taxes. Estimated tax is calculated for draft invoices. Actual tax is calculated for posted invoices.

After the tax is calculated, tax details appear on the Invoice Line Tax records. Several fields, such as the ones that drive the calculation and the status of the calculation process, are updated. This table provides a comprehensive list of fields that are populated during and after the tax calculation.

INVOICE LINE TAX FIELD	DESCRIPTION
Tax Amount	The total tax for the related invoice line. This amount is aggregated to the Tax Amount field of the Invoice Line object, which in turn is aggregated to the Total Tax field on the parent Invoice object.
Tax Code	The tax code is used to calculate the tax rate for the related invoice line.
Tax Document Number	The record in the external tax engine that corresponds to the related invoice line.
Tax Effective Date	The date that’s used to calculate the tax amount.
Tax Exempt Amount	The amount that's exempted from tax.
Tax Name	The name of the applied tax.
Tax Rate	The percentage value that’s used for calculating tax.
Tax Transaction Number	The record in the external tax engine that corresponds to the transaction that's related to the invoice line.
NOTE Use a tax system or a tax vendor that supports certificate management, including certificate validation, compliance with state registrations, lifecycle tracking, and audit trails for tax exemption scenarios. When managing exemption certificates, maintain a matching key between Billing records and the tax system.
For account-level exemptions, use the Account ID as the reference key.
For product-level exemptions, use the Product Code from the Product2 record.

During tax calculation, Billing sends account and product information in the tax request. The tax system uses these identifiers to evaluate and apply the appropriate exemption certificates.

SEE ALSO
Revenue Cloud Developer Guide: Tax Calculation API

=== ARTICLE: ind.billing_tax_configuration.htm ===
---
article_id: ind.billing_tax_configuration.htm
title: Tax Calculation for Invoices
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_configuration.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Tax Calculation for Invoices

Configure how taxes are calculated on the billing amounts of your taxable products or services, or import tax amounts calculated by an external system.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

This flowchart shows how users with the Billing Admin and Tax Admin permission sets can configure tax calculation for invoices in Revenue Management.

Tax Calculation Solutions
When you set up tax calculation, match each product’s tax needs to a partner or custom tax engine, the Revenue Standard Tax Engine, or imported tax lines. You can use more than one tax engine when products have different tax needs.
Partner or Custom Tax Engine
When you need complex tax jurisdictions or already use a tax vendor, you connect a partner tax app or your own tax engine. The TaxEngineAdapter Apex interface retrieves information from the tax engine and evaluates the information to define tax details.
Revenue Standard Tax Engine
Organizations often face challenges when managing taxes. Common issues include dependency on external tax vendors for simple scenarios, extra licensing and per-transaction costs, performance overhead from external API calls, and regulatory or data residency constraints. These challenges make tax management more complex and costly than necessary. The revenue standard tax engine addresses these issues by enabling internal tax calculation and storage for predictable tax structures. By handling simple tax scenarios internally, organizations can streamline their Revenue Management processes.
Import External Tax Lines into Billing
Bring in the tax amounts calculated by an external system for draft invoices.
Additional Tax Information
After you choose a tax engine, Billing uses tax policies and treatments to decide how invoices are taxed. You can also capture a consolidated tax amount at the invoice header. Billing then calculates tax and stores tax totals on the invoice.

=== ARTICLE: ind.billing_tax_configuration_engine.htm ===
---
article_id: ind.billing_tax_configuration_engine.htm
title: Tax Calculation Solutions
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_configuration_engine.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_configuration.htm
fetched_at: 2026-09-04
---

# Tax Calculation Solutions

When you set up tax calculation, match each product’s tax needs to a partner or custom tax engine, the Revenue Standard Tax Engine, or imported tax lines. You can use more than one tax engine when products have different tax needs.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Integrate a partner tax app, such as Vertex or Avalara, or your own tax engine, with the Billing TaxEngineAdapter Apex interface.
Calculate simple taxes in Billing with the Revenue Standard Tax Engine, without an external integration.
Import tax lines that were calculated outside Salesforce.

=== ARTICLE: ind.billing_tax_configuration_prerequisites.htm ===
---
article_id: ind.billing_tax_configuration_prerequisites.htm
title: Prerequisites for a Partner or Custom Tax Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_configuration_prerequisites.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_partner_or_custom_tax_engine.htm
fetched_at: 2026-09-04
---

# Prerequisites for a Partner or Custom Tax Engine

If you want to calculate taxes by using your own tax engine or by integrating the Billing TaxEngineAdapter Apex interface with a partner app, complete these prerequisites.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Gather Tax Provider Details

If you want to use a tax service provider, gather this information:

Tax provider’s seller code
Tax provider’s mailing address
Credentials for accessing the tax provider
Create a Named Credential

After you gather the tax provider details, create a named credential to secure and authenticate API callouts to the tax engine.

Define a Custom Apex Adapter

If you use your own tax engine, define a custom tax adapter by extending the TaxEngineAdapter Apex interface.

You can model your custom tax adapter’s implementation based on this example.

From Summer ’25, Billing supports up to 2000 invoice lines for a single invoice. To avoid limit-related issues, test your TaxEngineAdapter Apex interface’s implementation to make sure that it adheres to the Apex limit for total heap size.

=== ARTICLE: ind.billing_tax_engine_and_engine_providers_create.htm ===
---
article_id: ind.billing_tax_engine_and_engine_providers_create.htm
title: Create a Tax Engine Provider and Tax Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_engine_and_engine_providers_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_partner_or_custom_tax_engine.htm
fetched_at: 2026-09-04
---

# Create a Tax Engine Provider and Tax Engine

If you use a partner app or your own engine, create a tax engine provider and a tax engine.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create tax engine providers and tax engines:	Tax Admin permission set

Make sure that you complete the prerequisites before you create a tax engine provider and tax engine.

Create a Tax Engine Provider

Create a tax engine provider to store information about the Apex adapter class that manages communication with the tax engine.

From the App Launcher, find and select Tax Engine Providers.
Click New.
Enter a label and API name for the tax engine provider.
Select the ID of the Apex adapter that you want the tax engine provider to use.

If you use your own tax engine, select the custom tax adapter that you configured.

NOTE Select a unique Apex adapter for each tax engine provider.
If you have extended tax callouts, enter the API name of the custom metadata type you created.
Save your changes.
Create a Tax Engine

Create a tax engine record that Billing uses to calculate tax. Include the tax engine provider, named credential, seller code, and address.

From the App Launcher, find and select Tax Engines.
Click New.
Enter a name for the tax engine.
Select the type as Revenue Cloud Tax Extension.
Select the tax engine provider.
Select the named credential that you created to authenticate the tax engine.
Enter the seller code of the tax provider.
Enter the address of the tax provider.
Select the status as Active.
You can use only active tax engines to calculate taxes.
To capture taxes at the header level, select Capture Taxes At Header.
The Capture Taxes At Header checkbox appears only when Credit, Payment, and Refund Application Level is Header Level. See Capture Taxes at Header Level.
Save your changes.

Create tax policies and treatments. If the tax treatment is taxable, select this tax engine on the tax treatment. Then assign the tax policy to the relevant products. When Billing calculates tax for an order product, it uses the tax engine on the product’s tax treatment.

NOTE Make sure that your tax engine supports tax calculation for credits used for negative invoice lines and credit memos. If the tax engine doesn’t support credits, Billing can’t process negative invoice lines and invoice void operations fail.

=== ARTICLE: ind.billing_tax_engine_create.htm ===
---
article_id: ind.billing_tax_engine_create.htm
title: Create a Tax Engine
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_engine_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_standard_tax_rate.htm
fetched_at: 2026-09-04
---

# Create a Tax Engine

Create a tax engine record that Billing uses to calculate tax. Set the type to Revenue Standard Tax Engine. When you extend the Revenue Standard Tax Engine, associate a custom metadata type and a decision table.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To create tax engines:	Tax Admin permission set
From the App Launcher, find and select Tax Engines.
Click New.
Enter a name for the tax engine.
Select the type as Revenue Standard Tax Engine.
If the Type field is empty, Revenue Cloud Tax Extension is considered as the value.
When you extend the Revenue Standard Tax Engine, complete these fields.
Enter the API name of the custom metadata type in Custom Metadata Type API Name. See Configure Custom Metadata Types.
Custom Metadata Type API Name is the API name of the custom metadata type that maps billing transaction fields to Revenue Standard Tax Entries decision table inputs and outputs. The tax engine references this custom metadata type to identify which field mappings to apply when it evaluates the decision table.
Select the cloned decision table in Decision Table. See Clone the Decision Table.
The Revenue Standard Tax Engine matches tax rates with this decision table. If this field is blank, the engine uses the Revenue Standard Tax Entries decision table. To match custom tax rate fields, select your cloned table and make sure that table is active. The decision table must be active.
Select the status as Active.
You can use only active tax engines to calculate taxes.
To capture taxes at the header level, select Capture Taxes At Header.
The Capture Taxes At Header checkbox appears only when Credit, Payment, and Refund Application Level is Header Level. See Capture Taxes at Header Level.
Save your changes. Here’s how the tax engine appears after you associate the custom metadata type and decision table.

=== ARTICLE: ind.billing_tax_identification_configure.htm ===
---
article_id: ind.billing_tax_identification_configure.htm
title: Configure Additional Tax Identification Details
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_identification_configure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_partner_or_custom_tax_engine.htm
fetched_at: 2026-09-04
---

# Configure Additional Tax Identification Details

Send additional tax identification details to your external tax engine. Meet regional tax compliance requirements by storing tax identification and exemption information on the Billing Account and passing it to the tax engine.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To define tax details in a picklist:	Billing Admin permission set

For more information, see Add or Edit Picklist Values and Know Your Incoterms.

In Setup, find and select Object Manager.
Open Billing Accounts.
Select Fields & Relationships.
Click Tax Exemption Status.
In the Tax Exemption Status Picklist Values section, click New.
Enter the values that align with your tax engine, such as Exempt, Not Applicable, and Partial.
Save your changes.
Return to Fields & Relationships, click Delivery Terms, and repeat the same steps.
Go to Page Layouts.
Open the Billing Account Layout, add the additional tax identification details, and save the changes.
Only Tax Exemption Status and Delivery Terms are picklists. Add all six tax identification fields to the layout.
Tax Identification Number
Tax Identification Details
Tax Exemption Number
Tax Exemption Status
Exemption Expiration Date
Delivery Terms

After adding the required fields, you can open a Billing Account and verify the changes. When Billing calculates taxes, it automatically retrieves additional tax identification details from the default Billing Account associated with the Account. This information is passed to the configured external tax engine as part of the tax calculation request.

Tax identification support applies only to invoices, credit memos, and debit memos. Tax identification information isn’t used during tax calculation for quotes or orders.

=== ARTICLE: ind.billing_tax_lines_import.htm ===
---
article_id: ind.billing_tax_lines_import.htm
title: Import External Tax Lines into Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_lines_import.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_configuration.htm
fetched_at: 2026-09-04
---

# Import External Tax Lines into Billing

Bring in the tax amounts calculated by an external system for draft invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To export and import Invoice Line Tax records:	Billing Admin OR Billing Operations User permission set
Create draft invoices for order products having Is Taxable set to false on tax treatments.
See Create Tax Policies and Treatments and Generate Invoices in Revenue Management.
Use a data extraction tool to export the required Invoice Line fields.
The external tax system uses this data to calculate taxes.
Import the calculated Invoice Line Tax records into Billing.
The external tax system must provide a CSV file that includes the mandatory fields such as TaxTransactionNumber, TaxAmount, TaxRate, TaxName, TaxCode, TaxEffectiveDate, InvoiceLine, TaxDocumentNumber, TaxExemptAmount, and TaxProcessingStatus. The TaxProcessingStatus field in your import CSV file must be set to Posted. See Prepare a CSV File for Import.
Verify that the imported invoice line taxes are associated with the correct invoice lines.
You can modify or delete the imported invoice line taxes before posting the invoice.
Post the corresponding invoices.
EXAMPLE

Here's a sample CSV file for invoice line tax. Make sure to include the mandatory fields along with any additional fields you need.

INVOICELINEID	LEGALENTITYID	TAXAMOUNT	TAXCODE	TAXDOCUMENTNUMBER	TAXEXEMPTAMOUNT	TAXNAME	STARTDATE	ENDDATE
5TVSG0000007l0b4AA	0fwSG000000TwwfYAC	50	PA020111	3ttDU00000002Fr_Debit-4wADU0000002aH22AI	0	T1234	2025-03-21	2025-03-31
5TVSG0000007l0c4AA	0fwSG000000TwwfYAC	30	PA020111	3ttDU00000002Fr_Debit-4wADU0000002aH22AI	0	T1234	2025-03-21	2025-03-31

=== ARTICLE: ind.billing_tax_policies_and_treatments_create.htm ===
---
article_id: ind.billing_tax_policies_and_treatments_create.htm
title: Create Tax Policies and Treatments
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_policies_and_treatments_create.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_additional_configuration.htm
fetched_at: 2026-09-04
---

# Create Tax Policies and Treatments

Create tax policies and their treatments to define the tax calculation for your invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS
NEEDED
To create tax policies and tax treatments:	Tax Admin permission set
Create Tax Policies

Tax policies are related to order products, which pass the policy on to the resulting billing schedules. Each tax policy requires at least one tax treatment.

From the App Launcher, find and select Tax Policies.
Click New.
Enter a name for the tax policy.
Select the status as Draft.
Select the treatment selection.
To use the default tax treatment of the tax policy, select Default. If you don't specify a default tax treatment for the tax policy, the default tax treatment selected for your Salesforce org is used.
To use the tax treatment of the related order product, select Manual.
To use the tax treatment of the related order product's legal entity, select Legal Entity.

This table explains the usage of tax treatment.

TREATMENT SELECTION	SCENARIO	BEHAVIOR
Manual	No tax treatment selected for the related order product	Uses the default tax treatment of the tax policy
Manual	No default tax treatment selected for the tax policy	Uses the default tax treatment selected for your Salesforce org
Manual	No default tax treatment selected for your Salesforce org	The tax calculation fails
Legal Entity	No legal entity specified for the related order product or order	Uses the tax treatment of the default legal entity selected for your Salesforce org
Legal Entity	No default legal entity selected for your Salesforce org	Uses the tax treatment related to the tax policy that has the same legal entity as that of the related order product
Legal Entity	No matching legal entity	Uses the default tax treatment of the tax policy
Legal Entity	No default tax treatment selected for the tax policy	Uses the default tax treatment of the tax policy
Legal Entity	No default tax treatment selected for your Salesforce org	The tax calculation fails
If necessary, enter a description.
If the treatment selection is Default, specify a default tax treatment.
Save your changes.

After you create a tax policy, create and activate the related tax treatments.

Create Tax Treatments

Define the criteria for calculating taxes for invoices.

From the App Launcher, find and select Tax Treatments.
Click New.
Enter a name for the tax treatment.
If you select Is Taxable, select the tax engine for the tax treatment.
When tax is calculated for an order product, this tax engine of the product’s tax treatment is used.
If necessary, enter the code of the product that the tax treatment applies to.
Select the tax policy that you want to relate to the tax treatment.
If necessary, enter a description.
Enter the reference code that's used to calculate tax as the tax code.
The tax code of the tax engine is populated as the invoice line tax’s tax code.
To calculate taxes based on your product codes, select Use Tax Treatment Items.
When you select this option but don't have any tax treatment items for the tax treatment, Billing uses the tax code on the tax treatment. If you didn't define a tax code, Billing sends a null value to the tax engine.
If you selected Use Tax Treatment Items, set the status of the tax treatment to Draft, associate the required tax treatment items, and then set the status of the tax treatment to Active. If you didn't select the Use Tax Treatment Items option, select Active as the status.
To calculate tax for order products that are related to the tax policy, select Is Taxable.
If the treatment selection of the parent tax policy is Legal Entity, select the legal entity that you want to relate to the tax treatment.
Save your changes.

After you create an active tax treatment, change the status of the parent tax policy to Active. Only active tax policies can be used for tax calculation. Then, select the tax treatments for order products.

NOTE Make sure that the tax treatments or the orders products have a legal entity, or that a default legal entity is selected for the Salesforce org.
Create Tax Treatment Items

Use tax treatment items to define how individual products are taxed within a tax treatment. Resolve tax codes based on both the legal entity and the product, providing more granular and accurate tax calculations.

NOTE To calculate taxes based on a product code, select Use Tax Treatment Items on the tax treatment and associate the required tax treatment item. Billing resolves the applicable tax treatment item by using the product code on the transaction.
From the App Launcher, find and select Tax Treatment Items.
Click New.
Enter a name for the tax treatment item.
Select a tax treatment for the tax treatment item.
Enter the product code for the product associated with this tax treatment item.
Enter the tax code applicable for the selected product and for the legal entity.
Select the product that you're creating the tax treatment items for.
Save your changes.

=== ARTICLE: ind.billing_tax_rate_configure.htm ===
---
article_id: ind.billing_tax_rate_configure.htm
title: Configure Tax Rates
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_rate_configure.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_standard_tax_rate.htm
fetched_at: 2026-09-04
---

# Configure Tax Rates

Use the Revenue Standard Tax Engine to calculate taxes natively in Revenue Management. Define tax rates and use the built-in decision table to determine applicable taxes for products.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
USER PERMISSIONS NEEDED
To configure tax rates:	

Tax Admin permission set

To streamline tax rate configuration, make sure to provide sharing access and sharing rules for the Geo Country and Tax Rate objects.

From the App Launcher, find and select Tax Rates.
Click New.
Verify that the rate application is set to Revenue Management.
Enter a tax code.
The tax code defined here is used in tax treatment and tax treatment item records to determine how the tax rate is applied. Make sure that the same tax code is consistently referenced across tax configurations so the correct rate is applied during transaction processing.
Enter the geo country or geo state where the rate applies.
Geo Country and Geo State records must be created with the correct ISO code.
Select a currency ISO code.
This field is available for multi-currency orgs only. If you’re unable to view this field, add it from the page layout.
Enter the tax rate as a percentage or flat amount.
Revenue Management doesn’t validate tax percentage or flat tax amount values. Make sure that the tax percentage is greater than 0% or the flat tax amount is a positive value.
Select the application basis.
See Understand How Revenue Management Determines and Applies Tax Rates section to know how the gross and net taxes are used in tax calculation.
Enter a priority.
When multiple tax rates match a transaction, Revenue Management uses this value to determine the execution order. Lower values run first, with priority 1 taking precedence over priority 2 and so on.
Enter the product code if the tax rate is specific to a product.
You can find the product code from the respective products in your Salesforce org. For example, the invoice line includes a reference to the associated product. The product code specified here is matched against the product code on the transaction to determine the applicable tax rate.
Enter the start date and end date to define the validity of this tax rate record.
Select a legal entity.
Revenue Management doesn’t mandate a legal entity entry, but you must add one to manage and map tax rates to transactions by legal entity.
If you created custom fields on the Tax Rate object for additional matching criteria, enter values for those fields.
Save your changes.
Check for and refresh the Revenue Standard Tax Entries decision table every time a tax rate record is modified or added in your Salesforce org. If you cloned the decision table, activate and refresh the cloned table. See Refresh a Decision Table.

Create a Tax Engine record with the type set to Revenue Standard Tax Engine. If you use custom tax rate fields, extend the decision table and associate it with that tax engine. See Extend Your Revenue Standard Tax Engine. Next, create the Tax Policy and Tax Treatment records, making sure the Tax Treatment references the tax engine record with type set to Revenue Standard Tax Engine. Finally, assign the appropriate tax policy to the relevant products.

To maintain consistency and data integrity with country and state values that are used in addresses, it’s recommended to enable State and Country picklists. See Enable State and Country/Territory Picklists, Create Geo Countries for the Manual Salesforce Tax Solution, and Create Geo States for the Manual Salesforce Tax Solution.

=== ARTICLE: ind.billing_tax_summary_difference.htm ===
---
article_id: ind.billing_tax_summary_difference.htm
title: Tax Totals at the Line and Header Levels
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_tax_summary_difference.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_tax_additional_configuration.htm
fetched_at: 2026-09-04
---

# Tax Totals at the Line and Header Levels

Understand how Billing applies line-level and header-level tax amounts during balance calculation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

When Capture Taxes At Header is turned on:

For an Apex or partner tax engine, Billing stores the consolidated tax amount returned by your tax engine in the Total Taxes Captured at Header field on invoices and credit memos.
For the Revenue Standard Tax Engine, Billing calculates tax from the invoice total charge amount and shipping address, then stores the result at the invoice header.
Invoice balance calculations use the header tax amount instead of the sum of line-level taxes.
Billing retains line-level tax details as an aggregated total of all invoice lines for reporting or reconciliation when provided by the tax adaptor.
For credit memos created from invoices based on the header tax, the credit memo records the corresponding header tax amount. The Total Taxes Captured at Header field stores the tax amount returned for the credit memo calculation.

Billing applies line-level tax instead of header-level tax in these situations:

The header tax amount is null or missing.
The tax engine fails to return a header tax amount.
The invoice is created before header tax is enabled.
The Credit, Payment, and Refund Application Level is changed from Header Level to Line Level after invoice creation.
The users manually edit tax amounts while the invoice is in draft status.
A tax engine timeout occurs during header tax calculation.
A network connectivity issue interrupts tax service calls.
The currency conversion fails for the header tax amount.
Exchange rate calculation errors affect the header tax amount.
The header tax format in the API request is invalid.
An API version compatibility issue prevents header tax processing.

=== ARTICLE: ind.billing_transaction_amounts_corporate_currency.htm ===
---
article_id: ind.billing_transaction_amounts_corporate_currency.htm
title: Capture Transaction Amounts in Multiple Currencies
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_transaction_amounts_corporate_currency.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_financial_accounting.htm
fetched_at: 2026-09-04
---

# Capture Transaction Amounts in Multiple Currencies

Manage multi-currency billing transactions by viewing amounts in transactional currency, functional currency, and corporate currency.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management (formerly Revenue Cloud)


The feature is available for the Invoice and Credit memo records, and their related records with the Revenue Cloud Advanced license or the Revenue Cloud Billing license.

This feature is available for the Payment, Refund, and Debit Memo records, and their related records with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

Types of Currencies in Billing

In Salesforce org where multiple currencies are enabled, billing transactions are captured in these currencies.

Corporate Currency
The currency in which the organization's corporate headquarters reports revenue. For Salesforce orgs where multiple currencies are enabled, corporate currency serves as the basis for all currency conversion rates. See Manage Information About Your Company, Set Your Corporate Currency, and Edit Conversion Rates.
Functional Currency
The currency of the Legal Entity record associated with a transaction record.
Transaction Currency
The currency in which the transaction takes place.
Process Overview

After your Billing admin turns on Store Transaction Amounts in Corporate and Functional Currencies, the transaction amounts are automatically captured in corporate and functional currencies. The transaction amounts are converted based on the advanced currency management conversion rate on the day the transaction or one of its related records is posted, or processed.

Users with the Account Receivables Admin permission set can update the corporate and the functional currency conversion rate fields on the billing transaction record. They can also update the Functional Currency ISO Code field to match it with the currency of the transaction's legal entity

Transaction Amount Conversion Details

The transaction amounts that appear in brackets (1) are in the user's personal currency. The amount is calculated based on the static conversion rates defined in the Manage Currencies settings in your Salesforce org. If you don't want the transaction amounts in brackets to appear, disable parenthetical currency conversions.

The Corporate Currency Information section provides all the corporate conversion fields and the converted amounts. Similarly, the Functional Currency Information section provides all the functional conversion fields and the corresponding converted amounts, as defined in the Currency Conversion Amount Fields table.

The amounts that appear in the Corporate Currency Information (2) and Functional Currency Information (3) sections are calculated based on the advanced currency management conversion rates valid on the transaction's posted or processed date.

Currency Conversion Amount Fields

The table shows the fields that capture the converted amount for both corporate currency and functional currency.

BILLING TRANSACTION	TRANSACTION CURRENCY FIELD	CORPORATE CURRENCY FIELD	FUNCTIONAL CURRENCY FIELD
Invoice	Total with Tax	Corporate Currency Converted Total Amount With Tax	Functional Currency Converted Total Amount With Tax
Invoice Line	Charge Amount	Corporate Currency Converted Total Charge Amount	Functional Currency Converted Charge Amount
Invoice Line	Tax Amount	Corporate Currency Converted Total Tax Amount	Functional Currency Converted Total Tax Amount
Invoice Line Tax	Tax Amount	Corporate Currency Converted Tax Amount	Functional Currency Converted Tax Amount
Credit Memo	Total with Tax	Corporate Currency Converted Total Amount With Tax	Functional Currency Converted Total Amount With Tax
Credit Memo Line	Charge Amount	Corporate Currency Converted Total Charge Amount	Functional Currency Converted Charge Amount
Credit Memo Line	Tax Amount	Corporate Currency Converted Total Tax Amount	Functional Currency Converted Total Tax Amount
Credit Memo Line Tax	Tax Amount	Corporate Currency Converted Tax Amount	Functional Currency Converted Tax Amount
Payment	Amount	Corporate Currency Converted Amount	Functional Currency Converted Amount
Refund	Amount	Corporate Currency Converted Amount	Functional Currency Converted Amount
Debit Memo	Total Charge Amount	Corporate Currency Converted Total Charge Amount	Functional Currency Converted Total Charge Amount
Debit Memo Line	Charge Amount	Corporate Currency Converted Charge Amount	Functional Currency Converted Charge Amount
Debit Memo Line Tax	Tax Amount	Corporate Currency Converted Tax Amount	Functional Currency Converted Tax Amount

=== ARTICLE: ind.billing_treatment_exclude_from_billing.htm ===
---
article_id: ind.billing_treatment_exclude_from_billing.htm
title: Understand Exclude From Billing
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_treatment_exclude_from_billing.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_policies_and_treatments.htm
fetched_at: 2026-09-04
---

# Understand Exclude From Billing

When you set Exclude From Billing on a billing treatment value to Yes, the system skips creating billing schedules, billing schedule groups, and invoices for order items that aren’t ready for billing. Instead of delaying the entire order, you can exclude specific order items and continue processing the rest. When the excluded order items are ready, set Exclude From Billing to No, or assign a billable treatment to the order item, and then reprocess the order so the system reevaluates the items.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

Here’s how Exclude From Billing applies to various billing scenarios:

New Sales and Amendments, Renewals, and Cancellations: If you exclude a new sale order item from billing, the system also excludes its related amendment, renewal, or cancellation. The system doesn’t create billing schedules or invoices for those records. If you don’t exclude the related amendment, renewal, or cancellation, the system returns an error because the system can’t find a billing schedule for the original new sale. If the system already processed the new sale, excluding a related amendment, renewal, or cancellation has no effect. The system continues to include that related order item.

Product Bundles: For product bundles where the parent product’s billing treatment has Exclude From Billing set to Yes and child products have it set to No, the system creates billing schedules for the child products only. This behavior applies to new sales and to amendments, renewals, and cancellations.

Ramp Deals: Because multiple segments can be included in ramp deals, the system doesn’t bill or invoice any excluded segment. If you amend a non-billable ramp segment to billable, make sure that the billing reference on the amended order item points to the correct original order item so that billing schedules stay consistent.

Usage-Based Products: For usage-based products, when the order item is excluded from billing, no billing schedule groups or billing schedules are created regardless of the binding type.

To configure this value when you create a treatment, see Create Billing Treatments.

=== ARTICLE: ind.billing_treatment_resolution.htm ===
---
article_id: ind.billing_treatment_resolution.htm
title: Understand Billing Treatment Resolution
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_treatment_resolution.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_policies_and_treatments.htm
fetched_at: 2026-09-04
---

# Understand Billing Treatment Resolution

The billing treatment field of an order product determines how it is billed. If the billing treatment is missing on the order product, an attempt is made to resolve the issue and assign an active billing treatment during the resolution.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Scenarios for Billing Treatment Selection

The billing policy for a product determines the billing treatment if it isn't explicitly defined for an order product. The billing admin defines billing treatments and a default billing treatment for a billing policy. The billing treatment is then assigned to the order product at runtime based on these scenarios.

Billing Treatment Selection	Scenario	Behavior
Default	An active default billing treatment is available for the billing policy.	Assigns the default billing treatment of the billing policy to the order product.
Manual	An active default billing treatment is available for the billing policy.	Assigns the default billing treatment of the billing policy to the order product.
Legal Entity	A legal entity is specified for the order product.	The order product’s legal entity is compared with the billing treatments in the billing policy. If a match exists, that billing treatment is assigned. Otherwise, the default billing treatment from the billing policy is used.
No legal entity is specified for the order product.	The default legal entity of the Salesforce org is compared with the billing treatments in the billing policy. If a match exists, that billing treatment is assigned. Otherwise, the default billing treatment from the billing policy is used.
Considerations

A default billing treatment is required when creating a billing policy. If a product doesn't have an associated billing policy, the default billing treatment defined for your Salesforce org is assigned. If no default billing treatment is defined for your Salesforce org, the billing calculation fails.

Only active billing policies and treatments are considered. If none exists, the billing calculation fails.

=== ARTICLE: ind.billing_understand_billing_suspensions_and_target_date.htm ===
---
article_id: ind.billing_understand_billing_suspensions_and_target_date.htm
title: Understand Billing Suspensions and Target Date
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_understand_billing_suspensions_and_target_date.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_suspend_and_resume_overview.htm
fetched_at: 2026-09-04
---

# Understand Billing Suspensions and Target Date

Learn how Billing evaluates suspensions when invoice runs and the Invoice Creation API use a target date or billing period count.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Deferred Charges

Suspending billing defers charges for the suspension period—it doesn’t waive them. Charges for the suspended period are billed when billing resumes or when a later invoice run uses a target date on or after the resumption date.

Target Date and Suspensions

When a run uses a target date, Billing evaluates billing suspensions as of that date, not the run date. Backdating suspensions isn’t required to prevent charges during that suspension period. Depending on where the target date falls relative to the suspension window:

Target date before the suspension starts: Invoicing proceeds as normal—the suspension has no effect yet.
Target date falls within the suspension window: Billing doesn’t create billing period items or generate an invoice for the suspended billing periods, even if the run date is before the suspension starts. If a billing schedule falls partially in the suspension window, Billing creates billing period items and invoices for the periods before the suspension start date. Invoice run responses can report that the account or billing schedule group is suspended, if there are no billing periods falling before the suspension window.
Target date falls on or after the resumption date: The invoice run bills all periods up through the target date, including the previously deferred charges from the suspension period, in the same run. The suspension has no effect on those invoices, because the target date is on or after the resumption date.
EXAMPLE You suspend billing for a monthly billing schedule group. The group’s next billing date is July 15, and Billing Day of Month is 15. You set the suspension date to September 10 and the resumption date to September 30. On July 15, you send a request to the Invoice Creation API with a target date of September 15.

Because the target date falls in the suspension window, Billing creates billing period items only for periods that end before the suspension starts—through August 15—and generates an invoice for those charges. The billing period item for the period that ends September 15 isn’t created, because that period overlaps the suspension window.

September charges are billed when a later invoice run uses a target date on or after September 30, or when you cancel the suspension and run invoicing again.

Billing Period Count and Suspensions

When an invoice run uses billing period count instead of a target date, Billing still evaluates suspension for each schedule separately. A suspended schedule isn’t invoiced for any period that falls in its suspension window.

What changes is which periods the run retrieves. A target date selects schedules up to a calendar date. Billing period count selects a fixed number of periods per schedule, so the period range can differ for schedules with different next billing dates.

Multiple Suspensions

If more than one suspension applies to the same account or billing schedule group, Billing uses the earliest suspension start date.

EXAMPLE Account Acme has a suspension from June 1 through June 15, and the related billing schedule group has a suspension from June 10 through June 30. Billing uses June 1 as the suspension start. An invoice run with a target date of June 12 doesn’t create billing period items for the suspended schedules.

=== ARTICLE: ind.billing_understand_period_boundaries_and_billing_day_of_month.htm ===
---
article_id: ind.billing_understand_period_boundaries_and_billing_day_of_month.htm
title: About Period Boundaries and Billing Day of Month
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_understand_period_boundaries_and_billing_day_of_month.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_frequency_change_flow_impact.htm
fetched_at: 2026-09-04
---

# About Period Boundaries and Billing Day of Month

You can adjust when billing periods start and how charges are calculated by using flexible date settings that align with your business model and customer preferences. You can use the Period Boundary, Period Boundary Day, and Period Boundary Start Month fields on the order product, to define when billing begins, how billing periods are segmented, and how proration is applied. The period boundary on the order product ‌defines how the billing period is calculated. The Billing Day of the Month field on the Billing Schedule record specifies the day you expect to bill the customer. Together, these fields define how billing periods align with the transaction timeline and how Billing in Revenue Management calculates and groups charges on invoice lines.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license
Period Boundaries and Their Impact on Billing Cycles

Consider monthly advance billing of an order product that starts on August 5 with period boundary set to anniversary. When the billing schedule is created, the next billing date is set to August 5.

Billing periods follow the order start date and run from August 5 to September 4, September 5 to October 4, and so on.

If the period boundary is set to align to calendar, the first billing period covers August 5 to August 31. After the first billing cycle, the next billing date is updated to September 1. Then, billing follows calendar months from that point onward, such as September 1 to September 30, October 1 to October 31, and so on.

If the period boundary is set to the last day of the period, the first billing period spans August 5 to August 30. The next billing date is then updated to August 31. Each new billing period starts the day after the previous one ends. It continues through the day before the next period begins.

If the period boundary is set to day of period, and the period boundary day is 8 with period boundary start month as August, then the first billing period spans from August 5 to August 7. The day of month offers greater flexibility because it allows you to define the exact day for the billing period to begin. For example, if you specify the day as 8, the first billing cycle covers August 5 to August 7. After that, the next billing date is set to August 8 and billing continues from the 8th day of each period based on the configured billing frequency.

For quarterly, semiannual, or annual billing frequencies, the period boundary, period boundary day, and period boundary start month fields work together to determine when billing cycles begin.

For example, take the same order starting on August 5 with billing frequency set to quarterly and period boundary set to anniversary. In this setup, the initial next billing date is August 5, and the first billing period runs from August 5 to November 4. Once this period ends, the next billing date shifts to November 5 and billing recurs every three months, such as from November 5 to February 4, February 5 to May 4, and so on.

Choose the Right Period Boundary for Your Billing Needs
PERIOD BOUNDARY	DESCRIPTION	BILLING SCENARIOS	USE CASE
Align to Calendar	Billing periods follow the calendar month or year.	

Useful when billing needs to align to standard calendar-based cycles, such as monthly or yearly.

	

Acme Company sells B2B cloud licenses and recognizes revenue annually. They configure the Period Boundary to Align to Calendar, with October as the Period Boundary Start Month. An order starts on August 1. The first billing period spans from August 1 to December 31. If the subscription ends early, say on November 2, the billing schedule adjusts to cover August 1 through November 2. Otherwise, starting January 1, billing continues in full annual periods. This setup ensures invoices and revenue schedules stay aligned with calendar-based business processes.


Anniversary	Billing periods align with the order start day.	

Ideal if customers expect billing to occur on the day the subscription began.

	

Acme Fitness supports multiple billing models to suit different customer needs. One of their clients uses anniversary-based billing period with a monthly billing frequency. When a customer signs up on August 10, their billing periods run from August 10 to September 9, September 10 to October 9, and so on. Each invoice covers one full month starting from the customer’s sign-up date, ensuring consistent and personalized billing throughout the subscription.


Day of Period	Billing begins on a specific day of the billing period. The billing period can be a month, quarter, semiannual, or annual.	

Recommended for use cases where customers want to be billed on a specific day in the billing period.

	

Acme Telecom sells termed products and prefers billing periods that align with standard quarterly cycles. For one such product, the billing period begins on August 1, 2025. It’s configured with Billing Frequency set to Quarterly, Period Boundary as Day of Period, Period Boundary Day as 1, and Period Boundary Start Month as March.

With this setup, quarterly billing periods are aligned to start in March, June, September, and December. The first billing period item covers the partial period from August 1 to August 31, before the regular quarterly cycle begins in September.


Last Day of Period	Billing periods end on the last day of each period, based on the order start date.	

Useful for companies that consolidate all charges and usage data before issuing a final invoice, especially when dealing with variable consumption or compliance rules.

	

Acme Insights, a data analytics platform, bills customers monthly based on the volume of data processed, with invoices generated on the last day of each billing period. For example, if a customer signs up on August 17, their billing periods run from August 17 to August 30, August 31 to September 29, September 30 to October 29, and so on. Invoices are issued on the last day of each billing period, such as August 30 or September 29, to ensure all data usage is captured before billing. This setup provides accurate and transparent invoicing aligned with each customer’s subscription start date and billing cycle.

Relation Between Billing Day of Month and Invoice Generation Day

The billing day of the month on the billing schedule determines the day invoices are generated for that month.

If billed in advance, invoices are generated at the start of each billing period.
If billed in arrears, invoices are generated on the last day of each billing period.

=== ARTICLE: ind.billing_understand_target_date_and_billing_period_count.htm ===
---
article_id: ind.billing_understand_target_date_and_billing_period_count.htm
title: Understand Invoice Date, Target Date, and Billing Period Count
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_understand_target_date_and_billing_period_count.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_automate_invoice_generation.htm
fetched_at: 2026-09-04
---

# Understand Invoice Date, Target Date, and Billing Period Count

Before you schedule invoice batch runs, learn how invoice dates are determined, how billing schedules are selected, and how many billing periods are processed for each schedule. You can also process a specific number of billing periods without relying on a target date.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

During an invoice batch run, Billing selects billing schedules, generates invoices from those schedules, and applies tax. Billing also selects schedules using the filter criteria on the invoice scheduler and a target date, billing period count, or both. It then creates invoices for those schedules. The invoice date is stamped on each invoice and is the date used to calculate tax. Estimated tax is calculated for draft invoices. Actual tax is calculated for posted invoices. See Invoice Batch Run Process and Tax Calculation Process.

Use this table to compare invoice date, target date, and billing period count. You can set a target date, a billing period count, or both.

OPTION	WHAT IT DOES	WHEN TO USE
Invoice Date	Date stamped on the invoice and used for tax calculation.	Always set
Target Date	Selects which billing schedules to invoice.	When you want to invoice schedules through a specific date.
Billing Period Count	Caps how many periods are invoiced per schedule.	When you want to limit the number of periods invoiced per schedule.

You can select billing schedules using a target date, billing period count, or both, regardless of the invoice batch run frequency. The run frequency only affects how you specify or calculate the target date and invoice date.

Invoice Date

The invoice date is the date stamped on an invoice and used for tax calculation. For a one-time invoice batch run, you specify the invoice date directly. For recurring runs, Billing determines the invoice date by adding an invoice date offset to either the target date or the run date.

The invoice date offset is the number of days Billing adds to or subtracts from the selected date. A positive offset produces a date after the selected date, a negative offset produces a date before the selected date, and an offset of 0 uses the selected date as the invoice date. Base invoice date on determines whether Billing applies the offset to the target date or the run date.

When you base the invoice date on the target date, Billing adds the invoice date offset to the target date. For example, if the target date is August 23, an offset of 0 makes the invoice date August 23, an offset of 3 makes the invoice date August 26, and an offset of –3 makes the invoice date August 20.

When you base the invoice date on the run date, Billing adds the invoice date offset to the date the invoice batch run runs. For example, if the invoice batch run runs on July 23, an offset of 0 makes the invoice date July 23, an offset of 3 makes the invoice date July 26, and an offset of –3 makes the invoice date July 20.

Target Date

The target date tells Billing which billing schedules to invoice. Billing invoices a schedule when its next billing date is on or before the target date and the schedule matches the filter criteria on the invoice scheduler. When no target date is set, Billing invoices every schedule that matches those filters.

Use a target date when you want to invoice selected billing schedules through a specific date. For example, if the selected schedules are billed monthly, a target date of June 1 invoices those schedules with a next billing date on or before June 1.

For a one-time run, you specify the target date directly. For recurring invoice batch runs, Billing determines the target date from either the run date or a calendar day of the month. Base target date on chooses which of these dates to use.

When you base the target date on the run date, a positive offset produces a target date after the run date, a negative offset produces a target date before the run date, and an offset of 0 uses the run date as the target date. For example, if the invoice batch run executes on July 23, an offset of 0 makes the target date July 23, an offset of 3 makes the target date July 26, and an offset of –7 makes the target date July 16.

In some complex billing scenarios, businesses don’t have a fixed day offset. Instead they work with a flexible date like the Nth day of the coming month. When you base the target date on a calendar day of the month, Billing determines the target date from the target day of month and target month offset. The target day of month can be 1 through 28, or the last, second-to-last, or third-to-last day of the month. The target month offset is the number of months added to or subtracted from the month of the invoice batch run. For example, a monthly invoice batch run on July 23 with a target day of month of 23 and a target month offset of 1 has a target date of August 23.

NOTE For milestone billing, the target date determines which accomplished milestones are invoiced. When no target date is set, Billing uses the run date of the invoice batch run so that future milestones aren’t invoiced. Usage billing schedules with liable summaries in Ready for Invoicing status are always invoiced, regardless of the target date. The Milestone Billing and Usage-Based Invoicing features are available only with the Revenue Management Billing license.
Billing Period Count

When schedules have different next billing dates, using a fixed target date to select all of them can cause some schedules to be invoiced for extra billing periods. This can result in over-billing.

Billing period count specifies how many billing periods to process for each selected schedule, from 1 through 12. Each schedule is invoiced for the specified number of periods, even when schedules have different next billing dates or billing period lengths.

Use billing period count with a target date when you want to limit which schedules are invoiced and specify how many billing periods to invoice for each schedule. Each selected schedule is invoiced for the specified number of periods or through its end date, whichever comes first.

You can also use billing period count without a target date when you want to invoice every schedule that matches the invoice scheduler's filter criteria for a specific number of periods. For example, to invoice every matching schedule for the next two billing periods, set billing period count to 2.

NOTE Billing period count doesn’t apply to milestone or usage billing schedules. For milestone billing, the target date determines which milestones are invoiced. Usage billing invoices all Ready for Invoicing usage records. The Milestone Billing and Usage-Based Invoicing features are available only with the Revenue Management Billing license.

To create an invoice scheduler after you choose these options, see Generate Invoices Automatically Based on Billing Schedules.

EXAMPLE

You have a monthly schedule with a next billing date of April 1 and a quarterly schedule with a next billing date of June 1. A target date of June 1 without a billing period count invoices the monthly schedule for three monthly periods instead of one.

With billing period count set to 1, each schedule is invoiced for one period: April 1 to May 1 for the monthly schedule and June 1 to September 1 for the quarterly schedule.

=== ARTICLE: ind.billing_unreferenced_refunds.htm ===
---
article_id: ind.billing_unreferenced_refunds.htm
title: Refund Available Credit Balances to Customer Accounts
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_unreferenced_refunds.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_refunds_overview.htm
fetched_at: 2026-09-04
---

# Refund Available Credit Balances to Customer Accounts

Refund a customer’s available credit balance against a credit memo or credit memo line without referencing an original payment.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Header-Level and Line-Level Application

The refund application level determines how Billing applies a refund to a credit memo. In Setup, find and select Billing Settings. In the Credits, Payments, and Refunds section, set Credit, Payment, and Refund Application to the level you want. Select Header Level to refund against credit memos, or Line Level to refund against credit memo lines.

With header-level application, the refund amount applies to the credit memo as a whole. Billing creates a junction record, reduces the credit memo’s pending balance by the refund amount, and sets the refund balance to zero.
With line-level application, Billing distributes the refund amount across the credit memo lines that have an open balance, starting with the line that has the largest open balance, and reduces each line’s balance to zero. Because line-level application distributes the refund automatically, you enter the total refund amount once and Billing allocates it across the lines.
How Billing Resolves the Payment Method

Billing pays an unreferenced refund to a saved payment method. To determine the saved payment method, Billing checks the sources in this order.

First, the payment method that’s passed directly in the API request.
Next, the saved payment method that’s stamped on the credit memo.
Finally, the saved payment method resolved from the associated billing account or billing arrangement.
Synchronous and Asynchronous Payment Gateways

The payment gateway determines when a refund reaches its final status. A synchronous gateway returns a response immediately, so the refund status changes to Processed and Billing applies the refund to the credit memo. An asynchronous gateway doesn’t return an immediate response, so the refund status stays in Pending status. When the gateway confirms the refund, the status changes to Processed and Billing applies the refund to the credit memo.

Issue Refund Against a Credit Memo
Return an available credit balance to a customer by issuing a refund against a credit memo, paid to a saved payment method on a third-party gateway.

=== ARTICLE: ind.billing_view_billing_sched_group.htm ===
---
article_id: ind.billing_view_billing_sched_group.htm
title: Generated Billing Schedule Details
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_view_billing_sched_group.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_schedules_and_schedule_groups.htm
fetched_at: 2026-09-04
---

# Generated Billing Schedule Details

View all the key billing schedule and invoice details in the Billing Schedule Group records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with Revenue Management


This feature is available with the Revenue Management Advanced license or the Revenue Management Billing license.

The Usage Management feature is only available with the the Revenue Management Billing license. Contact your Salesforce account executive for more information.

From the App Launcher, find and select Billing, and then click Billing Schedule Groups. Open any Billing Schedule Group record to view all the required details.

Asset of the Billing Schedule Group

The asset related to the order for which the billing schedule group is created appears on the Asset field of the Billing Schedule Group record.

Billing Schedule Timeline

The Billing Schedule Details component shows the billing schedules in a billing schedule group, including summary metrics, a visual timeline of start and end dates, and billing period details. Billing operations teams use the timeline to evaluate billing outcomes. Sales teams use it to demonstrate complex billing.

When the component is on the Billing Schedule Group page, a timeline of the group’s billing schedules appears beneath these summary metrics.

Total Billing Schedules
Total Amendments
Percentage Billed
Total Billed Amount
Total Pending Amount

By default, the timeline spans from the earliest start date to the latest end date. For evergreen billing schedules, the range extends 12 months past the latest date. Each row represents a billing schedule. The bar spans the billing schedule’s start and end dates, and its color reflects the billing schedule’s state.

Active
Suspended
Canceled
Evergreen

Next to each schedule’s name, a tag shows its category, such as Original, Renewal, Amendment, or Cancellation, along with its quantity. The end of each bar shows the billing period amount and the billing frequency, such as / Month or / Annual. One-time billing schedules show (One-Time). Milestone plans show the amount followed by (Milestone Plan). Click the expand icon on a row to view these details.

Billing amount details: Total amount, billed amount, pending amount, period amount, quantity, unit price, and net unit price.
Billing date details: Start date, end date, next billing date, billing type, billing method, billing term, and billing term unit.
Billing progress: Shown as a percentage.

To change the timeline date range, click the Set Date Range icon, enter a start date and an end date, and then click Apply. This filter doesn’t change the summary metrics. Click a billing schedule’s name to open its record.

To add the component to a Billing Schedule Group page, see Add the Billing Schedule Details Component to a Group Page.

Billing Schedules for Original, Amended, Renewed, and Canceled Assets

The Billing Schedules related list of a Billing Schedule Group record shows all the billing schedules for original, amended, canceled, and renewed assets. The Billing Schedules tab also shows the same billing schedules with additional details that help you identify and differentiate between them easily.

The billing schedules for original, amended, renewed, or canceled assets are created with the corresponding category.

The billing schedules created for amended or canceled assets have a reference to the original billing schedule that they’re related to.
When you cancel an asset, the cancellation date is populated for all the billing schedules that are related to the billing schedule group for the asset.
EXAMPLE

These examples illustrate the process of how amending and canceling assets affect the creation of billing schedules.

Asset Amendment Scenario: SmartBytes is a large enterprise company that uses Revenue Management. One of its longstanding customers, Greenfield Enterprises, wants to purchase 10 more SmartBytes’ DocuCraft software licenses to cater to a rising employee demand. SmartBytes’ sales operations representative amends Greenfield Enterprises’ existing asset for DocuCraft software licenses to include 10 more licenses. On amending the asset, an amendment quote is created. The sales representative then creates an order for the amendment quote and activates it. On activating the order, a billing schedule is created for 10 licenses with Amendment as the category. The billing schedule is also linked to the billing schedule created for the initial asset.

Asset Cancellation Scenario: One of SmartBytes customers, TechCore Solutions, wants to cancel their ongoing order for DocuCraft software. SmartBytes’ sales operations representative cancels TechCore Solutions’ existing asset for DocuCraft software licenses. On canceling the asset, a cancellation quote is created. The sales representative then creates an order for the cancellation quote and activates it. On activating the order, a billing schedule is created with Cancellation as the category. The billing schedule is also linked to the billing schedule created for the initial asset.

Billing Schedules for Orders and Quotes With Future-Dated Changes

Billing automatically generates billing schedules when termed products are amended or renewed before or after future-dated orders or quotes. Any future-dated renewals on one-time and evergreen products are considered as amendments on the associated orders or quotes.

When you cancel an asset before or after the start of a future-dated amendment, Billing automatically generates billing schedules to reflect the correct quantity across different time periods.

When a future-dated amendment, renewal, or cancellation is rolled back before it takes effect, Billing doesn’t modify existing billing schedules. Instead, Billing creates compensating adjustment billing schedules that offset the impact of the rolled-back change. The original billing schedules are retained for historical accuracy, ensuring that future billing reflects the correct amounts and periods while preserving a complete audit trail.

Billing Schedules for Usage-Based Products

For usage-based products and add-on packs, billing schedules are ready for invoicing when the rated usage and overage charges are calculated.

See Track Product Usage and Consumption in Revenue Cloud.

Billing Schedules for Ramped Products

For ramped products, Billing automatically creates a billing schedule group for the asset and individual billing schedules for each ramp segment.

Billing Schedules for Price Changes

For evergreen, one-time, and termed products, Billing automatically generates billing schedules whenever a discount amount or discount percentage is applied on the associated quote or order.

Billing Schedules for Swapped Products

For evergreen, one-time, bundled, and termed products, Billing automatically generates billing schedules for the swapped in and swapped out products during various swap scenarios including and not limited to.

Swap from an evergreen to termed, termed to one-time, or one-time to evergreen product
Swap a bundled product with one or more single products
Swap products during the middle of a billing period
Swap products with different billing frequencies
Swap partial quantities of the same product
Billing Schedules for Updated Subscription End Dates

When a customer changes the end date of a subscription for an order, the related billing schedules are automatically updated to reflect the new service period. Billing regenerates billing schedules during amendments to ensure billing periods are accurate.

Billing Schedules for Billing Milestone Plans

When a billing treatment is configured for milestone-based billing, Billing creates a billing milestone plan and links it to the billing schedule. Billing generates the invoice lines based on the configured milestones.

Main and Associated Billing Schedule Groups

In an order, related products are grouped in a bundle. These order bundles are displayed in a hierarchy to highlight the difference between related and independent products of the order. When billing schedule groups are created for bundled products of an order, billing schedule groups are created for the root bundle product and for each child product. Each order bundle corresponds to a billing schedule bundle.

On the Billing Schedule Group record that’s created for a root bundle product, the billing schedule groups that are created for the child products appear in the Associated Billing Schedule Group related list.

On the Billing Schedule Group record that’s created for a child product, the billing schedule group that's created for the root bundle product appears in the Main Billing Schedule Group related list.

Billing History Tab

The Billing History tab shows all the billing period items, billing milestone plan items, invoice lines, and revenue transaction error logs that are related to the billing schedule group.

View the related billing period items to track the billing schedules that were processed and the expected amount to be billed for an invoice.
View all the billing milestone plan items for the product to understand the status of the project milestones and the milestone amount.
View all the invoice lines that are generated for the product.
Troubleshoot invoice batch run errors by accessing all the revenue transaction error logs for a billing schedule group in a single place.
Preview Invoices Tab

You can generate up to two invoice previews for the billing schedule group. The billing schedule group’s effective next billing date is preselected as the start date for the invoice preview.

See Generate Invoice Previews for Billing Schedule Groups.

Relationships Graph

In addition to the Related tab, the Relationships Actionable Relationship Center (ARC) graph also shows the associated and main billing schedule groups. If the billing schedule group is for a usage-based product, the graph also shows the billing schedule groups for the valid product usage grants of the same product.

Quantity and Unit of Measure

Billing schedules inherit their quantity and unit of measure from the related order products’ quantity and unit of measure. A billing schedule’s quantity is rounded off based on the scale and rounding method of its unit of measure.

See View and Edit Orders in Revenue Management and Decimal Quantity Support in Product Catalog Management.

Start and End Dates

Billing prioritizes the start and end dates found on Quote Line Detail and Order Item Detail records. If no dates are specified on the detail records, then Billing uses the dates from the parent order or quote item.

=== ARTICLE: ind.billing_void_taxes.htm ===
---
article_id: ind.billing_void_taxes.htm
title: Tax Implications of Invoice Voids
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_void_taxes.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_invoices_void.htm
fetched_at: 2026-09-04
---

# Tax Implications of Invoice Voids

Learn how voiding an invoice cancels its associated taxes and affects the status of related credit memos.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Advanced license or the Revenue Cloud Billing license

When you void a posted invoice, the Tax Calculation API calls out a tax engine to void or adjust the tax. The status of the related credit memo depends on the tax engine’s response, which varies based on the invoice’s line types. This table shows invoice line types along with tax engine responses and corresponding credit memo statuses.

INVOICE LINE TYPE	TAX ENGINE RESPONSE	CREDIT MEMO STATUS
All positive invoice lines	Void	Voided
All positive invoice lines	Credit	Posted
All negative invoice lines	Void	Voided
All negative invoice lines	Debit	Posted

When you void an invoice that contains both positive and negative invoice lines, Tax Calculation API makes two tax call-outs to the tax engine. This table shows the tax engine response for positive and negative invoice lines and the corresponding credit memo status.

TAX ENGINE RESPONSE FOR POSITIVE INVOICE LINES	TAX ENGINE RESPONSE FOR NEGATIVE INVOICE LINES	CREDIT MEMO STATUS
Void	Void	Voided
Credit	Void	Voided
Void	Debit	Voided
Credit	Debit	Posted

=== ARTICLE: ind.billing_write_off_invoice_balance.htm ===
---
article_id: ind.billing_write_off_invoice_balance.htm
title: Write Off Invoices
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_write_off_invoice_balance.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing.htm
fetched_at: 2026-09-04
---

# Write Off Invoices

Write off unpaid or partially paid invoices when the balance on the invoice is deemed uncollectible. To maintain accurate accounting, the system automatically creates and applies credit memos to write off the uncollectible balance on the invoice.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
Write Off Invoices by Using Invocable Action in Flow
Invoke the Write Off Invoices action in a flow to write off invoices.
Impact of Invoice Write-Offs
Invoices are written off by creating and applying credit memos to settle invoices. These credit memos are applied to the invoice or invoice lines based on the credit application level on the Billing Settings page.

=== ARTICLE: ind.billing_write_off_invoices_impact.htm ===
---
article_id: ind.billing_write_off_invoices_impact.htm
title: Impact of Invoice Write-Offs
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_write_off_invoices_impact.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_write_off_invoice_balance.htm
fetched_at: 2026-09-04
---

# Impact of Invoice Write-Offs

Invoices are written off by creating and applying credit memos to settle invoices. These credit memos are applied to the invoice or invoice lines based on the credit application level on the Billing Settings page.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.

The write-off process triggers specific updates to relevant records and fields.

On the Invoice record, the Write Off Status, Write Off Charge Amount, and Write Off Tax Amount fields are updated.
On the Credit Memo record, the Credit Memo Reason Code field is updated.
On the Credit Memo record, if the Reason was provided, it is populated on the Description field.

After an invoice is successfully written-off, you can't apply or unapply any further credit memos or payments to that invoice.

You can also use Write-Off API to write off invoices.

=== ARTICLE: ind.billing_write_off_invoices_invoke_action.htm ===
---
article_id: ind.billing_write_off_invoices_invoke_action.htm
title: Write Off Invoices by Using Invocable Action in Flow
source_url: https://help.salesforce.com/s/articleView?id=ind.billing_write_off_invoices_invoke_action.htm&type=5&release=264
release: 264
release_name: Winter '27
area: billing
parent_article: ind.billing_write_off_invoice_balance.htm
fetched_at: 2026-09-04
---

# Write Off Invoices by Using Invocable Action in Flow

Invoke the Write Off Invoices action in a flow to write off invoices.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions with the Revenue Cloud Billing license. Contact your Salesforce account executive for more information.
USER PERMISSIONS NEEDED
To write off invoices by using invocable action:	

Billing Operations User permission set

Or

Credit Memo Operations User permission set

Before you use the write-off process, go to the Object Manager and add all the required values to the Reason Code picklist field on the Credit Memo object. Add values such as BD for bad debt charges.

Create a screen flow, define the these variables to use as the input and output for the action.

Create WriteOffInvoiceInputList resource.
Select Variable as the resource type.
Enter WriteOffInvoiceInputList as the API name.
Select Apex-defined as the data type.
Select InvoiceWriteOff__WriteOffInvoiceInputList as the apex class.
Create WriteOffInvoiceInput resource.
Select Variable as the resource type.
Enter WriteOffInvoiceInput as the API name.
Select Apex-defined as the data type.
Select InvoiceWriteOff__WriteOffInvoiceInput as the apex class.
You can create multiple input resources as required.
Specify invoiceId, reasonCode, and reason as the API names for the input variables of text data type.

reasonCode is a required value but reason is optional.

Add an Assignment element and assign the text data type variables as values to the Apex-defined data type variables of the WriteOffInvoiceInput resource.
Add an Assignment element and add WriteOffInvoiceInput resource to WriteOffInvoiceInputList.
If you have created multiple WriteOffInvoiceInputs, click Add Assignment and add them all to the WriteOffInvoiceInputList in the same element.
Repeat the steps to create WriteOffInvoiceResponse and WriteOffInvoiceResponseList resources and assign WriteOffInvoiceResponse to WriteOffInvoiceResponseList resource.
Alternatively, you can also create a Loop element for WriteOffInvoiceResponseList resource.
Add an Action element, find and select writeOffInvoices-writeOffInvoices action.
Select the writeOffInvoiceInputList input value as the writeOffInvoiceInputList.
Select the writeOffInvoiceResponseList output value as the writeOffInvoiceResponseList.
Activate the flow.

After activating the flow, create and add a quick action to the invoice page layout and use the invocable action.

