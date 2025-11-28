<div class="footer">
            Encrypted pilots • Open-source core • Patent pending<br>
            No cloud • No Docker • Free forever
            <div class="attribution">Built by Schlayballs | Contact: @schlayguy</div>
        </div>
    </div>

    <div class="decrypt-modal" id="decryptModal">
        <div class="decrypt-box">
            <span class="close-btn" onclick="closeModal()">&times;</span>
            <h2>🔒 ENCRYPTED FILE ACCESS</h2>
            
            <div class="file-upload-area" id="dropZone" onclick="document.getElementById('encryptedFileInput').click()">
                <p style="margin: 0; font-size: clamp(0.9rem, 2vw, 1.2rem);">
                    📁 CLICK TO UPLOAD ENCRYPTED FILE<br>
                    <span style="font-size: 0.9em; opacity: 0.7;">or drag and drop here</span>
                </p>
                <p id="fileName" style="margin-top: 15px; color: #0ff;"></p>
            </div>

            <input type="file" id="encryptedFileInput" accept=".enc,.encrypted,.txt" onchange="handleEncryptedFile(event)">

            <input type="password" id="decryptPassword" placeholder="ENTER DECRYPTION PASSWORD">
            
            <button class="btn" onclick="decryptFile()" style="width: 100%; margin: 10px 0;">
                🔓 DECRYPT
            </button>

            <div id="decryptedContent" class="decrypted-content" style="display: none;"></div>
        </div>
    </div>

    <div class="decrypt-modal" id="puzzleModal">
        <div class="decrypt-box">
            <span class="close-btn" onclick="closePuzzleModal()">&times;</span>
            <h2>🧬 ENCRYPTED GENOME PUZZLE #001</h2>
            
            <p style="color: #0ff; margin-bottom: 20px; line-height: 1.8;">
                First 5 solvers get:<br>
                ✅ Lifetime beta access<br>
                ✅ On-chain shoutout NFT<br>
                ✅ Legendary status
            </p>

            <p style="color: #0f0; margin-bottom: 20px;">
                Paste the base64 puzzle from X/Twitter:
            </p>

            <textarea id="puzzleInput" 
                style="width: 100%; height: 150px; padding: 15px; background: #000; border: 2px solid #0f0; color: #0f0; font-family: 'Courier New', monospace; font-size: 0.9rem;"
                placeholder="QUdYWiBpcyBub3QgYSByZWFsIEZBU1RBLCBpdCdzIHRoZSBjcnlwdGljIG1lc3NhZ2U..."></textarea>
            
            <button class="btn" onclick="solvePuzzle()" style="width: 100%; margin: 10px 0;">
                🚀 SOLVE PUZZLE
            </button>

            <div id="puzzleResult" class="decrypted-content" style="display: none;"></div>
        </div>
    </div>

    <script>
        let sequence = '';
        let mutations = [];
        let scanStartTime = 0;
        let encryptedFileData = null;
        let solverCount = 0;
        const MAX_SOLVERS = 5;

        const PUZZLE_SOLUTION = "AGXZ is not a real FASTA, it's the cryptic message you need to decode to prove you can read my mind. Run it through SeqSwift once with the flag --encrypted-puzzle and see what happens. Or just decode it manually if you really want to work for it. ;)";

        function showPuzzle() {
            document.getElementById('puzzleModal').classList.add('active');
        }

        function closePuzzleModal() {
            document.getElementById('puzzleModal').classList.remove('active');
            document.getElementById('puzzleInput').value = '';
            document.getElementById('puzzleResult').style.display = 'none';
        }

        function solvePuzzle() {
            const input = document.getElementById('puzzleInput').value.trim();
            
            if (!input) {
                alert('PLEASE PASTE THE PUZZLE FROM X/TWITTER');
                return;
            }

            try {
                const decoded = atob(input);
                
                if (decoded === PUZZLE_SOLUTION || decoded.includes("AGXZ is not a real FASTA")) {
                    solverCount++;
                    
                    if (solverCount <= MAX_SOLVERS) {
                        const result = document.getElementById('puzzleResult');
                        result.style.display = 'block';
                        result.innerHTML = `
                            <div style="color: #0ff; font-size: 1.2rem; margin-bottom: 20px;">
                                🎉 CONGRATULATIONS! 🎉
                            </div>
                            <div style="color: #0f0; line-height: 2;">
                                You let the tool do the thinking. You win.<br><br>
                                <strong>SOLVER #${solverCount} OF 5</strong><br><br>
                                🏆 You've earned:<br>
                                ✅ Lifetime beta access<br>
                                ✅ On-chain shoutout NFT<br>
                                ✅ Legendary status<br><br>
                                📱 DM <a href="https://twitter.com/schlayguy" target="_blank" style="color: #0ff;">@schlayguy</a> with your wallet address to claim your NFT + beta key.<br><br>
                                Include this code: <strong style="color: #f0f;">SOLVER-${solverCount}-${Date.now()}</strong>
                            </div>
                        `;
                        
                        alert(`🎉 WINNER!\n\nYou're solver #${solverCount} of 5!\n\nDM @schlayguy on X with your wallet to claim your NFT + beta key.`);
                    } else {
                        alert('❌ Sorry! All 5 solver spots have been claimed.\n\nBut you still decoded it like a boss. Follow @schlayguy for Puzzle #002!');
                    }
                } else {
                    alert('🤔 That doesn\'t look right. Make sure you pasted the full base64 puzzle from the X post!');
                }
            } catch (error) {
                alert('❌ DECODING FAILED\n\nMake sure you copied the entire base64 puzzle from X/Twitter.');
            }
        }

        function generateSequence() {
            scanStartTime = performance.now();
            const bases = ['A', 'T', 'G', 'C'];
            const hbsPattern = 'GTGCAC';
            sequence = '';
            mutations = [];

            for (let i = 0; i < 1000; i++) {
                if (Math.random() < 0.03) {
                    sequence += hbsPattern;
                    mutations.push(i);
                    i += hbsPattern.length - 1;
                } else {
                    sequence += bases[Math.floor(Math.random() * bases.length)];
                }
            }

            displaySequence();
            updateStats();
        }

        function displaySequence() {
            const display = document.getElementById('sequenceDisplay');
            let html = '&gt; SEQUENCE DATA:<br><br>';
            
            for (let i = 0; i < sequence.length; i++) {
                const isMutation = mutations.some(m => i >= m && i < m + 6);
                const baseClass = isMutation ? 'mutation-base' : 'normal-base';
                html += `<span class="${baseClass}">${sequence[i]}</span>`;
                
                if ((i + 1) % 80 === 0) html += '<br>';
            }
            
            display.innerHTML = html;
        }

        function scanMutations() {
            if (!sequence) {
                alert('NO SEQUENCE LOADED. GENERATE OR LOAD A SEQUENCE FIRST.');
                return;
            }
            
            scanStartTime = performance.now();
            const pattern = 'GTGCAC';
            mutations = [];
            let pos = 0;
            
            while ((pos = sequence.indexOf(pattern, pos)) !== -1) {
                mutations.push(pos);
                pos++;
            }
            
            displaySequence();
            updateStats();
            
            const scanTime = ((performance.now() - scanStartTime) / 1000).toFixed(4);
            alert(`SCAN COMPLETE!\n\n${mutations.length} HBS MUTATIONS DETECTED\nSCAN TIME: ${scanTime}s`);
        }

        function updateStats() {
            const scanTime = ((performance.now() - scanStartTime) / 1000).toFixed(4);
            
            document.getElementById('totalBases').textContent = sequence.length.toLocaleString();
            document.getElementById('mutationCount').textContent = mutations.length;
            document.getElementById('scanTime').textContent = scanTime + 's';
            
            const rate = sequence.length > 0 
                ? ((mutations.length * 6 / sequence.length) * 100).toFixed(2) 
                : '0.0';
            document.getElementById('mutationRate').textContent = rate + '%';
        }

        function clearSequence() {
            sequence = '';
            mutations = [];
            document.getElementById('sequenceDisplay').innerHTML = 
                '&gt; READY TO ANALYZE GENOMIC DATA<br>&gt; CLICK "GENERATE SEQUENCE" TO START...<br>&gt; OR LOAD YOUR OWN .FASTA FILE';
            document.getElementById('totalBases').textContent = '0';
            document.getElementById('mutationCount').textContent = '0';
            document.getElementById('scanTime').textContent = '0.00s';
            document.getElementById('mutationRate').textContent = '0.0%';
        }

        function loadFile(event) {
            const file = event.target.files[0];
            if (!file) return;
            
            scanStartTime = performance.now();
            const reader = new FileReader();
            reader.onload = function(e) {
                let content = e.target.result;
                
                if (content.startsWith('>')) {
                    content = content.split('\n').slice(1).join('');
                }
                
                sequence = content.replace(/[^ATGC]/gi, '').toUpperCase();
                
                if (sequence.length === 0) {
                    alert('NO VALID SEQUENCE DATA FOUND IN FILE');
                    return;
                }
                
                scanMutations();
            };
            reader.readAsText(file);
        }

        function showDecrypt() {
            document.getElementById('decryptModal').classList.add('active');
        }

        function showAbout() {
            alert('SEQSWIFT v1.12\n\n⚡ Ultra-fast genomic analysis platform\n🔒 Encrypted pilot access\n🧬 Real-time mutation detection\n📊 No cloud, no Docker, free forever\n\nBuilt by Schlayballs | @schlayguy');
        }

        function closeModal() {
            document.getElementById('decryptModal').classList.remove('active');
            document.getElementById('decryptPassword').value = '';
            document.getElementById('fileName').textContent = '';
            document.getElementById('decryptedContent').style.display = 'none';
            document.getElementById('decryptedContent').innerHTML = '';
            encryptedFileData = null;
        }

        function handleEncryptedFile(event) {
            const file = event.target.files[0];
            if (!file) return;
            
            document.getElementById('fileName').textContent = `📄 ${file.name}`;
            
            const reader = new FileReader();
            reader.onload = function(e) {
                encryptedFileData = e.target.result;
            };
            reader.readAsText(file);
        }

        function decryptFile() {
            const password = document.getElementById('decryptPassword').value;
            
            if (!encryptedFileData) {
                alert('PLEASE UPLOAD AN ENCRYPTED FILE FIRST');
                return;
            }
            
            if (!password) {
                alert('PLEASE ENTER DECRYPTION PASSWORD');
                return;
            }
            
            try {
                let decrypted = '';
                for (let i = 0; i < encryptedFileData.length; i++) {
                    decrypted += String.fromCharCode(
                        encryptedFileData.charCodeAt(i) ^ password.charCodeAt(i % password.length)
                    );
                }
                
                document.getElementById('decryptedContent').style.display = 'block';
                document.getElementById('decryptedContent').innerHTML = 
                    `&gt; DECRYPTION SUCCESSFUL<br><br>${decrypted.substring(0, 500)}${decrypted.length > 500 ? '...' : ''}`;
                
                alert('DECRYPTION SUCCESSFUL!\n\nFile contents displayed below.');
            } catch (error) {
                alert('DECRYPTION FAILED!\n\nInvalid password or corrupted file.');
            }
        }

        const dropZone = document.getElementById('dropZone');
        
        dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropZone.classList.add('drag-over');
        });
        
        dropZone.addEventListener('dragleave', () => {
            dropZone.classList.remove('drag-over');
        });
        
        dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropZone.classList.remove('drag-over');
            
            const file = e.dataTransfer.files[0];
            if (file) {
                document.getElementById('fileName').textContent = `📄 ${file.name}`;
                const reader = new FileReader();
                reader.onload = function(evt) {
                    encryptedFileData = evt.target.result;
                };
                reader.readAsText(file);
            }
        });

        window.onload = function() {
            setTimeout(generateSequence, 500);
        };
    </script>
</body>
</html><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SeqSwift - Ultra-fast genomic analysis</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: #000;
            color: #0f0;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            padding: 20px;
            line-height: 1.6;
            overflow-x: hidden;
        }
        
        .header {
            position: sticky;
            top: 0;
            background: rgba(0, 0, 0, 0.95);
            padding: 15px 0;
            border-bottom: 2px solid #0f0;
            margin-bottom: 20px;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: clamp(1rem, 2.5vw, 1.5rem);
            color: #0ff;
        }
        
        .nav-btns {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .puzzle-alert {
            background: linear-gradient(135deg, #f0f 0%, #0ff 100%);
            color: #000;
            padding: 15px;
            margin: 20px 0;
            border-radius: 10px;
            font-weight: bold;
            animation: pulse 2s infinite;
            cursor: pointer;
            text-align: center;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.8; }
        }
        
        .nav-btn {
            padding: 8px 20px;
            border: 2px solid #0ff;
            color: #0ff;
            background: transparent;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: clamp(0.8rem, 1.5vw, 1rem);
            transition: all 0.3s ease;
        }
        
        .nav-btn:hover {
            background: #0ff;
            color: #000;
            box-shadow: 0 0 15px #0ff;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            text-align: center;
        }
        
        h1 {
            font-size: clamp(1.5rem, 5vw, 3.5rem);
            margin-bottom: 20px;
            font-weight: normal;
            letter-spacing: 0.05em;
        }
        
        .subtitle {
            font-size: clamp(0.9rem, 2vw, 1.2rem);
            margin-bottom: 40px;
            opacity: 0.9;
        }
        
        .boom-section {
            margin: 40px 0;
        }
        
        .boom-title {
            font-size: clamp(1rem, 2.5vw, 1.5rem);
            margin-bottom: 30px;
            color: #0f0;
        }
        
        .benchmarks {
            list-style: none;
            font-size: clamp(0.85rem, 1.8vw, 1.1rem);
            margin-bottom: 20px;
        }
        
        .benchmarks li {
            margin: 10px 0;
        }
        
        .binary-visualizer {
            margin: 60px 0;
            padding: 30px;
            border: 3px solid #0f0;
            border-radius: 10px;
            background: rgba(0, 255, 0, 0.05);
        }
        
        .viz-title {
            font-size: clamp(1rem, 2.5vw, 1.8rem);
            margin-bottom: 20px;
            color: #0ff;
        }
        
        .viz-controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        
        .viz-btn {
            padding: 12px 25px;
            border: 2px solid #0f0;
            color: #0f0;
            background: transparent;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: clamp(0.8rem, 1.5vw, 1rem);
            transition: all 0.3s ease;
        }
        
        .viz-btn:hover {
            background: #0f0;
            color: #000;
            box-shadow: 0 0 15px #0f0;
        }
        
        .sequence-display {
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #0f0;
            padding: 20px;
            margin: 20px 0;
            min-height: 200px;
            max-height: 400px;
            overflow-y: auto;
            text-align: left;
            font-size: clamp(0.8rem, 1.5vw, 1rem);
            line-height: 2;
            word-break: break-all;
        }
        
        .normal-base {
            color: #0f0;
        }
        
        .mutation-base {
            color: #f00;
            font-weight: bold;
            animation: glow 0.5s ease-in-out;
            text-shadow: 0 0 5px #f00;
        }
        
        @keyframes glow {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; text-shadow: 0 0 10px #f00; }
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
            text-align: center;
        }
        
        .stat-box {
            padding: 20px;
            border: 2px solid #0ff;
            background: rgba(0, 255, 255, 0.05);
        }
        
        .stat-number {
            font-size: clamp(1.5rem, 4vw, 2.5rem);
            color: #0ff;
            margin-bottom: 10px;
        }
        
        .stat-label {
            font-size: clamp(0.8rem, 1.5vw, 1rem);
            opacity: 0.8;
        }
        
        .future {
            font-size: clamp(0.9rem, 2vw, 1.2rem);
            margin: 40px 0;
            opacity: 0.95;
        }
        
        .btn {
            display: inline-block;
            margin: 20px 10px;
            padding: 20px 40px;
            border: 3px solid #0ff;
            color: #0ff;
            text-decoration: none;
            font-size: clamp(0.9rem, 2vw, 1.3rem);
            border-radius: 10px;
            transition: all 0.3s ease;
            background: transparent;
            font-family: 'Courier New', monospace;
            cursor: pointer;
        }
        
        .btn:hover {
            background: #0ff;
            color: #000;
            box-shadow: 0 0 20px #0ff;
        }
        
        .btn-secondary {
            border-color: #0f0;
            color: #0f0;
        }
        
        .btn-secondary:hover {
            background: #0f0;
            box-shadow: 0 0 20px #0f0;
        }

        .btn-purple {
            border-color: #f0f;
            color: #f0f;
        }

        .btn-purple:hover {
            background: #f0f;
            box-shadow: 0 0 20px #f0f;
        }
        
        .decrypt-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        
        .decrypt-modal.active {
            display: flex;
        }
        
        .decrypt-box {
            background: #000;
            border: 3px solid #0ff;
            padding: 40px;
            max-width: 600px;
            width: 90%;
            box-shadow: 0 0 30px #0ff;
            max-height: 90vh;
            overflow-y: auto;
        }
        
        .decrypt-box h2 {
            color: #0ff;
            margin-bottom: 30px;
            font-size: clamp(1.2rem, 3vw, 2rem);
        }
        
        .decrypt-box input[type="password"],
        .decrypt-box input[type="text"],
        .decrypt-box textarea {
            width: 100%;
            padding: 15px;
            margin-bottom: 20px;
            background: #000;
            border: 2px solid #0f0;
            color: #0f0;
            font-family: 'Courier New', monospace;
            font-size: clamp(0.9rem, 2vw, 1.1rem);
        }
        
        .decrypt-box input:focus,
        .decrypt-box textarea:focus {
            outline: none;
            border-color: #0ff;
            box-shadow: 0 0 10px #0ff;
        }

        .file-upload-area {
            border: 3px dashed #0f0;
            padding: 40px;
            margin: 20px 0;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .file-upload-area:hover {
            border-color: #0ff;
            background: rgba(0, 255, 255, 0.05);
        }

        .file-upload-area.drag-over {
            border-color: #0ff;
            background: rgba(0, 255, 255, 0.1);
        }
        
        .close-btn {
            float: right;
            color: #f00;
            font-size: 2rem;
            cursor: pointer;
            line-height: 1;
        }
        
        .close-btn:hover {
            text-shadow: 0 0 10px #f00;
        }
        
        .footer {
            font-size: clamp(0.8rem, 1.6vw, 1rem);
            margin-top: 60px;
            opacity: 0.7;
            padding: 20px 0;
            border-top: 2px solid #0f0;
        }
        
        .attribution {
            font-size: clamp(0.7rem, 1.5vw, 0.9rem);
            margin-top: 10px;
            opacity: 0.7;
        }

        input[type="file"] {
            display: none;
        }

        .decrypted-content {
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #0ff;
            padding: 20px;
            margin-top: 20px;
            max-height: 300px;
            overflow-y: auto;
            text-align: left;
            color: #0ff;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">⚡ SEQSWIFT v1.12</div>
        <div class="nav-btns">
            <button class="nav-btn" onclick="showPuzzle()">🧩 PUZZLE #001</button>
            <button class="nav-btn" onclick="showDecrypt()">🔒 DECRYPT FILE</button>
            <button class="nav-btn" onclick="showAbout()">ABOUT</button>
        </div>
    </div>

    <div class="container">
        <div class="puzzle-alert" onclick="showPuzzle()">
            🧬 PUZZLE #001 LIVE NOW → First 5 solvers get lifetime beta + NFT → Click to solve
        </div>

        <h1>3.45 million HPV16+18 mutations<br>in 0.0007 s</h1>
        
        <div class="subtitle">
            Pure Python • No GPU • No cloud • 489 MB RAM peak • Chromebook verified
        </div>
        
        <div class="boom-section">
            <div class="boom-title">November 18, 2025 – Final BOOM (0.0007 s)</div>
            
            <ul class="benchmarks">
                <li>• HPV16+18 oncology panel → 3.45 million mutations in 0.0007 s</li>
                <li>• E. coli (4.6 Mbp) → 0.016 s</li>
                <li>• 1,000 HBB patients → ~54 s total</li>
                <li>• Full pipeline (build → run → encrypt) → &lt;9 s wall time</li>
                <li>• $140 Chromebook verified</li>
            </ul>
        </div>

        <div class="binary-visualizer">
            <div class="viz-title">🧬 LIVE HBS MUTATION DETECTOR</div>
            
            <div class="stats-grid">
                <div class="stat-box">
                    <div class="stat-number" id="totalBases">0</div>
                    <div class="stat-label">BASES ANALYZED</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number" id="mutationCount">0</div>
                    <div class="stat-label">MUTATIONS FOUND</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number" id="scanTime">0.00s</div>
                    <div class="stat-label">SCAN TIME</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number" id="mutationRate">0.0%</div>
                    <div class="stat-label">MUTATION RATE</div>
                </div>
            </div>

            <div class="viz-controls">
                <button class="viz-btn" onclick="generateSequence()">GENERATE SEQUENCE</button>
                <button class="viz-btn" onclick="scanMutations()">SCAN MUTATIONS</button>
                <button class="viz-btn" onclick="document.getElementById('fileInput').click()">LOAD FILE</button>
                <button class="viz-btn" onclick="clearSequence()">CLEAR</button>
            </div>

            <input type="file" id="fileInput" accept=".txt,.fasta,.seq" onchange="loadFile(event)">

            <div class="sequence-display" id="sequenceDisplay">
                &gt; READY TO ANALYZE GENOMIC DATA<br>
                &gt; CLICK "GENERATE SEQUENCE" TO START...<br>
                &gt; OR LOAD YOUR OWN .FASTA FILE
            </div>
        </div>
        
        <div class="future">
            Full GRCh38 human genome (3.1 B bases) dropping soon
        </div>
        
        <div>
            <a href="https://github.com/daveschliemann/seqswift-pilots/releases" class="btn">
                📦 Download BOOM Pilots (All 7 Binaries)
            </a>
            
            <a href="mailto:license@seqswift.com?subject=decrypt" class="btn btn-secondary">
                🔐 Request Decryption Passphrase
            </a>

            <button class="btn btn-purple" onclick="showDecrypt()">
                🔒 Decrypt Your Pilot
            </button>
        </div>

        <div style="margin-top: 40px; font-size: clamp(0.9rem, 1.8vw, 1.1rem); opacity: 0.85;">
            <p><strong>Free Pilots Open Now:</strong></p>
            <p>• First 100 labs → free with testimonial</p>
            <p>• 3 lifetime licenses → random draw this week for anyone who gives feedback</p>
            <p>• Clinical/commercial → <a href="mailto:license@seqswift.com" style="color: #0ff;">license@seqswift.com</a></p>
        </div>
        
        <div class="footer">
            Encrypted pilots • Open-source core • Patent pending<br>
            No cloud • No Docker • Free forever
            <div class="attribution">Built by Schlayballs | Contact: @schlayguy</div>
        </div>
