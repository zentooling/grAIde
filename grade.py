import sys
import os
import docx
from openai import OpenAI

prompt_customization = "Please provide a grade on the 1 to 4 scale for each rubric item, along with reasoning for the grade. After grading the essay, check it for plagiarism. If it was plagiarized, link the source if possible."

# Set your OpenAI API key
client = OpenAI() # OPENAI_API_KEY must be set in env


def extract_text_from_docx(doc):
    text = ""
    doc_iter = doc.iter_inner_content()

    doc_obj = next(doc_iter, None)
    while(doc_obj):
        if hasattr(doc_obj, 'text'):
            text += doc_obj.text + "\n"

        if hasattr(doc_obj, 'rows'):
            for row in doc_obj.rows:
                for cell in row.cells:
                    text += cell.text + "\n"

        doc_obj = next(doc_iter, None)
    
    return text.strip()

def generate_feedback(essay_text, rubric_text, prompt_text):
    # Prepare the prompt for OpenAI GPT
    prompt = f"{prompt_text}\n\nEssay:\n{essay_text}\n\nRubric:\n{rubric_text}\n\nFeedback:"

    # Call OpenAI's API for completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a teacher grading an essay."},
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content

def grade_essays(essays_folder, rubric_path, prompt_path):
    # Open the rubric
    rubric_doc = docx.Document(rubric_path)
    rubric_text = extract_text_from_docx(rubric_doc)

    # Open the prompt
    prompt_file = open(prompt_path, "r")
    prompt_text = prompt_file.read()

    # Iterate through each essay in the folder
    for filename in os.listdir(essays_folder):
        if filename.endswith(".docx"):
            essay_path = os.path.join(essays_folder, filename)

            # Open the essay
            essay_doc = docx.Document(essay_path)
            essay_text = extract_text_from_docx(essay_doc)

            # Generate feedback
            feedback = generate_feedback(essay_text, rubric_text, prompt_text)

            # Output the feedback to a text file with the same name as the essay document
            output_file = os.path.splitext(essay_path)[0] + "_feedback.txt"
            with open(output_file, 'w') as f:
                f.write(feedback)

            print(f"Graded {os.path.splitext(essay_path)[0]}\n")
    
    print("Done.\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python grade.py <essays_folder> <rubric_path> <prompt_path>")
        sys.exit(1)

    essays_folder = sys.argv[1]
    rubric_path = sys.argv[2]
    prompt_path = sys.argv[3]

    grade_essays(essays_folder, rubric_path, prompt_path)
