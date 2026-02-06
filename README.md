# Auto_PPT_Gen
The system operates in three main stages: text analysis, slide planning, and PowerPoint generation.

First, the user submits a large block of text along with optional guidance such as tone or use case. This input is sent to a Large Language Model (LLM) using the user’s own API key. The LLM analyzes the content and converts it into a structured slide outline consisting of slide titles, bullet points, and optional speaker notes. The number of slides is dynamically determined based on the content length and user guidance.

Next, the user-uploaded PowerPoint template is parsed using the python-pptx library. The system extracts available slide layouts, text formatting styles, fonts, colors, and embedded images. Instead of generating new visuals, the application reuses existing images and layouts from the template to maintain visual and brand consistency.

Finally, the system programmatically generates a new PowerPoint presentation. Each slide is populated with AI-generated text while applying the same design elements from the uploaded template. The final .pptx file preserves the original look and feel of the template, ensuring a professional and polished presentation.

The result is a fully automated, template-aware PowerPoint generator that transforms raw text into a structured, visually consistent presentation with minimal user effort.
