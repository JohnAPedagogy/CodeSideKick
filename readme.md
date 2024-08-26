# Sidekick Code generator

> Special thanks to Alejandro's [YouTube](https://youtu.be/dXxQ0LR-3Hg) video for providing the base code for this project.

## Introduction
------------
The Sidekick code generator is a Python application that allows you to generate code based on base templates. Simply provide a template input files and the template output file.  Then, provide the final input file. The app utilizes a language model to generate your desired code snippets. 

## Dependencies and Installation
----------------------------
To install the Sidekick, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```

## Usage
-----
To use the Sidekick App, follow these steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

## Contributing
------------
Feel free to fork, send a PR, utilize and enhance the app based on your own requirements.

## License
-------
The MultiPDF Chat App is released under the [MIT License](https://opensource.org/licenses/MIT).
