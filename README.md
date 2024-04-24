# GrAIde

a quick and dirty python script to read in a rubric and essays and grade them using chatgpt
built for mac, maybe would run on linux? definitely won't run on windows.

## Usage

### Quickstart
1. put a folder with essays in .docx format to be graded inside this folder (the grading-script folder)
2. put the rubric in .docx format in this folder
3. put a prompt in .txt format in this folder
4. use the following command line prompt in the grading-script folder:
   grade <folder with essays> <rubric file> <prompt file>

So with the example folder and rubric file, the command would look like this:
   ./grade 23-11-15_video_game_essay 6th-rubric_2024_Zendle.docx prompt.txt

Note that spaces have meaning in the command line, so either rename folders/files with spaces in their names, or use "" around them.

The script will write to a text file of the same name as the .docx file for each essay. After the script has run, you can find these files in the essays folder.

### Using the script on folders/files in other locations
You don't need to move all you grading files into this folder to use the script! If you want to use the script on a folder that's not in the grading-script folder, you will need to get the full file path. On mac,
1. navigate to the file/folder in finder
2. right click on the file/folder
3. click "Get Info"
4. copy the path from the "Where" field in the dialog box that pops up
5. paste the path in the command line for the essay folder/rubric argument

### Running with python

The "grade" command is a pre-compiled executable. There's no room for customization besides the two command line arguments for file paths.
If you want to customize the script, you'll need to run it with python3.
Follow the exact same steps as the in Quickstart for steps 1-3, but replace step 4 with the following:
4. use the following command line prompt in the grading-script folder:
   python3 grade.py <folder with essays> <rubric file> <prompt file>

So with the example folder and rubric file, the command would look like this:
   python3 grade.py essays rubric.docx prompt.txt

If you get any errors, it's probably a dependency issue. See the Dependencies section below to install everything you need.

## Customization

The prompt.txt file contains a fairly simple prompt. You can edit this prompt in the existing .txt file, or make your own prompt files and run the script using them instead.

## Dependencies

If you want to edit the script and run using python3, you will need to install the dependencies.
This script needs python3, and the following packages:
sys
os
docx - SEE NOTE
openai

For mac, run the following commands from the command line:
brew install python3
brew install pip3
pip3 install sys
pip3 install os
pip3 install python-docx
pip3 install openai

NOTE: do not install docx with "pip3 install docx" - use python-docx instead. The docx version has weird python 2 dependencies.
