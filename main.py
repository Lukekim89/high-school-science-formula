<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>고등학교 과학 공식 모음</title>
  <style>
    :root {
      --bg-cream: #FFFDF5;
      --card-cream: #FFF9E6;
      --primary-yellow: #F6D061;
      --primary-hover: #E3B83B;
      --accent-warm: #E27B58;
      --accent-soft: #FFE385;
      --text-dark: #332C23;
      --text-muted: #6B5E4C;
      --border-warm: #EADCB9;
      --shadow-soft: 0 8px 24px rgba(165, 130, 70, 0.08);
      --font-main: 'Pretendard', 'Noto Sans KR', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; font-family: var(--font-main); }
    body { background-color: var(--bg-cream); color: var(--text-dark); min-height: 100vh; padding-bottom: 60px; line-height: 1.6; }

    header {
      background-color: var(--card-cream);
      border-bottom: 2px solid var(--border-warm);
      padding: 18px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }

    .header-left { display: flex; align-items: center; gap: 16px; }
    .back-btn {
      background: #FFF;
      border: 2px solid var(--border-warm);
      border-radius: 12px;
      padding: 8px 16px;
      font-size: 18px;
      font-weight: bold;
      color: var(--text-dark);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      visibility: hidden;
    }
    .back-btn.visible { visibility: visible; }
    .back-btn:hover { background: var(--primary-yellow); border-color: var(--primary-hover); transform: translateX(-2px); }

    h1.app-title { font-size: 24px; font-weight: 800; color: var(--text-dark); letter-spacing: -0.5px; }
    .badge-curr {
      background-color: var(--accent-warm);
      color: #FFF;
      font-size: 13px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 20px;
    }

    main.container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
    .step-section { display: none; }
    .step-section.active { display: block; animation: fadeIn 0.3s ease; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .section-header { text-align: center; margin-bottom: 30px; }
    .section-header h2 { font-size: 28px; font-weight: 800; margin-bottom: 8px; color: #2C241B; }
    .section-header p { font-size: 16px; color: var(--text-muted); }

    .grid-selection { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-top: 20px; }
    .select-card {
      background-color: var(--card-cream);
      border: 2px solid var(--border-warm);
      border-radius: 20px;
      padding: 32px 24px;
      text-align: center;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      box-shadow: var(--shadow-soft);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }
    .select-card:hover {
      transform: translateY(-6px);
      background-color: var(--accent-soft);
      border-color: var(--primary-hover);
    }
    .select-card .icon { font-size: 42px; margin-bottom: 4px; }
    .select-card .title { font-size: 22px; font-weight: 800; }
    .select-card .desc { font-size: 14px; color: var(--text-muted); }

    .search-box-container {
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .search-box {
      display: flex;
      align-items: center;
      gap: 12px;
      background: #FFF;
      padding: 10px 18px;
      border-radius: 16px;
      border: 2px solid var(--border-warm);
      box-shadow: 0 4px 10px rgba(0,0,0,0.02);
    }
    .search-box input {
      border: none;
      outline: none;
      width: 100%;
      font-size: 17px;
      padding: 4px;
    }
    .search-hint {
      font-size: 13.5px;
      color: var(--text-muted);
      padding-left: 6px;
    }

    .formula-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
    .formula-btn-card {
      background: #FFF;
      border: 2px solid var(--border-warm);
      border-radius: 16px;
      padding: 20px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }
    .formula-btn-card:hover {
      border-color: var(--primary-hover);
      background-color: var(--card-cream);
      transform: translateY(-3px);
    }
    .formula-btn-card .f-name { font-size: 18px; font-weight: 700; color: var(--text-dark); }
    .formula-btn-card .f-unit { font-size: 13px; color: var(--accent-warm); font-weight: 600; }
    .formula-btn-card .f-preview {
      font-size: 16px;
      font-family: 'Times New Roman', Times, serif;
      font-style: italic;
      color: #444;
      background: #FFFDF5;
      padding: 8px 12px;
      border-radius: 8px;
      border: 1px dashed var(--border-warm);
      margin-top: 4px;
    }
    .formula-btn-card .f-vars-list {
      font-size: 12.5px;
      color: #887B67;
      margin-top: 2px;
      word-break: break-all;
    }

    .modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.4);
      backdrop-filter: blur(4px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 20px;
    }
    .modal-overlay.active { display: flex; }
    .modal-content {
      background: var(--bg-cream);
      border: 3px solid var(--border-warm);
      border-radius: 24px;
      max-width: 800px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 32px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.15);
      position: relative;
    }
    .close-modal-btn {
      position: absolute;
      top: 20px; right: 20px;
      background: #FFF;
      border: 2px solid var(--border-warm);
      width: 40px; height: 40px;
      border-radius: 50%;
      font-size: 20px;
      font-weight: bold;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .close-modal-btn:hover { background: var(--accent-warm); color: #FFF; }

    .math-display {
      background: #FFF;
      border: 2px solid var(--border-warm);
      border-radius: 16px;
      padding: 24px;
      text-align: center;
      margin: 20px 0;
      font-size: 26px;
      font-family: 'Times New Roman', Georgia, serif;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.02);
    }

    .frac { display: inline-block; vertical-align: middle; text-align: center; font-size: 0.9em; padding: 0 4px; }
    .frac > span { display: block; }
    .frac span.bottom { border-top: 2px solid var(--text-dark); padding-top: 2px; }

    .modal-section-title {
      font-size: 18px;
      font-weight: 800;
      color: var(--text-dark);
      margin: 24px 0 12px 0;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .modal-section-title::before {
      content: '';
      display: inline-block;
      width: 6px;
      height: 18px;
      background: var(--accent-warm);
      border-radius: 3px;
    }

    .var-table {
      width: 100%;
      border-collapse: collapse;
      background: #FFF;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid var(--border-warm);
    }
    .var-table th, .var-table td { padding: 10px 14px; text-align: left; font-size: 15px; }
    .var-table th { background: var(--card-cream); font-weight: 700; border-bottom: 2px solid var(--border-warm); }
    .var-table tr:not(:last-child) td { border-bottom: 1px solid #F0E6D2; }

    .calc-box {
      background: var(--card-cream);
      border: 2px solid var(--border-warm);
      border-radius: 16px;
      padding: 20px;
    }
    .calc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .input-group { display: flex; flex-direction: column; gap: 6px; }
    .input-group label { font-size: 14px; font-weight: 700; }
    .input-group input {
      padding: 10px;
      border-radius: 10px;
      border: 1px solid var(--border-warm);
      font-size: 16px;
      outline: none;
    }
    .calc-btn {
      background: var(--primary-yellow);
      border: none;
      padding: 12px 24px;
      border-radius: 12px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      width: 100%;
      transition: background 0.2s;
    }
    .calc-btn:hover { background: var(--primary-hover); }
    .calc-result {
      margin-top: 14px;
      padding: 14px;
      background: #FFF;
      border-radius: 10px;
      font-weight: bold;
      font-size: 17px;
      text-align: center;
      color: var(--accent-warm);
      border: 1px solid var(--border-warm);
    }

    .chart-container {
      background: #FFF;
      border: 2px solid var(--border-warm);
      border-radius: 16px;
      padding: 16px;
      margin-top: 16px;
      text-align: center;
    }
    canvas { max-width: 100%; height: auto; }
  </style>
</head>
<body>

  <header>
    <div class="header-left">
      <button id="backBtn" class="back-btn" onclick="goBack()">← 뒤로</button>
      <h1 class="app-title">고등학교 과학 공식 모음</h1>
    </div>
    <span class="badge-curr">2022 개정 교육과정 (70+ 공식)</span>
  </header>

  <main class="container">
    <!-- 1단계: 학년 선택 -->
    <section id="stepGrade" class="step-section active">
      <div class="section-header">
        <h2>학년을 선택하세요</h2>
        <p>배우고자 하는 고등학교 학년을 클릭하세요.</p>
      </div>
      <div class="grid-selection">
        <div class="select-card" onclick="selectGrade(1)">
          <div class="icon">🌱</div>
          <div class="title">고등학교 1학년</div>
          <div class="desc">통합과학 1 · 통합과학 2 (전 과정 공식)</div>
        </div>
        <div class="select-card" onclick="selectGrade(2)">
          <div class="icon">🌿</div>
          <div class="title">고등학교 2학년</div>
          <div class="desc">물리학Ⅰ, 화학Ⅰ, 생명과학Ⅰ, 지구과학Ⅰ</div>
        </div>
        <div class="select-card" onclick="selectGrade(3)">
          <div class="icon">🌳</div>
          <div class="title">고등학교 3학년</div>
          <div class="desc">물리학Ⅱ, 화학Ⅱ, 생명과학Ⅱ, 지구과학Ⅱ</div>
        </div>
      </div>
    </section>

    <!-- 2단계: 과목 선택 -->
    <section id="stepSubject" class="step-section">
      <div class="section-header">
        <h2 id="subjectTitle">과목을 선택하세요</h2>
        <p>공식을 확인하고 싶은 과목을 누르세요.</p>
      </div>
      <div id="subjectGrid" class="grid-selection"></div>
    </section>

    <!-- 3단계: 공식 목록 및 검색 -->
    <section id="stepFormulaList" class="step-section">
      <div class="section-header">
        <h2 id="formulaListTitle">공식 목록</h2>
        <p>공식 이름이나 미지수(v, F, m, t, P, λ, pH 등)를 검색해보세요.</p>
      </div>
      
      <div class="search-box-container">
        <div class="search-box">
          🔍 <input type="text" id="searchInput" placeholder="공식 이름, 설명 또는 미지수(v, m, F, t, λ 등) 입력..." oninput="filterFormulas()">
        </div>
        <div class="search-hint">💡 <b>미지수 검색 지원:</b> 'v', 'm', '속도', '질량', '전압', 'pH' 기호나 명칭으로 전체 탐색이 가능합니다.</div>
      </div>

      <div id="formulaGrid" class="formula-grid"></div>
    </section>
  </main>

  <!-- 상세 모달 -->
  <div id="formulaModal" class="modal-overlay">
    <div class="modal-content">
      <button class="close-modal-btn" onclick="closeModal()">✕</button>
      <h2 id="modalTitle" style="font-size:24px; font-weight:800;">공식 이름</h2>
      <div id="modalCategory" style="color:var(--text-muted); font-size:14px; margin-top:4px;">단원명</div>
      
      <div class="math-display" id="modalMath"></div>

      <div class="modal-section-title">공식 설명</div>
      <p id="modalDesc" style="font-size:16px; color:#444; word-break:keep-all;"></p>

      <div class="modal-section-title">기호 및 변수(미지수) 설명</div>
      <table class="var-table">
        <thead>
          <tr>
            <th>기호</th>
            <th>의미</th>
            <th>기본 단위</th>
          </tr>
        </thead>
        <tbody id="modalVarTable"></tbody>
      </table>

      <div class="modal-section-title">실시간 대입 계산기</div>
      <div class="calc-box">
        <div id="calcInputs" class="calc-grid"></div>
        <button class="calc-btn" onclick="runCalculation()">값 계산하기</button>
        <div id="calcResult" class="calc-result">알려진 미지수 값을 입력하고 버튼을 누르세요.</div>
      </div>

      <div id="chartSection" style="display:none;">
        <div class="modal-section-title">실시간 그래프 변화</div>
        <div class="chart-container">
          <canvas id="formulaCanvas" width="600" height="260"></canvas>
        </div>
      </div>
    </div>
  </div>

  <script>
    const database = [
      // ---------------- 통합과학 (고1) ----------------
      {
        id: 'sc1_vel', grade: 1, subject: '통합과학', name: '평균 속도',
        mathHtml: 'v = <div class="frac"><span>Δs</span><span class="bottom">Δt</span></div>',
        desc: '변위를 걸린 시간으로 나눈 값으로, 운동의 방향과 빠르기를 함께 나타냅니다.',
        vars: [{ symbol: 'v', name: '평균 속도', unit: 'm/s' }, { symbol: 'Δs', name: '변위', unit: 'm' }, { symbol: 'Δt', name: '걸린 시간', unit: 's' }],
        calc: (inps) => (inps.ds && inps.dt) ? `평균 속도 (v) = ${(inps.ds / inps.dt).toFixed(2)} m/s` : '변위와 시간을 입력하세요.',
        inputs: [{ id: 'ds', label: '변위 Δs (m)' }, { id: 'dt', label: '시간 Δt (s)' }],
        hasChart: true,
        drawChart: (ctx, inps) => {
          const ds = parseFloat(inps.ds) || 10, dt = parseFloat(inps.dt) || 2;
          ctx.clearRect(0,0,600,260); ctx.beginPath(); ctx.strokeStyle="#EADCB9"; ctx.moveTo(50, 200); ctx.lineTo(550, 200); ctx.moveTo(50, 200); ctx.lineTo(50, 30); ctx.stroke();
          ctx.beginPath(); ctx.strokeStyle="#E27B58"; ctx.lineWidth=3; ctx.moveTo(50, 200); ctx.lineTo(50 + Math.min(dt*40, 450), 200 - Math.min(ds*10, 160)); ctx.stroke();
          ctx.fillStyle="#332C23"; ctx.fillText("시간 t (s)", 520, 220); ctx.fillText("변위 s (m)", 20, 25);
        }
      },
      {
        id: 'sc1_p', grade: 1, subject: '통합과학', name: '운동량',
        mathHtml: 'p = m · v',
        desc: '운동하는 물체의 운동 효과 크기를 나타내는 물리량입니다.',
        vars: [{ symbol: 'p', name: '운동량', unit: 'kg·m/s' }, { symbol: 'm', name: '질량', unit: 'kg' }, { symbol: 'v', name: '속도', unit: 'm/s' }],
        calc: (inps) => (inps.m && inps.v) ? `운동량 (p) = ${(inps.m * inps.v).toFixed(2)} kg·m/s` : 'm과 v를 입력하세요.',
        inputs: [{ id: 'm', label: '질량 m (kg)' }, { id: 'v', label: '속도 v (m/s)' }]
      },
      {
        id: 'sc1_I', grade: 1, subject: '통합과학', name: '충격량',
        mathHtml: 'I = F · Δt = Δp',
        desc: '물체에 가해진 힘과 작용 시간의 곱으로, 운동량의 변화량과 동일합니다.',
        vars: [{ symbol: 'I', name: '충격량', unit: 'N·s' }, { symbol: 'F', name: '힘', unit: 'N' }, { symbol: 'Δt', name: '시간', unit: 's' }],
        calc: (inps) => (inps.f && inps.dt) ? `충격량 (I) = ${(inps.f * inps.dt).toFixed(2)} N·s` : 'F와 Δt를 입력하세요.',
        inputs: [{ id: 'f', label: '힘 F (N)' }, { id: 'dt', label: '시간 Δt (s)' }]
      },
      {
        id: 'sc1_ep', grade: 1, subject: '통합과학', name: '중력 위치 에너지',
        mathHtml: 'E<sub>p</sub> = m · g · h',
        desc: '기준면으로부터 높이 h에 위치한 물체가 중력에 의해 가지는 위치 에너지입니다.',
        vars: [{ symbol: 'Ep', name: '위치 에너지', unit: 'J' }, { symbol: 'm', name: '질량', unit: 'kg' }, { symbol: 'g', name: '중력가속도', unit: 'm/s² (9.8)' }, { symbol: 'h', name: '높이', unit: 'm' }],
        calc: (inps) => (inps.m && inps.h) ? `위치 에너지 (Ep) = ${(inps.m * 9.8 * inps.h).toFixed(2)} J` : '질량 m과 높이 h를 입력하세요.',
        inputs: [{ id: 'm', label: '질량 m (kg)' }, { id: 'h', label: '높이 h (m)' }]
      },
      {
        id: 'sc1_ek', grade: 1, subject: '통합과학', name: '운동 에너지',
        mathHtml: 'E<sub>k</sub> = <div class="frac"><span>1</span><span class="bottom">2</span></div> m · v<sup>2</sup>',
        desc: '속도 v로 운동하는 질량 m인 물체가 가지는 운동 에너지입니다.',
        vars: [{ symbol: 'Ek', name: '운동 에너지', unit: 'J' }, { symbol: 'm', name: '질량', unit: 'kg' }, { symbol: 'v', name: '속도', unit: 'm/s' }],
        calc: (inps) => (inps.m && inps.v) ? `운동 에너지 (Ek) = ${(0.5 * inps.m * inps.v * inps.v).toFixed(2)} J` : '질량 m과 속도 v를 입력하세요.',
        inputs: [{ id: 'm', label: '질량 m (kg)' }, { id: 'v', label: '속도 v (m/s)' }]
      },
      {
        id: 'sc1_ohm', grade: 1, subject: '통합과학', name: '옴의 법칙',
        mathHtml: 'V = I · R',
        desc: '회로에 흐르는 전류의 세기는 전압에 비례하고 저항에 반비례합니다.',
        vars: [{ symbol: 'V', name: '전압', unit: 'V' }, { symbol: 'I', name: '전류', unit: 'A' }, { symbol: 'R', name: '저항', unit: 'Ω' }],
        calc: (inps) => (inps.i && inps.r) ? `전압 (V) = ${(inps.i * inps.r).toFixed(2)} V` : 'I와 R을 입력하세요.',
        inputs: [{ id: 'i', label: '전류 I (A)' }, { id: 'r', label: '저항 R (Ω)' }]
      },
      {
        id: 'sc1_power', grade: 1, subject: '통합과학', name: '소비 전력',
        mathHtml: 'P = V · I',
        desc: '전기 기구가 1초 동안 소비하는 전기 에너지의 양입니다.',
        vars: [{ symbol: 'P', name: '전력', unit: 'W' }, { symbol: 'V', name: '전압', unit: 'V' }, { symbol: 'I', name: '전류', unit: 'A' }],
        calc: (inps) => (inps.v && inps.i) ? `전력 (P) = ${(inps.v * inps.i).toFixed(2)} W` : 'V와 I를 입력하세요.',
        inputs: [{ id: 'v', label: '전압 V (V)' }, { id: 'i', label: '전류 I (A)' }]
      },
      {
        id: 'sc1_ploss', grade: 1, subject: '통합과학', name: '전력 수송 손실 전력',
        mathHtml: 'P<sub>손실</sub> = I<sup>2</sup> · R',
        desc: '송전선에서 저항 R에 의해 열에너지로 손실되는 전력입니다.',
        vars: [{ symbol: 'P손실', name: '손실 전력', unit: 'W' }, { symbol: 'I', name: '송전 전류', unit: 'A' }, { symbol: 'R', name: '송전선 저항', unit: 'Ω' }],
        calc: (inps) => (inps.i && inps.r) ? `손실 전력 = ${(inps.i * inps.i * inps.r).toFixed(2)} W` : 'I와 R을 입력하세요.',
        inputs: [{ id: 'i', label: '전류 I (A)' }, { id: 'r', label: '저항 R (Ω)' }]
      },
      {
        id: 'sc1_mole', grade: 1, subject: '통합과학', name: '물질의 양과 몰수 산출',
        mathHtml: 'n = <div class="frac"><span>m (질량)</span><span class="bottom">M (몰질량)</span></div> = <div class="frac"><span>N (입자수)</span><span class="bottom">6.02 × 10<sup>23</sup></span></div>',
        desc: '화학 물질의 몰수(n)는 질량을 화학식량(M)으로 나누어 구합니다.',
        vars: [{ symbol: 'n', name: '몰수', unit: 'mol' }, { symbol: 'm', name: '질량', unit: 'g' }, { symbol: 'M', name: '몰질량', unit: 'g/mol' }],
        calc: (inps) => (inps.m && inps.mw) ? `몰수 (n) = ${(inps.m / inps.mw).toFixed(3)} mol` : '질량과 몰질량을 입력하세요.',
        inputs: [{ id: 'm', label: '질량 m (g)' }, { id: 'mw', label: '몰질량 M (g/mol)' }]
      },

      // ---------------- 물리학Ⅰ (고2) ----------------
      {
        id: 'phy1_fma', grade: 2, subject: '물리학Ⅰ', name: '운동 방정식 (뉴턴 제2법칙)',
        mathHtml: 'F = m · a',
        desc: '물체에 가해진 알짜힘 F는 질량 m과 가속도 a의 곱과 같습니다.',
        vars: [{ symbol: 'F', name: '알짜힘', unit: 'N' }, { symbol: 'm', name: '질량', unit: 'kg' }, { symbol: 'a', name: '가속도', unit: 'm/s²' }],
        calc: (inps) => (inps.m && inps.a) ? `힘 (F) = ${(inps.m * inps.a).toFixed(2)} N` : 'm과 a를 입력하세요.',
        inputs: [{ id: 'm', label: '질량 m (kg)' }, { id: 'a', label: '가속도 a (m/s²)' }]
      },
      {
        id: 'phy1_v', grade: 2, subject: '물리학Ⅰ', name: '등가속도 속도 공식',
        mathHtml: 'v = v<sub>0</sub> + a · t',
        desc: '등가속도 운동하는 물체의 시간 t 후의 속도입니다.',
        vars: [{ symbol: 'v', name: '나중 속도', unit: 'm/s' }, { symbol: 'v₀', name: '초기 속도', unit: 'm/s' }, { symbol: 'a', name: '가속도', unit: 'm/s²' }, { symbol: 't', name: '시간', unit: 's' }],
        calc: (inps) => `나중 속도 (v) = ${(parseFloat(inps.v0||0) + parseFloat(inps.a||0)*parseFloat(inps.t||0)).toFixed(2)} m/s`,
        inputs: [{ id: 'v0', label: '초기속도 v₀' }, { id: 'a', label: '가속도 a' }, { id: 't', label: '시간 t' }]
      },
      {
        id: 'phy1_s', grade: 2, subject: '물리학Ⅰ', name: '등가속도 위치 공식',
        mathHtml: 's = v<sub>0</sub>t + <div class="frac"><span>1</span><span class="bottom">2</span></div>a t<sup>2</sup>',
        desc: '등가속도 운동 물체의 이동 거리 변위 식입니다.',
        vars: [{ symbol: 's', name: '변위', unit: 'm' }, { symbol: 'v0', name: '초기속도', unit: 'm/s' }, { symbol: 'a', name: '가속도', unit: 'm/s²' }, { symbol: 't', name: '시간', unit: 's' }],
        calc: (inps) => `이동거리 (s) = ${(parseFloat(inps.v0||0)*parseFloat(inps.t||0) + 0.5*parseFloat(inps.a||0)*Math.pow(parseFloat(inps.t||0),2)).toFixed(2)} m`,
        inputs: [{ id: 'v0', label: '초기속도 v₀' }, { id: 'a', label: '가속도 a' }, { id: 't', label: '시간 t' }]
      },
      {
        id: 'phy1_2as', grade: 2, subject: '물리학Ⅰ', name: '등가속도 속도-위치 공식 (시간 t 제거)',
        mathHtml: '2a · s = v<sup>2</sup> - v<sub>0</sub><sup>2</sup>',
        desc: '시간 t 정보가 주어지지 않을 때 속도와 위치 관계를 계산하는 식입니다.',
        vars: [{ symbol: 'a', name: '가속도', unit: 'm/s²' }, { symbol: 's', name: '변위', unit: 'm' }, { symbol: 'v', name: '나중속도', unit: 'm/s' }, { symbol: 'v₀', name: '초기속도', unit: 'm/s' }],
        calc: (inps) => (inps.v && inps.v0 && inps.a) ? `변위 s = ${((Math.pow(inps.v,2)-Math.pow(inps.v0,2))/(2*inps.a)).toFixed(2)} m` : 'v, v₀, a를 입력하세요.',
        inputs: [{ id: 'v', label: '나중속도 v' }, { id: 'v0', label: '초기속도 v₀' }, { id: 'a', label: '가속도 a' }]
      },
      {
        id: 'phy1_thermal', grade: 2, subject: '물리학Ⅰ', name: '열역학 제1법칙',
        mathHtml: 'Q = ΔU + W',
        desc: '기체에 흡수된 열량 Q는 내부 에너지 변화량(ΔU)과 외부로 한 일(W)의 합과 같습니다.',
        vars: [{ symbol: 'Q', name: '흡수한 열량', unit: 'J' }, { symbol: 'ΔU', name: '내부에너지 변화', unit: 'J' }, { symbol: 'W', name: '한 일 (P·ΔV)', unit: 'J' }],
        calc: (inps) => (inps.du && inps.w) ? `열량 Q = ${(parseFloat(inps.du) + parseFloat(inps.w)).toFixed(2)} J` : 'ΔU와 W를 입력하세요.',
        inputs: [{ id: 'du', label: '내부에너지 변화 ΔU (J)' }, { id: 'w', label: '한 일 W (J)' }]
      },
      {
        id: 'phy1_snell', grade: 2, subject: '물리학Ⅰ', name: '굴절의 법칙 (스넬의 법칙)',
        mathHtml: 'n<sub>1</sub> sin θ<sub>1</sub> = n<sub>2</sub> sin θ<sub>2</sub>',
        desc: '두 매질의 경계면에서 빛이 굴절할 때 각 매질의 굴절률과 굴절각 사이의 상호 관계입니다.',
        vars: [{ symbol: 'n1', name: '매질1 굴절률', unit: '-' }, { symbol: 'θ1', name: '입사각', unit: '°' }, { symbol: 'n2', name: '매질2 굴절률', unit: '-' }, { symbol: 'θ2', name: '굴절각', unit: '°' }],
        calc: (inps) => '각도와 굴절률 삼각비 관계식입니다.', inputs: []
      },
      {
        id: 'phy1_debroglie', grade: 2, subject: '물리학Ⅰ', name: '드브로이 물질파 파장',
        mathHtml: 'λ = <div class="frac"><span>h</span><span class="bottom">p</span></div> = <div class="frac"><span>h</span><span class="bottom">m · v</span></div>',
        desc: '운동하는 입자가 가지는 파동성 물질파 파장 계산식입니다.',
        vars: [{ symbol: 'λ', name: '물질파 파장', unit: 'm' }, { symbol: 'h', name: '플랑크 상수', unit: 'J·s' }, { symbol: 'p', name: '운동량', unit: 'kg·m/s' }],
        calc: (inps) => (inps.m && inps.v) ? `파장 (λ) ≈ ${(6.63e-34 / (inps.m * inps.v)).toExponential(3)} m` : '질량과 속도를 입력하세요.',
        inputs: [{ id: 'm', label: '질량 m (kg)' }, { id: 'v', label: '속도 v (m/s)' }]
      },

      // ---------------- 화학Ⅰ (고2) ----------------
      {
        id: 'ch1_molar', grade: 2, subject: '화학Ⅰ', name: '몰농도 (Molarity)',
        mathHtml: 'M = <div class="frac"><span>n (용질 몰수)</span><span class="bottom">V (용액 L)</span></div>',
        desc: '용액 1L 속에 포함되어 있는 용질의 몰수입니다.',
        vars: [{ symbol: 'M', name: '몰농도', unit: 'M' }, { symbol: 'n', name: '몰수', unit: 'mol' }, { symbol: 'V', name: '부피', unit: 'L' }],
        calc: (inps) => (inps.n && inps.v) ? `몰농도 = ${(inps.n / inps.v).toFixed(3)} M` : 'n과 V를 입력하세요.',
        inputs: [{ id: 'n', label: '몰수 n (mol)' }, { id: 'v', label: '부피 V (L)' }]
      },
      {
        id: 'ch1_molal', grade: 2, subject: '화학Ⅰ', name: '몰랄농도 (Molality)',
        mathHtml: 'm = <div class="frac"><span>용질의 몰수 (mol)</span><span class="bottom">용매의 질량 (kg)</span></div>',
        desc: '용매 1kg 속에 용해되어 있는 용질의 몰수입니다.',
        vars: [{ symbol: 'm', name: '몰랄농도', unit: 'm (mol/kg)' }, { symbol: 'n', name: '용질 몰수', unit: 'mol' }, { symbol: 'w', name: '용매 질량', unit: 'kg' }],
        calc: (inps) => (inps.n && inps.w) ? `몰랄농도 = ${(inps.n / inps.w).toFixed(3)} m` : 'n과 용매 질량을 입력하세요.',
        inputs: [{ id: 'n', label: '용질 몰수 (mol)' }, { id: 'w', label: '용매 질량 (kg)' }]
      },
      {
        id: 'ch1_ph', grade: 2, subject: '화학Ⅰ', name: '수소 이온 농도 지수 (pH)',
        mathHtml: 'pH = -log<sub>10</sub>[H<sup>+</sup>], &nbsp; pH + pOH = 14',
        desc: '수용액 속의 수소 이온 농도 [H+]를 로그 수치로 나타낸 산성도 지수입니다.',
        vars: [{ symbol: 'pH', name: '수소이온농도지수', unit: '-' }, { symbol: '[H+]', name: '수소 이온 농도', unit: 'M' }],
        calc: (inps) => (inps.h) ? `pH = ${(-Math.log10(inps.h)).toFixed(2)}` : '[H+] 농도를 입력하세요.',
        inputs: [{ id: 'h', label: '수소이온농도 [H+] (M)' }]
      },
      {
        id: 'ch1_neutral', grade: 2, subject: '화학Ⅰ', name: '산-염기 중화 적정',
        mathHtml: 'n · M · V = n\' · M\' · V\'',
        desc: '산이 내놓은 H+ 몰수와 염기가 내놓은 OH- 몰수가 완전히 일치하는 완전 중화 상태 관계식입니다.',
        vars: [{ symbol: 'n', name: '산의 가수', unit: '-' }, { symbol: 'M', name: '산의 몰농도', unit: 'M' }, { symbol: 'V', name: '산의 부피', unit: 'mL' }],
        calc: (inps) => '가수 및 몰농도 적정 유도식입니다.', inputs: []
      },
      {
        id: 'ch1_heat', grade: 2, subject: '화학Ⅰ', name: '반응 열량 측정',
        mathHtml: 'Q = c · m · ΔT',
        desc: '물체의 비열(c)과 질량(m), 온도 변화량(ΔT)을 곱하여 물질이 방출/흡수한 열량을 구합니다.',
        vars: [{ symbol: 'Q', name: '열량', unit: 'J' }, { symbol: 'c', name: '비열', unit: 'J/(g·°C)' }, { symbol: 'm', name: '질량', unit: 'g' }, { symbol: 'ΔT', name: '온도 변화', unit: '°C' }],
        calc: (inps) => (inps.c && inps.m && inps.dt) ? `열량 Q = ${(inps.c * inps.m * inps.dt).toFixed(2)} J` : '비열, 질량, ΔT를 입력하세요.',
        inputs: [{ id: 'c', label: '비열 c' }, { id: 'm', label: '질량 m (g)' }, { id: 'dt', label: '온도변화 ΔT (°C)' }]
      },

      // ---------------- 생명과학Ⅰ (고2) ----------------
      {
        id: 'bio1_hw', grade: 2, subject: '생명과학Ⅰ', name: '하디-바인베르크 동형/이형접합자 빈도',
        mathHtml: 'p + q = 1, &nbsp; p<sup>2</sup> + 2pq + q<sup>2</sup> = 1',
        desc: '진화가 일어나지 않는 이상적 멘델 집단에서 유전자형 빈도 상호 관계식입니다.',
        vars: [{ symbol: 'p', name: '우성 대립유전자 빈도', unit: '-' }, { symbol: 'q', name: '열성 대립유전자 빈도', unit: '-' }],
        calc: (inps) => {
          const p = parseFloat(inps.p);
          if(p>=0 && p<=1) { let q=1-p; return `AA: ${(p*p).toFixed(3)}, Aa: ${(2*p*q).toFixed(3)}, aa: ${(q*q).toFixed(3)}`; }
          return '0~1 사이의 p를 입력하세요.';
        },
        inputs: [{ id: 'p', label: '우성 유전자 빈도 p (0~1)' }]
      },
      {
        id: 'bio1_speed', grade: 2, subject: '생명과학Ⅰ', name: '신경 자극 전도 속도',
        mathHtml: 'v = <div class="frac"><span>전도 거리 (d)</span><span class="bottom">경과 시간 (t)</span></div>',
        desc: '축삭 돌기를 따라 활동 전위가 이동하는 빠르기를 계산합니다.',
        vars: [{ symbol: 'v', name: '전도 속도', unit: 'cm/ms' }, { symbol: 'd', name: '거리', unit: 'cm' }, { symbol: 't', name: '시간', unit: 'ms' }],
        calc: (inps) => (inps.d && inps.t) ? `속도 = ${(inps.d / inps.t).toFixed(2)} cm/ms` : 'd와 t를 입력하세요.',
        inputs: [{ id: 'd', label: '거리 d (cm)' }, { id: 't', label: '시간 t (ms)' }]
      },

      // ---------------- 지구과학Ⅰ (고2) ----------------
      {
        id: 'ea1_stefan', grade: 2, subject: '지구과학Ⅰ', name: '슈테판-볼츠만 법칙',
        mathHtml: 'E = σ · T<sup>4</sup>',
        desc: '흑체가 단위 면적당 단위 시간에 방출하는 방사 에너지의 총량 E는 절대온도 T의 4제곱에 비례합니다.',
        vars: [{ symbol: 'E', name: '방출 에너지', unit: 'W/m²' }, { symbol: 'T', name: '절대 온도', unit: 'K' }, { symbol: 'σ', name: '슈테판-볼츠만 상수', unit: '-' }],
        calc: (inps) => (inps.t) ? `상대 방출량 ∝ ${(Math.pow(inps.t,4)).toExponential(2)}` : '절대온도 T를 입력하세요.',
        inputs: [{ id: 't', label: '절대온도 T (K)' }]
      },
      {
        id: 'ea1_wien', grade: 2, subject: '지구과학Ⅰ', name: '빈의 변위 법칙',
        mathHtml: 'λ<sub>max</sub> = <div class="frac"><span>A</span><span class="bottom">T</span></div>',
        desc: '흑체가 최대 복사 에너지를 방출하는 파장 λmax는 표면 절대온도 T에 반비례합니다.',
        vars: [{ symbol: 'λmax', name: '최대 에너지를 내는 파장', unit: 'nm' }, { symbol: 'T', name: '표면 온도', unit: 'K' }],
        calc: (inps) => (inps.t) ? `최대 파장 λmax ≈ ${(2.898e6 / inps.t).toFixed(1)} nm` : '표면온도 T를 입력하세요.',
        inputs: [{ id: 't', label: '표면온도 T (K)' }]
      },
      {
        id: 'ea1_doppler', grade: 2, subject: '지구과학Ⅰ', name: '빛의 도플러 효과 (시선 속도)',
        mathHtml: 'v = c · <div class="frac"><span>Δλ</span><span class="bottom">λ<sub>0</sub></span></div>',
        desc: '천체의 접근 또는 후퇴 운동으로 인한 관측 파장 변화량(Δλ)으로 시선 속도를 구합니다.',
        vars: [{ symbol: 'v', name: '시선 속도', unit: 'km/s' }, { symbol: 'c', name: '빛의 속도', unit: '300,000 km/s' }, { symbol: 'Δλ', name: '파장 변화량', unit: 'nm' }, { symbol: 'λ₀', name: '고유 파장', unit: 'nm' }],
        calc: (inps) => (inps.dlam && inps.lam0) ? `시선속도 v = ${(300000 * (inps.dlam / inps.lam0)).toFixed(1)} km/s` : 'Δλ와 λ₀를 입력하세요.',
        inputs: [{ id: 'dlam', label: '파장변화 Δλ (nm)' }, { id: 'lam0', label: '고유파장 λ₀ (nm)' }]
      },
      {
        id: 'ea1_hubble', grade: 2, subject: '지구과학Ⅰ', name: '허블의 법칙',
        mathHtml: 'v = H<sub>0</sub> · d',
        desc: '외부 은하의 후퇴 속도 v는 은하까지의 거리 d에 비례함을 설명하는 법칙입니다.',
        vars: [{ symbol: 'v', name: '후퇴 속도', unit: 'km/s' }, { symbol: 'H0', name: '허블 상수', unit: 'km/s/Mpc' }, { symbol: 'd', name: '거리', unit: 'Mpc' }],
        calc: (inps) => (inps.d) ? `후퇴 속도 v = ${(70 * inps.d).toFixed(1)} km/s` : '거리 d를 입력하세요.',
        inputs: [{ id: 'd', label: '거리 d (Mpc)' }]
      },

      // ---------------- 물리학Ⅱ (고3) ----------------
      {
        id: 'phy2_pendulum', grade: 3, subject: '물리학Ⅱ', name: '단진자 주기 공식',
        mathHtml: 'T = 2π <div class="frac"><span>√L</span><span class="bottom">√g</span></div>',
        desc: '줄의 길이가 L인 단진자의 소진폭 진동 주기 T입니다.',
        vars: [{ symbol: 'T', name: '주기', unit: 's' }, { symbol: 'L', name: '진자 실의 길이', unit: 'm' }, { symbol: 'g', name: '중력가속도', unit: '9.8 m/s²' }],
        calc: (inps) => (inps.l) ? `주기 T ≈ ${(2 * Math.PI * Math.sqrt(inps.l / 9.8)).toFixed(2)} s` : '길이 L을 입력하세요.',
        inputs: [{ id: 'l', label: '실의 길이 L (m)' }]
      },
      {
        id: 'phy2_grav', grade: 3, subject: '물리학Ⅱ', name: '만유인력 법칙',
        mathHtml: 'F = G · <div class="frac"><span>m<sub>1</sub> · m<sub>2</sub></span><span class="bottom">r<sup>2</sup></span></div>',
        desc: '질량을 가진 두 물체 사이에 작용하는 중력의 크기식입니다.',
        vars: [{ symbol: 'F', name: '만유인력', unit: 'N' }, { symbol: 'G', name: '만유인력 상수', unit: 'N·m²/kg²' }, { symbol: 'r', name: '두 물체 거리', unit: 'm' }],
        calc: (inps) => (inps.m1 && inps.m2 && inps.r) ? `만유인력 F = ${(6.674e-11 * inps.m1 * inps.m2 / Math.pow(inps.r, 2)).toExponential(2)} N` : 'm1, m2, r를 입력하세요.',
        inputs: [{ id: 'm1', label: '질량 m1 (kg)' }, { id: 'm2', label: '질량 m2 (kg)' }, { id: 'r', label: '거리 r (m)' }]
      },
      {
        id: 'phy2_coulomb', grade: 3, subject: '물리학Ⅱ', name: '쿨롱의 법칙 (전기력)',
        mathHtml: 'F = k · <div class="frac"><span>|q<sub>1</sub> · q<sub>2</sub>|</span><span class="bottom">r<sup>2</sup></span></div>',
        desc: '전하를 띤 두 입자 사이에 작용하는 정전기력의 크기입니다.',
        vars: [{ symbol: 'F', name: '전기력', unit: 'N' }, { symbol: 'k', name: '쿨롱 상수', unit: '8.99×10⁹ N·m²/C²' }, { symbol: 'q', name: '전하량', unit: 'C' }],
        calc: (inps) => (inps.q1 && inps.q2 && inps.r) ? `전기력 F = ${(8.99e9 * inps.q1 * inps.q2 / Math.pow(inps.r, 2)).toExponential(2)} N` : 'q1, q2, r을 입력하세요.',
        inputs: [{ id: 'q1', label: '전하량 q1 (C)' }, { id: 'q2', label: '전하량 q2 (C)' }, { id: 'r', label: '거리 r (m)' }]
      },
      {
        id: 'phy2_faraday', grade: 3, subject: '물리학Ⅱ', name: '패러데이 전자기 유도 법칙',
        mathHtml: 'V = -N · <div class="frac"><span>ΔΦ</span><span class="bottom">Δt</span></div>',
        desc: '코일을 통과하는 자기선속의 변화율에 비례하여 유도 기전력이 발생합니다.',
        vars: [{ symbol: 'V', name: '유도 기전력', unit: 'V' }, { symbol: 'N', name: '코일 감은 수', unit: '-' }, { symbol: 'ΔΦ', name: '자기선속 변화량', unit: 'Wb' }],
        calc: (inps) => (inps.n && inps.dphi && inps.dt) ? `유도 기전력 V = ${(-inps.n * (inps.dphi / inps.dt)).toFixed(2)} V` : 'N, ΔΦ, Δt를 입력하세요.',
        inputs: [{ id: 'n', label: '감은수 N' }, { id: 'dphi', label: '자기선속 변화 ΔΦ' }, { id: 'dt', label: '시간 Δt' }]
      },

      // ---------------- 화학Ⅱ (고3) ----------------
      {
        id: 'ch2_vrms', grade: 3, subject: '화학Ⅱ', name: '기체 분자의 제곱평균제곱근 속도 (v_rms)',
        mathHtml: 'v<sub>rms</sub> = <div class="frac"><span>√3RT</span><span class="bottom">√M</span></div>',
        desc: '기체 분자 운동론에서 이상기체 분자들의 평균 이동 속도입니다.',
        vars: [{ symbol: 'v_rms', name: '평균 분자 속도', unit: 'm/s' }, { symbol: 'R', name: '기체상수', unit: '8.314 J/(mol·K)' }, { symbol: 'T', name: '절대온도', unit: 'K' }, { symbol: 'M', name: '몰질량', unit: 'kg/mol' }],
        calc: (inps) => (inps.t && inps.m) ? `평균 속도 v_rms ≈ ${Math.sqrt((3 * 8.314 * inps.t) / (inps.m / 1000)).toFixed(1)} m/s` : '온도 T와 분자량 M을 입력하세요.',
        inputs: [{ id: 't', label: '절대온도 T (K)' }, { id: 'm', label: '분자량 M (g/mol)' }]
      },
      {
        id: 'ch2_osmotic', grade: 3, subject: '화학Ⅱ', name: '반트호프 삼투압 공식',
        mathHtml: 'Π = M · R · T',
        desc: '묽은 용액의 삼투압(Π)은 용액의 몰농도(M)와 절대온도(T)에 비례합니다.',
        vars: [{ symbol: 'Π', name: '삼투압', unit: 'atm' }, { symbol: 'M', name: '몰농도', unit: 'M' }, { symbol: 'R', name: '기체상수', unit: '0.0821 atm·L/(mol·K)' }, { symbol: 'T', name: '절대온도', unit: 'K' }],
        calc: (inps) => (inps.m && inps.t) ? `삼투압 Π = ${(inps.m * 0.0821 * inps.t).toFixed(2)} atm` : '몰농도 M과 온도 T를 입력하세요.',
        inputs: [{ id: 'm', label: '몰농도 M' }, { id: 't', label: '절대온도 T (K)' }]
      },
      {
        id: 'ch2_half', grade: 3, subject: '화학Ⅱ', name: '1차 반응의 반감기',
        mathHtml: 't<sub>1/2</sub> = <div class="frac"><span>ln 2</span><span class="bottom">k</span></div> ≈ <div class="frac"><span>0.693</span><span class="bottom">k</span></div>',
        desc: '1차 반응의 반감기는 반응물의 초기 농도와 상관없이 속도 상수 k에만 의존합니다.',
        vars: [{ symbol: 't1/2', name: '반감기', unit: 's' }, { symbol: 'k', name: '반응 속도 상수', unit: '1/s' }],
        calc: (inps) => (inps.k) ? `반감기 t1/2 = ${(0.693 / inps.k).toFixed(2)} s` : '속도상수 k를 입력하세요.',
        inputs: [{ id: 'k', label: '속도상수 k (1/s)' }]
      },

      // ---------------- 생명과학Ⅱ (고3) ----------------
      {
        id: 'bio2_menten', grade: 3, subject: '생명과학Ⅱ', name: '미카엘리스-멘텐 효소 속도식',
        mathHtml: 'v = <div class="frac"><span>V<sub>max</sub> · [S]</span><span class="bottom">K<sub>m</sub> + [S]</span></div>',
        desc: '기질 농도 [S] 변화에 따른 효소 촉매 반응 속도 v를 나타내는 공식입니다.',
        vars: [{ symbol: 'v', name: '반응 속도', unit: 'μmol/min' }, { symbol: 'Vmax', name: '최대 속도', unit: 'μmol/min' }, { symbol: 'Km', name: '미카엘리스 상수', unit: 'mM' }, { symbol: '[S]', name: '기질 농도', unit: 'mM' }],
        calc: (inps) => (inps.vmax && inps.km && inps.s) ? `반응 속도 v = ${((inps.vmax * inps.s)/(inps.km + inps.s)).toFixed(2)}` : 'Vmax, Km, [S]를 입력하세요.',
        inputs: [{ id: 'vmax', label: 'Vmax' }, { id: 'km', label: 'Km' }, { id: 's', label: '기질농도 [S]' }]
      },
      {
        id: 'bio2_gibbs', grade: 3, subject: '생명과학Ⅱ', name: '깁스 자유 에너지 변화량',
        mathHtml: 'ΔG = ΔH - T · ΔS',
        desc: '생체 화학 반응의 자발성 여부를 결정하는 깁스 자유 에너지 변화 관계식입니다.',
        vars: [{ symbol: 'ΔG', name: '자유 에너지 변화량', unit: 'kJ/mol' }, { symbol: 'ΔH', name: '엔탈피 변화량', unit: 'kJ/mol' }, { symbol: 'T', name: '절대온도', unit: 'K' }, { symbol: 'ΔS', name: '엔트로피 변화량', unit: 'kJ/(mol·K)' }],
        calc: (inps) => (inps.dh && inps.t && inps.ds) ? `ΔG = ${(inps.dh - inps.t * inps.ds).toFixed(2)} kJ/mol` : 'ΔH, T, ΔS를 입력하세요.',
        inputs: [{ id: 'dh', label: '엔탈피 ΔH' }, { id: 't', label: '온도 T (K)' }, { id: 'ds', label: '엔트로피 ΔS' }]
      },

      // ---------------- 지구과학Ⅱ (고3) ----------------
      {
        id: 'ea2_geo', grade: 3, subject: '지구과학Ⅱ', name: '지균풍 풍속 공식',
        mathHtml: 'v<sub>g</sub> = <div class="frac"><span>1</span><span class="bottom">2Ω sinφ</span></div> · <div class="frac"><span>1</span><span class="bottom">ρ</span></div> · <div class="frac"><span>ΔP</span><span class="bottom">Δn</span></div>',
        desc: '기압경도력과 전향력이 등가 평형을 이루어 등압선에 평행하게 부는 바람의 속도입니다.',
        vars: [{ symbol: 'vg', name: '지균풍 속도', unit: 'm/s' }, { symbol: 'Ω', name: '지구자전 각속도', unit: 'rad/s' }, { symbol: 'φ', name: '위도', unit: '°' }, { symbol: 'ρ', name: '공기밀도', unit: 'kg/m³' }],
        calc: (inps) => '지균풍 수식 모델입니다.', inputs: []
      }
    ];

    let currentStep = 1;
    let selectedGrade = null;
    let selectedSubject = null;
    let currentFormula = null;

    function updateStep(step) {
      currentStep = step;
      document.querySelectorAll('.step-section').forEach(el => el.classList.remove('active'));
      const backBtn = document.getElementById('backBtn');

      if (step === 1) {
        document.getElementById('stepGrade').classList.add('active');
        backBtn.classList.remove('visible');
      } else if (step === 2) {
        document.getElementById('stepSubject').classList.add('active');
        backBtn.classList.add('visible');
      } else if (step === 3) {
        document.getElementById('stepFormulaList').classList.add('active');
        backBtn.classList.add('visible');
      }
    }

    function goBack() {
      if (currentStep === 3) updateStep(2);
      else if (currentStep === 2) updateStep(1);
    }

    function selectGrade(grade) {
      selectedGrade = grade;
      const subjectsMap = {
        1: ['통합과학'],
        2: ['물리학Ⅰ', '화학Ⅰ', '생명과학Ⅰ', '지구과학Ⅰ'],
        3: ['물리학Ⅱ', '화학Ⅱ', '생명과학Ⅱ', '지구과학Ⅱ']
      };

      const grid = document.getElementById('subjectGrid');
      grid.innerHTML = '';
      document.getElementById('subjectTitle').innerText = `고등학교 ${grade}학년 과목 선택`;

      subjectsMap[grade].forEach(sub => {
        const card = document.createElement('div');
        card.className = 'select-card';
        card.onclick = () => selectSubject(sub);
        card.innerHTML = `
          <div class="icon">📚</div>
          <div class="title">${sub}</div>
          <div class="desc">${grade}학년 과정 교과 수식 공식 모음</div>
        `;
        grid.appendChild(card);
      });

      updateStep(2);
    }

    function selectSubject(subject) {
      selectedSubject = subject;
      document.getElementById('formulaListTitle').innerText = `${subject} 공식 목록`;
      document.getElementById('searchInput').value = '';
      renderFormulas();
      updateStep(3);
    }

    function renderFormulas() {
      const grid = document.getElementById('formulaGrid');
      grid.innerHTML = '';
      const query = document.getElementById('searchInput').value.trim().toLowerCase();

      const filtered = database.filter(item => {
        const isMatchSubject = item.grade === selectedGrade && item.subject === selectedSubject;
        if (!isMatchSubject) return false;
        if (!query) return true;

        const matchName = item.name.toLowerCase().includes(query);
        const matchDesc = item.desc.toLowerCase().includes(query);
        const matchVars = item.vars.some(v => 
          v.symbol.toLowerCase().includes(query) || 
          v.name.toLowerCase().includes(query)
        );

        return matchName || matchDesc || matchVars;
      });

      if(filtered.length === 0) {
        grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:40px; color:#888;">일치하는 공식이 없습니다. 다른 미지수나 명칭을 입력해 보세요.</div>';
        return;
      }

      filtered.forEach(item => {
        const varSymbolsStr = item.vars.map(v => v.symbol).join(', ');
        const card = document.createElement('div');
        card.className = 'formula-btn-card';
        card.onclick = () => openModal(item);
        card.innerHTML = `
          <div class="f-name">${item.name}</div>
          <div class="f-unit">${item.subject}</div>
          <div class="f-preview">${item.mathHtml}</div>
          <div class="f-vars-list">📌 미지수: <b>${varSymbolsStr}</b></div>
        `;
        grid.appendChild(card);
      });
    }

    function filterFormulas() {
      renderFormulas();
    }

    function openModal(item) {
      currentFormula = item;
      document.getElementById('modalTitle').innerText = item.name;
      document.getElementById('modalCategory').innerText = `${item.subject} · 고등학교 ${item.grade}학년`;
      document.getElementById('modalMath').innerHTML = item.mathHtml;
      document.getElementById('modalDesc').innerText = item.desc;

      const varTable = document.getElementById('modalVarTable');
      varTable.innerHTML = '';
      item.vars.forEach(v => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td><b>${v.symbol}</b></td><td>${v.name}</td><td>${v.unit}</td>`;
        varTable.appendChild(tr);
      });

      const calcInputs = document.getElementById('calcInputs');
      calcInputs.innerHTML = '';
      item.inputs.forEach(inp => {
        const div = document.createElement('div');
        div.className = 'input-group';
        div.innerHTML = `<label>${inp.label}</label><input type="number" id="input_${inp.id}" placeholder="값 입력" oninput="runCalculation()">`;
        calcInputs.appendChild(div);
      });

      document.getElementById('calcResult').innerText = '알려진 미지수 값을 입력해 보세요.';
      
      const chartSec = document.getElementById('chartSection');
      if (item.hasChart) {
        chartSec.style.display = 'block';
        setTimeout(() => runCalculation(), 50);
      } else {
        chartSec.style.display = 'none';
      }

      document.getElementById('formulaModal').classList.add('active');
    }

    function closeModal() {
      document.getElementById('formulaModal').classList.remove('active');
    }

    function runCalculation() {
      if (!currentFormula) return;
      const inputVals = {};
      currentFormula.inputs.forEach(inp => {
        const el = document.getElementById(`input_${inp.id}`);
        const val = el ? el.value : '';
        inputVals[inp.id] = val !== '' ? parseFloat(val) : null;
      });

      const res = currentFormula.calc(inputVals);
      document.getElementById('calcResult').innerText = res;

      if (currentFormula.hasChart && currentFormula.drawChart) {
        const canvas = document.getElementById('formulaCanvas');
        const ctx = canvas.getContext('2d');
        currentFormula.drawChart(ctx, inputVals);
      }
    }
  </script>
</body>
</html>
