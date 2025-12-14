"""
Test Groq API connection with the updated model.
"""
import sys
import os

# Add parent directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
backend_dir = os.path.join(parent_dir, 'backend')
sys.path.insert(0, backend_dir)

print("=" * 60)
print("Testing Groq API Connection")
print("=" * 60)

try:
    from groq import Groq
    from app.core.config import settings
    
    print(f"✓ Groq client library installed")
    print(f"  API Key: {settings.groq_api_key[:20]}...")
    print(f"  Model: {settings.groq_model}")
    
    # Create client
    client = Groq(api_key=settings.groq_api_key)
    print("✓ Groq client created")
    
    # Test with simple query
    print("\nSending test request...")
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say 'Hello! Groq API is working.' in exactly 5 words."
            }
        ],
        model=settings.groq_model,
        temperature=0.3,
        max_tokens=20
    )
    
    result = response.choices[0].message.content
    print(f"✓ Response received: {result}")
    
    print("\n" + "=" * 60)
    print("✅ Groq API is working correctly!")
    print("=" * 60)
    print(f"\n📊 Model: {settings.groq_model}")
    print("🎉 Your PatentGuard app can now analyze patents!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("   Run: pip install groq")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\n📝 Possible issues:")
    print("   1. Check your GROQ_API_KEY in backend/.env")
    print("   2. Verify API key at: https://console.groq.com/keys")
    print("   3. Make sure you have API credits/quota")
    sys.exit(1)
