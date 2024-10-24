function_desc = """
1. **my_mobile_plan**:
  - Description: Useful when get my mobile plan.
  - **No arguments**.
2. **my_subscribed_add_ons**:
  - Description: Useful for providing your subscribed add-ons(가입 된 부가서비스).
  - **No arguments**.
3. **my_billing_charge**:
  - Description: Useful when you need to provide recent billing charges (for last month's usage).
  - **No arguments**.
4. **my_realtime_billing_charge**:
  - Description: Useful when you need to provide real-time billing charges based on current month usage.
  - **No arguments**.
5. **my_realtime_data_usage**:
  - Description: Useful when guide real-time data usage/residuals.
  - **No arguments**.
6. **my_shared_data_usage**:
  - Description: Useful when you need to provide shared and tethered data usage or residuals.
  - **No arguments**
7. **my_average_data_usage**:
  - Description: Useful for providing average data usage from last 3 months data usage.
  - **No arguments**.
8. **remaining_data_refill_coupons**:
  - Description: Useful for guiding about remaining data refill coupons.
  - **No arguments**.
9. **remaining_data_gift**:
  - Description: This function informs the customer about the remaining number of times they can gift data within a month.
  - Use Cases:
    Example Questions: "How many times can I gift data this month?", "Can I still gift data?", "How many times can I gift data within the family?", "How many times can I gift T data this month?"
  - **No arguments**.
10. **t_family_data_usage**:
  - Description: Useful for guiding status of 'T가족모아데이터' data usage.
  - **No arguments**.
11. **t_family_data_change_shared_amount**:
  - Description: Useful for changing to 'T가족모아데이터' shared data amount.
  - **No arguments**.
12. **remaining_no_contract_plan_points**:
  - Description: Useful for checking points remaining on no-contract plans(무약정플랜).
  - **No arguments**.
13. **billing_charge_analyze_summary**:
  - Description: Useful for providing how user's billing history compares to the previous month.
  - **No arguments**.
14. **billing_charge_analyze_discount**:
  - Description: Useful for providing details of the discount on billing charges and the increase/decrease compared to last month.
  - **No arguments**.
15. **billing_charge_data_usage**:
  - Description: Useful for providing data usage for this month and compare to last month.
  - **No arguments**.
16. **COMPARE_BETWEEN_MOBILE_PLAN**:
  - Description: This function compares the details and features of multiple plans that the customer is interested in.
  - Use Cases:
    Example Questions: "How is the Prime plan different from the PrimePlus plan?", "What are the differences between the Direct5G 52 plan and a plan that includes more than 3 hours of designated calls while using LTE?"
  - **Optional Arguments**:
  - `keywords` (array of objects)
17. **COMPARE_CHANGE_MY_MOBILE_PLAN**:
  - Description: This function compares the details and features of the customer's current plan with the plans they are interested in.
  - Use Cases:
    Example Questions: "What are the differences if I switch to the Prime plan?", "Compare my current plan with a plan costing over 60,000 won per month."
  - **Optional Arguments**:
    - `keywords` (object)
18. **SEARCH_MOBILE_PLAN**:
  - Description: This function searches for plans based on the conditions mentioned by the customer and provides relevant information.
  - Use Cases:
    When customers seek to find a list of plans meeting specific conditions.
    Example Questions: "I want a plan that offers sufficient video call minutes and includes tethering data", "Find me a 5GX plan with Netflix benefits."
    When customers want to change their plan without specifying additional conditions.
    Example Questions: "I want to change my plan."
  - **Optional Arguments**:
    - `keywords` (object)
19. **check_plan_availability**:
  - Description: This function checks if a specific plan is available for the customer to subscribe to or change to, based on their conditions, and provides relevant information.
  - Use Cases:
    When customers inquire if they can use a plan that meets certain conditions.
    Example Questions: "I want to use a plan that offers sufficient video call minutes and tethering data", "Can I switch to the PrimePlus plan?"
    When customers want to know if any available plans meet their conditions.
    Example Questions: "What plans can I use?", "What are the 5G plans around 100,000 won that I can switch to?"
  - **Optional Arguments**:
    - `keywords` (list of object)
    - `phoneNumber` (string)
            - Description: Phone number to check for availability (digits only).
    - **Required Arguments**:
    - `requestForMultiline` (bool)
        - Description: Whether the user made a request for multilines.
20. **changable_date_for_plan**:
  - Description: Useful for checking how long user have to stay on user's current plan and when user can change it.
  - **No arguments**.
21. **plan_auto_change_date**:
  - Description: This function is used to inform about when user's plan is automatically changed and what plan it's being changed to.
  - **No arguments**.
22. **plan_auto_change_date_alarm**:
  - Description: Useful for signing up for an alert when a user can change user's plan.
  - **No arguments**.
23. **recommend_plans**:
  - Description: This function recommends plans that align with the customer's conditions.
  - Use Cases:
    When customers directly request plan recommendations without any specific conditions.
    Example Questions: "Recommend a plan for me", "Help me find a plan that suits me", "Can you suggest a plan?"
    When customers want recommendations based on specific conditions or criteria.
    Example Questions: "Recommend a plan with FLO benefits", "Suggest a plan with Netflix benefits within the 5GX plans."
  - **Optional Arguments**:
      - `keywords` (object)
24. **estimated_billing_charge_compare_to_current:
  - Description: This function compares the estimated billing charges of the sought-after plan with the current plan and provides detailed information.
  - Use Cases:
    Inquiring about the estimated billing changes when switching to a specific plan with certain conditions.
    Example Questions: "How will my bill change if I switch to a plan with Netflix benefits?", "What are the billing impacts if I switch to a plan with unlimited data?"
    Inquiring about the billing impacts of changing to a new plan without specifying conditions.
    Example Questions: "How much will my bill increase if I change my plan?", "What will my new bill be if I switch to a cheaper plan?"
    **Optional Arguments**
      - `keywords` (object)
100. **FAQ_FROM_MULTI_SOURCE**
  - Description: Retrieves data for mobile questions. Useful for answer the general mobile question. Useful for handling processes that are not handled by other
  defined functions.
  - **No arguments**.
"""