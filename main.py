import streamlit as st

st.title("첫 배포 확인 👋")
st.write("여기까지 보이면 배포 성공입니다.")

import streamlit as st

# 1. 페이지 기본 설정 (귀여운 파비콘과 타이틀)
st.set_page_config(
    page_title="말랑퐁당 MBTI 여행 추천",
    page_icon="✈️",
    layout="centered"
)

# 2. 커스텀 CSS (사랑스러운 핑크&파스텔 테마 스타일링)
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 설정 */
    .main {
        background-color: #FFF5F7;
    }
    
    /* 타이틀 카드 스타일 */
    .header-card {
        background: linear-gradient(135deg, #FF9A9E 0%, #FECFEF 100%);
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        color: white;
        box-shadow: 0px 10px 20px rgba(255, 154, 158, 0.3);
        margin-bottom: 25px;
    }
    
    /* 메인 제목 */
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* 결과 카드 스타일 */
    .result-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #FFD1DC;
        box-shadow: 0px 8px 15px rgba(255, 182, 193, 0.2);
        margin-top: 20px;
    }
    
    /* 태그 스타일 */
    .tag {
        display: inline-block;
        background-color: #FFE4E1;
        color: #FF1493;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.9rem;
        font-weight: bold;
        margin-right: 5px;
        margin-bottom: 10px;
    }

    /* 스트림릿 버튼 커스텀 */
    .stButton>button {
        background: linear-gradient(135deg, #FFB6C1 0%, #FF69B4 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 12px 25px;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0px 5px 10px rgba(255, 105, 180, 0.3);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 15px rgba(255, 105, 180, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI별 귀여운 여행지 데이터 베이스
mbti_travel_data = {
    "ISTJ": {
        "destination": "🇯🇵 일본 교토",
        "concept": "차분하고 완벽한 질서의 힐링 여행 🍵",
        "description": "계획표대로 착착! 고즈넉한 정원과 깔끔한 거리에서 정갈한 휴식을 즐길 수 있어요.",
        "tags": ["#알찬계획", "#정갈함", "#고즈넉한풍경", "#말랑말랑산책"],
        "tip": "분단위로 짜놓은 일정표대로 움직일 때 엔돌핀이 솟구쳐요!"
    },
    "ISFJ": {
        "destination": "🇨🇭 스위스 인터라켄",
        "concept": "동화 속 아늑한 마을로 떠나는 여행 🏔️",
        "description": "따뜻하고 아기자기한 풍경 속에서 마음까지 보송보송해지는 평화로운 휴양지예요.",
        "tags": ["#동화같은풍경", "#마음치유", "#친절한사람들", "#포근함"],
        "tip": "기차 창밖을 바라보며 핫초코 한 잔 마시는 매력에 빠져보세요."
    },
    "INFJ": {
        "destination": "🇨🇿 체코 프라하",
        "concept": "감성과 낭만이 넘치는 비밀스러운 여행 🏰",
        "description": "조용한 골목길, 노을 지는 까를교 위에서 오롯이 나의 내면과 대화할 수 있는 곳이에요.",
        "tags": ["#감성폭발", "#낭만골목", "#깊은생각", "#예술의거리"],
        "tip": "작은 일기장을 챙겨가서 카페에서 느낀 감정을 적어보세요."
    },
    "INTJ": {
        "destination": "🇮🇸 아이슬란드 레이캬비크",
        "concept": "신비로운 우주를 탐험하는 지적 여행 🌌",
        "description": "오로라와 빙하! 대자연의 경이로움 속에서 깊은 통찰과 탐구를 즐겨보세요.",
        "tags": ["#오로라탐사", "#웅장한자연", "#조용한탐험", "#지적호기심"],
        "tip": "완벽하게 조사해둔 철저한 경로로 탐험을 시작해보세요!"
    },
    "ISTP": {
        "destination": "🇳🇿 뉴질랜드 퀸스타운",
        "concept": "스릴 가득! 자유로운 익스트림 여행 🏂",
        "description": "번지점프부터 스카이다이빙까지! 몸으로 직접 느끼는 짜릿한 자유로움이 기다려요.",
        "tags": ["#액티비티만점", "#자유로운영혼", "#스릴만점", "#멋진자연"],
        "tip": "너무 복잡한 계획보단 그날 마음 내키는 액티비티를 선택하세요."
    },
    "ISFP": {
        "destination": "🇮🇩 인도네시아 발리",
        "concept": "느릿느릿 여유롭고 누워있는 감성 휴양 🌴",
        "description": "예쁜 카페, 파도 소리, 붉은 노을 아래서 느긋하게 뒹굴거리며 예술적 감성을 채워요.",
        "tags": ["#느림의학학", "#선셋맛집", "#요가와힐링", "#감성샷"],
        "tip": "알람을 끄고 일어나고 싶을 때 일어나는 것이 핵심 포인트!"
    },
    "INFP": {
        "destination": "🇹🇭 태국 치앙마이",
        "concept": "몽글몽글 감성 충전 한 달 살기 여행 ☕",
        "description": "아기자기한 소품샵, 예쁜 카페에서 조용히 책을 읽고 아침 시장을 거니는 로망이 이뤄져요.",
        "tags": ["#몽글몽글감성", "#예쁜소품샵", "#평화로운일상", "#힐링라이프"],
        "tip": "마음에 드는 카페에 앉아 멍때리는 시간을 꼭 가져보세요."
    },
    "INTP": {
        "destination": "🇬🇧 영국 런던",
        "concept": "호기심을 자극하는 박물관&역사 여행 🏛️",
        "description": "세계적인 박물관과 미술관이 가득! 흥미로운 지식과 문화를 마음껏 탐구해봐요.",
        "tags": ["#지적탐구", "#박물관투어", "#독특한문화", "#자유로운생각"],
        "tip": "관심 있는 주제의 전시회를 찾아 홀로 몰입해보는 것을 추천해요."
    },
    "ESTP": {
        "destination": "🇺🇸 미국 라스베이거스",
        "concept": "화려함 그 자체! 잠들지 않는 에너제틱 여행 🎰",
        "description": "반짝이는 조명, 화려한 쇼, 즉흥적인 즐거움이 넘치는 에너지 충전소예요!",
        "tags": ["#에너지뿜뿜", "#화려한야경", "#즉흥여행", "#즐거움가득"],
        "tip": "현지에서 만난 새로운 친구들과 즉석에서 즐거운 추억을 만들어보세요."
    },
    "ESFP": {
        "destination": "🇪🇸 스페인 바르셀로나",
        "concept": "흥겨운 음악과 축제가 가득한 열정 여행 💃",
        "description": "맛있는 타파스, 신나는 음악, 언제나 웃음이 가득한 거리에서 축제 같은 하루를 보내요.",
        "tags": ["#열정파티", "#맛있는음식", "#해변의자유", "#항상즐거워"],
        "tip": "거리의 음악 소리에 맞춰 신나게 몸을 흔들어보세요!"
    },
    "ENFP": {
        "destination": "🇻🇳 베트남 다낭",
        "concept": "알록달록 통통 튀는 즐거운 감성 여행 🎈",
        "description": "맛있는 길거리 음식, 알록달록한 등불, 바다에서의 해양 스포츠까지 즐길 거리가 차고 넘쳐요!",
        "tags": ["#통통튀는매력", "#야시장탐방", "#즐거움천국", "#인생샷명소"],
        "tip": "오늘 만난 현지인과 친구가 되어 숨은 맛집을 물어보세요!"
    },
    "ENTP": {
        "destination": "🇹🇼 대만 타이베이",
        "concept": "다채로운 맛과 통통 튀는 호기심 여행 🥟",
        "description": "밤마다 열리는 야시장 탐방부터 독특한 골목길까지! 끊임없이 새로운 재미를 발견할 수 있어요.",
        "tags": ["#야시장뿌시기", "#새로운경험", "#호기심자극", "#식도락탐험"],
        "tip": "처음 보는 신기한 음식에 주저하지 말고 도전해보세요!"
    },
    "ESTJ": {
        "destination": "🇸🇬 싱가포르",
        "concept": "스마트하고 완벽하게 정돈된 도심 여행 🏙️",
        "description": "쾌적하고 안전한 도시, 효율적인 교통, 완벽한 야경 쇼까지 깔끔한 일정 계획에 딱 맞춰져요.",
        "tags": ["#완벽한동선", "#쾌적함그자체", "#멋진도심야경", "#효율성갑"],
        "tip": "분 단위로 알차게 짜여진 시티 투어 코스를 완주해보세요."
    },
    "ESFJ": {
        "destination": "🇬🇷 그리스 산토리니",
        "concept": "사랑하는 사람과 함께하는 낭만 따뜻 여행 💙",
        "description": "하얀 건물의 파란 지붕, 따스한 햇살 아래 모두가 행복해지는 최고의 추억을 쌓을 수 있어요.",
        "tags": ["#함께하는행복", "#인생샷천국", "#따뜻한온기", "#로맨틱성지"],
        "tip": "소중한 사람들에게 보낼 예쁜 엽서를 사서 마음을 전해보세요."
    },
    "ENFJ": {
        "destination": "🇮🇹 이탈리아 피렌체",
        "concept": "마음을 사로잡는 따뜻한 예술&문화 여행 🎨",
        "description": "주황빛 지붕 너머로 지는 노을을 바라보며 따뜻한 감동과 영감을 가득 채워오는 곳이에요.",
        "tags": ["#감동적인풍경", "#예술의향기", "#모두함께즐겁게", "#따뜻한리더"],
        "tip": "두오모 성당 쿠폴라에 올라 도시 전체의 감동을 나눠보세요."
    },
    "ENTJ": {
        "destination": "🇺🇸 미국 뉴욕",
        "concept": "당당하고 에너제틱한 트렌디 시티 여행 🗽",
        "description": "세계의 중심! 거대한 빌딩 숲과 넘치는 열정 속에서 영감을 얻고 정상을 느껴보세요.",
        "tags": ["#열정가득", "#트렌드중심", "#성취감뿜뿜", "#웅장한시티"],
        "tip": "브로드웨이 뮤지컬 로열석에서 최고의 공연을 감상해보세요!"
    }
}

# 4. 헤더 영역 출력
st.markdown("""
    <div class="header-card">
        <div style="font-size: 3rem; margin-bottom: 10px;">✨🎀✨</div>
        <div class="header-title">말랑퐁당 MBTI 여행지 추천</div>
        <div style="font-size: 1.1rem; opacity: 0.9;">나의 성격 유형에 딱 맞는 러블리 여행지는 어디일까? ✈️💖</div>
    </div>
""", unsafe_allow_html=True)

# 5. MBTI 선택 영역 (아기자기한 선택창)
st.write("### 💖 당신의 MBTI를 선택해주세요!")
selected_mbti = st.selectbox(
    "아래 목록에서 쏙 골라보세요 🌸",
    list(mbti_travel_data.keys()),
    index=6 # 기본값: INFP (가장 인기있는 파스텔 감성)
)

# 6. 추천 버튼 클릭 시 결과 출력
if st.button("✨ 나에게 꼭 맞는 여행지 찾기 ✨"):
    # 가벼운 풍선 애니메이션 효과
    st.balloons()
    
    info = mbti_travel_data[selected_mbti]
    
    # 결과 카드 출력
    st.markdown(f"""
        <div class="result-card">
            <h3 style="color: #FF69B4; margin-top:0;">🎀 {selected_mbti}를 위한 추천 여행지 🎀</h3>
            <h1 style="color: #333; font-size: 2.2rem; margin-bottom: 10px;">{info['destination']}</h1>
            <p style="font-size: 1.2rem; font-weight: bold; color: #FF1493;">"{info['concept']}"</p>
            <hr style="border: 0.5px solid #FFE4E1; margin: 15px 0;">
            <p style="font-size: 1.05rem; line-height: 1.6; color: #555;">{info['description']}</p>
            <div style="margin-top: 15px;">
                {" ".join([f'<span class="tag">{tag}</span>' for tag in info['tags']])}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # 추가 꿀팁 아코디언
    with st.expander("🍯 **사랑스러운 여행 꿀팁 보기**"):
        st.write(info['tip'])

# 7. 하단 푸터 영역
st.markdown("""
    <br><br>
    <div style="text-align: center; color: #BBB; font-size: 0.85rem;">
        Made with 💕 for your lovely trip!
    </div>
""", unsafe_allow_html=True)
