# AI Code Roaster 🎯🔥
# Yeh project Google Gemini AI ka use karta hai
# aapke Python code ko roast (mazaaq) karne ke liye! 😂

# Libraries import kar rahe hain
from google import genai
from dotenv import load_dotenv
import os

# .env file load karenge - isme API key stored hai
load_dotenv()


# =============================================
# STEP 1 : Gemini client setup
# =============================================

def setup_gemini():
    """
    Kaam: Gemini AI ka client banata hai
    Return: ready-to-use Gemini client object

    Process:
    1. Environment se API key nikalta hai
    2. Check karta hai key mili ya nahi
    3. Client banata hai aur return karta hai
    """

    # API key environment se laao
    api_key = os.getenv("GEMINI_API")

    # Check karo - API key mili ya nahi?
    if not api_key:
        # Agar key nahi mili to error dikhao aur program band karo
        print("Error: Gemini API key not available ")
        exit()

    # Client banaya aur return kiya
    client = genai.Client(api_key=api_key)
    return client


# =============================================
# STEP 2 : User se code lena
# =============================================

def get_code_from_user():
    """
    Kaam: User se code input leta hai (multiple lines)
    Return: Saare lines ko ek string mein jod kar return karta hai

    User END likh kar batata hai ki code khatam hua
    """

    # User ko instructions dikhao
    print("*\n*" + "=" * 40)
    print("apna code paste karo aur END likh kar khatam karo ")
    print("*\n*" + "=" * 40)

    # Code lines store karne ke liye empty list
    code_lines = []

    # Loop - user se baar baar line lo, END aane tak
    # Hamein nahi pata user kitni lines likhega, isiliye while True use kiya
    while True:
        # User se ek line lo
        line = input("➡️ ")

        # Check karo - kya user ne END likha?
        # .strip() -> extra spaces hataye
        # .upper() -> "end" ko "END" banaye
        if line.strip().upper() == "END":
            break  # Loop se bahar!

        # Line ko list mein store karo
        code_lines.append(line)

    # Saari lines ko ek string mein jodo
    # "\n" ka matlab hai new line - har line ke beech mein enter lagao
    complete_code = "\n".join(code_lines)

    return complete_code

    # Example:
    # code_lines = ["print('hi')", "print('bye')"]
    # join -> "print('hi')\nprint('bye')"


# =============================================
# STEP 3 : Gemini se roast karwana
# =============================================

def roast_code(client, code):
    """
    Kaam: Gemini AI ko prompt dekar code roast karwana
    Return: AI ka roast response (text)

    Input:
    - client: Gemini client object
    - code: User ka jo code roast karna hai
    """

    # Prompt banaya - yeh Gemini ko batata hai ki kya karna hai
    prompt = f"""

    tu ek expert Python developer hai
    jo funny style mai code review karta hai

    neeche diya gaya Python code dekh

    ```python
    {code}
    ```
    ab yeh karo:

    1. Roast funny style code main
    iski kamiya batao, Hindi aur English mix karke. Emoji bhi use kar sakte ho
    genuine mistakes ko point out karo

    2. Better code - sahi tarika dikhao
    explain karo kyun better hai yeh

    3. Level - batao yeh code hai
    Beginner / Intermediate / Advanced

    4. Score - 1 to 10 mein score do

    format exactly yeh rakho:
    Roast:
    [roast yaha par]

    Better Code:
    [better code yahan par]

    Level: [level]

    [motivational line]
    """

    # Gemini ko prompt bhejo
    response = client.models.generate_content(
        model="gemini-3.5-flash",  # Model ka naam
        contents=prompt             # Jo prompt bhejna hai
    )

    # Response ka text return karo
    return response.text


# =============================================
# STEP 4 : Result print karna
# =============================================

def print_result(roast):
    """
    Kaam: Gemini ka roast response nicely format karke print karna
    Input: roast - Gemini ka response text
    """

    print("\n" + "=" * 40)          # Upar ki border
    print("Gemini ka roast: ")       # Title
    print("=" * 40)                  # Border
    print(roast)                     # Roast ka content
    print("\n" + "=" * 40)          # Neeche ki border


# =============================================
# STEP 5 : Dobara puchhna
# =============================================

def ask_again():
    """
    Kaam: User se puchhta hai ki aur code roast karwana hai ya nahi
    Return: True (haan) / False (nahi)

    Agar user "yes" (kuch bhi case mein) likhega to True return hoga
    """

    choice = input("\n Ek aur code roast karna hai kya? (yes/no): ")

    # choice.strip() -> extra spaces hatao
    # .lower() -> "YES" ko "yes" karo
    # == "yes" -> agar "yes" hai to True, nahi to False
    return choice.strip().lower() == "yes"


# =============================================
# MAIN FUNCTION - Poora program yahan se chalta hai
# =============================================

def main():
    """
    Kaam: Program ka entry point - saare steps ko coordinate karta hai

    Flow:
    1. Gemini setup karo (ek baar)
    2. Loop chalao (baar baar)
       a. User se code lo
       b. Check karo code empty to nahi
       c. Gemini se roast karwao
       d. Result print karo
       e. Puchho - aur karna hai?
    3. Bye bolo
    """

    # Step 1: Gemini setup karo (sirf ek baar!)
    client = setup_gemini()

    # Step 2: Loop - user jab tak chahe tab tak roast karte raho
    while True:
        # User se code lo
        code = get_code_from_user()

        # Check karo - kya code empty hai?
        if not code.strip():           # code.strip() -> extra spaces hatao
            print("Bhai kuch to likho! ")  # Warning!
            continue                    # Wapas loop ke shuru mein jao

        # Roast karwao
        print("\n Gemini se roast karwa raha hoon... ")
        roast = roast_code(client, code)

        # Result print karo
        print_result(roast)

        # Dobara puchho
        if not ask_again():            # Agar user ne "no" kaha
            print("\n Bye! Code likhte raho ")
            break                      # Loop se bahar, program khatam!


# Program ka starting point
main()
