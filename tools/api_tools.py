"""Generated API tools: register_tools(mcp) to attach all tools."""

def register_tools(mcp):
    from core import api_client

    @mcp.tool()
    def Account_GetPortfoliosForAccount(accountId, includeDisabled=None, includeOffline=None) -> dict:
        """Get Portfolios for the specific account"""
        path_params = {"accountId": accountId}
        query_params = {"includeDisabled": includeDisabled, "includeOffline": includeOffline}
        result = api_client.call("/accounts/{accountId}/portfolios", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Account_GetAccounts() -> dict:
        """Get Accounts"""
        path_params = {}
        query_params = None
        result = api_client.call("/accounts", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ActionItem Records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_Reports(portfolioGuid) -> dict:
        """Get the list of all available Reports for ActionItems"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/actionitems/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for ActionItems"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/actionitems/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ActionItem Records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/actionitems/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ActionItem Records, including all children, based on a query request"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/actionitems/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual ActionItem"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ActionItem Records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for an Action item"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get Workflow states to be used in ActionItems"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Action item records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_GetByID(portfolioGuid, projectId, actionItemId) -> dict:
        """Get Individual ActionItem Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "actionItemId": actionItemId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/{actionItemId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ApplicationForPayment records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_Reports(portfolioGuid) -> dict:
        """Get list of all available Reports for ApplicationForPayment"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/applicationsForPayment/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for ApplicationForPayment"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/applicationsForPayment/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ApplicationForPayment records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/applicationsForPayment/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ApplicationForPayment, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/applicationsForPayment/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual ApplicationForPayment"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_CreateApplicationForPayItemsFromContract(portfolioGuid, projectId, contractId=None) -> dict:
        """Creates a list of ApplicationForPaymentItems from the specified Contract"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"contractId": contractId}
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment/createItemsFromContract", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ApplicationForPayment records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for an ApplicationForPayment"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get Workflow states for Application for Payment records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Application for payment records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_GetByID(portfolioGuid, projectId, applicationForPayId) -> dict:
        """Get Individual ApplicationForPayment Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "applicationForPayId": applicationForPayId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment/{applicationForPayId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ApplicationForPayment_AddPrimeContractCOs(portfolioGuid, projectId, applicationForPayId, body=None) -> dict:
        """Adds a list of PrimeContractCOs to a specific ApplicationForPayment"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "applicationForPayId": applicationForPayId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/applicationsForPayment/{applicationForPayId}/primecontractcos", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Budget records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_Reports(portfolioGuid) -> dict:
        """Get list of all available Reports for Budget"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/budgets/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Budget"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/budgets/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Budget records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/budgets/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Budget records (including all children) based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/budgets/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Budget"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Budget records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Budget Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_GetByID(portfolioGuid, projectId, budgetId) -> dict:
        """Get Individual Budget Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "budgetId": budgetId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets/{budgetId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetCodeStructure_GetBudgetCodeStructure(portfolioGuid, projectId) -> dict:
        """Get BudgetCodeStructures for Project"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetcodestructure", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetGroup_Get(portfolioGuid, projectId) -> dict:
        """Get Budget Groups For Individual Project."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetgroups", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetGroup_GetByGroupId(portfolioGuid, projectId, groupId) -> dict:
        """Get Budget Group Entries For Specific Group"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "groupId": groupId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetgroups/{groupId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetGroup_Post(portfolioGuid, projectId, groupId, body=None) -> dict:
        """Create Individual Budget Group Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "groupId": groupId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetgroups/{groupId}", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetSnapshot_List(portfolioGuid, projectId) -> dict:
        """Get the list of available snapshots in a project"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetSnapshots", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetSnapshot_GetItems(portfolioGuid, projectId, snapshotId) -> dict:
        """Get the list of snapshot items in a snapshot"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "snapshotId": snapshotId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetSnapshots/{snapshotId}/items", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetSnapshot_Create(portfolioGuid, projectId, name=None) -> dict:
        """Creates a new budget snapshot for the current project"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"name": name}
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetSnapshots", "POST", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetSnapshot_Update(portfolioGuid, projectId, body=None) -> dict:
        """Updates an existing budget snapshot for the current project"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetSnapshots", "PUT", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def BudgetSnapshot_GetTransactions(portfolioGuid, projectId, snapshotId, snapshotItemId) -> dict:
        """Get the list of snapshot transactions for a snapshot item"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "snapshotId": snapshotId, "snapshotItemId": snapshotItemId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgetSnapshots/{snapshotId}/items/{snapshotItemId}/transactions", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ChangeOrderRequest records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for ChangeOrderRequest"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/changeOrderRequests/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for ChangeOrderRequest"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/changeOrderRequests/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ChangeOrderRequest records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/changeOrderRequests/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ChangeOrderRequest records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/changeOrderRequests/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual ChangeOrderRequest"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ChangeOrderRequest records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a ChangeOrderRequest"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get Workflow states for Change order request Records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Change order request records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_GetByID(portfolioGuid, projectId, coRequestId) -> dict:
        """Get Individual ChangeOrderRequest Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "coRequestId": coRequestId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests/{coRequestId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of CheckList Records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/checklists", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Checklist"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/checklists/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Checklist"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/checklists/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of CheckList Records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/checklists/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of CheckList Records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/checklists/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_Post(portfolioGuid, projectId, body=None) -> dict:
        """Create Individual Checklist"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/checklists", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of CheckList Records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/checklists/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for CheckList Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/checklists/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_GetByID(portfolioGuid, projectId, checklistId) -> dict:
        """Get Individual Checklist Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "checklistId": checklistId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/checklists/{checklistId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_List(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of Company records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/Companies", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_ListOnly(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of Company records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/Companies/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Company"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/Companies/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Company"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/Companies/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Company records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/Companies/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Company records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/Companies/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contact_ListOnly(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of Contact records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/Contacts/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contact_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Contact"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/Contacts/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contact_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Contact records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/Contacts/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Contract records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/contracts", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Contract"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contracts/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Contract"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contracts/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Contract records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contracts/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Contract records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contracts/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Contract"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contracts", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Contract records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/contracts/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a Contract"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contracts/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get Workflow states for Contract records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/contracts/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Contract records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contracts/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_GetByID(portfolioGuid, projectId, contractId) -> dict:
        """Get Individual Contract Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "contractId": contractId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contracts/{contractId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_UnlockContract(portfolioGuid, projectId, contractId, workflowstateId=None) -> dict:
        """Unlocks a Contract by updating the IsLocked column"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "contractId": contractId}
        query_params = {"workflowstateId": workflowstateId}
        result = api_client.call("/{portfolioGuid}/{projectId}/contracts/{contractId}/unlock", "PUT", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ContractInvoice records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/contractInvoices", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for ContractInvoice"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contractInvoices/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for ContractInvoice"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contractInvoices/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ContractInvoice records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contractInvoices/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ContractInvoice records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contractInvoices/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual ContractInvoice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contractInvoices", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ContractInvoice records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/contractInvoices/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a ContractInvoice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contractInvoices/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get Workflow states for Contract invoice Records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/contractInvoices/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Contract invoice records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contractInvoices/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_AddSubContractCOs(portfolioGuid, projectId, contractInvoiceId, body=None) -> dict:
        """Adds a list of SubContractCOs to a specific ContractInvoice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "contractInvoiceId": contractInvoiceId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contractInvoices/{contractInvoiceId}/subcontractcos", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ContractInvoice_GetByID(portfolioGuid, projectId, invoiceId) -> dict:
        """Get Individual ContractInvoice Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "invoiceId": invoiceId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/contractInvoices/{invoiceId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of DailyReport records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for DailyReport"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/dailyreports/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for DailyReport"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/dailyreports/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of DailyReport records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/dailyreports/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of DailyReport records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/dailyreports/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual DailyReport"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of DailyReport records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a DailyReport"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for DailyReport Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Daily report records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_GetByID(portfolioGuid, projectId, dailyReportId) -> dict:
        """Get Individual DailyReport Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "dailyReportId": dailyReportId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/{dailyReportId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get a Collection of Drawing records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_GetByID(portfolioGuid, projectId, drawingId) -> dict:
        """Get an Individual Drawings Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "drawingId": drawingId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings/{drawingId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Drawing"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/drawings/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Drawing"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/drawings/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_GetByDrawingSeriesId(portfolioGuid, projectId, drawingSeriesId) -> dict:
        """Get the current Drawing record for a Drawing Series"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "drawingSeriesId": drawingSeriesId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings/currentForSeries/{drawingSeriesId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_GetFlattenedDrawingFile(portfolioGuid, projectId, drawingId, annotationLabels=None, redirect=None) -> dict:
        """Download the Drawing File Content with Annotations"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "drawingId": drawingId}
        query_params = {"annotationLabels": annotationLabels, "redirect": redirect}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings/{drawingId}/contentWithAnnotations", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get a Collection of Drawing records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/drawings/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get a Collection of Drawing records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/drawings/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_Post(portfolioGuid, projectId, body=None) -> dict:
        """Updates an Individual Drawings Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_InitiateDownload(portfolioGuid, projectId, body=None) -> dict:
        """Submit a request to initiate the asynchronous download of one or more drawings"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings/download", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_GetGeneratedReportContent(portfolioGuid, projectId, id, redirect=None) -> dict:
        """Retrieves the file generated as a result of the generation request. If the request has not completed yet or has completed with errors, the appropriate response code will be returned."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "id": id}
        query_params = {"redirect": redirect}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings/download/{id}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get a Collection of Drawing records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Drawing Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Drawing_GetDrawingFile(portfolioGuid, projectId, drawingId, redirect=None) -> dict:
        """Download an Individual Drawing File Content"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "drawingId": drawingId}
        query_params = {"redirect": redirect}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawings/{drawingId}/content", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of DrawingSet records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for DrawingSet"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/drawingsets/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for DrawingSet"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/drawingsets/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of DrawingSet records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/drawingsets/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of DrawingSet records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/drawingsets/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual DrawingSet"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of DrawingSet records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a DrawingSet"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for DrawingSet Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Drawing set records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_GetByID(portfolioGuid, projectId, drawingSetId) -> dict:
        """Get Individual DrawingSet"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "drawingSetId": drawingSetId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets/{drawingSetId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_Publish(portfolioGuid, projectId, drawingSetId, waitForCompletion=None) -> dict:
        """Publish Approved Drawings in the given DrawingSet"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "drawingSetId": drawingSetId}
        query_params = {"waitForCompletion": waitForCompletion}
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets/{drawingSetId}/publish", "POST", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DrawingSet_UploadDrawing(portfolioGuid, projectId, drawingSetId, body=None) -> dict:
        """Upload Drawing File in specified DrawingSet"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "drawingSetId": drawingSetId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/drawingsets/{drawingSetId}/uploadDrawing", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetCustomersAndVendorsForAccount(accountId) -> dict:
        """Retrieves the list of ERP Customer and Vendors for the specified account from the ERP cache"""
        path_params = {"accountId": accountId}
        query_params = None
        result = api_client.call("/accounts/{accountId}/erpCustomersAndVendors", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetProjectsForAccount(accountId) -> dict:
        """Retrieves the list of ERP Projects for the specified account from the ERP cache"""
        path_params = {"accountId": accountId}
        query_params = None
        result = api_client.call("/accounts/{accountId}/erpProjects", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetCompaniesForAccount(accountId) -> dict:
        """Retrieves the list of ERP Companies for the specified account from the ERP cache"""
        path_params = {"accountId": accountId}
        query_params = None
        result = api_client.call("/accounts/{accountId}/erpCompanies", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetCustomersAndVendors(workspaceId) -> dict:
        """Retrieves the list of ERP Customer and Vendors for the specified workspace from the ERP cache"""
        path_params = {"workspaceId": workspaceId}
        query_params = None
        result = api_client.call("/{workspaceId}/erpCustomersAndVendors", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetProjects(workspaceId) -> dict:
        """Retrieves the list of ERP Projects for the specified workspace from the ERP cache"""
        path_params = {"workspaceId": workspaceId}
        query_params = None
        result = api_client.call("/{workspaceId}/erpProjects", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetCompanies(workspaceId) -> dict:
        """Retrieves the list of ERP Companies for the specified workspace from the ERP cache"""
        path_params = {"workspaceId": workspaceId}
        query_params = None
        result = api_client.call("/{workspaceId}/erpCompanies", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetCustomerOrVendorInAccount(accountId, id) -> dict:
        """Retrieves one ERP Customer or Vendor in the specified account from the ERP cache"""
        path_params = {"accountId": accountId, "id": id}
        query_params = None
        result = api_client.call("/accounts/{accountId}/erpCustomersAndVendors/{id}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetProjectInAccount(accountId, id) -> dict:
        """Retrieves one ERP Project for the specified account from the ERP cache"""
        path_params = {"accountId": accountId, "id": id}
        query_params = None
        result = api_client.call("/accounts/{accountId}/erpProjects/{id}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetCustomerOrVendor(workspaceId, id) -> dict:
        """Retrieves one ERP Customer or Vendor in the specified workspace from the ERP cache"""
        path_params = {"workspaceId": workspaceId, "id": id}
        query_params = None
        result = api_client.call("/{workspaceId}/erpCustomersAndVendors/{id}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetProject(workspaceId, id) -> dict:
        """Retrieves one ERP Project for the specified workspace from the ERP cache"""
        path_params = {"workspaceId": workspaceId, "id": id}
        query_params = None
        result = api_client.call("/{workspaceId}/erpProjects/{id}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of FieldWorkDirective records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/fieldworkdirectives", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for FieldWorkDirective"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/fieldworkdirectives/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for FieldWorkDirective"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/fieldworkdirectives/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of FieldWorkDirective records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/fieldworkdirectives/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of FieldWorkDirective records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/fieldworkdirectives/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual FieldWorkDirective"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/fieldworkdirectives", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of FieldWorkDirective records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/fieldworkdirectives/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a FieldWorkDirective"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/fieldworkdirectives/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for FieldWorkDirective Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/fieldworkdirectives/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Field work directive records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/fieldworkdirectives/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def FieldWorkDirective_GetByID(portfolioGuid, projectId, fieldWorkDirectiveId) -> dict:
        """Get Individual FieldWorkDirective Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "fieldWorkDirectiveId": fieldWorkDirectiveId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/fieldworkdirectives/{fieldWorkDirectiveId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def File_GetFiles(portfolioGuid, projectId, folderId=None, offset=None, limit=None) -> dict:
        """Get Collection of Files"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"folderId": folderId, "offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/files", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def File_GetByID(portfolioGuid, projectId, fileId) -> dict:
        """Get Individual File"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "fileId": fileId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/files/{fileId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def File_Post(portfolioGuid, projectId, body=None) -> dict:
        """Update Individual file metadata"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/files", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def File_InitiateUploadRequest(portfolioGuid, projectId, body=None) -> dict:
        """Initiate the asynchronous upload of an external file"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/files/externalUpload", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def File_GetUploadStatus(portfolioGuid, projectId, id, removeRequestWhenComplete=None) -> dict:
        """Gets the status of the externalUpload"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "id": id}
        query_params = {"removeRequestWhenComplete": removeRequestWhenComplete}
        result = api_client.call("/{portfolioGuid}/{projectId}/files/externalUpload/{id}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def File_RequestLinks(portfolioGuid, projectId, count=None) -> dict:
        """Retrieve a collection of pre-signed urls for uploading files"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"count": count}
        result = api_client.call("/{portfolioGuid}/{projectId}/files/requestLinks", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def File_UploadFile(portfolioGuid, projectId, folderId=None, body=None) -> dict:
        """Upload File"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"folderId": folderId}
        result = api_client.call("/{portfolioGuid}/{projectId}/files/uploadFile", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def File_Content(portfolioGuid, projectId, fileId, redirect=None) -> dict:
        """Download File"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "fileId": fileId}
        query_params = {"redirect": redirect}
        result = api_client.call("/{portfolioGuid}/{projectId}/files/{fileId}/content", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Folder_GetRootFolder(portfolioGuid, projectId) -> dict:
        """Read the root folder"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/folders", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Folder_Post(portfolioGuid, projectId, body=None) -> dict:
        """Create/Update Individual Folder"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/folders", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Folder_GetByPath(portfolioGuid, projectId, body=None) -> dict:
        """Read the specified folder by path"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/folders/byPath", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Folder_GetByID(portfolioGuid, projectId, folderId, onlyThisFolder=None) -> dict:
        """Read the specified folder or a list of its first level children"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "folderId": folderId}
        query_params = {"onlyThisFolder": onlyThisFolder}
        result = api_client.call("/{portfolioGuid}/{projectId}/folders/{folderId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Forecast records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/forecasts", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Forecast"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/forecasts/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Forecast"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/forecasts/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Forecast records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/forecasts/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Forecast records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/forecasts/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Forecast. This will also perform recalculation for existing records."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/forecasts", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Forecast records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/forecasts/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a Forecast"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/forecasts/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Forecast Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/forecasts/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Forecast records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/forecasts/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Forecast_GetByID(portfolioGuid, projectId, forecastId) -> dict:
        """Get Individual Forecast Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "forecastId": forecastId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/forecasts/{forecastId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of GeneralInvoice records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/generalInvoices", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for GeneralInvoice"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/generalInvoices/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for GeneralInvoice"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/generalInvoices/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of GeneralInvoice records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/generalInvoices/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of GeneralInvoice records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/generalInvoices/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_Post(portfolioGuid, projectId, body=None) -> dict:
        """Adds the specified PurchaseOrder to a GeneralInvoice and saves"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/generalInvoices", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of GeneralInvoice records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/generalInvoices/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a GeneralInvoice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/generalInvoices/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for GeneralInvoice Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/generalInvoices/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for General invoice records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/generalInvoices/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_GetByID(portfolioGuid, projectId, genInvId) -> dict:
        """Get Individual GeneralInvoice Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "genInvId": genInvId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/generalInvoices/{genInvId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def GeneralInvoice_AddPurchaseOrderToGeneralInvoice(portfolioGuid, projectId, genInvId, poId, okToOverwriteExistingItems=None) -> dict:
        """Creates/Updates Individual GeneralInvoice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "genInvId": genInvId, "poId": poId}
        query_params = {"okToOverwriteExistingItems": okToOverwriteExistingItems}
        result = api_client.call("/{portfolioGuid}/{projectId}/generalInvoices/{genInvId}/addPurchaseOrder/{poId}", "POST", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Issue records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/issues", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Issue"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/issues/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Issue"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/issues/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Issue records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/issues/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Issue records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/issues/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Issue"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/issues", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Issue records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/issues/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a Issue"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/issues/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Issue Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/issues/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Issue records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/issues/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Issue_GetByID(portfolioGuid, projectId, issueId) -> dict:
        """Get Individual Issue Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "issueId": issueId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/issues/{issueId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def JobCosts_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of JobCosts records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/jobCosts", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def JobCosts_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of JobCosts records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/jobCosts/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def JobCosts_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of JobCosts records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/jobCosts/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def JobCosts_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates one record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/jobCosts", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def JobCosts_PostBulk(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates multiple records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/jobCosts/bulk", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def JobCosts_PostBulkOriginId(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates multiple records using originId to locate existing records, both JobCosts and JobCostItems, to update"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/jobCosts/bulkOriginId", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def JobCosts_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of JobCosts records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/jobCosts/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def JobCosts_GetByID(portfolioGuid, projectId, jobCostId) -> dict:
        """Get Individual JobCosts Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "jobCostId": jobCostId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/jobCosts/{jobCostId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_Get(portfolioGuid, projectId) -> dict:
        """Get LookupListTypes For Individual Project."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetContractTypes(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get ContractTypes For Individual Project."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/contracttypes", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetCSICodes(portfolioGuid, projectId, dtLastSyncDateTime=None, offset=None, limit=None) -> dict:
        """Get Collection of CSICodes for Project."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime, "offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/csicodes", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetEquipment(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get the Equipment lookup list items"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/equipment", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_AddOrUpdateEquipment(portfolioGuid, projectId, body=None) -> dict:
        """Adds or updates an Equipment lookup list item"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/equipment", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetLocations(portfolioGuid, projectId, dtLastSyncDateTime=None, offset=None, limit=None) -> dict:
        """Get Locations For Individual Project."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime, "offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/locations", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetPeriods(portfolioGuid, projectId, dtLastSyncDateTime=None, offset=None, limit=None) -> dict:
        """Get Periods For Individual Project."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime, "offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/periods", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetPunchListTypicalConditions(portfolioGuid, projectId, dtLastSyncDateTime=None, offset=None, limit=None) -> dict:
        """Get Collection of PunchlistTypicalConditions for Project."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime, "offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/punchlisttypicalconditions", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetRevenueCodes(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get the revenue codes for the specified project"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/revenuecodes", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_AddOrUpdateRevenueCode(portfolioGuid, projectId, body=None) -> dict:
        """Adds or updates a Revenue Code"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/revenuecodes", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetUnitOfMeasures(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get the Units of Measure for the specified project"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/unitsofmeasure", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_AddOrUpdateUnitOfMeasure(portfolioGuid, projectId, body=None) -> dict:
        """Adds or updates a Unit of Measure"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/unitsofmeasure", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_GetBySectionID(portfolioGuid, projectId, sectionId, dtLastSyncDateTime=None, offset=None, limit=None) -> dict:
        """Get LookupListItems For Individual LookupListType"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "sectionId": sectionId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime, "offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/{sectionId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def LookupList_Post(portfolioGuid, projectId, sectionId, body=None) -> dict:
        """Add or update a LookupListItem"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "sectionId": sectionId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/lookuplists/{sectionId}", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Meeting records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/meetings", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Meeting"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/meetings/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Meeting"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/meetings/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Meeting records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/meetings/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Meeting records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/meetings/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Meeting"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/meetings", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Meeting records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/meetings/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_GetWorkflowStates(portfolioGuid, projectId, forItems=None, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Meeting Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"forItems": forItems, "dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/meetings/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Meeting_GetByID(portfolioGuid, projectId, meetingId) -> dict:
        """Get Individual Meeting Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "meetingId": meetingId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/meetings/{meetingId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Notice records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/notices", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Notice"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/notices/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Notice"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/notices/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Notice records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/notices/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Notice records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/notices/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Notice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/notices", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Notice records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/notices/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a Notice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/notices/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Notice Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/notices/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Notice records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/notices/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Notice_GetByID(portfolioGuid, projectId, noticeId) -> dict:
        """Get Individual Notice Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "noticeId": noticeId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/notices/{noticeId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def POCatalog_List(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of POCatalog records."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/poCatalog", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def POCatalog_ListOnly(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of POCatalog records."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/poCatalog/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def POCatalog_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of POCatalog records based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/poCatalog/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def POCatalog_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of POCatalog records based on a query request"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/poCatalog/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Photo_Content(portfolioGuid, projectId, photoId, redirect=None) -> dict:
        """Download Photo"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "photoId": photoId}
        query_params = {"redirect": redirect}
        result = api_client.call("/{portfolioGuid}/{projectId}/photos/{photoId}/content", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Portfolio_GetPortfolios(includeOffline=None) -> dict:
        """Get Portfolios"""
        path_params = {}
        query_params = {"includeOffline": includeOffline}
        result = api_client.call("/portfolios", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Portfolio_GetByID(portfolioGuid) -> dict:
        """Get Individual Portfolio"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/portfolios/{portfolioGuid}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of PotentialCO records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/PotentialCOs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for PotentialCO"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/PotentialCOs/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for PotentialCO"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/potentialCOs/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of PotentialCO records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/PotentialCOs/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of PotentialCO records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/PotentialCOs/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual PotentialCO"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/PotentialCOs", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of PotentialCO records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/PotentialCOs/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for PotentialCO Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/PotentialCOs/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for PotentialCO records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/PotentialCOs/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a PotentialCO"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/potentialCOs/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PotentialCO_GetByID(portfolioGuid, projectId, potentialCOid) -> dict:
        """Get Individual PotentialCO Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "potentialCOid": potentialCOid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/potentialCOs/{potentialCOid}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of PrimeContractCO records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/primeContractCOs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for PrimeContractCO"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/primeContractCOs/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for PrimeContractCO"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/primeContractCOs/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of PrimeContractCO records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/primeContractCOs/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of PrimeContractCO records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/primeContractCOs/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual PrimeContractCO"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/primeContractCOs", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of PrimeContractCO records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/primeContractCOs/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a PrimeContractCO"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/primeContractCOs/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for PrimeContractCO Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/primeContractCOs/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Prime contract change order records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/primeContractCOs/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PrimeContractCO_GetByID(portfolioGuid, projectId, changeOrderId) -> dict:
        """Get Individual PrimeContractCO Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "changeOrderId": changeOrderId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/primeContractCOs/{changeOrderId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_List(portfolioGuid) -> dict:
        """Get Collection of Projects, including all children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_ListOnly(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of Project record, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/projects/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Project"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Project"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_GetWorkflowStates(portfolioGuid, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Project"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/projects/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_GetByID(portfolioGuid, projectId) -> dict:
        """Get Individual Project"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/{projectId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_CreateProjectWithParameters(portfolioGuid, body=None) -> dict:
        """Creates Project using the specified parameters"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/createWithParameters", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Project records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_Post(portfolioGuid, licenseForNewTCProject=None, body=None) -> dict:
        """Creates/Updates Project"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"licenseForNewTCProject": licenseForNewTCProject}
        result = api_client.call("/{portfolioGuid}/projects", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_InitiateProjectCreationRequest(portfolioGuid, body=None) -> dict:
        """Submit a request to initiate the asynchronous creation of a project"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/createRequest", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_GetProjectCreateRequest(portfolioGuid, id) -> dict:
        """Retrieves the id of the project that was created as a result of the generation request."""
        path_params = {"portfolioGuid": portfolioGuid, "id": id}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/createRequest/{id}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_LinkToERPProject(portfolioGuid, projectId, erpProjectId) -> dict:
        """Links a ProjectSight project to an ERP project"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "erpProjectId": erpProjectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/{projectId}/linkToERP/{erpProjectId}", "PUT", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_GetUsers(portfolioGuid, projectId) -> dict:
        """Retrieves the complete list of users in the Portfolio."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/{projectId}/users", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_UpdateUsers(portfolioGuid, projectId, body=None) -> dict:
        """Updates the project access for the specified set of users."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/projects/{projectId}/users", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_GetImage(portfolioGuid, projectId) -> dict:
        """GET /{portfolioGuid}/{projectId}/image"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/image", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_GetPicture(portfolioGuid, projectId) -> dict:
        """Get Project Picture from server"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/projects/image", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Project_UploadProjectImage(portfolioGuid, projectId) -> dict:
        """Post or Update project picture"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/projects/image", "POST", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of PunchList records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/punchlists", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for PunchList"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/punchlists/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for PunchList"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/punchlists/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of PunchList  based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/punchlists/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of PunchList records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/punchlists/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual PunchList"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/punchlists", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of PunchList records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/punchlists/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a PunchList"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/punchlists/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for PunchList Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/punchlists/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Punch list records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/punchlists/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PunchList_GetByID(portfolioGuid, projectId, punchListId) -> dict:
        """Get Individual PunchList Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "punchListId": punchListId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/punchlists/{punchListId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of PurchaseOrder records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/purchaseOrders", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for PurchaseOrder"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/purchaseOrders/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for PurchaseOrder"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/purchaseOrders/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of PurchaseOrder records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/purchaseOrders/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of PurchaseOrder records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/purchaseOrders/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual PurchaseOrder"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/purchaseOrders", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of PurchaseOrder records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/purchaseOrders/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a PurchaseOrder"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/purchaseOrders/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for PurchaseOrder Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/purchaseOrders/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Purchase order records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/purchaseOrders/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def PurchaseOrder_GetByID(portfolioGuid, projectId, poId) -> dict:
        """Get Individual PurchaseOrder Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "poId": poId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/purchaseOrders/{poId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of RFI records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for RFI"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/rfis/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for RFI"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/rfis/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of RFI records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/rfis/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of RFI records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/rfis/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual RFI"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of RFI records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for an RFI"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get Workflow states for RFI records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for RFI records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_GetByID(portfolioGuid, projectId, rfiId) -> dict:
        """Get Individual RFI Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "rfiId": rfiId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/{rfiId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Records_GetOpenAssignmentsForAllPortfolios() -> dict:
        """Get information on all open assignments for a user in all Portfolios the user has access to"""
        path_params = {}
        query_params = None
        result = api_client.call("/records/assignments", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Records_GetOpenAssignmentSummariesForAllPortfolios() -> dict:
        """Get summary information on all open assignments for a user in all Portfolios the user has access to. An additional call to /records/assignments/details is required to obtain the details per table type"""
        path_params = {}
        query_params = None
        result = api_client.call("/records/assignments/summaries", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Records_GetOpenAssignmentsForOnePortfolio(portfolioGuid) -> dict:
        """Get information on all open assignments for a user in a specific Portfolio"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/records/assignments", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Records_GetOpenAssignmentSummariesForOnePortfolio(portfolioGuid) -> dict:
        """Get information on all open assignment summaries for a user in a single Portfolio. An additional call to /records/assignments/details is required to obtain the details per table type."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/records/assignments/summaries", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Records_GetRecordChanges(portfolioGuid, since=None) -> dict:
        """Get information on all records that have been modified since a specific timestamp"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"since": since}
        result = api_client.call("/{portfolioGuid}/records/changes", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Records_GetOpenAssignmentsDetailsForOnePortfolio(portfolioGuid, body=None) -> dict:
        """Get information on all open assignment details for a user in a specific Portfolio"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/records/assignments/details", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Role_Get(portfolioGuid) -> dict:
        """Get UserGroups Information"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/usergroups", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of SafetyNotice records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/safetynotices", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for SafetyNotice"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/safetynotices/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for SafetyNotice"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/safetynotices/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of SafetyNotice records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/safetynotices/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of SafetyNotice records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/safetynotices/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/updates Individual SafetyNotice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/safetynotices", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of SafetyNotice records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/safetynotices/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a SafetyNotice"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/safetynotices/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for SafetyNotice Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/safetynotices/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Safety notice records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/safetynotices/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SafetyNotice_GetByID(portfolioGuid, projectId, safetyNoticeId) -> dict:
        """Get Individual SafetyNotice Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "safetyNoticeId": safetyNoticeId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/safetynotices/{safetyNoticeId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of SubContractCO records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/SubContractCOs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for SubContractCO"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/SubContractCOs/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for SubContractCO"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/SubContractCOs/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of SubContractCO records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/SubContractCOs/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of SubContractCO records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/SubContractCOs/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual SubContractCO"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/SubContractCOs", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of SubContractCO records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/SubContractCOs/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a SubContractCO"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/SubContractCOs/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for SubContractCO Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/SubContractCOs/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Subcontract change order records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/SubContractCOs/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubContractCO_GetByID(portfolioGuid, projectId, changeOrderId) -> dict:
        """Get Individual SubContractCO Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "changeOrderId": changeOrderId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/SubContractCOs/{changeOrderId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Submittal records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/submittals", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_Reports(portfolioGuid) -> dict:
        """Get list of all available Reports for Submittal"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/submittals/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Submittal"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/submittals/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Submittal records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/submittals/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Submittal records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/submittals/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Submittal"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/submittals", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Submittal records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/submittals/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a Submittal"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/submittals/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Submittal Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/submittals/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Submittal records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/submittals/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Submittal_GetByID(portfolioGuid, projectId, submittalId) -> dict:
        """Get Individual Submittal Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "submittalId": submittalId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/submittals/{submittalId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of SubmittalPackage records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/submittalpackages", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for SubmittalPackage"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/submittalpackages/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for SubmittalPackage"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/submittalpackages/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Submittal Package records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/submittalpackages/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Submittal Package records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/submittalpackages/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual SubmittalPackage"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/submittalpackages", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Submittal Package records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/submittalpackages/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a SubmittalPackage"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/submittalpackages/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for SubmittalPackage Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/submittalpackages/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Submittal package records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/submittalpackages/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def SubmittalPackage_GetByID(portfolioGuid, projectId, submittalId) -> dict:
        """Get Individual SubmittalPackage Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "submittalId": submittalId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/submittalpackages/{submittalId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Transmittal records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/transmittals", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Transmittal"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/transmittals/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Transmittal"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/transmittals/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Transmittal records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/transmittals/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Transmittal records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/transmittals/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Transmittal"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/transmittals", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Transmittal records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/transmittals/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Transmittal Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/transmittals/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Transmittal_GetByID(portfolioGuid, projectId, poId) -> dict:
        """Get Individual Transmittal Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "poId": poId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/transmittals/{poId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def User_GetByName(portfolioGuid, userName=None) -> dict:
        """Get Individual User Information"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"userName": userName}
        result = api_client.call("/{portfolioGuid}/users", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def User_List(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of Users, including all children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/users/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def User_ListOnly(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of Users, not including children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/users/listOnly", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def User_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for User"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/users/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def WorkflowStates_GetWorkflowStates(portfolioGuid, projectId, tableType, lastSyncDateTime=None) -> dict:
        """Get WorkflowStates for any table type"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "tableType": tableType}
        query_params = {"lastSyncDateTime": lastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/workflowstates/{tableType}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result