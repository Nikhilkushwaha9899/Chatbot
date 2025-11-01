from flask import Flask, render_template, request, jsonify
import re
import random

app = Flask(__name__)

# Comprehensive message library for suicide helpline chatbot
MESSAGE_LIBRARY = {
    # Crisis detection keywords and responses
    "crisis_keywords": {
        "immediate": ["kill myself", "end my life", "suicide", "want to die", "ending it all", 
                     "not worth living", "better off dead", "cant go on", "no reason to live",
                     "goodbye cruel world", "final goodbye", "last message"],
        "high_risk": ["suicidal", "self harm", "hurt myself", "cutting", "overdose", 
                     "jump off", "hanging", "pills", "no hope", "give up"],
        "moderate": ["depressed", "hopeless", "worthless", "alone", "cant take it", 
                    "everything hurts", "numb", "empty", "burden", "tired of living"]
    },
    
    # Immediate crisis responses
    "crisis_responses": [
        "I'm really concerned about what you're sharing. Your life matters, and I want to help. Please reach out to a crisis counselor immediately:\n\n🆘 National Suicide Prevention Lifeline: 988 (US)\n🆘 Crisis Text Line: Text HOME to 741741\n🆘 International: findahelpline.com\n\nAre you in immediate danger right now?",
        
        "Thank you for trusting me with this. What you're feeling is serious, and you deserve immediate support. Please contact:\n\n🆘 988 Suicide & Crisis Lifeline (24/7)\n🆘 Crisis Text Line: Text TALK to 741741\n🆘 Emergency Services: 911\n\nIs there someone with you right now, or can I help you reach out to someone?",
        
        "I hear how much pain you're in, and I'm glad you're talking about it. This is a crisis moment, and professional help is crucial:\n\n🆘 Call 988 for immediate support (24/7)\n🆘 Text HOME to 741741 for Crisis Text Line\n🆘 Go to your nearest emergency room\n\nCan you tell me if you're safe right now?"
    ],
    
    # Empathetic opening responses
    "greetings": [
        "Hello, I'm here to listen and support you. You're not alone. How are you feeling right now?",
        "Hi there. Thank you for reaching out. This is a safe space. What's on your mind today?",
        "Welcome. I'm glad you're here. Whatever you're going through, you don't have to face it alone. How can I support you?",
        "Hello. It takes courage to reach out. I'm here to listen without judgment. What brings you here today?"
    ],
    
    # Responses for depression/hopelessness
    "depression_responses": [
        "I hear that you're feeling depressed, and I want you to know that your feelings are valid. Depression can make everything feel overwhelming, but these feelings can change with support. Have you been able to talk to anyone about how you're feeling?",
        
        "Feeling hopeless is incredibly difficult, and I'm sorry you're experiencing this. These dark feelings are symptoms of what you're going through, not the reality of your situation. Would it help to talk about what's contributing to these feelings?",
        
        "Depression can make it feel like things will never get better, but that's the illness talking, not the truth. Many people who've felt this way have found relief and hope again. Are you currently getting any support or treatment?",
        
        "I understand you're in a lot of emotional pain right now. That pain is real, but it doesn't have to be permanent. There are people who want to help you through this. Can you tell me more about what you're experiencing?"
    ],
    
    # Responses for feeling alone
    "loneliness_responses": [
        "Feeling alone can be one of the most painful experiences. I want you to know that by reaching out here, you've already taken a brave step toward connection. You're not as alone as you might feel. What's making you feel isolated right now?",
        
        "Loneliness can be overwhelming, but connection is possible even when it doesn't feel that way. I'm here with you now. Is there someone in your life you trust, even if you haven't talked to them recently?",
        
        "I hear that you're feeling alone. That's a heavy burden to carry. Sometimes isolation happens gradually, and sometimes it's sudden. Either way, reaching out is important, and you've done that. What would support look like for you right now?"
    ],
    
    # Responses for self-harm mentions
    "self_harm_responses": [
        "I'm concerned about what you're sharing about self-harm. These thoughts and behaviors are serious signs that you need additional support. Please reach out to:\n\n📞 988 Suicide & Crisis Lifeline\n📞 Crisis Text Line: Text HOME to 741741\n\nHave you been able to talk to a mental health professional about this?",
        
        "Thank you for being honest about self-harm. This takes courage to share. Self-harm is often a way of coping with overwhelming emotions, but there are safer ways to manage these feelings. Please contact a crisis counselor who can provide immediate support. Are you currently seeing a therapist?"
    ],
    
    # Validation and support messages
    "validation_responses": [
        "What you're feeling is valid, and it's okay to not be okay. Thank you for sharing this with me.",
        "I hear you, and I want you to know that your pain matters. You matter.",
        "It takes strength to talk about these feelings. I'm glad you're here.",
        "Your feelings are important, and you deserve support and care.",
        "You're not being dramatic, and you're not being weak. What you're experiencing is real and difficult."
    ],
    
    # Coping strategies
    "coping_strategies": [
        "When feelings become overwhelming, here are some things that might help in this moment:\n\n• Take slow, deep breaths - in for 4 counts, out for 6\n• Ground yourself: name 5 things you see, 4 you hear, 3 you can touch\n• Reach out to someone you trust\n• Write down your thoughts\n• Take a walk or change your environment\n\nWhat sounds manageable for you right now?",
        
        "Distraction can be a helpful tool when emotions are intense:\n\n• Listen to music\n• Watch something comforting\n• Do a simple physical activity\n• Practice self-care (shower, drink water, eat something)\n• Call or text a friend\n\nWhich of these feels possible for you?",
        
        "Creating safety in the moment is important:\n\n• Remove immediate means of harm if possible\n• Stay in a public or populated space\n• Contact someone you trust\n• Use a crisis line for support\n• Focus on getting through the next hour, then the next\n\nCan you commit to your safety for the next few hours?"
    ],
    
    # Professional help encouragement
    "professional_help": [
        "I encourage you to connect with a mental health professional who can provide ongoing support. Have you considered:\n\n• Talking to your doctor about a referral\n• Contacting a therapist or counselor\n• Reaching out to a local mental health clinic\n• Calling 988 to discuss treatment options\n\nWould you like help finding resources in your area?",
        
        "Professional support can make a real difference. A therapist or counselor can work with you to develop coping strategies and address what you're going through. If cost is a concern, many communities have sliding-scale or free mental health services. Would you like suggestions on how to find help?"
    ],
    
    # Check-in questions
    "check_in_questions": [
        "How are you feeling right now in this moment?",
        "Are you in a safe place currently?",
        "Is there someone you trust who you can reach out to?",
        "Have you been able to eat or sleep recently?",
        "What's the most pressing thing on your mind right now?",
        "On a scale of 1-10, how intense are your feelings right now?"
    ],
    
    # Resources information
    "resources": {
        "crisis_lines": """
🆘 IMMEDIATE CRISIS RESOURCES:

United States:
• 988 Suicide & Crisis Lifeline (24/7) - Call or Text 988
• Crisis Text Line - Text HOME to 741741
• Veterans Crisis Line - Call 988 and Press 1

International:
• Find a helpline: findahelpline.com
• Befrienders Worldwide: befrienders.org

Emergency:
• Call 911 or go to nearest emergency room
        """,
        
        "ongoing_support": """
ONGOING SUPPORT RESOURCES:

Mental Health:
• NAMI (National Alliance on Mental Illness): 1-800-950-6264
• SAMHSA National Helpline: 1-800-662-4357
• Psychology Today Therapist Finder: psychologytoday.com

Online Support:
• 7 Cups (free emotional support): 7cups.com
• NAMI Online Support Groups: nami.org
• Reddit r/SuicideWatch community

Apps:
• Calm Harm (self-harm management)
• Headspace (meditation)
• Woebot (mental health support)
        """
    },
    
    # Goodbye/closing messages
    "goodbye_responses": [
        "I'm glad you reached out today. Please remember that support is available 24/7. If you're in crisis, call 988 or text HOME to 741741. You matter, and your life has value. Take care of yourself.",
        
        "Thank you for sharing with me. Remember, you're not alone in this. Crisis support is always available at 988. Please reach out whenever you need to. Be safe.",
        
        "Before you go, please save these numbers: 988 (Suicide & Crisis Lifeline) and 741741 (Crisis Text Line). You deserve support, and help is available anytime you need it. Take care."
    ],
    
    # Clarification/general responses
    "clarification_requests": [
        "I want to make sure I understand what you're going through. Can you tell me more about that?",
        "That sounds really difficult. Would you like to share more about what you're experiencing?",
        "I'm here to listen. What's most important for you to talk about right now?",
        "Help me understand what you're feeling. Can you describe what's happening?"
    ],
    
    # Positive reinforcement
    "positive_reinforcement": [
        "Reaching out is a sign of strength, not weakness. I'm proud of you for being here.",
        "You've taken an important step by talking about this. That takes courage.",
        "Thank you for trusting me with your feelings. That's not easy to do.",
        "You're doing the right thing by seeking support."
    ]
}

# Enhanced chatbot logic with pattern matching
def chatbot_response(user_input):
    user_input_lower = user_input.lower()
    
    # Check for immediate crisis keywords
    for keyword in MESSAGE_LIBRARY["crisis_keywords"]["immediate"]:
        if keyword in user_input_lower:
            return random.choice(MESSAGE_LIBRARY["crisis_responses"])
    
    # Check for high-risk keywords
    for keyword in MESSAGE_LIBRARY["crisis_keywords"]["high_risk"]:
        if keyword in user_input_lower:
            return random.choice(MESSAGE_LIBRARY["crisis_responses"])
    
    # Check for self-harm mentions
    if any(word in user_input_lower for word in ["self harm", "cut myself", "hurt myself", "cutting"]):
        return random.choice(MESSAGE_LIBRARY["self_harm_responses"])
    
    # Check for greetings
    if re.search(r'\b(hello|hi|hey|greetings)\b', user_input_lower):
        return random.choice(MESSAGE_LIBRARY["greetings"])
    
    # Check for depression/hopelessness
    for keyword in MESSAGE_LIBRARY["crisis_keywords"]["moderate"]:
        if keyword in user_input_lower:
            return random.choice(MESSAGE_LIBRARY["depression_responses"])
    
    # Check for loneliness
    if any(word in user_input_lower for word in ["alone", "lonely", "isolated", "no one", "nobody"]):
        return random.choice(MESSAGE_LIBRARY["loneliness_responses"])
    
    # Request for resources
    if any(word in user_input_lower for word in ["resource", "help", "support", "hotline", "crisis line", "number"]):
        return MESSAGE_LIBRARY["resources"]["crisis_lines"]
    
    # Request for coping strategies
    if any(word in user_input_lower for word in ["coping", "cope", "what can i do", "how do i", "help me feel better"]):
        return random.choice(MESSAGE_LIBRARY["coping_strategies"])
    
    # Request for professional help info
    if any(word in user_input_lower for word in ["therapist", "counselor", "professional", "therapy", "treatment"]):
        return random.choice(MESSAGE_LIBRARY["professional_help"])
    
    # Goodbye
    if any(word in user_input_lower for word in ["bye", "goodbye", "gotta go", "have to go", "thanks"]):
        return random.choice(MESSAGE_LIBRARY["goodbye_responses"])
    
    # Positive acknowledgment for sharing
    if any(word in user_input_lower for word in ["i feel", "i'm feeling", "feeling", "i think", "i've been"]):
        return random.choice(MESSAGE_LIBRARY["validation_responses"]) + "\n\n" + random.choice(MESSAGE_LIBRARY["check_in_questions"])
    
    # Default response with validation and clarification
    return random.choice(MESSAGE_LIBRARY["clarification_requests"]) + "\n\nIf you're in crisis, please reach out immediately:\n🆘 Call or Text 988\n🆘 Text HOME to 741741"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "I'm here to listen. What's on your mind?"})
    
    response = chatbot_response(user_input)
    return jsonify({"response": response})

# Health check endpoint
@app.route("/health")
def health_check():
    return jsonify({"status": "active", "service": "suicide helpline chatbot"})

if __name__ == "__main__":
    app.run(debug=True)