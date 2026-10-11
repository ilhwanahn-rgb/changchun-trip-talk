import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="창춘 직진도 교정기 검수 & 실전 출장 중국어 (PRO Ver)",
    page_icon="⚙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
            max-width: 500px !important;
        }
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        iframe {
            border-radius: 24px;
            box-shadow: 0 16px 40px -10px rgba(0, 0, 0, 0.8);
            border: 1px solid #1e293b;
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
  <title>창춘 직진도 교정기 검수 & 실전 출장 중국어 (PRO Ver)</title>
  
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    body {
      font-family: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
      letter-spacing: -0.015em;
      -webkit-font-smoothing: antialiased;
      -webkit-tap-highlight-color: transparent;
      user-select: text;
    }
    .no-scrollbar::-webkit-scrollbar { display: none; }
    .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    .pb-safe { padding-bottom: env(safe-area-inset-bottom, 20px); }

    .blind-active .blind-target {
      filter: blur(8px);
      user-select: none;
      transition: filter 0.2s ease;
    }
    .blind-active .blind-target:active,
    .blind-active .blind-target:hover {
      filter: blur(0);
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col items-center">

  <div class="w-full max-w-md min-h-screen flex flex-col bg-slate-950 border-x border-slate-900 pb-safe relative">

    <div id="toast" class="hidden fixed top-4 left-1/2 -translate-x-1/2 z-50 bg-slate-800/95 border border-slate-700 text-sky-300 text-xs px-4 py-2 rounded-full shadow-2xl flex items-center gap-2 pointer-events-none transition-all">
      <span id="toast-text" class="font-semibold"></span>
    </div>

    <!-- 현장 전광판(Show-Me) 모달 -->
    <div id="showme-modal" class="hidden fixed inset-0 z-50 bg-black flex flex-col justify-between p-6 cursor-pointer" onclick="closeShowMe()">
      <div class="flex items-center justify-between text-slate-500 text-xs">
        <span>📱 공장/식당 현장 보여주기 모드 (화면 터치 시 닫힘)</span>
        <span class="text-slate-400 font-bold">✕ 닫기</span>
      </div>
      <div class="flex flex-col items-center justify-center my-auto text-center gap-6">
        <div id="showme-hanzi" class="text-4xl sm:text-5xl font-extrabold text-amber-300 leading-tight tracking-wide">
          上料机构动作顺畅吗？
        </div>
        <div id="showme-pinyin" class="text-lg font-mono text-emerald-400">
          Shàngliào jīgòu dòngzuò shùnchàng ma?
        </div>
        <div id="showme-ko" class="text-base text-slate-300 bg-slate-900 px-4 py-2 rounded-2xl border border-slate-800">
          "로딩 기구 동작이 원활한가요?"
        </div>
      </div>
      <div class="text-center text-xs text-amber-500/80 font-mono">
        💡 상대방 중국인 작업자에게 이 화면을 그대로 보여주세요
      </div>
    </div>

    <header class="sticky top-0 z-30 bg-slate-900/95 backdrop-blur-md border-b border-slate-800 px-4 py-3 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-lg bg-sky-500/20 border border-sky-500/40 flex items-center justify-center text-sm font-bold text-sky-400">
          ⚙️
        </div>
        <div>
          <h1 class="text-sm font-bold text-slate-100 leading-tight">창춘 교정기 검수 & 현장 중국어</h1>
          <p class="text-[10px] text-slate-400">2주 고밀도 완성 · 현장 치트키 탑재</p>
        </div>
      </div>
      
      <div class="flex items-center gap-1.5">
        <button id="btn-toggle-blind" class="px-2 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-400 border border-slate-700 hover:text-amber-300 transition-all flex items-center gap-1" title="한국어만 보고 먼저 말해보는 블라인드 모드">
          <span id="blind-icon">🙈</span> <span id="blind-text" class="text-[11px]">노룩</span>
        </button>

        <div class="flex bg-slate-800/80 p-0.5 rounded-lg border border-slate-700/60 text-xs">
          <button id="btn-mode-card" class="px-2 py-1 rounded font-bold bg-sky-500 text-white transition-all">카드</button>
          <button id="btn-mode-list" class="px-2 py-1 rounded text-slate-400 hover:text-slate-200 transition-all">목록</button>
        </div>
      </div>
    </header>

    <div id="category-tabs" class="px-3 py-2 bg-slate-900/60 border-b border-slate-800/60 overflow-x-auto no-scrollbar flex items-center gap-1.5 shrink-0"></div>

    <div class="p-3.5 shrink-0">
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-3.5 shadow-md">
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center gap-2">
            <span id="auto-status-dot" class="w-2 h-2 rounded-full bg-slate-600"></span>
            <span id="auto-status-text" class="text-xs font-semibold text-slate-300">정지됨</span>
          </div>
          <div class="text-[11px] font-mono text-sky-400">
            <span id="current-index-num">1</span> / <span id="total-count-num">44</span>
          </div>
        </div>

        <button id="btn-toggle-auto" class="w-full py-3 px-4 rounded-xl font-bold text-sm flex items-center justify-center gap-2 transition-all active:scale-[0.99] bg-sky-500 text-white shadow-lg shadow-sky-500/20">
          <svg id="play-icon" class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
          <span id="play-btn-text">▶ 유튜브 스타일 자동 섀도잉 시작</span>
        </button>

        <div class="flex items-center justify-between text-xs text-slate-400 mt-2.5 pt-2.5 border-t border-slate-800/80">
          <div class="flex items-center gap-1">
            <span class="text-[11px]">간격:</span>
            <select id="interval-select" class="bg-slate-800 border border-slate-700 text-slate-300 rounded px-1.5 py-0.5 text-[11px] outline-none">
              <option value="2500">2.5초 (빠르게)</option>
              <option value="3500" selected>3.5초 (권장)</option>
              <option value="4500">4.5초 (따라하기)</option>
            </select>
          </div>

          <div class="flex items-center gap-1">
            <span class="text-[11px]">배속:</span>
            <div class="flex bg-slate-800 p-0.5 rounded border border-slate-700 text-[11px]">
              <button data-speed="0.75" class="speed-btn px-1.5 py-0.5 rounded text-slate-400">0.75x</button>
              <button data-speed="0.85" class="speed-btn px-1.5 py-0.5 rounded bg-sky-500 text-white font-bold">0.85x</button>
              <button data-speed="1.0" class="speed-btn px-1.5 py-0.5 rounded text-slate-400">1.0x</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="card-view-container" class="px-4 flex-1 flex flex-col justify-start">
      <div id="flashcard" class="bg-slate-900 border border-slate-800 rounded-3xl p-5 shadow-xl flex flex-col gap-4 relative overflow-hidden transition-all">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-1.5">
            <span id="card-category-badge" class="text-[11px] font-bold text-sky-400 bg-sky-950/60 border border-sky-800/60 px-2.5 py-1 rounded-lg">
              교정기/검수
            </span>
            <button id="btn-star-card" class="p-1 rounded-lg text-slate-500 hover:text-amber-400 transition-all text-sm" title="즐겨찾기 추가/해제">
              ★
            </button>
          </div>

          <div class="flex items-center gap-1.5">
            <button id="btn-open-showme" class="px-2 py-1 bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 rounded-lg text-xs font-bold flex items-center gap-1" title="상대방에게 크게 보여주기">
              📱 전광판
            </button>
            <button id="btn-copy-card" class="p-1.5 text-slate-400 hover:text-sky-300 rounded-lg bg-slate-800 border border-slate-700/60" title="문장 복사">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
              </svg>
            </button>
          </div>
        </div>

        <div class="bg-slate-950/80 rounded-2xl p-4 border border-slate-800/80">
          <div class="flex items-center justify-between mb-1">
            <span class="text-[11px] font-bold text-amber-400 tracking-wider uppercase">Step 1. 핵심 단어</span>
            <button id="btn-play-word" class="p-1 text-slate-400 hover:text-white rounded" title="단어 듣기">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
              </svg>
            </button>
          </div>
          <div class="flex items-baseline gap-2.5 blind-target">
            <div id="card-word-hanzi" class="text-2xl font-bold text-slate-100">上料</div>
            <div id="card-word-pinyin" class="text-xs font-mono text-amber-300">shàngliào</div>
          </div>
          <div id="card-word-meaning" class="text-xs text-slate-400 mt-1">로딩 / 자재 투입</div>
        </div>

        <div class="bg-slate-950/80 rounded-2xl p-4 border border-slate-800/80">
          <div class="flex items-center justify-between mb-1">
            <span class="text-[11px] font-bold text-emerald-400 tracking-wider uppercase">Step 2. 실전 1문장</span>
            <button id="btn-play-sentence" class="p-1 text-slate-400 hover:text-white rounded" title="문장 듣기">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
              </svg>
            </button>
          </div>
          <div id="card-sentence-pinyin" class="text-xs font-mono text-emerald-300 leading-snug blind-target">Shàngliào jīgòu dòngzuò shùnchàng ma?</div>
          <div id="card-sentence-hanzi" class="text-xl font-bold text-slate-100 mt-1 leading-snug blind-target">上料机构动作顺畅吗？</div>
          <div id="card-sentence-meaning" class="text-sm font-semibold text-sky-300 mt-2 bg-sky-950/40 p-2 rounded-xl border border-sky-900/40">
            "로딩 기구 동작이 원활한가요?"
          </div>
        </div>

        <div class="flex gap-2 mt-1">
          <button id="btn-prev-card" class="flex-1 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700 transition-all flex items-center justify-center gap-1">
            ◀ 이전 단어
          </button>
          <button id="btn-replay-card" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold text-xs border border-slate-700 transition-all" title="다시 듣기">
            🔄
          </button>
          <button id="btn-next-card" class="flex-1 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-100 font-bold text-xs border border-slate-700 transition-all flex items-center justify-center gap-1">
            다음 단어 ▶
          </button>
        </div>
      </div>

      <div id="field-tip-box" class="mt-4 p-3.5 rounded-2xl bg-slate-900 border border-slate-800/80 text-xs text-slate-400 leading-relaxed">
        <span class="text-amber-400 font-bold">💡 현장 엔지니어 은어 팁:</span> 
        중국 가공 현장에서 <strong>0.01mm</strong>는 교과서식 발음 대신 <strong>"丝(sī)"</strong>라고 부릅니다. "오차가 0.02mm 났다"는 <strong>"差了两个丝(chà le liǎng ge sī)"</strong>라고 표현하세요!
      </div>
    </div>

    <div id="list-view-container" class="hidden px-4 flex-1 overflow-y-auto no-scrollbar pb-6 flex flex-col gap-2.5"></div>
  </div>

  <script>
    const VOCAB_DATA = [
      { id: 1, cat: "교정기/검수", word: "校直机", pinyin: "xiàozhíjī", wordKo: "직진도 교정기", senZh: "这台棒料校直机准备好了吗？", senPy: "Zhè tái bàngliào xiàozhíjī zhǔnbèi hǎo le ma?", senKo: "이 환봉 교정기는 준비 완료되었나요?" },
      { id: 2, cat: "교정기/검수", word: "棒料", pinyin: "bàngliào", wordKo: "봉재 / 환봉", senZh: "先拿几根测试棒料过来吧。", senPy: "Xiān ná jǐ gēn cèshì bàngliào guòlai ba.", senKo: "먼저 테스트용 봉 몇 개 가져와 보세요." },
      { id: 3, cat: "교정기/검수", word: "上料", pinyin: "shàngliào", wordKo: "로딩 / 자재 투입", senZh: "上料机构动作顺畅吗？", senPy: "Shàngliào jīgòu dòngzuò shùnchàng ma?", senKo: "로딩 기구 동작이 원활한가요?" },
      { id: 4, cat: "교정기/검수", word: "顺畅", pinyin: "shùnchàng", wordKo: "원활하다 / 순조롭다", senZh: "确认一下上料动作是否顺畅。", senPy: "Quèrèn yíxià shàngliào dòngzuò shìfǒu shùnchàng.", senKo: "로딩 동작이 원활한지 확인해 주십시오." },
      { id: 5, cat: "교정기/검수", word: "卡料", pinyin: "kǎliào", wordKo: "자재 걸림 / 잼", senZh: "连续上料时有没有卡料现象？", senPy: "Liánxù shàngliào shí yǒu méiyǒu kǎliào xiànxiàng?", senKo: "연속 로딩 시 자재 걸림 현상이 있나요?" },
      { id: 6, cat: "교정기/검수", word: "旋转", pinyin: "xuánzhuǎn", wordKo: "회전시키다", senZh: "把棒料旋转一周测一下。", senPy: "Bǎ bàngliào xuánzhuǎn yìzhōu cè yíxià.", senKo: "봉을 한 바퀴 회전시켜서 측정해 보시죠." },
      { id: 7, cat: "교정기/검수", word: "直线度", pinyin: "zhíxiàndù", wordKo: "직진도", senZh: "旋转时直线度跳动多少？", senPy: "Xuánzhuǎn shí zhíxiàndù tiàodòng duōshao?", senKo: "회전 시 직진도 런아웃(흔들림)이 얼마나 나오나요?" },
      { id: 8, cat: "교정기/검수", word: "跳动", pinyin: "tiàodòng", wordKo: "런아웃 / 흔들림 편차", senZh: "中间位置的跳动有点大。", senPy: "Zhōngjiān wèizhi de tiàodòng yǒudiǎnr dà.", senKo: "가운데 지점 흔들림이 좀 큽니다." },
      { id: 9, cat: "교정기/검수", word: "测头", pinyin: "cètóu", wordKo: "측정 프로브 / 센서", senZh: "激光测头的位置校准过了吗？", senPy: "Jīguāng cètóu de wèizhi jiàozhǔn guò le ma?", senKo: "레이저 측정 프로브 위치는 보정된 상태인가요?" },
      { id: 10, cat: "교정기/검수", word: "合格", pinyin: "hégé", wordKo: "합격 / 양품 판정", senZh: "系统判定合格的基准是多少？", senPy: "Xìtǒng pàndìng hégé de jīzhǔn shì duōshao?", senKo: "시스템에서 합격으로 판정하는 기준값이 얼마인가요?" },
      { id: 11, cat: "교정기/검수", word: "不良", pinyin: "bùliáng", wordKo: "불량 / NG", senZh: "如果判定为不良，会自动校直吗？", senPy: "Rúguǒ pàndìng wéi bùliáng, huì zìdòng xiàozhí ma?", senKo: "불량으로 판정되면 자동으로 교정 작업에 들어가나요?" },
      { id: 12, cat: "교정기/검수", word: "丝", pinyin: "sī", wordKo: "0.01mm (현장 절대은어)", senZh: "直线度跳动差了两个丝。", senPy: "Zhíxiàndù tiàodòng chà le liǎng ge sī.", senKo: "직진도 런아웃 편차가 0.02mm(2사) 납니다." },
      { id: 13, cat: "교정기/검수", word: "公差", pinyin: "gōngchā", wordKo: "공차 (Tolerance)", senZh: "这批棒料的直线度公差是多少？", senPy: "Zhè pī bàngliào de zhíxiàndù gōngchā shì duōshao?", senKo: "이 환봉 배치의 직진도 공차는 얼마인가요?" },
      { id: 14, cat: "교정기/검수", word: "压下量", pinyin: "yàxiàliàng", wordKo: "압하량 / 프레스 가압량", senZh: "校直时的压下量和压力能调吗？", senPy: "Xiàozhí shí de yàxiàliàng hé yālì néng tiáo ma?", senKo: "교정 시 프레스 가압량과 압력 조절이 가능한가요?" },
      { id: 15, cat: "교정기/검수", word: "下料", pinyin: "xiàliào", wordKo: "언로딩 / 자재 배출", senZh: "校直完成后下料是否顺畅？", senPy: "Xiàozhí wánchéng hòu xiàliào shìfǒu shùnchàng?", senKo: "교정 완료 후 언로딩 배출이 원활한가요?" },
      { id: 16, cat: "교정기/검수", word: "分选", pinyin: "fēnxuǎn", wordKo: "분리 배출 / 선별", senZh: "良品和不良品能自动分选吗？", senPy: "Liángpǐn hé bùliángpǐn néng zìdòng fēnxuǎn ma?", senKo: "양품과 불량품이 자동으로 분류 배출되나요?" },
      { id: 17, cat: "교정기/검수", word: "划伤", pinyin: "huáshāng", wordKo: "스크래치 / 긁힘", senZh: "上下料过程中棒料表面有划伤吗？", senPy: "Shàngxiàliào guòchéng zhōng bàngliào biǎomiàn yǒu huáshāng ma?", senKo: "로딩/언로딩 과정에서 봉 표면에 스크래치가 생기나요?" },
      { id: 18, cat: "교정기/검수", word: "超标", pinyin: "chāobiāo", wordKo: "기준치 초과", senZh: "校直后的残留跳动还是超标。", senPy: "Xiàozhí hòu de cánliú tiàodòng háishì chāobiāo.", senKo: "교정 후 남은 흔들림이 여전히 기준치를 초과합니다." },
      { id: 19, cat: "교정기/검수", word: "调机", pinyin: "tiáojī", wordKo: "설비 파라미터 세팅", senZh: "麻烦李工现场微调一下参数。", senPy: "Máfan Lǐ gōng xiànchǎng wēitiáo yíxià cānshù.", senKo: "엔지니어님, 현장에서 파라미터 미세 조정 좀 부탁드립니다." },

      { id: 20, cat: "식당/주문", word: "菜单", pinyin: "càidān", wordKo: "메뉴판", senZh: "服务员，麻烦拿一下菜单。", senPy: "Fúwùyuán, máfan ná yíxià càidān.", senKo: "직원분, 메뉴판 좀 가져다주세요." },
      { id: 21, cat: "식당/주문", word: "点菜", pinyin: "diǎncài", wordKo: "주문하다", senZh: "我们准备好点菜了。", senPy: "Wǒmen zhǔnbèi hǎo diǎncài le.", senKo: "저희 주문할 준비 됐습니다." },
      { id: 22, cat: "식당/주문", word: "稍等", pinyin: "shāoděng", wordKo: "잠시 기다리다", senZh: "稍等一下，我们还没选好。", senPy: "Shāoděng yíxià, wǒmen hái méi xuǎnhǎo.", senKo: "잠시만요, 아직 다 못 골랐어요." },
      { id: 23, cat: "식당/주문", word: "筷子", pinyin: "kuàizi", wordKo: "젓가락", senZh: "麻烦再拿一双筷子。", senPy: "Máfan zài ná yì shuāng kuàizi.", senKo: "젓가락 한 벌만 더 가져다주세요." },
      { id: 24, cat: "식당/주문", word: "米饭", pinyin: "mǐfàn", wordKo: "공깃밥", senZh: "先来两碗米饭吧。", senPy: "Xiān lái liǎng wǎn mǐfàn ba.", senKo: "먼저 공깃밥 두 공기 주세요." },
      { id: 25, cat: "식당/주문", word: "加水", pinyin: "jiāshuǐ", wordKo: "물 추가 / 물 채우기", senZh: "服务员，这边加一下水。", senPy: "Fúwùyuán, zhèbiān jiā yíxià shuǐ.", senKo: "직원분, 여기 물 좀 더 채워주세요." },
      { id: 26, cat: "식당/주문", word: "催菜", pinyin: "cuīcài", wordKo: "음식 재촉하다", senZh: "麻烦帮我们催一下菜。", senPy: "Máfan bāng wǒmen cuī yíxià cài.", senKo: "음식 좀 빨리 나오게 재촉 부탁드려요." },
      { id: 27, cat: "식당/주문", word: "微辣", pinyin: "wēilà", wordKo: "살짝 매운맛", senZh: "做微辣就可以了。", senPy: "Zuò wēilà jiù kěyǐ le.", senKo: "살짝만 맵게 해주시면 돼요." },
      { id: 28, cat: "식당/주문", word: "香菜", pinyin: "xiāngcài", wordKo: "고수", senZh: "千万别放香菜。", senPy: "Qiānwàn bié fàng xiāngcài.", senKo: "고수는 절대 넣지 마세요." },

      { id: 29, cat: "류리ON생활어휘", word: "我扫您", pinyin: "wǒ sǎo nín", wordKo: "제가 찍을게요 (QR)", senZh: "我扫您还是您扫我？", senPy: "Wǒ sǎo nín háishì nín sǎo wǒ?", senKo: "제가 찍을까요, 아니면 찍으시나요?" },
      { id: 30, cat: "류리ON생활어휘", word: "充电宝", pinyin: "chōngdiànbǎo", wordKo: "보조배터리", senZh: "这儿有充电宝可以借吗？", senPy: "Zhèr yǒu chōngdiànbǎo kěyǐ jiè ma?", senKo: "여기 보조배터리 대여할 수 있나요?" },
      { id: 31, cat: "류리ON생활어휘", word: "常温", pinyin: "chángwēn", wordKo: "상온 (미지근한 것)", senZh: "要一瓶常温矿泉水。", senPy: "Yào yì píng chángwēn kuàngquánshuǐ.", senKo: "상온 생수로 한 병 주세요." },
      { id: 32, cat: "류리ON생활어휘", word: "纸巾", pinyin: "zhǐjīn", wordKo: "휴지 / 냅킨", senZh: "服务员，麻烦拿一包纸巾。", senPy: "Fúwùyuán, máfan ná yì bāo zhǐjīn.", senKo: "직원분, 휴지 한 팩만 가져다주세요." },
      { id: 33, cat: "류리ON생활어휘", word: "打包", pinyin: "dǎbāo", wordKo: "포장하다 / 테이크아웃", senZh: "剩下的菜帮我们打包一下。", senPy: "Shèngxià de cài bāng wǒmen dǎbāo yíxià.", senKo: "남은 음식 포장 좀 해주세요." },
      { id: 34, cat: "류리ON생활어휘", word: "小票", pinyin: "xiǎopiào", wordKo: "영수증", senZh: "顺便打一张小票，谢谢！", senPy: "Shùnbiàn dǎ yì zhāng xiǎopiào, xièxie!", senKo: "영수증도 한 장 뽑아주세요, 감사합니다!" },
      { id: 35, cat: "류리ON생활어휘", word: "尾号", pinyin: "wěihào", wordKo: "번호 뒷자리 (디디/택시)", senZh: "手机尾号是四三二一。", senPy: "Shǒujī wěihào shì sì sān èr yī.", senKo: "휴대폰 번호 뒷자리는 4321입니다." },
      { id: 36, cat: "류리ON생활어휘", word: "靠边停", pinyin: "kàobiān tíng", wordKo: "갓길에 정차하다", senZh: "师傅，在门口靠边停一下。", senPy: "Shīfu, zài ménkǒu kàobiān tíng yíxià.", senKo: "기사님, 입구 갓길에 세워주세요." },

      { id: 37, cat: "만찬/비즈니스", word: "招牌菜", pinyin: "zhāopáicài", wordKo: "대표 메뉴 / 간판 요리", senZh: "先来一份正宗的锅包肉吧！", senPy: "Xiān lái yí fèn zhèngzōng de guōbāoròu ba!", senKo: "먼저 정통 꿔바오로우 하나 주세요!" },
      { id: 38, cat: "만찬/비즈니스", word: "以茶代酒", pinyin: "yǐ chá dài jiǔ", wordKo: "차로 술을 대신하다", senZh: "我以茶代酒敬您一杯！", senPy: "Wǒ yǐ chá dài jiǔ jìng nín yì bēi!", senKo: "차로 술을 대신해 한잔 올립니다!" },
      { id: 39, cat: "만찬/비즈니스", word: "黄金乱蹦", pinyin: "huángjīn luàn bèng", wordKo: "황금이 튀다 (MZ건배)", senZh: "酒杯一碰，黄金乱蹦！", senPy: "Jiǔbēi yí pèng, huángjīn luàn bèng!", senKo: "술잔을 딱 부딪치니 황금이 와르르!" },
      { id: 40, cat: "만찬/비즈니스", word: "结账", pinyin: "jiézhàng", wordKo: "계산하다", senZh: "麻烦结一下账。", senPy: "Máfan jié yíxià zhàng.", senKo: "계산 부탁드립니다." },
      { id: 41, cat: "만찬/비즈니스", word: "破费", pinyin: "pòfèi", wordKo: "무리하다 / 비용을 쓰다", senZh: "今天李总太破费了，非常感谢！", senPy: "Jīntiān Lǐ zǒng tài pòfèi le, fēicháng gǎnxiè!", senKo: "오늘 이 대표님께서 너무 무리하셨습니다, 감사합니다!" },
      { id: 42, cat: "만찬/비즈니스", word: "留步", pinyin: "liúbù", wordKo: "배웅을 멈추다", senZh: "您快留步，千万不用送了！", senPy: "Nín kuài liúbù, qiānwàn bú yòng sòng le!", senKo: "대표님 어서 들어가세요, 배웅 나오지 마세요!" },
      { id: 43, cat: "만찬/비즈니스", word: "特意", pinyin: "tèyì", wordKo: "일부러 / 특별히", senZh: "辛苦您特意跑一趟来接我！", senPy: "Xīnkǔ nín tèyì pǎo yí tàng lái jiē wǒ!", senKo: "일부러 마중 나와주셔서 감사합니다!" },
      { id: 44, cat: "만찬/비즈니스", word: "顺利", pinyin: "shùnlì", wordKo: "순조롭다", senZh: "航班非常顺利，一点都不累。", senPy: "Hángbān fēicháng shùnlì, yìdiǎn dōu bú lèi.", senKo: "비행은 아주 순조로웠고 전혀 피곤하지 않아요." }
    ];

    const CATEGORIES = ["전체", "★즐겨찾기", "교정기/검수", "식당/주문", "류리ON생활어휘", "만찬/비즈니스"];

    let currentCategory = "전체";
    let filteredList = [...VOCAB_DATA];
    let currentIndex = 0;
    let isAutoPlaying = false;
    let audioSpeed = 0.85;
    let intervalDelay = 3500;
    let isBlindMode = false;
    let starSet = new Set(JSON.parse(localStorage.getItem('changchun_stars') || "[]"));

    const toast = document.getElementById('toast');
    const toastText = document.getElementById('toast-text');
    const categoryTabs = document.getElementById('category-tabs');
    const btnToggleAuto = document.getElementById('btn-toggle-auto');
    const playBtnText = document.getElementById('play-btn-text');
    const playIcon = document.getElementById('play-icon');
    const autoStatusDot = document.getElementById('auto-status-dot');
    const autoStatusText = document.getElementById('auto-status-text');
    const currentIndexNum = document.getElementById('current-index-num');
    const totalCountNum = document.getElementById('total-count-num');
    const intervalSelect = document.getElementById('interval-select');
    const speedButtons = document.querySelectorAll('.speed-btn');

    const cardViewContainer = document.getElementById('card-view-container');
    const listViewContainer = document.getElementById('list-view-container');
    const btnModeCard = document.getElementById('btn-mode-card');
    const btnModeList = document.getElementById('btn-mode-list');

    const cardCategoryBadge = document.getElementById('card-category-badge');
    const cardWordHanzi = document.getElementById('card-word-hanzi');
    const cardWordPinyin = document.getElementById('card-word-pinyin');
    const cardWordMeaning = document.getElementById('card-word-meaning');
    const cardSentencePinyin = document.getElementById('card-sentence-pinyin');
    const cardSentenceHanzi = document.getElementById('card-sentence-hanzi');
    const cardSentenceMeaning = document.getElementById('card-sentence-meaning');

    const btnPlayWord = document.getElementById('btn-play-word');
    const btnPlaySentence = document.getElementById('btn-play-sentence');
    const btnCopyCard = document.getElementById('btn-copy-card');
    const btnPrevCard = document.getElementById('btn-prev-card');
    const btnNextCard = document.getElementById('btn-next-card');
    const btnReplayCard = document.getElementById('btn-replay-card');
    const btnStarCard = document.getElementById('btn-star-card');

    const btnToggleBlind = document.getElementById('btn-toggle-blind');
    const blindIcon = document.getElementById('blind-icon');
    const blindText = document.getElementById('blind-text');

    const showmeModal = document.getElementById('showme-modal');
    const showmeHanzi = document.getElementById('showme-hanzi');
    const showmePinyin = document.getElementById('showme-pinyin');
    const showmeKo = document.getElementById('showme-ko');
    const btnOpenShowme = document.getElementById('btn-open-showme');

    function showToast(msg) {
      toastText.innerText = msg;
      toast.classList.remove('hidden');
      setTimeout(() => toast.classList.add('hidden'), 2000);
    }

    function playTTS(text, speed = audioSpeed) {
      return new Promise((resolve) => {
        if ('speechSynthesis' in window) {
          window.speechSynthesis.cancel();
          const u = new SpeechSynthesisUtterance(text);
          u.lang = 'zh-CN';
          u.rate = speed;
          u.onend = () => resolve();
          u.onerror = () => resolve();
          window.speechSynthesis.speak(u);
        } else {
          setTimeout(resolve, 1500);
        }
      });
    }

    function delay(ms) { return new Promise((resolve) => setTimeout(resolve, ms)); }

    function copyText(text, msg = "복사되었습니다") {
      try {
        const el = document.createElement('textarea');
        el.value = text;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        showToast(msg);
      } catch (e) {
        if (navigator.clipboard) navigator.clipboard.writeText(text).then(() => showToast(msg));
      }
    }

    function openShowMe() {
      if (filteredList.length === 0) return;
      const item = filteredList[currentIndex];
      showmeHanzi.innerText = item.senZh;
      showmePinyin.innerText = item.senPy;
      showmeKo.innerText = `"${item.senKo}"`;
      showmeModal.classList.remove('hidden');
    }

    function closeShowMe() { showmeModal.classList.add('hidden'); }

    function toggleStar(item) {
      if (starSet.has(item.id)) {
        starSet.delete(item.id);
        showToast("즐겨찾기에서 해제되었습니다");
      } else {
        starSet.add(item.id);
        showToast("★ 즐겨찾기에 추가되었습니다");
      }
      localStorage.setItem('changchun_stars', JSON.stringify([...starSet]));
      updateCardStarUI();
      if (currentCategory === "★즐겨찾기") applyCategoryFilter();
    }

    function updateCardStarUI() {
      if (filteredList.length === 0) return;
      const item = filteredList[currentIndex];
      const isStarred = starSet.has(item.id);
      btnStarCard.className = `p-1 rounded-lg text-sm transition-all ${
        isStarred ? 'text-amber-400 font-bold scale-110' : 'text-slate-600 hover:text-slate-400'
      }`;
    }

    function applyCategoryFilter() {
      if (currentCategory === "전체") {
        filteredList = [...VOCAB_DATA];
      } else if (currentCategory === "★즐겨찾기") {
        filteredList = VOCAB_DATA.filter(item => starSet.has(item.id));
      } else {
        filteredList = VOCAB_DATA.filter(item => item.cat === currentCategory);
      }
      currentIndex = 0;
      updateCardView();
      renderListView();
    }

    function renderCategories() {
      categoryTabs.innerHTML = '';
      CATEGORIES.forEach(cat => {
        const btn = document.createElement('button');
        const isActive = cat === currentCategory;
        btn.className = `shrink-0 px-3 py-1 rounded-xl text-xs font-semibold transition-all ${
          isActive ? 'bg-sky-500 text-white font-bold shadow-sm' : 'bg-slate-800 text-slate-400 hover:text-slate-200'
        }`;
        if (cat === "★즐겨찾기") {
          btn.innerText = `★ 즐겨찾기 (${starSet.size})`;
          btn.className += ' text-amber-300';
        } else {
          btn.innerText = cat;
        }
        btn.onclick = () => {
          currentCategory = cat;
          applyCategoryFilter();
          renderCategories();
        };
        categoryTabs.appendChild(btn);
      });
    }

    function updateCardView() {
      if (filteredList.length === 0) {
        cardWordHanzi.innerText = "데이터 없음";
        cardWordPinyin.innerText = "";
        cardWordMeaning.innerText = "즐겨찾기 항목이 비어 있습니다.";
        cardSentencePinyin.innerText = "";
        cardSentenceHanzi.innerText = "별표(★)를 눌러 원하는 문장을 등록하세요.";
        cardSentenceMeaning.innerText = "";
        currentIndexNum.innerText = 0;
        totalCountNum.innerText = 0;
        return;
      }
      const item = filteredList[currentIndex];
      cardCategoryBadge.innerText = item.cat;
      cardWordHanzi.innerText = item.word;
      cardWordPinyin.innerText = item.pinyin;
      cardWordMeaning.innerText = item.wordKo;
      cardSentencePinyin.innerText = item.senPy;
      cardSentenceHanzi.innerText = item.senZh;
      cardSentenceMeaning.innerText = `"${item.senKo}"`;
      currentIndexNum.innerText = currentIndex + 1;
      totalCountNum.innerText = filteredList.length;
      updateCardStarUI();
    }

    function renderListView() {
      listViewContainer.innerHTML = '';
      filteredList.forEach((item, idx) => {
        const isCurrent = idx === currentIndex;
        const isStarred = starSet.has(item.id);
        const row = document.createElement('div');
        row.className = `p-3 rounded-2xl border transition-all cursor-pointer ${
          isCurrent ? 'bg-slate-900 border-sky-500 shadow-md' : 'bg-slate-900/60 border-slate-800 hover:border-slate-700'
        }`;
        row.innerHTML = `
          <div class="flex items-center justify-between mb-1">
            <span class="text-[10px] font-bold text-amber-400 bg-amber-950/40 border border-amber-800/40 px-2 py-0.5 rounded">
              ${item.word} (${item.pinyin}) - ${item.wordKo}
            </span>
            <div class="flex items-center gap-1.5">
              <span class="text-xs ${isStarred ? 'text-amber-400' : 'text-slate-600'}">★</span>
              <span class="text-[10px] text-slate-500">${item.cat}</span>
            </div>
          </div>
          <div class="text-xs font-mono text-emerald-400 mt-1">${item.senPy}</div>
          <div class="text-sm font-bold text-slate-100">${item.senZh}</div>
          <div class="text-xs text-sky-300 mt-0.5">${item.senKo}</div>
        `;
        row.onclick = () => {
          currentIndex = idx;
          updateCardView();
          renderListView();
          playTTS(item.senZh);
        };
        listViewContainer.appendChild(row);
      });
    }

    async function runAutoRoutine() {
      while (isAutoPlaying) {
        if (filteredList.length === 0) { stopAutoPlay(); return; }
        const item = filteredList[currentIndex];
        updateCardView();
        renderListView();

        autoStatusText.innerText = `🎙️ [단어] ${item.word}`;
        await playTTS(item.word, audioSpeed);
        if (!isAutoPlaying) return;
        await delay(600);

        autoStatusText.innerText = `🗣️ [문장] 따라하세요!`;
        await playTTS(item.senZh, audioSpeed);
        if (!isAutoPlaying) return;

        await delay(intervalDelay);
        if (!isAutoPlaying) return;

        currentIndex = (currentIndex + 1) % filteredList.length;
      }
    }

    function toggleAutoPlay() {
      if (filteredList.length === 0) {
        showToast("재생할 카드가 없습니다");
        return;
      }
      isAutoPlaying = !isAutoPlaying;

      if (isAutoPlaying) {
        btnToggleAuto.className = "w-full py-3 px-4 rounded-xl font-bold text-sm flex items-center justify-center gap-2 transition-all active:scale-[0.99] bg-amber-500 text-slate-950 shadow-lg shadow-amber-500/20";
        playBtnText.innerText = "일시 정지";
        playIcon.innerHTML = '<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>';
        autoStatusDot.className = "w-2 h-2 rounded-full bg-emerald-400 animate-ping";
        autoStatusText.innerText = "자동 섀도잉 루프 진행 중";
        runAutoRoutine();
      } else {
        stopAutoPlay();
      }
    }

    function stopAutoPlay() {
      isAutoPlaying = false;
      window.speechSynthesis && window.speechSynthesis.cancel();
      btnToggleAuto.className = "w-full py-3 px-4 rounded-xl font-bold text-sm flex items-center justify-center gap-2 transition-all active:scale-[0.99] bg-sky-500 text-white shadow-lg shadow-sky-500/20";
      playBtnText.innerText = "▶ 유튜브 스타일 자동 섀도잉 시작";
      playIcon.innerHTML = '<path d="M8 5v14l11-7z"/>';
      autoStatusDot.className = "w-2 h-2 rounded-full bg-slate-600";
      autoStatusText.innerText = "정지됨";
    }

    btnToggleBlind.onclick = () => {
      isBlindMode = !isBlindMode;
      if (isBlindMode) {
        document.body.classList.add('blind-active');
        btnToggleBlind.className = "px-2 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 border border-amber-400 font-bold transition-all flex items-center gap-1";
        blindIcon.innerText = "👀";
        blindText.innerText = "노룩 ON";
        showToast("노룩 모드 활성화: 한국어만 보고 먼저 말해보세요!");
      } else {
        document.body.classList.remove('blind-active');
        btnToggleBlind.className = "px-2 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-400 border border-slate-700 hover:text-amber-300 transition-all flex items-center gap-1";
        blindIcon.innerText = "🙈";
        blindText.innerText = "노룩";
      }
    };

    btnToggleAuto.onclick = toggleAutoPlay;
    btnPlayWord.onclick = (e) => { e.stopPropagation(); playTTS(filteredList[currentIndex].word); };
    btnPlaySentence.onclick = (e) => { e.stopPropagation(); playTTS(filteredList[currentIndex].senZh); };

    btnReplayCard.onclick = () => {
      if (filteredList.length === 0) return;
      const item = filteredList[currentIndex];
      playTTS(item.word).then(() => delay(500)).then(() => playTTS(item.senZh));
    };

    btnPrevCard.onclick = () => {
      if (filteredList.length === 0) return;
      currentIndex = (currentIndex > 0) ? currentIndex - 1 : filteredList.length - 1;
      updateCardView(); renderListView(); playTTS(filteredList[currentIndex].senZh);
    };

    btnNextCard.onclick = () => {
      if (filteredList.length === 0) return;
      currentIndex = (currentIndex + 1) % filteredList.length;
      updateCardView(); renderListView(); playTTS(filteredList[currentIndex].senZh);
    };

    btnStarCard.onclick = () => {
      if (filteredList.length === 0) return;
      toggleStar(filteredList[currentIndex]);
      renderCategories();
    };

    btnOpenShowme.onclick = openShowMe;

    btnCopyCard.onclick = () => {
      if (filteredList.length === 0) return;
      const item = filteredList[currentIndex];
      const copyStr = `[단어] ${item.word} (${item.pinyin}) - ${item.wordKo}\n[실전문장] ${item.senZh}\n${item.senPy}\n(${item.senKo})`;
      copyText(copyStr, "단어 & 문장이 복사되었습니다");
    };

    btnModeCard.onclick = () => {
      btnModeCard.className = "px-2 py-1 rounded font-bold bg-sky-500 text-white transition-all";
      btnModeList.className = "px-2 py-1 rounded text-slate-400 hover:text-slate-200 transition-all";
      cardViewContainer.classList.remove('hidden');
      listViewContainer.classList.add('hidden');
    };

    btnModeList.onclick = () => {
      btnModeList.className = "px-2 py-1 rounded font-bold bg-sky-500 text-white transition-all";
      btnModeCard.className = "px-2 py-1 rounded text-slate-400 hover:text-slate-200 transition-all";
      cardViewContainer.classList.add('hidden');
      listViewContainer.classList.remove('hidden');
    };

    intervalSelect.onchange = (e) => { intervalDelay = parseInt(e.target.value); };

    speedButtons.forEach(btn => {
      btn.onclick = () => {
        speedButtons.forEach(b => b.className = "speed-btn px-1.5 py-0.5 rounded text-slate-400");
        btn.className = "speed-btn px-1.5 py-0.5 rounded bg-sky-500 text-white font-bold";
        audioSpeed = parseFloat(btn.dataset.speed);
      };
    });

    window.addEventListener('DOMContentLoaded', () => {
      renderCategories();
      updateCardView();
      renderListView();
    });
  </script>
</body>
</html>
"""

components.html(HTML_CONTENT, height=890, scrolling=True)
