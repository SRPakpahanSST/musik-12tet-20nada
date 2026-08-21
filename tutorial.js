// ================================================================
// TUTORIAL PMD Musik 12 TET
// ================================================================

const tutorialData = [
    {
        title: "🎵 Selamat Datang di PMD Musik 12 TET!",
        content: `
            <p>Aplikasi ini adalah eksplorasi musik sistem <b>12-TET dengan 20 nada per oktaf</b>, 
            berdasarkan karya tulis Sukma Riadi Pakpahan, SST.</p>
            <p>Tutorial ini akan memandu Anda melalui semua fitur yang tersedia.</p>
            <p><b>Mulai dengan mengklik tombol "Mulai" di layar pembuka.</b></p>
        `
    },
    {
        title: "🎹 Keyboard — Mode Nada Tunggal",
        content: `
            <p>Di tab <b>Keyboard</b>, Anda dapat memainkan nada dengan mengklik tuts.</p>
            <ul>
                <li><b>Nada Tunggal:</b> Setiap tuts membunyikan satu nada. Nada yang Anda mainkan akan <b>direkam</b> secara otomatis.</li>
                <li>Pilih <b>oktaf</b> (3, 4, atau 5) dan <b>instrumen</b> (8 pilihan).</li>
                <li>Atur <b>Reverb</b>, <b>Delay</b>, dan <b>Amplifier</b> untuk efek suara.</li>
            </ul>
            <p><b>💡 Tombol "Mayor" dan "Minor" akan memutar ulang melodi yang telah Anda rekam!</b></p>
        `
    },
    {
        title: "🎹 Keyboard — Mode Akord",
        content: `
            <p>Pilih mode <b>Akord</b> untuk memainkan akord triad.</p>
            <ul>
                <li><b>Rentang akord:</b> C2 – B#3 (20 nada).</li>
                <li><b>Tuts putih</b> = akord <b>Mayor</b>, <b>tuts hitam</b> = akord <b>Minor</b>.</li>
                <li>Akord akan <b>sustain</b> (terus berbunyi) hingga Anda menekan akord lain atau menekan tombol Stop/Reset.</li>
                <li>Akord selalu menggunakan suara <b>Piano</b> (statis) untuk iringan yang stabil.</li>
            </ul>
            <p><b>💡 Nada tunggal di luar rentang dapat dimainkan sebagai melodi tanpa menghentikan akord.</b></p>
        `
    },
    {
        title: "🎵 AI Composer",
        content: `
            <p>Tab ini memungkinkan Anda menciptakan melodi otomatis.</p>
            <ul>
                <li><b>Mode Deskripsi:</b> Tulis deskripsi (misal: "melodi romantis yang perlahan"), pilih mood & skala, lalu klik <b>Generate</b>.</li>
                <li><b>Mode Prompt AI:</b> Masukkan <b>OpenAI API Key</b> dan prompt spesifik. AI GPT-3.5 akan menghasilkan notasi nada.</li>
                <li>Hasil melodi dapat diputar, dihentikan, atau dihapus.</li>
            </ul>
        `
    },
    {
        title: "🎤 AI Transcriber",
        content: `
            <p>Rekam audio dari mikrofon dan transkripsi menjadi notasi 20 nada per oktaf.</p>
            <ul>
                <li>Klik tombol 🎤 untuk mulai merekam (maks. 22 menit).</li>
                <li>Pilih algoritma: <b>Standar</b> (autokorelasi) atau <b>Improved (YIN)</b> (lebih akurat).</li>
                <li>Atur <b>Mode</b> (Vokal, Instrumental, Full Range) dan <b>Sensitivitas</b>.</li>
                <li>Setelah rekaman selesai, klik <b>AI Transcribe</b> untuk melihat hasil.</li>
                <li>Hasil transkripsi dapat diputar ulang dengan tombol <b>Play Hasil</b>.</li>
            </ul>
        `
    },
    {
        title: "🎶 Chord Progression Generator",
        content: `
            <p>Analisis progresi akord dari hasil transkripsi.</p>
            <ul>
                <li>Masukkan urutan nada (misal: <code>E3 → G3 → H3 → E4 → G4 → H4</code>) ke dalam kotak input.</li>
                <li>Pilih mode analisis: <b>Otomatis</b>, <b>Mayor</b>, atau <b>Minor</b>.</li>
                <li>Pilih jumlah akord yang ditampilkan (4, 6, atau 8).</li>
                <li>Klik <b>Generate Progresi</b> untuk melihat akord-akord yang terbentuk beserta notasi Romawi.</li>
            </ul>
        `
    },
    {
        title: "📖 Informasi & Referensi",
        content: `
            <p>Panel <b>Informasi & Referensi</b> di bagian bawah menyediakan:</p>
            <ul>
                <li><b>Teori</b>: dasar sistem 12-TET 20 nada per oktaf.</li>
                <li><b>Frekuensi</b>: tabel frekuensi nada di oktaf 4.</li>
                <li><b>Skala</b>: mayor dan minor dengan interval.</li>
                <li><b>Akord</b>: referensi pembentukan akord.</li>
                <li><b>Tentang</b>: informasi aplikasi dan penulis.</li>
            </ul>
            <p>Gunakan tab-tab ini untuk memahami teori di balik sistem musik baru ini.</p>
        `
    },
    {
        title: "🎯 Selesai!",
        content: `
            <p>Anda sekarang siap menjelajahi <b>PMD Musik 12 TET</b>!</p>
            <p>Semoga aplikasi ini menginspirasi eksplorasi musik mikrotonal Anda.</p>
            <p><b>Selamat berkarya! 🎵</b></p>
        `
    }
];

let currentStep = 0;
let tutorialOverlay = null;
let tutorialContainer = null;

function createTutorialOverlay() {
    // Buat overlay jika belum ada
    if (document.getElementById('tutorialOverlay')) return;

    const overlay = document.createElement('div');
    overlay.id = 'tutorialOverlay';
    overlay.style.cssText = `
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0,0,0,0.75);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10000;
        backdrop-filter: blur(4px);
        padding: 20px;
        animation: fadeIn 0.3s ease;
    `;

    const container = document.createElement('div');
    container.style.cssText = `
        background: #16213e;
        border-radius: 20px;
        max-width: 650px;
        width: 100%;
        padding: 30px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.8);
        border: 1px solid #2a3a5e;
        max-height: 80vh;
        overflow-y: auto;
        color: #eee;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        position: relative;
    `;

    container.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <h2 id="tutorialTitle" style="color:#f5a623; margin:0; font-size:1.4rem;">🎵 Tutorial</h2>
            <button id="tutorialCloseBtn" style="background:none; border:none; color:#aaa; font-size:1.8rem; cursor:pointer; transition:0.2s;">&times;</button>
        </div>
        <div id="tutorialContent" style="line-height:1.7; font-size:0.95rem; min-height:200px;">
            ${tutorialData[0].content}
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; gap:10px; flex-wrap:wrap;">
            <div>
                <span id="tutorialStepIndicator" style="color:#888; font-size:0.8rem;">Langkah 1 dari ${tutorialData.length}</span>
            </div>
            <div style="display:flex; gap:8px;">
                <button id="tutorialPrevBtn" style="padding:8px 18px; background:#0f3460; border:none; border-radius:20px; color:#fff; cursor:pointer; font-size:0.8rem;">← Sebelumnya</button>
                <button id="tutorialNextBtn" style="padding:8px 18px; background:#e94560; border:none; border-radius:20px; color:#fff; cursor:pointer; font-size:0.8rem;">Selanjutnya →</button>
                <button id="tutorialDoneBtn" style="padding:8px 18px; background:#2d7d46; border:none; border-radius:20px; color:#fff; cursor:pointer; font-size:0.8rem; display:none;">Selesai</button>
            </div>
        </div>
        <div style="margin-top:12px; display:flex; gap:6px; justify-content:center;">
            ${tutorialData.map((_, i) => `<span id="tutorialDot${i}" style="width:10px; height:10px; border-radius:50%; background:${i===0 ? '#e94560' : '#2a3a5e'}; display:inline-block; transition:0.3s;"></span>`).join('')}
        </div>
    `;

    overlay.appendChild(container);
    document.body.appendChild(overlay);

    tutorialOverlay = overlay;
    tutorialContainer = container;

    // Event listeners
    document.getElementById('tutorialCloseBtn').addEventListener('click', closeTutorial);
    document.getElementById('tutorialPrevBtn').addEventListener('click', () => navigateTutorial(-1));
    document.getElementById('tutorialNextBtn').addEventListener('click', () => navigateTutorial(1));
    document.getElementById('tutorialDoneBtn').addEventListener('click', closeTutorial);

    // Keyboard shortcut: Escape
    document.addEventListener('keydown', handleEscape);

    updateTutorialStep();
}

function updateTutorialStep() {
    const data = tutorialData[currentStep];
    document.getElementById('tutorialTitle').textContent = data.title;
    document.getElementById('tutorialContent').innerHTML = data.content;
    document.getElementById('tutorialStepIndicator').textContent = `Langkah ${currentStep+1} dari ${tutorialData.length}`;

    // Update tombol navigasi
    document.getElementById('tutorialPrevBtn').style.display = currentStep === 0 ? 'none' : 'inline-block';
    document.getElementById('tutorialNextBtn').style.display = currentStep === tutorialData.length - 1 ? 'none' : 'inline-block';
    document.getElementById('tutorialDoneBtn').style.display = currentStep === tutorialData.length - 1 ? 'inline-block' : 'none';

    // Update dots
    tutorialData.forEach((_, i) => {
        const dot = document.getElementById(`tutorialDot${i}`);
        if (dot) {
            dot.style.background = i === currentStep ? '#e94560' : '#2a3a5e';
        }
    });
}

function navigateTutorial(delta) {
    const newStep = currentStep + delta;
    if (newStep < 0 || newStep >= tutorialData.length) return;
    currentStep = newStep;
    updateTutorialStep();
}

function closeTutorial() {
    if (tutorialOverlay) {
        tutorialOverlay.remove();
        tutorialOverlay = null;
        tutorialContainer = null;
        document.removeEventListener('keydown', handleEscape);
    }
}

function handleEscape(e) {
    if (e.key === 'Escape') {
        closeTutorial();
    }
}

// Fungsi untuk memulai tutorial (dipanggil dari tombol)
function startTutorial() {
    currentStep = 0;
    createTutorialOverlay();
}

// Ekspos fungsi ke global
window.startTutorial = startTutorial;

console.log('🎯 Tutorial PMD Musik 12 TET siap digunakan!');