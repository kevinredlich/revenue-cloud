# Salesforce Help 264 — área: approvals (43 artículos)

=== ARTICLE: ind.approvals_add_an_approval_button_for_sales_reps.htm ===
---
article_id: ind.approvals_add_an_approval_button_for_sales_reps.htm
title: "Example: Add an Approval Button on a Record Page"
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_add_an_approval_button_for_sales_reps.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_design_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Example: Add an Approval Button on a Record Page

Add a button that users can click to submit a record for approval. Let’s see an example for adding a button on the quote page.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions of Revenue Management (formerly Revenue Cloud) where Transaction Management is enabled
NOTE In an autolaunched flow triggered by a quick action, $User resolves to the Automated Process User, not to the submitting user. If your flow needs details about the submitting user, use the Visualforce page and Apex controller approach to pass that information into the flow as an input variable. You can’t hard code the User, Group, or Queue ID in a packaged orchestration. See Revenue Cloud Advanced Approvals: Cannot deploy or package Flow Orchestration with User, Group, or Queue assignee type.

To add an approval button, follow the instructions in each of these sections.

Create an Apex Class

Follow these steps to create and use the QuoteApprovalController Apex class, which begins the approval workflows.

From Setup, search for and select Apex Classes.
Click New.
In the class editor, enter the Apex code for the class.
public class QuoteApprovalController {
    private Id quoteId;
    private String userId;
    public String submitterComments { get; set; }
   
    public QuoteApprovalController(ApexPages.StandardController controller) {
        Quote quote = (Quote) controller.getRecord();
        quoteId = quote.Id;
        userId = UserInfo.getUserId();
    }
    
    public void submitQuoteForApproval() {
        String flowApiName = 'Approval_Autolaunched_Flow';
        Map<String, Object> inputs = new Map<String, Object>();
        inputs.put('recordId', quoteId);
        inputs.put('submitter', userId);
        inputs.put('submissionComments', submitterComments);
        Flow.Interview myFlow = Flow.Interview.createInterview(flowApiName, inputs);
        myFlow.start();
    }
}

Save your changes.
Create a Visualforce Page

Follow these steps to create a Visualforce page called QuoteApprovalPage to trigger the Apex class.

From Setup, search for and select Visualforce Pages.
Click New.
Enter QuoteApprovalPage as the label and name.
Select Available for Salesforce mobile apps and Require CSRF protection on GET requests.
In the Visualforce Markup text box, enter Visualforce markup for the page.
<apex:page standardController="Quote" extensions="QuoteApprovalController" showQuickActionVfHeader="false" lightningStylesheets="true">
    <script>
        function closePopupWindow() {
            if (typeof sforce != 'undefined' && sforce && sforce.one) {
                var quoteId = '{!Quote.Id}';
                sforce.one.navigateToSObject(quoteId);
            } else {
                window.close();
            }
        }
    </script>
    <h2 align='center'>
        Submit for Approval
    </h2>
   <apex:form >
        <apex:pageBlock >
            <apex:pageBlockButtons location="bottom">
                <p align='left'>Enter comments for Approver(s):</p>
                <p align='center'><apex:inputTextarea value="{!submitterComments}" cols="100"/></p>          
                <apex:commandButton value="Submit" action="{!submitQuoteForApproval}" oncomplete="closePopupWindow();" /> 
            </apex:pageBlockButtons>
        </apex:pageBlock>
    </apex:form>
</apex:page>

Save your changes.
From Setup, search for and select Visualforce Pages.
Click Security against the QuoteApprovalPage.
Add your sales reps profiles to enable access to the Visualforce pages.
Create a Custom Action

Follow these steps to create a custom action on an object. For example, let’s create this custom action on the Quote object.

From the Object Manager, search for and select Quote.
Select Buttons, Links, and Actions.
Click New Action and specify these details.
Action Type: Custom Visualforce
Visualforce Page: QuoteApprovalPage
Label: Request for Approval
Name: Request_for_Approval
Save your changes.
Modify Page Layout of the Object

Follow these steps to add the newly created action, Submit for Approval to the page layout of the Quote object.

On the Quote object settings page, click Page Layouts.
Select Quote Layout.
In the palette, click Mobile & Lightning Actions.
Drag Submit for Approval to the Salesforce Mobile and Lightning Experience Actions section in the layout.
Save your changes.

=== ARTICLE: ind.approvals_add_partners_to_approval_steps.htm ===
---
article_id: ind.approvals_add_partners_to_approval_steps.htm
title: Advanced Approval Objects
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_add_partners_to_approval_steps.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_manage_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Advanced Approval Objects

Learn about the objects and list views available in Advanced Approvals.

OBJECT	FUNCTIONALITY
Approval Submission	Represents the master record of an approval request, tracking its overall progress and storing the requests assigned to various reviewers.
Approval Work Item	Represents an approval step assigned to a specific user, group, or queue. It tracks the step's status and stores the reviewer's final decision, such as Approved or Rejected.
Approval Submission Detail	Stores a detailed audit trail for the entire approval process, logging every change on the main request or any of its individual tasks.
Approval Work Item Criteria	Represents the approval logic for the workflow. It contains the logical conditions used to evaluate the entry and exit criteria for each approval step.
Approval Work Item Condition	Stores the outcome of the approval logic, including the entry and exit conditions evaluated for every approval step.
Record Sharing

By default, any user with access to an approval submission has access to all its associated approval work items. To limit visibility, in Sharing Settings, set the sharing default of the Approval Work Item object to Private. This setting prevents reviewers at one step from seeing the work items assigned to reviewers at other steps. Reviewers also see only the work items that they're directly assigned or delegated to.

The owner and submitter of the approval submission can view the associated work items but can't review or reassign them.

To extend access to other users of the approval work item, create criteria-based sharing rules. See Create Criteria-Based Sharing Rules.

Default List Views

Based on record access, the following lists are available to users. Customize these lists by updating filter criteria or displayed columns. You can also create a new list view or clone an existing one to suit your needs.

All Approval Submissions: All submission records that you have access to, irrespective of the record's status.
My Approval Submissions: All submission records that are assigned to you.
Pending Approval Submissions: All submission records awaiting review that you have access to.
All Approval Work Items: All work item records that you have access to, irrespective of the record's status.
Assigned Approval Work Items: All work item records awaiting your review, including those assigned through groups, queues, or delegations.
All Approval Submission Details: All submission detail records that you have access to.
SEE ALSO
Data Model Gallery: Revenue Management Advanced Approvals Data Model
Considerations for Approval Objects
Considerations for Approval List Views

=== ARTICLE: ind.approvals_advanced_approvals.htm ===
---
article_id: ind.approvals_advanced_approvals.htm
title: Advanced Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_advanced_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
fetched_at: 2026-09-07
---

# Advanced Approvals

Advanced Approvals in Revenue Management (formerly Revenue Cloud) provides a streamlined platform to ensure complex business processes are consistent, compliant, and adhere to business policies.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
NOTE Revenue Cloud is now Revenue Management. You may see references to Revenue Cloud in Salesforce applications and documentation.

Design tailored, multi-step approval workflows for any supported object, including quotes, orders, or custom objects. Configure both sequential and parallel approval chains to ensure all required authorizations are completed before a record progresses.

A centralized Approvals app enables reviewers and submitters to efficiently manage, track, and respond to approval requests. Built-in audit trails and real-time notifications provide clear visibility into approval status, improving transparency and helping records move forward without delays.

This functionality is powered by Flow Orchestration, which coordinates complex, multi-team workflows and supports defined steps, conditional logic, and pauses for user input. As a result, the same limitations and best practices that apply to Flow Orchestration also apply to Advanced Approvals.

Begin Using Advanced Approvals
To efficiently set up and manage your approval strategies, first configure the experience for your team by creating users and assigning permissions based on their persona. Once your users are prepared with the correct access, you must complete the recommended base configuration from the Approvals Settings page to activate the features.
Customize Pages for Approvals
Customize approval and related pages with Lightning components, related lists, and custom actions that help trigger, monitor, and review approvals.
Design an Approval Workflow
Approval workflows enable businesses to implement complex, multi-step approval rules and efficiently manage transaction compliance.
Preview Approvals
Review the steps, chains, and approvers for a record before you submit it. Preview Approvals evaluates the record's field values and simulates the approval steps triggered. During the preview, approval-related records aren’t created or modified.
Advanced Approval Delegation
With Advanced Approval Delegation, reviewers can hand off their approval responsibilities to another user, group, or queue for a set period or indefinitely.
Approvals in Slack
With Approvals in Slack, approvers can approve or reject requests and add comments without leaving Slack, while submitters receive real-time updates on their requests. Your Slack actions are saved to Salesforce, so approval data stays consistent across channels.
Email Templates in Advanced Approvals
In an approval workflow, a request passes through multiple stages and reviewers. To provide reviewers and submitters clear and contextual information in their emails, create custom email templates for different notification reasons.
Advanced Approvals Considerations
This topic details known limitations, system boundaries, and common troubleshooting scenarios for the Advanced Approvals feature.

=== ARTICLE: ind.approvals_advanced_approvals_considerations.htm ===
---
article_id: ind.approvals_advanced_approvals_considerations.htm
title: Advanced Approvals Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_advanced_approvals_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Advanced Approvals Considerations

This topic details known limitations, system boundaries, and common troubleshooting scenarios for the Advanced Approvals feature.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Considerations for Approval Objects
This section covers considerations and limitations for approval objects and related records.
Environment & Setup
This section covers the limitations related to core setup and environment configuration.
Design, Build, and Activation
This section covers rules, constraints, and errors you might encounter while designing, building, and activating your approval processes.
Approval Process Execution
This section covers errors and expected behaviors that occur after a flow is activated and in use.
User Interface, Component, and List View Behavior
This section covers known behaviors and limitations for front-end components and list views.
Preview Approvals Considerations
Keep these considerations in mind when working with Preview Approvals.
Considerations for Advanced Approval Delegations
Keep these considerations in mind when working with approval delegation.
Considerations for Emails in Advanced Approvals
Keep these considerations in mind when working with approval emails and notifications.
Considerations for Approvals in Slack
Keep these considerations in mind when working with approvals in Slack.
Smart Approval Limitations
This section covers eligibility rules and known constraints for the Smart Approvals feature.

=== ARTICLE: ind.approvals_approval_delegation.htm ===
---
article_id: ind.approvals_approval_delegation.htm
title: Advanced Approval Delegation
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_approval_delegation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Advanced Approval Delegation

With Advanced Approval Delegation, reviewers can hand off their approval responsibilities to another user, group, or queue for a set period or indefinitely.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled

When a reviewer is unavailable, approval work items can stall a workflow. With Advanced Approval Delegation, reviewers redirect their approval responsibilities to another user, group, or queue for a set period or indefinitely. During an active delegation, delegates receive email notifications and review and act on approval work items on behalf of the original reviewer.

To find and manage delegation records, use these list views on the Approval Delegation object.

Approval Delegations from Me: Shows delegations that you set up.
Approval Delegations for Me: Shows delegations where you’re the designated delegate.
All Approval Delegations: Shows all delegation records in the org.

To view approval work items assigned to you as a delegate, use the Delegated Approval Work Items list view on the Approval Work Item object.

Turn On Advanced Approval Delegation
Give reviewers the ability to delegate their approval responsibilities to another user, group, or queue for a set period or indefinitely.
Create Approval Delegation Records
Set up approval coverage by specifying who handles your approval responsibilities and for how long.

=== ARTICLE: ind.approvals_approval_process_execution.htm ===
---
article_id: ind.approvals_approval_process_execution.htm
title: Approval Process Execution
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_approval_process_execution.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Approval Process Execution

This section covers errors and expected behaviors that occur after a flow is activated and in use.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Execution Errors

When a flow execution results in an errored state, this is often due to multiple steps trying to lock the same record simultaneously or because of issues rendering the Work Item screen guide. Administrators should be directed to review the flow in Paused and Failed Interviews within Setup or check the error email sent to the admin user for specific troubleshooting details.

Multiple Reviewers Conflict

A user may receive an error stating a work item is already completed if they attempt to review it at the same time as another member of their group or queue. The system correctly processes the first user's completion request and rejects the second user's request. No action is required as this is normal system operation.

=== ARTICLE: ind.approvals_building_blocks_of_advanced_approvals.htm ===
---
article_id: ind.approvals_building_blocks_of_advanced_approvals.htm
title: Design an Approval Workflow
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_building_blocks_of_advanced_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Design an Approval Workflow

Approval workflows enable businesses to implement complex, multi-step approval rules and efficiently manage transaction compliance.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled

This functionality leverages the Flow Orchestration engine, which manages and coordinates these approval processes, providing a flexible and powerful way to manage both simple and complex approval scenarios of the Flow Approval Process Type.

Approval workflows manage processes using your organization's staffing structure. They link together different Salesforce Flows, assign tasks to various people or queues, and automatically manage the handoffs and sequencing of work. These workflows are made up of sequential or parallel steps, and you can easily configure them to create smart, flexible governance strategies that span multiple teams (like Sales, Finance, and Legal). Furthermore, the process can pause to await user input and provides clear audit tracking, simplifying the understanding and management of complex approvals.

Before you design an approval workflow, we recommend you understand the fundamental details about the Flow Approval Process.

Building Blocks of Flow Approval Processes
Flow Approval Processes Concepts
Build a Flow Approval Process

You can create flow approval processes in Flow Builder, including the autolaunched flow from the Approvals app on your org or the Flow Approval Process from Setup.

Create a Draft Autolaunched Flow Approval Process
Create a Flow Approval Process from Scratch
Approval Workflow Types
You can implement approvals in your workflow using two primary methods: serial or parallel. These are managed by setting up an approval chain, which is a label that identifies the specific group and sequence of approvers for a given process.
Smart Approvals and Rule-Based Auto-Approvals
Smart Approvals and Rule-Based Auto-Approvals speed up resubmissions by auto-approving steps that don’t need another manual review. They differ in how the auto-approval decision is made and the level of control you have over that decision.
Example: Configure an Approval Workflow
Let’s build a complete approval workflow to determine the approvals required on a quote’s discounts, implementing both Smart Approvals and Dynamic Approval Notifications.
Use the Stage Exit Condition
Serial and approval workflows can easily get stuck in a “waiting” state if the Stage element's exit condition isn't configured properly. The problem occurs when the stage is set to wait for all steps to finish, as it can't account for conditional steps that were never triggered. This creates a deadlock.
Flow Core Action: Override Approval Work Item
Update the status of an approval work item to reflect the approval admin's decision, allowing admins to override the decision for any assignee.
Use Advanced Approvals in a Quote
Now that your Approval Designer has created and activated an approval workflow for discounts, you’re ready to create quotes as a sales rep and use it.

=== ARTICLE: ind.approvals_create_a_flow_to_update_records.htm ===
---
article_id: ind.approvals_create_a_flow_to_update_records.htm
title: User Interface, Component, and List View Behavior
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_create_a_flow_to_update_records.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# User Interface, Component, and List View Behavior

This section covers known behaviors and limitations for front-end components and list views.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Approval Trace Component

The Approval Trace component is a predefined, locked tool that you can’t customize.

The component shows only the record that’s associated with the approval submission. It doesn’t show details for its related records. For example, if you submit an approval for a quote line item, the Approval Trace component doesn’t show the work items associated with the parent quote. If your business requires extended visibility from a single page, redesign the approval flow.

Approval List Views
You can’t modify the filters in the Assigned Approval Work Items list view.
Custom list views cannot filter approval work items by ownership because the Approval Work Item object lacks an Owner field. To view the work items assigned to you, use the Assigned Approval Work Items list view.
You can't modify the sharing settings of the default list views in Advanced Approvals.
You can't delete any default list view in Advanced Approvals.
Approval Object Page Layout Customization

You can't customize the layout of the Approval object pages before the records are created.

To override the default page layout for objects, you can do the following.

Viewing a record after creation activates the default page layout.
From the App Launcher, search for any Approval object. Change the view to a List View, then click on any record. When you click the Details tab, the object's page layout is activated.

=== ARTICLE: ind.approvals_create_approval_alert_content_definition_records.htm ===
---
article_id: ind.approvals_create_approval_alert_content_definition_records.htm
title: Create Approval Alert Content Definition Records
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_create_approval_alert_content_definition_records.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_email_templates.htm
fetched_at: 2026-09-07
---

# Create Approval Alert Content Definition Records

To map a custom email template to notification reasons, create an approval alert content definition.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To turn on email settings:	Customize Application
To create approval alert content definition records:	

Approval Admin

OR

Approval Designer

Before you begin, make sure that you complete these prerequisites.

Create email templates for different notification reasons for a given record. You can use a Lightning email template or a Visualforce email template. If you’re using a Visualforce email template, the recipient type must be User.
Turn on email notification settings.
Review these considerations for approval emails.
From the App Launcher, find and select Approvals.
Click Configure Approval Alerts.
Click New.
Enter a name for the record.
Enter your approval flow API name and the step API name.
If your email template is associated with the Approval Creation Success and the Approval Submission Approved or Rejected Status Update notification reasons, leave the step API name empty. These notification reasons apply to the entire workflow, not an individual step.
Under Email Template, enter the API name of your email template.
Select a notification reason.
Save your changes.

=== ARTICLE: ind.approvals_create_delegation_records.htm ===
---
article_id: ind.approvals_create_delegation_records.htm
title: Create Approval Delegation Records
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_create_delegation_records.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_approval_delegation.htm
fetched_at: 2026-09-07
---

# Create Approval Delegation Records

Set up approval coverage by specifying who handles your approval responsibilities and for how long.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To create delegation records:	Create, Edit, and Delete on Approval Delegation
From the App Launcher, find and select Approvals.
Open Manage Approval Delegations.
Click New.
In the Delegated From User field, select the user delegating their approvals.
In the Delegated To field, select the user, group, or queue that manages approvals on the reviewer's behalf.
In the Start Date field, enter the date and time when the delegation is active.
The start date must be in the future.
In the End Date field, enter the date and time when the delegation expires.
The end date must be later than the start date. If left blank, the delegation remains active indefinitely.
Enter your comments.
Save your changes.
NOTE A reviewer can have only 1 active delegation at a time. To assign different delegates for different periods, create non-overlapping approval delegation records.
SEE ALSO
Considerations for Advanced Approval Delegations

=== ARTICLE: ind.approvals_define_custom_logic_auto_approvals.htm ===
---
article_id: ind.approvals_define_custom_logic_auto_approvals.htm
title: Rule-Based Auto-Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_define_custom_logic_auto_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_smart_or_rule_based_approvals.htm
fetched_at: 2026-09-07
---

# Rule-Based Auto-Approvals

Set your own rules and conditions on specific fields for auto-approving resubmissions. Compare the current submission’s record details against the previously submitted record so that only significant changes require manual review.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To configure the properties of an approval step in a workflow:	

Approval Designer

OR

Manage Flow

Before you begin, make sure that you have an approval workflow with at least one stage and an approval step.

To determine whether an approval step can skip manual review during resubmission, use a custom autolaunched flow. You can invoke the flow from a background step that precedes the target approval step in your workflow.

In your custom flow, use an Apex action to retrieve the previously submitted record’s data and compare it with the current submission. This data serves as reference to help you create your own evaluation logic for auto-approvals. The evaluation must provide a boolean outcome that the target approval step uses to execute the auto-approval decision.

Create an Apex Class for the Apex Action to Retrieve and Evaluate Data
From Setup, find and select Apex Classes.
Click New.
In the class editor, enter the sample Apex code, and customize it per your requirements.
// This is wrapper class to get getPreviousRelaRecDetails results
public class ApprovalPreviousRelatedRecordDetails {
    
    static final String ACTION_NAME = 'getPreviousRelaRecDetails';
    static final String ACTION_INPUT_PARAM_FOI_ID = 'flowOrchestrationInstanceId';
    static final String ACTION_INPUT_PARAM_STEP_API_NAMES = 'stepApiNamesList';
    static final String ACTION_OUTPUT_PARAM_PREVIOUS_RECORD_DETAILS = 'previousRelatedRecordDetails';
        
    @InvocableMethod(label='Get Previous Related Record Details' description='Gets the related record details submitted for approval prior to the current approval submission, which is required for approval steps that use custom logic for auto-approvals.')
    // This method gets the previous related record details for the passed flow orchestration instance ID and the step api names.
    public static List<List<SObject>> getPreviousRelaRecDetails(List<FlowInputs> flowInputs) {
        List<List<SObject>> response = new List<List<SObject>>();
        List<SObject> allPreviousRelatedRecordDetails = new List<SObject>();

        // Set the action as the getPreviousRelaRecDetails which fetches related record details from the previous submission. 
        Invocable.Action action = Invocable.Action.createStandardAction(ACTION_NAME);
        action.setInvocationParameter(ACTION_INPUT_PARAM_FOI_ID, flowInputs[0].flowOrchestrationInstanceId);
        action.setInvocationParameter(ACTION_INPUT_PARAM_STEP_API_NAMES, flowInputs[0].stepApiNamesList);

        // Run the invocable action.
        List<Invocable.Action.Result> results = action.invoke();

        // Get all the previous related record details. They are retrieved in the same order as the order of the input step API names.
        if (results.size() > 0 && results[0].isSuccess()) {
            allPreviousRelatedRecordDetails = (List<SObject>) results[0].getOutputParameters().get(ACTION_OUTPUT_PARAM_PREVIOUS_RECORD_DETAILS);
            response.add(allPreviousRelatedRecordDetails);
        } else if (!results[0].isSuccess()){
            // If there are no results returned, consider it as a failure.
            // Based upon the use case, this can also be success with 0 records.
            for(Invocable.Action.Error error : results[0].getErrors()) {
                // throw new InvocableActionException(error.getMessage());
            }
        }
        return response;
    }
    
    // This inner class sets invocable action input variables
    public class FlowInputs {
        @InvocableVariable
        public String flowOrchestrationInstanceId;

        @InvocableVariable(required=false)
        public List<String> stepApiNamesList;
        
    }
    
    // This inner class is to handle any invocable action related exceptions
    public class InvocableActionException extends Exception {
   // Add your custom logic here.
    }
}

Create an autolaunched flow that uses the Apex action to retrieve the previous submitted record details for your custom evaluations. You can configure your evaluation conditions either in this flow or in the approval workflow by using variables.

Configure Your Approval Workflow

Invoke your custom flow from a background step that precedes the target approval step in your approval workflow.

From Setup, find and select Flows.
Open the flow that you use for managing approvals.
In the stage with the target approval step, click + Add Step.
Select Background Step and specify these details.
Enter a name, an API name, and a description.
Select a condition.
Under the Select an Action to Run section, select the custom flow that you created.
For Select Who to Run the Action as, select Automated Process User as the user type.
Go to the target approval and specify these details.
If your background step precedes the target approval step within the same stage, select When another step is marked Complete, the step starts as the condition.
For Step API Name, enter the name of the background step that runs your custom flow.
Select Set custom logic for auto-approvals.
For Auto-Approve Step, specify the boolean output from your custom evaluations.
Save and activate your flow.

=== ARTICLE: ind.approvals_delegation_considerations.htm ===
---
article_id: ind.approvals_delegation_considerations.htm
title: Considerations for Advanced Approval Delegations
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_delegation_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Considerations for Advanced Approval Delegations

Keep these considerations in mind when working with approval delegation.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
A delegate user must be active. Inactive users can't be set as delegate users.
When delegating to a queue or group, the queue or group must have at least 1 member.
A reviewer can't delegate to themselves.
Delegates receive email notifications when approval work items are assigned or reassigned. Slack notifications aren't sent to delegates.
Approval Delegation records can't be deleted. To end a delegation early, update the end date.
Delegations for the same approver can't overlap in date ranges.

=== ARTICLE: ind.approvals_design_advanced_approvals.htm ===
---
article_id: ind.approvals_design_advanced_approvals.htm
title: Customize Pages for Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_design_advanced_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Customize Pages for Approvals

Customize approval and related pages with Lightning components, related lists, and custom actions that help trigger, monitor, and review approvals.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Configure Lightning Components for Approvals
Add Lightning components to pages to enable users to track progress, preview an approval chain, and review outstanding approvals.
Add a Related List to an Approval Page
Add related lists to your approval pages for easy access to work items, record history, and files and attachments.
Example: Add an Approval Button on a Record Page
Add a button that users can click to submit a record for approval. Let’s see an example for adding a button on the quote page.

=== ARTICLE: ind.approvals_design_build_activation.htm ===
---
article_id: ind.approvals_design_build_activation.htm
title: Design, Build, and Activation
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_design_build_activation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Design, Build, and Activation

This section covers rules, constraints, and errors you might encounter while designing, building, and activating your approval processes.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Activating a Flow

You can’t activate an approval flow that has validation errors. Errors are listed on the Flow Builder Error tab.

Create, Update, and Delete Operations

You can’t use the sObject APIs to perform create, update, and delete (CUD) operations on a standard field for an approval object. Instead, update approval records using the available invocable actions or by designing alternate flows. However, you can use the APIs to update custom fields.

Apex Trigger Update Restriction

All triggers must be updated to avoid any create, update, and delete operations on standard approval fields, as these operations will fail. However, you can use triggers to update custom fields.

=== ARTICLE: ind.approvals_email_notification_behavior.htm ===
---
article_id: ind.approvals_email_notification_behavior.htm
title: Considerations for Emails in Advanced Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_email_notification_behavior.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Considerations for Emails in Advanced Approvals

Keep these considerations in mind when working with approval emails and notifications.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
To enable approval email notifications, turn on Send Approval Work Item Assignment Emails and Send Approval Submission Status Email Notifications in Advanced Approval settings, and deselect Don’t send approver notifications in the approval step of your workflow.
To use the email templates that you create, make sure that they’re marked as Available for Use.
The entity of the email template must match the target object of the approval workflow.
You can create only one email template for a given combination of approval flow, approval step, and notification reason.
An email template associated with the approval alert content definition record overrides the custom email specified for an approval step within the workflow.
A template that isn’t associated with a specific step is applied to all steps in the workflow that lack a unique template.
If your email template uses an Apex controller, grant the Automated Process user access to the Apex class. Without this access, the custom template isn’t applied.
When reviewers respond by email, they must place the decision keyword such as Approve on the first line and their comment on the second line. Otherwise, the comment isn’t captured.
Queue emails can be sent to a maximum of 1,000 recipients. To avoid exceeding this limit, enable Send approval work item emails only to queue members. This restricts emails to queue members and prevents them from being sent to users higher in the role hierarchy.
If the org reaches its email limit, users don’t receive approval emails until the cool-down period resets or the limit is increased.
Emails sent after a reassignment may include the extra word "null" in the body. You can ignore this text.
When Advanced Approval Delegation is enabled, delegates receive email notifications when approval work items are assigned or reassigned to them.

=== ARTICLE: ind.approvals_email_templates.htm ===
---
article_id: ind.approvals_email_templates.htm
title: Email Templates in Advanced Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_email_templates.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Email Templates in Advanced Approvals

In an approval workflow, a request passes through multiple stages and reviewers. To provide reviewers and submitters clear and contextual information in their emails, create custom email templates for different notification reasons.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled

With Lightning or Visualforce email templates, use advanced formatting capabilities that help organize details for complex records, such as quotes. The formatted template helps the reviewer review all the necessary details to act on the request directly from their email.

Create an email template for each of these notification reasons in an approval workflow. The template defines the specific trigger event that sends the email to the reviewer and the submitter. A reviewer can be a user, group, or queue.

NOTIFICATION REASON	DEFINITION
Approval Step Assignment	The reviewer is notified about the approval step.
Approval Step Reassignment	The new reviewer is notified about the approval step.
Approval Step Assignment to Delegate	The delegate of the reviewer is notified about the approval step.
Approval Step Reassignment to Delegate	The delegate of the newly assigned reviewer is notified about the approval step.
Approval Creation Success	The submitter is notified about the creation of the approval submission.
Approval Submission Approved or Rejected Status Update	The submitter is notified about the approval or rejection on the related approval submission.
Approval Work Item Approved or Rejected Status Update	The submitter is notified about the approval or rejection on the related approval work item.
Auto-Approval Confirmation	The reviewer is notified about the auto-approval of the resubmitted record.

After you create the email templates, create approval alert content definition records. These record defines the association between your email template and notification reason within an approval step or the entire workflow.

Create Approval Alert Content Definition Records
To map a custom email template to notification reasons, create an approval alert content definition.
SEE ALSO
Considerations for Emails in Advanced Approvals

=== ARTICLE: ind.approvals_environment_setup.htm ===
---
article_id: ind.approvals_environment_setup.htm
title: Environment & Setup
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_environment_setup.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Environment & Setup

This section covers the limitations related to core setup and environment configuration.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Sandbox Permission Discrepancy  

For sandbox users to have the same feature access and licenses as production users, ensure that the Match Production License tool is run in the sandbox environment, especially after a release. Otherwise, sandbox user permissions won’t be automatically upgraded, and users will lack access to features that are available in the production instance.

=== ARTICLE: ind.approvals_example_configure_an_approval_workflow.htm ===
---
article_id: ind.approvals_example_configure_an_approval_workflow.htm
title: "Example: Configure an Approval Workflow"
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_example_configure_an_approval_workflow.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_building_blocks_of_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Example: Configure an Approval Workflow

Let’s build a complete approval workflow to determine the approvals required on a quote’s discounts, implementing both Smart Approvals and Dynamic Approval Notifications.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To configure approval workflows:	Approval Designer

To demonstrate this, we'll use an example of a vendor who sells products that require quotes. This vendor offers discounts and, to ensure approvals are applied efficiently, sets the following conditions:

DISCOUNT VALUE	APPROVAL LEVEL
Up to 25%	No approval necessary
Over 25%	Approval necessary
Over 50%	Second level of approval necessary

To ensure our approval process works seamlessly, you must first configure the approvers. This involves mapping them to their correct personas and assigning the corresponding permissions to control their access and actions. See Advanced Approvals Personas and Permissions for more information.

Here are the steps you must follow to configure an approval workflow.

Create the Get Quote Record Flow
Create a Discount Approval Workflow
Make Decisions for Your Discount
Create an Approval Stage
Create the Get Quote Record Flow
From Setup, find and select Flows.
Select New Flow.
Select Autolaunched Flow (No Trigger).
Create a variable to store the quote record that we will fetch based on the ID provided as input.
Click and select New Resource.
Specify these details.
Resource Type: Variable
API Name: FetchedQuoteRecord
Description: Store the quote record that fetches the quote ID
Data Type: Record
Object: Quote
Select Available for output.
Click Done.
Create another variable to receive the quote ID as input.
Resource Type: Variable
API Name: InputQuoteID
Description: Receive the quote ID as input
Data Type: Text
Select Available for output.
Click Done.
Now, on your Flow Builder canvas, click and select the Get Records element to get the quote record details.
Specify these details.
Label: Get the Complete Record
Click Tab to autopopulate the API Name. Or provide an API name that’s similar to your label.
Object: Quote
Then, set a condition to filter quote records.
Condition Requirements: All Conditions Are Met (AND)
Set Quote ID under Record Fields as the resource.
Operator: Equals
Value: InputQuoteID
Then, click  to add the Assignment element to get the fetched quote record and assign it to the fetched quote record variable.
Specify these details.
Label: Assign the Fetched Record
Click Tab to autopopulate the API Name. Or provide an API name that’s similar to your label.
Set the variable values.
Variable: FetchedQuoteRecord
Operator: Equals
Value: Quote from Get the Complete Record
Save your flow as Fetch Quote Details and activate it.
Your flow should look like this.
Create a Discount Approval Workflow
From Setup, find and select Flows.
Select New Flow.
Select Autolaunched Flow Approval Process (No Trigger).
Click and and verify that you see these predefined variables..
recordId - Represents the submitted approval record
submitter - Represents the user who submitted the approval
submitterComments - Represents the comments provided by the submitter
If you don’t see these predefined variables, verify if you’ve selected the right automation flow - Autolaunched Flow Approval Process (No Trigger).
Now, on your Flow Builder canvas, click and select the Stage element to invoke the fetch the quote record.
Specify these details.
Label: Get quote record
Click Tab to autopopulate the API Name. Or provide an API name that’s similar to your label.
Condition: When all steps have been marked Completed, the state is marked Completed
In the Get quote record element, click + Add Step.
Select Background Step and specify these details.
Label: Get quote record for record id
Click Tab to autopopulate the API Name. Or provide an API name that’s similar to your label.
Condition: When the stage starts, the step starts
Under the Select an Action to Run section, select the flow you created in the previous step.
Action: Fetch Quote Details
InputQuoteID: recordId
Your background step should look like this.
Make Decisions for Your Discount

Decision elements are used to evaluate conditions and route the workflow down different paths. For example, a designer can configure a Decision element to check if a business rule is met, such as a discount exceeding a certain discount percentage. Based on the outcome, the approval workflow will be routed to the next step or stop the process by routing it to a default outcome.

On the same flow, click  and select the Decision element.
Enter If quote discount is greater than 25 as the label.
Next, set your outcomes.
Specify these details under New Outcome.
Outcome Label: Discount > 25
Condition Requirements to Execute Outcome: All Condition Are Met (AND)
Resource: Get quote record > Get quote record for record id > Outputs > FetchedQuoteRecord > Discount
Operator: Greater Than
Value: 25
Your outcome should look like this.
Create an Approval Stage

Approval Steps are used to assign a request to a specific user or queue and can require the approver to complete a specific action. For example, following an outcome from a Decision element (like a discount exceeding a certain percentage), a designer can add an Approval Step to route the request to a manager where they can approve or reject the record.

On the same flow, after the Discount > 25 outcome, click to another Stage element.
Specify these details.
Label: Send for approval
Click Tab to autopopulate the API Name. Or provide an API name that’s similar to your label.
Condition: When all steps have been marked Completed, the state is marked Completed
In the Send for approval element, click + Add Step.
Select Approval Step and specify these details.
Label: Approval discount greater than 25
Click Tab to autopopulate the API Name. Or provide an API name that’s similar to your label.
Condition: When the stage starts, the step starts
Under the Select an Action to Run section, select the Evaluate Approval Requests action.
Assign an approver by selecting the Approver Type as User and providing the user’s name. Users see this option only if they’ve enabled the Enable email approval response setting. Also, users must use recognizable keywords such as Approve or Reject, for the response to be processed.
Under the Select the Record to Approve, specify these details.
Record: recordId
Optionally, select Use Smart Approvals to set automatic approvals.
Finally, if you’ve set serial or parallel approvals, provide a chain name to ensure approvers can provide the approval sequentially or simultaneously.
To complete the workflow, add another Decision element under the Send for approval Stage element to set outcomes if the discount is greater than 50%.
Add a final approval stage element with an approval step, assigning it to the appropriate approver. Inside this step, set the completion condition to When the assigned user has completed the action, the step is marked Completed.

Finally, save the flow with the name Discount Threshold Approval; this exact name is essential as the integration layer will use it to invoke the flow.

=== ARTICLE: ind.approvals_implement_serial_and_parallel_approvers.htm ===
---
article_id: ind.approvals_implement_serial_and_parallel_approvers.htm
title: Implement Serial and Parallel Approvers
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_implement_serial_and_parallel_approvers.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_types_of_approvals.htm
fetched_at: 2026-09-07
---

# Implement Serial and Parallel Approvers

To implement serial and parallel approvers, you’ll need to set up an approval chain.

USER PERMISSIONS NEEDED
To implement serial and approval approvals:	Approval Designer

The steps below assume you are already familiar with how to create a flow.

Open Flow Builder and create a new flow (either an Autolaunched Flow Approval Process or a Record-Triggered Flow Approval Process).
Add a Stage element to the flow and include approval steps for the approvers.
For each approval step, fill out the required fields, including the Approval Chain Name.
The Approval Chain Name should reflect the list of approvers for that step or stage in the process.

=== ARTICLE: ind.approvals_lightning_components.htm ===
---
article_id: ind.approvals_lightning_components.htm
title: Configure Lightning Components for Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_lightning_components.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_design_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Configure Lightning Components for Approvals

Add Lightning components to pages to enable users to track progress, preview an approval chain, and review outstanding approvals.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To customize approval pages in Lightning App Builder:	Customize Application
LIGHTNING COMPONENT	DESCRIPTION	SUPPORTED PAGES
Approval Trace	Shows the approval work items associated with a record.	Any record page associated with an approval workflow.
Orchestration Work Guide	Shows pending approval work items to assigned users.	Any record page associated with an approval workflow.
Approval Workflow	Provides a preview of the approval process, including conditions, chain names, and assignees triggered when a record is submitted. This component is available only with Advanced Approvals.	Any record page associated with an approval workflow.
Chatter	Shows the activity feed for a record.	All approval and related record pages.
From Setup, in the Quick Find box, find and select Lightning App Builder.
On the record page that you want to add the component, click Edit.
Drag the component to the canvas.
To edit the component properties, click it.
For components such as Approval Workflow, enter the API name of the autolaunched flow that triggers your approval process.
Save your changes.

=== ARTICLE: ind.approvals_manage_advanced_approvals.htm ===
---
article_id: ind.approvals_manage_advanced_approvals.htm
title: Begin Using Advanced Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_manage_advanced_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Begin Using Advanced Approvals

To efficiently set up and manage your approval strategies, first configure the experience for your team by creating users and assigning permissions based on their persona. Once your users are prepared with the correct access, you must complete the recommended base configuration from the Approvals Settings page to activate the features.

Advanced Approval Objects
Learn about the objects and list views available in Advanced Approvals.
Advanced Approvals Personas and Permissions
Explore the different types of users who work with Advanced Approvals and the permissions they need.
Set Up Advanced Approvals
To use all Advanced Approvals features, you must first complete the recommended base configuration. The Approvals settings page is the central hub for managing your organization-wide settings. This setup is essential for your approval workflows to run effectively.
Share Temporary Access to Records in Advanced Approvals
Share temporary access to related records with your approvers by setting up triggers. After the approval action is complete, use a trigger to withdraw the record access.
Set Up Dynamic Approval Notifications
To accelerate approval times, turn on Dynamic Approval Notifications. This feature embeds AI-generated summaries directly into approval email notifications and individual Slack direct messages, giving approvers the context they need to act quickly.

=== ARTICLE: ind.approvals_objects_considerations.htm ===
---
article_id: ind.approvals_objects_considerations.htm
title: Considerations for Approval Objects
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_objects_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Considerations for Approval Objects

This section covers considerations and limitations for approval objects and related records.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
An approval request can be triggered only from supported objects. To check or request support for your object, contact your Salesforce admin.
If a related record’s access is set to Public Read Only, all users automatically get access to its approval submissions. However, if it's set to Private, you can share temporary access to the related record using Apex triggers. See Share Temporary Access to Records in Advanced Approvals.

=== ARTICLE: ind.approvals_personas.htm ===
---
article_id: ind.approvals_personas.htm
title: Advanced Approvals Personas and Permissions
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_personas.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_manage_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Advanced Approvals Personas and Permissions

Explore the different types of users who work with Advanced Approvals and the permissions they need.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled

To begin, create users for Advanced Approvals. Each user must be assigned a profile, which defines their default settings. Grant specific access by assigning the appropriate permissions. A user can have many permissions.

APPROVALS PERSONA	WHAT PERSONAS CAN DO	PERMISSION NAME
Approval Designer	Design and activate approval workflows.	
Manage Flow
Approval Designer
Read on Approval Submission

Approval Submitter	Initiate submissions and submit or recall them for approval.	
Run Flows
Read on Approval Submission

Approval Reviewer	Receive notifications and review approval work items. A reviewer can be a user, group, or queue.	
Run Flows
Read on Approval Submission

Approval Delegate	Review and act on approval work items on behalf of the original reviewer during an active delegation period. Delegates receive email notifications for assigned work items.	
Run Flows
Read on Approval Submission

Approval Administrator	Manage organization-wide settings and modify, recall, or cancel submissions and review or override any work item. An approval admin also has access to work item conditions and criteria.	
Run Flows
Approval Admin
Read on Approval Submission

=== ARTICLE: ind.approvals_preview.htm ===
---
article_id: ind.approvals_preview.htm
title: Preview an Approval Workflow
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_preview.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_preview_approvals.htm
fetched_at: 2026-09-07
---

# Preview an Approval Workflow

To visualize the approval journey of your submission, add the Approval Workflow component to your record page. The preview sorts steps by their chain name and shows them in their sequence order.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To customize record pages in Lightning App Builder:	Customize Application
To preview the approval submission from a related record:	Run Flows
Add the Approval Workflow Lightning component to a record page.

After adding the component, verify the approval flow's API name. If the flow API name is incorrect, the preview fails.

Open the related record.
Click Preview.

=== ARTICLE: ind.approvals_preview_approvals.htm ===
---
article_id: ind.approvals_preview_approvals.htm
title: Preview Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_preview_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Preview Approvals

Review the steps, chains, and approvers for a record before you submit it. Preview Approvals evaluates the record's field values and simulates the approval steps triggered. During the preview, approval-related records aren’t created or modified.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled

Approval steps are shown in sequence within each chain, along with their dependencies. The step dependencies are evaluated by using the step entry conditions configured in the associated flow.

The preview window shows the following for each step:

Approval Chain: The chain associated with the step.
Assignee: The user, group, or queue assigned to approve the step.
Status: The status of the approval step, which is Not Submitted by default.
Approval Condition: The name of the condition that triggered the step.
Example: How Step Conditions Affect a Preview
See how step entry conditions in your workflow determine the order and visibility of approval steps during preview.
Preview an Approval Workflow
To visualize the approval journey of your submission, add the Approval Workflow component to your record page. The preview sorts steps by their chain name and shows them in their sequence order.
SEE ALSO
Preview Considerations

=== ARTICLE: ind.approvals_preview_example.htm ===
---
article_id: ind.approvals_preview_example.htm
title: "Example: How Step Conditions Affect a Preview"
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_preview_example.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_preview_approvals.htm
fetched_at: 2026-09-07
---

# Example: How Step Conditions Affect a Preview

See how step entry conditions in your workflow determine the order and visibility of approval steps during preview.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled

This example uses a flow of type Autolaunched Flow Approval Process (No Trigger) with these stages.

Stage 0: Runs a background step to get the account record.
Stage 1: Contains four approval steps across HR, Legal, and Finance chains.
Decision element: Evaluates the account revenue after stage 1 completes.
Stage 3: Contains one approval step that’s triggered when the account revenue is less than 1000.
Scenario One: Account Revenue Is 1000 or Greater

If the account’s revenue meets or exceeds 1000, the flow ends after stage 1. The preview window shows the four steps in stage 1 across the HR, Legal, and Finance chains based on their entry condition and sequence order.

HR 1: Starts when the stage starts and appears at level one of the HR chain.
HR 2: Starts when HR 1 completes and appears at level two of the HR chain.
Legal 1: Starts when HR 1 completes and appears at level two of the Legal chain.
Finance 1: Starts when Legal 1 completes and appears at level three of the Finance chain.

HR 2 and Legal 1 are at the same level because they both depend on HR 1.

Scenario Two: Account Revenue Is Less Than 1000

If the account’s revenue is less than 1000, the flow moves to stage 3. The preview window shows the same steps as Scenario One and another approval step belonging to stage 3.

=== ARTICLE: ind.approvals_preview_feature_limitations.htm ===
---
article_id: ind.approvals_preview_feature_limitations.htm
title: Preview Approvals Considerations
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_preview_feature_limitations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Preview Approvals Considerations

Keep these considerations in mind when working with Preview Approvals.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
You can use Preview Approvals only with the Autolaunched Flow Approval Process (No Trigger) flow type.
Steps that have entry conditions based on runtime or asynchronous evaluations, such as subflows in background steps, aren’t shown during preview. As a workaround, set mock output values for these evaluations in Flow Builder.
Preview Approvals treats all referenced steps as required dependencies and doesn’t distinguish between AND and OR conditions. For example, if a step is configured to start after Step A OR Step B, the preview shows it as dependent on both.
You can’t pass input variables to the flow manually during preview. If the flow requires input variables, configure default values for them in Flow Builder.
The preview doesn’t show the dependencies between approval steps that belong to different chains. However, the steps are shown in their sequential order.
If an internal error occurs during preview, verify that each stage has a valid exit path and the steps aren't assigned to approvers of type Resource.

=== ARTICLE: ind.approvals_related_lists.htm ===
---
article_id: ind.approvals_related_lists.htm
title: Add a Related List to an Approval Page
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_related_lists.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_design_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Add a Related List to an Approval Page

Add related lists to your approval pages for easy access to work items, record history, and files and attachments.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To add a related list to a page layout:	Customize Application
From Setup, select Object Manager and select the object that you want to add a related list to.
Click Page Layouts
In the list of available items, select Related Lists.
Drag the related list to the Related Lists section.
Save your changes.

=== ARTICLE: ind.approvals_set_up_advanced_approvals.htm ===
---
article_id: ind.approvals_set_up_advanced_approvals.htm
title: Set Up Advanced Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_set_up_advanced_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_manage_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Set Up Advanced Approvals

To use all Advanced Approvals features, you must first complete the recommended base configuration. The Approvals settings page is the central hub for managing your organization-wide settings. This setup is essential for your approval workflows to run effectively.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To enable approval settings:	Customize Application
From Setup, find and select Approval Settings.
To automate flows, turn on these settings.
Use Flow Approval Process
Use Advanced Approvals
To manage email notifications as an administrator, turn on these settings.
Send Approval Work Item Assignment Emails to Approvers
Send Approval Submission Status Email Notifications to Submitters
Optionally, you can send flow approval work items by turning on the Send approval work item emails only to queue members option. By default, the work items are sent to queued members or delegates.
To let reviewers delegate their approval responsibilities to another user, group, or queue, turn on Use Advanced Approval Delegation.
To use generative AI to respond to approvals, turn on Use Dynamic Approval Notifications.
To allow approvers review approval items by replying to an email, you’ll need to make edits in the Process Automation Settings page.
From Setup, find and select Process Automation Settings.
Select Enable email approval response.
Save your changes.

=== ARTICLE: ind.approvals_share_records_using_triggers.htm ===
---
article_id: ind.approvals_share_records_using_triggers.htm
title: Share Temporary Access to Records in Advanced Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_share_records_using_triggers.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_manage_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Share Temporary Access to Records in Advanced Approvals

Share temporary access to related records with your approvers by setting up triggers. After the approval action is complete, use a trigger to withdraw the record access.

When you submit a record for approval, the approver must have access to the record’s related object to perform actions on the approval request. If your object’s internal organization-wide sharing default is Private, you can use a trigger to create a share object that grants access to the approver. After the record is approved, you can withdraw the record access by using a trigger to delete the share record.

Create an Apex trigger to share access to a record's related object. Under Security, select the profile of your approver. See Define Apex Triggers.
TIP

If you're sharing access to a custom object, you can create an Apex sharing reason and include it in the trigger. An apex sharing reason restricts the record access to your specific use case.

Create an Apex trigger to delete the share record and revoke the record access after the approval request is complete. Under Security, select the profile of your approver.

You can customize the sample code snippet to suit your specific use case.

trigger AWIUpdate on ApprovalWorkItem(after update) {
List<ApprovalWorkItem> awiList = new List<ApprovalWorkItem>();
// Get the related opportunities for the accounts in this trigger
awiList = [SELECT Id, RelatedRecordId, AssignedToId FROM ApprovalWorkItem WHERE Id IN :Trigger.new];

for (ApprovalWorkItem awi : awiList) {
// Use the related record id, to delete the share record created for the user

Id relatedRecordId = awi.RelatedRecordId;
Id assignedToId = awi.AssignedToId;

SObjectType relatedRecordType = relatedRecordId.getSObjectType();
if (relatedRecordType.getDescribe().isCustom()) {
Map<String, Schema.SObjectType> tokens = Schema.getGlobalDescribe();
String relatedRecordShareName = relatedRecordType.getDescribe().getName().removeEnd('__c') + '__Share';
if(tokens.containsKey(relatedRecordShareName)) {
// Share object exists
SObject[] customShare = Database.query('SELECT Id FROM '
+ relatedRecordShareName + ' WHERE '
+ ' RowCause = \'AdvancedApprovalTriggerShareReason__c\' '
+ ' AND ParentId = :relatedRecordId'
+ ' AND UserOrGroupId = :assignedToId');
} else {
// OWD is Public Read Write
}
}
}
}

=== ARTICLE: ind.approvals_slack.htm ===
---
article_id: ind.approvals_slack.htm
title: Approvals in Slack
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_slack.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Approvals in Slack

With Approvals in Slack, approvers can approve or reject requests and add comments without leaving Slack, while submitters receive real-time updates on their requests. Your Slack actions are saved to Salesforce, so approval data stays consistent across channels.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals or Flow Approval Processes is enabled

In Slack, reviewers can view approval-related details, such as the work item name, the related record, the submitter, and the condition that triggered the request. The approval and related records are visible in the Slack unfurl and flexpane components. To manage the fields in these components, see Slack Record Layout.

When reviewers approve or reject requests in Slack, Salesforce automatically updates the corresponding approval records. For example, approving or rejecting a request updates the approval work item's Status and Comments fields, along with the Action Channel Name field on the related approval submission detail.

Notifications
In the Salesforce Slack app, notifications are sent as direct messages to individual reviewers.
When an approval step is assigned to a public group or queue, each active member receives a direct message.
To notify group and queue members of approval requests in a shared channel, the approval designer can specify a Slack channel in the approval step.
If Dynamic Approval Notifications is enabled, direct message notifications also include an AI-generated summary of the approval request.
Turn On Slack Notifications for Approvals
Connect Salesforce to your Slack workspace so that users can receive and act on approval requests in Slack.
Post Approval Notifications to a Slack Channel
Configure an approval step to post its notification to a specific Slack channel instead of sending it to the assigned group or queue.

=== ARTICLE: ind.approvals_slack_channel_notifications.htm ===
---
article_id: ind.approvals_slack_channel_notifications.htm
title: Post Approval Notifications to a Slack Channel
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_slack_channel_notifications.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_slack.htm
fetched_at: 2026-09-07
---

# Post Approval Notifications to a Slack Channel

Configure an approval step to post its notification to a specific Slack channel instead of sending it to the assigned group or queue.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To configure an approval step's properties:	Manage Flow
Find and copy your Slack channel ID.
From your Slack workspace, open a channel.
To open the channel details, click the channel name at the top.
In the About tab, copy the channel ID.
NOTE If your Slack channel is private, add the Salesforce app to the channel. Private channels don't have access to Salesforce by default. See Guide to apps in Slack.
Configure your approval workflow to send notifications to a Slack channel.
From Setup, find and select Flows.
Open the flow that contains your approval step.
Click the step to open its properties.
Set the Approver Type to Group or Queue.
Specify a group or queue.
Select Send Approval Notification to Slack Channel.
In the Slack Channel ID field, enter your Slack channel's ID. For example, C01234ABC.
Save and activate the flow.

=== ARTICLE: ind.approvals_slack_considerations.htm ===
---
article_id: ind.approvals_slack_considerations.htm
title: Considerations for Approvals in Slack
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_slack_considerations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Considerations for Approvals in Slack

Keep these considerations in mind when working with approvals in Slack.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals or Flow Approval Processes is enabled
Slack channel notifications for approval requests are only available in Advanced Approvals.
If an assigned group or queue has no active members, Slack notifications aren't sent for that step.
AI-generated summaries from Dynamic Approval Notifications are not included in channel posts.
When an approval work item is completed, you can't review again regardless of the channel used.
Delegates don’t receive approval notifications in Slack.
For Flow Approval Processes, Slack notifications for groups and queues are supported for up to 100 active members. If the group or queue exceeds this limit, no members receive a Slack notification for that step. This limit doesn't apply to unanimous group approval steps in Advanced Approvals.

=== ARTICLE: ind.approvals_smart_approval_limitations.htm ===
---
article_id: ind.approvals_smart_approval_limitations.htm
title: Smart Approval Limitations
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_smart_approval_limitations.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_advanced_approvals_considerations.htm
fetched_at: 2026-09-07
---

# Smart Approval Limitations

This section covers eligibility rules and known constraints for the Smart Approvals feature.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Smart Approval Eligibility - Evaluation Flows

Using an evaluation flow as an entry or exit condition in any approval step marks the entire flow as ineligible, violating a key constraint for Smart Approvals. To resolve this issue, update the workflow to incorporate those conditions directly.

Smart Approval Eligibility - Decision Nodes

A flow is considered ineligible if you add a decision node before a stage when you add the condition When the stage starts, the step starts in an approval step. To resolve this issue, update the approval step's entry conditions to directly include the criteria from the preceding decision node.

Unsupported Data Types for Smart Approval

Approval conditions must use a supported Number or Text data type to be eligible for auto-review in Smart Approvals.

Smart Approval Trigger Requirement

A record's preceding submission status must be Rejected or Recalled for the resubmission to be eligible for Smart Approval evaluation.

Smart Approval Version Dependency

Smart Approvals are dependent on a consistent flow definition version. If the active flow definition version changes between the original submission and a resubmission, Smart Approvals won’t be considered. To ensure correct function,a resubmission must use the same flow definition version as the original submission to be eligible for Smart Approval evaluation.

Smart Approval Logic Constraint

Using the NOT operator in custom entry logic marks the approval step as ineligible for Smart Approvals. To resolve this issue, you must rebuild the logic using only positive conditions to achieve the same outcome.

Smart Approval Limitation Post-Reassignment

Reassigning a work item during the original submission's execution marks the resubmission as ineligible for Smart Approvals. This scenario will require a manual review of the work item.

=== ARTICLE: ind.approvals_smart_approvals.htm ===
---
article_id: ind.approvals_smart_approvals.htm
title: Smart Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_smart_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_smart_or_rule_based_approvals.htm
fetched_at: 2026-09-07
---

# Smart Approvals

To eliminate approval bottlenecks, Smart Approvals routes requests by auto-approving pre-qualified data changes and not reviewing unchanged data. When a record is resubmitted for approval, Smart Approvals compares the new conditions against the previous submission. If the values remain within the defined range, it skips re-approval.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS
NEEDED
To turn on smart approvals:	

Approval Designer

OR

Manage Flow

Before we introduce the steps to be followed to implement Smart Approvals, familiarize yourself with how to create an approval flow.

Review these considerations for how smart approvals work for different step entry conditions in your flow.

APPROVAL STEP ENTRY CONDITION	SMART APPROVAL CONSIDERATIONS
When the stage starts, the step starts	If the approval stage that contains the step has a decision element before it, the smart approval evaluation fails.
When another step is marked Complete, the step starts	None.
When the specified requirements are met, the step starts	You can specify up to 30 conditions. Apex and Record data types aren’t eligible for smart approval evaluation.
When the specified evaluation flow returns True, the step starts	Not eligible for smart approval evaluation.
EXAMPLE A company uses Smart Approvals for its multistep discount workflow. John can approve discounts up to 40%, James approves 41–50%, and the CFO, Jenny, must approve anything over 50%. A sales rep submits a quote with a 55% discount. After John and James approve the quote, Jenny rejects it and asks for a lower discount. The rep adjusts the quote to 52% and resubmits. Instead of restarting the entire process, Smart Approvals compares the new submission to the previous one and sees that John and James’s conditions are still met, so it routes the request only to Jenny for the final sign-off. This process eliminates redundant approvals.
Turn On Smart Approvals
To skip reviewing previously approved steps in an approval resubmission, turn on Smart Approvals.

=== ARTICLE: ind.approvals_smart_or_rule_based_approvals.htm ===
---
article_id: ind.approvals_smart_or_rule_based_approvals.htm
title: Smart Approvals and Rule-Based Auto-Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_smart_or_rule_based_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_building_blocks_of_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Smart Approvals and Rule-Based Auto-Approvals

Smart Approvals and Rule-Based Auto-Approvals speed up resubmissions by auto-approving steps that don’t need another manual review. They differ in how the auto-approval decision is made and the level of control you have over that decision.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Considerations for Auto-Approvals

Smart or Rule-Based Auto-Approvals trigger only when a user resubmits a previously recalled or rejected record. Also, the previous submission must have reached at least 2 steps, with at least 1 of those steps approved.

A completely approved submission can't be recalled. Any subsequent submission is a new request rather than a resubmission, making it ineligible for auto-approval.

Understanding Smart Approvals

Smart Approvals uses each approval step’s existing entry conditions to decide whether the step can be auto-approved on resubmission. If the values that satisfied a step in the previous submission still satisfy it on resubmission, Smart Approvals skips the manual review for that step.

Use Smart Approvals when your approval steps already rely on entry conditions and the resubmission decision depends on whether those same conditions are still met.

Understanding Rule-Based Auto-Approvals

With Rule-Based Auto-Approvals, you can define custom logic such as flows or Apex to determine whether a step is automatically approved on resubmission. Optionally, use the Get Previous Related Record Details invocable action to compare the current submission with a prior submission. Define any business logic that you need, and pass a boolean value as the final auto-approval decision.

Use Rule-Based Auto-Approvals when your auto-approval decision depends on logic that step entry conditions can’t express, such as cross-field comparisons.

Smart Approvals vs. Rule-Based Auto-Approvals

Here’s how Smart Approvals and Rule-Based Auto-Approvals differ.

CAPABILITY	SMART APPROVALS	RULE-BASED AUTO-APPROVALS
Setup	In the approval step’s properties, select Use Smart Approval.	
In the approval step’s properties, select Set custom logic for auto-approvals.
In the Approve Step field, enter a boolean value.

Comparison logic	Reevaluates the step’s existing entry conditions against the previous submission.	Uses any logic that you define, including cross-field or cross-submission rules.
Skip conditions support	Supported. Use the Smart Approval Skip Conditions field to exclude specific conditions from evaluation.	Not applicable
Sample use case	A discount or quantity stays within an approver’s tier on resubmission.	The discount delta between submissions is below a threshold.
Smart Approvals
To eliminate approval bottlenecks, Smart Approvals routes requests by auto-approving pre-qualified data changes and not reviewing unchanged data. When a record is resubmitted for approval, Smart Approvals compares the new conditions against the previous submission. If the values remain within the defined range, it skips re-approval.
Rule-Based Auto-Approvals
Set your own rules and conditions on specific fields for auto-approving resubmissions. Compare the current submission’s record details against the previously submitted record so that only significant changes require manual review.

=== ARTICLE: ind.approvals_turn_on_delegation.htm ===
---
article_id: ind.approvals_turn_on_delegation.htm
title: Turn On Advanced Approval Delegation
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_turn_on_delegation.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_approval_delegation.htm
fetched_at: 2026-09-07
---

# Turn On Advanced Approval Delegation

Give reviewers the ability to delegate their approval responsibilities to another user, group, or queue for a set period or indefinitely.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To turn on Approval settings:	Customize Application
IMPORTANT When you turn on this setting, delegations configured on reviewer user records no longer apply. Reviewers must create Approval Delegation records to set up their delegations.
From Setup, find and select Approval Settings.
Turn on Use Advanced Approval Delegation.

=== ARTICLE: ind.approvals_turn_on_dynamic_approvals.htm ===
---
article_id: ind.approvals_turn_on_dynamic_approvals.htm
title: Set Up Dynamic Approval Notifications
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_turn_on_dynamic_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_manage_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Set Up Dynamic Approval Notifications

To accelerate approval times, turn on Dynamic Approval Notifications. This feature embeds AI-generated summaries directly into approval email notifications and individual Slack direct messages, giving approvers the context they need to act quickly.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals and Einstein for Sales, Einstein for Platform, Einstein for Service, Einstein 1 Service, or Einstein GPT Service are enabled
IMPORTANT In order to use the AI generated email feature to approve or reject approval work items, your org must be provisioned with Data Cloud and Einstein. If you don’t have access to them, reach out to your Salesforce account executive.
USER PERMISSIONS NEEDED
To turn on dynamic approval notifications:	Approval Administrator
To receive AI-generated approval notifications:	Execute Prompt Template
From Setup, find and select Approval Settings.
Turn on Dynamic Approval Notifications.
When turned on, dynamic approval notifications are used in the body of approval emails of approval email templates. The prompt template that's provided in the org is the only one used with dynamic approval notifications.
EXAMPLE Let's consider a scenario where a manufacturing company uses dynamic approval notifications to streamline its quoting process. When a sales rep submits a quote, the sales manager receives an email that includes key data generated based on the step's approval conditions and user context, like the total quote amount and discount percentage, and features an AI-powered summary highlighting critical factors, such as low profit margins. The manager can then review all necessary context and approve or reject the quote directly from their email—without logging into another system. This process reduces approval times by 30% and ensures all decisions are fully informed.

=== ARTICLE: ind.approvals_turn_on_slack_notifs.htm ===
---
article_id: ind.approvals_turn_on_slack_notifs.htm
title: Turn On Slack Notifications for Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_turn_on_slack_notifs.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_slack.htm
fetched_at: 2026-09-07
---

# Turn On Slack Notifications for Approvals

Connect Salesforce to your Slack workspace so that users can receive and act on approval requests in Slack.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals or Flow Approval Processes is enabled
USER PERMISSIONS NEEDED
To connect Salesforce and Slack:	Connect Salesforce with Slack
To manage approval settings:	Customize Application

Before you begin, connect a Salesforce org to your Slack workspace.

From Setup, find and select Approval Settings.
Turn on Notify Reviewers on Slack.
Turn on Notify Submitters on Slack.
SEE ALSO
Considerations for Approvals in Slack

=== ARTICLE: ind.approvals_turn_on_smart_approvals.htm ===
---
article_id: ind.approvals_turn_on_smart_approvals.htm
title: Turn On Smart Approvals
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_turn_on_smart_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_smart_approvals.htm
fetched_at: 2026-09-07
---

# Turn On Smart Approvals

To skip reviewing previously approved steps in an approval resubmission, turn on Smart Approvals.

From Setup, find and select Flows.
Open the flow that you use for managing approvals.
Select an approval step.
In the step’s properties tab, select Use Smart Approval.
To skip conditions from smart approvals evaluation, enter each condition number separated by a comma in the Smart Approval Skip Conditions field.
If you specify an invalid value or provide a resource, the conditions aren’t skipped during the evaluation.
Save your changes.

=== ARTICLE: ind.approvals_types_of_approvals.htm ===
---
article_id: ind.approvals_types_of_approvals.htm
title: Approval Workflow Types
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_types_of_approvals.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_building_blocks_of_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Approval Workflow Types

You can implement approvals in your workflow using two primary methods: serial or parallel. These are managed by setting up an approval chain, which is a label that identifies the specific group and sequence of approvers for a given process.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
Serial Approvals

Serial approvals create a sequential chain where approvers must complete their tasks one after another. Each approver waits for the previous approver to complete their task before receiving the task assigned to them. This method is particularly useful in complex workflows with multiple stages of approvals, as it ensures a specific order of review is followed.

To implement serial approvals, set the first approval step’s condition to When the stage starts, the step starts. The second approval step's condition must be set to When another step is marked Completed, the step starts, and it should watch for the approved or rejected status of the first step.

EXAMPLE Set up a serial chain named Finance Approvals. The process could involve an accountant, a finance manager, and a VP of Finance, each approving in sequence. The request will not go to the manager until the accountant has approved it.
Parallel Approvals

Parallel approvals, in contrast, send the task to multiple approvers at the same time. This approach is used when you need a group of people to review an item, but the order in which they do so does not matter.

The workflow can be configured in two common ways:

First Response: The task is completed (either approved or rejected) as soon as the first person in the parallel chain responds.
All Must Approve: The task is only considered approved after every individual in the parallel chain has given their approval.

Using parallel approvals, you can trigger multiple steps simultaneously as long as their conditions are satisfied at the same time. For instance, setting the condition for several different approval steps to When the stage starts, the step starts will cause them all to begin together. You can structure this by placing all parallel chains within a single Stage element, which allows each chain's steps to execute independently of the others.

Alternatively, you can group all steps of the same level into one Stage element to ensure all steps at that level are executed together before the flow moves on to the next. However, within any single parallel chain, you can still define serial sequencing (like Step B waiting for Step A) by using the same output-based conditions mentioned for serial approvals.

EXAMPLE A marketing campaign might be sent to the Head of Legal, the Head of PR, and the Head of Brand simultaneously. If configured for All Must Approve, the campaign can’t launch until all three have signed off.
Implement Serial and Parallel Approvers
To implement serial and parallel approvers, you’ll need to set up an approval chain.

=== ARTICLE: ind.approvals_use_advanced_approvals_in_a_quote.htm ===
---
article_id: ind.approvals_use_advanced_approvals_in_a_quote.htm
title: Use Advanced Approvals in a Quote
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_use_advanced_approvals_in_a_quote.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_building_blocks_of_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Use Advanced Approvals in a Quote

Now that your Approval Designer has created and activated an approval workflow for discounts, you’re ready to create quotes as a sales rep and use it.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled
USER PERMISSIONS NEEDED
To create a quote:	Create on Quotes
To submit a quote for approval:	Run Flows
To approve a quote:	Approval Admin

This example builds on the previous one, where we created an approval workflow called Discount Threshold Approval. We've also modified our Quote object’s page with the Apex classes and buttons required to trigger the approval process.

Here’s our scenario. Any quote discounted at 25% or above requires approval from a Sales Manager. Quotes with discounts larger than 50% also require approval from a Senior Vice President (SVP, Sales).

Follow the steps below to see how to create a quote and manage it's approval workflow.

Create a quote for the buyer (add products, specify discounts)
Submit your quote for approval
View and Manage Approvals
Create a Quote for Approvals

Let’s start by creating a quote and adding products to it. Then, add associated discounts to verify that the approval workflow triggers and routes as designed.

From the App Launcher, find and select Quotes.
Click New Quote.
On the quote page, click Browse Catalogs.
Select a catalog, and click Next.
Add products to your quote and click Save.
Provide a discount of over 50% to any product at the line item level.
Submit the Quote for Approval

When your quote is ready, you’ll need to submit it for approval. Notice that since one of the line items in the quote has a discount of 50%, the approval workflow will be triggered and the quote will be sent for approval.

Save your quote after making all pricing changes.
Click Submit for Approval. Note: The name of this button may be different if you provided a different name when you performed the Add Approval Button task.
Provide comments to aid the quote approval process.
Submit your quote for approval.
View and Manage Approvals

The Approvals home page helps your approval submitters and approvers to manage their approval work items.

If you can’t view the Approvals home page, ensure that your administrator grants you READ access on the ApprovalSubmission object to the user.
By default, sharing for the ApprovalSubmission object and related records is set to Private, which can be misconfigured. If public visibility is required, the administrator must ensure the related record has a Public Read access set. 

If you’re an approval submitter, click Manage My Approval Submissions. A list of all the approval requests made by the submitter along with their statuses is displayed.
If you’re an approval administrator, click Manage All Pending Approval Submissions.
Approval administrators can view all submissions and their statuses. They can also perform approval actions on behalf of other approvers.
If you’re an approver or a reviewer, click Review My Approval Work Items. Reviewers can approve or reject any pending quotes assigned to them. They can also navigate from the Approval Work Item record by clicking the Related Record ID, which will take them to the Approvals tab on the Quote record to approve or reject the quote.
Reviewers can also approve or reject an approval submission as a response to the email without going to the work item on your Approvals application.
Finally, if Smart Approvals is enabled, submissions that meet the workflow's conditions will be automatically approved.

If you’ve got multiple approvers, they’ll see assigned work items on their login.

=== ARTICLE: ind.approvals_use_the_stage_exit_condition.htm ===
---
article_id: ind.approvals_use_the_stage_exit_condition.htm
title: Use the Stage Exit Condition
source_url: https://help.salesforce.com/s/articleView?id=ind.approvals_use_the_stage_exit_condition.htm&type=5&release=264
release: 264
release_name: Winter '27
area: approvals
parent_article: ind.approvals_building_blocks_of_advanced_approvals.htm
fetched_at: 2026-09-07
---

# Use the Stage Exit Condition

Serial and approval workflows can easily get stuck in a “waiting” state if the Stage element's exit condition isn't configured properly. The problem occurs when the stage is set to wait for all steps to finish, as it can't account for conditional steps that were never triggered. This creates a deadlock.

REQUIRED EDITIONS
Available in: Lightning Experience
Available in: Enterprise, Unlimited, and Developer Editions where Advanced Approvals is enabled

For example, let's consider a discount approval stage with two steps:

Step 1
Required if the discount is greater than 10%
Step 2
Required if the discount is greater than 20%

If a sales rep submits a quote with a 15% discount, Step 1 will trigger and complete. However, Step 2 will never start. Since the stage is configured to wait for all steps to finish, it will get stuck waiting for Step 2, and the workflow can't move on.

To resolve this, you must define a smarter exit condition. In the Stage element, change the condition to When the specified requirements are met, the stage is marked Complete. This allows you to define the exact logic for when the stage should be considered complete by accounting for every possible scenario.

You can apply this logic by following steps as detailed in the Example: Configure an Approval Workflow topic with the values from this example. But, when you’re creating an approval stage, combine these three cases into a single custom requirement. The stage is marked complete when ANY of the following logic blocks is true:

Discount <= 10%. No approvals are necessary.

(OR)

(Discount > 10% AND Discount <= 20% AND Step 1 review is approved) Step 2 approvals aren’t necessary here.

(OR)

(Discount > 20% AND Step 1 AND Step 2 reviews are complete)

(OR)

(Discount > 20% AND Step 1 review has been rejected) Step 2 approvals aren’t necessary here.

The logic should look like this.

