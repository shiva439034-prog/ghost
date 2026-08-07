<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GhostEngine v6.0 Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .container { width: 100%; max-width: 600px; background: #1e293b; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        h1 { text-align: center; color: #38bdf8; font-size: 24px; margin-bottom: 5px; }
        .status { text-align: center; font-size: 14px; margin-bottom: 25px; color: #94a3b8; }
        .card { background: #0f172a; padding: 15px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #334155; }
        .card h3 { margin-top: 0; color: #cbd5e1; font-size: 16px; }
        button { background: #0284c7; color: white; border: none; padding: 10px 15px; border-radius: 6px; cursor: pointer; font-weight: bold; width: 100%; margin-top: 10px; }
        button:hover { background: #0369a1; }
        .result { background: #1e293b; padding: 10px; margin-top: 10px; border-radius: 4px; font-family: monospace; font-size: 13px; color: #4ade80; word-break: break-all; }
        input { width: 100%; padding: 8px; margin-top: 5px; box-sizing: border-box; background: #334155; border: 1px solid #475569; color: white; border-radius: 4px; }
    </style>
</head>
<body>

<div class="container">
    <h1>👻 GhostEngine v6.0</h1>
    <div class="status" id="server-status">सर्वर स्टेटस चेक हो रहा है...</div>

    <!-- AI Mentor Section -->
    <div class="card">
        <h3>🤖 AI Creator Mentor</h3>
        <button onclick="getMentorAdvice()">सलाह लें (Get Advice)</button>
        <div class="result" id="mentor-result">क्लिक करने पर यहाँ सलाह दिखेगी...</div>
    </div>

    <!-- P2P Streaming Section -->
    <div class="card">
        <h3>📡 P2P Video Stream</h3>
        <label>Video ID:</label>
        <input type="text" id="video-id" value="101">
        <button onclick="getStreamUrl()">स्ट्रीम लिंक जनरेट करें</button>
        <div class="result" id="stream-result">स्ट्रीम URL यहाँ दिखेगा...</div>
    </div>

    <!-- Wallet Withdrawal Section -->
    <div class="card">
        <h3>💰 Wallet & Withdrawal</h3>
        <label>रकम (Amount in ₹):</label>
        <input type="number" id="withdraw-amount" value="500">
        <button onclick="requestWithdrawal()">विथड्रॉल रिक्वेस्ट भेजें</button>
        <div class="result" id="withdraw-result">विथड्रॉल स्टेटस यहाँ दिखेगा...</div>
    </div>
</div>

<script>
    const API_BASE = "https://ghost-16i.onrender.com";

    // सर्वर स्टेटस चेक करें
    async function checkServer() {
        try {
            let res = await fetch(API_BASE + "/");
            let data = await res.json();
            document.getElementById("server-status").innerText = `Engine: ${data.engine} | Status: ${data.status}`;
            document.getElementById("server-status").style.color = "#4ade80";
        } catch (err) {
            document.getElementById("server-status").innerText = "⚠️ सर्वर से कनेक्ट नहीं हो पा रहा है!";
            document.getElementById("server-status").style.color = "#f87171";
        }
    }
    checkServer();

    // AI मेंटर सलाह लाएं
    async function getMentorAdvice() {
        document.getElementById("mentor-result").innerText = "लोड हो रहा है...";
        try {
            let res = await fetch(API_BASE + "/mentor");
            let data = await res.json();
            document.getElementById("mentor-result").innerText = data.advice;
        } catch (err) {
            document.getElementById("mentor-result").innerText = "एरर आ गया!";
        }
    }

    // P2P स्ट्रीम लिंक लाएं
    async function getStreamUrl() {
        let vid = document.getElementById("video-id").value;
        document.getElementById("stream-result").innerText = "लोड हो रहा है...";
        try {
            let res = await fetch(`${API_BASE}/stream?video_id=${vid}&mode=video`);
            let data = await res.json();
            document.getElementById("stream-result").innerText = JSON.stringify(data, null, 2);
        } catch (err) {
            document.getElementById("stream-result").innerText = "एरर आ गया!";
        }
    }

    // बैंक विथड्रॉल रिक्वेस्ट
    async function requestWithdrawal() {
        let amt = document.getElementById("withdraw-amount").value;
        document.getElementById("withdraw-result").innerText = "प्रोसेसिंग...";
        try {
            let res = await fetch(`${API_BASE}/withdraw?amount=${amt}`);
            let data = await res.json();
            document.getElementById("withdraw-result").innerText = JSON.stringify(data, null, 2);
        } catch (err) {
            document.getElementById("withdraw-result").innerText = "एरर आ गया!";
        }
    }
</script>

</body>
</html>
