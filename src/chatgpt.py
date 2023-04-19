import openai

#defining Open api key
# Add your personal Open API key here
openai.api_key = ""


#set up the model and prompt
def chatgptmoedel(text):
    model_engine = "text-davinci-003"


    # Generating the response
    completion = openai.Completion.create(
        model=model_engine,
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.2,

    )
    response = completion.choices[0].text
    return response

