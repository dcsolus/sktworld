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
  - **No arguments**.
7. **my_average_data_usage**:
  - Description: Useful for providing average data usage from last 3 months data usage.
  - **No arguments**.
8. **remaining_data_refill_coupons**:
  - Description: Useful for guiding about remaining data refill coupons.
  - **No arguments**.
9. **remaining_data_gift**:
  - Description: Useful for guiding whether data can be gifted and how many times it remains available.
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
  - Description: Useful when compare features of multiple SKTelecom mobile plans.
  - **Optional Arguments**:
  - `keywords` (array of objects)
17. **COMPARE_CHANGE_MY_MOBILE_PLAN**:
  - Description: Useful for comparing my plan to other plans.
  - **Optional Arguments**:
    - `keywords` (object)
18. **SEARCH_MOBILE_PLAN**:
  - Description: This function searches or offer mobile plans based on a specific keyword.
  - **Optional Arguments**:
    - `keywords` (object)
19. **check_plan_availability**:
  - Description: This function is used to check whether user can subscribe to the given plan.
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
  - Description: Useful for recommending plans to users.
  - **Optional Arguments**:
      - `keywords` (object)
100. **FAQ_FROM_MULTI_SOURCE**
  - Description: Retrieves data for mobile questions. Useful for answer the general mobile question. Useful for handling processes that are not handled by other
  defined functions.
  - **No arguments**.
"""