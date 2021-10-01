# Japanese-Law-Web-Scraping
A web scraping program I made for the Visual Novel OCR Project using the selenium library on Python.

# What is Visual Novel OCR? 
Visual Novel OCR is a project made with the purpose of translating Japanese text from visual novels or heavy-dialogue games into English. OCR stands for Optical Character Recognition, the act of extracting text from images. To find out about more details on the project, visit this link: https://visual-novel-ocr.sourceforge.io/

# What does this program do?
Since Visual Novel OCR needs a wide array of data sources to accurately translate Japanese to English, some people who joined the project, including myself, were assigned to collect data to be fed to the model used by the program. I chose to use a public dataset on a Japanese Law Translation site. The programs in this repository were made to automatically download, compile and list the documents found on the site. 

# Things to NOTE:
- I am not an expert at web-scraping, if you have any questions that only a professional can answer please don't ask me.
- The downloader program can only download documents with the default format, it won't work on public notices, untranslated laws and documents of other formats

# Instructions for Use:
* After downloading the 'downloader', 'compiler', 'variables' and 'lister' files, copy the path you downloaded the files into in the "path" variable in your variables files
* Run the downloader file, a translations directory will be created in the same directory your programs are in. This is where the downloaded files will be uploaded.
* Run the compiler file, the downloaded files will be paired into their english and japanese translations and copied inside folders with the titles as their names. Stop running the program once all the folders have been created. If one file is missing its pair, simply look for the original file and find the file that shares the same 14 characters it has.
* If you want to list all the document-translation pairs that have been successfully compiled, run the lister file. It will create a txt file and list the titles of all the compiled documents.
