import streamlit as st
import streamlit.components.v1 as components

# Streamlit Page Configuration for Mobile-optimized Layout
st.set_page_config(
    page_title="창춘 10분 중국어 회화",
    page_icon="🇨🇳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        /* Remove default Streamlit top/bottom paddings for app-like feeling */
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
            max-width: 540px !important;
        }
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        iframe {
            border-radius: 16px;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        }
    </style>
    """,
    unsafe_allow_html=True
)

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>창춘 10분 중국어 회화</title>
  
  <!-- Pretendard Font -->
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    body {
      font-family: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
      letter-spacing: -0.015em;
      -webkit-font-smoothing: antialiased;
      -webkit-tap-highlight-color: transparent;
      user-select: text;
    }
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
    @keyframes subtle-fade {
      0% { opacity: 0; transform: translateY(-8px); }
      100% { opacity: 1; transform: translateY(0); }
    }
    .animate-toast {
      animation: subtle-fade 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .pb-safe {
      padding-bottom: env(safe-area-inset-bottom, 20px);
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-sky-500 selection:text-white flex flex-col items-center">

  <!-- Mobile Wrapper Container -->
  <div class="w-full max-w-lg min-h-screen flex flex-col bg-slate-950 border-x border-slate-900 pb-safe relative">

    <!-- Floating Toast Notification -->
    <div id="toast" class="hidden fixed top-5 left-1/2 -translate-x-1/2 z-50 bg-slate-800/95 border border-slate-700/80 backdrop-blur-md text-emerald-300 text-xs px-4 py-2.5 rounded-full shadow-2xl flex items-center gap-2 animate-toast pointer-events-none">
      <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
      </svg>
      <span id="toast-text" class="font-semibold tracking-tight"></span>
    </div>

    <!-- Navigation Header -->
    <header class="sticky top-0 z-30 bg-slate-900/95 backdrop-blur-md border-b border-slate-800/80 px-4 py-3 flex items-center justify-between shadow-sm">
      <div class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-sm shadow-md shadow-sky-500/10">
          🇨🇳
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="text-[10px] font-bold text-sky-400 tracking-wide uppercase">10-Min Biz Coach</span>
            <span class="w-1 h-1 rounded-full bg-slate-600"></span>
            <span class="text-[10px] text-slate-400 font-medium">창춘 출장 실전</span>
          </div>
          <h1 class="text-sm font-bold text-slate-100 leading-tight">창춘 10분 중국어 회화</h1>
        </div>
      </div>
      
      <button id="btn-open-toast-modal" class="px-3 py-1.5 bg-slate-800 active:bg-slate-700 border border-slate-700 text-amber-300 font-semibold text-xs rounded-xl flex items-center gap-1.5 transition-all">
        <span>🥂</span>
        <span>MZ 건배사</span>
      </button>
    </header>

    <!-- Horizontal Category Filter Tabs -->
    <div id="scenario-tabs" class="px-3 py-2.5 bg-slate-900/60 border-b border-slate-800/60 overflow-x-auto no-scrollbar flex items-center gap-1.5 shrink-0">
      <!-- Tabs rendered by JS -->
    </div>

    <!-- Master Controller Dashboard Card -->
    <div class="p-4 shrink-0">
      <div class="bg-slate-900 border border-slate-800/90 rounded-2xl p-4 shadow-lg shadow-black/40">
        
        <!-- Status & Countdown -->
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center gap-2">
            <span id="status-dot" class="w-2 h-2 rounded-full bg-slate-500"></span>
            <span id="status-text" class="text-xs font-semibold text-slate-300">준비 완료 (재생 버튼을 누르세요)</span>
          </div>
          <div id="timer-display" class="font-mono text-xl font-bold tracking-tight text-sky-400">
            10:00
          </div>
        </div>

        <!-- Progress Bar -->
        <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden mb-3">
          <div id="progress-bar" class="bg-sky-500 h-full transition-all duration-500 ease-linear rounded-full" style="width: 0%;"></div>
        </div>

        <!-- Meta Context Card -->
        <div class="bg-slate-950/70 p-3 rounded-xl border border-slate-800/80 mb-3 flex items-center justify-between">
          <div class="pr-2">
            <div id="scenario-place" class="text-[11px] text-slate-400 font-medium">위치 정보</div>
            <div id="scenario-title" class="text-sm font-bold text-slate-100 mt-0.5 leading-snug">상황 타이틀</div>
          </div>
          <span id="phase-badge" class="shrink-0 text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-slate-800 text-sky-300 border border-slate-700">
            1단계: 통으로 듣기
          </span>
        </div>

        <!-- Action Control Buttons -->
        <div class="flex gap-2">
          <button id="btn-toggle-play" class="flex-1 py-3 px-4 rounded-xl font-bold text-sm flex items-center justify-center gap-2 transition-all active:scale-[0.99] bg-sky-500 active:bg-sky-600 text-white shadow-md shadow-sky-500/20">
            <svg id="play-icon" class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8 5v14l11-7z"/>
            </svg>
            <span id="btn-play-text">▶ 10분 자동 트레이닝 시작</span>
          </button>

          <button id="btn-reset" class="p-3 bg-slate-800 active:bg-slate-700 text-slate-300 rounded-xl transition-all border border-slate-700" title="처음부터 다시">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
          </button>
        </div>

        <!-- Sub Tools: Copy All & Speed Selection -->
        <div class="flex items-center justify-between text-xs text-slate-400 mt-3 pt-3 border-t border-slate-800/80">
          <button id="btn-copy-all" class="flex items-center gap-1.5 text-slate-300 active:text-sky-300 transition-colors py-1 px-2 rounded-lg bg-slate-800/70 border border-slate-700/60 font-medium">
            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
            <span>대화 4문장 전체 복사</span>
          </button>

          <div class="flex items-center gap-1.5">
            <span class="text-[11px] text-slate-400">속도:</span>
            <div class="flex bg-slate-800/80 p-0.5 rounded-lg border border-slate-700/70">
              <button data-speed="0.75" class="speed-btn px-2 py-0.5 rounded text-[11px] font-semibold text-slate-400">0.75x</button>
              <button data-speed="0.85" class="speed-btn px-2 py-0.5 rounded text-[11px] font-semibold bg-sky-500 text-white">0.85x</button>
              <button data-speed="1.0" class="speed-btn px-2 py-0.5 rounded text-[11px] font-semibold text-slate-400">1.0x</button>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Dialogue Container -->
    <div class="px-4 flex-1 flex flex-col">
      <div class="flex items-center justify-between text-xs text-slate-400 mb-2 px-1">
        <span class="font-semibold text-slate-300">실전 4문장 순차 대화</span>
        <span id="sentence-counter" class="text-[11px] text-sky-400 font-medium">1 / 4 문장</span>
      </div>

      <div id="dialogue-list" class="flex flex-col gap-2.5">
        <!-- Dialogue Cards rendered dynamically -->
      </div>

      <!-- Field Business Tips Card -->
      <div class="mt-4 p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 flex flex-col gap-1.5 mb-6">
        <div class="font-bold text-slate-100 flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.286L13 21l-2.286-6.857L5 12l5.714-2.286L13 3z" />
          </svg>
          현장 비즈니스 핵심 포인트
        </div>
        <p id="scenario-tip" class="leading-relaxed text-slate-400 select-text"></p>
      </div>
    </div>

    <!-- MZ Toast Modal -->
    <div id="toast-modal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
      <div class="bg-slate-900 border border-slate-700 w-full max-w-sm rounded-2xl p-5 shadow-2xl flex flex-col gap-4 animate-toast">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
          <div class="flex items-center gap-2">
            <span class="text-lg">🎉</span>
            <h3 class="text-sm font-bold text-slate-100">중국 MZ 인기 건배사</h3>
          </div>
          <button id="btn-close-toast-modal" class="w-7 h-7 rounded-lg bg-slate-800 text-slate-400 active:text-white flex items-center justify-center text-xs font-bold">
            ✕
          </button>
        </div>

        <div id="mz-list" class="flex flex-col gap-2.5 max-h-[380px] overflow-y-auto no-scrollbar">
          <!-- Populated by JS -->
        </div>

        <button id="btn-close-toast-modal-bottom" class="w-full py-2.5 bg-slate-800 active:bg-slate-700 text-slate-200 font-semibold rounded-xl text-xs transition-colors">
          닫기
        </button>
      </div>
    </div>

  </div>

  <script>
    const SCENARIOS = [
      {
        id: 1,
        title: "공항 도착 & 수하물 찾기",
        emoji: "✈️",
        place: "창춘 룽자공항 입국장",
        tips: "교과서 '请帮帮我' 대신 '请问一下(말씀 좀 여쭙겠습니다)', '麻烦您(번거롭게 해드리겠습니다)'를 쓰세요.",
        dialogue: [
          { speaker: "나", hanzi: "请问一下，从首尔飞过来的航班，在几号转盘取行李？", pinyin: "Qǐngwèn yíxià, cóng Shǒu'ěr fēiguòlái de hángbān, zài jǐhào zhuànpán qǔ xíngli?", meaning: "말씀 좀 여쭙겠습니다, 서울에서 온 항공편은 몇 번 벨트에서 짐을 찾나요?" },
          { speaker: "직원", hanzi: "您顺着左边往前走，五号转盘就是，现在已经开始出箱子了。", pinyin: "Nín shùnzhe zuǒbiān wǎng qián zǒu, wǔhào zhuànpán jiùshì, xiànzài yǐjīng kāishǐ chū xiāngzi le.", meaning: "왼쪽으로 쭉 직진하시면 5번 벨트입니다, 지금 막 캐리어가 나오기 시작했어요." },
          { speaker: "나", hanzi: "好的！如果行李箱有破损或者没出来，要去哪里登记？", pinyin: "Hǎo de! Rúguǒ xínglixiāng yǒu pòsǔn huòzhě méi chūlái, yào qù nǎlǐ dēngjì?", meaning: "네 감사합니다! 혹시 캐리어가 파손되었거나 안 나오면 어디서 접수하나요?" },
          { speaker: "직원", hanzi: "五号转盘旁边就有行李查询柜台，您拿登机牌过去办就可以。", pinyin: "Wǔhào zhuànpán pángbiān jiù yǒu xíngli cháxún guìtái, nín ná dēngjīpái guòqù bàn jiù kěyǐ.", meaning: "5번 벨트 바로 옆에 수하물 문의 창구가 있으니 탑승권 들고 가시면 됩니다." }
        ]
      },
      {
        id: 2,
        title: "화장실 위치 문의 & 주변 편의시설",
        emoji: "🚻",
        place: "공항 / 공장 복도",
        tips: "북방/동북 지역은 '在哪里(zài nǎlǐ)'보다 '在哪儿 (zài nǎr)'이 훨씬 입에 착 붙습니다.",
        dialogue: [
          { speaker: "나", hanzi: "不好意思，麻烦问一下，最近的洗手间在哪儿？", pinyin: "Bù hǎoyìsi, máfan wèn yíxià, zuìjìn de xǐshǒujiān zài nǎr?", meaning: "죄송하지만 실례합니다, 가장 가까운 화장실이 어디에 있나요?" },
          { speaker: "직원", hanzi: "顺着走廊一直往前走，到底往右拐就看到了。", pinyin: "Shùnzhe zǒuláng yìzhí wǎng qián zǒu, dàodǐ wǎng yòuguǎi jiù kàndào le.", meaning: "복도 따라 쭉 직진하시고 끝까지 가서 우회전하시면 바로 보입니다." },
          { speaker: "나", hanzi: "好的谢谢！请问洗手间旁边有自动售货机或者便利店吗？", pinyin: "Hǎo de xièxie! Qǐngwèn xǐshǒujiān pángbiān yǒu zìdòng shòuhuòjī huòzhě biànlìdiàn ma?", meaning: "감사합니다! 혹시 화장실 옆에 음료 자판기나 편의점도 있을까요?" },
          { speaker: "직원", hanzi: "有的，就在拐角处有一台机器，微信和支付宝都能扫。", pinyin: "Yǒu de, jiù zài guǎijiǎochù yǒu yì tái jīqì, Wēixìn hé Zhīfùbǎo dōu néng sǎo.", meaning: "네 있습니다, 코너에 기계 한 대 있고 위챗페이랑 알리페이 모두 결제됩니다." }
        ]
      },
      {
        id: 3,
        title: "픽업 파트너 조우 & 차내 이동 안부",
        emoji: "🚗",
        place: "창춘 공항 주차장 & 이동 차량 안",
        tips: "파트너에게 '辛苦您特意跑一趟(일부러 걸음해 주셔서 감사합니다)'를 건네면 즉시 친밀해집니다.",
        dialogue: [
          { speaker: "나", hanzi: "王经理，辛苦您特意跑一趟来接我！", pinyin: "Wáng jīnglǐ, xīnkǔ nín tèyì pǎo yí tàng lái jiē wǒ!", meaning: "왕 매니저님, 일부러 먼 길 걸음해 마중 나와주셔서 정말 감사합니다!" },
          { speaker: "파트너", hanzi: "哪里哪里！一路飞过来辛苦啦！行李放后备箱，咱们上车暖和暖和。", pinyin: "Nǎlǐ nǎlǐ! Yílù fēi guòlái xīnkǔ la! Xíngli fàng hòubèixiāng, zánmen shàngchē nuǎnhuo nuǎnhuo.", meaning: "별말씀을요! 비행기 타고 오시느라 고생하셨습니다! 짐은 트렁크에 넣고 차에서 몸 좀 녹이시죠." },
          { speaker: "나", hanzi: "路上挺顺利的，长春这天气比我想象的还要舒服，挺凉爽的！", pinyin: "Lùshang tǐng shùnlì de, Chángchūn zhè tiānqì bǐ wǒ xiǎngxiàng de hái yào shūfu, tǐng liángshuǎng de!", meaning: "비행은 아주 순조로웠습니다. 창춘 날씨가 생각했던 것보다 훨씬 상쾌하고 시원하네요!" },
          { speaker: "파트너", hanzi: "哈哈今天刚好赶上好天气！从机场到厂里大概四十分钟，累的话您先眯会儿。", pinyin: "Hāhā jīntiān gānghǎo gǎnshang hǎo tiānqì! Cóng jīchǎng dào chǎnglǐ dàgài sìshí fēnzhōng, lèi dehuà nín xiān mī huìr.", meaning: "하하 오늘 딱 좋은 날씨에 맞춰 오셨네요! 공항에서 공장까지 약 40분 걸리니 피곤하시면 눈 좀 붙이세요." }
        ]
      },
      {
        id: 4,
        title: "공장 도착 후 설비 검수 직전 현황 파악",
        emoji: "⚙️",
        place: "생산 공장 현장 (车间)",
        tips: "현장 엔지니어들과는 '咱们(너와 나 한 팀)'과 '开机(가동)', '验收(검수)' 표현이 핵심입니다.",
        dialogue: [
          { speaker: "나", hanzi: "李工，今天咱们要验的那台设备，目前准备情况怎么样？", pinyin: "Lǐ gōng, jīntiān zánmen yào yàn de nà tái shèbèi, mùqián zhǔnbèi qíngkuàng zěnmeyàng?", meaning: "리 엔지니어님, 오늘 저희가 검수할 그 장비의 현재 준비 상태는 어떤가요?" },
          { speaker: "엔지니어", hanzi: "设备昨天已经通电预热了，空载跑了一宿，量具和图纸都在现场备齐了。", pinyin: "Shèbèi zuótiān yǐjīng tōngdiàn yùrè le, kōngzǎi pǎo le yì xiǔ, liángjù hé túzhǐ dōu zài xiànchǎng bèiqí le.", meaning: "장비는 어제 이미 전원 넣어 예열했고 밤새 무부하로 돌렸습니다. 계측기와 도면도 현장에 다 준비되었습니다." },
          { speaker: "나", hanzi: "太好了！咱们先对一下关键尺寸，然后再看带载试运行怎么样？", pinyin: "Tài hǎo le! Zánmen xiān duì yíxià guānjiàn chǐcun, ránhòu zài kàn dàizǎi shìyùnxíng zěnmeyàng?", meaning: "좋습니다! 저희 먼저 핵심 치수부터 대조해 보고 나서 부하 시운전을 보는 건 어떨까요?" },
          { speaker: "엔지니어", hanzi: "没问题！全按您的检测标准来，发现任何细节问题咱们现场随时改。", pinyin: "Méi wèntí! Quán àn nín de jiǎncè biāozhǔn lái, fāxiàn rènhé xìjié wèntí zánmen xiànchǎng suíshí gǎi.", meaning: "문제없습니다! 대표님 검사 기준대로 전적으로 진행하시고, 세부 문제점은 현장에서 언제든 수정하시죠." }
        ]
      },
      {
        id: 5,
        title: "식사 만찬 & 센스 있는 건배 에티켓",
        emoji: "🥂",
        place: "창춘 현지 식당 만찬장",
        tips: "주량이 약할 땐 '以茶代酒(차로 대신)'를 말하며 '酒杯一碰，黄金乱蹦!'을 띄우면 분위기 최고입니다.",
        dialogue: [
          { speaker: "나", hanzi: "这锅包肉酸甜酥脆，外焦里嫩，真是名不虚传！", pinyin: "Zhè guōbāoròu suāntián sūcuì, wàijiāo lǐnèn, zhēn shì míng bù xū chuán!", meaning: "이 꿔바오로우 새콤달콤 바삭하고 겉바속촉이네요. 과연 명불허전입니다!" },
          { speaker: "호스트", hanzi: "喜欢就多吃点！尝尝东北特色！年轻人带个头，咱们碰一杯怎么样？", pinyin: "Xǐhuan jiù duō chī diǎn! Chángchang Dōngběi tèsè! Niánqīngrén dài ge tóu, zánmen pèng yì bēi zěnmeyàng?", meaning: "입에 맞으시면 많이 드세요! 동북 특색 맛보시고, 젊은 분이 한마디 띄워주시죠, 다 같이 한잔 칠까요?" },
          { speaker: "나", hanzi: "李总，我酒量真不行，今天以茶代酒敬您！酒杯一碰，黄金乱蹦！祝咱们合作愉快！", pinyin: "Lǐ zǒng, wǒ jiǔliàng zhēn bùxíng, jīntiān yǐ chá dài jiǔ jìng nín! Jiǔbēi yí pèng, huángjīn luàn bèng! Zhù zánmen hézuò yúkuài!", meaning: "대표님, 제가 주량이 약해서 오늘은 차로 술을 대신해 올립니다! 잔을 치니 황금이 와르르! 원활한 협력을 위해!" },
          { speaker: "호스트", hanzi: "哈哈！这词儿太敞亮了！借您吉言，不掉头发只搞钱，干杯！", pinyin: "Hāhā! Zhè cír tài chǎngliàng le! Jiè nín jíyán, bù diào tóufa zhǐ gǎo qián, gānbēi!", meaning: "하하! 멘트가 정말 시원시원하니 기분 최고네요! 덕담대로 탈모 없이 돈만 왕창 법시다, 건배!" }
        ]
      },
      {
        id: 6,
        title: "식당 실전 주문 & 취향 요청",
        emoji: "🍲",
        place: "동북 요리 식당",
        tips: "직원에게 메뉴를 물을 땐 '咱们家招牌菜', 고수 뺄 땐 '千万别放香菜'를 쓰세요.",
        dialogue: [
          { speaker: "나", hanzi: "服务员，请问咱们家有啥招牌菜？推荐两道呗。", pinyin: "Fúwùyuán, qǐngwèn zánmen jiā yǒu shà zhāopáicài? Tuījiàn liǎng dào bei.", meaning: "직원분, 이 집 대표 메뉴가 뭐예요? 두 개 정도 추천 좀 해주세요." },
          { speaker: "직원", hanzi: "咱们家锅包肉和大拉皮桌桌必点！两位能吃辣不？", pinyin: "Zánmen jiā guōbāoròu hé dàlāpí zhuōzhuō bìdiǎn! Liǎng wèi néng chī là bu?", meaning: "저희 집 꿔바오로우랑 넓적당면무침은 테이블마다 필수입니다! 두 분 매운 건 드시나요?" },
          { speaker: "나", hanzi: "做微辣就可以，另外千万别放香菜，再来两瓶常温矿泉水。", pinyin: "Zuò wēilà jiù kěyǐ, lìngwài qiānwàn bié fàng xiāngcài, zài lái liǎng píng chángwēn kuàngquánshuǐ.", meaning: "살짝만 맵게 해주시고, 고수는 절대 넣지 마세요. 그리고 상온 생수 두 병 부탁합니다." },
          { speaker: "직원", hanzi: "好的记下了，微辣不放香菜常温水，马上给您安排下单！", pinyin: "Hǎo de jìxià le, wēilà bú fàng xiāngcài chángwēn shuǐ, mǎshàng gěi nín ānpái xiàdān!", meaning: "네 적었습니다. 살짝 맵게, 고수 빼고, 상온 미온수, 지금 바로 주문 넣겠습니다!" }
        ]
      },
      {
        id: 7,
        title: "식사 마무리 & 귀가 배웅 스몰토크",
        emoji: "☕",
        place: "식당 입구 & 택시 승차장",
        tips: "계산해 준 파트너에겐 '今天太破费了(너무 무리하셨습니다)', 배웅 만류엔 '您快留步(들어가세요)'가 기본입니다.",
        dialogue: [
          { speaker: "나", hanzi: "今天李总太破费了！吃得特别好，真的非常感谢！", pinyin: "Jīntiān Lǐ zǒng tài pòfèi le! Chī de tèbié hǎo, zhēn de fēicháng gǎnxiè!", meaning: "오늘 이 대표님께서 너무 무리하셨습니다! 정말 맛있게 잘 먹었습니다, 감사합니다!" },
          { speaker: "호스트", hanzi: "哪里哪里，粗茶淡饭招待不周！车已经在门口等了，我送你们回酒店吧。", pinyin: "Nǎlǐ nǎlǐ, cūchádànfàn zhāodài bùzhōu! Chē yǐjīng zài ménkǒu děng le, wǒ sòng nǐmen huí jiǔdiàn ba.", meaning: "별말씀을요, 소박한 음식이라 대접이 변변찮았습니다! 차가 문 앞에 대기 중이니 호텔까지 모셔다드릴게요." },
          { speaker: "나", hanzi: "李总您快留步，千万不用送了！路上慢点儿，咱们明天厂里见。", pinyin: "Lǐ zǒng nín kuài liúbù, qiānwàn bú yòng sòng le! Lùshang màndiǎnr, zánmen míngtiān chǎnglǐ jiàn.", meaning: "대표님 어서 들어가세요, 절대 배웅 안 나오셔도 됩니다! 조심히 가시고 내일 공장에서 뵙겠습니다." },
          { speaker: "호스트", hanzi: "好嘞！那你们到了酒店发个微信报平安，明天上午九点咱们厂里见！", pinyin: "Hǎolei! Nà nǐmen dào le jiǔdiàn fā ge Wēixìn bào píng'ān, míngtiān shàngwǔ jiǔdiǎn zánmen chǎnglǐ jiàn!", meaning: "좋습니다! 그럼 호텔 도착하시면 안전하다고 위챗 하나 남겨주시고, 내일 오전 9시에 공장에서 뵙죠!" }
        ]
      },
      {
        id: 8,
        title: "편의점 결제 & 도시락 데우기",
        emoji: "🏪",
        place: "편의점 (便利店)",
        tips: "중국 편의점은 봉투(塑料袋) 유상 판매이며, 결제 시 '我扫你(내가 찍기)'나 '你扫我(보여주기)', 데우기는 '加热'를 씁니다.",
        dialogue: [
          { speaker: "직원", hanzi: "你好，欢迎光临！需要塑料袋吗？", pinyin: "Nǐ hǎo, huānyíng guānglín! Xūyào sùliàodài ma?", meaning: "안녕하세요, 어서오세요! 비닐봉투 필요하신가요?" },
          { speaker: "나", hanzi: "要一个中号的，另外这个便当麻烦帮我加热一下。", pinyin: "Yào yí ge zhōnghào de, lìngwài zhège biàndang máfan bāng wǒ jiārè yíxià.", meaning: "중간 크기 하나 주시고, 이 도시락 전자레인지에 좀 데워주세요." },
          { speaker: "직원", hanzi: "好的稍等！加热大概一分钟。请出示付款码，我扫您。", pinyin: "Hǎo de shāoděng! Jiārè dàgài yì fēnzhōng. Qǐng chūshì fùkuǎnmǎ, wǒ sǎo nín.", meaning: "네 잠시만요! 데우는 데 1분 정도 걸립니다. 결제 바코드 보여주시면 제가 찍겠습니다." },
          { speaker: "나", hanzi: "好的，给您扫。顺便麻烦打一张小票，谢谢！", pinyin: "Hǎo de, gěi nín sǎo. Shùnbiàn máfan dǎ yì zhāng xiǎopiào, xièxie!", meaning: "네, 찍어주세요. 참, 영수증도 한 장 출력 부탁드립니다, 감사합니다!" }
        ]
      },
      {
        id: 9,
        title: "호텔 체크인 & 조식·와이파이",
        emoji: "🏨",
        place: "호텔 로비 프런트 (前台)",
        tips: "호텔 체크인 시 '办理入住', 보증금 '押金(체크아웃 시 자동 환불)', 룸키 '房卡', 조식 '早餐'만 알면 완벽합니다.",
        dialogue: [
          { speaker: "나", hanzi: "你好，我预订了大床房，麻烦办理一下入住。", pinyin: "Nǐ hǎo, wǒ yùdìng le dàchuángfáng, máfan bànlǐ yíxià rùzhù.", meaning: "안녕하세요, 킹베드룸 예약했는데요, 체크인 좀 부탁드립니다." },
          { speaker: "직원", hanzi: "请出示一下护照，押金需要交两百，退房时原路退回。", pinyin: "Qǐng chūshì yíxià hùzhào, yājīn xūyào jiāo liǎngbǎi, tuìfáng shí tuìhuí.", meaning: "여권 보여주세요. 보증금은 200위안이며 체크아웃 시 원래 결제 수단으로 환불됩니다." },
          { speaker: "나", hanzi: "好的，微信扫给您。请问早餐在几楼？几点开始？", pinyin: "Hǎo de, Wēixìn sǎo gěi nín. Qǐngwèn zǎocān zài jǐ lóu? Jǐdiǎn kāishǐ?", meaning: "네, 위챗으로 결제할게요. 조식은 몇 층이고 몇 시부터 시작하나요?" },
          { speaker: "직원", hanzi: "早餐在二楼，早上七点到九点半，凭房卡直接用餐就可以。", pinyin: "Zǎocān zài èrlóu, zǎoshang qīdiǎn dào jiǔdiǎn bàn, píng fángkǎ zhíjiē yòngcān jiù kěyǐ.", meaning: "조식은 2층이고 오전 7시부터 9시 반까지이며 룸카드로 바로 식사하시면 됩니다." }
        ]
      },
      {
        id: 10,
        title: "택시 탑승 & 목적지 하차 요청",
        emoji: "🚕",
        place: "길거리 / 택시·디디 승차",
        tips: "디디나 택시 탈 땐 전화번호 뒷자리 '手机尾号'를 확인하며, 내릴 때 갓길 정차는 '靠边停', 트렁크는 '后备箱'입니다.",
        dialogue: [
          { speaker: "기사", hanzi: "师傅接单了，手机尾号是四三二一吗？去净月潭对吧？", pinyin: "Shīfu jiēdān le, shǒujī wěihào shì sì sān èr yī ma? Qù Jìngyuètán duì ba?", meaning: "기사입니다. 폰 번호 뒷자리가 4321 맞으신가요? 정월담 가시는 것 맞죠?" },
          { speaker: "나", hanzi: "对的师傅！咱们走高架桥吗？路上大概多久能到？", pinyin: "Duì de shīfu! Zánmen zǒu gāojiàqiáo ma? Lùshang dàgài duōjiǔ néng dào?", meaning: "네 맞습니다 기사님! 고가도로로 가나요? 도착까지 대략 얼마나 걸릴까요?" },
          { speaker: "기사", hanzi: "走高架快，不堵车二十来分钟就到，车里热的话我开空调。", pinyin: "Zǒu gāojià kuài, bù dǔchē èrshí lái fēnzhōng jiù dào, chēlǐ rè dehuà wǒ kāi kōngtiáo.", meaning: "고가가 빠릅니다. 차 안 막히면 20여 분이면 도착해요. 차 안이 더우시면 에어컨 틀어드릴게요." },
          { speaker: "나", hanzi: "好的谢谢！到了麻烦在门口靠边停一下，我拿一下后备箱行李。", pinyin: "Hǎo de xièxie! Dào le máfan zài ménkǒu kàobiān tíng yíxià, wǒ ná yíxià hòubèixiāng xíngli.", meaning: "감사합니다! 도착하면 입구 갓길에 세워주세요, 트렁크에서 짐 좀 꺼내겠습니다." }
        ]
      }
    ];

    const MZ_TOASTS = [
      { hanzi: "酒杯一碰，黄金乱蹦！", pinyin: "Jiǔbēi yí pèng, huángjīn luàn bèng!", meaning: "술잔을 딱 부딪치니 황금이 와르르 튄다!", tag: "MZ 대세 라임" },
      { hanzi: "酒杯一响，黄金万两！干杯！", pinyin: "Jiǔbēi yì xiǎng, huángjīn wàn liǎng! Gānbēi!", meaning: "잔 소리 한 번에 황금 만 냥! 건배!", tag: "비즈니스 대박" },
      { hanzi: "祝咱们：不掉头发，只搞钱！", pinyin: "Zhù zánmen: bù diào tóufa, zhǐ gǎo qián!", meaning: "우리 모두 탈모 없이 돈만 왕창 법시다!", tag: "직장인 밈" },
      { hanzi: "祝我们：顺风顺水，一路生花！", pinyin: "Zhù wǒmen: shùnfēng shùnshuǐ, yílù shēnghuā!", meaning: "순풍에 돛 단 듯, 꽃길만 펼쳐지길!", tag: "우아한 덕담" }
    ];

    // State Variables
    let currentScenarioIdx = 0;
    let isPlaying = false;
    let remainingSeconds = 600;
    let trainingPhase = 0;
    let activeSentenceIdx = 0;
    let audioSpeed = 0.85;
    let timerInterval = null;
    let autoRoutineActive = false;

    // DOM Elements
    const toast = document.getElementById('toast');
    const toastText = document.getElementById('toast-text');
    const scenarioTabs = document.getElementById('scenario-tabs');
    const statusDot = document.getElementById('status-dot');
    const statusText = document.getElementById('status-text');
    const timerDisplay = document.getElementById('timer-display');
    const progressBar = document.getElementById('progress-bar');
    const scenarioPlace = document.getElementById('scenario-place');
    const scenarioTitle = document.getElementById('scenario-title');
    const phaseBadge = document.getElementById('phase-badge');
    const btnTogglePlay = document.getElementById('btn-toggle-play');
    const btnPlayText = document.getElementById('btn-play-text');
    const playIcon = document.getElementById('play-icon');
    const btnReset = document.getElementById('btn-reset');
    const btnCopyAll = document.getElementById('btn-copy-all');
    const sentenceCounter = document.getElementById('sentence-counter');
    const dialogueList = document.getElementById('dialogue-list');
    const scenarioTip = document.getElementById('scenario-tip');
    const toastModal = document.getElementById('toast-modal');
    const btnOpenToastModal = document.getElementById('btn-open-toast-modal');
    const btnCloseToastModal = document.getElementById('btn-close-toast-modal');
    const btnCloseToastModalBottom = document.getElementById('btn-close-toast-modal-bottom');
    const mzList = document.getElementById('mz-list');
    const speedButtons = document.querySelectorAll('.speed-btn');

    // Toast Utility
    let toastTimeout = null;
    function showToast(msg) {
      toastText.innerText = msg;
      toast.classList.remove('hidden');
      clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {
        toast.classList.add('hidden');
      }, 2000);
    }

    // Reliable Clipboard Copy for Mobile Safari & Iframe
    function copyText(text, successMsg = "문장이 복사되었습니다") {
      try {
        const el = document.createElement('textarea');
        el.value = text;
        el.setAttribute('readonly', '');
        el.style.position = 'absolute';
        el.style.left = '-9999px';
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        showToast(successMsg);
      } catch (err) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(() => showToast(successMsg));
        }
      }
    }

    // TTS Web Speech Synthesizer with iOS support
    function playTTS(text, speed = audioSpeed) {
      return new Promise((resolve) => {
        if ('speechSynthesis' in window) {
          window.speechSynthesis.cancel();
          const utterance = new SpeechSynthesisUtterance(text);
          utterance.lang = 'zh-CN';
          utterance.rate = speed;
          utterance.onend = () => resolve();
          utterance.onerror = () => resolve();
          window.speechSynthesis.speak(utterance);
        } else {
          setTimeout(resolve, 1500);
        }
      });
    }

    // Sleep helper
    function delay(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    }

    // Format Seconds MM:SS
    function formatTime(s) {
      const m = Math.floor(s / 60).toString().padStart(2, '0');
      const sec = (s % 60).toString().padStart(2, '0');
      return `${m}:${sec}`;
    }

    // Render Scenario Tabs
    function renderTabs() {
      scenarioTabs.innerHTML = '';
      SCENARIOS.forEach((sc, idx) => {
        const btn = document.createElement('button');
        const isActive = idx === currentScenarioIdx;
        btn.className = `shrink-0 px-3 py-1.5 rounded-xl text-xs font-semibold transition-all flex items-center gap-1.5 border ${
          isActive 
            ? 'bg-sky-500 text-white border-sky-400 font-bold shadow-sm shadow-sky-500/25' 
            : 'bg-slate-800/60 text-slate-400 border-slate-800 active:bg-slate-800 active:text-slate-200'
        }`;
        btn.innerHTML = `<span>${sc.emoji}</span><span>${sc.id}. ${sc.title.split('&')[0].trim()}</span>`;
        btn.onclick = () => {
          selectScenario(idx);
        };
        scenarioTabs.appendChild(btn);
      });
    }

    function selectScenario(idx) {
      currentScenarioIdx = idx;
      trainingPhase = 0;
      activeSentenceIdx = 0;
      renderTabs();
      renderScenarioDetails();
    }

    // Render Active Dialogue Cards
    function renderScenarioDetails() {
      const sc = SCENARIOS[currentScenarioIdx];
      scenarioPlace.innerText = sc.place;
      scenarioTitle.innerText = sc.title;
      scenarioTip.innerText = sc.tips;
      sentenceCounter.innerText = `${activeSentenceIdx + 1} / 4 문장`;

      const phaseNames = [
        "1단계: 통으로 듣기",
        "2단계: 섀도잉 발화",
        "3단계: 실전 롤플레잉",
        "4단계: 완주 성공"
      ];
      phaseBadge.innerText = phaseNames[trainingPhase] || phaseNames[0];

      dialogueList.innerHTML = '';
      sc.dialogue.forEach((item, idx) => {
        const isCurrent = activeSentenceIdx === idx && isPlaying;
        const isUser = item.speaker === "나";

        const card = document.createElement('div');
        card.id = `dialogue-item-${idx}`;
        card.className = `p-3.5 rounded-xl border transition-all cursor-pointer relative overflow-hidden ${
          isCurrent 
            ? (isUser ? 'bg-sky-950/60 border-sky-500 shadow-md shadow-sky-500/10' : 'bg-emerald-950/60 border-emerald-500 shadow-md shadow-emerald-500/10')
            : 'bg-slate-900/80 border-slate-800 active:border-slate-700'
        }`;

        card.innerHTML = `
          ${isCurrent ? `<div class="absolute left-0 top-0 bottom-0 w-1 ${isUser ? 'bg-sky-400' : 'bg-emerald-400'}"></div>` : ''}
          <div class="flex items-center justify-between mb-1.5 pl-0.5">
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded ${isUser ? 'bg-sky-500 text-white' : 'bg-emerald-600 text-white'}">
                ${item.speaker}
              </span>
              ${isCurrent ? `
                <span class="text-[11px] font-semibold text-amber-400 flex items-center gap-1 animate-pulse">
                  <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                  </svg>
                  재생 중
                </span>
              ` : ''}
            </div>

            <div class="flex items-center gap-1">
              <button class="btn-copy-item p-1.5 text-slate-400 active:text-sky-300 rounded active:bg-slate-800 transition-colors" title="복사">
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
              </button>
              <button class="btn-play-item p-1.5 text-slate-400 active:text-white rounded active:bg-slate-800 transition-colors" title="소리 듣기">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                </svg>
              </button>
            </div>
          </div>

          <div class="pl-0.5 select-text">
            <div class="text-[11px] text-sky-400 font-mono tracking-tight leading-relaxed">${item.pinyin}</div>
            <div class="text-base font-semibold text-slate-100 mt-0.5 leading-snug tracking-wide">${item.hanzi}</div>
            <div class="text-xs text-slate-400 mt-1 leading-relaxed">${item.meaning}</div>
          </div>
        `;

        // Card Click Handler
        card.onclick = (e) => {
          if (e.target.closest('.btn-copy-item') || e.target.closest('.btn-play-item')) return;
          activeSentenceIdx = idx;
          renderScenarioDetails();
          playTTS(item.hanzi);
        };

        // Copy Item
        card.querySelector('.btn-copy-item').onclick = (e) => {
          e.stopPropagation();
          copyText(`${item.hanzi}\\n${item.pinyin}\\n(${item.meaning})`, `"${item.hanzi}" 문장이 복사되었습니다`);
        };

        // Play Item TTS
        card.querySelector('.btn-play-item').onclick = (e) => {
          e.stopPropagation();
          activeSentenceIdx = idx;
          renderScenarioDetails();
          playTTS(item.hanzi);
        };

        dialogueList.appendChild(card);
      });
    }

    // Auto Coaching Routine Execution Loop
    async function runAutoCoach() {
      autoRoutineActive = true;

      while (isPlaying && remainingSeconds > 0) {
        const sentences = SCENARIOS[currentScenarioIdx].dialogue;

        // PHASE 0: Listen All Sentences
        if (trainingPhase === 0) {
          for (let i = 0; i < sentences.length; i++) {
            if (!isPlaying) return;
            activeSentenceIdx = i;
            renderScenarioDetails();
            await playTTS(sentences[i].hanzi, 0.9);
            await delay(1200);
          }
          if (!isPlaying) return;
          trainingPhase = 1;
          activeSentenceIdx = 0;
          renderScenarioDetails();
        }

        // PHASE 1: Shadowing Repeat
        else if (trainingPhase === 1) {
          for (let i = 0; i < sentences.length; i++) {
            if (!isPlaying) return;
            activeSentenceIdx = i;
            renderScenarioDetails();

            // 1. Slow Demonstration
            await playTTS(sentences[i].hanzi, 0.75);
            if (!isPlaying) return;

            // 2. Countdown pause for user speaking
            statusText.innerText = "🎙️ 소리 내어 따라 말하세요!";
            await delay(3000);
            if (!isPlaying) return;

            // 3. Re-play normal
            statusText.innerText = "자동 코칭 트레이닝 진행 중";
            await playTTS(sentences[i].hanzi, 0.9);
            await delay(1200);
          }
          if (!isPlaying) return;
          trainingPhase = 2;
          activeSentenceIdx = 0;
          renderScenarioDetails();
        }

        // PHASE 2: Roleplay Simulation
        else if (trainingPhase === 2) {
          for (let i = 0; i < sentences.length; i++) {
            if (!isPlaying) return;
            activeSentenceIdx = i;
            renderScenarioDetails();

            if (sentences[i].speaker === "나") {
              statusText.innerText = "🎙️ 내 차례! 답변해보세요!";
              await delay(3200);
              if (!isPlaying) return;
              await playTTS(sentences[i].hanzi, 0.9);
            } else {
              statusText.innerText = "상대방의 답변을 잘 들어보세요";
              await playTTS(sentences[i].hanzi, 0.9);
            }
            await delay(1500);
          }
          if (!isPlaying) return;
          trainingPhase = 3;
          renderScenarioDetails();
        }

        // PHASE 3: Next Scenario Loop
        else if (trainingPhase === 3) {
          statusText.innerText = "🎉 1개 세션 완주! 다음 상황으로 이동합니다.";
          await delay(3000);
          if (!isPlaying) return;
          currentScenarioIdx = (currentScenarioIdx + 1) % SCENARIOS.length;
          trainingPhase = 0;
          activeSentenceIdx = 0;
          renderTabs();
          renderScenarioDetails();
        }
      }

      autoRoutineActive = false;
    }

    // Toggle Play / Pause
    function togglePlay() {
      isPlaying = !isPlaying;

      if (isPlaying) {
        btnTogglePlay.className = "flex-1 py-3 px-4 rounded-xl font-bold text-sm flex items-center justify-center gap-2 transition-all active:scale-[0.99] bg-amber-500 active:bg-amber-600 text-slate-950";
        btnPlayText.innerText = "일시 정지";
        playIcon.innerHTML = '<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>';
        statusDot.className = "w-2 h-2 rounded-full bg-emerald-400 animate-ping";
        statusText.innerText = "자동 코칭 트레이닝 진행 중";

        // Start Countdown Timer
        if (!timerInterval) {
          timerInterval = setInterval(() => {
            if (remainingSeconds > 0) {
              remainingSeconds--;
              timerDisplay.innerText = formatTime(remainingSeconds);
              const pct = Math.min(100, Math.round(((600 - remainingSeconds) / 600) * 100));
              progressBar.style.width = `${pct}%`;
            } else {
              resetTraining();
            }
          }, 1000);
        }

        runAutoCoach();

      } else {
        pauseTraining();
      }
    }

    function pauseTraining() {
      isPlaying = false;
      window.speechSynthesis && window.speechSynthesis.cancel();
      clearInterval(timerInterval);
      timerInterval = null;

      btnTogglePlay.className = "flex-1 py-3 px-4 rounded-xl font-bold text-sm flex items-center justify-center gap-2 transition-all active:scale-[0.99] bg-sky-500 active:bg-sky-600 text-white shadow-md shadow-sky-500/20";
      btnPlayText.innerText = "▶ 10분 자동 트레이닝 시작";
      playIcon.innerHTML = '<path d="M8 5v14l11-7z"/>';
      statusDot.className = "w-2 h-2 rounded-full bg-slate-500";
      statusText.innerText = "일시 정지됨 (다시 누르면 계속됩니다)";
      renderScenarioDetails();
    }

    function resetTraining() {
      pauseTraining();
      remainingSeconds = 600;
      trainingPhase = 0;
      activeSentenceIdx = 0;
      timerDisplay.innerText = "10:00";
      progressBar.style.width = "0%";
      statusText.innerText = "준비 완료 (재생 버튼을 누르세요)";
      renderScenarioDetails();
    }

    // Copy All Dialogue Action
    btnCopyAll.onclick = () => {
      const activeSc = SCENARIOS[currentScenarioIdx];
      const fullText = activeSc.dialogue.map(
        (d) => `[${d.speaker}]\\n${d.hanzi}\\n${d.pinyin}\\n${d.meaning}`
      ).join("\\n\\n");
      copyText(fullText, "전체 대화 4문장이 복사되었습니다");
    };

    // Speed Setting Buttons
    speedButtons.forEach((btn) => {
      btn.onclick = () => {
        speedButtons.forEach(b => {
          b.className = "speed-btn px-2 py-0.5 rounded text-[11px] font-semibold text-slate-400";
        });
        btn.className = "speed-btn px-2 py-0.5 rounded text-[11px] font-semibold bg-sky-500 text-white";
        audioSpeed = parseFloat(btn.dataset.speed);
      };
    });

    // Populate MZ Toasts in Modal
    function renderMzToasts() {
      mzList.innerHTML = '';
      MZ_TOASTS.forEach((toast) => {
        const card = document.createElement('div');
        card.className = "bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col gap-1";
        card.innerHTML = `
          <div class="flex items-center justify-between">
            <span class="text-[10px] font-bold text-amber-400 bg-amber-950/50 px-2 py-0.5 rounded border border-amber-800/40">
              ${toast.tag}
            </span>
            <div class="flex items-center gap-1">
              <button class="btn-copy-mz p-1 text-slate-400 active:text-sky-300 rounded" title="복사">
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
              </button>
              <button class="btn-play-mz p-1 text-slate-400 active:text-white rounded" title="발음 듣기">
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                </svg>
              </button>
            </div>
          </div>
          <div class="text-sm font-bold text-slate-100 mt-0.5 select-text">${toast.hanzi}</div>
          <div class="text-xs text-sky-400 font-mono select-text">${toast.pinyin}</div>
          <div class="text-xs text-slate-400 select-text">${toast.meaning}</div>
        `;

        card.querySelector('.btn-copy-mz').onclick = () => {
          copyText(`${toast.hanzi} (${toast.pinyin})\\n${toast.meaning}`, `"${toast.hanzi}" 건배사가 복사되었습니다`);
        };

        card.querySelector('.btn-play-mz').onclick = () => {
          playTTS(toast.hanzi);
        };

        mzList.appendChild(card);
      });
    }

    // Modal Events
    btnOpenToastModal.onclick = () => {
      toastModal.classList.remove('hidden');
    };
    btnCloseToastModal.onclick = () => {
      toastModal.classList.add('hidden');
    };
    btnCloseToastModalBottom.onclick = () => {
      toastModal.classList.add('hidden');
    };

    // Controller Buttons
    btnTogglePlay.onclick = togglePlay;
    btnReset.onclick = resetTraining;

    // Initialization on Page Load
    window.addEventListener('DOMContentLoaded', () => {
      renderTabs();
      renderScenarioDetails();
      renderMzToasts();
    });
  </script>
</body>
</html>
"""

components.html(HTML_CONTENT, height=920, scrolling=True)