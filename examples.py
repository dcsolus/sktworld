examples = """### EXAMPLES
user: "가입 중인 요금제"
assistant: {"name": "my_mobile_plan", "arguments": {}}

user: "내가 현재 어떤 요금상품을 이용중인 거야?"
assistant: {"name": "my_mobile_plan", "arguments": {}}

user: "내가 어떤 요금제 사용해?"
assistant: {"name": "my_mobile_plan", "arguments": {}}

user: "나 지금 부가서비스 가입 중인 거 알려줄래? "
assistant: {"name": "my_subscribed_add_ons", "arguments": {}}

user: "지금 부가서비스 뭔지 알려줄래? "
assistant: {"name": "my_subscribed_add_ons", "arguments": {}}

user: "부가요금제 어떤 거 이용 중인지 알려줄래? "
assistant: {"name": "my_subscribed_add_ons", "arguments": {}}

user: "나 이번 달 청구 요금 얼마야? "
assistant: {"name": "my_billing_charge", "arguments": {}}

user: "지난 달 사용 요금 알려줘 "
assistant: {"name": "my_billing_charge", "arguments": {}}

user: "이번 달 청구 요금 얼마야? "
assistant: {"name": "my_billing_charge", "arguments": {}}

user: "나의 실시간 요금 "
assistant: {"name": "my_realtime_billing_charge", "arguments": {}}

user: "지금까지 요금 얼마? "
assistant: {"name": "my_realtime_billing_charge", "arguments": {}}

user: "많이 쓰면 안되는데,내 실시간 청구 요금 얼만지 알려줘 "
assistant: {"name": "my_realtime_billing_charge", "arguments": {}}

user: "나 일반적으로 어느 정도 데이터 사용해?"
assistant: {"name": "my_average_data_usage", "arguments": {}}

user: "내 데이터 사용 패턴 알고 싶어"
assistant: {"name": "my_average_data_usage", "arguments": {}}

user: "나는 데이터를 어떻게 쓰고있어?"
assistant: {"name": "my_average_data_usage", "arguments": {}}

user: "내 미사용 데이터 알려줘 "
assistant: {"name": "my_realtime_data_usage", "arguments": {}}

user: "잔여 데이터 "
assistant: {"name": "my_realtime_data_usage", "arguments": {}}

user: "데이터 현재까지 얼마나 썼어? "
assistant: {"name": "my_realtime_data_usage", "arguments": {}}

user: "지금까지 내가 사용한 선물하기 데이터 이용량이 어떻게 돼? "
assistant: {"name": "my_shared_data_usage", "arguments": {}}

user: "나의 공유 데이터 잔여량이 얼마나 되는지 알려줘 "
assistant: {"name": "my_shared_data_usage", "arguments": {}}

user: "내가 사용중인 실시간 테더링 데이터의 잔여량이 얼마나 되는지 확인해줘 "
assistant: {"name": "my_shared_data_usage", "arguments": {}}

user: "현재 미사용 데이터 쿠폰 조회 "
assistant: {"name": "remaining_data_refill_coupons", "arguments": {}}

user: "지금 데이터 쿠폰을 내가 얼마나 가지고 있는지 확인해봐 "
assistant: {"name": "remaining_data_refill_coupons", "arguments": {}}

user: "데이터 리필 쿠폰 확인 "
assistant: {"name": "remaining_data_refill_coupons", "arguments": {}}

user: "이번 달에 내가 데이터 추가로 선물 하려 하는데 가능해?"
assistant: {"name": "remaining_data_gift", "arguments": {}}

user: "데이터를 추가로 선물 하고싶어"
assistant: {"name": "remaining_data_gift", "arguments": {}}

user: "나 데이터 선물하기 가능해?"
assistant: {"name": "remaining_data_gift", "arguments": {}}

user: "잔여 가족공유데이터 "
assistant: {"name": "t_family_data_usage", "arguments": {}}

user: "나 T가족데이터 남은 데이터량 실시간으로 알려줘 "
assistant: {"name": "t_family_data_usage", "arguments": {}}

user: "가족모아데이터 잔여량 얼만큼 남았나? "
assistant: {"name": "t_family_data_usage", "arguments": {}}

user: "가족공유데이터에 적용되어 있는 공유 설정을 다른 걸로 바꿀 수 있나? "
assistant: {"name": "t_family_data_change_shared_amount", "arguments": {}}

user: "T가족공유데이터에서 공유량 바꾸기 "
assistant: {"name": "t_family_data_change_shared_amount", "arguments": {}}

user: "나 궁금한데, T가족데이터 공유 바꿀 수 없어? "
assistant: {"name": "t_family_data_change_shared_amount", "arguments": {}}

user: "지금 내 무약정플랜 잔여 포인트가 얼마나 되는지 확인해볼 수 있어? "
assistant: {"name": "remaining_no_contract_plan_points", "arguments": {}}

user: "무약정 포인트들이 지금까지 얼마만큼 있을지 궁금하네 "
assistant: {"name": "remaining_no_contract_plan_points", "arguments": {}}

user: "약정없이 적립 된 포인트 "
assistant: {"name": "remaining_no_contract_plan_points", "arguments": {}}

user: "내 청구요금 전 월 대비 증가했을지 궁금해 "
assistant: {"arguments": "{}", "name": "billing_charge_analyze_summary"}

user: "나의 현재 휴대폰요금을 얼마나 많이 추가 지불할 것 같니 "
assistant: {"arguments": "{}", "name": "billing_charge_analyze_summary"}

user: "최근에 변동된 내 청구요금 내역 알려줘 "
assistant: {"arguments": "{}", "name": "billing_charge_analyze_summary"}

user: "할인금액이 늘었는지 지난 달과 비교해서 알고싶어 "
assistant: {"arguments": "{}", "name": "billing_charge_analyze_discount"}

user: "최근에 변동된 내 할인요금 내역 알려줘 "
assistant: {"arguments": "{}", "name": "billing_charge_analyze_discount"}

user: "내 이번 달 할인금액 얼만큼 더 늘어날지 예상 가능? "
assistant: {"arguments": "{}", "name": "billing_charge_analyze_discount"}

user: "데이터 사용량이 증가했는지 이전 월에 비해 어때? "
assistant: {"arguments": "{}", "name": "billing_charge_data_usage"}

user: "내 이번 달 데이터 사용량 얼만큼 더 늘어날지 예상 가능? "
assistant: {"arguments": "{}", "name": "billing_charge_data_usage"}

user: "나의 이번에 데이터 소비량이 얼마나 더 줄어들었는지 궁금해 "
assistant: {"arguments": "{}", "name": "billing_charge_data_usage"}

user: "band 데이터 퍼펙트와 요금제와 band 데이터 퍼펙트S 요금제는 어떻게 다른가요? "
assistant: {"name": "COMPARE_BETWEEN_MOBILE_PLAN", "arguments": {"plans": ["band 데이터 퍼펙트", "band 데이터 퍼펙트S"] } }

user: "0플랜 히어로랑 0플랜 슈퍼히어로 요금제의 세부 사항 어떻게 다른거지? "
assistant: {"name": "COMPARE_BETWEEN_MOBILE_PLAN", "arguments": {"plans": ["0플랜 히어로", "0플랜 슈퍼히어로"] } }

user: "뉴실버요금제와 T끼리 어르신은 다른게 뭐지? "
assistant: {"name": "COMPARE_BETWEEN_MOBILE_PLAN", "arguments": {"plans": ["뉴실버요금제", "T끼리 어르신"] } }

user: " 내가 지금 온가족 행복플랜85 요금제인데 온가족 행복플랜78으로 변경하면 뭐가 달라져? "
assistant: {"name": "COMPARE_CHANGE_MY_MOBILE_PLAN", "arguments": {"plan": "온가족 행복플랜78"} }

user: " 지금 내가 안심음성500 요금제인데 안심음성350으로 변경하면 뭐가 달라져? "
assistant: {"name": "COMPARE_CHANGE_MY_MOBILE_PLAN", "arguments": {"plan": "안심음성350"} }

user: " 내가 골든에이지15으로 바꾸면 어떻게 달라져? "
assistant: {"name": "COMPARE_CHANGE_MY_MOBILE_PLAN", "arguments": {"plan": "골든에이지15"} }

user: "3G 전국민 무한 85 요금제가 알고싶어 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"productName": "3G 전국민 무한 85"}} }

user: "3G T끼리팅55 요금제에 대해서 설명해줄래? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"productName": "3G T끼리팅55"}} }

user: "0 청년 69 요금제의 내용을 자세하게 설명 좀 해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"productName": "0 청년 69"}} }

user: "내가 전화 160분 넘게 사용할 수 있는 요금제 플랜 알고 싶어 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCall": "160분"}} }

user: "전화 업무를 많이 하는데나한테 통화 무제한으로 이용할 수 있는 요금제 제공해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCall": "무제한"}} }

user: "내가 통화를 충분하게 사용가능한 모바일 요금제 알고싶어 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCall": "충분하게"}} }

user: "나 영상통화 제공하는 요금제 가입하려고 하는데 알려줘"
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVideoOrValueAddedCall": ""}} }

user: "영상통화 무제한으로 제공하는 요금제 찾아줘"
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVideoOrValueAddedCall": "무제한"}} }

user: "영상통화 넉넉한 요금제"
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVideoOrValueAddedCall": "넉넉한"}} }

user: "아빠랑 충분하게 무료 통화할 수 있는 요금제 어떤 거 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCallTospecifiedNumbers": "충분하게"}} }

user: "아빠랑 충분하게 통화할 수 있는 요금제 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCallTospecifiedNumbers": "충분하게"}} }

user: "남친이랑 넉넉하게 무제한 통화할 수 있는 요금제 알려줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCallTospecifiedNumbers": "넉넉하게"}} }

user: "나 데이터 많이 제공하는 요금제 뭐 있는지 찾고있어 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedData": "많이"}} }

user: "나 데이터 제한없는 요금제 알려줘 아껴쓰기 싫다"
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedData": "제한없는"}} }

user: "나 기본 데이터 50GB가 넘게 사용가능한 모바일 요금제를 알고싶어 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedData": "50GB가 넘게"}} }

user: "테더링 데이터 용량을 30기가 초과로 이용할 수 있는 모바일 요금제 어떤 것이 있는 거야? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "30기가 초과"}} }

user: "테더링 용량을 무제한으로 쓸 수 있는 요금제 알려줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "무제한"}} }

user: "테더링 용량을 10GB 이상 쓸 수 있는 요금제 뭐 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "10GB 이상"}} }

user: "데이터 쉐어를 모자라지 않게 줄 수 있는 요금제 뭐가있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "모자르지 않게"}} }

user: "50기가 이상 데이터 공유 가능한 요금제 찾아줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "50기가 이상"}} }

user: "데이터 공유를 무제한으로 할 수 있는 요금제 찾고 있는데 알려줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "무제한"}} }

user: "별도 요금 없이 심야에 무제한 쓸 수 있는 옵션데이터 요금제 있을까? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"optionData": ""}} }

user: "심야 전용 데이터 프리인 요금제 있나? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"optionData": ""}} }

user: "돈 따로 안내고 지정된 시간에 무한으로 쓰는 옵션데이터 요금제 설명해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"optionData": ""}} }

user: "현 시점에 데이터 쿠폰을 제공하는 요금 플랜을 확인하고 싶어 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"availableAmountForDataOptionRefill": ""}} }

user: "당장 데이터 리필쿠폰 많이 제공하는 휴대폰 요금제 정리 좀 해줘~  더 많으면 좋겠어"
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"availableAmountForDataOptionRefill": "많이"}} }

user: "지금 데이터 리필쿠폰 사용가능량이 삼십기가 이상인 요금 상품은 어떤건지 알아봐줄래? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"availableAmountForDataOptionRefill": "삼십기가 이상"}} }

user: "요금 플랜 중에서 나눠 줄 수 있는 데이터가 넉넉한 거 뭐가 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"maximumAmountForSharing": "넉넉한"}} }

user: "나 데이터 나눔 하는게 가능한 요금 상품 뭐 뭐 있는지 궁금해 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"maximumAmountForSharing": ""}} }

user: "모바일 데이터 나눠주기가 허용되는 용량이 500mb 정도 되는 요금 상품 소개해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"maximumAmountForSharing": "2GB 보다 많은"}} }

user: "문자를 무한대로 보낼 수 있는 요금 제를 사용하려고 하는데 안내해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedText": "무한대로"}} }

user: "문자를 무제한으로 쓸 수 있는  요금제를 가입하려고  하는데 뭐가 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedText": "무제한"}} }

user: "내가 기본제공 문자가 들어있는 요금 상품을 쓰고 하는데 어떤게 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"includedText": ""}} }

user: "월정액 요금이 경제적인 리스트 검색 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"monthlyPrice": "경제적인"}} }

user: "돈 많이 안내는 요금제 말해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"monthlyPrice": "돈 많이 안내는"}} }

user: "월정액 고액 상품 목록 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"monthlyPrice": "고액"}} }

user: "5G 요금제 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"generation": "5G"}} }

user: "3G 쓸 수 있는 폰에 어떤 요금제가 괜찮아? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"generation": "3G"}} }

user: "무슨 4G 요금 상품이 있나 알 수 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"generation": "4G"}} }

user: "요금 상품 중 속도가 줄지 않는 거 뭐 뭐야? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"dataQoS": ""}} }

user: "데이터를 많이 사용해도 속도 제한 없는 모바일 플랜 알려줄래? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"dataQoS": ""}} }

user: "월정액 포함 데이터 전부 써도 요금 부과되는 거 없이 계속해서 이용할 수 있는 모바일 플랜 안내해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"dataQoS": ""}} }

user: "쓰고 싶은게 청년 혜택이 있는건데 뭐야? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"benefit": "청년"}} }

user: "복지할인 혜택이 있는 요금 플랜을 알고 싶은데 뭐뭐 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"benefit": "복지할인"}} }

user: "이용하고 싶은게 보험할인 혜택이 있는건데 어떤게 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"benefit": "보험할인"}} }

user: "LTE 복지 말해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"lineup": "LTE 복지"}} }

user: "소리누리에 대해 나에게 구체적으로 말해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"lineup": "소리누리"}} }

user: "올인원 커플 설명해줄래? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"lineup": "올인원 커플"}} }

user: "T월드에서 할 수 있는 요금제 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingChannel": "T월드"}} }

user: "판매점에서 어느 요금제 가능해? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingChannel": "판매점"}} }

user: "지점에서 할 수 있는 요금제 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingChannel": "지점"}} }

user: "요금제 중 유심 전용인거 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingTypeEligibility": ""}} }

user: "티다이렉트에서 가능한 USIM 요금제 알 수 있어? "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingTypeEligibility": ""}} }

user: "요금제 중 유심 개통되는거 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingTypeEligibility": ""}} }

user: "나 스마트폰 전용 요금제 어떤 게 있나 궁금해 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDevice": "스마트폰"}} }

user: "나에게 스마트워치에서 쓸 수 있는 요금제 추천해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDevice": "스마트워치"}} }

user: "나 스마트 기능 없는 폰에서 사용할 수 있는 요금 상품 뭐 뭐 인지 설명해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDevice": "스마트 기능 없는 폰"}} }

user: "아이폰 11 이거에 사용 가능한 요금 상품 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDeviceAlias": "아이폰 11"}} }

user: "요금 상품중에 갤럭시 Z 폴드2에 가입 가능한거 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDeviceAlias": "갤럭시 Z 폴드2"}} }

user: "구입한게 갤럭시 WIN인데  요금 서비스 가능한거 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDeviceAlias": "갤럭시 WIN"}} }

user: "가입 자격 되면 쓰는 요금제 중에 대학생을 위해서 만든 특정 요금제 설명해줘 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"specialCustomerOnboard": "대학생"}} }

user: "군인이 선택할 수 있는 요금제 찾기 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"specialCustomerOnboard": "군인"}} }

user: "특정된 사람만 가능한 요금제 중에 어린이가 가입 가능한 특별 요금제 궁금해 "
assistant: {"name": "SEARCH_MOBILE_PLAN", "arguments": {"keywords": {"specialCustomerOnboard": "어린이"}} }

user: "나도 올인원 64 요금 상품으로다가 바로 신청할께 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"productName": "올인원 64"}} }

user: "마이투넘버 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"productName": "골든에이지15"}} }

user: "골든에이지15 신청할께 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"productName": "T시그니처 Classic"}} }

user: "나 음성 가능한 요금제로 변경하려는데 찾아줄래? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCall": ""}} }

user: "전화 업무를 많이 하는데, 나 통화 무제한으로 이용할 수 있는 요금제 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCall": "무제한"}} }

user: "나 음성통화 없는 요금제 가입하고 싶은데 알려줄래? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCall": ""}} }

user: "영상통화 부족하지 않게 주는 요금제 가입하고 싶어 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVideoOrValueAddedCall": "부족하지 않게"}} }

user: "영상통화 충분히 주는 요금 서비스 쓰고 싶어 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVideoOrValueAddedCall": "충분히"}} }

user: "돈 안내고 500분 보다 많이 영상통화 주는 요금 서비스 안내해줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVideoOrValueAddedCall": "500분 보다 많이"}} }

user: "엄마랑 오랫동안 통화해도 되는 요금제 할 수 있는 거 알려줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCallTospecifiedNumbers": "오랫동안"}} }

user: "특정인이랑 제한없이 200분 이상 통화해도 되는 요금제 나도 가입할 수 있나? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCallTospecifiedNumbers": "200분 이상"}} }

user: "아빠랑 안부족하게 통화할 수 있는 요금제 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedVoiceCallTospecifiedNumbers": "안부족하게"}} }

user: "데이터 많은 요금제 쓰고 싶어 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedData": "많은"}} }

user: "내게 기본 제공 데이터를 넉넉하게 퍼주는 요금 프로그램으로 가입할거거든, 뭐가 나을지 추천해줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedData": "넉넉하게"}} }

user: "데이터 무제한 요금제인거 찾아줘. 나 가입하고 싶거든~ "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedData": "무제한"}} }

user: "노트북이랑 연결해서 데이터 쓰는 요금제 중에 제공량 많은 걸로 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "많은"}} }

user: "나 테더링 데이터 제공되는 요금제 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": ""}} }

user: "나 테더링 무제한으로 쓸 수 있는 요금제 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "무제한"}} }

user: "내가 가입할 수 있는 데이터 공유할 수 있는 요금제 알려줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": ""}} }

user: "데이터 공유 무제한인 요금제 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "무제한"}} }

user: "나 데이터 충분하게 공유할 수 있는 요금제  가입하고 싶은데 뭐가 있어? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedDataForSharingAndTethering": "충분하게"}} }

user: "내꺼 변경할 건데,  매일 3시간 무제한 데이터 옵션이 있는 요금제 찾아줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"optionData": ""}} }

user: "내꺼 변경할건데,  일요일에 데이터 계속 쓸 수 있는 모바일 플랜 뭐있어? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"optionData": ""}} }

user: "추가 요금 없이 내가 정한 시간에 무한 제공 되는 옵션데이터 요금제 가입시켜줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"optionData": ""}} }

user: "현재 데이터 리필 용량이 30GB 이상인 요금제 쓰고 싶은데, 뭐 있는지 알려줘 용량을 늘려야겠어"
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"availableAmountForDataOptionRefill": "30GB 이상"}} }

user: "데이터 리필 쿠폰 요금제 쓰고싶어 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"availableAmountForDataOptionRefill": ""}} }

user: "지금 데이터 리필을 할 수 있는 요금제를 쓰고싶은데, 찾아주라 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"availableAmountForDataOptionRefill": ""}} }

user: "나 데이터 나눔 하는게 가능한 요금 상품으로 변경할건데 제공해줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"maximumAmountForSharing": ""}} }

user: "내가 가입할 수 있는 요금제 중에 데이터를 많이 선물 할 수 있는 거 찾아줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"maximumAmountForSharing": "많이"}} }

user: "나 이용 가능한 요금제 중 데이터를 부족하지 않게 줘도 문제 없는 거 보여줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"maximumAmountForSharing": "부족하지 않게"}} }

user: "문자 기본제공 50건 정도 되는 모바일 요금제 쓰고 싶은데 안내해줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedText": "50건 정도"}} }

user: "문자 한도없이 이용할 수 있는 요금 서비스 이용하고 싶어 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedText": "한도없이"}} }

user: "문자 기본제공 포함된 요금 서비스 쓰고 싶은데 알려줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"includedText": ""}} }

user: "5만원 미만인 요금제 할 수 있는 거 알려줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"monthlyPrice": "5만원 미만인"}} }

user: "돈 많이 안내는 요금제 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"monthlyPrice": "돈 많이 안내는"}} }

user: "월정액이 3만원 이하인 요금제 가입하고 싶어 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"monthlyPrice": "3만원 이하"}} }

user: "지금 바로 4G만 가능한 요금 상품으로 변경할거거든, 뭐든 있다면 말해줘바 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"generation": "4G"}} }

user: "LTE 사용했던 기기에 바꿔보려고. 어떤 요금 상품 추천해? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"generation": "LTE"}} }

user: "3G 기기 요금 상품으로 바꾸고 싶어 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"generation": "3G"}} }

user: "월정액 데이터 다 사용해도 요금 부과되는 거 없고 끊기지 않는 요금 상품으로 가입하고 싶어 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"dataQoS": ""}} }

user: "데이터 속도가 줄지 않는 요금 상품 쓸 수 있어? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"dataQoS": ""}} }

user: "월정액 포함 데이터 전부 써도 요금 부과되는 거 없이 계속해서 이용할 수 있는 모바일 플랜으로 변경할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"dataQoS": ""}} }

user: "리필 혜택 요금플랜 가입할게 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"benefit": "리필"}} }

user: "내가 사용할 수 있는 넷플릭스 혜택 포함된 요금제 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"benefit": "넷플릭스"}} }

user: "커피 혜택 포함된 요금제 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"benefit": "커피"}} }

user: "T끼리 요금제로 변경하고 싶은데, 특장점 있으면 말해줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"lineup": "T끼리"}} }

user: "band YT 나 가입할래 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"lineup": "band YT"}} }

user: "T시그니처 요금제로 바꾸고 싶어. 부가설명 좀 해주셈 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"lineup": "T시그니처"}} }

user: "나는 오프라인 매장에서 어느 요금제 가입 할 수 있는 거야? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingChannel": "오프라인 매장"}} }

user: "나 홈쇼핑에서 실시간 가입 진행할 수 있는 요금제 있어? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingChannel": "홈쇼핑"}} }

user: "내가 11번가에서 바로 가입 할 수 있는 요금제 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingChannel": "11번가"}} }

user: "티다이렉트에서 가능한 USIM 요금제로 변경해볼래. 당장 알 수 있어? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingTypeEligibility": ""}} }

user: "티다이렉트샵에서 가입 가능한 유심 전용 요금제 지금 알려줘. 변경하고 싶어. "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingTypeEligibility": ""}} }

user: "요금 상품 중 유심으로 가입되는거 쓸거야. "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingTypeEligibility": ""}} }

user: "나 스마트폰 전용 모바일 플랜 중 뭐 쓸 수 있는지 가르쳐줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDevice": "스마트폰"}} }

user: "나에게 탭에서 사용 가능한 요금 플랜 중에 어느 거 쓰는게 가능한지 보여줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDevice": "탭"}} }

user: "내게 태블릿피씨 용 요금 플랜 중 뭐 뭐 가입 가능한지 말해줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDevice": "태블릿피씨"}} }

user: "IPAD2 사용하는데 요금제 가입할 수 있는거 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDeviceAlias": "IPAD2"}} }

user: "Apple Watch 5 쓰고 있는데 사용할 수 있는 요금 플랜 말해줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDeviceAlias": "Apple Watch 5"}} }

user: "IPHONE 15 PRO MAX 사용하는데 가입할 수 있는 요금제 알려줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"onboardingDeviceAlias": "IPHONE 15 PRO MAX"}} }

user: "대학생 전용 요금제 변경 가능해? "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"specialCustomerOnboard": "대학생"}} }

user: "나 요금제 중에 초등학생 전용 요금제 가입시켜줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"specialCustomerOnboard": "초등학생"}} }

user: "온라인전용으로 가입할 수 있는 요금제 가입되나 봐줘 "
assistant: {"name": "AVAILABLE_MOBILE_PLAN", "arguments": {"keywords": {"specialCustomerOnboard": "온라인전용"}} }

user: "바꿀때가 된 것 같은데 내 요금제 쓰는거 변경 가능한 시점이 언제인지 알려줘 "
assistant: {"name": "changable_date_for_plan", "arguments": {} }

user: "요금 상품 변경 날짜 "
assistant: {"name": "changable_date_for_plan", "arguments": {} }

user: "매일 3시간 데이터 혜택에서 주말 데이터 혜택으로 지금 변경하고 싶어 "
assistant: {"name": "changable_date_for_plan", "arguments": {} }

user: "나 지금 요금제 변경 알림 신청이 가능한지 알려줘 "
assistant: {"name": "plan_auto_change_date", "arguments": {} }

user: "모바일 요금제 변경 안내 신청 "
assistant: {"name": "plan_auto_change_date", "arguments": {} }

user: "매일3시간 데이터 혜택 변경 알림 설정해줘 "
assistant: {"name": "plan_auto_change_date", "arguments": {} }

user: "지금 요금제 언제까지 쓸 수 있어? "
assistant: {"name": "plan_auto_change_date_alarm", "arguments": {} }

user: "지금 쓰는 요금제 몇 살까지 쓸 수 있어? "
assistant: {"name": "plan_auto_change_date_alarm", "arguments": {} }

user: "나이 지나면 무슨 요금제로 바뀌어? "
assistant: {"name": "plan_auto_change_date_alarm", "arguments": {} }

user: "음성 기본 제공되는 요금제 중에 나한테 맞는 걸로 추천해줘 "
assistant: {"name": "recommend_plans", "arguments":  {"keywords": {"includedVoiceCall": ""}} }

user: "부족하지 않게 영상통화 할 수 있는 요금 서비스를 나한테 어울리는 걸로 제공해줄래? "
assistant: {"name": "recommend_plans", "arguments":  {"keywords": {"includedVideoOrValueAddedCall": "부족하지 않게"}} }

user: "내 연락처에 있는 사람이랑 통화 제한 없이 할 수 있는 요금제를 나랑 맞는 걸로 안내해줘 "
assistant: {"name": "recommend_plans", "arguments":  {"keywords": {"includedVoiceCallTospecifiedNumbers": "제한 없이"}} }

user: "기본 제공 데이터가 있는 핸드폰 요금제 어떤게 있는지 나한테 적절한 걸로 보여줘 "
assistant: {"name": "recommend_plans", "arguments":  {"keywords": {"includedData": ""}} }

user: "테더링을 10GB 초과로 써도 되는 모바일 플랜 중에 어떤거 추천해줄 수 있어? "
assistant: {"name": "recommend_plans", "arguments":  {"keywords": {"includedDataForSharingAndTethering": "10GB 초과"}} }

user: "문자를 무한대로 보낼 수 있는 요금제를 알아보려고 해. 요금제 선택에 도움을 줄 수 있어? "
assistant: {"name": "recommend_plans", "arguments":  {"keywords": {"includedText": "무한대로"}} }

user: "매달 나가는 금액이 8만원보다 적은 요금 상품 중에 나한테 어울리는 거 알려줄래? "
assistant: {"name": "recommend_plans", "arguments":  {"keywords": {"monthlyPrice": "8만원보다 적은"}} }

user: "5GX플래티넘 요금제로 요금제 바꾸면 요금 얼마나 더 내야 돼? "
assistant: {"name": "estimated_billing_charge_compare_to_current", "arguments": {"keywords": {"productName": "5GX플래티넘"}} }

user: "음성통화 제공하는 요금제로 변경할때 예상요금 알려줘 "
assistant: {"name": "estimated_billing_charge_compare_to_current", "arguments": {"keywords": {"includedVoiceCall": ""}} }

user: "데이터가 너무 부족해. 데이터 무제한 요금제로 바꾸면 예상 지불 금액은? "
assistant: {"name": "estimated_billing_charge_compare_to_current", "arguments": {"keywords": {"includedData": "무제한"}} }

user: "넷플릭스 혜택이 있는 요금제로 가입하면 요금이 어떻게 변해? "
assistant: {"name": "estimated_billing_charge_compare_to_current", "arguments": {"keywords": {"benefit": "넷플릭스"}} }

user: "시니어가 쓸 수 있는 요금제를 사용할때 요금을 알려줘 "
assistant: {"name": "estimated_billing_charge_compare_to_current", "arguments": {"keywords": {"specialCustomerOnboard": "시니어"}} }

user: "요금제 가입시 매달 내는 돈을 알려줘 "
assistant: {"name": "estimated_billing_charge_compare_to_current", "arguments": {} }

user: "티다이렉트샵에서 가입 가능한 유심 전용 요금제를 사용할건데 요금이 달라져? "
assistant: {"name": "estimated_billing_charge_compare_to_current", "arguments": {"keywords": {"onboardingTypeEligibility": ""}} }

user: "내가 지금 쓰고 있는 요금제에서 테더링 데이터가 30기가 이상인 요금제로 변경 가능한가? "
assistant: {"name": "check_plan_availability", "arguments": {"keywords": {"includedDataForSharingAndTethering": "30기가 이상"}} }

user: "아이폰 16 출시했으니까 그걸로 요금제 변경할래 "
assistant: {"name": "check_plan_availability", "arguments": {"keywords": {"onboardingDevice": "아이폰 16"}} }

user: "내 요금제를 다이렉트5G 55이나 다이렉트플랜중에 기본제공데이터가 100기가 넘는 요금제로 변경 가능한지 알려줘 "
assistant: {"name": "check_plan_availability", "arguments": {"keywords": {"productName": "다이렉트5G 55"}} }
""" 