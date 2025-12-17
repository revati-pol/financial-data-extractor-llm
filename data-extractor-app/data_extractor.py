from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

def extract(article):
      prompt = '''
      From the below article, extract movie name, budget, revenue, studio name in JSON output format containing the following keys: 'revenue_actual', 'eps_actual', 'revenue_expected', 'eps_expected'

      Add units like Million or Billion
      e.g - $ 120 Million
      Only return the valid JSON . No preamble

      Artilce
      =========
      {article}

      '''

      pt = PromptTemplate.from_template(prompt)

      global llm

      chain = pt | llm

      response = chain.invoke({'article':article})

      parser = JsonOutputParser()

      try:
            res = parser.parse(response.content)
      except OutputParserException:
            raise OutputParserException("Content too big. Unable to parse jobs")
      
      return res



