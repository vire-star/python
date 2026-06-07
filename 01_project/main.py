# AI Code Roaster

from google import genai
from dotenv import load_dotenv
import os

# .env file loadk karenge

load_dotenv()

# step 1

def setup_gemini():
    """
    gemini client banayenge
    """

    # API key ko laayenge environment se

    api_key=os.getenv("GEMINI_API")

    # check karo api mili ya nhi 

    if not api_key:
        print("Error: Gemini API key not available 🔑❌")
        exit()

    # client banayenge and return karenge

    client = genai.Client(api_key=api_key)
    return client
    

# Step 2

def get_code_from_user():
    """
    hum yahan par user se uska code lenge
    """
    print("*\n*" +"="*40)
    print("apna code paste karo aur END likh kar khatam karo 📝")

    print("*\n*" +"="*40)

    # code lines store karne k liye

    code_lines=[]

    # Baar baar lines lo- end aaney tak
    # yeh loop ka kaam

    # user code dega, aur hummey nhi pata ki user k code mai kitni line hia 
    while True:
        # Ek line lo user se
        line = input("➡️ ")

        #  End aaya band karo

        # print("hello word")
        #    print("hi")
        if line.strip().upper()=="END":
            # end End -> "END"
            break

        # line store karo
        
        code_lines.append(line)

        # sab lines ek string mein jodo

    complete_code ="\n".join(code_lines)
    return complete_code
    
    # ["line1",
    #  "line2",
    #  "line3"]
    # "line1/line2/line3"



# step 3
# gemini se roast krwayenge

def roast_code(client,code):
    """
    gemini se roast karwayebge
    """

    prompt=f"""

    tu ek expert Python developer hai 🐍
    jo funny style mai code review karta hai 😂

    neeche diya gaya Python code dekh 👇

    ```python
    {code}
    ```
    ab yeh karo:

    1. Roast funny style code main 🔥
    iski kamiya batao, Hindi aur English mix karke. Emoji bhi use kar sakte ho 😄
    genuine mistakes ko point out karo 🎯

    2. Better code - sahi tarika dikhao ✅
    explain karo kyun better hai yeh 💡

    3. Level - batao yeh code hai 📊
    Beginner / Intermediate / Advanced

    4. Score - 1 to 10 mein score do ⭐

    format exactly yeh rakho:
    🔥 Roast:
    [roast yaha par]

    ✨ Better Code:
    [better code yahan par]

    📈 Level: [level]

    💪 [motivational line]
    """
    
    # gemini ko prompt de

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt

    )

    return response.text


# step 4 result print karo

def print_result(roast):
    """
    roast result nicely print karo
    """

    print("\n"+"="*40)
    print("Gemini ka roast: 🔥😆")
    print("="*40)
    print(roast)
    print("\n"+"="*40)




# step 5

def ask_again():
    """
    User se dobara puchenge

    """

    choice=input("\n Ek aur code roast karna hai kya? (yes/no): 🤔 ")
    return choice.strip().lower()=="yes"
# "Yes, yes YES"


def main():
    """
    maine function poora program chalta hai 


    
    """

    # gemini setyp karo- ek baar
    client = setup_gemini()


    # pehli baar seedha chalao

    # phir user ki marzi pe

    while True:
        # user se code lo
        code = get_code_from_user()

        # checke karo -code empty toh nhi 

        if not code.strip():
            print("Bhai kuch to likho! 😤✍️")
            continue

        # roast karwao

        print("\n Gemini se roast karwa raha hoon... ⏳🔥")
        roast = roast_code(client,code)

        # result dikhao
        print_result(roast)

        # dobara
        if not ask_again():
            print("\n Bye! Code likhte raho 🚀👨‍💻")
            break
    



main()