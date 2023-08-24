import os
from dotenv import load_dotenv
import streamlit as st
import openai

t_in = """foo
    bar
"""
g_out = """Car
    break
    startEngine
Truck
    move
    stop
"""
t_out="""class foo{
    public void bar();
}
"""

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



def main():
    load_dotenv()
    key = os.environ.get('OPENAI_API_KEY')
    openai.api_key=key
    st.set_page_config(page_title="Code Sidekick")
    st.header("Code Sidekick")
    s_in = st.text_area("Sample Input:",value=t_in)
    s_cx = st.text_area("Optional Context:")
    s_out = st.text_area("Sample Output:",value=t_out)
    g_in = st.text_area("Generator Input:",value=g_out)

    if st.button("Generate Code"):
        button_handler(s_in, s_out, g_in, s_cx)

def button_handler(s_in, s_out, g_in, s_cx):
    input_ok = len(s_in)>0 and len(s_out)>0 and len(g_in)>0
 
    if input_ok:
        ctx = f"""
and the startup code in backticks given as 
```
{g_in}
```
"""
        prompt = f"""
Given the following pattern bounded in backticks:
```
{s_in}
```
{ctx if len(s_cx)>0 else ""}
gives the following code output also in backticks:
```
{s_out}
```
Generate the new code based on this new input in back ticks:
```
{g_in}
```
Otherwise say "I don't understand the pattern"
"""
        response = get_completion(prompt)
        st.write(response)
    else:
        st.write(f"s_in={len(s_in)},g_in={len(g_in)}, s_cx={len(s_cx)}")

if __name__ == '__main__':
    main()
  