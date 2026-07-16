const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(express.json());
app.use(cors());

// ==========================================
// 🔴 ส่วนที่ 1: ตั้งค่า LINE API ID ต่างๆ (นำมาใส่ที่นี่)
// ==========================================
// 1. นำ Channel Access Token จาก LINE Developers (Messaging API) มาใส่
const LINE_CHANNEL_ACCESS_TOKEN = 'YOUR_CHANNEL_ACCESS_TOKEN_HERE';

// 2. นำ User ID ของผู้รับ (หาได้ในหน้าจอ Basic Settings ล่างสุดของ LINE Developers)
const TARGET_LINE_USER_ID = 'YOUR_LINE_USER_ID_HERE'; 

// ==========================================
// 🔴 ส่วนที่ 2: โครงสร้าง Flex Message JSON
// (เอา JSON จาก LINE Flex Message Simulator มาวางแทนที่นี่)
// ==========================================
const flexMessageJson = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "รอการออกแบบ Flex Message...",
        "weight": "bold",
        "size": "xl",
        "color": "#00B900"
      },
      {
        "type": "text",
        "text": "นำ JSON จาก Simulator มาวางทับก้อนเนื้อหานี้ได้เลย",
        "wrap": true,
        "color": "#666666",
        "size": "sm",
        "margin": "md"
      }
    ]
  }
};

// Endpoint รับคำสั่งจากหน้าเว็บเพื่อส่ง Flex Message
app.post('/send-flex', async (req, res) => {
    try {
        const response = await axios.post(
            'https://api.line.me/v2/bot/message/push',
            {
                to: TARGET_LINE_USER_ID,
                messages: [
                    {
                        type: 'flex',
                        altText: 'คุณได้รับ Flex Message ใหม่ (เปิดดูในแอป LINE)',
                        contents: flexMessageJson
                    }
                ]
            },
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${LINE_CHANNEL_ACCESS_TOKEN}`
                }
            }
        );

        res.json({ success: true, message: 'ส่ง Flex Message สำเร็จ!', data: response.data });
    } catch (error) {
        // จัดการ Error หากส่งไม่สำเร็จ (เช่น Token ผิด หรือ User ID ผิด)
        console.error('Error sending Flex Message:', error.response ? error.response.data : error.message);
        res.status(500).json({ 
            success: false, 
            message: 'เกิดข้อผิดพลาดในการส่งข้อความ', 
            error: error.response ? error.response.data : error.message 
        });
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`✅ Backend Server เปิดทำงานแล้วที่ http://localhost:${PORT}`);
    console.log(`⚠️ อย่าลืมใส่ LINE_CHANNEL_ACCESS_TOKEN และ TARGET_LINE_USER_ID ในโค้ด server.js นะครับ!`);
});
