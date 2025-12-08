# 🆘 Suicide Helpline Chatbot

A web-based mental health support system providing immediate, confidential, and accessible crisis intervention for individuals experiencing emotional distress or suicidal ideation.

## 🌟 Overview

The Suicide Helpline Chatbot is a Flask-based web application designed to provide immediate mental health support through an intelligent conversational interface. The system uses rule-based natural language processing to detect crisis levels and respond with appropriate interventions, resources, and coping strategies.

**Key Highlights:**
- 24/7 Accessible Crisis Support
- Anonymous Chat Capability
- Multi-Level Crisis Detection
- Comprehensive Resource Integration
- User Privacy Protection

## ✨ Features

### 🔐 Dual Access Modes
- **Anonymous Mode**: Start chatting immediately without any login
- **Registered Mode**: Create an account to save conversation history

### 🚨 Intelligent Crisis Detection
- **Immediate Crisis Recognition**: Detects keywords indicating imminent danger
- **High-Risk Assessment**: Identifies self-harm and severe distress indicators
- **Moderate Distress Support**: Recognizes depression, loneliness, and anxiety patterns

### 💬 Comprehensive Response Library
- Crisis intervention protocols with emergency hotline numbers
- Emotional validation and support messages
- Coping strategies and grounding techniques
- Professional help guidance
- Mental health resources and support organizations

### 🔒 Security & Privacy
- Encrypted password storage using Werkzeug security
- Session-based authentication
- SQLite database for secure data management
- Optional anonymous usage without data storage

### 🎨 User-Friendly Interface
- Responsive design for all devices
- Calming purple gradient theme
- Animated background for visual engagement
- Clear crisis information display
- Real-time message exchange

## 🆘 Crisis Resources

**If you or someone you know is in immediate danger, please contact:**

### United States
- **988 Suicide & Crisis Lifeline**: Call or Text **988** (24/7)
- **Crisis Text Line**: Text **HOME** to **741741**
- **Veterans Crisis Line**: Call **988** and Press **1**
- **Emergency Services**: **911**

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**
- **Flask 3.0.0** - Web framework
- **SQLite3** - Database management
- **Werkzeug 3.0.1** - Security utilities

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with animations
- **JavaScript (ES6+)** - Interactivity and AJAX

### Key Libraries
- `flask` - Web application framework
- `sqlite3` - Database operations
- `werkzeug.security` - Password hashing
- `re` - Regular expressions for pattern matching

## 🚀 Usage

### For Anonymous Users
1. Navigate to `http://localhost:5000`
2. Click "TALK NOW - No Login Required"
3. Start chatting immediately

### For Registered Users
1. Navigate to `http://localhost:5000/signup`
2. Create an account with username and password
3. Login at `http://localhost:5000/login`
4. Access chat with conversation history saving

### Sample Interactions

**Crisis Situation:**
```
User: "I want to end my life"
Bot: [Provides immediate crisis resources with 988 hotline and emergency services]
```

**Emotional Support:**
```
User: "I'm feeling really depressed"
Bot: [Offers validation, checks safety, provides coping strategies]
```

**Resource Request:**
```
User: "I need help finding a therapist"
Bot: [Provides professional help guidance and resource links]
```

### Crisis Detection Algorithm

The chatbot uses a hierarchical keyword matching system:

1. **Immediate Crisis Keywords** (Highest Priority)
   - "kill myself", "end my life", "suicide", "want to die"
   - **Action**: Immediate crisis response with emergency contacts

2. **High-Risk Keywords**
   - "suicidal", "self harm", "cutting", "overdose"
   - **Action**: Crisis intervention with safety resources

3. **Moderate Distress Keywords**
   - "depressed", "hopeless", "worthless", "alone"
   - **Action**: Emotional support and coping strategies

4. **General Support**
   - Validation responses, professional help guidance, resources

### Message Flow

```
User Input → Lowercase Conversion → Keyword Matching → 
Category Identification → Response Selection → 
Database Logging (if logged in) → Response Delivery
```

## 🔒 Security

### Implemented Security Measures

- **Password Hashing**: Uses Werkzeug's `generate_password_hash()` with PBKDF2
- **Session Management**: Cryptographically signed Flask sessions
- **SQL Injection Prevention**: Parameterized queries throughout
- **Input Validation**: Client and server-side validation
- **XSS Protection**: HTML escaping for user-generated content

### Contribution Guidelines

- Ensure code follows PEP 8 style guidelines
- Add appropriate comments and documentation
- Test thoroughly before submitting
- Update README if adding new features
- Respect user privacy and security in all changes

### Areas for Contribution

- 🌐 Multi-language support
- 🤖 Enhanced NLP capabilities
- 📱 Mobile app development
- 🎨 UI/UX improvements
- 🔧 Performance optimizations
- 📊 Analytics dashboard
- 🧪 Comprehensive testing suite

## ⚠️ Disclaimer

**IMPORTANT: This chatbot is NOT a replacement for professional mental health care or emergency services.**

### Limitations

- This is a rule-based chatbot, not an AI counselor
- It cannot provide medical diagnosis or treatment
- It cannot replace human therapists or crisis counselors
- Responses are based on keyword matching, not contextual understanding

### When to Seek Immediate Help

If you or someone you know is in immediate danger:
- **Call 911** (Emergency Services)
- **Call 988** (Suicide & Crisis Lifeline)
- **Go to the nearest emergency room**
- **Contact a mental health professional**

### Privacy Notice

- Anonymous users: No data is stored
- Registered users: Chat history is stored securely
- No personal health information is shared with third parties
- Users can delete accounts and data at any time
