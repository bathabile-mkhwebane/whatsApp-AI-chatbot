from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from textblob import TextBlob
app=Flask(__name__)

@app.route("/Whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg=request.values.get('Body', '').lower
    response=MessagingResponse()
    msg=response.message()

    if 'claim' in incoming_msg:
        msg.body("Please enter your claim number")
    elif 'hi' in incoming_msg or 'hello' in incoming_msg:
        msg.body("Hi there!👋 I am Rob for Abacus Insurance ready to assist you with your claim")
    else:
        sentiment = TextBlob(incoming_msg).sentiment.polarity
        if sentiment<0:
            msg.body("I'm sorry you having troubles, let me help you")
        else:
            msg.body("Thank you for your message! How can I assist you today?")

    return str(response)

if __name__=="__main__":
    app.run(debug=True)git